# FUENTE DE VERDAD — Proyecto IRAM / Documentación / Diplomatura UTN
**Fecha de consolidación:** 2026-07-07
**Reemplaza como punto de partida operativo a:** toda la serie `SESSION_LOG_REPLANTEO_*` (DR-01 a DR-54), los 3 borradores de plan (`Qwen_markdown_20260705_q4xkzeqjf.md`, `deepseek_markdown_20260705_98aa15.md`/`(1).md`, `plan.md` v1.3), y los 2 logs de auditoría de continuidad (`SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` y `...-07.md`).
**Método:** cotejo línea por línea de las 4 fuentes citadas arriba contra el ZIP `IRAM_PROYECTO_REORGANIZADO_carpeta_raiz.zip` (33 archivos de logs/planes, sin la estructura `1_MOD/2_DOCUMENTACION/...` — ver §0 sobre esta limitación). Regla de consolidación aplicada: **append-only estricta (DR-42)** — ninguna decisión anterior se reescribe; donde dos fuentes contradicen, se cita ambas y se marca cuál rige y por qué.

**Este documento es, de acá en adelante, el único punto de partida.** No cargar la serie `SESSION_LOG_REPLANTEO_*` completa, no cargar los 3 borradores de plan por separado, no cargar los 2 logs de auditoría de continuidad como si fueran el estado vigente. Todos quedan como evidencia histórica citable por ID, no como insumo a releer entero.

> **VERSIÓN _3 (2026-07-07, mismo día que _2) — banner de versión, sin tocar contenido heredado.**
> Esta versión agrega §10 (RECONCILIACIÓN CRÍTICA #5 — cierre del Paquete A) y §11 (estado de los paquetes de debate tras la sesión del 2026-07-07) al final del documento, siguiendo la regla append-only (DR-42): ninguna palabra de §0–§9 de la versión `_2` se reescribe. El disparador fue el debate del Paquete A (§9), que verificó contra el ZIP completo — no solo los 33 archivos que tuvo esta consolidación (ver §0) — que DC-06 ya está resuelto en el origen (DR-22) y solo faltaba trasladarlo a `WIKI_DOCUMENTACION_v2.md`. Ese traslado se ejecutó como `WIKI_DOCUMENTACION_v3.md`, documento hermano de esta versión. Ver §10 para el detalle completo y la justificación de por qué esto no viola DR-12.

---

## 0. ADVERTENCIA SOBRE EL MATERIAL DISPONIBLE PARA ESTA CONSOLIDACIÓN

El ZIP adjuntado para esta consolidación (`IRAM_PROYECTO_REORGANIZADO_carpeta_raiz.zip`) contiene **solo 33 archivos de logs y planes**, todos sueltos en la raíz — **no** la estructura física completa del proyecto (`1_MOD/`, `2_DOCUMENTACION/`, `3_PORTAFOLIO_UTN/`, `_CUARENTENA_DUPLICADOS/`, 2382 archivos) que la auditoría de continuidad del 06/07-07 sí tuvo. Este documento consolida **la cadena de decisiones y planes**, no vuelve a verificar el estado físico del ZIP completo — para eso siguen rigiendo `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` y `...-07.md` como última verificación física confirmada (§6 de este documento la resume).

---

## 1. LÍNEA DE TIEMPO REAL — TODAS LAS FUENTES EN UNA SOLA CADENA

Reconstruida por contenido (no por nombre de archivo — varios nombres se repiten con contenido distinto). Fuente entre paréntesis.

| Fecha/hora | Evento | Fuente |
|---|---|---|
| hasta 06-19/06-20 | DR-01 a DR-09 (fundacionales) | `SESSION_LOG_REPLANTEO_2026-06-19_2.md` |
| 06-20 | DR-10 a... (metodología, Framework B, criterios) | `SESSION_LOG_REPLANTEO_2026-06-20_5.md` |
| 07-03 02:43 | DR-10 a DR-26 (Tarea 0, criterio de cierre, DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO) | `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` |
| 07-03 17:47 | Borrador intermedio de DR-27-30, **descartado formalmente (DR-40)** | `..._17-47.md` — no citar |
| 07-03 17:58 (sin sufijo) | Versión con cita rota, **no usar (DR-39)** | `..._17-58.md` — no citar |
| 07-03 17:58 "2" | DR-27 a DR-33 (estructura de carpetas, DR-29 prueba de memoria cuenta claude.ai, DR-30 pendiente, nomenclatura, DR-32 plan 3 capas, DR-33 zips anidados) — **versión canónica** | `..._17-58 2.md` |
| 07-04, antes de 23:17 | Prueba de fuga de memoria repetida en cuenta claude.ai (Paso 1/Paso 2 separados): **2 fugas reales confirmadas**, ambas sobre UTN/Portafolio | `volcado_memoria.md`, `resultado_prueba_fuga_memoria.md` |
| 07-04 23:17 | **DR-34: cierre de DR-30.** Prueba en las 5 cuentas del corpus. `claude_1`-`claude_4`: negativo limpio. `claude_5`: memoria activada/desactivada sin borrar → propagación de info desactualizada a otro chat de la misma cuenta (mecanismo distinto de DR-30) | `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` |
| 07-04 23:44 | Auditoría de continuidad #1: DR-35 (2 tareas perdidas en el salto 02-43→17-58), DR-36 (detalle de bugs del mod comprimido), DR-37 (mismo mecanismo de fuga ya ocurrido antes en otra serie, con regla de prevención nunca portada), DR-38 (regla de consolidación adoptada — versión débil) | `..._23-44.md` |
| 07-05 00:10 | Auditoría de continuidad #2: DR-39 (corrige cita de 17-58), DR-40 (descarta 17-47), **DR-41 (ID formal a las 2 fugas de UTN/Portafolio)**, DR-42 (corrige cita de origen de DR-38 y **restaura la regla append-only original, más estricta**), **DR-43 (causa raíz: contaminación de memoria en `claude_5` filtró la convención de nombres a otro proyecto — no verificable con material disponible, no genera tarea)**, DR-44 (encuadra el caso como evidencia citable para C1) | `..._00-10.md` |
| 07-05 00:32 | DR-45 (`DOCUMENTACION/` es respaldo exacto de `fuentes de documentacion/`), DR-46 (clasificación inicial, luego corregida), DR-47 (`claude_N_processed.json` existen, sin abrir), DR-48 (mod pack mezclado en carpeta de docs), DR-49 (archivos "instrucción" revisados, sin peso operativo) | `..._00-32.md` |
| 07-05 00:52 | **DR-50 (corrige DR-46: los 5 `data-*.zip` son Corpus A, no B)**, **DR-51 (estructura física de carpetas aplicada — `IRAM_PROYECTO_REORGANIZADO.zip` + `LOG_REORGANIZACION_2026-07-05.md`)** | `..._00-52.md` |
| 07-05 01:37 | **DR-52 (encuadre corregido: C1/C2 son productos del objetivo 2, auxiliares del objetivo 3, no "usos parejos")**, **DR-53 (cierra la nota de vínculo diplomatura↔pipeline pendiente desde 02-43)**, **DR-54 (bloqueante nuevo: no hay mapeo entre el diseño de métricas y el formato que exige Consigna 1 UTN)** | `..._01-37.md` |
| 07-05 02:12/02:13 | Borrador de plan v1.0 (DeepSeek), cortado en la sección 3 | `deepseek_markdown_20260705_98aa15.md` / `(1).md` |
| 07-05 03:58 | Plan integrado v1.1 (Qwen) — primera versión completa de las 5 fases | `Qwen_markdown_20260705_q4xkzeqjf.md` |
| 07-05 04:30 | **Plan integrado v1.3 (`plan.md`) — vigente hasta esta consolidación.** Agrega nota crítica: DTI/FCC son propuestas conceptuales nuevas de la charla del 07-05, no hallazgos documentados previamente; agrega Tarea 1.7 para buscar evidencia de su origen | `plan.md` |
| 07-05/06 | Reorganización aplicada, inventario completo (1991 archivos con esa base) | `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`, `LOG_REORGANIZACION_2026-07-05.md` |
| 07-06 | **Auditoría de continuidad #3 (cuenta distinta, sin memoria previa):** conteo real del ZIP sube a **2382 archivos** (no 1991 — la diferencia son ZIPs que nunca se habían abierto: 5 `data-*.zip`, mod packs legacy). 43 grupos de colisión de nombre confirmados. **Esta auditoría no cita ni una vez la serie `SESSION_LOG_REPLANTEO_*`** — trabajó solo con las transcripciones `IRAM_PROYECTO_REORGANIZADO_*.md` y el ZIP | `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` |
| 07-06/07 | Paso 0: apertura de contenido real de los 17 grupos de colisión con hash distinto. Hallazgo nuevo: prueba de fuga de memoria adicional (`memoria_claude_volcado.md`, 157 líneas) con **6 preguntas de cruce, de las cuales 4 siguen sin responder** — este volcado **no está conectado a la cadena DR-01→DR-54** en ningún log que exista | `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-07.md`, `PASO_0_grupos_divergentes_checklist.md` |

---

## 2. RECONCILIACIÓN CRÍTICA #1 — Las dos ramas de logs no se cruzaron nunca

**Hallazgo estructural de esta consolidación:** la serie `SESSION_LOG_REPLANTEO_*` (DR-01 a DR-54, la que diseña el plan de trabajo) y la serie `SESSION_LOG_AUDITORIA_CONTINUIDAD_*` (la que verifica el ZIP físico) **corrieron en paralelo sin leerse entre sí**. Evidencia:
- La auditoría de continuidad del 07-06 trató DR-30 (fuga de memoria en las 5 cuentas) como si nunca se hubiera ejecutado. **Ya estaba cerrada desde el 07-04 23:17 (DR-34).**
- Las 2 fugas reales de UTN/Portafolio que la auditoría de continuidad presenta el 07-07 como "hallazgo nuevo" **ya estaban documentadas, con ID formal, desde el 07-05 00:10 (DR-41)**.
- El archivo `memoria_claude_volcado.md` (157 líneas, con 6 preguntas de cruce) que aparece en la auditoría de continuidad **no está citado en ningún `SESSION_LOG_REPLANTEO`** — es de origen desconocido dentro de esta cadena.

**Regla nueva para prevenir que se repita (candidato a próximo DR, ver §5):** ninguna sesión de auditoría o de planeamiento debe declarar un ítem "pendiente" o "hallazgo nuevo" sin, como primer paso, grep del ID o del tema en **toda** la cadena disponible — no solo en la rama de la que parte. Esto es una instancia directa del mismo mecanismo ya diagnosticado en DR-37 (fuga de continuidad entre logs) y DR-42 (regla de consolidación), pero a nivel de series completas, no de sesiones consecutivas dentro de una serie.

---

## 3. RECONCILIACIÓN CRÍTICA #2 — Estado real de la fuga de memoria (cierre completo)

| Pregunta | Respuesta consolidada | Fuente |
|---|---|---|
| ¿DR-30 está cerrada? | **Sí, desde 07-04 23:17 (DR-34).** No pendiente. | `23-17.md` |
| ¿Qué encontró DR-34? | `claude_1`-`claude_4`: sin fugas (memoria persistente nunca activada). `claude_5`: memoria activada/desactivada sin borrar → propagó info desactualizada a otro chat de la misma cuenta. **No es una fuga tipo DR-30** — es contaminación cruzada por mal manejo de memoria, mecanismo distinto (regla explícita en QUÉ NO HACER de varios logs: no mezclar ambos). | `23-17.md` |
| ¿Cuál es la causa raíz del efecto en nombres de archivo (`ModuloN_UnidadM_Tema_Corto.md`)? | DR-43: contaminación de memoria de `claude_5` en una charla sin relación con IRAM (debate diplomatura/portfolio) hizo que Claude nombrara archivos de la diplomatura como si fueran de IRAM. **No verificable con el material disponible** (el zip de `claude_5` no llega a la fecha de esa charla) — diagnosticado por relato directo del operador, no por evidencia documental. No genera tarea de verificación. | `00-10.md` |
| ¿`claude_5` quedó limpiado? | **El operador confirma en esta conversación que ya se limpió.** Pero **ningún log de la cadena registra ese cierre** — el punto 5 de "próximas tareas" ("confirmar que la memoria quedó desactivada y borrar el residuo") sigue apareciendo como opcional/no bloqueante/sin resolver en los 4 logs posteriores a DR-34 que existen (`23-44`, `00-10`, `00-32`, `00-52`, `01-37`). **Se registra ahora, en este documento, como el cierre formal** (ver tabla de decisiones nuevas, §5). |
| ¿Las 2 fugas de UTN/Portafolio (Módulos "16 unidades", convención `ModuloN_UnidadM...`) siguen vigentes como fugas confirmadas? | Sí — DR-41 las cierra con ID formal. No hay nada en ningún log posterior que las revierta. | `00-10.md` (DR-41), `resultado_prueba_fuga_memoria.md` |
| ¿Qué pasa con `memoria_claude_volcado.md` (157 líneas, 6 preguntas)? | **Sin resolver — no conectado a la cadena.** No aparece citado en ningún `SESSION_LOG_REPLANTEO`. De sus 6 preguntas de cruce, 2 tienen respuesta parcial (ver tabla siguiente) y 4 siguen abiertas. No se sabe de qué cuenta/sesión salió. | `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-07.md` |

### Las 6 preguntas de `memoria_claude_volcado.md` — estado tras esta consolidación

| # | Pregunta | Estado |
|---|---|---|
| 1 | ¿"5 cuentas secuenciales, no paralelas" propagado a `PROMPT_MAESTRO R18` y `Plantilla D Block 2`? | Parcial — el Paso 0 checklist confirma que la corrección de "cuentas paralelas→secuenciales" existe en `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO_(1).md`, pero no se confirmó si llegó al PROMPT_MAESTRO. **Sigue como tarea abierta (§5).** |
| 2 | ¿DC-06 (mislabel "democratización") sigue abierto? | Parcial — DR-22 (citado en el Paso 0 checklist, caso #4) ubica dónde se detectó el error, pero no confirma si la WIKI oficial se corrigió. **Sigue abierta.** |
| 3 | ¿Los "tres patrones operativos" (tiering, techo operacional, "lenguaje de Claude") ya incorporados? | Sin responder. Solo el tiering está confirmado (DR-29, sección 4D del paper). Los otros dos, sin dato en ningún log de esta cadena. |
| 4 | ¿Estado S5 ❌ del paper (bloqueado por datos cuantitativos) sigue así? | Sin responder — ningún log de esta cadena lo confirma o lo niega directamente. **Nota: `plan.md` v1.3 sí lo trata como pendiente** ("Paper C1: CERRADO en s34, pero con S4A y S5 sin respaldo cuantitativo — pendiente de corrección"), así que la respuesta probable es "sigue así", pero no está verificado contra el paper mismo. |
| 5 | ¿"SKILL v1.0 no es la base — es el esqueleto de s17" reflejado consistentemente? | Sin auditar de forma exhaustiva. El Paso 0 checklist confirma revisiones de documentos relacionados (casos #6, #9) pero no una auditoría específica de esta afirmación puntual. |
| 6 | ¿DC-08 Sesión 2 (ejecución de scripts A/B/C) ya se corrió? | Sin responder en ningún log. **Nota: el plan nuevo (Qwen/DeepSeek/plan.md) no usa el nombre "DC-08" ni "Spec A/B/C" — reformula todo el diseño del análisis desde DR-54 con nombres y estructura distintos (tabla única, columnas, EDA).** Es altamente probable que estas preguntas pertenezcan al plan viejo, truncado por el episodio de memoria, y que el plan nuevo las haya vuelto obsoletas de hecho sin decirlo explícitamente. **Se marca así en §5, sin darlo por cerrado sin confirmación tuya.** |

---

## 4. RECONCILIACIÓN CRÍTICA #3 — Plan viejo vs. plan nuevo, punto por punto

El "plan viejo" es el diseño de análisis que vive en `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (sección "DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO", Framework B, Grupos 1/2/3) más las menciones sueltas a DC-06/DC-08/Spec A-B-C en `memoria_claude_volcado.md`. El "plan nuevo" es la cadena Qwen v1.1 → DeepSeek v1.0 (más corto, antecesor) → **`plan.md` v1.3 (vigente)**.

| Punto | Plan viejo (pre-DR-54) | Plan nuevo (`plan.md` v1.3) | ¿Reconciliado? |
|---|---|---|---|
| Objetivos/productos | DR-11/DR-25/DR-26: C1, C2 y portfolio como "tres usos parejos" del análisis | DR-52: C1 y C2 son productos del **objetivo 2**, auxiliares del objetivo 3 (no un tercer/cuarto producto de rango propio). Orden de dependencia obligatorio: pipeline → corrige C1/C2 → alimenta UTN/Portafolio | **Sí — DR-52 corrige explícitamente el encuadre de DR-11/26 sin reescribirlas.** `plan.md` ya lo refleja (§2-3 del plan). |
| Bloqueante único | Tarea 0 con 2 sub-puntos (criterio de cierre + nota de vínculo diplomatura↔pipeline) | DR-53 cierra la nota de vínculo. DR-54 identifica un bloqueante **nuevo y distinto**: falta el mapeo entre el diseño de métricas y el formato de Consigna 1 UTN | **Sí — DR-54 es el bloqueante vigente, ya lleva su Fase 0 completa en `plan.md`.** El sub-punto "umbrales concretos del criterio B" de la Tarea 0 vieja **sigue sin resolver** y no aparece explícitamente en `plan.md` — queda reincorporado en §5. |
| Estructura de datos (Spec A/B/C, DC-08) | 3 specs de investigación (autoría, democratización, Sección 21) + 3 sesiones (diseño→ejecución→síntesis) | Una única `tabla_analisis.csv`, con columnas fijas (`id`, `corpus`, `fase`, `origen_propuesta`, `nivel_friccion`, etc.), generada en la Fase 1 con `process_iram_v2.py` + `exportar_tabla_analisis.py` | **No hay reconciliación explícita en ningún log — es un rediseño completo, no una evolución citada.** El plan nuevo no menciona ni descarta formalmente Spec A/B/C ni DC-08. Queda como tarea abierta en §5: confirmar si el plan nuevo reemplaza al viejo por completo o si algo de Spec A/B/C sigue teniendo valor (p. ej. Spec B, "trazado del principio de democratización", se solapa con DC-06/DR-22, que sigue sin cerrar). |
| Conceptos DTI/FCC | No existen en el plan viejo | Aparecen en DeepSeek/Qwen v1.1 tratados casi como hallazgos ya documentados; **`plan.md` v1.3 los corrige explícitamente como "propuestas conceptuales nuevas generadas en la conversación del 2026-07-05, NO documentadas en historiales previos"**, con Tarea 1.7 dedicada a buscar evidencia de su origen | **Ya reconciliado dentro del propio plan nuevo** (v1.1→v1.3 es la corrección). Nota: esto es la misma clase de error que motivó DR-41/DR-43 (tratar una idea generada en el momento como si tuviera respaldo documental previo) — vale la pena que la Tarea 1.7 lo tenga presente como precedente. |
| Cifra de conversaciones/mensajes | Memoria (`memoria_claude_volcado.md`) dice "441 conversaciones, 7.345 mensajes" | `plan.md`/Qwen no citan esta cifra directamente; el Paso 0 checklist (caso #7) sí confirma **7.345** (total post-dedup) y **7.313** (subconjunto con timestamp) como cifras correctas, ambas usadas en el paper de metodología | **Parcialmente reconciliado** — la cifra sobrevive en el Paso 0, pero ningún documento conecta explícitamente esa verificación con la sección 6 de `memoria_claude_volcado.md` que originó la pregunta. |
| Skill C2 | "NO EXISTE — pendiente de generación", ligada a Tabla de análisis | Igual en `plan.md` (Fase 4, Tarea 4.6) — sin cambios de fondo, solo de posición en el flujo (ahora depende de DR-54 resuelto) | **Sí, coherente.** |
| Fecha de entrega diplomatura | `SESSION_LOG_REPLANTEO_2026-07-03.md` versión `2.md` (ver Paso 0, caso #4): **15/07/2026** confirmado | `plan.md`: "Próximo hito crítico: Entrega Parte 1 UTN → 2026-07-15" | **Sí, coincide.** |
| Estructura física de carpetas | DR-27 diseñada, DR-51 aplicada (04/05-07) — cuenta 1991 archivos | `plan.md` Anexo A: mismo árbol, mismo conteo (1991, 241, 6, 424) | **Desactualizado por la auditoría de continuidad del 06-07**, que confirma el conteo real es **2382** (1545/264/6/544 + 23 sueltos). Ni `plan.md` ni ningún log de la serie REPLANTEO lo reflejan — ver §6. |

---

## 5. TABLA ÚNICA DE TAREAS PENDIENTES — consolidada y priorizada

*(Formato append-only: cada fila cita su origen. Nada se inventa nuevo salvo lo explícitamente marcado "NUEVO — esta consolidación".)*

| # | Tarea | Bloqueante? | Origen | Estado |
|---|---|---|---|---|
| 1 | **Resolver DR-54**: unidad de fila, columnas, 3 preguntas de EDA, enfoque de ML — sesión dedicada, con propuesta preliminar ya escrita en `01-37.md` y refinada en `plan.md` Fase 0 | **Sí — bloquea todo lo demás** | DR-54, `plan.md` Fase 0 | Abierta — propuesta preliminar sin confirmar |
| 2 | Ejecutar Fase 1 del plan nuevo (procesar Corpus A/B → `tabla_analisis.csv`) | Depende de #1 | `plan.md` Fase 1 | Bloqueada por #1 |
| 3 | Tarea 1.7: buscar origen documental de DTI/FCC en los 5 JSONs de Corpus B (grep semántico) — confirmar o refutar que son propuestas nuevas sin precedente | No bloqueante, pero condiciona cómo se presentan en el paper | `plan.md` Tarea 1.7 | Abierta |
| 4 | Reconciliar Spec A/B/C y DC-08 del plan viejo contra el plan nuevo — **¿el plan nuevo los reemplaza del todo, o Spec B (democratización) sigue teniendo valor porque se solapa con DC-06/DR-22 sin cerrar?** | No bloqueante | **NUEVO — esta consolidación**, ver §4 | Abierta |
| 5 | Responder las 4 preguntas sin resolver de `memoria_claude_volcado.md` (#1, #3, #4, #5 de la tabla en §3) — o, alternativamente, confirmar que el plan nuevo las vuelve obsoletas y descartarlas formalmente con nota explícita | No bloqueante | Auditoría de continuidad 07-07, esta consolidación | Abierta — **requiere tu confirmación de si siguen siendo relevantes** |
| 6 | Confirmar si DC-08 Sesión 2 se corrió alguna vez (pregunta #6 de `memoria_claude_volcado.md`) | No bloqueante, probablemente obsoleta por el rediseño de DR-54/plan nuevo | ídem | Abierta, candidata a cerrar como "absorbida por el plan nuevo" |
| 7 | **Registrar formalmente el cierre de `claude_5`** (memoria confirmada desactivada, residuo borrado) — el operador confirma que ya se hizo, pero ningún log lo registra | No bloqueante | **NUEVO — esta consolidación**, confirmado por el operador en este chat el 2026-07-07 | **Se marca CERRADO en este documento** (ver nota abajo) |
| 8 | Sub-punto "umbrales concretos del criterio B" de la Tarea 0 vieja (DR-26) — nunca se resolvió, y no aparece en `plan.md` | No bloqueante | `02-43.md`, nunca cerrado en ningún log posterior | Abierta — **posiblemente absorbida por DR-54 (columnas/preguntas de la tabla), a confirmar en la sesión dedicada de #1** |
| 9 | Ejecutar plan de 3 capas de DR-32 sobre `07_fuentes_documentacion/` (mapa de vigencia → citas cruzadas → renombrado) | No bloqueante | DR-32, `plan.md` Fase 5 Tarea 5.1 | Abierta |
| 10 | Decidir destino de `_CUARENTENA_DUPLICADOS/` (borrar o conservar) — **ahora son 544 archivos, no 424** (ver §6) | No bloqueante | DR-51, `plan.md` Fase 5 Tarea 5.2, actualizado por auditoría 06-07 | Abierta |
| 11 | Decidir qué representan `claude_1_processed.json` a `claude_5_processed.json` | No bloqueante | DR-47/50 | **Cerrada por la auditoría de continuidad 07-07**: confirmado como procesamiento real y completo (resuelve DR-47) |
| 12 | Inventario terminológico completo (ACM/arXiv/IEEE/etc.) | No bloqueante | DR-35a, `plan.md` Fase 5 Tarea 5.3 | Abierta |
| 13 | Verificación de cifras de hitos (cita de línea exacta en `hitos_v7`) | No bloqueante | DR-35b, `plan.md` Fase 5 Tarea 5.4 | Abierta |
| 14 | Decidir los 2 pares de redacciones paralelas del Paso 0 (`paper_metodologia`, `skill_desarrollo_ia_v2_0`) — ¿fusionar o elegir? | No bloqueante | Paso 0 checklist, casos #7 y #8 | Abierta |
| 15 | Confirmar estado real de Skill C2 en `CONSOLIDADO_s11` (contradicción "VIGENTE" vs "PENDIENTE") | No bloqueante | Paso 0 checklist, caso #13 | Abierta — probable: PENDIENTE (coincide con `plan.md`) |
| 16 | **Actualizar `plan.md` y toda referencia a "1991 archivos" al conteo real confirmado (2382)** | No bloqueante para el análisis, sí para no citar datos obsoletos | **NUEVO — esta consolidación**, ver §6 | Abierta |
| 17 | Archivar los `SESSION_LOG_REPLANTEO_*` sueltos en `01_logs_replanteo/` (puede que ya esté hecho por DR-51 — confirmar contra el estado físico real) | No bloqueante | Auditoría de continuidad 06-07 | Abierta — a confirmar |

**Nota sobre la tarea #7 (cierre de `claude_5`):** el operador confirmó en esta conversación (2026-07-07) que la limpieza ya se realizó. Como ningún `SESSION_LOG_REPLANTEO` lo registra, este documento asienta el cierre aquí mismo, de forma explícita, cumpliendo la regla append-only: **no se reescribe ninguna entrada anterior sobre `claude_5` (DR-34, DR-43 siguen vigentes tal cual están) — se agrega esta confirmación como nueva pieza de estado, fechada 2026-07-07, por relato directo del operador, sin evidencia documental de la interfaz** (mismo estándar de trazabilidad que DR-43 ya usó para el diagnóstico de causa raíz).

---

## 6. RECONCILIACIÓN CRÍTICA #4 — Estado físico real del ZIP vs. lo que dice el plan

Confirmado por `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` (última verificación física real que existe, con comandos ejecutados contra el ZIP adjunto en esa sesión — no heredado de texto pegado):

| Métrica | Plan nuevo (`plan.md`, Anexo A, basado en DR-45–51) | Estado físico real confirmado (07-06) |
|---|---|---|
| Archivos totales | 1991 | **2382** |
| `1_MOD/` | 1320 | **1545** |
| `2_DOCUMENTACION/` | 241 | **264** |
| `3_PORTAFOLIO_UTN/` | 6 | 6 (sin cambios) |
| `_CUARENTENA_DUPLICADOS/` | 424 | **544** |
| Sueltos en raíz | no contemplados en el Anexo A | 23 |

**Causa de la diferencia (ya explicada en la auditoría de continuidad, no es una discrepancia sin resolver):** ZIPs que el inventario original (DR-45–49, base de `plan.md`) nunca abrió — los 5 `data-*.zip` de Corpus A, los 4 `mod_pack_IRAM_v4_3_*` y las copias de `mod_pack_v5_5` se extrajeron **después** de que `plan.md` se escribiera, pero `plan.md` nunca se actualizó para reflejarlo. **Ningún documento "vigente" (ni `plan.md` ni ningún `SESSION_LOG_REPLANTEO`) tiene el número correcto** — es una fuga de continuidad más, de la misma familia que DR-35/37/39, pero entre la serie REPLANTEO y la serie de auditoría de continuidad, no dentro de una sola serie.

**Estado de los 17 grupos de colisión (Paso 0):** confirmado y cerrado por `PASO_0_grupos_divergentes_checklist.md` — ninguno es un duplicado seguro de borrar. Resumen ya consolidado en la tabla de tareas §5 (#14, #15) para los 2 casos que requieren tu decisión.

**Hallazgo de "fuga de memoria" adicional de la auditoría de continuidad (4 archivos sueltos en la raíz del ZIP, sección 3 de `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-07.md`):** `instruccion_prueba_fuga_memoria.md`, `volcado_memoria.md`/`(2).md`, `resultado_prueba_fuga_memoria.md`, y `memoria_claude_volcado.md`. **Los primeros 3 ya están completamente integrados a la cadena principal en este documento (§3).** El cuarto (`memoria_claude_volcado.md`, 157 líneas) es el que queda sin resolver — ver tarea #5 de §5.

---

## 7. REGLAS ANTI-FUGA DE CONTINUIDAD — consolidadas y ampliadas

*(Todas las reglas `QUÉ NO HACER` de la serie REPLANTEO siguen vigentes sin excepción — no se listan todas de nuevo aquí por espacio, están íntegras en la cadena citada en §1. Esta sección solo agrega las reglas nuevas que esta consolidación identifica como faltantes.)*

**Reglas ya existentes, más relevantes para lo que pasó en esta cadena:**
- **(DR-42, la vigente sobre DR-38)** Al agregar contenido nuevo a un log o documento de estado, nunca reescribir celdas de tabla existentes — solo agregar al final, marcando explícitamente resuelto/descartado/absorbido con el ID que lo resuelve. Esta es la regla que este mismo documento sigue.
- **(DR-39)** Verificar duplicados con sufijo numérico antes de asumir cuál archivo es el vigente.
- **(DR-37)** Un log largo con mucho contenido nuevo es el escenario de mayor riesgo de comprimir/perder detalle al reescribir el estado de memoria en vez de cotejar ítem por ítem.

**Reglas nuevas, agregadas por esta consolidación:**
- **(NUEVO-1)** Antes de declarar cualquier ítem "pendiente" o "hallazgo nuevo", grep del ID/tema en **todas** las series de logs existentes (REPLANTEO y AUDITORIA_CONTINUIDAD por igual), no solo en la serie de la que parte la sesión actual. Esto previene lo que pasó con DR-30/DR-34 (§2).
- **(NUEVO-2)** Cuando dos series de documentación paralelas (p. ej. planeamiento vs. auditoría física) coexisten, cada una debe citar explícitamente, al abrir, si consultó o no a la otra serie — aunque sea para decir "no aplica a esta sesión". Un silencio total sobre la otra serie (como pasó con la auditoría de continuidad y DR-30/34/41) debe tratarse como señal de alerta, no como omisión inocua.
- **(NUEVO-3)** Toda cifra de conteo físico (archivos totales, por carpeta) citada en un documento de planeamiento debe llevar fecha de verificación. Si ese documento se sigue usando después de una nueva verificación física con cifra distinta, se marca explícitamente desactualizado en la próxima versión — no basta con que la cifra nueva exista en otro documento sin que el primero la referencie.
- **(NUEVO-4)** Cuando una idea o concepto surge dentro de una conversación (p. ej. DTI/FCC), su primera mención en cualquier plan debe llevar la fecha y el marcador explícito "generado en esta sesión, sin precedente documental confirmado" — el error de tratar a DTI/FCC como si ya estuvieran documentados (v1.1 Qwen) es de la misma familia que las fugas de memoria DR-41/43 (tratar una construcción reciente como si tuviera respaldo histórico que no tiene).

---

## 8. PRÓXIMO PASO INMEDIATO

Sin cambios respecto a lo que ya decía `plan.md`: **iniciar la sesión dedicada para resolver DR-54** (tarea #1 de §5) — es el único bloqueante real que impide avanzar con Fase 1 (procesamiento), Fase 2/3 (entregas UTN, con fecha límite 15/07/2026 ya encima) y Fase 4 (Paper C1 corregido + Skill C2).

Antes de esa sesión, materiales a releer completos (no solo el resumen de este documento):
- `Consigna_1.md` y `Consigna_2.md`
- Sección "DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO" de `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (Framework B completo)
- La propuesta preliminar de DR-54 en `SESSION_LOG_REPLANTEO_2026-07-05_01-37.md`, refinada en `plan.md` Fase 0

En paralelo, sin bloquear lo anterior, quedan las decisiones tuyas explícitas pendientes de §5: tareas #4, #5, #6, #8, #10, #14, #15 — ninguna es bloqueante, pero varias (#4, #5, #8) tocan directamente el diseño que se va a cerrar en la sesión de DR-54, así que conviene tenerlas resueltas o al menos descartadas explícitamente antes de esa sesión, no después.

---

## 9. PAQUETES DE DEBATE — para abrir en un chat nuevo, uno por vez o todos juntos

Cada paquete de abajo es **autocontenido**: trae el contexto necesario para debatir esa decisión puntual a fondo sin tener que releer el resto de este documento ni la cadena de logs original. Si abrís un chat nuevo por espacio de contexto, podés pegar un paquete individual (o varios) sin perder nada esencial. Cada uno cierra con una pregunta concreta a resolver, no con una tarea abierta genérica.

---

### PAQUETE A — ¿Spec A/B/C y DC-08 (plan viejo) quedan reemplazados del todo por la tabla única del plan nuevo?

**Contexto:** el plan viejo (memoria de la cuenta claude.ai, sección 3 de `memoria_claude_volcado.md`) diseñaba el análisis como una arquitectura de 3 sesiones (DC-08): Sesión 1 diseñaba 3 specs de investigación —Spec A (análisis de autoría), Spec B (trazado del principio de "democratización"), Spec C (completar Sección 21 de la wiki)—, Sesión 2 los ejecutaba mecánicamente, Sesión 3 sintetizaba. Nunca se confirmó si la Sesión 2 se corrió.

El plan nuevo (`plan.md` v1.3, vía DR-54) descarta esa arquitectura sin mencionarla ni una vez: en su lugar diseña una única `tabla_analisis.csv` con columnas fijas (`id`, `corpus`, `fase`, `origen_propuesta`, `nivel_friccion`, etc.), generada con dos scripts (`process_iram_v2.py`, `exportar_tabla_analisis.py`).

**Por qué importa:** Spec B ("trazado del principio de democratización") es, por contenido, el mismo tema que DC-06/DR-22 — el error de mislabeling donde la wiki dice que "la IA no democratiza la programación" es el claim central del paper, cuando el paper no dice eso. DR-22 (citado en el Paso 0 checklist, caso #4) ya ubicó **dónde** se detectó ese error (en `failed_3.md`), pero nunca se confirmó si la corrección llegó a la WIKI oficial. Si Spec B se abandona sin más, esa verificación puede quedar huérfana — nadie la va a hacer porque "ya no es parte del plan", pero tampoco está resuelta.

**Lo que no sabemos:** si el diseño de la tabla única del plan nuevo *cubre* lo que Spec B iba a responder (probablemente sí, vía la columna `presencia_DR08`/`texto_evidencia`), o si hace falta una tarea explícita aparte para cerrar DC-06.

**Pregunta a resolver:** ¿la tabla única resuelve DC-06 como efecto colateral, o hace falta agregar una tarea explícita (tipo "Tarea 1.8: verificar si la corrección de DC-06 llegó a la WIKI oficial") al plan nuevo?

---

### PAQUETE B — Las 4 preguntas sin responder de `memoria_claude_volcado.md`: ¿siguen siendo relevantes o son parte del plan truncado?

**Contexto:** `memoria_claude_volcado.md` es un volcado de memoria de 157 líneas, fechado 2026-07-03, que **no está citado en ningún `SESSION_LOG_REPLANTEO`** de la cadena DR-01→DR-54 — apareció recién en la auditoría de continuidad del 07-07, de origen no identificado (posiblemente otra cuenta o sesión que nunca se integró). Termina con 6 preguntas de cruce; 2 tienen respuesta parcial, 4 no:

1. ¿Los "tres patrones operativos nunca documentados" (tiering, "techo operacional por sesión", "lenguaje de Claude como comandos secuenciales") ya se incorporaron a algún documento? Solo el tiering está confirmado (sección 4D del paper, vía DR-29). Los otros dos, sin dato.
2. ¿El estado S5 ❌ del paper (bloqueado por datos cuantitativos) sigue así? `plan.md` v1.3 lo trata como pendiente ("S4A y S5 sin respaldo cuantitativo"), pero nadie lo confirmó contra el paper mismo.
3. ¿La corrección "SKILL v1.0 no es la base — es el esqueleto de s17" está reflejada consistentemente en todos los documentos? Sin auditar de forma exhaustiva.
4. ¿DC-08 Sesión 2 (ejecución de los scripts Spec A/B/C) ya se corrió? Ver Paquete A — es altamente probable que esta pregunta ya no aplique porque el plan nuevo reemplazó esa arquitectura.

**Por qué importa:** si el plan viejo quedó completamente truncado por el episodio de fuga de memoria (como confirmaste vos mismo) y el plan nuevo (Qwen→DeepSeek→`plan.md`) es una reconstrucción independiente y no una continuación literal, es razonable que estas preguntas hayan quedado obsoletas de hecho. Pero eso nunca se declaró explícitamente en ningún log — nadie dijo "esta pregunta ya no aplica porque X".

**Pregunta a resolver:** para cada una de las 4 preguntas — ¿se responde ahora con lo que ya sabemos (aunque sea "sin dato, no bloqueante"), se agenda como tarea explícita del plan nuevo, o se descarta formalmente con una nota de "absorbida por el rediseño de DR-54/plan nuevo, ya no aplica"?

---

### PAQUETE C — Dos redacciones paralelas sin fusionar: `IRAM_paper_metodologia_v1_0.md` y `IRAM_skill_desarrollo_ia_v2_0.md`

**Contexto (del Paso 0 checklist, casos #7 y #8):**

**Caso #7 — paper de metodología.** Dos versiones bajo el mismo nombre, con hash distinto, que son **dos redacciones completas y genuinamente distintas**, no borrador/final:
- `(1).md` (20390B): título "IRAM: Desarrollo de software con IA sin dominar programación", 12 secciones, tono de estudio de caso académico. Tiene mejor marco de "tres condiciones de transferibilidad", más detallado.
- base `.md` (24362B): título "Desarrollo técnico sostenido con IA: lecciones de un mod de videojuego", estructura distinta, foco narrativo en la arquitectura de documentación multisesión. Mejor narrativa de esa arquitectura.
- Ambas usan correctamente dos cifras distintas para dos mediciones distintas (7.345 total post-dedup, 7.313 subconjunto con timestamp) — no hay error de cifras entre ellas, eso ya se descartó.

**Caso #8 — skill de desarrollo con IA v2.0.** Mismo patrón: dos versiones con `version: 2.0` en el frontmatter pero contenido y organización distintos.

**Por qué importa:** esto es material directo para dos de los 4 productos del objetivo 2 (Paper C1 corregido, y potencialmente insumo de Skill C2) — no son duplicados descartables, cada versión tiene valor real que la otra no tiene.

**Pregunta a resolver, por cada caso:** ¿fusionar tomando lo mejor de cada versión, o elegir una como definitiva y archivar la otra explícitamente como material de referencia (no como descartada)? Si se fusiona, ¿quién hace la fusión — un pase de edición humano, o un pase de IA con instrucción explícita de qué tomar de cada lado?

---

### PAQUETE D — Estado real de la Skill C2 en `CONSOLIDADO_s11`: ¿"VIGENTE completa" o "PENDIENTE"?

**Contexto (del Paso 0 checklist, caso #13):** dos versiones de `SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s11.md` con hash distinto — una dice que la skill C2 está "✅ VIGENTE completa", la otra dice "❌ PENDIENTE". Contradicción directa, no matiz de redacción.

**Evidencia a favor de "PENDIENTE":** coincide con `plan.md` ("Skill C2: NO EXISTE — pendiente de generación") y con el encuadre de DR-52 (C2 es un producto del objetivo 2 que todavía no existe, se genera recién después de la base de hechos del objetivo 3).

**Lo que falta para cerrar esto con certeza:** abrir ambas versiones completas de `CONSOLIDADO_s11` y ver si una es simplemente más vieja que la otra (como pasó con el caso #12 del mismo Paso 0 — `CONSOLIDADO_2026-06-12`, donde el nombre sin sufijo resultó ser el más viejo de los tres, no el vigente). Ninguna sesión llegó a hacer ese cotejo puntual para `s11`.

**Pregunta a resolver:** ¿alguna de las dos versiones de `CONSOLIDADO_s11` tiene fecha de sesión o menciones cruzadas que permitan establecer cuál es más reciente? Si no, ¿se toma "PENDIENTE" como la vigente por default (coincide con `plan.md`) y se archiva la otra como error puntual de esa sesión?

---

### PAQUETE E — El sub-punto "umbrales concretos del criterio B" (Tarea 0 vieja, DR-26): ¿sigue vivo o lo absorbe DR-54?

**Contexto:** la Tarea 0 original (`SESSION_LOG_REPLANTEO_2026-07-03_02-43.md`) tenía dos sub-puntos: (a) criterio de cierre de fase, resuelto por DR-26 con un solo detalle suelto —los umbrales concretos del criterio B (% de cobertura del corpus, completitud de timestamps)— nunca definidos; (b) nota de vínculo diplomatura↔pipeline, cerrada recién por DR-53 (07-05 01:37).

El sub-punto (a) — los umbrales de B — **nunca se cerró explícitamente en ningún log posterior**, y no aparece mencionado por su nombre en `plan.md`. Pero DR-54 (el bloqueante vigente) diseña columnas y preguntas de EDA para la tabla de análisis que, por contenido, podrían ya cubrir lo que ese umbral iba a medir (cobertura de corpus, completitud de timestamps son justo el tipo de cosa que una columna `fecha_sesion` con control de nulos resolvería).

**Pregunta a resolver:** al cerrar la sesión dedicada de DR-54 (que ya está agendada como la prioridad #1), ¿conviene chequear explícitamente si las columnas/criterios que se definan ahí satisfacen lo que el criterio B pedía, y cerrar ese sub-punto ahí mismo citándolo? ¿O el criterio B mide algo distinto (calidad/rigor de cierre de fase) que ninguna columna de datos puede capturar, y necesita su propia definición aparte?

---

### PAQUETE F — Actualizar el conteo de archivos del plan (1991 → 2382) y decidir destino de `_CUARENTENA_DUPLICADOS/` con el número real

**Contexto:** `plan.md` (Anexo A) y toda la cadena DR-45–51 se basan en un conteo de **1991 archivos** que quedó desactualizado el 07-06, cuando la auditoría de continuidad confirmó **2382** (1545 en `1_MOD/`, 264 en `2_DOCUMENTACION/`, 6 en `3_PORTAFOLIO_UTN/`, **544** —no 424— en `_CUARENTENA_DUPLICADOS/`, más 23 sueltos en raíz). La causa ya está identificada y no es un misterio: son ZIPs (5 `data-*.zip`, mod packs legacy) que se extrajeron después de que el inventario original se escribiera, y ese inventario nunca se actualizó.

**Por qué importa junto con la decisión de cuarentena:** la Tarea 5.2 del plan nuevo ("decidir destino de `_CUARENTENA_DUPLICADOS/`, borrar o conservar") se decidió pensando en 424 archivos. Con 544 confirmados, y con el hallazgo de la auditoría de continuidad de que **2 de esos archivos no tienen gemelo fuera de la cuarentena** (las 2 copias de `mod_pack_IRAM_v5_5_2026-06-09_03-22.zip`, que solo existen ahí — aunque su contenido extraído sí sobrevive en `1_MOD/`), borrar la carpeta entera sin extraer esos 2 zips primero perdería el original, aunque no el contenido.

**Pregunta a resolver:** (1) ¿confirmás que se actualice `plan.md` con el conteo real 2382 antes de seguir citándolo? (2) Para la cuarentena — ¿se conserva indefinidamente (respaldo, sin costo real más allá de espacio), se borra completa una vez extraídos esos 2 zips huérfanos, o se define algún criterio intermedio (p. ej. conservar solo lo que no tiene gemelo)?

---

*(Fin de los paquetes de debate tal como estaban en la versión `_2`. Cualquiera de los 6 puede tratarse de forma completamente independiente de los demás — no hay dependencias entre A-F, salvo que E se resuelve más naturalmente durante la sesión de DR-54 ya agendada. Ver §10 y §11 para el estado del Paquete A tras el debate del 2026-07-07.)*

---

## 10. RECONCILIACIÓN CRÍTICA #5 — Cierre del Paquete A (debate 2026-07-07, contra el ZIP completo)

**Disparador:** el Paquete A (§9) quedó abierto en esta consolidación con la pregunta "¿la tabla única resuelve DC-06 como efecto colateral, o hace falta una tarea explícita?". Esta consolidación (§0) trabajó solo con 33 archivos sueltos, sin la estructura `1_MOD/2_DOCUMENTACION/...`. El debate del Paquete A sí tuvo el ZIP reorganizado completo y fue a verificar los hechos en vez de debatir en abstracto.

**Lo que se verificó, con cita y archivo exacto:**
- `IRAM_C1_final.md` (18/06 16:00, la versión más tardía del paper que existe en el proyecto) tiene **cero** menciones de "democratiza" en todo el archivo. Su Sección 3 se titula "El hallazgo central: la posición y el formato importan más que el contenido" (`grep -n "^## 3"` → línea 118).
- `WIKI_DOCUMENTACION_v2.md` (17/06 22:01 — no existe v3 en ningún lado del ZIP hasta esta versión) todavía tiene, línea 20-21, "PRINCIPIO CENTRAL DEL PAPER (definitivo): 'La IA no democratiza la programación...'" — el texto viejo, nunca actualizado.
- DR-22 (`SESSION_LOG_REPLANTEO_2026-07-03_02-43.md`) trae la cadena de origen completa del error, con hora exacta: el principio "democratiza" se fosilizó en el CONSOLIDADO del 12/06 sin la reserva de estilo con que se propuso originalmente (11/06 22:48); el 17/06 05:43-05:51 se detectó y escribió la "Corrección 1"; el draft de Sección 3 salió corregido el 17/06 16:18; **la WIKI nunca se actualizó**, aunque el paper sí quedó corregido desde ese mismo día.
- Hallazgo adicional, no citado por esta consolidación ni por la auditoría de continuidad: `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md` muestra que Spec A, B y C (plan viejo, DC-08) **sí se corrieron**. Spec B encontró cero ocurrencias reales de "democratización" en los 7.345 mensajes de las 5 cuentas — consistente con que la frase se fosilizó en un paso de redacción, no en una conversación real. Esto cierra la pregunta #6 del Paquete B (§9) con dato, no con "probablemente ya no aplica".

**Respuesta a la pregunta de cierre del Paquete A:** no hace falta una "Tarea 1.8" de investigación nueva — DR-22 ya es esa tarea, completa. Lo que faltaba era una tarea de *ejecución* ya especificada: aplicar la Corrección 1 de DR-22 a `WIKI_DOCUMENTACION`.

**Sobre DR-12 (bloqueo general de tocar la wiki hasta tener la base de hechos del análisis A/B):** se debatió si este párrafo puntual necesitaba esperar igual. Conclusión del debate: **no** — se trata como excepción documentada, no como derogación de DR-12. Razón: DR-12 existe para evitar corregir por apuro sin inventario completo (mismo principio que DR-07). Acá no hay apuro ni falta de inventario — DR-22 ya hizo el trabajo, con fecha y cita exacta, tres semanas antes de esta consolidación. El estándar aplicado a la excepción es el mismo que exige el resto del documento: cita exacta, fecha, ID propio, append-only. DR-12 **sigue vigente sin cambios** para el resto de `WIKI_DOCUMENTACION` — solo este párrafo puntual queda resuelto.

**Texto aplicado (ver `WIKI_DOCUMENTACION_v3.md`, documento hermano de esta versión):**

> **PRINCIPIO CENTRAL DEL PAPER (vigente):**
> "La posición y el formato dentro del contexto importan tanto como el contenido de una instrucción: una regla bien escrita, pero mal ubicada, compite por atención con todo lo que la rodea — y puede perder. El límite no es solo la calidad de la regla; es también la arquitectura de contexto que la sostiene."
> (Corregido 2026-07-07. Reemplaza el principio de "democratización". Cadena de origen: DR-22. Fuente del texto: `IRAM_C1_final.md`, Sección 3.)

Nota sobre la redacción: el paper (Sección 3) usa "más que" (jerarquía: posición sobre contenido). La wiki usa "tanto como" (igualdad: ambos son necesarios) por decisión explícita del operador en el debate del Paquete A — el argumento es que el propio mecanismo de documentación del proyecto (esta wiki incluida: el contenido correcto existía desde el 17/06, pero por estar en la posición equivocada del documento nunca se propagó al resumen) es evidencia viva de que forma y contenido son inseparables, no jerárquicos. Esto es una revisión de tesis, no una transcripción — queda marcado como tal, no como cita literal del paper.

**Tareas de §5 que este cierre resuelve o actualiza (append-only — no se reescriben las filas originales, se marca su resolución acá):**
- **Tarea #4** (reconciliar Spec A/B/C y DC-08 contra el plan nuevo): resuelto por partes, no como bloque. Spec A (autoría) — su esquema de codificación se parece al de la columna `origen_propuesta` de `tabla_analisis.csv`; queda absorbida por la tabla nueva. Spec B (democratización) — no absorbida por la tabla, pero tampoco hace falta: la investigación ya está hecha (DR-22), solo faltaba ejecutarla por escrito — **ejecutado en esta sección**. Spec C (Sección 21 / historia de zips) — apunta a completar la wiki técnica del mod, algo que `tabla_analisis.csv` no cubre; sigue huérfana, necesita tarea propia si importa.
- **Tarea #5 / pregunta #2 de `memoria_claude_volcado.md`** (§3): pasa de "Parcial... sigue abierta" a **cerrada en el origen** (DR-22, con cita y hora completas), pendiente solo la escritura — que ya se ejecutó en `WIKI_DOCUMENTACION_v3.md`.
- **Tarea #6 / pregunta #4 de Paquete B** ("¿DC-08 Sesión 2 se corrió?"): pasa de "no bloqueante, probablemente obsoleta" a **cerrada con dato**: sí corrió, en `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md`, rama no citada por esta consolidación ni por la auditoría de continuidad.

---

## 11. ESTADO DE LOS PAQUETES DE DEBATE TRAS LA SESIÓN DEL 2026-07-07

| Paquete | Estado tras esta sesión |
|---|---|
| A | **Cerrado.** Ver §10. `WIKI_DOCUMENTACION_v3.md` generado con la corrección aplicada. |
| B | **Parcialmente cerrado.** Pregunta #4 resuelta con dato (ver §10). Preguntas #1, #2, #3 siguen abiertas — no se debatieron en esta sesión. |
| C | Sin debatir en esta sesión. Sigue como en §9. |
| D | Sin debatir en esta sesión. Sigue como en §9. |
| E | Sin debatir en esta sesión. Sigue como en §9. |
| F | Sin debatir en esta sesión. Sigue como en §9. |

**Archivos generados por esta sesión, pendientes de reemplazar sus versiones anteriores en el proyecto real:**
- `WIKI_DOCUMENTACION_v3.md` — reemplaza a `WIKI_DOCUMENTACION_v2.md` en `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/` (y su respaldo espejo en `08_documentacion_respaldo/DOCUMENTACION/`, según DR-45).
- `FUENTE_DE_VERDAD_IRAM_2026-07-07_3.md` (este archivo) — reemplaza como punto de partida operativo a la versión `_2`.

**Pendiente explícito, no ejecutado todavía (requiere confirmación del operador antes de tocar el ZIP real):** ninguno de los dos archivos de arriba fue insertado de vuelta en `IRAM_PROYECTO_REORGANIZADO2.zip` — existen solo como archivos sueltos generados en esta sesión. Si se confirma el fix, falta decidir si se reemplaza el ZIP completo o se entregan los dos archivos sueltos para que el operador los coloque manualmente.

**Próximo paso sugerido:** continuar con las 3 preguntas restantes de Paquete B (los tres patrones operativos, el estado real de S5, la corrección del esqueleto de s17), u otro paquete a elección — ninguno depende de A ni de B.

---

## 12. PROCESO DE LAS 4 CHARLAS QUE PRODUJERON EL CIERRE DEL PAQUETE A — meta-registro de continuidad

**Por qué existe esta sección:** el propio cierre del Paquete A (§10) diagnostica un patrón de fuga de continuidad entre sesiones (dos series de logs que corrieron en paralelo sin leerse, §2). El proceso que produjo §10/§11 sufrió una instancia menor del mismo patrón — vale la pena documentarlo con el mismo estándar que el resto de este archivo, no dejarlo implícito.

**Charla 1 — apertura del debate.** El operador subió el ZIP completo (`IRAM_PROYECTO_REORGANIZADO2.zip`) más `FUENTE_DE_VERDAD_IRAM_2026-07-07_2.md` y pidió "debatamos A". A diferencia de la consolidación original (§0: solo 33 archivos sueltos), esta sesión tuvo acceso al árbol físico completo (`1_MOD/`, `2_DOCUMENTACION/`, etc.) y fue a verificar los hechos del Paquete A directamente contra los archivos en vez de debatir en abstracto. Resultado: se estableció que DC-06 está resuelto en el origen (cadena DR-22 completa, con hora exacta), que `WIKI_DOCUMENTACION_v2.md` nunca heredó la corrección, y se descubrió `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md` — una tercera rama no citada por esta consolidación ni por la auditoría de continuidad, donde Spec A/B/C sí se ejecutaron. La charla terminó con una pregunta abierta al operador: si el bloqueo general de DR-12 debía aplicar igual a este párrafo puntual, dado que DR-22 ya había hecho el trabajo de verificación.

**Charla 2/3 — misma sesión, continuación (charla_3 es la misma charla_2 pegada de nuevo, truncada antes del final).** El operador confirmó el criterio de excepción documentada a DR-12, y pidió además un cambio de fondo: reemplazar "más que" (jerarquía, tal como dice el paper) por **"tanto como"** (igualdad) en el principio central, con el argumento de que todo el aparato de documentación del proyecto — incluida esta misma wiki, cuyo contenido correcto existía desde el 17/06 pero nunca se propagó por estar en la posición equivocada — es evidencia viva de que forma y contenido son inseparables, no jerárquicos. Con eso, la sesión pidió armar los archivos necesarios para continuar en otra conversación antes de perder contexto. Se construyeron `WIKI_DOCUMENTACION_v3.md` y `FUENTE_DE_VERDAD_IRAM_2026-07-07_3.md` en `/home/claude/build/`, aplicando el fix con "tanto como" y preparando el banner de versión y las secciones §10/§11 nuevas. La charla_3 corta justo cuando se iba a redactar el contenido final de esas secciones — el estado exacto de avance en el momento del corte no quedó confirmado.

**Fuga de continuidad detectada:** los archivos construidos en charla 2/3 vivían solo en `/home/claude/build/` de esa sesión — un directorio de trabajo efímero, no en el ZIP ni subido como adjunto. Al abrirse una charla nueva, ese trabajo no estaba disponible. Es la misma clase de pérdida que este documento ya diagnostica en otros puntos (§2, "ninguna sesión de auditoría o planeamiento debe declarar algo sin grep primero en toda la cadena disponible") — acá el equivalente sería "ningún archivo de trabajo generado en sesión debe considerarse persistente hasta que se suba o se adjunte explícitamente".

**Charla 4 — reconstrucción.** Detectada la pérdida (los archivos de charla 2/3 no estaban disponibles), se verificó contra el ZIP que solo existe `WIKI_DOCUMENTACION_v2.md` (confirmado de nuevo en esta sesión — ver comando `unzip -l` filtrado por "WIKI_DOCUMENTACION|FUENTE_DE_VERDAD", que muestra `v1` y `v2` únicamente, en `07_fuentes_documentacion` y su espejo `08_documentacion_respaldo`). Se reconstruyeron ambos archivos desde cero, aplicando exactamente lo decidido en charla 2/3, incluyendo el ajuste "tanto como". El operador pidió además, al cierre, actualizar esta fuente de verdad detallando el proceso de las charlas reconstruidas — lo que se ejecuta en esta misma sección.

**Esta sesión (continuación de charla 4) — verificación final y esta sección.** Se releyeron las 4 charlas y ambas versiones de la fuente de verdad (`_2` y `_3`) en orden, se confirmó una vez más contra el ZIP que la reconstrucción de charla 4 es fiel byte a byte a `WIKI_DOCUMENTACION_v2.md` real (mismo tamaño, 12364 bytes, mismo timestamp 2026-06-17 22:01), y se redactó esta §12 para cerrar el registro de las 4 charlas con el mismo estándar de cita y fecha que exige el resto del documento.

**Estado de los archivos entregables, sin cambios respecto a §11:** `WIKI_DOCUMENTACION_v3.md` y esta misma `FUENTE_DE_VERDAD_IRAM_2026-07-07_3.md` siguen existiendo solo como archivos sueltos — **no reinsertados en el ZIP real**. Esa decisión sigue pendiente de confirmación del operador.

---

*Este documento reemplaza como punto de partida operativo a toda la cadena citada en el encabezado. Se mantiene la regla append-only (DR-42) hacia adelante: la próxima actualización de este documento debe cotejar ítem por ítem contra esta versión, no reescribir de memoria.*
