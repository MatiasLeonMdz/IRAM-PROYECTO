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
