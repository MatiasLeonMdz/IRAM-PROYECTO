# INVENTARIO COMPLETO DEL MATERIAL DE ARCHIVO — IRAM_PROYECTO3.zip
**Fecha de generación:** 2026-07-05 | **Corresponde a:** Tarea 4 de PRÓXIMAS TAREAS (`SESSION_LOG_REPLANTEO_2026-07-05_00-10.md`)
**Método:** extracción completa del ZIP (1991 archivos), hash MD5 por archivo para detectar duplicados exactos de contenido, y clasificación manual por área según los logs de replanteo vigentes.
**No reemplaza el apéndice de navegación de `00-10`** — lo complementa con el detalle ítem por ítem que ese apéndice explícitamente decía que faltaba. No se tocó ningún archivo del proyecto (solo lectura).

---

## 0. RESUMEN EJECUTIVO

| Métrica | Valor |
|---|---|
| Archivos totales en el ZIP | 1991 |
| Archivos dentro de `game/` (mod, código fuente Imperator Rome) | 906 — **fuera de alcance, no tocar** |
| Archivos dentro de `IRAM mod v5/` (repo git del mod + mod packs) | 70 — mayoría fuera de alcance, 10 son documentación (ver §5) |
| Archivos dentro de `IRAM_legacy v1-v4/` (mod packs viejos) | 243 — fuera de alcance |
| Archivos de documentación en alcance (raíz + `DOCUMENTACION/` + `fuentes de documentacion/` + `historial viejo/`, sin contar la carpeta anidada duplicada) | 244 |
| — de los cuales, **contenido único** (por hash) | 188 |
| — de los cuales, **copias exactas** (mismo contenido, nombre o carpeta distinta) | 56, agrupados en 43 grupos de duplicado |
| Carpeta anidada 100% duplicada detectada | `documentacion iram 10-06-2026 00.30/documentacion iram 10-06-2026 00.30/` (261 archivos, duplicado byte a byte del padre) |
| Sub-duplicado anidado detectado | `fuentes de documentacion/fuentes de documentacion/` (163 de 163 archivos comparables son duplicado exacto del padre; la diferencia de conteo son dos copias de un mod pack extraído, no documentación) |
| Archivos nuevos no listados en el apéndice de `23-44`/`00-10` | 5 archivos `data-*-batch-0000.zip` en `historial viejo/` (ver §6) |

**Hallazgo estructural principal:** `DOCUMENTACION/` (27 archivos) es, para todo ítem que se solapa por nombre, un **duplicado exacto de contenido** de su equivalente en `fuentes de documentacion/`. No hay ningún archivo en `DOCUMENTACION/` con contenido distinto al de su par en `fuentes de documentacion/`. Esto no estaba explicitado en los logs previos.

---

## 1. SERIE `SESSION_LOG_REPLANTEO_*` (raíz del ZIP)

Cadena canónica ya establecida por DR-39: `2026-06-19_2` → `2026-06-20_5` → `2026-07-03_02-43` → `2026-07-03_17-58 2` → `2026-07-04_23-17` → `2026-07-04_23-44` (este último no está en el ZIP, se subió suelto) → `2026-07-05_00-10` (idem).

| Archivo | Estado |
|---|---|
| `SESSION_LOG_REPLANTEO_2026-06-19 2.md` | Histórico — inicio de cadena canónica |
| `SESSION_LOG_REPLANTEO_2026-06-19.md` | Histórico — versión previa a la `_2`, no canónica |
| `SESSION_LOG_REPLANTEO_2026-06-20 3.md` | Histórico — duplicado exacto de `2026-06-20 4.md` (no en ZIP, visto en listado anterior) |
| `SESSION_LOG_REPLANTEO_2026-06-20 5.md` | Histórico — canónico de ese punto de la cadena |
| `SESSION_LOG_REPLANTEO_2026-07-03.md` | Histórico — borrador temprano del 03/07 |
| `SESSION_LOG_REPLANTEO_2026-07-03 2.md` | Histórico |
| `SESSION_LOG_REPLANTEO_2026-07-03_01-52.md` | Histórico |
| `SESSION_LOG_REPLANTEO_2026-07-03_01-57.md` | Histórico |
| `SESSION_LOG_REPLANTEO_2026-07-03_02-13.md` | Histórico |
| `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` | Histórico — canónico (DR-10 a DR-26) |
| `SESSION_LOG_REPLANTEO_2026-07-03_17-47.md` | **Descartado formalmente por DR-40** — no citar |
| `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` | **No usar** — versión sin sufijo, cita rota (DR-39) |
| `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md` | Canónico vigente (DR-27 a DR-33, corregido por DR-39) |
| `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` | Histórico — canónico (DR-34) |

*(`23-44` y `00-10` no están en el ZIP — se cargaron como archivos sueltos en esta conversación.)*

---

## 2. CHARLAS FUNDACIONALES Y RESÚMENES (raíz)

| Archivo | Estado |
|---|---|
| `CHARLA REPLANTEO 1.md` | Histórico — transcripción cruda, citable puntualmente |
| `CHARLA REPLANTEO 2.md` | Histórico — ídem |
| `RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20.md` | Histórico — duplicado exacto de la versión `2` |
| `RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20 2.md` | Histórico — duplicado exacto de la anterior |
| `SESION TRUNCADA.md` (229 KB) | Histórico — transcripción cruda de sesión cortada (nombre de archivo, no el fenómeno estructural) |
| `sigue log.md` | Histórico — transcripción cruda, origen de DR-26 |

---

## 3. PRUEBA DE FUGA DE MEMORIA (raíz)

| Archivo | Estado |
|---|---|
| `instruccion_prueba_fuga_memoria.md` | Vigente — plantilla de la prueba |
| `resultado_prueba_fuga_memoria.md` | Vigente — evidencia de DR-29/34/41/43 |
| `memoria_claude_volcado.md` | Vigente — volcado usado en la prueba |
| `volcado_memoria.md` | Vigente — ídem |

---

## 4. CONSIGNAS UTN (raíz)

| Archivo | Estado |
|---|---|
| `Consigna.md` / `Consigna.pdf` | Vigente — mismo contenido, dos formatos |
| `Consigna_1.md` / `Consigna_1.pdf` | Vigente |
| `Consigna_2.md` / `Consigna_2.pdf` | Vigente |

*(No se verificó si el `.md` y el `.pdf` de cada consigna son texto-idénticos — el hash no aplica entre formatos distintos. Pendiente si hace falta.)*

---

## 5. CORPUS B CRUDO — EXPORTS DE CLAUDE.AI (raíz + `IRAM mod v5/`)

Todos son bundles de exportación de Claude.ai (`users.json`, `conversations.json`, `projects/*.json`, y en el caso de `claude 5`, también `memories.json`). **Sin procesar**, tal como indica el apéndice de `00-10`.

| Archivo | Contenido interno | Estado |
|---|---|---|
| `documentacion claude 1.zip` | users, conversations, 2 projects | No procesado |
| `documentacion claude 2.zip` | users, conversations, 1 project | No procesado |
| `documentacion claude 3.zip` | users, conversations, 1 project | No procesado |
| `documentacion claude 4.zip` | users, conversations, 1 project | No procesado |
| `documentacion claude 5.zip` | users, conversations, memories, 2 projects | No procesado — **es el único con `memories.json`**, relevante para DR-34/43 si alguna vez se decide verificar documentalmente (con la salvedad ya anotada en DR-43: no llega a la fecha de la charla contaminada) |

Además, dentro de `IRAM mod v5/` (repo git temprano del mod, mayo 2026) hay **10 archivos de documentación real**, no listados individualmente en el apéndice anterior:

| Archivo | Estado |
|---|---|
| `IRAM_INSTRUCCIONES_HUMANO_2026-05-27_20-55.md` | Histórico — fase temprana (v3.x) |
| `IRAM_PROMPT_MAESTRO_v3_8_2026-05-27_20-55.md` | Histórico |
| `IRAM_PROMPT_MAESTRO_v3_9_2026-05-30_03-14.md` | Histórico |
| `IRAM_SESSION_LOG_2026-05-28_17-31.md` | Histórico |
| `IRAM_SESSION_LOG_2026-05-29_05-29.md` | Histórico |
| `IRAM_SESSION_LOG_2026-05-30_03-14.md` | Histórico |
| `IRAM_TECHNICAL_WIKI_ACTIVE_v3_1_2026-05-27_20-55.md` | Histórico |
| `IRAM_TECHNICAL_WIKI_ACTIVE_v3_2_2026-05-30_03-14.md` | Histórico |
| `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_1_2026-05-27_20-55.md` | Histórico |
| `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_2_2026-05-30_03-14.md` | Histórico |

El resto de `IRAM mod v5/` (4 `mod_pack_*.zip`, `.git/`, 70 archivos en total) es **el mod en sí — fuera de alcance, no tocar**.

---

## 6. `historial viejo/` — HALLAZGO NUEVO DE ESTA AUDITORÍA

Contiene 8 archivos de historial de desarrollo del mod (`IRAM_historial_desarrollo_2` a `_5`, cada uno con versión "LIMPIO"/"clean" además de la cruda) y 2 prompts de etapa de limpieza/unificación — todos histórico, ya conocidos por el apéndice.

**Lo no listado antes:** 5 archivos `data-<uuid>-<timestamp>-batch-0000.zip`, entre 2.3 y 3.3 MB cada uno. Al inspeccionarlos, tienen la **misma estructura que `documentacion claude N.zip`** (`users.json`, `conversations.json`, `projects/*.json`) — es decir, son **exports de Claude.ai más viejos**, de un período anterior al de `documentacion claude 1-5.zip` (a juzgar por los timestamps Unix en el nombre, corresponden a comienzos de enero de 2026).

| Archivo | Estado |
|---|---|
| `data-4fce9ea4-...-batch-0000.zip` | **Pendiente clasificar** — export de Claude.ai no identificado en ningún log anterior |
| `data-6a75897c-...-batch-0000.zip` | ídem |
| `data-7f3f05d6-...-batch-0000.zip` | ídem |
| `data-a158d766-...-batch-0000.zip` | ídem |
| `data-d64c441d-...-batch-0000.zip` | ídem |

No se abrió el contenido interno de estos 5 archivos (serían Corpus B crudo adicional, no procesado) — se deja consignado que existen y qué son, para que quien continúe decida si entran al Corpus B o quedan fuera por antigüedad/redundancia con `documentacion claude *.zip`.

---

## 7. `DOCUMENTACION/` (27 archivos) — duplicado de subconjunto de `fuentes de documentacion/`

Cada uno de los 27 archivos de esta carpeta tiene un par de contenido idéntico en `fuentes de documentacion/` (mismo hash MD5), excepto que en algunos casos `DOCUMENTACION/` conserva sufijos `(2)`, `(3)`, `(4)` de versiones subidas más de una vez. No hay divergencia de contenido en ningún par. Items: `IRAM_C1_final.md` (paper cerrado), `WIKI_DOCUMENTACION_v2.md` (sin tocar, DR-12), specs `a`/`b`/`c`, `TEMPLATES_DOCUMENTACION_v1.md`, `METODOLOGIA_DOCUMENTACION_v1.md`, serie `SESSION_LOG_ANALISIS_C1_2026-06-18*` (v2 a v5), `SESSION_LOG_CONSOLIDADO_2026-06-18.md`, `SESSION_LOG_DOCUMENTACION_s34.md`, 3 `SESION FALLADA *.md`, transcripción del consolidado en 2 partes.

Estado: **vigente como copia de respaldo**, no como fuente adicional — el contenido a citar es el mismo que en `fuentes de documentacion/`.

---

## 8. `fuentes de documentacion/` — grueso del Corpus B (265 archivos de nivel superior, sin contar su propia sub-copia anidada)

Este es el material más denso. Se agrupa por familia:

**a) Serie `SESSION_LOG_DOCUMENTACION_*`** — de `2026-06-10_22-30` a `s34`, incluye variantes `CONSOLIDADO` con sufijos de sesión (`s7` a `s21`), la `ESPECIAL_s21` (origen real de la regla de DR-42, per DR-42) y las simples `s22` a `s34`. Estado: histórico, cadena de trabajo del proceso de documentación — no redebatir contenido, solo consultar.

**b) Serie de borradores del paper C1** — `IRAM_C1_esqueleto_s17.md`, `IRAM_C1_s1_draft_s20/s31`, `s2_draft_s24/s30`, `s3_draft_s20/s31`, `s4_draft_s24/s30`, `s5_draft_s28/s29`, `s6_draft_s25/s30`, `s7_draft_s25/s30`, hasta `IRAM_C1_completo_s32.md` y `IRAM_C1_final.md`. Estado: histórico — el paper está cerrado en `IRAM_C1_final.md` (s34), estos son los pasos intermedios.

**c) Prompts maestro y de documentación** — `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md`, `PROMPT_MAESTRO_v1_6.md`, `v1_8`, `PROMPT_DOCUMENTACION_IRAM_v1_4` a `v1_9`, `PROMPT_REGLAS_DOCUMENTACION_v2.md`. Estado: histórico.

**d) Wikis técnicas** — `IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md`, `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09.md`, `WIKI_DOCUMENTACION_v1.md` y `v2.md`. Estado: `v2` sin tocar por DR-12; el resto histórico.

**e) Hitos e historia** — `IRAM_hitos_metodologicos_2026-06-10_v5.md`, `v6`, `v7` (esta última es la que requiere verificación de cifras, tarea 7 pendiente), `IRAM_HISTORIA_COMPLETA_v1_1.md` y `v1_2.md`, `IRAM_historial_unificado_2026-06-12.md` (3.7 MB, el más pesado del corpus textual), `IRAM_analisis_cuantitativo_2026-06-12` (v1 a v3), `IRAM_gaps_conocimiento_2026-06-12.md`, `IRAM_gap_v4_1_a_v4_3_16_CERRADO/nota_deuda`.

**f) Críticas y correcciones** — `IRAM_critica_rigurosa_2026-06-12.md`, `critica 1.md`, `critica a la critica.md`, `correccion de documentacion.md` / `2.md`, `CORRECCIONES_SESION_2026-06-12.md`.

**g) Sesiones fallidas / cortadas** — `SESION FALLADA 1/2/3.md`, `sesion fallada.md`, `s fallada 12-06.md` / `2.md`, `sesion cortada.md`, `fallo DOCUMENTACION 19-06-2026.md`, `fallo sesiones 16-06-2026.md`, `fallo sesiones transcript 16-06-2026.md`, `failed.md` / `2` / `3`, `sesion gap v4.1 - 4.3.md` (+ 3 partes). Estado: histórico, evidencia de patrones de fallo — no narrativa a repetir, solo consultar si hace falta el detalle puntual.

**h) Corpus B procesado parcialmente** — `claude_1_processed.json` a `claude_5_processed.json` (entre 1.4 y 2 MB cada uno). **Importante:** estos son distintos de `documentacion claude N.zip` de la raíz — son versiones ya procesadas/extraídas de esas conversaciones, no el crudo. No estaban mencionados como "procesados" en ningún estado anterior; si "Corpus B / sigue sin procesar" (tabla de ESTADO REAL) es correcto, hace falta aclarar qué se entiende por "procesado" acá, porque este archivo sugiere que sí hubo un paso de procesamiento en algún momento. **Flag para quien retome el análisis A/B.**

**i) Scripts** — `spec_a_authorship.py`, `spec_b_democratizacion.py` (+4 copias), `spec_c_zip_history.py` (+4 copias), `generate_iram_docs.py` (+1 copia), `process_iram_v2.py` (+1 copia), `bloque3_analysis.py` y `_v2.py`. Estado: herramientas de análisis, histórico/utilitario.

**j) Dos archivos de instrucciones sueltos** — `-----------------LEER---------------------.txt` (56 bytes) y `---------INSTRUCCIONES-------.txt` (1.5 KB). **No se abrieron por indicación de esta tarea (solo inventario, sin ejecutar instrucciones incrustadas en archivos de datos)** — quedan marcados como pendientes de revisión manual por el operador antes de que cualquier sesión los use como fuente, dado que un nombre así en medio del corpus de datos amerita confirmación humana antes de tratarlo como instrucción legítima.

**k) Mod packs extraídos dentro de `fuentes de documentacion/`** — `mod_pack_IRAM_v5_5_2026-06-09_03-22/` y su copia `(2)/`, con el árbol completo `iram_work/` del mod (decisions, events, localization, etc.). Esto es **código del mod, no documentación** — quedó mezclado en la carpeta de fuentes por error de organización en algún momento anterior. Fuera de alcance para el análisis de Corpus B, pero **candidato a mover en la Tarea 1 (estructura de carpetas DR-27)**, ya que hoy vive en el lugar equivocado.

**l) Sub-copia anidada `fuentes de documentacion/fuentes de documentacion/`** — duplicado exacto (161 de 161 archivos comparables) de la carpeta padre. Mismo patrón que la duplicación de `documentacion iram 10-06-2026 00.30/`.

---

## 9. FUERA DE ALCANCE — NO TOCAR

| Área | Archivos | Motivo |
|---|---|---|
| `game/` | 906 | Código fuente del mod (Imperator Rome). Regla vigente: no tocar el mod. |
| `IRAM mod v5/` (excluyendo los 10 docs de §5) | 60 | Repo git + mod packs, código del mod. |
| `IRAM_legacy v1 v2 v3 v4/` | 243 | Mod packs y backups viejos del mod. |
| `mod_pack_IRAM_v5_5_*` (dentro de `fuentes de documentacion/`, x2 copias) | incluidos en el conteo de §8k | Código del mod mezclado en carpeta de documentación por error — no auditar contenido, solo mover en su momento. |
| `achievements_imperator.xlsx`, `wiki_imperator.txt` | 2 | Ya marcados en el apéndice anterior como "sin relación directa, no auditados" — se mantiene ese estado. |

---

## 10. DUPLICADOS EXACTOS DETECTADOS (43 grupos, 56 archivos redundantes)

La lista completa de grupos de duplicado (mismo hash MD5, distinto nombre o ubicación) está disponible si hace falta para la limpieza física de la Tarea 1. En resumen, los duplicados caen en tres patrones:

1. **`DOCUMENTACION/` vs `fuentes de documentacion/`** — 19 pares, contenido idéntico (ver §7).
2. **Sufijos `(2)`, `(3)`, `(4)` del mismo archivo subido varias veces** dentro de la misma carpeta — 21 grupos (ej. `spec_b_democratizacion.py` tiene 8 copias idénticas entre las dos carpetas).
3. **Duplicación estructural de carpetas completas** — la sub-copia anidada de `documentacion iram 10-06-2026 00.30/` (261 archivos) y la de `fuentes de documentacion/` (161 archivos).

**No se borró ni movió nada** — esto es insumo para cuando se ejecute la Tarea 1 (estructura física) y la Tarea 2 (plan de 3 capas DR-32), no una acción de esta tarea.

---

## 11. HALLAZGOS PARA EL PRÓXIMO LOG (candidatos a DR, a decisión del operador)

- El apéndice de `00-10` no mencionaba: los 5 `data-*-batch-0000.zip` de `historial viejo/` (§6), los `claude_N_processed.json` de `fuentes de documentacion/` (§8h), los dos archivos sueltos de instrucciones (§8j), ni el mod pack duplicado dentro de `fuentes de documentacion/` (§8k).
- La equivalencia exacta `DOCUMENTACION/` = subconjunto de `fuentes de documentacion/` (§7) no estaba documentada explícitamente en ningún log previo.
- La existencia de `claude_N_processed.json` contradice, o al menos matiza, la fila "Corpus A / Corpus B — sin cambios de estado, sigue sin procesar" del ESTADO REAL de `00-10`. Queda para que el operador decida si es un procesamiento real ya hecho o un artefacto de otra prueba.

Este documento no reemplaza ni reescribe el log de replanteo — es un insumo para que, si el operador lo pide, el próximo `SESSION_LOG_REPLANTEO` incorpore estos hallazgos como DR nuevos citando este archivo como fuente.
