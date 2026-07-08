# FUENTE DE VERDAD — Proyecto IRAM / Documentación / Diplomatura UTN
**Fecha de consolidación:** 2026-07-07
**Reemplaza como punto de partida operativo a:** toda la serie `SESSION_LOG_REPLANTEO_*` (DR-01 a DR-54), los 3 borradores de plan (`Qwen_markdown_20260705_q4xkzeqjf.md`, `deepseek_markdown_20260705_98aa15.md`/`(1).md`, `plan.md` v1.3), y los 2 logs de auditoría de continuidad (`SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` y `...-07.md`).
**Método:** cotejo línea por línea de las 4 fuentes citadas arriba contra el ZIP `IRAM_PROYECTO_REORGANIZADO_carpeta_raiz.zip` (33 archivos de logs/planes, sin la estructura `1_MOD/2_DOCUMENTACION/...` — ver §0 sobre esta limitación). Regla de consolidación aplicada: **append-only estricta (DR-42)** — ninguna decisión anterior se reescribe; donde dos fuentes contradicen, se cita ambas y se marca cuál rige y por qué.

**Este documento es, de acá en adelante, el único punto de partida.** No cargar la serie `SESSION_LOG_REPLANTEO_*` completa, no cargar los 3 borradores de plan por separado, no cargar los 2 logs de auditoría de continuidad como si fueran el estado vigente. Todos quedan como evidencia histórica citable por ID, no como insumo a releer entero.

> **VERSIÓN _6 (2026-07-07) — nombrada correctamente según la cadena real de versiones, no según el sufijo de archivo.**
> El nombre de archivo dice `_3` en varias copias que circularon este mismo día, pero por contenido esta es la **sexta** versión de este documento: (1) original → (2) `_2`, sin cambios de fondo respecto a la original, solo reetiquetado → (3) primera `_3`, generada en charla 2/3, con banner + §10/§11 nuevas (perdida por vivir solo en un directorio de trabajo efímero, nunca subida) → (4) segunda `_3`, reconstruida desde cero en charla 4 tras esa pérdida, contenido equivalente a (3) → (5) `_5`, que agrega §12 (meta-registro de las 4 charlas) sobre (4), más una nota dentro de §12 sobre un quinto incidente menor (una copia sin §12 pisó en disco a la versión con §12, detectada y corregida en el acto) → (6) **esta versión**, que agrega §13 (cierre parcial del Paquete B — preguntas #1, #2, #3) sobre (5). Esta versión sufrió el **mismo patrón de fuga documentado en §12**: se redactó y se guardó como `FUENTE_DE_VERDAD_IRAM_2026-07-07_6.md` en el directorio de trabajo efímero de la charla 6, nunca se subió como adjunto, y por lo tanto no estaba disponible al abrirse la charla siguiente. Se reconstruye acá desde el contenido íntegro de la transcripción de charla 6 (grep, comandos y salidas incluidos), verificando de nuevo cada dato contra el ZIP antes de asentarlo — mismo procedimiento que usó charla 4 para reconstruir `_3`. Ver nota al cierre de §13 para el registro completo de este sexto incidente.
>
> Esta versión agrega §10 (RECONCILIACIÓN CRÍTICA #5 — cierre del Paquete A), §11 (estado de los paquetes de debate tras la sesión del 2026-07-07), §12 (meta-registro de las 4 charlas) y §13 (cierre parcial del Paquete B) al final del documento, siguiendo la regla append-only (DR-42): ninguna palabra de §0–§9 de la versión `_2` se reescribe. El disparador de §10/§11 fue el debate del Paquete A (§9), que verificó contra el ZIP completo — no solo los 33 archivos que tuvo esta consolidación (ver §0) — que DC-06 ya está resuelto en el origen (DR-22) y solo faltaba trasladarlo a `WIKI_DOCUMENTACION_v2.md`. Ese traslado se ejecutó como `WIKI_DOCUMENTACION_v3.md`, documento hermano de esta versión (ese archivo sí conserva el sufijo `_3` con sentido, porque solo tuvo una versión previa, `v2.md`). Ver §10 para el detalle completo y la justificación de por qué esto no viola DR-12. El disparador de §13 fue continuar con el Paquete B (§9/§11): tres de las cuatro preguntas de `memoria_claude_volcado.md` se verificaron contra el ZIP completo, con resultados que corrigen matices del resumen de partida — ver §13.
>
> **VERSIÓN _8 (2026-07-07, sesión posterior) — agrega §15.** Disparador: se abrió el Paquete C (§9, casos #7 y #8) a pedido explícito del operador. Se verificó contra el ZIP completo (hashes, mtimes, diffs y greps ejecutados en esta sesión) el estado real de las dos versiones del paper (`IRAM_paper_metodologia_v1_0.md` / `(1).md`) y de las dos redacciones de la skill (`IRAM_skill_desarrollo_ia_v2_0.md` / `(2).md`, con `(3).md` confirmado duplicado exacto de `(2).md` por hash). **El Paquete C no queda cerrado en esta sesión.** El Caso #7 (paper) sí queda resuelto con dato: ambas versiones del 12/06 quedan superadas por `IRAM_C1_final.md` (18/06), que ya no tiene el mislabel "democratiza" y ya tiene la estructura de 7 secciones vigente. El Caso #8 (skill) queda caracterizado — evidencia de que son dos redacciones genuinamente complementarias, no borrador/final — pero sin que el operador llegara a decidir fusionar, elegir una, o mantener ambas con roles distintos. Ver §15 para el detalle completo y la pregunta exacta que quedó pendiente.
>
> **VERSIÓN _9 (2026-07-08) — agrega §16, séptimo incidente de fuga de continuidad.** Disparador: entre esta versión y `_8` hubo **cinco sesiones cortadas** (`charla_7` a `charla_11`), todas sobre una pregunta nueva que surgió en vivo dentro de `charla_7` — encuadre de "4 productos" (mod, documentación, trabajo UTN, portafolio) contra las ramas del proyecto, más una opinión sobre el núcleo narrativo — y ninguna llegó a escribir su avance en un documento persistente. Una sexta sesión (`charla_12`) reconstruyó el contenido recuperable de las cinco anteriores cotejando cada charla contra `plan.md` (extraído directo del ZIP, no heredado de transcripciones), llegó a redactar un `§16` y a empezar a escribirlo en `FUENTE_DE_VERDAD_IRAM_2026-07-07_9.md` — pero ese archivo nunca se subió como adjunto y no estuvo disponible en la sesión que produce esta versión. Es, por lo tanto, el **séptimo incidente de la misma familia que documentan §12/§13/§14**: un archivo de trabajo que solo vivió en un directorio de sesión efímero. Esta versión se reconstruye desde cero, releyendo las cinco charlas cortadas completas y re-verificando cada dato contra el ZIP (`IRAM_PROYECTO_REORGANIZADO3.zip`) en esta misma sesión — no se hereda ningún dato de las transcripciones sin re-chequeo. Ver §16 para el detalle completo, incluyendo la corrección final de encuadre que dio el operador (Objetivo 3 tiene 2 productos, no 3; el trabajo UTN es un producto único en dos etapas; el Portafolio no es una rama paralela sino el contenedor mayor) y los "3 ángulos" que el operador propuso como lectura alternativa, más liviana, de la misma estructura.
>
> **VERSIÓN _10 (2026-07-08, sesión posterior) — agrega §17, árbol definitivo de documentación como tarea prioritaria nueva.** Disparador: el operador señaló en vivo un problema estructural real y verificado en esta sesión — los `SESSION_LOG_REPLANTEO_*` viven **duplicados** en el ZIP: una copia ya organizada en `2_DOCUMENTACION/01_logs_replanteo/` (15 archivos) y una segunda copia idéntica por nombre, suelta en la raíz del ZIP fuera de toda carpeta (13 archivos), junto con otros 33 archivos de trabajo (planes viejos, volcados de memoria, charlas 1-6, versiones viejas de esta misma fuente de verdad) que tampoco están en ninguna carpeta del árbol reorganizado. A esto se suma `_CUARENTENA_DUPLICADOS/`, con 544 archivos en dos subcopias anidadas casi completas del proyecto, cuyo destino nunca se decidió (tarea #10 de §5, abierta desde `_2`). Esta versión no resuelve el árbol — lo declara **tarea prioritaria número 1**, por encima de DR-54, y añade §17 con el inventario verificado de lo que hay que ordenar/purgar antes de poder confiar en el árbol de documentación como fuente estable.

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
| B | **Cerrado (actualizado de nuevo en sesión posterior — ver §14).** Pregunta #4 resuelta con dato (ver §10, sesión 2026-07-07). Preguntas #1, #2 y #3 verificadas contra el ZIP completo y cerradas con matices en §13 (sesión posterior, mismo día). La pregunta de cierre que el propio §9 planteaba para el paquete completo ("¿se confirma el cierre con lo ya encontrado, o hace falta agregar tarea(s) explícitas?") se resuelve en §14: se confirma el cierre de las 4 preguntas sin reabrirlas, y se formaliza como tarea nueva de §5 la actualización de PROMPT_MAESTRO al modelo "rotación secuencial" que había quedado anotada al final de §13. |
| C | Sin debatir en esta sesión. Sigue como en §9. |
| D | Sin debatir en esta sesión. Sigue como en §9. |
| E | Sin debatir en esta sesión. Sigue como en §9. |
| F | Sin debatir en esta sesión. Sigue como en §9. |

**Archivos generados por esta sesión, pendientes de reemplazar sus versiones anteriores en el proyecto real:**
- `WIKI_DOCUMENTACION_v3.md` — reemplaza a `WIKI_DOCUMENTACION_v2.md` en `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/` (y su respaldo espejo en `08_documentacion_respaldo/DOCUMENTACION/`, según DR-45).
- `FUENTE_DE_VERDAD_IRAM_2026-07-07_5.md` (este archivo, ver nota de numeración en el banner de versión al inicio) — reemplaza como punto de partida operativo a la versión `_2`.

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

**Nota de esta reinserción (continuación posterior, mismo día):** en una sesión siguiente se subió por error una copia de este archivo sin §12 (316 líneas, hash `e9d3105b...`), que sobrescribió en disco a la versión completa (334 líneas, hash `21c9b428...`). Se detectó por comparación directa de ambas versiones a pedido del operador, y se restaura §12 aquí, sin cambios de contenido respecto a como se redactó originalmente — mismo texto, misma fecha. Sirve como segundo ejemplo, más leve, del mismo patrón de fuga que esta sección ya documenta: un archivo de trabajo entre sesiones puede perderse o retroceder a una versión anterior si no se verifica su hash/tamaño antes de asumir que es el vigente. Regla aplicable hacia adelante (consistente con NUEVO-1/§7): antes de dar por bueno un archivo re-subido con el mismo nombre, comparar tamaño y hash contra la última versión conocida, no asumir por el nombre.

**Estado de los archivos entregables, sin cambios respecto a §11:** `WIKI_DOCUMENTACION_v3.md` y esta misma `FUENTE_DE_VERDAD_IRAM_2026-07-07_5.md` siguen existiendo solo como archivos sueltos — **no reinsertados en el ZIP real**. Esa decisión sigue pendiente de confirmación del operador.

---

## 13. RECONCILIACIÓN CRÍTICA #6 — Cierre parcial del Paquete B (preguntas #1, #2, #3), sesión posterior del 2026-07-07, contra el ZIP completo

**Disparador:** el Paquete B (§9) quedó con 4 preguntas de `memoria_claude_volcado.md` sin responder tras la consolidación original. §10/§11 cerraron la pregunta #4 como efecto colateral del cierre del Paquete A. Esta sección cierra, con verificación directa contra el ZIP completo, las preguntas #1, #2 y #3. La pregunta #4 no se retrabaja acá — sigue como quedó en §10/§11.

**Advertencia de partida, importante para leer el resto de esta sección:** la sesión que produjo este cierre arrancó con un resumen de trabajo previo (de otra sesión sin registro propio en este documento) que afirmaba conclusiones preliminares para las 3 preguntas. La verificación contra el ZIP **corrigió matices de ese resumen en dos de las tres preguntas** — no lo confirmó tal cual. Se documentan ambas cosas: lo que decía el resumen de partida y lo que la verificación encontró.

### Pregunta #1 — "5 cuentas secuenciales" propagado a R18/Plantilla D

**Lo que decía el resumen de partida:** que la corrección "rotación secuencial, no paralela" vivía en `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` (la más tardía de 3 versiones divergentes) pero nunca llegó al PROMPT_MAESTRO real.

**Lo que la verificación encontró, y que corrige ese resumen:** no son 2 versiones con una corrección pendiente de trasladar — son **3 versiones del mismo `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO` que se contradicen entre sí en la conclusión misma**, no solo en si se trasladó o no:
- `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO.md` (mtime 03:23:30) — versión base: reporta el hallazgo de "cuentas aparentemente paralelas" como pendiente de verificación, sin veredicto.
- `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO (2).md` (mtime 04:03:40) — veredicto: **"Bloque 2 RESUELTO: cuentas eran GENUINAMENTE PARALELAS (85% de días IRAM con múltiples cuentas)"**; declara **"R18 era correcta"**, sin cambios necesarios.
- `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` (mtime 04:20:58) — veredicto opuesto: **"rotación secuencial rápida, no paralelismo simultáneo"**; declara que "R18 necesita actualización" y que "el modelo 'cuentas paralelas' debe reemplazarse por 'rotación secuencial de contextos'". Esta versión se autoidentifica internamente como posterior — su encabezado dice "actualizado sesión 6" y describe el análisis cuantitativo como "v2 ... Bloque 2 rehecho. v1 obsoleta" — mientras que (2) no lleva ningún marcador de sesión ni de versión corregida.

El orden de mtime (03:23 → 04:03 → 04:20) coincide con el orden que las propias versiones declaran internamente sobre sí mismas (base sin veredicto → "GENUINAMENTE PARALELAS" → "rotación secuencial, v2 corregida, sesión 6"), así que la lectura más consistente con la evidencia disponible es que **la versión `(1)` (04:20, rotación secuencial) es la más tardía de las tres** y por lo tanto la conclusión vigente sobre el hallazgo mismo.

Pero eso no cierra la pregunta original — la corrección "secuencial" existe en `(1)`, y aun así:
- `PROMPT_MAESTRO_v1_6.md` (mtime 2026-06-12 03:23:34 — nótese: **anterior** a las 3 versiones de CONSOLIDADO citadas arriba, ninguna de las tres pudo haber alimentado a este archivo) tiene R18 con el modelo "cuentas paralelas" y una nota explícita de "PENDIENTE: verificar si son paralelas reales o reinicios post-corte" (línea 182, 251, 326).
- `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` (la versión vigente, mtime 2026-06-06 — **también anterior** a las 3 versiones de CONSOLIDADO, por 6 días) reasignó el número R18 a un tema completamente distinto ("antes de preguntar si algo fue subido..."). No hay ninguna mención a "paralela", "secuencial", "solapamiento" en ningún lugar del archivo. El contenido original de R18 no fue trasladado a otro número — desapareció sin dejar rastro en este archivo.

**Conclusión de la pregunta #1:** el hallazgo del resumen de partida ("nunca llegó al PROMPT_MAESTRO") sigue siendo cierto, pero por una razón más simple y distinta a la que el resumen daba a entender: **no es que la corrección no se haya trasladado a tiempo — es que ambos PROMPT_MAESTRO relevantes (`v1_6` y `v5_2`) tienen fecha *anterior* a los 3 `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO` que contienen la discusión completa (base, "paralelas", "secuencial").** El PROMPT_MAESTRO vigente (`v5_2`, 06-06) es anterior en 6 días al hallazgo original de "cuentas paralelas" (que aparece recién en los CONSOLIDADO del 12/06) y por lo tanto no pudo haberlo incorporado nunca — su R18 fue reescrita para otro propósito antes de que la pregunta de fondo (paralelas vs. secuenciales) se abriera y cerrara. Esto no es una fuga de continuidad en el sentido de "se decidió algo y no se propagó" — es un problema de **orden temporal**: el documento que se supone debía reflejar la conclusión es más viejo que la conclusión misma. Queda como tarea nueva (no bloqueante): si se quiere que el PROMPT_MAESTRO refleje el modelo correcto ("rotación secuencial", según la versión `(1)` más tardía), hace falta una revisión explícita post-12/06 que hoy no existe en ningún archivo del ZIP.

### Pregunta #2 — Tiering, techo operacional, "lenguaje de Claude"

**Lo que decía el resumen de partida:** que tiering y techo operacional están confirmados en la Sección 4D de `IRAM_C1_final.md`, pero que "lenguaje de Claude" (comandos secuenciales) no aparece en ningún documento — solo en transcripciones de charla (`critica a la critica.md`).

**Lo que la verificación encontró, y que corrige ese resumen:** la afirmación sobre "lenguaje de Claude" era incorrecta. Además de `critica a la critica.md` (que es efectivamente una transcripción de charla, no documentación operativa), el término aparece también en documentos que sí son documentación operativa del proyecto:
- `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md`, línea 71: `"✅ 'Lenguaje de Claude': comandos secuenciales con estructura específica — construido en prueba y error, no prosa. El PROMPT_MAESTRO es el artifact de este aprendizaje."`
- El mismo texto (con variaciones menores) se repite en `s19.md`, `s19_1.md`, `s19 (2).md`, y `s20.md` cita la referencia al PROMPT_MAESTRO v5.2 como "el artifact central. Estructura real del 'lenguaje de Claude'".
- También aparece, con contexto más extenso, en `fallo sesiones 16-06-2026.md` y su duplicado `fallo sesiones transcript 16-06-2026.md`, y en `failed 3.md` — estos tres sí son transcripciones/reconstrucciones de sesión, no documentos de estado, pero muestran que el concepto viene de una charla real del operador (línea 4305 de `fallo sesiones 16-06-2026.md`: "Hay tres patrones operacionales que no llegaron a ningún documento: el tiering..., el techo operacional por sesión..., el 'lenguaje de Claude'... — construido en prueba y error"), y ese mismo pasaje es, con alta probabilidad, la fuente original de la pregunta #2 tal como está formulada en `memoria_claude_volcado.md`.

**Conclusión de la pregunta #2:** el concepto **sí está incorporado a documentación operativa real** (`SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18` en adelante, dentro de la serie s18–s20 del 17/06), contra lo que decía el resumen de partida. La pregunta original de `memoria_claude_volcado.md` ("¿ya incorporado a algún documento?") se responde: **sí, desde s18 (17/06).** Tiering y techo operacional, ya confirmados en el resumen de partida vía Sección 4D de `IRAM_C1_final.md`, se mantienen sin cambios.

### Pregunta #3 — "SKILL v1.0 no es la base — es el esqueleto de s17"

**Lo que decía el resumen de partida:** que está ampliamente propagado y consistente desde s21 en adelante (DEC-08, DEC-12, DEC-16), incluida `WIKI_DOCUMENTACION_v3.md` ya vigente.

**Lo que la verificación encontró:** confirmado, con un matiz que precisa la formulación de la pregunta misma. `DEC-08` (nace en s21: "REGLA DE CONTRADICCIÓN: SESSION_LOG > WIKI > SKILL v1.0 en framing; SKILL v1.0 > todo en hechos técnicos") y `DEC-12` (s18→s21: "SKILL v1.0 es fuente de hechos técnicos. Framing estructural superado desde s18") se repiten de forma idéntica o cuasi-idéntica en `SESSION_LOG_DOCUMENTACION_s23` hasta `s34` (s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s34 — 11 archivos), y en `WIKI_DOCUMENTACION_v2.md` línea 42 (heredado sin cambios en `WIKI_DOCUMENTACION_v3.md`, que es la versión que este documento ya trata como vigente desde §10).

El matiz: la formulación de la pregunta ("SKILL v1.0 no es la base — es el esqueleto de s17") mezcla dos hechos relacionados pero distintos, y la cadena DEC-08/DEC-12/DEC-16 solo documenta directamente uno de ellos con esas palabras exactas. Lo que dicen los documentos, con precisión:
- El **esqueleto de s17** (`IRAM_C1_esqueleto_s17.md`, confirmado también en `WIKI_DOCUMENTACION_v3.md` como vigente) se construyó **a partir de** SKILL v1.0 — la propia wiki lo describe como "mapping desde SKILL v1.0" (fila `IRAM_C1_esqueleto`).
- El **framing estructural de SKILL v1.0** (no el esqueleto) es lo que queda marcado como "superado" — y la fecha de esa marca es **s18**, no s17: `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` es donde aparece por primera vez la revisión crítica que degrada el framing del SKILL a "fuente de hechos técnicos" solamente.
- `DEC-12` formaliza esto en s21 citando el rango "s18→s21", consistente con lo anterior.

En otras palabras: **el esqueleto de s17 usa el SKILL v1.0 como insumo; el framing del SKILL v1.0 queda superado un día después, en s18; y la regla que formaliza que el esqueleto (vía s18 en adelante) es la estructura real, no el SKILL, se nombra recién en s21 (DEC-08/DEC-12).** La pregunta original, tal como está en `memoria_claude_volcado.md`, comprime estos tres momentos en una sola frase — correcta en su conclusión, imprecisa en la mecánica interna si se cita con el detalle que este documento exige.

### Tareas de §5 que este cierre resuelve o actualiza (append-only — no se reescriben las filas originales, se marca su resolución acá)

- **Tarea #5 / preguntas #1, #2, #3 de `memoria_claude_volcado.md`** (§3, §9 Paquete B): pasan de "abiertas, requieren confirmación" a **cerradas con dato en esta sección**, con dos matices importantes documentados arriba (pregunta #1: problema de orden temporal entre PROMPT_MAESTRO y el hallazgo, no de traslado; pregunta #2: el resumen de partida de esta misma sesión estaba equivocado y se corrige acá). La pregunta #4, ya cerrada en §10, no se retrabaja.
- **Nueva tarea, candidata a §5** (no bloqueante): revisar si el PROMPT_MAESTRO vigente (`v5_2`) debería actualizarse para reflejar el modelo "rotación secuencial" de `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md`, dado que ningún PROMPT_MAESTRO existente pudo haberlo incorporado por ser anterior en fecha al hallazgo mismo (ver Pregunta #1 arriba). No urgente — el PROMPT_MAESTRO no se usa como fuente operativa activa desde que el flujo pasó a `plan.md`/Fase 1 en adelante, pero queda como inconsistencia documental sin cerrar si alguna vez se vuelve a citar ese archivo.

**Nota sobre la reconstrucción de esta sección (sexto incidente de fuga de continuidad, mismo patrón que §12):** esta §13 fue redactada originalmente en una sesión posterior a la que cerró §10/§11/§12, y guardada como `FUENTE_DE_VERDAD_IRAM_2026-07-07_6.md` en el directorio de trabajo efímero de esa sesión (`/home/claude/work/` de esa charla). Ese archivo **nunca se subió como adjunto** — ni al ZIP del proyecto ni como archivo suelto a una conversación posterior — y por lo tanto no estaba disponible al abrirse la charla siguiente, que solo tenía acceso a `_5.md` (sin §13) más la transcripción cruda de la sesión que había producido `_6.md` (`charla_6.md`, con todos los comandos, greps y salidas de esa verificación, pero sin el documento final redactado). Esta versión de §13 se reconstruyó desde esa transcripción, re-verificando cada dato citado (mtimes de los 3 `CONSOLIDADO`, contenido exacto de R18 en ambos PROMPT_MAESTRO, y las menciones de "lenguaje de Claude" fuera de `critica a la critica.md`) contra el ZIP antes de asentarlo de nuevo — mismo procedimiento que usó charla 4 para reconstruir `_3.md` tras la pérdida documentada en §12. Es el sexto incidente de esta clase que este documento registra (los cinco anteriores están en §12 y su nota de reinserción). Refuerza, sin necesidad de una regla nueva, la que ya existe: **NUEVO-1/§7 y la nota de §12 sobre "ningún archivo de trabajo generado en sesión debe considerarse persistente hasta que se suba o se adjunte explícitamente"** — esta vez aplicada al propio documento que enuncia la regla.

**Estado de los archivos entregables, actualizado respecto a §11/§12:** `WIKI_DOCUMENTACION_v3.md` y esta misma `FUENTE_DE_VERDAD_IRAM_2026-07-07_6.md` siguen existiendo solo como archivos sueltos — **no reinsertados en el ZIP real**. Esa decisión sigue pendiente de confirmación del operador. Queda abierta, para cuando el operador decida resolverlo, la pregunta #6 de §9 Paquete F (destino de `_CUARENTENA_DUPLICADOS/`) y las preguntas #1, #2, #3 restantes de Paquete B originales de §9 (los tres patrones operativos, S5, esqueleto s17) — que son, precisamente, las que esta sección acaba de cerrar. Quedan sin debatir en esta cadena: Paquetes C, D, E, F (ver §11 para el estado exacto de cada uno).

---

## 14. RECONCILIACIÓN CRÍTICA #7 — Cierre final del Paquete B (pregunta de cierre de §9), sesión posterior del 2026-07-07

**Disparador:** el Paquete B (§9) cerraba con una pregunta explícita para el paquete completo, no solo pregunta por pregunta: *"para cada una de las 4 preguntas — ¿se responde ahora con lo que ya sabemos, se agenda como tarea explícita del plan nuevo, o se descarta formalmente con una nota de 'absorbida por el rediseño, ya no aplica'?"* Esa pregunta de cierre nunca se respondió como tal: §10 cerró la pregunta #4 y §13 cerró las preguntas #1, #2 y #3, pero ninguna de las dos secciones evaluó el paquete *como conjunto* contra el criterio que §9 había fijado. Esta sección hace ese cierre de paquete. **No se reabre ni se reverifica ninguna de las 4 preguntas individuales** — se toman tal como quedaron cerradas en §10 y §13, y solo se aplica sobre ellas el criterio de cierre de §9.

**Verificación previa a este cierre:** antes de redactar esta sección se releyó el ZIP completo (`IRAM_PROYECTO_REORGANIZADO2.zip`, mismo insumo que usó la sesión de §13) para confirmar que no hay ningún archivo posterior a `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` que ya haya trasladado el modelo "rotación secuencial" a un PROMPT_MAESTRO. `find` sobre el árbol reorganizado confirma que las únicas versiones de PROMPT_MAESTRO que existen en todo el proyecto son `PROMPT_MAESTRO_v1_6.md`, `PROMPT_MAESTRO_v1_8.md` / `v1_8(1).md`, `IRAM_PROMPT_MAESTRO_v3_8_2026-05-27_20-55.md`, `v3_9_2026-05-30_03-14.md` e `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` (más su duplicado `(2).md`, idéntico salvo posición en `_CUARENTENA_DUPLICADOS/`) — ninguna con fecha posterior al 06-06, y por lo tanto ninguna pudo haber incorporado nunca una corrección que aparece recién en los CONSOLIDADO del 12-06. Esto confirma, sin contradecirla, la lectura de §13 pregunta #1: el problema es de orden temporal, no de traslado fallido, y sigue sin existir ningún archivo que lo resuelva.

### Aplicación del criterio de cierre de §9, pregunta por pregunta

| # | Pregunta (§9) | Resolución en | Resultado del criterio de cierre |
|---|---|---|---|
| 1 | "5 cuentas secuenciales" propagado a R18/Plantilla D | §13 | **Se responde con lo ya encontrado** (no hace falta más investigación: el hecho de que ambos PROMPT_MAESTRO sean anteriores a la conclusión misma ya explica por completo el "no propagado", sin ambigüedad pendiente). **Además, se agenda una tarea explícita** — ver más abajo, la única de las 4 que genera tarea nueva. |
| 2 | ¿DC-06 (mislabel "democratización") sigue abierto? | §10 | **Cerrada con dato y ya ejecutada**, no solo respondida: la corrección se escribió en `WIKI_DOCUMENTACION_v3.md`. No requiere tarea adicional. |
| 3 | "Tres patrones operativos" (tiering, techo operacional, "lenguaje de Claude") ya incorporados | §13 | **Se responde con lo ya encontrado**: los tres están incorporados a documentación operativa real (tiering y techo vía Sección 4D del paper, "lenguaje de Claude" desde `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` en adelante). No requiere tarea — es un cierre afirmativo, no una ausencia de dato. |
| 4 | "SKILL v1.0 no es la base — es el esqueleto de s17" reflejado consistentemente | §13 | **Se responde con lo ya encontrado**, con el matiz de mecánica interna documentado en §13 (tres momentos distintos: esqueleto s17 usa SKILL v1.0 como insumo → framing superado en s18 → regla formalizada en s21 vía DEC-08/DEC-12). El matiz no genera tarea porque no señala ninguna inconsistencia real entre documentos — al contrario, confirma consistencia s18→s34 en 11 archivos. |

**Conclusión general:** de las 4 preguntas originales de `memoria_claude_volcado.md`, **3 se cierran limpiamente con lo ya encontrado, sin generar tarea** (#2, #3, #4 de esta tabla — que corresponden a las preguntas #4, #1 y #3 de la numeración original de §9, respectivamente, dado que §9 no numeró en el mismo orden que esta tabla; ver columna "#" de §9 para el mapeo exacto). La única que sí requiere una tarea explícita es la pregunta #1 de §9 ("5 cuentas secuenciales" → PROMPT_MAESTRO), no porque quede sin responder, sino porque la respuesta misma ("nunca pudo haberse incorporado, por orden temporal") deja una inconsistencia documental real y accionable: el PROMPT_MAESTRO vigente sigue sin reflejar el modelo correcto. Ninguna de las 4 preguntas se descarta como "absorbida por el rediseño, ya no aplica" — las 4 tenían respuesta real disponible en el material, contra lo que el encuadre de §9 dejaba abierto como posibilidad.

### Decisión sobre la "nueva tarea candidata a §5" anotada al final de §13

**Texto original de la nota (§13, cierre de pregunta #1):** revisar si el PROMPT_MAESTRO vigente (`v5_2`) debería actualizarse para reflejar el modelo "rotación secuencial", marcada ahí como "no urgente" porque el PROMPT_MAESTRO no se usa como fuente operativa activa desde que el flujo pasó a `plan.md`/Fase 1 en adelante.

**Evidencia adicional encontrada para esta decisión, no citada en §13:** `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` no se limita a describir el hallazgo — en su propio texto (línea 110, confirmada por grep contra el ZIP en esta sesión) ya prescribe la acción: *"El modelo de 'cuentas paralelas' debe reemplazarse por 'rotación secuencial de contextos'. Acción manual del operador sobre el PROMPT_MAESTRO v1.6."* Es decir, la tarea no es una ocurrencia nueva de esta consolidación — **ya estaba especificada, con archivo objetivo exacto (`PROMPT_MAESTRO v1.6`), en la fuente original del 12/06**, y quedó sin ejecutar por el mismo motivo que el resto de esta cadena diagnostica repetidamente: nadie volvió a esa fila una vez escrita.

**Decisión:** se formaliza como tarea nueva de §5, no se descarta. Razones:
- No es una tarea inventada por esta sesión — es una instrucción explícita del propio 12/06 que nunca se marcó como ejecutada ni como descartada en ningún log posterior (grep contra toda la cadena REPLANTEO y AUDITORIA_CONTINUIDAD no la encuentra citada en ningún lugar salvo su origen).
- La calificación de "no urgente" de §13 sigue siendo correcta y se mantiene sin cambios (el PROMPT_MAESTRO no es fuente operativa activa desde `plan.md`/Fase 1), por lo que esta tarea se agrega como **no bloqueante**, igual que la mayoría de la tabla de §5.
- Dejarla sin formalizar sería repetir exactamente el patrón que NUEVO-1/§7 existe para prevenir: una instrucción con archivo objetivo exacto, escrita y nunca ejecutada ni descartada, que queda flotando fuera de la tabla única de tareas.

**Tarea nueva, append-only sobre §5 (no se renumera ni se reescribe ninguna fila existente de esa tabla):**

| # | Tarea | Bloqueante? | Origen | Estado |
|---|---|---|---|---|
| 18 | Actualizar `PROMPT_MAESTRO_v1_6.md` (o la versión que se declare vigente para ese propósito) para reemplazar el modelo "cuentas paralelas" (R18) por "rotación secuencial de contextos", tal como prescribe textualmente `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` línea 110. Nota: `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` (la versión operativa vigente) ya no tiene R18 con este contenido — fue reasignada a otro tema antes de que el hallazgo existiera (ver §13 pregunta #1) — por lo que esta tarea, si se ejecuta, aplica sobre `v1_6` como registro histórico corregido, no sobre `v5_2` como cambio de comportamiento operativo activo. | No bloqueante — el PROMPT_MAESTRO no es fuente operativa activa desde `plan.md`/Fase 1 en adelante | `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO(1).md` línea 110 (instrucción original, nunca ejecutada); nota candidata de §13; formalizada en §14 | Abierta |

### Cierre formal del Paquete B

**Las 4 preguntas de `memoria_claude_volcado.md` quedan cerradas en su totalidad**, con el siguiente balance: 3 respondidas y confirmadas sin tarea adicional (mislabel "democratización" ya corregido y escrito; los tres patrones operativos ya incorporados a documentación real; consistencia del esqueleto s17/SKILL v1.0 confirmada con matiz de mecánica interna sin inconsistencia real), y 1 respondida con una tarea nueva formalizada (tarea #18 de §5, PROMPT_MAESTRO). Ninguna pregunta queda en estado "sin dato" ni "descartada sin resolver". El Paquete B no requiere más sesiones dedicadas — cualquier trabajo futuro sobre él es, a partir de acá, la ejecución de la tarea #18 cuando el operador lo priorice, no investigación adicional.

**Tareas de §5 que este cierre resuelve o actualiza (append-only — no se reescriben las filas originales, se marca su resolución acá):**
- **Tarea #5** (§5, "responder las 4 preguntas... o confirmar que el plan nuevo las vuelve obsoletas"): pasa de "Abierta — requiere tu confirmación" a **cerrada por partes**: 3 de 4 preguntas cerradas sin tarea (vía §10 y §13), 1 de 4 cerrada con tarea nueva (#18, esta sección). Ninguna resultó "obsoleta por el rediseño" — las 4 tenían respuesta real en el material disponible.
- **Tarea nueva #18** (PROMPT_MAESTRO / rotación secuencial): agregada en esta sección, ver tabla arriba.

**Estado de los archivos entregables, sin cambios de fondo respecto a §11/§13:** esta versión (`FUENTE_DE_VERDAD_IRAM_2026-07-07_7.md`) y `WIKI_DOCUMENTACION_v3.md` siguen existiendo solo como archivos generados en sesión — **no reinsertados en el ZIP real**. Esa decisión sigue pendiente de confirmación del operador. A diferencia de las dos veces anteriores (§12, §13), **esta versión se entrega al operador como adjunto explícito en el mismo turno en que se genera**, precisamente para no repetir el patrón de fuga de continuidad que produjo los incidentes quinto y sexto ya documentados.

**Nota de continuidad — por qué esta vez se adjunta explícitamente:** los dos incidentes de pérdida más recientes de este documento (la nota de reinserción dentro de §12, y el incidente completo narrado en el banner de versión y al cierre de §13) ocurrieron por la misma causa: un archivo redactado y guardado únicamente en el directorio de trabajo efímero de la sesión, nunca subido como adjunto, no disponible al abrirse la charla siguiente. La regla que ya existe para esto (NUEVO-1/§7, reforzada en la nota de §12 y de nuevo en la nota de §13: "ningún archivo de trabajo generado en sesión debe considerarse persistente hasta que se suba o se adjunte explícitamente") se aplica acá de forma literal: este archivo se presenta como adjunto mediante la herramienta correspondiente en el mismo turno en que se termina de escribir, no se deja como una promesa de "está guardado en el directorio de trabajo".

---

## 15. RECONCILIACIÓN CRÍTICA #8 — Apertura del Paquete C (paper y skill), sesión posterior del 2026-07-07 — CIERRE PARCIAL

**Disparador:** el operador pidió explícitamente trabajar el Paquete C (§9) en esta sesión: "fusionar o elegir entre las dos redacciones paralelas de `IRAM_paper_metodologia_v1_0.md` e `IRAM_skill_desarrollo_ia_v2_0.md`". Se verificó todo contra el ZIP completo (`IRAM_PROYECTO_REORGANIZADO2.zip`), con comandos ejecutados en esta sesión — hashes, mtimes, diffs, greps — no heredados de ningún resumen de partida.

### 15.1 — Inventario real de archivos del paquete

`find` sobre el árbol reorganizado (`2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`, con espejo idéntico en `_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/` y respaldo parcial en `08_documentacion_respaldo/DOCUMENTACION/`) confirma:

- **Paper:** 2 archivos con contenido distinto — `IRAM_paper_metodologia_v1_0.md` (24362B, mtime 2026-06-12 22:21:28) y `IRAM_paper_metodologia_v1_0(1).md` (20390B, mtime 2026-06-12 22:37:28). Hashes MD5 distintos (`16d9672e...` vs `8d94ee1b...`) — confirmado que son dos redacciones reales, no un duplicado con nombre distinto.
- **Skill:** 3 archivos, pero solo 2 contenidos distintos. `IRAM_skill_desarrollo_ia_v2_0.md` (4381B, mtime 22:59:24) es una redacción. `IRAM_skill_desarrollo_ia_v2_0 (2).md` (5237B, mtime 2026-06-18 15:03:54) y `(3).md` (5237B, mtime 15:26:52) son **byte-idénticos** (mismo hash MD5 `18c7c444...`, `diff` sin salida) — `(3)` es una copia mecánica de `(2)`, probablemente del propio proceso de reorganización del ZIP, no una tercera redacción real. El paquete real, tal como decía §9, es dos versiones, no tres.

### 15.2 — Caso #7 (paper): resuelto con dato, no con elección

Se leyeron las dos versiones completas. Ambas contienen el mislabel "democratización" sin corregir:
- `IRAM_paper_metodologia_v1_0.md`: dos ocurrencias (línea 15, resumen ejecutivo; línea 164, cita de cierre) — *"La afirmación central de este documento: la IA no democratiza la programación..."*
- `IRAM_paper_metodologia_v1_0(1).md`: tres ocurrencias (línea 12, 14, 175) — formulación equivalente, con el agregado de plantear primero "la tesis convencional" para después refutarla.

Esto es exactamente el error que **DR-22/DC-06 ya identificó y cerró en el paper mismo el 17/06** (ver §10, ya cerrado en esta cadena). Se verificó de forma independiente que `IRAM_C1_final.md` — presente en tres copias idénticas en el proyecto (vigente + 2 respaldos), mtime 2026-06-18 16:00:06, **posterior** a ambas versiones del 12/06 — tiene **cero** menciones de "democrat" en todo el archivo (`grep -c` confirma 0) y ya tiene la estructura definitiva de 7 secciones (§1 "El laboratorio" a §7 "Qué transfiere y qué no"), con la Sección 3 ya titulada "El hallazgo central: la posición y el formato importan más que el contenido" — el mismo principio que §10 de este documento ya trasladó a `WIKI_DOCUMENTACION_v3.md`.

**Conclusión:** la pregunta de cierre que planteaba §9 para el Caso #7 ("¿fusionar o elegir entre las dos versiones del 12/06?") parte de un supuesto que ya no aplica — no hace falta elegir entre esas dos, porque ninguna de las dos es la versión final del paper. `IRAM_C1_final.md` ya es una tercera redacción, posterior a ambas y con el error de fondo corregido, y es la que la wiki (`WIKI_DOCUMENTACION_v3.md`) ya trata como fuente vigente del principio central desde §10. Las dos versiones del 12/06 pasan de "candidatas a fusionar" a **material de referencia histórica**: conservan valor real como evidencia de cómo evolucionó el argumento (en particular, el marco de "tres condiciones de transferibilidad" de `(1).md` es más explícito que en la base — vale la pena cotejar si `IRAM_C1_final.md` §7 ya lo capturó con el mismo nivel de detalle, tarea menor no bloqueante, no evaluada en esta sesión), pero no compiten por ser "el paper" y no requieren fusión ni decisión de cuál archivar.

### 15.3 — Caso #8 (skill): caracterizado, decisión pendiente

Se leyeron las dos redacciones completas (`IRAM_skill_desarrollo_ia_v2_0.md` y `(2).md` — `(3).md` no se releyó aparte, por ser duplicado confirmado byte a byte de `(2).md`). A diferencia del paper, **no hay una tercera versión posterior que resuelva esto con dato** — son dos redacciones genuinamente distintas y complementarias, sin una relación de borrador/final:

- **Versión base** (`IRAM_skill_desarrollo_ia_v2_0.md`, 12/06): estructura de **runbook de sesión** — arranque, durante, cierre, qué hacer si se corta, checklist explícito por fase. Frontmatter la describe como "cargar al inicio de proyectos técnicos... señales de activación: instrucciones que se olvidan, errores que se repiten". Se autodeclara en el pie: *"Extraído de: IRAM_paper_metodologia_v1_0.md. Reemplaza: IRAM_SKILL_desarrollo_con_IA_v1_0.md"*.
- **Versión (2)/(3)** (18/06, seis días después): estructura de **skill temática** — arquitectura de contexto, división de trabajo operador/IA, diagnóstico de dos modos de falla (epistémica vs. técnica), decisiones descartadas, overhead de documentación, condiciones de transferencia. No tiene estructura de sesión (arranque/durante/cierre) y no se autodeclara como reemplazo de nada — su frontmatter dice "Operación de proyectos técnicos sostenidos con Claude... arquitectura de contexto, división de trabajo, diagnóstico de modos de falla".

Ambas comparten el `name` y el `version: 2.0` del frontmatter, pero el contenido se solapa poco: la base cubre *cuándo hacer qué* dentro de una sesión; la (2)/(3) cubre *por qué* funciona el sistema (arquitectura de contexto, tiering, las tres condiciones de transferencia — este último punto ya citado en §10 de este documento como material potencialmente no capturado en `IRAM_C1_final.md` §7). Un operador que solo tuviera una de las dos perdería información real que la otra sí tiene.

**Lo que esta sesión no llegó a resolver:** la decisión entre (a) fusionar tomando lo mejor de cada versión en una sola skill C2, (b) mantener ambas con roles declarados y distintos (una como runbook operativo, otra como fundamento conceptual), o (c) elegir una como la C2 definitiva y archivar la otra como referencia — y, si se fusiona, quién hace el pase (edición humana vs. instrucción explícita a Claude sobre qué tomar de cada lado). La sesión se cortó en este punto antes de que el operador respondiera a la pregunta planteada.

### 15.4 — Tareas de §5 que este cierre parcial resuelve o actualiza (append-only)

- **Tarea #14** (§5: "Decidir los 2 pares de redacciones paralelas del Paso 0 — ¿fusionar o elegir?"): se separa en sus dos componentes, que ya no comparten el mismo estado.
  - Componente paper (Caso #7): **cerrado con dato en esta sección.** No hace falta fusionar ni elegir — ambas versiones del 12/06 quedan como referencia histórica, `IRAM_C1_final.md` es la versión vigente del paper (consistente con lo que §10 ya estableció sobre el principio central).
  - Componente skill (Caso #8): **sigue abierta**, ahora con caracterización completa y evidencia de que las dos versiones son complementarias, no jerárquicas — pendiente de la decisión del operador (fusionar / mantener ambas con roles distintos / elegir una).

### 15.5 — Estado de los archivos entregables

Ningún archivo nuevo de contenido (paper o skill fusionados) se generó en esta sesión — el trabajo fue de verificación y caracterización, no de redacción de una versión nueva de esos documentos. Esta misma fuente de verdad (`FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md`) es el único artefacto nuevo, y se entrega como adjunto explícito en el mismo turno en que se termina de escribir, siguiendo la regla de continuidad ya vigente desde la nota de §14 (para no repetir los seis incidentes de fuga de continuidad ya documentados en §12/§13). `WIKI_DOCUMENTACION_v3.md` no tiene cambios respecto a la versión ya adjuntada al inicio de esta sesión — no hizo falta tocarla, porque el Caso #7 no generó ningún cambio de contenido en el principio central (ya estaba correcto desde §10).

---

## 16. RECONCILIACIÓN CRÍTICA #9 — Cinco sesiones cortadas sobre encuadre de "4 productos" y núcleo narrativo — séptimo incidente de fuga, reconstrucción completa

**Disparador:** en `charla_7`, en vivo, el operador hizo una pregunta que no está en `_8.md`: *"antes de armar la propuesta reflexiona profundamente teniendo en cuenta los objetivos del proyecto (4 productos: mod, documentación, trabajo UTN y portafolio) en el marco de las grandes ramas del mismo (Mod, Documentación, Análisis). De paso dame tu opinión sobre el tema del proyecto como núcleo narrativo: 'cómo aprendimos a trabajar con IA en un proyecto corto de múltiples sesiones'."* Esta pregunta generó cinco sesiones consecutivas (`charla_7` a `charla_11`), todas cortadas antes de entregar una respuesta de texto completa al operador. Esta sección reconstruye lo recuperable de las cinco, verificado de nuevo contra `plan.md` y el ZIP en esta misma sesión (no heredado de las transcripciones sin re-chequeo), y cierra con la corrección de encuadre final que dio el operador.

### 16.1 — Qué hizo cada sesión cortada, y por qué se perdió

| Sesión | Avance real | Por qué se perdió |
|---|---|---|
| `charla_7` | Preguntó lo de arriba. Rastreó objetivos/productos contra `_8.md`, encontró DR-52 (C1/C2 no son "4 productos parejos", son 2 productos del objetivo 2, auxiliares del objetivo 3) y la tensión con Paquete D (¿C2 "existe" o está "pendiente"?). Armó un primer SVG (`estructura_objetivos_iram.svg`, el mismo que el operador adjuntó a esta sesión). | Se cortó generando el SVG, antes de escribir una sola línea de respuesta al operador. |
| `charla_8` | Recuperó el SVG de `charla_7` completo. Dio una recomendación completa sobre Caso #8 (elegir la base del 12/06 como C2 operacional, archivar `(2)/(3)` del 18/06 como insumo conceptual para el paper — no como descartada). Detectó, correctamente para el ZIP de *esa* sesión, que `plan.md` y el log fuente de DR-52/53/54 no estaban presentes. | El operador cortó la sesión en vivo corrigiendo ese último punto ("mal, ambos archivos... están en el zip que adjunté también") — corrección real, pero que nunca quedó escrita en ningún documento persistente. |
| `charla_9` | Confirmó que `plan.md` sí está en el ZIP v3, lo leyó directo. Encontró la estructura real de `plan.md`: 3 objetivos (no "4 productos parejos") y el marco de "3 niveles" (Nivel 1 = mod/vehículo, Nivel 2 = documentación, Nivel 3 = análisis/metacognición) — que responde directamente la pregunta de núcleo narrativo. | Se cortó justo al terminar de citar el marco de niveles, sin sintetizar una respuesta. |
| `charla_10` | Encontró el dato más valioso de las cinco sesiones: **ANEXO D** de `plan.md` ("EVALUACIÓN HONESTA DEL PROYECTO"), con tres frases de pitch ya redactadas para portafolio y una advertencia explícita de no presentarlo como "hice un mod". Detectó y verificó una inconsistencia real (ver §16.3). Corrigió la topología del diagrama: Documentación y Entregas/Portafolio UTN son ramas paralelas de Fase 1/Análisis (ambas dependen solo de que Fase 1 corra), no una cadena secuencial. Anunció `estructura_dependencias_iram_v2.svg`. | Se cortó justo después de anunciar el SVG corregido, sin adjuntarlo ni escribir la respuesta de texto. |
| `charla_11` | Repitió el mismo recorrido que `charla_10` de forma independiente (mismo hallazgo del Anexo D, mismo cálculo de duración, misma corrección de topología), llegando otra vez a generar el SVG corregido. | Mismo punto de corte: inmediatamente después de mostrar el diagrama, sin adjuntarlo ni entregar texto. |
| `charla_12` | Reconstruyó lo anterior comparando las cinco charlas entre sí y contra `plan.md` releído directo del ZIP. Entregó la síntesis completa al operador (ver §16.2). Recibió del operador dos correcciones de encuadre en vivo (ver §16.4) y una tercera lectura alternativa ("3 ángulos", ver §16.5). Empezó a escribir esta misma sección `§16` en un archivo `_9.md`. | El archivo `_9.md` que estaba escribiendo nunca se subió como adjunto — mismo patrón de fuga, séptima instancia. Se reconstruye acá desde cero. |

**Nota:** el SVG corregido (`estructura_dependencias_iram_v2.svg`) mencionado por `charla_10` y `charla_11` no existe como archivo entregado — ninguna de las dos sesiones lo adjuntó antes de cortarse. El único SVG que el operador tiene y adjuntó es `estructura_objetivos_iram.svg`, la versión v1 (de `charla_7`), que dos sesiones (`10` y `11`) ya habían identificado como topológicamente incorrecta antes de la corrección final del operador en `charla_12` (§16.4).

### 16.2 — Estructura real según `plan.md`, verificada de nuevo en esta sesión

Confirmado por lectura directa de `plan.md` (extraído de `IRAM_PROYECTO_REORGANIZADO3.zip`, `IRAM_PROYECTO_REORGANIZADO/plan.md`, 27027 bytes, mtime 2026-07-05 05:01:48, md5 `7deea4e7c49bca89a1be68ad06cd1d7e` — mismo hash que verificó `charla_12`, sin cambios en el ZIP entre esa sesión y esta):

- **Objetivo 1 — Mod IRAM.** Producto: código jugable v5.6. Estado: cerrado.
- **Objetivo 2 — Documentación del proceso.** Productos: (a) Paper C1 corregido, (b) Skill C2 operacional. Estado: pendiente.
- **Objetivo 3 — Análisis A/B + Diplomatura UTN.** Productos, tal como los lista `plan.md` línea 32 textualmente: (a) base de hechos verificada, (b) Entregas Parte 1 y 2, (c) Portafolio GitHub. Estado: en diseño, bloqueado por DR-54.

Los "4 productos" que nombró el operador al abrir `charla_7` (mod, documentación, trabajo UTN, portafolio) no son 4 ítems de rango parejo — son una lectura de superficie de los 3 objetivos de `plan.md`, donde "documentación" es el objetivo 2 completo y "trabajo UTN" + "portafolio" son dos de los tres productos listados del objetivo 3. "Análisis" (la tercera "gran rama" que nombró el operador) no aparece como nombre propio en ningún documento — es el nombre que las cinco sesiones le fueron dando a la Fase 1 (`tabla_analisis.csv`), confirmado contra las dependencias reales de `plan.md`:

```
FASE 0 — Resolución de DR-54 (línea 70)
FASE 1 — Procesamiento de datos → tabla_analisis.csv (línea 188)
FASE 2 — Entrega Parte 1 UTN (línea 234) — Dependencia: Fase 1 completada (línea 236)
FASE 3 — Entrega Parte 2 UTN (línea 270) — Dependencia: Fase 2 completada (línea 272)
FASE 4 — Corrección Paper C1 + Skill C2 (línea 305) — Dependencia: Fase 1 completada (línea 307)
FASE 5 — Limpieza y cierre (línea 361)
```

Esto confirma con precisión lo que `charla_10` y `charla_11` encontraron de forma independiente: Fase 2 (UTN Parte 1) y Fase 4 (Documentación/C1/C2) dependen **ambas y únicamente** de Fase 1 — son ramas paralelas, no una cadena secuencial Mod→Análisis→Documentación→Portafolio como mostraba el SVG v1 (`estructura_objetivos_iram.svg`, el único adjuntado). Fase 3 depende de Fase 2 (con posible avance parcial en paralelo, según el propio texto de `plan.md` línea 272). El Portafolio GitHub no tiene fase propia en ningún punto de `plan.md` — confirmado por `grep -i "portafolio"` contra el archivo completo en esta sesión: aparece solo como nombre de carpeta (línea 9, 445), como ítem (c) del objetivo 3 (línea 32), como destino narrativo genérico ("parte central del portafolio y del paper", línea 49) y dentro del Anexo D (línea 524). Esto es consistente con el estado físico ya confirmado por `charla_7`: `3_PORTAFOLIO_UTN/` contiene únicamente los 3 archivos de consigna (`Consigna.md/pdf`, `Consigna_1.md/pdf`, `Consigna_2.md/pdf`) — cero trabajo entregado todavía.

### 16.3 — Hallazgo verificado: "6 meses / 101 sesiones" (Anexo D) es una sobreestimación de duración

`plan.md`, Anexo D (línea 499 en adelante, texto completo releído en esta sesión), lista como primera fortaleza del proyecto un *"estudio de caso longitudinal riguroso (6 meses, 101 sesiones)"*, y repite "6 meses" en una de las tres frases de pitch sugeridas (línea 527: *"Desarrollé un proyecto complejo de 6 meses trabajando 100% con IA generativa"*).

Verificado de forma independiente, con el mismo cálculo que hicieron `charla_10` y `charla_11` por separado (coincidencia entre ambas, y recalculado una tercera vez en esta sesión):

```
Fecha de inicio documentada (WIKI_DOCUMENTACION_v3.md, hito "primeros_scripts"): 2026-04-16
Fecha actual de esta sesión: 2026-07-08
Días transcurridos: 83
Meses aproximados (÷30.44): 2.73
```

`WIKI_DOCUMENTACION_v3.md` línea 11 dice explícitamente *"construido en ~2 meses"* — consistente con el cálculo de 83 días (~2.7 meses), no con los "6 meses" del Anexo D. La cifra del Anexo D es, por tanto, una sobreestimación de aproximadamente el doble. **Esto importa porque el Anexo D es, literalmente, texto de pitch ya redactado para el portafolio** (§16.2) — si se usa tal cual, hay una cifra objetivamente incorrecta que corregir antes de publicarlo. La cifra "101 sesiones" no se verificó independientemente en ninguna de las cinco sesiones ni en esta reconstrucción (requeriría contar entradas reales en el historial unificado o en la serie de `SESSION_LOG`, tarea no ejecutada) — se mantiene sin disputar pero sin confirmar, mismo tratamiento que le dio `charla_10`.

### 16.4 — Núcleo narrativo: el Anexo D ya responde la pregunta, con una cifra a corregir

Sobre la pregunta de núcleo narrativo del operador ("cómo aprendimos a trabajar con IA en un proyecto corto de múltiples sesiones"): el marco de "3 niveles" de `plan.md` (Nivel 1 = mod/vehículo, valor bajo como producto; Nivel 2 = documentación, valor alto como metodología replicable; Nivel 3 = análisis/metacognición, valor alto como caso de estudio académico) y el Anexo D convergen en la misma idea que propone el operador, ya redactada en tres frases de pitch (líneas 526-528, citadas también en §16.3) más una advertencia explícita de no vender el proyecto como *"hice un mod de Imperator: Rome"* (línea 531) porque eso es el vehículo, no el producto. La formulación del operador coincide en sustancia con lo que el propio plan ya trae escrito — con la corrección de cifra de §16.3 pendiente de aplicar antes de usar ese texto en el portafolio real.

### 16.5 — Correcciones de encuadre dadas por el operador en vivo, en esta sesión de reconstrucción

El operador corrigió dos veces el encuadre que traía la reconstrucción de `charla_12`, en este orden:

**Primera corrección — Objetivo 3 tiene 2 productos, no 3.** Contra la lectura literal de `plan.md` línea 32 (que lista tres ítems: base de hechos, entregas, portafolio), el operador estableció: las dos entregas UTN (Parte 1 y Parte 2) son continuación directa una de la otra — la Parte 2 construye sobre el diagnóstico y limpieza de datos que entrega la Parte 1 — y por tanto son **un solo producto en dos etapas**, no dos entregables paralelos. El Portafolio, a su vez, no es un tercer ítem al lado de las otras dos — es el trabajo más extenso, que engloba y presenta tanto el trabajo UTN como el resto del proyecto (documentación, metodología, estudio de caso completo). Esto no contradice el texto literal de `plan.md` — lo reagrupa: la "base de hechos verificada" no es un producto entregable aparte, es el insumo compartido (la propia Fase 1/`tabla_analisis.csv`) que alimenta tanto al trabajo UTN como a la documentación.

Estructura resultante de esta primera corrección:
- Objetivo 1 — Mod. Cerrado.
- Objetivo 2 — Documentación (Paper C1 + Skill C2). Pendiente.
- Objetivo 3 — Análisis A/B + Diplomatura, con 2 productos: (a) Trabajo UTN (Parte 1 → Parte 2, un solo producto en dos etapas), (b) Portafolio — el entregable mayor, que engloba tanto (a) como el objetivo 2 completo, no un tercer ítem paralelo.

Esto ajusta también la topología del diagrama: el "atajo" Análisis→Portafolio que marcaba el SVG v1 no debería ser un tercer brazo paralelo a Documentación — el Portafolio cuelga de todo lo demás (Trabajo UTN y Documentación juntos), no directamente de Fase 1/Análisis. La corrección de `charla_10`/`charla_11` (Documentación y Trabajo UTN como ramas paralelas de Fase 1) sigue siendo válida como primera capa de la topología; lo que agrega esta corrección es una segunda capa arriba: Portafolio como nodo final que absorbe ambas ramas, no como tercera rama al mismo nivel.

**Segunda corrección — "3 ángulos" como lectura alternativa, no como reemplazo.** El operador propuso después una relectura distinta, más liviana: el trabajo total tiene 3 ángulos — (1) el mod, con el código como producto; (2) su documentación de desarrollo, con logs, wikis y registros, sumando ahí Skill y Paper; (3) el metaanálisis del proyecto, que sería las dos tareas de la UTN más el portafolio. Esta lectura no contradice `plan.md` ni la primera corrección — los mismos 3 objetivos y sus mismos contenidos siguen ahí — pero cambia el criterio de agrupación: no "qué depende de qué" (que es como está armado el diagrama de dependencias de Fase 0-5) sino "qué tipo de trabajo es cada cosa" — código vs. registro del proceso vs. reflexión sobre el proceso. Bajo esta lectura, Skill y Paper se mueven al ángulo 2 (documentación) en vez de quedar como "objetivo 2 separado" del resto, y el Portafolio se mueve adentro del ángulo 3 (metaanálisis) junto con las dos entregas UTN, no como nodo aparte que las contiene desde afuera.

**Estado de la tensión entre los tres marcos, sin resolver silenciosamente:** quedan tres lecturas válidas y no idénticas del mismo material, útiles para propósitos distintos — (a) los 3 objetivos literales de `plan.md` con sus productos tal como los lista el documento; (b) la corrección por dependencias de esta sesión (Objetivo 3 con 2 productos, Portafolio como contenedor mayor de Trabajo UTN + Documentación); (c) los "3 ángulos" del operador, agrupados por tipo de trabajo en vez de por dependencia. Esta sección no elige una sobre las otras — las tres coexisten como marcos válidos, cada uno útil según la pregunta que se esté haciendo (¿qué falta hacer y en qué orden? → (b); ¿cómo se presenta el proyecto? → (c); ¿qué dice literalmente el documento fuente? → (a)).

### 16.6 — Estado de Caso #8 (fusión de la skill): sin cambios, sigue exactamente donde lo dejó `_8.md` §15.3

Ninguna de las cinco sesiones cortadas, ni esta reconstrucción, cerraron el Caso #8. `charla_8` sí llegó a producir una recomendación completa (elegir la base del 12/06 como C2 operacional, archivar `(2)/(3)` del 18/06 como insumo conceptual, no como descartada — ver §16.1), pero esa recomendación nunca fue confirmada ni rechazada por el operador antes de que la sesión se cortara por otro motivo (la corrección sobre qué archivos estaban en qué ZIP). El Caso #8 sigue, por tanto, en el mismo estado que registra `_8.md` §15.3: caracterizado, sin decisión. La recomendación de `charla_8` queda registrada acá como insumo disponible para cuando el operador decida retomarlo, no como decisión tomada.

### 16.7 — SVG pendiente de regenerar

El SVG corregido (`estructura_dependencias_iram_v2.svg`) que anunciaron `charla_10` y `charla_11` no existe como archivo — ninguna de las dos sesiones llegó a adjuntarlo antes de cortarse. Con la topología ya fijada en dos capas por la corrección del operador (§16.5: Fase 1 → {Documentación, Trabajo UTN} → Portafolio), la regeneración queda pendiente para cuando el operador la pida explícitamente — no se ejecuta en esta sección para mantener el foco de esta reconstrucción en el texto, verificado y citado, antes que en un artefacto visual nuevo.

### 16.8 — Tareas de §5 que esta sección resuelve o actualiza (append-only)

- **Tarea #14** (§5, componente skill / Caso #8): sin cambios de estado — sigue "Abierta". Se agrega como insumo disponible la recomendación de `charla_8` (§16.1, §16.6), sin darla por decidida.
- **Nueva nota, no numerada como tarea de §5 por no ser bloqueante ni accionable por sí sola:** la cifra "6 meses" del Anexo D de `plan.md` (línea 499, 527) queda documentada como sobreestimación verificada (§16.3) — a corregir manualmente en `plan.md` o en cualquier texto de portafolio que reutilice esa cita, antes de publicarla.

### 16.9 — Estado de los archivos entregables

Esta misma versión (`FUENTE_DE_VERDAD_IRAM_2026-07-07_9.md`) es el único artefacto nuevo de esta sesión, y se entrega como adjunto explícito en el mismo turno en que se termina de escribir, siguiendo la regla de continuidad ya vigente desde `_7`/`_8` — precisamente para no producir un octavo incidente de la misma familia que ya documentan §12, §13, §14 y esta misma sección (§16, séptimo incidente). El SVG corregido (§16.7) no se genera en esta sesión — queda pendiente, explícitamente, para cuando el operador lo pida.

---

## 17. RECONCILIACIÓN CRÍTICA #10 — Árbol definitivo de documentación: nueva tarea prioritaria, por encima de DR-54

**Disparador:** el operador señaló en vivo que los `SESSION_LOG_REPLANTEO_*` viven en la misma carpeta que no deberían, y pidió declarar como tarea prioritaria la construcción de un árbol definitivo de documentación, más la purga de archivos innecesarios. Se verificó el estado físico real contra `IRAM_PROYECTO_REORGANIZADO3.zip` en esta misma sesión (comandos ejecutados ahora, no heredados).

### 17.1 — El problema, confirmado con precisión

No es que los `SESSION_LOG_REPLANTEO_*` estén "en la carpeta equivocada" — es peor: **existen duplicados, en dos ubicaciones a la vez**:

- **Copia organizada** (correcta): `2_DOCUMENTACION/01_logs_replanteo/` — 15 archivos, incluyendo la serie completa del 19/06 al 05/07 (`SESSION_LOG_REPLANTEO_2026-07-03_02-43.md`, `..._17-58 2.md`, etc.).
- **Copia suelta** (incorrecta, redundante): 13 archivos con nombre idéntico o casi idéntico, sueltos directamente en la raíz del ZIP, fuera de `IRAM PROYECTO/` — entre ellos `SESSION_LOG_REPLANTEO_2026-07-05_01-37.md` (la fuente directa de DR-52/53/54, ya usada y citada en §16.2 de esta misma fuente de verdad) y `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (fuente de DR-10 a DR-26, citada desde §1).

Esta segunda copia no es un archivo más "de trabajo" — es la razón exacta por la que `charla_8` diagnosticó (incorrectamente, para el ZIP de esa sesión) que `plan.md` y el log de DR-52/53/54 "no estaban" en el proyecto: estaban, pero sueltos fuera de toda carpeta reconocible, no en `2_DOCUMENTACION/01_logs_replanteo/` donde el árbol organizado los esperaría. Es el mismo patrón de fuga que ya documentan §12/§13/§16, ahora visto desde el lado de la **estructura de carpetas** en vez del lado de "qué sesión subió qué".

### 17.2 — Inventario completo de lo que hay que ordenar, verificado en esta sesión

**A. Archivos sueltos en la raíz del ZIP (fuera de `IRAM PROYECTO/` por completo) — 46 archivos:**

| Categoría | Archivos | Destino probable |
|---|---|---|
| `SESSION_LOG_REPLANTEO_*` duplicados | 13 archivos, mismo contenido que ya vive en `01_logs_replanteo/` | Verificar que sean duplicados exactos (hash) y **borrar la copia suelta** |
| Versiones viejas de esta fuente de verdad | `FUENTE_DE_VERDAD_IRAM_2026-07-07.md`, `_2.md` (con espacio), `_3.md`, `_4.md`, `_5.md`, `_6.md`, `_7.md` — 7 archivos | Mover a una carpeta de histórico propia (p. ej. `2_DOCUMENTACION/00_fuente_de_verdad_historico/`), no borrar — son evidencia citable |
| Planes viejos (Qwen/DeepSeek) | `Qwen_markdown_20260705_q4xkzeqjf.md`, `deepseek_markdown_20260705_98aa15.md` y `(1).md` | Ya superados por `plan.md` — mover a histórico o purgar, a decidir |
| Volcados de memoria y pruebas de fuga | `memoria_claude_volcado.md`, `volcado_memoria.md`, `volcado_memoria (2).md`, `resultado_prueba_fuga_memoria.md`, `instruccion_prueba_fuga_memoria.md` | Ya absorbidos en `_8.md` §3/§13 (Paquete B) — mover a `2_DOCUMENTACION/03_prueba_fuga_memoria/`, que ya existe con 4 archivos, o purgar si son duplicados de lo que ya está ahí |
| Charlas 1-6 sueltas | `charla 1.md` a `charla 6.md` | Mismo tipo de material que `charla_7` a `charla_12` (no incluidas en el ZIP) — decidir una carpeta única de charlas/transcripciones para toda la serie |
| Logs de auditoría de continuidad y checklists | `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`, `...-07.md`, `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`, `PASO_0_grupos_divergentes_checklist.md` y `2.md`, `colisiones_verificadas_2026-07-06.txt` | Ya absorbidos por `_8.md` §6 — mover a una carpeta de auditoría propia o purgar si el contenido ya está capturado |
| Inventario y reorganización | `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`, `LOG_REORGANIZACION_2026-07-05.md`, `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md`, `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md` | Documentan la reorganización DR-51 — mover a histórico, no son operativos activos |
| Script y reporte suelto | `verificar_iram.py`, `reporte_resumen.txt`, `sigue log.md` | Sin clasificar en esta sesión — revisar contenido antes de decidir destino |

**B. `_CUARENTENA_DUPLICADOS/` — 544 archivos, sin decisión de destino desde `_2` (tarea #10 de §5, sigue abierta):**

- `documentacion iram 10-06-2026 00.30 (subcopia anidada)/` — 277 archivos
- `fuentes de documentacion (subcopia anidada)/` — 267 archivos

Son dos subcopias anidadas casi completas del proyecto, generadas en algún punto de la reorganización (DR-51) y nunca resueltas. Es el bloque más grande de todo lo pendiente de purgar.

**C. Carpetas ya organizadas dentro de `2_DOCUMENTACION/` (para referencia, sin cambios propuestos acá):** `01_logs_replanteo` (15), `02_charlas_y_resumenes` (6), `03_prueba_fuga_memoria` (4), `04_corpus_A_mod_docs` (10), `05_corpus_B_crudo` (28), `06_historial_desarrollo_mod` (13), `07_fuentes_documentacion` (161 — la carpeta más grande y la que ya contiene la mayoría de las contradicciones documentadas en `_8.md` §15, Paso 0), `08_documentacion_respaldo` (27).

### 17.3 — Nueva tarea prioritaria, por encima de DR-54

**Se declara tarea #19 de §5, con prioridad explícita por encima de la tarea #1 (DR-54)**, a pedido directo del operador:

| # | Tarea | Bloqueante? | Origen | Estado |
|---|---|---|---|---|
| 19 | **Construir el árbol definitivo de documentación**: (a) eliminar la duplicación de `SESSION_LOG_REPLANTEO_*` entre la raíz suelta y `01_logs_replanteo/`, dejando una sola copia vigente por archivo; (b) reubicar o purgar los 46 archivos sueltos de la raíz según la clasificación de §17.2.A; (c) decidir destino de los 544 archivos de `_CUARENTENA_DUPLICADOS/` (absorbe y cierra la tarea #10 de §5, ya no queda como ítem separado); (d) dejar un único árbol de carpetas documentado como estructura vigente, sin ambigüedad de "cuál es la copia real" para ningún archivo del proyecto. | **Sí — el operador la declara prioridad #1, por encima de DR-54.** Nota: esto invierte el orden de `plan.md` (que tenía esta tarea como Fase 5, no urgente) — se registra acá como corrección explícita de prioridad, no como error de `plan.md`, ya que `plan.md` no podía anticipar que la duplicación fuera a crecer hasta el tamaño confirmado en §17.2. | **NUEVO — esta sesión**, a pedido explícito del operador | Abierta — sin ejecutar, pendiente de sesión dedicada |

**Nota sobre el reordenamiento de prioridades:** esta tarea pasa a bloquear el resto del trabajo de facto, no porque tenga una dependencia técnica con DR-54 (no la tiene — son problemas independientes: uno es de estructura de carpetas, el otro es de diseño de tabla de análisis), sino porque el propio operador estableció el orden de trabajo para las próximas sesiones. Cualquier sesión que se abra después de esta debe tratar la tarea #19 como el primer punto del orden del día, y solo pasar a DR-54 (tarea #1) una vez que el árbol esté resuelto o el operador indique explícitamente lo contrario.

### 17.4 — Lo que esta sección no resuelve

Esta sección **inventaría y prioriza**, no ejecuta. No se movió, renombró ni borró ningún archivo del ZIP en esta sesión — hacerlo requiere una sesión dedicada con acceso de escritura real al proyecto (no solo lectura del ZIP adjuntado), y una decisión explícita del operador sobre cada categoría de la tabla de §17.2.A antes de tocar nada, siguiendo el mismo criterio de precaución que ya aplicó la tarea #10 original (DR-51: "decidir destino de `_CUARENTENA_DUPLICADOS/`, borrar o conservar" — nunca ejecutada sin confirmación explícita).

### 17.5 — Estado de los archivos entregables

Esta misma versión (`FUENTE_DE_VERDAD_IRAM_2026-07-07_10.md`) es el único artefacto nuevo de esta sesión, y se entrega como adjunto explícito en el mismo turno en que se termina de escribir — mismo estándar de continuidad que ya establecieron §12, §13, §14 y §16 (ahora octavo registro consecutivo de la misma disciplina, no un octavo incidente: esta vez el archivo se completa y se adjunta dentro del mismo turno).

---

*Este documento reemplaza como punto de partida operativo a toda la cadena citada en el encabezado, incluidas las versiones `_2` a `_9` de sí mismo. Se mantiene la regla append-only (DR-42) hacia adelante: la próxima actualización de este documento debe cotejar ítem por ítem contra esta versión, no reescribir de memoria.*
