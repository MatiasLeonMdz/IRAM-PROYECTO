# 04_corpus_A_mod_docs/

Versión procesada/curada del "corpus A" — documentación específica del
desarrollo del mod IRAM (prompts maestros, wikis técnicas, logs de sesión,
instrucciones al humano). Es la contraparte organizada del material crudo
que vive en `1_MOD/corpus_A_crudo/` (exports sin procesar de conversaciones
de Claude).

## Contenido (9 archivos)

- `IRAM_PROMPT_MAESTRO_v3_8_2026-05-27_20-55.md` y `_v3_9_2026-05-30_03-14.md`
- `IRAM_SESSION_LOG_2026-05-28_17-31.md`, `_2026-05-29_05-29.md`, `_2026-05-30_03-14.md`
- `IRAM_TECHNICAL_WIKI_ACTIVE_v3_1_2026-05-27_20-55.md` y `_v3_2_2026-05-30_03-14.md`
- `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_1_2026-05-27_20-55.md` y `_v3_2_2026-05-30_03-14.md`

Las versiones `v3_1`/`v3_8` corresponden a la sesión del 27-05-2026 y las
`v3_2`/`v3_9` a la del 30-05-2026 — ambas se conservan como snapshots de
distintos momentos, no como borrador vs. versión final.

## Nota de verificación: duplicado resuelto con `00_fuente_de_verdad/`

Esta carpeta tenía una copia de `IRAM_INSTRUCCIONES_HUMANO_2026-05-27_20-55.md`
que era **duplicado exacto** (idéntico ignorando CRLF/LF) del mismo archivo
en `00_fuente_de_verdad/`. El operador confirmó `00_fuente_de_verdad/` como
copia canónica —consistente con que su README ya lo lista como parte de su
contenido esperado— y se eliminó la copia de esta carpeta con `git rm`
(ítem #9 de pendientes organizativos, resuelto).
