# FUENTE DE VERDAD — Proyecto IRAM / Documentación / Diplomatura UTN
**Fecha de consolidación:** 2026-07-07
**Reemplaza como punto de partida operativo a:** toda la serie `SESSION_LOG_REPLANTEO_*` (DR-01 a DR-54), los 3 borradores de plan (`Qwen_markdown_20260705_q4xkzeqjf.md`, `deepseek_markdown_20260705_98aa15.md`/`(1).md`, `plan.md` v1.3), y los 2 logs de auditoría de continuidad (`SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` y `...-07.md`).
**Método:** cotejo línea por línea de las 4 fuentes citadas arriba contra el ZIP `IRAM_PROYECTO_REORGANIZADO_carpeta_raiz.zip` (33 archivos de logs/planes, sin la estructura `1_MOD/2_DOCUMENTACION/...` — ver §0 sobre esta limitación). Regla de consolidación aplicada: **append-only estricta (DR-42)** — ninguna decisión anterior se reescribe; donde dos fuentes contradicen, se cita ambas y se marca cuál rige y por qué.

**Este documento es, de acá en adelante, el único punto de partida.** No cargar la serie `SESSION_LOG_REPLANTEO_*` completa, no cargar los 3 borradores de plan por separado, no cargar los 2 logs de auditoría de continuidad como si fueran el estado vigente. Todos quedan como evidencia histórica citable por ID, no como insumo a releer entero.

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

*Este documento reemplaza como punto de partida operativo a toda la cadena citada en el encabezado. Se mantiene la regla append-only (DR-42) hacia adelante: la próxima actualización de este documento debe cotejar ítem por ítem contra esta versión, no reescribir de memoria.*
