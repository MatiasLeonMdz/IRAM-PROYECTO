# 2_DOCUMENTACION/

## Qué contiene
Objetivo 2 del proyecto: documentación del *proceso* de creación del mod y de la metodología de trabajo con Claude (Paper C1, Skill C2) — no el análisis A/B ni la tarea UTN (eso vive en `3_ANALISIS/`).

## Subcarpetas
- `02_charlas_y_resumenes/` — charlas 1-6 + resúmenes de charlas de replanteo
- `04_corpus_A_mod_docs/`, `05_corpus_B_crudo/` — corpus documental usado para el paper/skill
- `07_fuentes_documentacion/` — fuentes documentales de referencia. Subdividida
  el 2026-07-08 en 10 subcarpetas temáticas (prompts, session logs, borradores
  C1, paper/skill, wikis, hitos, sesiones fallidas, análisis C1, scripts,
  corpus procesado) — ver su README para el índice completo. En el mismo
  proceso se purgaron 27 duplicados exactos por hash (nunca detectados antes)
  a `_CUARENTENA_DUPLICADOS/07_fuentes_documentacion_duplicados_2026-07-08/`.
- `08_documentacion_respaldo/` — respaldos de documentación (subconjunto
  parcial de `07_fuentes_documentacion/`, no espejo completo — ver nota en
  el README de esa carpeta)

## Punto de entrada
Para entender la metodología de trabajo: empezar por `07_fuentes_documentacion/` y
`0_REPLANTEOS_Y_DECISIONES/` (ver nota abajo).

## Nota — dos mudanzas del 2026-07-08
- La serie `SESSION_LOG_REPLANTEO_*` (antes `01_logs_replanteo/` acá) se movió
  a `0_REPLANTEOS_Y_DECISIONES/01_logs_replanteo/`, carpeta nueva a la misma
  altura que `1_MOD/`, `2_DOCUMENTACION/` y `3_ANALISIS/` — no es documentación
  del proceso del mod, es el replanteo transversal de encuadre de todo el
  proyecto (define las 3 piezas, sus reglas, y toca a las tres por igual).
  Ver ese README para el índice completo.
- `06_historial_desarrollo_mod/` se movió a `1_MOD/06_historial_desarrollo/` —
  es desarrollo técnico estricto del mod, no documentación del proceso.

Las charlas 7-12 tampoco están acá — viven en
`3_ANALISIS/02_charlas_diseño_analisis/` porque son insumo directo del
análisis, no documentación del proceso del mod.
