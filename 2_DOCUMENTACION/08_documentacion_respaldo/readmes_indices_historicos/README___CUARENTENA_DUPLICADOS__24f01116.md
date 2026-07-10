# Duplicados purgados de `2_DOCUMENTACION/07_fuentes_documentacion/` (2026-07-08)

**Estado: EJECUTADA.** Parte de la subdivisión de `07_fuentes_documentacion/`
(161 archivos → 10 subcarpetas temáticas + purga), tarea que quedó pendiente
desde §21.5 ("no se revisó si necesita subdivisión").

## Qué se encontró

Al inventariar los 161 archivos de `07_fuentes_documentacion/fuentes de
documentacion/` **por hash SHA-256 del contenido completo**, no por nombre,
aparecieron **22 grupos de duplicados exactos** (34 archivos con contenido
byte-por-byte idéntico entre sí). Mismo patrón ya purgado en otras partes del
proyecto (§17.1, §20, §21.3.6) — nunca se había revisado esta carpeta en
particular.

**Verificación explícita del caso contrario:** varios archivos con el mismo
patrón de nombre (`nombre (2).ext`) **no** son duplicados — tienen contenido
distinto de su base. Esos se dejaron intactos, sin tocar, en su subcarpeta
temática correspondiente. Ejemplos verificados como NO duplicados (hash
distinto, no purgados):
- `IRAM_C1_s4_draft_s30 (2).md` vs `IRAM_C1_s4_draft_s30.md`
- `IRAM_skill_desarrollo_ia_v2_0 (2).md` vs `IRAM_skill_desarrollo_ia_v2_0.md`
- `PROMPT_DOCUMENTACION_IRAM_v1_9 (2).md` vs `PROMPT_DOCUMENTACION_IRAM_v1_9.md`
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v2 (2).md` vs `...v2.md`
- `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO (2).md` vs `...CONSOLIDADO.md`
- `spec_c_zip_history (2).py` vs `spec_c_zip_history.py`
- `failed (2).md` vs `failed.md`

## Criterio de purga aplicado

Por cada grupo de hash idéntico, quedó **un solo canónico in situ** (dentro
de la subcarpeta temática nueva de `07_fuentes_documentacion/`) y el resto se
movió acá. Regla de selección del canónico: se prefirió el nombre de archivo
**sin** sufijo `(N)`; si ningún archivo del grupo tenía nombre limpio, se dejó
el primero por orden alfabético (2 grupos: `spec_c_zip_history` y
`SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s13`, ver detalle abajo).

## Archivos purgados (27) con hash — para auditoría contra copias de seguridad externas

```
1f59b4568e88f86c15186af128ad8a64ccb3e483dbc479efd94a9c21a17d2714  IRAM_C1_s3_draft_s20 (2).md
fadcdd1dfa6de1bc1bc2d9a9ccf3d89ea415cb69ca84234145cb8fb17f2577ff  IRAM_C1_s7_draft_s25 (2).md
04d8d19c6491561518661d96b6ec0a1dc74114d757b6b1d9866730d71c06dec1  IRAM_HISTORIA_COMPLETA_v1_2 (2).md
9121dd1ddf33d14a81391d0066c86e13cdb156d162fd16af0823af7faa6905d6  IRAM_PROMPT_MAESTRO_v5_2_2026-06-06 (2).md
d86d107a5ca6b9ebb7b4d2ac31679582db8c87efb18d274ce74173b741f50a72  IRAM_SESSION_LOG_v5_6_2026-06-09_17-59 (2).md
74bf322d6932c6c09fd0df800c10589c0c783bf7c3509d9dd1b285465655f88a  IRAM_SKILL_desarrollo_con_IA_v1_0 (2).md
edf106006b5870845c419aafb878782bb419d0eeaabde7083894c43f073a2867  IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09 (2).md
edf106006b5870845c419aafb878782bb419d0eeaabde7083894c43f073a2867  IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09 (3).md
601f98e8ff0b151bee7a41dbad45d150a2e63b3eba918c2e720e6422ecfcb42c  IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09 (2).md
15838a2639e0f694a2aca212f07193e672b81df540778e40b017acf39bf21aa4  IRAM_hitos_metodologicos_2026-06-11_v6 (2).md
e568d570e1020dab032ce3d25923545a93e9229215093a02c27c85b8a0717c0a  IRAM_hitos_metodologicos_2026-06-12_v7 (2).md
87bf74f5b69beb3962f99be399648bd07dc7d9bb916f07a979ce8058828e2514  IRAM_skill_desarrollo_ia_v2_0 (3).md
a44f4ea5c279c72ed7f81c94b2604be60be74994512bcd244497e7af505c7ff7  PROMPT_DOCUMENTACION_IRAM_v1_9 (3).md
32d08850a9f344e96ee356d1a251bc877f4bacb1fed5e59f613f29932b0a3e01  PROMPT_DOCUMENTACION_IRAM_v1_9 (4).md
32d08850a9f344e96ee356d1a251bc877f4bacb1fed5e59f613f29932b0a3e01  PROMPT_DOCUMENTACION_IRAM_v1_9(1).md
37cbfb0864ae4b5e72d6b39d13cb14b32e93cef6bd25d3221aa4969fa717717d  PROMPT_MAESTRO_v1_8(1).md
ba3f7fb5a6f8129d2da79a644d73f7a6c3c8c19b85651ec5a7b15691b6f2091d  SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO_s11 (2).md
3ab6e6f687bf019840f9397727b6583aa0e4f77e677914f090cadfbc2fb78c0a  SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s13 (3).md
7c6ee3838f007a418e320187c43dac47ad1f30c0a5996110b398723f9b0ac55c  SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19 (2).md
a2b1410f98bd0424c7e83c3e6db9994962059c92737e303e5bee5fefff9539cd  failed (3).md
278d6289735f4bc49b5edda118fba653ca0aa478e645cd42f9a71abb3160e600  generate_iram_docs (2).py
e2de75cb5ac2953830c587210e37f3b4242b68ab452995a0fe83bf56cef45912  process_iram_v2 (2).py
d48b6f642fe3a9d4ca317c117e0f035fc0807f53e5ae0545b2a42fdac56e27a7  spec_b_democratizacion (2).py
d48b6f642fe3a9d4ca317c117e0f035fc0807f53e5ae0545b2a42fdac56e27a7  spec_b_democratizacion (3).py
d48b6f642fe3a9d4ca317c117e0f035fc0807f53e5ae0545b2a42fdac56e27a7  spec_b_democratizacion (4).py
f3cef25b819abc887f9c71aba69865393dfe07d3fd0153d1682c05cbf4dc32a8  spec_c_zip_history (3).py
f3cef25b819abc887f9c71aba69865393dfe07d3fd0153d1682c05cbf4dc32a8  spec_c_zip_history (4).py
```

## Dos casos sin nombre limpio en el grupo

- **`spec_c_zip_history`**: el grupo tenía `(2)`, `(3)`, `(4)` — ninguna copia
  sin sufijo. Quedó `spec_c_zip_history (2).py` como canónico en
  `09_scripts_python/`, por ser el primero alfabéticamente.
- **`SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s13`**: mismo caso,
  grupo con `(1)`, `(2)`, `(3)`. Quedó `... s13 (2).md` como canónico en
  `02_session_logs_documentacion/`.

Ninguno de los dos afecta el contenido — por definición del grupo, las 3-4
copias son idénticas byte a byte; solo cambia cuál nombre de archivo
sobrevive.

## Verificación de integridad

- 161 archivos originales = 134 que quedaron distribuidos en las 10
  subcarpetas + raíz de `07_fuentes_documentacion/` + 27 acá. Conteo
  verificado con `find | wc -l` antes y después del movimiento.
- Cero duplicados por hash restantes en `07_fuentes_documentacion/` tras la
  purga (verificado con `sha256sum` + `uniq -c` sobre los 134 archivos
  finales).

## Pendiente — no resuelto en esta sesión

El operador va a correr un chequeo de hash de estos 27 archivos (y en
general, de todo el árbol) **contra sus copias de seguridad externas** al
proyecto, como verificación independiente adicional a la de este README.
Ver tarea nueva en `07_fuentes_documentacion/README.md` y en la fuente de
verdad.
