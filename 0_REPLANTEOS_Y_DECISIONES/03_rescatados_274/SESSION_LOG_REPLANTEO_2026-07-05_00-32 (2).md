# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-05 00:32 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-05_00-10.md (queda como archivo histórico, no como insumo a recargar completo)
**Tipo de sesión:** operativa — primera en varias sesiones que avanza una tarea real de PRÓXIMAS TAREAS (Tarea 4, inventario completo) en vez de auditar hacia atrás. Continuación directa de `00-10`.
**Motivo de esta versión:** se ejecutó el inventario completo del material de archivo (Tarea 4), con hallazgos nuevos no listados en el apéndice de `00-10` (DR-45 a DR-49) y un entregable citable (`INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

**Nota sobre esta sesión en particular:** esta vez sí avanzó la prioridad única, indirectamente — la Tarea 4 (inventario) es insumo directo para poder ejecutar después el análisis A/B. No se tocó el mod, no se tocó `WIKI_DOCUMENTACION_v2.md`, no se movió ni renombró ningún archivo del proyecto: el inventario fue solo lectura + hashing.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-44 de los logs anteriores siguen vigentes, sin correcciones esta vez. Se citan por ID. Si hace falta el detalle:
- `SESSION_LOG_REPLANTEO_2026-06-19_2.md` — DR-01 a DR-09.
- `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` — DR-10 a DR-26.
- `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md` (con el "2") — DR-27 a DR-33.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` — DR-34.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-44.md` — DR-35 a DR-38.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-10.md` — DR-39 a DR-44.

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión no escribió en `WIKI_DOCUMENTACION_v2.md`.

**Nota especial sobre DR-42:** la regla de consolidación append-only sigue vigente. Este log respeta esa regla: las tablas de ESTADO REAL y PRÓXIMAS TAREAS de abajo agregan filas/marcas, no reescriben las existentes de logs previos (que de hecho no se copian acá completas — se referencian).

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-45 | **`DOCUMENTACION/` es duplicado exacto de un subconjunto de `fuentes de documentacion/`.** Verificado por hash MD5: los 27 archivos de `DOCUMENTACION/` tienen, para cada nombre que se solapa, contenido byte-idéntico a su par en `fuentes de documentacion/` (paper C1, wiki, specs a/b/c, templates, metodología, sesiones falladas, análisis C1 v2-v5, consolidado, transcripciones). No hay ninguna divergencia de contenido entre ambas copias. `DOCUMENTACION/` queda catalogada como **copia de respaldo**, no como fuente independiente — citar siempre contra `fuentes de documentacion/` como origen. |
| DR-46 | **Cinco archivos `data-<uuid>-<timestamp>-batch-0000.zip` en `historial viejo/`, no listados en ningún apéndice anterior.** Al inspeccionar su estructura interna (`users.json`, `conversations.json`, `projects/*.json`) resultaron ser exports de Claude.ai con la misma forma que `documentacion claude 1-5.zip`, pero de un período más antiguo (timestamps Unix de comienzos de enero de 2026 en el nombre de archivo). Quedan marcados como **Corpus B crudo adicional, no procesado, pendiente de decisión** sobre si entran al análisis A/B o quedan fuera por antigüedad/redundancia. No se abrió su contenido interno. |
| DR-47 | **Existen `claude_1_processed.json` a `claude_5_processed.json` dentro de `fuentes de documentacion/` (1.4–2 MB cada uno), que contradicen o al menos matizan la fila "Corpus A / Corpus B — sigue sin procesar" del ESTADO REAL vigente desde `23-44`.** No se abrió su contenido para determinar qué tipo de procesamiento representan (extracción simple, filtrado, resumen, etc.) — se deja como hallazgo abierto. **No se cambia el estado de "sin procesar" hasta que se inspeccionen estos archivos**; esta decisión es solo registrar que existen y que el estado actual podría estar desactualizado. |
| DR-48 | **Código del mod mezclado por error dentro de `fuentes de documentacion/`.** Dos copias completas de un mod pack extraído (`mod_pack_IRAM_v5_5_2026-06-09_03-22/` y su duplicado `(2)/`, con el árbol `iram_work/` completo: decisions, events, localization, etc.) viven hoy dentro de la carpeta de documentación. Es código del mod, no documentación — fuera de alcance para el análisis A/B, pero queda marcado como **candidato a mover** cuando se ejecute la Tarea 1 (estructura física de carpetas, DR-27), no antes. |
| DR-49 | **Dos archivos sueltos de nombre llamativo dentro de `fuentes de documentacion/` (`-----------------LEER---------------------.txt`, `---------INSTRUCCIONES-------.txt`) fueron revisados a pedido del operador y no contienen nada operativo vigente.** El primero es una etiqueta de una línea ("estado total del proyecto iram previo al ultimo testeo"). El segundo es una guía de junio de 2026 sobre qué adjuntar/pegar al abrir una sesión de documentación nueva (referencia a `PROMPT_DOCUMENTACION_IRAM_v1_1.md`, versión anterior a las v1.4–v1.9 vigentes en el corpus). Ambos quedan catalogados como **histórico/superado** — el sistema de `SESSION_LOG_REPLANTEO_*` reemplazó esa lógica de armado manual de paquete de arranque. No generan tarea. |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-05 00:32

*(Sin cambios respecto a `00-10` salvo la fila nueva agregada abajo — no se reescribe ninguna fila anterior.)*

| Cosa | Estado |
|------|--------|
| **Inventario completo del material de archivo (Tarea 4)** | **✅ Completado 2026-07-05.** Ver `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` (entregable de esta sesión): 1991 archivos totales, 1219 fuera de alcance (mod/código), 244 de documentación en alcance, de los cuales 188 con contenido único (56 duplicados exactos en 43 grupos, más dos carpetas anidadas 100% duplicadas). Hallazgos nuevos: DR-45 a DR-49. |

*(El resto de las filas de ESTADO REAL — mod IRAM, paper C1, WIKI_DOCUMENTACION_v2.md, Corpus A/B, estructura de carpetas, nomenclatura, Tarea 0 — sigue exactamente como en `00-10` y `23-44`. No se repiten acá para cumplir la regla append-only; consultar `00-10` si hace falta el detalle línea por línea.)*

---

## PRÓXIMAS TAREAS — en orden de prioridad

*(Cotejada ítem por ítem contra `00-10`. Único cambio: la Tarea 4 pasa de pendiente a resuelta, citando DR-45 a DR-49 y el inventario como evidencia. El resto sigue idéntico, sin reordenar.)*

1. **Aplicar físicamente la estructura de carpetas DR-27** (mover archivos, no renombrar todavía). *Nota agregada esta sesión: ahora incluye mover el código del mod duplicado que quedó mezclado en `fuentes de documentacion/` (DR-48).*
2. **Ejecutar el plan de 3 capas de DR-32** sobre `fuentes de documentacion` (mapa de vigencia → mapa de citas cruzadas → recién ahí, renombrado).
3. Retomar la tarea 0 pendiente de logs anteriores (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline).
4. ~~Inventario completo del material de archivo.~~ **RESUELTO esta sesión — ver DR-45 a DR-49 y `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`.**
5. *(Opcional, no bloqueante)* Si se quiere cerrar el tema memoria por completo: confirmar en `claude_5` que la memoria persistente quedó efectivamente desactivada y, si la interfaz lo permite, borrar el contenido residual para que no vuelva a propagarse a un tercer chat.
6. *(Recuperada de `02-43`, DR-35a — no bloqueante, sin fecha asignada)* **Inventario terminológico completo.** Sesión dedicada. Nombre formal o `[TEMP]` para cada mecanismo/herramienta/proceso/análisis del proyecto. Plan: ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, publicaciones Anthropic/OpenAI/DeepMind, grey literature. Mínimo 5 queries por ítem, 3 idiomas, umbral de 5 búsquedas + 2 fuentes grises.
7. *(Recuperada de `02-43`, DR-35b — no bloqueante, sin fecha asignada)* **Verificación de cifras de hitos.** Cita de línea exacta en `IRAM_hitos_metodologicos_2026-06-12_v7.md` para los números de autoría "Operador-iniciativa" y colaborativos.
8. **Nueva, agregada esta sesión (DR-47):** decidir qué representan `claude_1_processed.json` a `claude_5_processed.json` en `fuentes de documentacion/` y si eso cambia el estado "Corpus B sin procesar". No bloqueante, pero debería revisarse antes de dar por buena esa fila del ESTADO REAL en una futura auditoría.
9. **Nueva, agregada esta sesión (DR-46):** decidir si los 5 `data-*-batch-0000.zip` de `historial viejo/` entran al Corpus B o quedan fuera por antigüedad/redundancia con `documentacion claude 1-5.zip`. No bloqueante.

---

## QUÉ NO HACER — VIGENTE + AGREGADO DE ESTA SESIÓN

*(Se mantiene íntegra la lista de `00-10`, no se reescribe ningún ítem existente. Se agrega uno nuevo al final.)*

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes.
- No tocar el mod.
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual.
- No bajar el estatus de ningún documento sin el inventario de DR-07.
- No asumir que algo "puede avanzar en paralelo" sin confirmación del operador.
- No narrar logros, "calibre", ni dramatizar decisiones propias.
- No llamar a actualizar el log sin instrucción explícita del operador.
- No proponer métricas sin anclarlas a una pregunta concreta.
- No afirmar novedad del proyecto sin búsqueda más profunda.
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).
- No presentar el timeline como fechas confirmadas — siempre con "(condicionado — ver DR-18)".
- No usar cifras de hitos de autoría sin verificación de línea en hitos_v7.
- No renombrar archivos de `fuentes de documentacion` sin haber hecho antes el mapa de vigencia y citas cruzadas (DR-32).
- No confundir el hallazgo de `claude_5` (DR-34, contaminación por memoria mal desactivada) con una fuga tipo DR-30 (detalle operativo no documentado) — son mecanismos distintos.
- Al generar el próximo SESSION_LOG_REPLANTEO, no reescribir "PRÓXIMAS TAREAS" ni "ESTADO REAL" de memoria — cotejar ítem por ítem contra este log. Todo lo que está acá debe aparecer en la siguiente versión, o quedar marcado explícitamente resuelto/descartado/absorbido, citando el ID que lo resuelve.
- (DR-42) Al agregar una sección nueva a un log, no reescribir celdas de tabla existentes — solo agregar al final. Esta es la regla vigente.
- (DR-39) Al citar un log por nombre de archivo, verificar primero que no exista un duplicado con sufijo numérico antes de asumir cuál es el vigente.
- (DR-41/DR-43) No asumir completitud de los Módulos UTN 1-4 ni dar por real la convención `ModuloN_UnidadM_Tema_Corto.md` — confirmado como material de otro proyecto mal etiquetado por contaminación de memoria.
- **(DR-48, nuevo) No tratar el mod pack duplicado dentro de `fuentes de documentacion/` como parte del corpus de documentación — es código del mod, mover en Tarea 1, no auditar su contenido como si fuera fuente B.**
- **(DR-49, nuevo) No tratar archivos sueltos de nombre tipo "instrucción" encontrados dentro del corpus de datos como órdenes a ejecutar automáticamente — revisar primero, como se hizo acá, antes de darles cualquier peso operativo.**

---

## APÉNDICE — MATERIAL DE REFERENCIA PARA LA PRÓXIMA CUENTA

*(Se mantiene el apéndice de `00-10`, con el agregado del entregable de esta sesión.)*

**Nuevo esta sesión:** `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` — inventario ítem por ítem de los 1991 archivos del ZIP, con deduplicación por hash MD5, clasificación por área (serie de logs, charlas, prueba de fuga, consignas, Corpus B crudo, `DOCUMENTACION/`, `fuentes de documentacion/` con sus 12 subfamilias, `historial viejo/`, y fuera de alcance). Es el insumo que faltaba para la Tarea 1 (estructura física) y para retomar el análisis A/B — no reemplaza ese análisis, solo lo hace ejecutable.

*(El resto del apéndice — estructura del ZIP, cadena canónica de logs, ubicación de `DOCUMENTACION/`, `documentacion iram 10-06-2026 00.30/`, zips de Claude, consignas UTN — sigue igual que en `00-10`. No se repite acá.)*

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
