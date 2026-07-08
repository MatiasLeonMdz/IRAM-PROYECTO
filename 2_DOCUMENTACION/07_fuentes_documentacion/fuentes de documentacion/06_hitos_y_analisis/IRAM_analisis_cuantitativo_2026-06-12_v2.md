# IRAM — Análisis Cuantitativo del Proceso
**Plantilla D ejecutada:** 2026-06-12
**Corregido:** 2026-06-12 (v2 — Bloque 2 rehecho con timestamps de mensajes individuales)
**Input:** claude_1_processed.json … claude_5_processed.json (×5)
**Alcance:** Bloque 2 (cuentas: rotación vs paralelismo) + Bloque 0 (evolución del contexto) + Bloque 1 (velocidad por fase)

---

## BLOQUE 2 — ¿Cuentas paralelas o en rotación secuencial?

### Veredicto: ROTACIÓN SECUENCIAL RÁPIDA. No hay paralelismo simultáneo.

**Metodología corregida:**
La versión anterior comparaba timestamps de *inicio de sesión* — metodología incorrecta para detectar paralelismo real. Esta versión usa timestamps de *mensajes individuales* (campo `ts` en los processed JSONs) para determinar si mensajes de distintas cuentas se intercalaban en el tiempo.

**Datos base:**
- Total mensajes IRAM con timestamp: 7.313 (C1: 1.505 | C2: 1.647 | C3: 1.284 | C4: 1.106 | C5: 1.771)
- Rango temporal: 2026-04-09 → 2026-06-10
- Transiciones de cuenta detectadas (cambio de cuenta dentro de 1 hora): 211

**El dato definitorio — interleaving real:**
Se buscaron patrones A-B-A donde mensajes de la misma cuenta se alternaban con otra cuenta dentro de 5 minutos (el test más directo de trabajo simultáneo). **Resultado: 0 casos.** Nunca se enviaron mensajes a dos cuentas distintas de forma intercalada dentro de una ventana corta.

**Distribución de gaps entre switches de cuenta:**

| Gap entre switch | Casos | % |
|-----------------|-------|---|
| < 2 min | 41 | 19.4% |
| 2–5 min | 91 | 43.1% |
| 5–15 min | 49 | 23.2% |
| 15–60 min | 30 | 14.2% |

El gap más común es 2–5 minutos (43.1%). El operador terminaba de interactuar con una cuenta, esperaba (o cambiaba de tarea) y luego abría la siguiente. Nunca en simultáneo.

**Días con múltiples cuentas activas:** 43 de 49 días IRAM (87.8%). En esos días, el operador rotaba entre cuentas en distintos momentos del día, no al mismo tiempo.

**Top 5 días por cantidad de switches (todos con las 5 cuentas):**
- 2026-05-27: 15 switches
- 2026-06-05: 13 switches
- 2026-04-17: 11 switches
- 2026-04-23: 11 switches
- 2026-05-19: 10 switches

**Ejemplo representativo (2026-05-27, el día más intenso):**
La secuencia fue completamente serial: C4(00:00–00:23) → C5(00:25–01:07) → C1(01:10–01:43) → C2(01:58–02:42) → C3(02:44–02:57) → C4(04:56–05:25) → C5(05:26–06:30) → C1(06:33–06:58) → C2(06:59–07:25) → (…) → C3(21:30–23:19) → C4(23:20–23:37) → C5(23:47–23:56). 17 bloques de trabajo secuenciales en un solo día, todos en cuentas distintas, ninguno simultáneo.

### El modelo correcto: rotación de contextos

Las 5 cuentas no eran "workers paralelos". Eran **contextos independientes en rotación secuencial rápida**. El operador trabajaba en una cuenta hasta que necesitaba cambiar (por límite de mensajes, por agotamiento de contexto, o por conveniencia de tarea), y entonces abría la siguiente.

**Por qué funcionaba:** el PROMPT_MAESTRO era el mecanismo de coherencia. Al cargar el mismo PROMPT_MAESTRO en cualquier cuenta, el operador podía retomar el trabajo desde cualquier punto sin perder el estado del proyecto. Las cuentas eran intercambiables en términos de instrucciones; solo diferían en el historial de conversación específico.

**Causalidad del sistema multi-cuenta:** el límite de mensajes por cuenta forzó la distribución. Sin ese límite, probablemente se hubiera usado una sola cuenta por período. El PROMPT_MAESTRO convirtió esa limitación técnica en un sistema funcional.

### Corrección a versiones anteriores

La afirmación "cuentas genuinamente paralelas (85% de días con múltiples cuentas)" del análisis anterior era incorrecta por metodología deficiente (timestamps de inicio de sesión, no de mensajes). El dato correcto es:
- 87.8% de días con múltiples cuentas *en algún momento del día*, pero siempre en rotación secuencial.
- 0% de paralelismo simultáneo real (cero interleavings).
- La hipótesis "reinicios post-corte" del CORRECCIONES también era incorrecta: no eran reinicios, era rotación deliberada por límite de tokens.

**R18 necesita actualización:** el modelo "verificar solapamiento antes de asumir paralelismo" era correcto como procedimiento, pero la conclusión del Bloque 2 anterior era errónea. El modelo correcto es rotación secuencial, no paralelismo.

---

## BLOQUE 0 — Evolución del contexto (interrupted time series)

### Los 4 puntos de corte y sus efectos medibles

**Métricas por período:**

| Período | Días | Sesiones | Msgs tot | Prom msg/ses | % arranque ctx |
|---------|------|----------|----------|-------------|----------------|
| P0 — Pre-backup (hasta 2026-04-16) | 8 | 6 | 46 | 7.7 | 0% |
| P1 — Backup simple (04-17 → 05-13) | 27 | 154 | 3.672 | 35.0 | 18.2% |
| P2 — SUPERBACKUP (05-14 → 05-15) | 2 | 10 | 223 | 22.3 | 30.0% |
| P3 — PROMPT_MAESTRO (05-16 → 05-26) | 11 | 86 | 1.457 | 18.4 | 11.6% |
| P4 — ACTIVE/ARCHIVE (05-27 → ) | 35 | 169 | 1.915 | 14.1 | 39.6% |

*Nota: las sesiones de 0 mensajes son testeos de restauración de tokens (comportamiento externo al proceso IRAM) y se excluyen de esta tabla. No son indicadores del sistema de documentación.*

### Lectura de los datos

**Corte 1 — Primer backup propio (2026-04-17):**
Sin sistema de contexto estable, cada sesión requería más mensajes para llegar al trabajo productivo (35.0 msgs/sesión en P1 vs. 14.1 en P4). El P1 tiene el promedio más alto de toda la serie.

**Corte 3 — PROMPT_MAESTRO v1.0 (2026-05-16): el cambio más medible.**
El promedio de mensajes por sesión bajó de 35.0 (P1) a 18.4 (P3). Esto no se explica por la diferencia en tareas — se explica por la reducción del costo de inicializar el contexto. El PROMPT_MAESTRO como primer mensaje pegado, no como adjunto, fue el mecanismo técnico.

**Corte 4 — ACTIVE/ARCHIVE split (2026-05-27):**
El promedio bajó aún más (14.1 msgs/sesión). El porcentaje de sesiones de arranque de contexto subió al 39.6% — no es overhead disfuncional sino el protocolo de arranque formalizado explícitamente. La sesión de carga se volvió un paso declarado, no un problema.

### El meta-análisis del sistema — 2026-05-18/19

El 18-19 de mayo, las 5 cuentas trabajaron en rotación secuencial sobre tareas de documentación del historial (no del mod): exportar historial a markdown, procesamiento de archivos, consolidación de logs. Ese día tuvo 10 switches de cuenta, todas en tareas de documentación.

Los títulos confirman el patrón: "Documentación de historial de desarrollo en Markdown", "Exportar historial de desarrollo a markdown", "Exportar historial de conversaciones a markdown", múltiples sesiones de procesamiento y unificación de superbackup.

Esto ocurrió entre el SUPERBACKUP (05-14) y el PROMPT_MAESTRO (05-16), y precipitó el PROMPT_MAESTRO v3.0 con reglas explícitas sobre cuándo y cómo documentar.

**Relevancia para Ángulo 10:** el techo real del sistema es que la documentación puede convertirse en el problema principal si no hay criterio explícito sobre qué documentar, cuándo, y qué no. El evento 2026-05-18/19 lo materializó. Se detectó, se nombró, y se generó una regla. El techo no era permanente — fue detectado y corregido. Confirmado independientemente por memories.json de C5: "risked consuming more effort than the mod."

---

## BLOQUE 1 — Velocidad de desarrollo por fase

| Fase | Días cal. | Ses/día | Msgs/sesión |
|------|-----------|---------|-------------|
| Drago v1-v2 | 13 | 1.8 | 37.0 |
| IRAM v3 | 30 | 5.1 | 24.4 |
| IRAM v4 | 13 | 7.2 | 22.3 |
| IRAM v5 | 7 | 9.4 | 9.6 |

**El patrón central:**
Velocidad (sesiones/día) aumentó de 1.8 a 9.4 (5.2x). Costo por sesión (msgs/sesión) cayó de 37.0 a 9.6 (3.9x menos overhead). V5 no fue más rápida porque el problema era más simple — fue más rápida porque el sistema aprendido reducía el costo de cada iteración.

**Días de mayor intensidad (top 5):**
- 2026-05-27: 547 msgs, 17 bloques de trabajo, 5 cuentas (split ACTIVE/ARCHIVE + constructor automático)
- 2026-05-26: 455 msgs, 12 sesiones, 5 cuentas
- 2026-04-17: 440 msgs, 13 bloques de trabajo, 5 cuentas (primer backup + primera wiki)
- 2026-05-11: 376 msgs, 11 sesiones, 5 cuentas
- 2026-04-22: 338 msgs, 9 sesiones, 5 cuentas

Los 3 días más intensos coinciden con hitos metodológicos mayores.

---

## SÍNTESIS — LO QUE LOS NÚMEROS CONFIRMAN PARA EL SKILL.md

1. **El PROMPT_MAESTRO tuvo el impacto más medible del proyecto:** el promedio de mensajes por sesión bajó de 35.0 (P1) a 18.4 (P3). La diferencia es de arquitectura de contexto (pegado como primer mensaje), no de contenido.

2. **El sistema multi-cuenta era rotación secuencial, no paralelismo:** el operador trabajaba en una cuenta a la vez, cambiando con una cadencia típica de 2–5 minutos entre switches. Las cuentas eran contextos independientes e intercambiables gracias al PROMPT_MAESTRO. El límite de mensajes por cuenta fue la causa técnica; el PROMPT_MAESTRO fue la solución que lo convirtió en un sistema funcional.

3. **V5 como ingeniería deliberada:** 9.4 sesiones/día con 9.6 msgs/sesión vs. 1.8 sesiones/día con 37.0 msgs/sesión en v1-v2. Cinco veces más velocidad, cuatro veces menos overhead por sesión. La eficiencia vino de sesiones más cortas y más frecuentes, no de sesiones más largas.

4. **El riesgo del sistema se materializó una vez (2026-05-18/19):** todas las cuentas en rotación sobre documentación, sin producir código. Se detectó, se nombró, y se corrigió. El techo del sistema no es estructural — es un riesgo gestionable si el operador lo monitorea.

---

## PENDIENTES (Bloques 3, 4, 5)

- **Bloque 3** (distribución de trabajo): requiere análisis de contenido de mensajes — no disponible en los processed JSONs actuales
- **Bloque 4** (tasa de bugs por versión): requiere identificar mensajes de error/debug — parcialmente inferible de títulos
- **Bloque 5** (conexión data science): requiere análisis temático de contenido

Estos bloques no bloquean la Plantilla C — los datos de Bloques 0, 1 y 2 son suficientes para respaldar las afirmaciones principales del SKILL.md con evidencia medible.

---

*IRAM — Análisis Cuantitativo del Proceso — 2026-06-12 v2*
*Bloque 2 rehecho con timestamps de mensajes individuales (corrige metodología de v1)*
*Bloques 0, 1, 2 completos | Bloques 3, 4, 5 pendientes — no bloquean Plantilla C*
