# 08_documentacion_respaldo/

Material de respaldo/histórico rescatado de las copias de seguridad viejas del
escritorio, en la sesión de unificación del 2026-07-10 (ver
`LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` en la raíz del proyecto para el
detalle completo, archivo por archivo, de esa auditoría).

No es documentación de trabajo activo — es contexto histórico que se conserva
por completitud. Para el estado vigente del proyecto, ver
`FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md` en la raíz.

## Contenido actual

Solo queda una subcarpeta:

- **`readmes_indices_historicos/`** — versiones anteriores de README/INDICE de
  otras carpetas del proyecto, distintas por contenido de la versión vigente
  (se conservan calificadas por carpeta de origen, nunca reemplazan al README/INDICE
  actual de ninguna carpeta). 9 archivos.

## Subcarpetas eliminadas (100% redundantes, verificado por hash)

En la sesión de unificación del 2026-07-10 se crearon originalmente 3
subcarpetas más acá (`historiales_completos/`, `reorganizaciones/`,
`borradores_planificacion/`), con contenido rescatado de copias de seguridad
viejas. Una revisión posterior en la misma sesión (§23 de la fuente de
verdad) encontró que las tres eran, en su totalidad, contenido ya presente en
otras partes del árbol activo — verificado por hash normalizado (CRLF/LF)
archivo por archivo:

- **`historiales_completos/`** (15 archivos) → idénticos a material ya en
  `1_MOD/06_historial_desarrollo/` (11 de 15) y en
  `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/` (3 de 15:
  `IRAM_HISTORIA_COMPLETA_v1_1.md`, `IRAM_HISTORIA_COMPLETA_v1_2.md`,
  `IRAM_historial_unificado_2026-06-12.md`) y en
  `1_MOD/IRAM_legacy v1 v2 v3 v4/` (1 de 15: `IRAM_SUPERBACKUP_v2_1.md`).
- **`reorganizaciones/`** (4 archivos: `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`,
  `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md`, `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md`,
  `LOG_REORGANIZACION_2026-07-05.md`) → idénticos a los mismos 4 archivos que
  vivían (hasta que se borraron por duplicado, en sesión posterior) en
  `00_fuente_de_verdad/`.
- **`borradores_planificacion/`** (5 archivos) → idénticos a material ya en
  `00b_descartables/` (`Qwen_markdown_20260705_q4xkzeqjf.md`,
  `deepseek_markdown_20260705_98aa15.md`) y en
  `3_ANALISIS/04_prueba_fuga_memoria/` (`memoria_claude_volcado.md`,
  `volcado_memoria.md`) y en `2_DOCUMENTACION/02_charlas_y_resumenes/`
  (`sigue log.md`).

Las 3 se eliminaron enteras (24 archivos en total) con `git rm`. Esta acción
había quedado **documentada como ya hecha en §23.3 de la fuente de verdad,
pero sin ejecutar sobre los archivos** hasta la sesión de auditoría del
2026-07-10 (continuación) que encontró la discrepancia y la resolvió — ver
esa sección de la fuente de verdad para el registro completo del hallazgo y
la corrección.

## Nota sobre una carpeta que ya no existe acá: `_viejo_100pct_duplicado_verificar_borrar/`

Durante el armado de este árbol (10-07) se encontró una carpeta `DOCUMENTACION/`
preexistente en este mismo lugar, con 27 archivos que resultaron ser, sin
excepción, duplicados exactos (verificados por hash SHA-256 normalizado) de
material ya organizado en `2_DOCUMENTACION/07_fuentes_documentacion/`. Se aisló
temporalmente con nombre explícito para permitir confirmación del operador antes
de borrar, y se confirmó y borró el mismo día. El contenido sigue disponible en
su ubicación organizada dentro de `07_fuentes_documentacion/`.
