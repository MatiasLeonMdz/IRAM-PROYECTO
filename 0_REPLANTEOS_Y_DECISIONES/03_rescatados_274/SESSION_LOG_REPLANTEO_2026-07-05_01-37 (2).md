# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-05 01:37 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-05_00-52.md (queda como archivo histórico, no como insumo a recargar completo)
**Tipo de sesión:** conceptual — no se tocó ningún archivo del proyecto, ninguna carpeta, ningún corpus. Fue una sesión de diseño sobre la relación entre objetivos y productos, motivada por una revisión de claridad de la documentación pedida por el operador.
**Motivo de esta versión:** corrección del encuadre de Paper C1 y Skill C2 respecto a los 3 objetivos / 4 productos del proyecto (DR-52), cierre de la nota de vínculo diplomatura↔pipeline que seguía abierta desde `02-43` (DR-53), e identificación de un vacío nuevo y bloqueante: el mapeo entre el diseño de métricas existente y el formato concreto que exige la Consigna 1 de la UTN nunca se hizo (DR-54, sin resolver, a debatir en sesión dedicada).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

**Nota especial sobre esta línea, agregada esta sesión (no se reescribe, se aclara):** la frase "generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science" ya no debe leerse como tres cosas del mismo nivel saliendo del análisis. Ver DR-52: C1 y C2 son productos del objetivo 2 (Documentación), no usos paralelos del objetivo 3 (Análisis). Se corrigen con la base de hechos del análisis y **después** sirven de insumo para el portfolio y el trabajo UTN. Esta línea se mantiene sin editar por la regla append-only; la relectura correcta está en DR-52.

**Nota sobre esta sesión en particular:** no avanzó ninguna tarea operativa de la lista (no se procesó corpus, no se tocó carpeta, no se corrigió el paper). Avanzó exclusivamente el diseño conceptual de cómo se relacionan los productos entre sí, a partir de una pregunta del operador sobre claridad de la documentación. Ese diseño resultó en un hallazgo con consecuencia operativa real: DR-54 bloquea el diseño detallado del análisis hasta que se resuelva.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-51 de los logs anteriores siguen vigentes, con una corrección de encuadre puntual esta sesión (ver DR-52 — no anula DR-11/DR-25/DR-26, les corrige el encuadre respecto a C1/C2). Se citan por ID. Si hace falta el detalle:
- `SESSION_LOG_REPLANTEO_2026-06-19_2.md` — DR-01 a DR-09.
- `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` — DR-10 a DR-26. **(DR-11, DR-25, DR-26 — ver nota de encuadre en DR-52 de esta sesión.)**
- `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md` (con el "2") — DR-27 a DR-33.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` — DR-34.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-44.md` — DR-35 a DR-38.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-10.md` — DR-39 a DR-44.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-32.md` — DR-45 a DR-49.
- `SESSION_LOG_REPLANTEO_2026-07-05_00-52.md` — DR-50 a DR-51.

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión no tocó `WIKI_DOCUMENTACION_v2.md`.

**Nota especial sobre DR-42:** la regla de consolidación append-only sigue vigente. Este log respeta esa regla: no se reescribe ninguna celda de tabla existente de sesiones anteriores.

**Nota especial sobre DR-11/DR-25/DR-26:** siguen vigentes como registro histórico de cómo se pensó la relación C1/C2/portfolio hasta esta sesión. DR-52 no las borra ni las contradice de fondo — corrige específicamente el punto en que trataban a C1 y C2 como "usos parejos" del análisis del objetivo 3, cuando en realidad son productos del objetivo 2 que el análisis corrige antes de que sirvan de insumo a los productos del objetivo 3.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-52 | **Encuadre corregido de Paper (C1) y Skill (C2): son productos del objetivo 2 (Documentación), no un uso paralelo del análisis del objetivo 3.** Tabla fija de objetivo→producto: (1) Mod IRAM → archivos del mod. (2) Documentación del proceso → (a) documentación técnica, (b) Paper C1, (c) Skill C2. (3) Análisis A/B → (a) base de hechos verificada, (b) Trabajo UTN, (c) Portafolio de data science. Paper C1 existe (`IRAM_C1_final.md`, cerrado en s34, con 2 afirmaciones sin verificar: S4A y S5). Skill C2 no existe todavía. Ninguno de los dos es un entregable final ni un cuarto/quinto producto: son **auxiliares** de Trabajo UTN y Portafolio — auxiliar significa que este par se usa como material de apoyo, no que se escriban desde cero. Orden de dependencia obligatorio, no saltear pasos: (1) procesar Corpus A/B → base de hechos del objetivo 3 → (2) corregir S4A/S5 del Paper C1 con esa base de hechos → (3) generar Skill C2 con esa misma base de hechos → (4) usar Paper C1 corregido + Skill C2 + base de hechos como insumo del Trabajo UTN → (5) ídem para el Portafolio. Corrige el encuadre de DR-11 y DR-26 (que trataban a C1, C2 y portfolio como "tres usos parejos" del mismo análisis) sin reescribirlas. |
| DR-53 | **DR-52 resuelve la nota de vínculo diplomatura↔pipeline que quedó abierta en `02-43` (Tarea 0) y sin cerrar hasta `00-52`.** Esa nota preguntaba cómo se conecta el trabajo de la diplomatura UTN con el pipeline del análisis; nunca se había repreguntado ni resuelto explícitamente (`02-43` decía "puede que ya no haga falta una nota aparte [...] repreguntar antes de dar por cerrado este punto"). Con el orden de dependencia de DR-52 (pipeline → corrige C1/C2 → alimenta UTN/Portafolio), la pregunta tiene respuesta: el vínculo es que el pipeline corrige el material de documentación (C1/C2) antes de que ese material sirva de insumo a la diplomatura. Esta nota de Tarea 0 queda cerrada. **Sigue abierto, sin cambios, el otro sub-punto de Tarea 0:** los umbrales/indicadores concretos del criterio B de DR-26 (% de cobertura del corpus, completitud de timestamps) — DR-53 no lo toca. |
| DR-54 | **Vacío identificado, bloqueante, sin resolver: no existe mapeo entre el diseño de métricas ya acordado (Grupo 1/2/3, Framework B — todos de `02-43`) y el formato concreto que exige la Consigna 1 de la diplomatura UTN.** La consigna real (`Consigna_1.md`) pide una única tabla con mínimo 50 filas, 3 preguntas de EDA respondidas con datos, 2 gráficos, y un enfoque de Machine Learning (clasificación / regresión / agrupamiento) con variables de entrada explícitas. Ningún DR anterior define: (a) qué es una fila de esa tabla, (b) cuáles son las 3 preguntas de EDA exactas, (c) cuáles son las columnas, (d) cuál de los tres enfoques de ML aplica y con qué variables. Este vacío **condiciona el diseño de todo lo demás** — qué exporta el pipeline, qué corrige el Paper C1 con datos reales (DR-52), qué entrena la Skill C2, qué entra en la Entrega 1 de la UTN y en el Portafolio. **No resuelto en esta sesión — el operador pidió tratarlo en una charla aparte, más profunda.** Se discutió una propuesta preliminar, **no confirmada, solo como punto de partida para esa próxima sesión**: unidad de fila = decisión codificada (Framework B); columnas candidatas = corpus (A/B), fase, categoría de autoría (Framework B), fecha/sesión, presencia de patrón DR-08, presencia de patrón DR-09; 3 preguntas de EDA candidatas ancladas a DR-16 (proporción de autoría operador/IA por corpus; fase donde más aparecen DR-08/DR-09; intensidad de trabajo en el tiempo vs. picos de fricción del ciclo de vida); enfoque de ML candidato = clasificación (predecir categoría de autoría a partir de features de la decisión). **Ninguno de estos cuatro puntos está confirmado.** |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-05 01:37

*(Sin cambios respecto a `00-52` salvo la fila nueva agregada abajo — no se reescribe ninguna fila anterior.)*

| Cosa | Estado |
|------|--------|
| **Relación Paper C1 / Skill C2 con objetivos y productos** | **Corregida esta sesión — ver DR-52.** Deja de ser "uso paralelo del análisis" y pasa a ser "producto del objetivo 2, auxiliar de los productos del objetivo 3, con corrección obligatoria vía la base de hechos como paso intermedio". |
| **Nota de vínculo diplomatura↔pipeline (Tarea 0, abierta desde `02-43`)** | **Cerrada esta sesión — ver DR-53.** |
| **Mapeo diseño de métricas ↔ formato exigido por Consigna 1 UTN** | **Nuevo, sin resolver — ver DR-54.** Bloqueante para el diseño detallado del análisis. Sesión dedicada pendiente de agendar. |

*(El resto de las filas de ESTADO REAL sigue exactamente como en `00-52`. No se repiten acá para cumplir la regla append-only.)*

---

## PRÓXIMAS TAREAS — en orden de prioridad

*(Cotejada ítem por ítem contra `00-52`. Cambios: el sub-punto "nota de vínculo diplomatura↔pipeline" del ítem 3 queda resuelto por DR-53 — el resto del ítem 3, sin cambios. Se agrega un ítem nuevo, marcado bloqueante, al final de la lista de no-bloqueantes porque es justamente lo opuesto — pero se deja al final por orden de aparición cronológica, no por prioridad real: **es, en los hechos, la tarea de mayor prioridad de toda la lista**, ver nota.)*

1. ~~Aplicar físicamente la estructura de carpetas DR-27.~~ **RESUELTO — ver DR-51.**
2. **Ejecutar el plan de 3 capas de DR-32** sobre `2_DOCUMENTACION/07_fuentes_documentacion/`. Sin cambios.
3. Retomar la tarea 0 pendiente de logs anteriores. **Sub-punto "nota de vínculo diplomatura↔pipeline": RESUELTO — ver DR-53.** Sigue abierto el sub-punto "umbrales concretos del criterio B (DR-26)" — sin cambios, no bloqueante.
4. ~~Inventario completo del material de archivo.~~ Resuelto en `00-32`.
5. *(Opcional, no bloqueante)* Cierre del tema memoria en `claude_5`.
6. *(No bloqueante)* Inventario terminológico completo.
7. *(No bloqueante)* Verificación de cifras de hitos.
8. *(No bloqueante)* Decidir qué representan `claude_1_processed.json` a `claude_5_processed.json`.
9. ~~Decidir a qué corpus entran los 5 `data-*-batch-0000.zip`.~~ Resuelto — ver DR-50.
10. *(No bloqueante)* Decidir destino final de `_CUARENTENA_DUPLICADOS/`.
11. **Nueva, agregada esta sesión — DR-54, BLOQUEANTE PARA EL DISEÑO DETALLADO DEL ANÁLISIS.** Definir, en sesión dedicada más profunda: unidad de fila de la tabla del análisis, columnas, las 3 preguntas de EDA exactas, y el enfoque de ML con sus variables — de forma que el mismo diseño sirva simultáneamente para el pipeline del objetivo 3, la corrección de C1/C2 (DR-52), y el formato exacto que exige la Consigna 1 de la UTN. Hay una propuesta preliminar sin confirmar (ver DR-54) como punto de partida. **Nota sobre el orden de esta lista:** aunque aparece último por orden de aparición cronológica, esta tarea condiciona el contenido real de los ítems 2, 3 (sub-punto de umbrales), 6, 7 y 8 — no tiene sentido avanzarlos en detalle antes de resolver esto.

---

## QUÉ NO HACER — VIGENTE + AGREGADO DE ESTA SESIÓN

*(Se mantiene íntegra la lista de `00-52`, no se reescribe ningún ítem existente. Se agregan los de esta sesión al final.)*

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
- No confundir el hallazgo de `claude_5` (DR-34) con una fuga tipo DR-30.
- Al generar el próximo SESSION_LOG_REPLANTEO, no reescribir "PRÓXIMAS TAREAS" ni "ESTADO REAL" de memoria — cotejar ítem por ítem contra este log.
- (DR-42) No reescribir celdas de tabla existentes al agregar una sección nueva — solo agregar al final.
- (DR-39) Verificar duplicados con sufijo numérico antes de asumir cuál archivo es el vigente.
- (DR-41/DR-43) No asumir completitud de los Módulos UTN 1-4 ni la convención `ModuloN_UnidadM_Tema_Corto.md`.
- (DR-48) No tratar el mod pack duplicado como parte del corpus de documentación.
- (DR-49) No tratar archivos sueltos tipo "instrucción" como órdenes automáticas sin revisar antes.
- (DR-50) No asumir que una clasificación Corpus A/B anterior es correcta solo porque un DR previo la asentó — verificar contra la definición de origen.
- **(DR-52, nuevo) No tratar a Paper C1 y Skill C2 como productos finales de rango propio, ni como "tercer y cuarto uso" del análisis del objetivo 3 — son productos del objetivo 2, auxiliares del objetivo 3, y se corrigen antes de usarse.**
- **(DR-54, nuevo) No avanzar el diseño detallado de las métricas de Grupo 1/2/3 ni empezar a construir la tabla del análisis sin haber cerrado, en la sesión dedicada pendiente, la unidad de fila, las columnas, las 3 preguntas de EDA y el enfoque de ML — la propuesta preliminar de esta sesión no está confirmada, no es la decisión final.**

---

## APÉNDICE — MATERIAL DE REFERENCIA PARA LA PRÓXIMA CUENTA

*(Se mantiene el apéndice de `00-52`. Se agrega lo siguiente.)*

**Contexto de origen para DR-52/DR-53/DR-54:** esta sesión surgió de una revisión de claridad de la documentación pedida por el operador (¿en qué consisten los 3 objetivos y 4 productos del proyecto?). Al revisar la cadena completa se encontró que DR-25 (`02-43`) ya definía la estructura de 3 objetivos/4 productos correctamente, pero DR-11/DR-26 seguían describiendo a C1/C2/portfolio como "tres usos parejos" — encuadre que el operador corrigió en esta charla (DR-52). Al revisar la consigna real de la UTN (`3_PORTAFOLIO_UTN/consignas/Consigna_1.md`, `Consigna_2.md`) para entender qué va a analizar en concreto el Trabajo UTN, apareció el vacío de DR-54.

**Para la próxima sesión dedicada a DR-54:** releer `Consigna_1.md` y `Consigna_2.md` completos (no solo el resumen de este log), más la sección "DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO" completa de `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (Grupo 1/2/3, Framework B, tabla de normalización) antes de confirmar la propuesta preliminar de fila/columnas/preguntas/enfoque de ML.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
