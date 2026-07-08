# 07_fuentes_documentacion/

## Qué contiene

Los insumos crudos de trabajo de la metodología multi-sesión de
documentación del mod (prompts maestros, session logs, borradores del paper
C1, wikis técnicas, hitos, sesiones fallidas, scripts de análisis y el
corpus de conversaciones de Claude ya procesado). 161 archivos originales,
subdivididos el 2026-07-08 tras detectar que era la carpeta más grande sin
tocar del proyecto (pendiente arrastrado desde §21.5 de la fuente de
verdad).

**No confundir con `08_documentacion_respaldo/`** — no es un espejo
completo de esta carpeta (tiene 27 archivos, no 161). Es un subconjunto
puntual de una etapa anterior del proyecto. La relación exacta entre ambas
no está verificada archivo por archivo; DR-45 (`fuentes de verdad`, línea
45) los describe como "respaldo exacto" pero eso corresponde a un estado
más chico y anterior de esta carpeta, no al estado actual de 161 archivos.
Si hace falta cerrar esa relación con certeza, comparar por hash — mismo
método que se usó para la purga de esta sesión (ver abajo).

## Subcarpetas

| Carpeta | Contenido | Archivos |
|---|---|---|
| `01_prompts_maestros/` | Prompts maestros y de documentación (versiones v1.4 a v1.9, v5.2, reglas v2) | 9 |
| `02_session_logs_documentacion/` | Serie `SESSION_LOG_DOCUMENTACION_*` completa (s7 a s34, consolidados) | 35 |
| `03_borradores_C1/` | Borradores del paper C1 por sesión (`s1_draft` a `s7_draft`), esqueleto, completo y final | 18 |
| `04_paper_y_skill_versiones/` | Versiones del paper de metodología y de la skill v1.0/v2.0 | 5 |
| `05_wikis_y_metodologia/` | `WIKI_DOCUMENTACION_v1/v2`, `TECHNICAL_WIKI_ACTIVE/ARCHIVE`, metodología, templates | 7 |
| `06_hitos_y_analisis/` | Hitos metodológicos, análisis cuantitativo, gaps de conocimiento, crítica rigurosa | 11 |
| `07_sesiones_fallidas/` | Sesiones cortadas o fallidas — transcripciones crudas, incluye la que ubica DR-22 (mislabel "democratiza") | 17 |
| `08_analisis_C1_consolidado/` | `SESSION_LOG_ANALISIS_C1_*`, consolidado 2026-06-18 y sus transcripciones, correcciones de sesión | 10 |
| `09_scripts_python/` | Scripts de análisis (`spec_a/b/c`, `bloque3_analysis`, `generate_iram_docs`, `process_iram_v2`) — 1 copia por script tras purga | 8 |
| `10_corpus_claude_processed/` | Los 5 `claude_N_processed.json` (corpus de conversaciones ya procesado, ~1.4-2 MB c/u) | 5 |

## Sueltos en la raíz (no encajan en ninguna subcarpeta temática)

- `IRAM_historial_unificado_2026-06-12.md` (3.6 MB) — el propio archivo
  `---------INSTRUCCIONES-------.txt` de esta carpeta indica que **no** hace
  falta adjuntarlo en sesiones nuevas, porque se puede regenerar con los
  scripts + el corpus en minutos.
- `IRAM_HISTORIA_COMPLETA_v1_1.md`, `IRAM_HISTORIA_COMPLETA_v1_2.md`
- `critica 1.md`, `critica a la critica.md`
- `correccion de documentacion.md`, `correccion de documentacion 2.md`
- `-----------------LEER---------------------.txt`,
  `---------INSTRUCCIONES-------.txt` — guía original de qué adjuntar en
  cada tipo de sesión de trabajo con Claude (SIEMPRE / Plantilla B / Plantilla C)

## Purga ejecutada en esta sesión (2026-07-08)

Se detectaron **22 grupos de duplicados exactos por hash SHA-256** (34
archivos con contenido idéntico) — nunca se había revisado esta carpeta con
ese método. Se dejó 1 canónico por grupo in situ (en su subcarpeta temática)
y se movieron los 27 archivos redundantes a
`_CUARENTENA_DUPLICADOS/07_fuentes_documentacion_duplicados_2026-07-08/`,
con README propio que incluye la lista completa de hashes.

**Importante — verificado explícitamente:** varios archivos con nombre
parecido (mismo nombre base + sufijo `(2)`) **no** son duplicados —
contenido genuinamente distinto, mismo patrón que ya identificó el Paquete C
de la fuente de verdad para `IRAM_paper_metodologia_v1_0` e
`IRAM_skill_desarrollo_ia_v2_0`. Esos casos se dejaron intactos.

Verificación de integridad: 161 archivos originales = 134 quedaron acá
(distribuidos + sueltos en raíz) + 27 en cuarentena. Cero pérdida.

## Pendiente

Chequeo de hash de esta carpeta (y en general, del árbol completo del
proyecto) contra las copias de seguridad externas que tiene el operador —
verificación independiente adicional, no ejecutada en esta sesión. Ver
tarea nueva registrada en la fuente de verdad.
