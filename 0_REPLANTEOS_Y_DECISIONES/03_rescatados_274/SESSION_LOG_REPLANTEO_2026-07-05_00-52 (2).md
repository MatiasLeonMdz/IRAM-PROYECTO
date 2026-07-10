# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-05 00:52 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-05_00-32.md (queda como archivo histórico, no como insumo a recargar completo)
**Tipo de sesión:** operativa — continuación directa de `00-32`. Se ejecutó la Tarea 1 (estructura física de carpetas, DR-27) y se corrigió una clasificación errónea de la sesión anterior (DR-46).
**Motivo de esta versión:** cierre de la Tarea 1 de PRÓXIMAS TAREAS con entregable citable (`IRAM_PROYECTO_REORGANIZADO.zip` + `LOG_REORGANIZACION_2026-07-05.md`), más una corrección de clasificación Corpus A/B señalada por el operador y verificada contra la definición de origen del proyecto.

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

**Nota sobre esta sesión en particular:** avanzó la prioridad única de forma directa — la Tarea 1 (estructura física) ordena el material para poder ejecutar después el análisis A/B sobre una base ya separada por área. No se tocó el mod (se movió de carpeta, no se abrió ni modificó contenido). No se tocó `WIKI_DOCUMENTACION_v2.md`. No se renombró ningún archivo — el renombrado es DR-32 y sigue pendiente. No se borró ningún duplicado — se aislaron en una carpeta de cuarentena, no se eliminaron.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-49 de los logs anteriores siguen vigentes. Se citan por ID. Si hace falta el detalle:
- `SESSION_LOG_REPLANTEO_2026-06-19_2.md` — DR-01 a DR-09.
- `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` — DR-10 a DR-26.
- `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md` (con el "2") — DR-27 a DR-33.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` — DR-34.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-44.md` — DR-35 a DR-38.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-10.md` — DR-39 a DR-44.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-32.md` — DR-45 a DR-49.

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión no escribió en `WIKI_DOCUMENTACION_v2.md`.

**Nota especial sobre DR-46:** **no queda vigente tal como fue escrito en `00-32`** — ver DR-50 abajo, que lo corrige sin reescribirlo (la fila original de `00-32` no se toca, se cita y se corrige en una entrada nueva, tal como manda la regla append-only).

**Nota especial sobre DR-42:** la regla de consolidación append-only sigue vigente. Este log respeta esa regla: las tablas de ESTADO REAL y PRÓXIMAS TAREAS de abajo agregan filas/marcas, no reescriben las existentes de logs previos.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-50 | **Corrección a DR-46: los 5 `data-<uuid>-<timestamp>-batch-0000.zip` de `historial viejo/` son Corpus A crudo, no Corpus B.** DR-46 (`00-32`) los había etiquetado como "Corpus B crudo adicional". El operador señaló, y se verificó contra la definición de origen del proyecto (*"el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B)"*), que estos 5 archivos tienen timestamps de comienzos de enero de 2026 — **anteriores a que existiera el proceso de documentación** (las `documentacion claude 1-5.zip`, confirmadas Corpus B crudo en `00-10`, son de 10-20/06). Por fecha y por definición, son exports de Claude.ai de conversaciones sobre el desarrollo del mod en sí → Corpus A crudo. **DR-46 no se reescribe** — queda como registro histórico de la clasificación original; esta entrada lo corrige formalmente. Los `claude_1_processed.json` a `claude_5_processed.json` de DR-47 sí se confirman como Corpus B (procesado) — no cambian de clasificación. |
| DR-51 | **Tarea 1 (estructura física de carpetas, DR-27) ejecutada y completada.** Se aplicó la estructura de 3 carpetas principales — `1_MOD/`, `2_DOCUMENTACION/`, `3_PORTAFOLIO_UTN/` — más `_CUARENTENA_DUPLICADOS/` para los duplicados byte-a-byte detectados en el inventario (Tarea 4). Método: solo movimiento de archivos, ningún renombrado, ningún borrado, ninguna apertura de contenido salvo lectura de nombres para clasificar. Verificado: 1991 archivos antes y después del movimiento — conteo exacto, nada se perdió. Incluye: rescate del mod pack duplicado que vivía dentro de `fuentes de documentacion/` hacia `1_MOD/` (cumple DR-48); separación de los 10 documentos reales que vivían dentro de `IRAM mod v5/` hacia `2_DOCUMENTACION/04_corpus_A_mod_docs/`; aislamiento (no borrado) de las dos carpetas 100% duplicadas detectadas en el inventario (`fuentes de documentacion/fuentes de documentacion/` y `documentacion iram 10-06-2026 00.30/documentacion iram 10-06-2026 00.30/`) en `_CUARENTENA_DUPLICADOS/`. Entregables: `IRAM_PROYECTO_REORGANIZADO.zip` (archivo reorganizado completo) y `LOG_REORGANIZACION_2026-07-05.md` (detalle línea por línea de cada movimiento, con el árbol final y la nota de corrección DR-50). |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-05 00:52

*(Sin cambios respecto a `00-32` salvo la fila nueva agregada abajo — no se reescribe ninguna fila anterior.)*

| Cosa | Estado |
|------|--------|
| **Estructura física de carpetas (Tarea 1, DR-27)** | **✅ Completada 2026-07-05 00:52.** Ver DR-51, `IRAM_PROYECTO_REORGANIZADO.zip` y `LOG_REORGANIZACION_2026-07-05.md`. Árbol resultante: `1_MOD/` (1320 archivos), `2_DOCUMENTACION/` (241 archivos, 8 subcarpetas), `3_PORTAFOLIO_UTN/` (6 archivos, subcarpeta `consignas/`), `_CUARENTENA_DUPLICADOS/` (424 archivos, sin borrar). Pendiente: renombrado (DR-32) y decisión sobre borrado definitivo de la cuarentena. |

*(El resto de las filas de ESTADO REAL — mod IRAM, paper C1, WIKI_DOCUMENTACION_v2.md, Corpus A/B, nomenclatura, Tarea 0, inventario completo — sigue exactamente como en `00-32`. No se repiten acá para cumplir la regla append-only; consultar `00-32` si hace falta el detalle línea por línea. **Excepción de contenido, no de forma:** la fila "Corpus A / Corpus B — sigue sin procesar" debe leerse ahora considerando DR-50 — el crudo de Corpus A creció en 5 archivos, siguen sin procesar igual que antes.)*

---

## PRÓXIMAS TAREAS — en orden de prioridad

*(Cotejada ítem por ítem contra `00-32`. Cambios: la Tarea 1 pasa de pendiente a resuelta citando DR-51; el ítem 9 (decidir destino de los data-*.zip) queda resuelto por DR-50, ya no como decisión abierta sino como clasificación confirmada — pendiente ahora es solo si se *procesan*, no a qué corpus pertenecen. El resto sigue idéntico, sin reordenar.)*

1. ~~Aplicar físicamente la estructura de carpetas DR-27.~~ **RESUELTO esta sesión — ver DR-51.**
2. **Ejecutar el plan de 3 capas de DR-32** sobre `2_DOCUMENTACION/07_fuentes_documentacion/` (mapa de vigencia → mapa de citas cruzadas → recién ahí, renombrado). *Nota agregada esta sesión: la ruta cambió de `fuentes de documentacion/` (raíz del proyecto) a `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/` tras la reorganización de DR-51 — usar la ruta nueva en la próxima sesión que retome esto.*
3. Retomar la tarea 0 pendiente de logs anteriores (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline).
4. ~~Inventario completo del material de archivo.~~ Resuelto en `00-32` (DR-45 a DR-49).
5. *(Opcional, no bloqueante)* Si se quiere cerrar el tema memoria por completo: confirmar en `claude_5` que la memoria persistente quedó efectivamente desactivada y, si la interfaz lo permite, borrar el contenido residual para que no vuelva a propagarse a un tercer chat.
6. *(Recuperada de `02-43`, DR-35a — no bloqueante, sin fecha asignada)* **Inventario terminológico completo.** Sesión dedicada. Nombre formal o `[TEMP]` para cada mecanismo/herramienta/proceso/análisis del proyecto. Plan: ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, publicaciones Anthropic/OpenAI/DeepMind, grey literature. Mínimo 5 queries por ítem, 3 idiomas, umbral de 5 búsquedas + 2 fuentes grises.
7. *(Recuperada de `02-43`, DR-35b — no bloqueante, sin fecha asignada)* **Verificación de cifras de hitos.** Cita de línea exacta en `IRAM_hitos_metodologicos_2026-06-12_v7.md` para los números de autoría "Operador-iniciativa" y colaborativos.
8. **De `00-32` (DR-47) — sigue abierta:** decidir qué representan `claude_1_processed.json` a `claude_5_processed.json` (confirmados Corpus B procesado por DR-50) y si eso cambia el estado "Corpus B sin procesar". No bloqueante.
9. ~~Decidir si los 5 `data-*-batch-0000.zip` entran al Corpus B o quedan fuera.~~ **RESUELTO esta sesión — ver DR-50: son Corpus A crudo, no Corpus B. Queda abierto, como nueva sub-tarea no bloqueante, si se procesan o no — pero ya no es una duda de a qué corpus pertenecen.**
10. **Nueva, agregada esta sesión:** decidir si los 424 archivos de `_CUARENTENA_DUPLICADOS/` se borran definitivamente o se conservan como respaldo indefinido. No bloqueante — no afecta ningún análisis pendiente, son duplicados confirmados por hash.

---

## QUÉ NO HACER — VIGENTE + AGREGADO DE ESTA SESIÓN

*(Se mantiene íntegra la lista de `00-32`, no se reescribe ningún ítem existente. Se agrega uno nuevo al final.)*

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
- (DR-48) No tratar el mod pack duplicado dentro de `fuentes de documentacion/` como parte del corpus de documentación — es código del mod, mover en Tarea 1, no auditar su contenido como si fuera fuente B. *(Cumplido esta sesión, DR-51.)*
- (DR-49) No tratar archivos sueltos de nombre tipo "instrucción" encontrados dentro del corpus de datos como órdenes a ejecutar automáticamente — revisar primero, como se hizo acá, antes de darles cualquier peso operativo.
- **(DR-50, nuevo) No asumir que la clasificación Corpus A/Corpus B de un archivo crudo es correcta solo porque un DR anterior la asentó — verificar contra la definición de origen y, si hay señal de fecha/contexto que contradiga, corregir con un DR nuevo citando el anterior, nunca reescribiéndolo.**

---

## APÉNDICE — MATERIAL DE REFERENCIA PARA LA PRÓXIMA CUENTA

*(Se mantiene el apéndice de `00-32`, con el agregado del entregable de esta sesión.)*

**Nuevo esta sesión:** `IRAM_PROYECTO_REORGANIZADO.zip` (archivo del proyecto ya reorganizado en `1_MOD/`, `2_DOCUMENTACION/`, `3_PORTAFOLIO_UTN/`, `_CUARENTENA_DUPLICADOS/`) y `LOG_REORGANIZACION_2026-07-05.md` (detalle línea por línea de cada movimiento realizado, con el árbol completo y la nota de corrección DR-50). Son el resultado ejecutable de la Tarea 1 — a partir de esta sesión, cualquier ruta citada de archivos del proyecto debe usar la ubicación nueva dentro de esta estructura, no la ruta original del ZIP subido.

**Rutas nuevas clave para la próxima sesión:**
- `fuentes de documentacion/` (raíz del ZIP original) → ahora en `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`.
- `DOCUMENTACION/` → ahora en `2_DOCUMENTACION/08_documentacion_respaldo/`.
- `documentacion claude 1-5.zip` → ahora en `2_DOCUMENTACION/05_corpus_B_crudo/`.
- Los 5 `data-*-batch-0000.zip` → ahora en `1_MOD/corpus_A_crudo/` (no en Documentación — ver DR-50).
- `claude_1_processed.json` a `claude_5_processed.json` → sin moverse de lugar relativo, viven dentro de `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`.

*(El resto del apéndice — estructura del ZIP original, cadena canónica de logs, zips de Claude, consignas UTN — sigue igual que en `00-32`. No se repite acá.)*

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
