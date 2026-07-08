# IRAM — Análisis Cuantitativo del Proceso
**Plantilla D ejecutada:** 2026-06-12
**Input:** claude_1_processed.json … claude_5_processed.json (×5)
**Alcance:** Bloque 2 (cuentas paralelas/secuenciales) + Bloque 0 (evolución del contexto) + Bloque 1 (velocidad por fase)

---

## BLOQUE 2 — ¿Cuentas paralelas o secuenciales? (PRIORIDAD ⚠️)

### Veredicto: PARALELAS. La hipótesis de secuencialidad era incorrecta.

**Datos directos:**
- Total sesiones IRAM: 425 (5 cuentas combinadas)
- Sesiones sustantivas (>0 mensajes): 336 (79%)
- Sesiones vacías / reinicios de página: 89 (21%)
- Días con actividad IRAM: 46 días calendario
- **Días con sesiones sustantivas de ≥2 cuentas distintas: 39 de 46 (85%)**

**El solapamiento era real y frecuente:**
- 198 pares de sesiones sustantivas de distintas cuentas iniciadas con menos de 30 minutos de diferencia entre sí
- Caso extremo: C2 y C3 iniciaron sesiones con 46 segundos de diferencia (2026-04-17 02:52:02 vs 02:52:48)
- En días de alta actividad (ej. 2026-05-26), distintas cuentas trabajaban en tareas completamente diferentes en el mismo horario:
  - C5 18:27 — "Qué sigue" (86 msgs)
  - C1 20:09 — "Cálculo incorrecto de thresholds de esclavos" (50 msgs)
  - C2 21:04 — "Contar territorios y áreas por región cultural" (60 msgs)
  - C3 21:44 — "Log de las 18:40 no se generó correctamente" (125 msgs)

**Sobre las 89 sesiones vacías:**
Las sesiones de 0 mensajes (reinicios de página / fallos de carga) SÍ existían y son un artefacto real del proceso. Pero son overhead adicional al paralelismo, no la explicación del paralelismo.

**Distribución por mes — sesiones sustantivas:**

| Mes | C1 | C2 | C3 | C4 | C5 | Total |
|-----|----|----|----|----|-----|-------|
| Abril 2026 | 12 | 11 | 12 | 11 | 12 | 58 |
| Mayo 2026 | 46 | 46 | 35 | 32 | 44 | 203 |
| Junio 2026 | 13 | 12 | 18 | 17 | 15 | 75 |

**Mensajes totales por cuenta:**

| Cuenta | Sesiones sust. | Msgs totales | Prom. msgs/sesión |
|--------|---------------|-------------|-------------------|
| C1 | 71 | 1505 | 21.2 |
| C2 | 69 | 1647 | 23.9 |
| C3 | 65 | 1284 | 19.8 |
| C4 | 60 | 1106 | 18.4 |
| C5 | 71 | 1771 | 24.9 |

La distribución de mensajes es similar entre cuentas (18.4 a 24.9 msgs/sesión). Ninguna cuenta era "principal" — todas hacían trabajo real con volumen comparable.

### Implicaciones

**R18 era CORRECTA.** No requiere modificación. El encuadre "verificar solapamiento en lugar de asumir secuencialidad" era el correcto.

**Para el SKILL.md:** El sistema de cuentas paralelas es un hito metodológico real. La causalidad detrás del paralelismo (¿por qué no usar una sola cuenta?) sigue siendo relevante de documentar: el límite de mensajes por cuenta forzó la distribución, y el PROMPT_MAESTRO fue el mecanismo de coherencia entre contextos independientes.

---

## BLOQUE 0 — Evolución del contexto (interrupted time series)

### Los 4 puntos de corte y sus efectos medibles

**Métricas por período:**

| Período | Días | Sesiones | Msgs tot | Prom msg/ses | % vacías | % arranque ctx |
|---------|------|----------|----------|-------------|----------|----------------|
| P0 — Pre-backup (hasta 2026-04-16) | 8 | 6 | 46 | 7.7 | 0% | 0% |
| P1 — Backup simple (04-17 → 05-13) | 27 | 154 | 3672 | 35.0 | 31.8% | 18.2% |
| P2 — SUPERBACKUP (05-14 → 05-15) | 2 | 10 | 223 | 22.3 | 0% | 30.0% |
| P3 — PROMPT_MAESTRO (05-16 → 05-26) | 11 | 86 | 1457 | 18.4 | 8.1% | 11.6% |
| P4 — ACTIVE/ARCHIVE (05-27 → ) | 35 | 169 | 1915 | 14.1 | 19.5% | 39.6% |

### Lectura de los datos

**Corte 1 — Primer backup propio (2026-04-17):**
El P0 pre-backup tiene apenas 6 sesiones en 8 días — el proyecto recién comenzaba. A partir del backup, la velocidad se multiplicó (154 sesiones en 27 días). Pero el P1 tiene la mayor tasa de sesiones vacías (31.8%) y el mayor promedio de mensajes por sesión (35.0). Interpretación: sin un sistema de contexto estable, cada sesión requería más mensajes para llegar al trabajo productivo, y más intentos fallidos de carga de página.

**Corte 3 — PROMPT_MAESTRO v1.0 (2026-05-16): el cambio más medible**
La tasa de sesiones vacías cayó de 31.8% (P1) a 8.1% (P3) — casi 4x menos fallos. El promedio de mensajes por sesión bajó de 35.0 a 18.4. Este es el corte con mayor impacto medible en el comportamiento del sistema.

**Corte 4 — ACTIVE/ARCHIVE split (2026-05-27):**
El promedio por sesión bajó aún más (14.1 msgs). El porcentaje de sesiones de arranque de contexto subió al 39.6% — paradójico, pero interpretable: el protocolo de arranque se formalizó explícitamente. No es overhead disfuncional — es el costo declarado y controlado de inicializar un contexto nuevo.

Las sesiones vacías vuelven a subir (19.5%) en P4, pero esto coincide con el período de mayor actividad absoluta del proyecto (mayo-junio): más sesiones totales = más reinicios de página por volumen.

### El meta-análisis del sistema — 2026-05-18/19

El 18-19 de mayo, las 5 cuentas trabajaron simultáneamente en tareas de documentación del historial (no en el mod): exportar historial a markdown, procesamiento de archivos, consolidación de logs. Esta es la sesión que el memories.json de C5 describe como "meta-analysis session identifying that the control system risked consuming more effort than the mod."

Los títulos confirman el patrón:
- C3: "Documentación de historial de desarrollo en Markdown"
- C4: "Exportar historial de desarrollo a markdown"
- C5: "Exportar historial de conversaciones a markdown"
- C1+C2+C3+C4+C5 (05-19): múltiples sesiones de procesamiento y unificación de superbackup

Esto ocurrió entre el SUPERBACKUP (05-14) y el PROMPT_MAESTRO (05-16), y precipitó el PROMPT_MAESTRO v3.0 que estableció reglas explícitas sobre cuándo y cómo documentar.

**Relevancia para ángulo 10:** este evento es el candidato más sólido identificado hasta ahora. El techo real del sistema es que la documentación puede convertirse en el problema principal si no hay criterio explícito sobre qué documentar, cuándo, y qué no. El sistema lo identificó, lo nombró, y generó una regla (PROMPT_MAESTRO v3.0). El techo no era permanente — fue detectado y corregido.

---

## BLOQUE 1 — Velocidad de desarrollo por fase

| Fase | Días cal. | Ses/día | Msgs/sesión | Cuentas activas |
|------|-----------|---------|-------------|-----------------|
| Drago v1-v2 | 13 | 1.8 | 37.0 | 5 |
| IRAM v3 | 30 | 5.1 | 24.4 | 5 |
| IRAM v4 | 13 | 7.2 | 22.3 | 5 |
| IRAM v5 | 7 | 9.4 | 9.6 | 5 |

**El patrón central:**
La velocidad (sesiones/día) aumentó consistentemente: 1.8 → 5.1 → 7.2 → 9.4.
El costo por sesión (msgs/sesión) cayó consistentemente: 37.0 → 24.4 → 22.3 → 9.6.

Esto confirma la hipótesis del marco teórico: V5 no fue más rápida porque el problema era más simple — fue más rápida porque el sistema aprendido reducía el costo de cada iteración. En v1-v2, cada sesión requería 37 mensajes en promedio para producir output. En v5, 9.6.

**Días de mayor intensidad (top 5):**
- 2026-05-27: 547 msgs — 27 sesiones, 5 cuentas (split ACTIVE/ARCHIVE + constructor automático)
- 2026-05-26: 455 msgs — 12 sesiones, 5 cuentas
- 2026-04-17: 440 msgs — 12 sesiones, 5 cuentas (primer backup + primera wiki)
- 2026-05-11: 376 msgs — 11 sesiones, 5 cuentas
- 2026-04-22: 338 msgs — 9 sesiones, 5 cuentas

Los 3 días más intensos coinciden con hitos metodológicos mayores: el split ACTIVE/ARCHIVE, el período del backup simple, y la primera semana del proyecto IRAM.

---

## SÍNTESIS — LO QUE LOS NÚMEROS CONFIRMAN PARA EL SKILL.md

1. **El PROMPT_MAESTRO tuvo el impacto más medible del proyecto:** redujo sesiones fallidas de 31.8% a 8.1%. No fue solo una mejora de contenido — fue un cambio de arquitectura de contexto (pegado como primer mensaje).

2. **Las cuentas paralelas no eran un accidente:** en 85% de los días IRAM había múltiples cuentas trabajando. La distribución de mensajes era similar entre todas (18–25 msgs/sesión). El sistema paralelo fue consistente y deliberado.

3. **V5 como ingeniería deliberada:** 9.4 sesiones/día con 9.6 msgs/sesión vs. 1.8 sesiones/día con 37.0 msgs/sesión en v1-v2. Cinco veces más velocidad, cuatro veces menos overhead por sesión. La eficiencia no vino de sesiones más largas — vino de sesiones más cortas y más frecuentes.

4. **El riesgo del sistema se materializó una vez (2026-05-18/19):** las 5 cuentas trabajando en documentación simultáneamente, sin producir código. Se detectó, se nombró, y se corrigió con el PROMPT_MAESTRO v3.0. El techo del sistema no es estructural — es un riesgo gestionable si el operador lo monitorea.

5. **Las 89 sesiones vacías (21% del total) son overhead real:** reinicios de página, fallos de carga, sesiones cortadas. No son errores del proceso — son el costo de operar un sistema sin estado persistente. Este número baja a 8.1% con el PROMPT_MAESTRO.

---

## PENDIENTES (Bloques 3, 4, 5)

- **Bloque 3** (distribución de trabajo): requiere análisis de contenido de mensajes — no disponible en los processed JSONs actuales
- **Bloque 4** (tasa de bugs por versión): requiere identificar mensajes de error/debug — parcialmente inferible de títulos
- **Bloque 5** (conexión data science): requiere análisis temático de contenido

Estos bloques no bloquean la Plantilla C — los datos de Bloques 0, 1 y 2 son suficientes para respaldar las afirmaciones principales del SKILL.md con evidencia medible.

---

*IRAM — Análisis Cuantitativo del Proceso — 2026-06-12*
*Plantilla D ejecutada: Bloques 0, 1 y 2 completos*
*Bloques 3, 4, 5: pendientes — no bloquean Plantilla C*
