# 0_REPLANTEOS_Y_DECISIONES/

## Qué contiene

La serie completa `SESSION_LOG_REPLANTEO_*` (19/06 a 05/07, 20 archivos) — el
registro cronológico de las sesiones donde se redefinió **el encuadre del
proyecto entero**: qué piezas lo componen, cómo se relacionan entre sí, qué
tema central tiene, y las reglas de trabajo (DR = "Decisión Registrada") que
rigen desde entonces.

## Por qué está separada de `1_MOD/`, `2_DOCUMENTACION/` y `3_ANALISIS/`

No es "documentación del mod", ni "análisis A/B", ni "desarrollo técnico" —
es meta: el proceso que decidió *qué es* cada una de esas tres piezas y cómo
encajan. Varias sesiones de esta serie tocan las tres a la vez en el mismo
archivo (por ejemplo, la sesión que define "3 piezas, no 4" también fija
nomenclatura del mod y criterio de cierre del análisis). Partir la serie por
sección fragmentaría decisiones que se tomaron como una unidad. Ver
`FUENTE_DE_VERDAD` para el detalle de por qué se llegó a esta estructura.

## Subcarpetas

- **`01_logs_replanteo/`** — 19/06 al 04/07 (15 archivos). El grueso histórico
  de la serie: fundacionales (DR-01 a DR-09), metodología y Framework B,
  estructura de 3 piezas (DR-25), prueba de fuga de memoria (DR-28 a DR-34),
  auditoría de continuidad entre logs (DR-35 a DR-38).
- **`02_logs_replanteo_cola/`** — 04/07 tarde a 05/07 (5 archivos). Continuación
  directa de `01_logs_replanteo/`, misma serie. Contiene **DR-45 a DR-54**,
  el bloqueante vigente del Objetivo 3 (Análisis A/B), por eso el material
  más citado y más reciente de la carpeta — ver `SESSION_LOG_REPLANTEO_
  2026-07-05_01-37.md` para el estado exacto de DR-54 (sin resolver).

## Índice por archivo — fecha, contenido y a qué sección afecta

| Archivo | Fecha | DR principales | Afecta a |
|---|---|---|---|
| `SESSION_LOG_REPLANTEO_2026-06-19.md` / `_2.md` | 19/06 | DR-01 a DR-09 (fundacionales) | Transversal |
| `SESSION_LOG_REPLANTEO_2026-06-20_3/4/5.md` | 20/06 | DR-10 (3er objetivo: portfolio de data science) | `3_ANALISIS/` |
| `SESSION_LOG_REPLANTEO_2026-07-03.md` / `_2.md` | 03/07 | DR-22 (origen "democratización"), DR-23 (gaps de conocimiento del mod) | **`1_MOD/`** (DR-22, DR-23) |
| `SESSION_LOG_REPLANTEO_2026-07-03_01-52.md` | 03/07 01:52 | + DR-24 (nomenclatura, extiende regla del mod al replanteo) | **`1_MOD/`** (DR-24 nace de una regla ya existente del mod) |
| `SESSION_LOG_REPLANTEO_2026-07-03_01-57.md` | 03/07 01:57 | Refuerzo de DR-24 (la regla escrita falló al primer uso real) | Transversal (regla de proceso) |
| `SESSION_LOG_REPLANTEO_2026-07-03_02-13.md` | 03/07 02:13 | Sin cambios de fondo sobre `01-57` | — |
| `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` | 03/07 02:43 | + DR-25 (3 piezas, no 4), DR-26 (criterio de cierre) | Transversal — define la relación entre las 3 piezas |
| `SESSION_LOG_REPLANTEO_2026-07-03_17-47.md` / `_17-58.md` / `_17-58 2.md` | 03/07 tarde | DR-27 (estructura física de carpetas), DR-28-30 (prueba de fuga de memoria), DR-31 (nomenclatura de `fuentes de documentacion`), DR-33 (verificación de 21 zips anidados) | **`2_DOCUMENTACION/`** (DR-31, la carpeta con más contradicciones, ver `07_fuentes_documentacion/`) |
| `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` | 04/07 23:17 | DR-34 (cierre de prueba de fuga de memoria, causa raíz en `claude_5`) | `3_ANALISIS/04_prueba_fuga_memoria/` |
| `SESSION_LOG_REPLANTEO_2026-07-04_23-44.md` | 04/07 23:44 | DR-35 a DR-38 (auditoría de fugas de continuidad, regla de consolidación) | Transversal |
| `SESSION_LOG_REPLANTEO_2026-07-05_00-10.md` | 05/07 00:10 | DR-39 a DR-44 (correcciones de citas, causa raíz de contaminación de memoria en `claude_5`) | Transversal |
| `SESSION_LOG_REPLANTEO_2026-07-05_00-32.md` | 05/07 00:32 | DR-45 a DR-49 (inventario completo de material de archivo) | Transversal |
| `SESSION_LOG_REPLANTEO_2026-07-05_00-52.md` | 05/07 00:52 | Cierre de Tarea 1 (reorganización), corrección de clasificación Corpus A/B | **`1_MOD/`** + **`2_DOCUMENTACION/`** (límite Corpus A/B) |
| `SESSION_LOG_REPLANTEO_2026-07-05_01-37.md` | 05/07 01:37 | **DR-52** (encuadre Paper C1/Skill C2), **DR-53** (vínculo diplomatura↔pipeline), **DR-54** (bloqueante: mapeo métricas↔Consigna 1 UTN, sin resolver) | **`2_DOCUMENTACION/`** (DR-52) + **`3_ANALISIS/`** (DR-53, DR-54) |

## Qué NO va acá

Historia de desarrollo técnico del mod en sí (sesiones de código, mecánicas,
eventos) — eso es `1_MOD/06_historial_desarrollo/`. Charlas de diseño del
análisis (7-12) o auditorías de continuidad de archivos — eso es
`3_ANALISIS/`.
