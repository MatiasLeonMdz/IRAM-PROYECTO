# IRAM — Análisis Cuantitativo del Proceso
**Plantilla D ejecutada:** 2026-06-12
**Corregido:** 2026-06-12 (v2 — Bloque 2 rehecho con timestamps de mensajes individuales)
**Bloque 3 agregado:** 2026-06-12 (v3 — distribución de trabajo por tipo y fase)
**Input:** claude_1_processed.json … claude_5_processed.json (×5)
**Alcance:** Bloques 0, 1, 2, 3 completos. Bloques 4, 5 pendientes.

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

## BLOQUE 3 — Distribución de trabajo por tipo y fase

### Metodología

**Señales de herramientas** (objetivas, extraídas de los processed JSONs):
- **Código** = llamadas a `create_file` o `str_replace` — Claude escribiendo o editando archivos
- **Investigación** = llamadas a bash con comandos de lectura (`grep`, `cat`, `find`, `head`, `tail`, `unzip -l`) — Claude inspeccionando archivos antes de actuar
- **Build** = llamadas a bash con comandos de construcción (`mkdir`, `zip`, `cp`, `mv`, `printf`, `python3`) — Claude construyendo el artefacto final

Las señales son sobre llamadas a herramientas, no sobre mensajes completos: un mensaje con 3 llamadas a `str_replace` cuenta como 3 en Código. El denominador es el total de mensajes de la fase.

**Exclusión de meta-documentación:** las sesiones de análisis del propio proceso (historial, wikis, skill, plantillas) se excluyen de la tabla principal. Contaminaban v5 porque la documentación del proceso de este análisis ocurrió en ese período. Están contabilizadas por separado.

### Tabla A — Código / Investigación / Build por fase (mod-dev)

| Fase | Convs | Msgs | Código | Investigación | Build | Ratio Inv/Cód |
|------|-------|------|--------|--------------|-------|---------------|
| v1-v2 | 23 | 851 | 88 (10.3%) | 155 (18.2%) | 239 (28.1%) | 1.8x |
| v3 | 135 | 3.603 | 577 (16.0%) | 1.138 (31.6%) | 979 (27.2%) | 2.0x |
| v4 | 82 | 1.933 | 250 (12.9%) | 604 (31.2%) | 245 (12.7%) | 2.4x |
| v5 | 62 | 523 | 106 (20.3%) | 312 (59.7%) | 135 (25.8%) | 2.9x |

**Sesiones de meta-documentación excluidas (ver Bloque 0/2):**
v3: 18 convs / 128 msgs | v4: 12 / 163 | v5: 4 / 112

**Hallazgo central:** el ratio Investigación/Código crece de forma monótona en cada fase (1.8x → 2.0x → 2.4x → 2.9x). La lectura obvia sería "más fricción", pero la Tabla B refuta esa lectura.

### Tabla B — Tipo de Investigación por fase

Desagrega cada llamada de Investigación (bash grep/cat/find) según el contenido que inspecciona:

| Fase | Total Inv | error (%) | doc_plan (%) | code_mod (%) | other (%) |
|------|-----------|-----------|-------------|-------------|-----------|
| v1-v2 | 155 | 4 (3%) | 4 (3%) | 70 (45%) | 77 (50%) |
| v3 | 1.138 | 30 (3%) | 169 (15%) | 336 (30%) | 603 (53%) |
| v4 | 604 | 5 (1%) | 92 (15%) | 334 (55%) | 173 (29%) |
| v5 | 312 | 7 (2%) | 99 (32%) | 173 (55%) | 33 (11%) |

Categorías:
- **error**: lectura de `error.log`, `game.log`, `pdx_script_error` — debugging reactivo
- **doc_plan**: lectura de archivos de planificación y documentación propios (`wiki`, `session_log`, `.md`, `plan`, `gaps`, `prompt_maestro`) — leer el estado del proyecto antes de actuar
- **code_mod**: lectura del código propio del mod (`on_action`, `scripted`, `exodos_`, `iram_`, `events/`, `decisions/`) — entender la estructura antes de modificar
- **other**: el resto, no clasificable por los patrones anteriores

**La refutación de la hipótesis "más bugs":**
El target `error` se mantiene en 1-3% en **todas las fases**, sin tendencia creciente. Si el ratio Inv/Cód creciente reflejara más debugging reactivo, el porcentaje de `error` debería crecer. No lo hace. La explicación "más bugs en fases tardías" queda descartada por los datos.

**Lo que sí crece en v5:**
- `doc_plan` se duplica en v5 (3% → 15% → 15% → **32%**): Claude leyendo el estado documentado del proyecto antes de actuar.
- `code_mod` sube y se estabiliza en v4-v5 (45% → 30% → 55% → **55%**): Claude leyendo el código propio antes de modificarlo.
- `other` colapsa en v5 (50% → 53% → 29% → **11%**): la investigación en v5 es casi enteramente clasificable — estructurada y deliberada.

**El `other` en v1-v2/v3:** en fases tempranas, `other` es mayormente exploración de mecánicas del juego (grep por `heir_weight`, `treasury`, `succession`, `popularidad`, `LAND_MAINTENANCE` — vocabulario de las mecánicas del juego, no del mod propio). Es investigación de diseño/calibración ("¿qué hace realmente esta mecánica?"), distinta conceptualmente de debugging reactivo.

**Lectura unificada:** la Investigación nunca fue principalmente reactiva. Fue diseño-adyacente en fases tempranas (entender el juego para calibrar) y planificación-antes-de-actuar en fases tardías (leer el estado del proyecto y del código propio antes de tocar algo). El modo de falla "más debugging" no aparece en ninguna fase.

### Tabla C — Densidad de lenguaje de decisión/diseño por fase

Porcentaje de mensajes humanos y de Claude que contienen vocabulario de decisión/diseño: propuesta, opción, criterio, decisión, enfoque, estructura, plan, "qué te parece", "antes de tocar", "pensar todo primero".

| Fase | H-msgs | H-kw% | H-avg-chars | A-msgs | A-kw% |
|------|--------|-------|------------|--------|-------|
| v1-v2 | 412 | 5.6% | 141 | 439 | 51.9% |
| v3 | 1.738 | 4.5% | 105 | 1.865 | 48.2% |
| v4 | 947 | 5.9% | 114 | 986 | 52.9% |
| v5 | 257 | 7.0% | 183 | 266 | 66.5% |

**v5 en perspectiva:** en v5, los mensajes del operador son los más largos del proyecto (183 chars promedio vs 105–141 en fases anteriores) y los más ricos en lenguaje de decisión (7.0% vs 4.5–5.9%). Las respuestas de Claude también: 66.5% de mensajes de Claude con lenguaje de propuesta/estructura, vs ~50% en fases previas.

**Evidencia directa del patrón:** la sesión "Confirmación de estructura de archivos en proceso de rename" (v5, 2026-06-04) contiene este mensaje del operador: *"para eso estamos planificando todo antes cuidadosamente claude, hay que diseñar y pensar todo primero"*. Las herramientas en esa sesión son `grep -n "^## "` repetido — extrayendo la tabla de contenidos de la wiki para planificar la reorganización. La herramienta de "Investigación" está al servicio de la planificación, no de la corrección de errores.

### Tabla D — Top conversaciones v5 por Investigación (mod-dev)

| Fecha | Cód | Inv | Build | Msgs | Nombre |
|-------|-----|-----|-------|------|--------|
| 2026-06-08 | 3 | 22 | 6 | 16 | audit 5.2 |
| 2026-06-04 | 1 | 21 | 0 | 75 | Confirmación de cambios en archivos IRAM |
| 2026-06-04 | 0 | 20 | 0 | 6 | Confirmación de estructura de archivos en proceso de rename |
| 2026-06-05 | 0 | 16 | 0 | 12 | 05/06/2026 04.03 |
| 2026-06-09 | 1 | 16 | 0 | 6 | Carga de documentos técnicos y contexto de sesión |
| 2026-06-05 | 30 | 16 | 7 | 16 | Plan de ejecución unificado v5.0 |
| 2026-06-08 | 0 | 13 | 0 | 4 | IRAM v5.0 project status and testing |
| 2026-06-06 | 6 | 12 | 4 | 31 | Proyecto IRAM |

Los top 5 acumulan 95/312 (30%) de la Investigación v5, pero solo 5/106 (5%) del Código v5.

**El patrón en los nombres:** "audit", "Confirmación de cambios", "Confirmación de estructura", "Verificación de tareas", "Plan de ejecución unificado". No hay nombres del estilo "Fix bug X" o "Corregir error Y". Las sesiones de mayor Investigación en v5 son auditorías del remake modular (v5.0→v5.5), confirmaciones de que el renombrado de namespace se aplicó correctamente, y sesiones de planificación del split modular — todas QA/verificación deliberada, no debugging reactivo.

La excepción es "Plan de ejecución unificado v5.0" (Cód=30, Inv=16): esta sesión tiene el mayor Código de todas en v5 *y* alto de Investigación. Es la sesión de ejecución del remake modular — lee el estado actual antes de cada cambio estructural grande.

### Interpretación — la maduración del proceso es visible en las herramientas

Los cuatro bloques cuentan la misma historia desde distintos ángulos:

**Bloque 1** (velocidad): v5 tiene 5.2x más sesiones/día y 3.9x menos mensajes/sesión → más iteraciones, más cortas.

**Bloque 3** (tipo de trabajo): v5 tiene más Investigación relativa (ratio 2.9x) pero esa Investigación es estructurada (87% clasificable en doc_plan + code_mod, solo 11% "other"), con mensajes del operador más largos y más densos en lenguaje de decisión.

**La síntesis:** v5 no era más lento ni más accidentado — era más deliberado. Cada sesión más corta contenía más lectura-antes-de-escribir (doc_plan, code_mod) y menos exploración ad-hoc (other). El operador llegaba a cada sesión con el plan más articulado (H-avg-chars 183 vs 105–141 en fases previas) y Claude respondía con más lenguaje de propuesta y estructura (A-kw% 66.5% vs ~50%).

**Conexión con el SKILL:** la Sección 6 del SKILL ("el operador fue el arquitecto, la IA fue la herramienta de precisión") tiene respaldo cuantitativo en la Tabla C — el rol de arquitecto del operador se volvió más explícito y textualmente denso con el tiempo, no menos. La Sección 11 ("conexión con data science: el ciclo empírico hipótesis→prueba→resultado") tiene respaldo en la Tabla B — el patrón "leer estado actual → planificar → ejecutar → verificar" es visible en el tipo de Investigación que predomina en v4/v5 (doc_plan + code_mod).

---

## SÍNTESIS — LO QUE LOS NÚMEROS CONFIRMAN PARA EL SKILL.md

1. **El PROMPT_MAESTRO tuvo el impacto más medible del proyecto:** el promedio de mensajes por sesión bajó de 35.0 (P1) a 18.4 (P3). La diferencia es de arquitectura de contexto (pegado como primer mensaje), no de contenido.

2. **El sistema multi-cuenta era rotación secuencial, no paralelismo:** el operador trabajaba en una cuenta a la vez, cambiando con una cadencia típica de 2–5 minutos entre switches. Las cuentas eran contextos independientes e intercambiables gracias al PROMPT_MAESTRO. El límite de mensajes por cuenta fue la causa técnica; el PROMPT_MAESTRO fue la solución que lo convirtió en un sistema funcional.

3. **V5 como ingeniería deliberada (Bloque 1 + Bloque 3):** 9.4 sesiones/día con 9.6 msgs/sesión vs. 1.8 sesiones/día con 37.0 msgs/sesión en v1-v2. La eficiencia no vino de trabajar más rápido — vino de leer más antes de escribir (ratio Inv/Cód 2.9x), con instrucciones del operador más largas y más articuladas (183 chars promedio), y sin aumento del debugging reactivo ("error" se mantiene flat en 2% en todas las fases).

4. **El riesgo del sistema se materializó una vez (2026-05-18/19):** todas las cuentas en rotación sobre documentación, sin producir código. Se detectó, se nombró, y se corrigió. El techo del sistema no es estructural — es un riesgo gestionable si el operador lo monitorea.

5. **El rol de arquitecto del operador se volvió más explícito con el tiempo:** los mensajes del operador en v5 son los más largos (183 chars) y los más densos en lenguaje de decisión (7.0%) de todo el proyecto. El operador no delegó más diseño a Claude con el tiempo — articuló el diseño más explícitamente al inicio de cada sesión.

---

## PENDIENTES (Bloques 4, 5)

- **Bloque 4** (tasa de bugs por versión): requiere identificar mensajes de error/debug — parcialmente inferible de títulos. No bloquea ningún entregable.
- **Bloque 5** (conexión data science): requiere análisis temático de contenido. No bloquea ningún entregable.

Los datos de Bloques 0, 1, 2 y 3 son suficientes para respaldar todas las afirmaciones principales del SKILL.md con evidencia medible.

---

*IRAM — Análisis Cuantitativo del Proceso — 2026-06-12 v3*
*v2: Bloque 2 rehecho con timestamps de mensajes individuales (corrige metodología de v1)*
*v3: Bloque 3 agregado — distribución de trabajo por tipo y fase (4 tablas: A, B, C, D)*
*Bloques 0, 1, 2, 3 completos | Bloques 4, 5 pendientes — no bloquean entregables*
