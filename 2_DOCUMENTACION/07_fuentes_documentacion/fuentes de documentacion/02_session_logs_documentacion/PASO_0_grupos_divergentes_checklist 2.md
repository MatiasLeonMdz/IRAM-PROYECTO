# PASO 0 — Checklist de grupos con contenido genuinamente divergente

Filtrado de los 43 grupos detectados por `verificar_iram.py colisiones`. Se excluyen los que son
particiones secuenciales legítimas (CHARLA REPLANTEO 1/2, SESION FALLADA 1/2/3, sesion gap parte 1/2/3,
documentacion claude 1-5.zip, transcripcion parte 1/2) — esos NO se tocan como si fueran duplicados.

Los 16 casos de `07_fuentes_documentacion` están espejados 1:1 en `_CUARENTENA_DUPLICADOS/fuentes de
documentacion (subcopia anidada)` — mismo hash, mismo problema, misma decisión sirve para ambos.

Marcá tu decisión en la columna final cuando tengas el ZIP conmigo y hayamos abierto el contenido real.

---

## Grupo A — Root del ZIP y `01_logs_replanteo/` (fuera de 07_fuentes_documentacion)

| # | Archivo base | Variantes | Tamaños | ¿Divergente? | Decisión |
|---|---|---|---|---|---|
| 1 | `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` | ` 2.md` vs base (aparece 2 veces: root y logs_replanteo, mismos hashes) | 14832B vs 14476B | Sí — hash distinto | pendiente |
| 2 | `SESSION_LOG_REPLANTEO_2026-06-19.md` | ` 2.md` vs base | 12518B vs 7623B | Sí | pendiente |
| 3 | `SESSION_LOG_REPLANTEO_2026-06-20.md` | ` 3.md` = ` 4.md` (idénticos) vs ` 5.md` | 12879B(x2) vs 16083B | Sí (2 de 3 son duplicado exacto, el 3ro diverge) | pendiente |
| 4 | `SESSION_LOG_REPLANTEO_2026-07-03.md` | ` 2.md` vs base | 20368B vs 16314B | Sí | pendiente |

## Grupo B — `05_corpus_B_crudo/`

| # | Archivo base | Variantes | Tamaños | ¿Divergente? | Decisión |
|---|---|---|---|---|---|
| 5 | `documentacion claude.zip` | claude 1..5.zip | 1.65/2.12/1.89/1.91/1.67 MB | **No es colisión real** — son 5 exports distintos por diseño (1 a 5), no duplicados de nombre. No tocar. | n/a |

## Grupo C — `07_fuentes_documentacion/fuentes de documentacion/` (espejado en cuarentena)

| # | Archivo base | Variantes | Tamaños | ¿Divergente? | Decisión |
|---|---|---|---|---|---|
| 6 | `IRAM_C1_s4_draft_s30.md` | `(2).md` vs base | 11991B vs 11748B | Sí | pendiente |
| 7 | `IRAM_paper_metodologia_v1_0.md` | `(1).md` vs base | 20390B vs 24362B | **Sí — crítico** (ya señalado en el log: enfoques/cifras distintas) | pendiente |
| 8 | `IRAM_skill_desarrollo_ia_v2_0.md` | `(2)=(3).md` (idénticos) vs base | 5237B(x2) vs 4381B | Sí | pendiente |
| 9 | `PROMPT_DOCUMENTACION_IRAM_v1_9.md` | `(2)=(4)=(1).md` (idénticos, 25827B) vs `(3).md`=base (idénticos, 24418B) | En realidad 2 contenidos, no 5 | Sí, pero solo 2 versiones reales entre 5 copias | pendiente |
| 10 | `SESION FALLADA.md` | 1/2/3 | 25629/77455/64134B | **No es colisión real** — partes secuenciales. No tocar. | n/a |
| 11 | `SESSION_LOG_ANALISIS_C1_2026-06-18_v2.md` | `(2).md` vs base | 20422B vs 15024B | Sí | pendiente |
| 12 | `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO.md` | `(2).md`, `(1).md`, base | 7757/9242/10426B | **Sí — el más crítico**: 3 hashes distintos entre sí, ninguno coincide | pendiente |
| 13 | `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO_s11.md` | `(2)=base` (idénticos, 14376B) vs `(3).md` (8940B) | Sí, 2 versiones reales | pendiente |
| 14 | `SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s13.md` | `(1).md` vs `(2)=(3).md` (idénticos) | 14434B vs 15974B(x2) | Sí, 2 versiones reales | pendiente |
| 15 | `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19.md` | `(2).md` vs base | 37388B vs 36840B | Sí | pendiente |
| 16 | `correccion de documentacion.md` | `2.md` vs base | 25908B vs 22334B | Sí | pendiente |
| 17 | `failed.md` | **trampa de nomenclatura**: `(2)=(3).md` (idénticos, 5337B) vs `3.md` sin paréntesis (181781B, muy distinto) vs base (6091B) | 3 contenidos reales entre 4 copias | **Sí — crítico**, cuidado con `(3)` ≠ `3` | pendiente |
| 18 | `s fallada 12-06.md` | `2.md` vs base | 25274B vs 57228B | Sí | pendiente |
| 19 | `sesion gap v4.1 - 4.3 parte.md` | parte 1/2/3 | 169391/4913/50461B | **No es colisión real** — partes secuenciales. No tocar. | n/a |
| 20 | `spec_c_zip_history.py` | `(2)=(3)=(4).py` (idénticos) vs base | 10594B(x3) vs 11052B | Sí, 2 versiones reales (código) | pendiente |
| 21 | `transcripcion de SESSION_LOG_CONSOLIDADO_2026-06-18 parte.md` | parte 1/2 | 11823/29061B | **No es colisión real** — partes secuenciales. No tocar. | n/a |

---

## Resumen de casos que SÍ requieren revisión manual (contenido real distinto)

**13 casos únicos** (los del Grupo C se cuentan una sola vez pese a estar espejados en cuarentena):
\#1, #2, #3, #4, #6, #7, #8, #9, #11, #12, #13, #14, #15, #16, #17, #18, #20 → son 17 filas de tabla,
pero #7, #12 y #17 son los de mayor impacto (contenido de fondo distinto, no cosmético).

**Prioridad de revisión sugerida:**
1. `IRAM_paper_metodologia_v1_0.md` (#7) — afecta la cifra "441 conversaciones / 7.313 mensajes" ya en uso
2. `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO.md` (#12) — 3 hashes distintos, ninguno de referencia
3. `failed.md` / `failed 3.md` (#17) — trampa de nomenclatura, riesgo de borrado accidental de 181KB únicos
4. Resto en el orden que prefieras

**Confirmado que NO son colisiones reales** (partes secuenciales o exports por diseño): #5, #10, #19, #21 — no tocar.

---

*Envía el ZIP del proyecto y abro el contenido real de cada fila pendiente, empezando por la prioridad 1, para que decidas cuál versión conservar (o si hace falta fusionar).*

---

## RESUELTOS — contenido real ya revisado (2026-07-06, sesión de continuidad)

### #7 — `IRAM_paper_metodologia_v1_0.md` vs `(1).md`
**Conclusión: son DOS REDACCIONES PARALELAS distintas del mismo paper, no borrador/versión final.**
- `(1).md` (20390B): título "IRAM: Desarrollo de software con IA sin dominar programación", 12 secciones, tono más de estudio de caso académico.
- base `.md` (24362B): título "Desarrollo técnico sostenido con IA: lecciones de un mod de videojuego", estructura distinta (5 secciones numeradas diferente), foco más narrativo en la arquitectura de documentación multisesión.
- **Corrección al hallazgo anterior sobre cifras**: no es un error entre versiones. Ambos documentos, *cada uno por separado*, usan dos cifras distintas para dos mediciones distintas: **7.345** (total post-deduplicación, en su propia tabla) vs **7.313** (subconjunto con timestamp individual analizable, en su sección de hallazgos). El "7.300" de la intro de la base es solo un redondeo de 7.345, no una tercera cifra real.
- **Decisión pendiente tuya**: ¿fusionar (la base tiene mejor narrativa de arquitectura de documentación; (1) tiene mejor marco de "tres condiciones de transferibilidad" con más detalle), o elegir una como C1 definitivo y archivar la otra como material de referencia?

### #12 — `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO` (3 versiones)
**Conclusión: NO son 3 alternativas sin orden — hay una secuencia cronológica clara, y el nombre engaña.**
- **`(2).md`** (7757B) = Sesión 5, primera pasada de Plantilla D Bloque 2. Concluye que las cuentas eran "genuinamente paralelas" (conclusión que se revierte después). Genera `IRAM_analisis_cuantitativo` v1.
- **`(1).md`** (9242B) = el más nuevo de los tres: "Sesión 6", **corrige** el error metodológico de la sesión 5 (Bloque 2 medía timestamps de inicio de sesión en vez de timestamps de mensaje individual). Conclusión correcta: rotación secuencial, no paralela. Marca v1 del análisis cuantitativo como obsoleta, genera v2.
- **Base `.md`** (10426B, sin sufijo) = en realidad **el más viejo de los tres**, no el vigente: no menciona `IRAM_analisis_cuantitativo` en absoluto, Plantilla D todavía no se había ejecutado.
- **Decisión recomendada**: `(1).md` es la versión con la información correcta y más avanzada. La base y (2) documentan pasos intermedios ya superados — podrían archivarse como historial del proceso pero **no deberían tratarse como la fuente de verdad vigente**. Revisar si en el PROMPT_MAESTRO u otro documento quedó citada la conclusión errónea de "cuentas paralelas" antes de esta corrección.

### #17 — `failed.md` / `failed (2).md` = `(3).md` / `failed 3.md`
**Conclusión: NO son variantes del mismo contenido — son 3 extractos de conversación distintos y genuinamente valiosos, cada uno de un momento distinto del proyecto.**
- `failed.md` (6091B): qué documentación revisar antes de escribir el esqueleto de C1 (prioriza ARCHIVE sección 19 y hitos v7).
- `failed (2).md` = `(3).md` (5337B, idénticos entre sí): sugerencias de estructura de sesiones — un entregable declarado por sesión, tabla de 4 sesiones propuestas (17: esqueleto, 18-19: draft, 20: revisión).
- `failed 3.md` (181781B, **sin paréntesis** — la trampa real de nomenclatura): extracto mucho más largo y posterior, trabaja "correcciones de criterio" cruzando paper v1.0 vs skill v2.0, termina con 3 ajustes concretos al esqueleto de C1 (tiering como hallazgo 4D, resolución de la circularidad criterio-preexistente/habilidades-entrenadas, "razón-junto-con-la-decisión" con lugar propio).
- **Decisión recomendada**: los 4 archivos son materialmente distintos y **ninguno es descartable como duplicado**. `failed 3.md` en particular tiene el ajuste de esqueleto más reciente detectado hasta ahora en todo el proyecto.

### #6 — `IRAM_C1_s4_draft_s30.md` vs `(2).md`
**Conclusión: `(2).md` es una revisión posterior (draft s32) que corrige la base (draft s30).**
La base deja pendiente "INC-13 — verificar contra SESSION_LOG v5.6"; `(2).md` dice explícitamente "INC-13 verificado y corregido en s32", con el párrafo técnico reescrito con detalle correcto del engine (`trigger_event`, `immediate`).
**Decisión recomendada:** `(2).md` es la vigente.

### #8 — `IRAM_skill_desarrollo_ia_v2_0.md` vs `(2)=(3).md`
**Conclusión: dos redacciones paralelas de la misma skill v2.0, mismo patrón que el paper (#7).**
Ambas tienen `version: 2.0` en el frontmatter pero estructura y enfoque distintos.
**Decisión pendiente tuya:** fusionar o elegir una y archivar la otra.

### #9 — `PROMPT_DOCUMENTACION_IRAM_v1_9.md` (2 contenidos entre 5 copias)
**Conclusión: la versión de 25827B es una revisión estrictamente superior a la de 24418B (base).**
La versión larga agrega un "PRINCIPIO GENERAL" nuevo y le agrega la razón causal a cada regla existente — no quita nada.
**Decisión recomendada:** usar la versión de 25827B como vigente.

### #11 — `SESSION_LOG_ANALISIS_C1_2026-06-18_v2.md` vs `(2).md`
**Conclusión: `(2).md` (20422B) es simplemente más completo que la base (15024B) — sin conflicto.**
`(2).md` tiene todo el contenido de la base más una sección adicional entera.
**Decisión recomendada:** `(2).md` es la vigente.

### #13, #14, #15 — Serie `SESSION_LOG_DOCUMENTACION_..._CONSOLIDADO_sNN` (s11, s13, s19)
**Conclusión: redacciones paralelas del resumen de la misma sesión, con matices de estado distintos.**
s11: una versión llama a C2 "✅ VIGENTE completo"; la otra "❌ PENDIENTE". Probablemente la que dice PENDIENTE es correcta — coincide con `plan.md`, que hoy dice "Skill C2 no existe". s13 y s19: diferencias menores sin contradicción de fondo.

### #16 — `correccion de documentacion.md` vs `2.md`
Dos extractos de conversación de momentos distintos (mismo patrón que #17), no duplicado. Conservar ambos.

### #18 — `s fallada 12-06.md` vs `2.md`
Mismo patrón: dos extractos distintos y secuenciales, no duplicado.

### #20 — `spec_c_zip_history.py` (código)
**Hallazgo crítico: la base (11052B) es la versión CORREGIDA; las copias `(2)=(3)=(4)` (10594B) tienen el bug sin corregir.**
La base incluye el comentario "BUG-C1 (corregido en Sesión 2, 2026-06-19)": la regex vieja capturaba mal nombres como "v5_5_2026-06-09" → "v5.5.2026".
**Decisión recomendada: conservar la base; NO usar (2)(3)(4) para re-analizar.**

---

## Resumen ejecutivo del Paso 0 (tras revisión de contenido real)

| # | Caso | Tipo de divergencia | Acción recomendada |
|---|---|---|---|
| 6 | C1_s4_draft_s30 | corrección posterior | usar `(2).md` |
| 7 | paper_metodologia | redacciones paralelas | tu decisión: fusionar o elegir |
| 8 | skill_desarrollo_ia_v2_0 | redacciones paralelas | tu decisión: fusionar o elegir |
| 9 | PROMPT_DOCUMENTACION_v1_9 | revisión superior | usar versión 25827B |
| 11 | ANALISIS_C1_v2 | ampliación, no conflicto | usar `(2).md` |
| 12 | CONSOLIDADO 06-12 | secuencia cronológica | usar `(1).md`, archivar resto |
| 13 | CONSOLIDADO_s11 | estado C2 contradictorio | confirmar (probable: PENDIENTE) |
| 14 | CONSOLIDADO_s13 | diferencias menores | sin acción urgente |
| 15 | CONSOLIDADO_s19 | diferencias menores | sin acción urgente |
| 16 | correccion de documentacion | extractos complementarios | conservar ambos |
| 17 | failed.md / failed 3.md | 4 extractos distintos, todos valiosos | conservar los 4 |
| 18 | s fallada 12-06 | extractos complementarios | conservar ambos |
| 20 | spec_c_zip_history.py | bug corregido vs sin corregir | usar la base |

**Ningún caso de los 13 revisados con contenido real resultó ser un duplicado seguro de borrar.**

---

## Grupo A resuelto — root del ZIP y `01_logs_replanteo/`

### #1 — `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` (root y logs_replanteo, mismos hashes)
**`2.md` (14832B) es la vigente.** Agrega verificación de un tercer zip de backup (`DOCUMENTACION.zip`, 18/18 archivos confirmados idénticos por diff) que la base (14476B) no llegó a cubrir. Amplía la conclusión de DR-33 sin contradecir nada.

### #2 — `SESSION_LOG_REPLANTEO_2026-06-19.md`
**`2.md` (12518B) es la vigente.** Agrega dos categorías de hallazgo nuevas (DR-08 "costo narrativo no solicitado", DR-09 "acción sin autorización") y una sección completa de "Investigación de novedad" ausente en la base (7623B).

### #3 — `SESSION_LOG_REPLANTEO_2026-06-20.md` (3=4 idénticos, 5 diverge)
**`5.md` (16083B) es la vigente.** Reorganiza y corrige la metodología de categorización de la sesión anterior (3=4, 12879B); incluso marca una afirmación previa como "(estimación sin fuente)" — autocorrección explícita, buena señal.

### #4 — `SESSION_LOG_REPLANTEO_2026-07-03.md`
**`2.md` (20368B) es la vigente — hallazgo importante.** Agrega:
- **DR-22**: reconstruye con cita exacta el origen del error "democratización" en el marco teórico, y confirma que **`failed_3.md`** (el archivo de 181KB de la trampa de nomenclatura, §17 arriba) es precisamente donde se detectó por primera vez ese error sin que llegara a corregirse en la WIKI oficial — confirma independientemente que ese archivo tiene contenido único e insustituible.
- **DR-23**: los gaps de conocimiento del mod (`IRAM_gaps_conocimiento_2026-06-12.md`) ya están mapeados — no rehacer ese trabajo.
- **Fecha de entrega confirmada de la diplomatura UTN: 15/07/2026** — dato operativo que no aparece en la versión base ni, hasta donde se revisó, en `plan.md`.
- **El antecedente directo de DR-54**: la "Tarea 0" de esta versión ("definir todos los criterios de forma y fondo pendientes... antes de tocar los ZIPs o el pipeline", con los dos puntos sin resolver: "criterio de cierre de fase A/B" y "nota de vínculo diplomatura↔pipeline") es, con altísima probabilidad, el origen textual de lo que el plan posterior nombró DR-54. Vale la pena confirmarlo al resolver DR-54.

---

## Resumen ejecutivo actualizado — TODOS los grupos de contenido divergente revisados

| # | Caso | Vigente / decisión |
|---|---|---|
| 1 | REPLANTEO_07-03_17-58 | `2.md` |
| 2 | REPLANTEO_06-19 | `2.md` |
| 3 | REPLANTEO_06-20 | `5.md` |
| 4 | REPLANTEO_07-03 | `2.md` — **contiene antecedente de DR-54 y fecha de entrega 15/07** |
| 6 | C1_s4_draft_s30 | `(2).md` |
| 7 | paper_metodologia | tu decisión (fusionar o elegir) |
| 8 | skill_desarrollo_ia_v2_0 | tu decisión (fusionar o elegir) |
| 9 | PROMPT_DOCUMENTACION_v1_9 | versión 25827B |
| 11 | ANALISIS_C1_v2 | `(2).md` |
| 12 | CONSOLIDADO 06-12 | `(1).md` |
| 13 | CONSOLIDADO_s11 | confirmar estado real de C2 (probable: PENDIENTE) |
| 14 | CONSOLIDADO_s13 | sin acción urgente |
| 15 | CONSOLIDADO_s19 | sin acción urgente |
| 16 | correccion de documentacion | conservar ambos |
| 17 | failed.md / failed 3.md | conservar los 4 — confirmado contenido único e insustituible |
| 18 | s fallada 12-06 | conservar ambos |
| 20 | spec_c_zip_history.py | usar la base (corregida) |

**Los 17 grupos de contenido genuinamente divergente están todos revisados. Ninguno es un duplicado seguro de borrar sin decisión.**

---

## HALLAZGO NUEVO — no detectado en ninguna auditoría anterior: prueba de "fuga de memoria"

Al revisar los 23 archivos sueltos de la raíz del ZIP contra la lista que el session log ya conocía, aparecen **3 archivos no mencionados en ningún log previo** (ni el session log del 06-07, ni el chat de auditoría de continuidad):

- `instruccion_prueba_fuga_memoria.md` — plantilla de instrucción para hacer que cada cuenta (claude_1 a claude_5) vuelque su memoria de conversaciones pasadas ANTES de mirar los archivos reales, y luego cruce ese volcado contra el material documentado, clasificando cada afirmación como ✅ CONFIRMADO / ⚠️ DESACTUALIZADO / 🚨 FUGA.
- `volcado_memoria.md` = `volcado_memoria (2).md` (idénticos): el Paso 1 ya ejecutado en la cuenta claude.ai — memoria recordada sin mirar archivos.
- `resultado_prueba_fuga_memoria.md`: el Paso 2 — cruce de esa memoria contra el ZIP real.
- `memoria_claude_volcado.md`: un volcado de memoria **distinto y más extenso** (157 líneas), fechado 2026-07-03, que parece ser de otra sesión/cuenta, con memoria persistente inyectada por Anthropic (no solo memoria conversacional) y termina con **6 preguntas explícitas de cruce sin responder**.

### Resultado de la prueba ya ejecutada (`resultado_prueba_fuga_memoria.md`)
**2 fugas reales confirmadas, ambas sobre la pieza UTN/Portafolio** (la única de las tres piezas del proyecto sin ningún artefacto físico todavía, según DR-27):
1. La afirmación de que "Módulos 1-4 (16 unidades) de la diplomatura ya están verificados completos y reorganizados" — **no tiene respaldo en ningún documento real**. Las Consignas describen 5 módulos, no 16 unidades.
2. La convención de nombres `ModuloN_UnidadM_Tema_Corto.md` para archivos UTN — **tampoco está documentada en ningún lugar**. Existe solo en la memoria de Claude.

### Lo que queda pendiente y no se hizo
- **DR-30** (correr la misma prueba en las 5 cuentas del corpus, claude_1 a claude_5) — según el propio archivo, **"no ejecutada todavía"**. Es la prueba que de verdad mediría si el sistema de documentación es suficiente, porque esas cuentas trabajaron directamente en el proyecto (a diferencia de la cuenta claude.ai, cuya alta coincidencia era esperable por haber participado en la generación del log).
- **Las 6 preguntas de cruce de `memoria_claude_volcado.md`** nunca se respondieron contra el material real:
  1. ¿La corrección "5 cuentas secuenciales, no paralelas" está propagada en `PROMPT_MAESTRO R18` y `Plantilla D Block 2`? (parcialmente respondida por hallazgo #12 de este checklist: la corrección SÍ existe en `(1).md` del CONSOLIDADO 06-12, pero no se confirmó si se propagó al PROMPT_MAESTRO)
  2. ¿El problema DC-06 (mislabel de "democratización" como claim central) sigue abierto? (parcialmente respondida por DR-22, hallazgo del grupo #4 arriba: sí se corrigió en un draft de Sección 3, pero la WIKI oficial nunca se actualizó)
  3. ¿Los "tres patrones operativos nunca antes documentados" (tiering, techo operacional por sesión, "lenguaje de Claude" como comandos secuenciales) ya se incorporaron a algún documento, o siguen solo en memoria?
  4. ¿El estado S5 ❌ del paper C1 (bloqueado por datos cuantitativos) sigue así?
  5. ¿La corrección "SKILL v1.0 no es la base estructural — es el esqueleto de s17" está reflejada consistentemente, o quedó alguna referencia vieja?
  6. ¿DC-08 Sesión 2 (ejecución de scripts A/B/C) ya se corrió?

**Esto es un hueco de auditoría real que ninguna sesión anterior (ni la del 05-07 ni la del 06-07, hasta donde se cortó) llegó a cubrir.** Vale la pena sumarlo a los próximos pasos, posiblemente con más prioridad que algunos de los grupos ya resueltos arriba, porque apunta a fugas de información activas, no solo a archivos duplicados.

---

## Revisión de ZIPs anidados — resultado

Se extrajo el ZIP completo (2382 archivos, coincide exactamente con el conteo de todos los logs previos) y se verificaron los 21 zips anidados uno por uno.

**Confirmado, sin novedades respecto a lo ya documentado:**
- Los 5 `data-*-batch-0000.zip` (Corpus A crudo) y sus copias en cuarentena — código/historial crudo, consistente.
- Los 4 `mod_pack_IRAM_v4_3_*.zip` y el `mod_pack_v5_5` — código/assets legacy del mod, nada narrativo.
- Los 2 `.zip` únicos de `mod_pack_IRAM_v5_5` que solo viven en `_CUARENTENA_DUPLICADOS/` — **confirmado nuevamente**: el contenido extraído sí sobrevive en `1_MOD/IRAM mod v5/` como carpeta, pero los `.zip` originales no existen en ningún otro lado. Riesgo real si se borra la cuarentena entera sin extraerlos antes.

**Resuelto — pendientes de logs anteriores:**
- **`claude_N_processed.json` (Corpus A, 5 archivos) — CONFIRMADO como procesamiento real y completo**, no crudo sin tocar. Esto resuelve DR-47: cada archivo tiene `total_conversations`, `total_messages`, `total_dups_removed`, `date_range` y un diccionario `hito_first_seen` con hitos ya extraídos por cuenta (ej. `primer_prompt_maestro`, `primera_wiki`, `separacion_active_archive`). **No es una tarea pendiente — ya está hecho.**
- **`Consigna.md` vs `Consigna.pdf` (y `_1`, `_2`) — CONFIRMADO idénticos en texto**, verificado extrayendo el PDF con `pdfplumber` y comparando contra el .md línea por línea. El .md es transcripción fiel con formato markdown agregado; sin divergencias de contenido en los 3 pares.
  - **Dato relevante para la fuga #10 de arriba:** las Consignas confirman que la diplomatura tiene **2 entregas sobre 5 módulos** (Entrega 1: Módulos 1-3; Entrega 2: Módulos 4-5) — no "16 unidades" como afirmaba la memoria de Claude marcada como fuga. Confirma independientemente que esa afirmación de "16 unidades" no tiene respaldo real en ningún lado del proyecto.
- **Las 5 `documentacion claude N.zip` (Corpus B) — CONFIRMADO que siguen crudas, sin procesar**: contienen `conversations.json` + `users.json` + `projects/*.json` en formato export estándar de Claude, sin ningún processed.json equivalente al de Corpus A. Consistente con todo lo documentado — Corpus B es la única pieza real que falta procesar del pipeline de análisis.

**No se encontró ningún archivo o zip adicional fuera de los ya catalogados en el session log del 06-07.** El único hallazgo genuinamente nuevo de esta ronda es la prueba de fuga de memoria (arriba), que no es un problema de ZIPs sino de archivos sueltos en la raíz que ningún log anterior había señalado.
