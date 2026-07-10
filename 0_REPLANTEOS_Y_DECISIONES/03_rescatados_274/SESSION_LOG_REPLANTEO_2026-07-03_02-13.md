# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-03 02:13 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-06-20_5.md (queda como archivo histórico, no como insumo a recargar completo)
**Motivo de esta versión:** verificación puntual del origen de la democratización con cita exacta (DR-22) + gaps de conocimiento del mod ya mapeados, confirmado (DR-23) + adopción de convención de nombres AAAA-MM-DD_HH-MM para archivos del replanteo (DR-24) + entrega de diplomatura vence 15/07. **El inventario completo del material de archivo (tarea 1) NO se hizo todavía** — lo que se hizo fue una revisión dirigida de 3-4 documentos puntuales para reconstruir el núcleo del replanteo y verificar una hipótesis específica (democratización); no es lo mismo que el inventario ítem-por-ítem de toda la tarea 1, que sigue pendiente.

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-09 del SESSION_LOG_REPLANTEO_2026-06-19_2.md siguen vigentes sin modificación. No se repiten acá — se citan por ID. Si hace falta el detalle, ir al log del 19/06.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-10 | El proyecto tiene un tercer objetivo operativo además del mod y la metodología: **portfolio de data science**. No es un objetivo nuevo — estaba en el STRATEGIC LOG del 27/05 ("objetivo real: ciencia de datos") pero nunca había entrado al sistema operativo del replanteo. Desde esta sesión vive acá. |
| DR-11 | El análisis comparativo Corpus A/B es el **núcleo único** que sirve para los tres usos: paper (C1), skill (C2) y portfolio. No son tres trabajos separados — es un solo análisis bien hecho presentado para tres audiencias. |
| DR-12 | La WIKI_DOCUMENTACION_v2.md **no se toca todavía**. Corregirla antes de tener la base de hechos del análisis A/B produce el mismo error que se está corrigiendo. DR-07 aplica: inventario ítem por ítem antes de cualquier baja de estatus. |
| DR-13 | El portfolio se presenta como **trabajo sin equivalente publicado verificado**: un proyecto donde el objeto de documentación es el propio proceso de trabajar con IA, con evidencia trazable hora por hora, donde el instrumento de diagnóstico reprodujo en vivo la falla que estaba diagnosticando. Caveat obligatorio: esto es ausencia en las fuentes revisadas el 19/06, no confirmación de novedad — requiere búsqueda más profunda antes de afirmarlo en el paper. |
| DR-14 | El portfolio habla a **dos audiencias simultáneas**: mercado de data science (dataset real, análisis comparativo, metodología reproducible) y mercado de IA aplicada (cómo trabajar con IA con evidencia, no con opinión). No son presentaciones separadas — el mismo trabajo, dos ángulos. |
| DR-15 | Las métricas del análisis se organizan en **tres grupos** con distinto nivel de esfuerzo (ver sección DISEÑO DEL ANÁLISIS abajo). No medir todo junto sin filtro — eso reproduce el error de T2 a mayor escala. |
| DR-16 | El mismo set de métricas se aplica a **los dos corpus en paralelo** para poder comparar cómo se comportó el sistema operador+IA en tarea técnica (Corpus A) vs. tarea metodológica (Corpus B). Ese contraste es el hallazgo más interesante del proyecto y todavía no tiene evidencia cuantitativa. |
| DR-17 | El Corpus B tiene los zips crudos disponibles. El operador los agrupa cuando sea el momento. No es un bloqueo — es una tarea pendiente con material ya disponible. |
| DR-18 | El timeline tentativo (listo para postularse a puestos remotos entry-level en noviembre/diciembre 2026) está **condicionado a los números reales del Corpus A**. No es una proyección confirmada — es lo que resulta de cruzar el ritmo estimado (3 horas/día promedio, picos de 6 en reworks pesados) con el stack técnico que falta aprender. Los números reales los da el análisis. |
| DR-19 | Stack técnico pendiente para data science, en orden de prioridad: Python con pandas (base ya existe en scripts del proyecto), SQL básico, Power BI o Tableau. Ninguno requiere prerequisito que el operador no tenga. |
| DR-20 | El proyecto final integrador de la diplomatura UTN se presenta usando IRAM como caso real — no un dataset de ejercicio. Es más sólido que la mayoría de los proyectos entry-level que usan datasets de Kaggle genéricos. (estimación sin fuente) |
| DR-21 | El análisis sigue el pipeline **Diseño → Limpieza → Análisis → Comparativa**. Los parámetros se diseñan sobre Corpus A y Corpus B en paralelo antes de correr ningún script. Esto resuelve la decisión pendiente desde el 19/06 — no era "A ahora vs. esperar B" sino que el diseño precede a la ejecución en los dos corpus simultáneamente. |
| DR-22 | **Origen verificado de la frase "democratización" — con cita exacta, no de resumen.** Cadena completa: (1) s12, el operador articula el principio real. (2) 11/06 22:48, CLAUDE_3 propone "democratiza" como reformulación; el operador la acepta con reserva de estilo y la sesión sigue con una versión sin esa palabra. (3) 12/06, el CONSOLIDADO fosiliza la versión con "democratiza" como "Principio central (definitivo)", sin la reserva de estilo. (4) s18 (17/06 madrugada), alguien ya señala que la frase está mal como apertura — queda en el transcript crudo `failed_3.md`, nunca consolidado. (5) 17/06 05:43–05:51, CLAUDE_3 (conversación "Preparación de draft para Sección 3 del C1") lee ese transcript y escribe explícitamente la "Corrección 1": la frase "no es el principio correcto de apertura". (6) 17/06 16:18, el draft de Sección 3 sale ya con "posición y formato", coherente con la Corrección 1. (7) WIKI_DOCUMENTACION nunca se actualizó — quedó "definitivo" desde el 17/06 17:13 pese a que el propio proyecto ya sabía, horas antes, que estaba mal. Conclusión: el error no fue "nadie lo notó" — fue que la corrección se encontró y se escribió, y aun así no llegó al documento oficial. Mismo mecanismo que DR-08/DR-09 (etiqueta de estado reemplaza verificación), ahora confirmado también como patrón histórico, no solo en tiempo real. No cambia DR-12: la WIKI sigue sin tocarse hasta la base de hechos A/B. |
| DR-23 | **Gaps de conocimiento del mod ya mapeados — no rehacer.** `IRAM_gaps_conocimiento_2026-06-12.md` (pre-replanteo, 12/06) ya ejecutó una "Plantilla B" completa: 6 categorías (A–F), 18 gaps identificados, cada uno con fuente en el historial unificado (7345 msgs) contrastado contra WIKI ACTIVE v3.10 + ARCHIVE v3.7, y cada gap ya vinculado a una sección específica del futuro SKILL.md. Es insumo válido para Corpus A / skill C2 tal como está — no es parte del inventario pendiente (tarea 1), es un resultado ya cerrado de ese tipo de trabajo. Quedan 5 huecos puntuales sin resolver dentro de ese mismo documento (marcados como pendientes de búsqueda en el propio archivo), no bloquean el uso del resto. |
| DR-24 | **Convención de nombres de archivo — extender al replanteo la regla ya existente del mod, no crear una nueva.** La Sección 3.2.1 de TECHNICAL_WIKI_ACTIVE ya define el formato `AAAA-MM-DD_HH-MM` (fecha ISO + hora) para archivos del sistema de control (`IRAM_SESSION_LOG_AAAA-MM-DD_HH-MM.md`), con dos reglas explícitas: (1) nunca usar letras de sufijo (`_A`, `_B`, `_E`) porque la hora identifica unívocamente cada entrega, y (2) **antes de generar cualquier archivo con nombre de fecha/hora, preguntar la hora al operador — nunca asumir ni usar la hora del sistema**. Esa regla existía pero nunca se había extendido a los archivos del replanteo (`SESSION_LOG_REPLANTEO_...`), que hasta esta sesión solo llevaban fecha sin hora — por eso el operador venía resolviendo los choques de nombre a mano (agregando "2", "3"), el mismo síntoma que la regla original ya prevenía en el mod. Desde esta sesión, todo archivo nuevo del replanteo sigue el mismo formato: `SESSION_LOG_REPLANTEO_AAAA-MM-DD_HH-MM.md`. Este archivo pasa a llamarse `SESSION_LOG_REPLANTEO_2026-07-03_01-52.md` (hora confirmada por el operador). **Refuerzo (misma sesión, 01:57):** la regla declarativa falló al primer uso real — se generó/editó un archivo con nombre de fecha/hora sin pedir la hora, pese a que DR-24 ya estaba escrita. Confirma el mismo mecanismo de DR-08/DR-09/DR-22: una regla escrita no se ejecuta sola. Gatillo mecánico agregado para que no dependa de que la IA se acuerde: **antes de cualquier `create_file`, `mv`/rename, o edición de encabezado que fije un nombre con `HH-MM`, el primer paso obligatorio es preguntar la hora — no un paso más de una lista, sino la acción previa a cualquier otra herramienta que toque ese nombre.** Si la hora ya fue preguntada y confirmada en el mismo tramo de conversación (sin haber cambiado de archivo ni de tarea), no hace falta repetir la pregunta para operaciones subsiguientes sobre ese mismo nombre. |
| DR-25 | **Estructura del proyecto en tres piezas — no cuatro, y la relación entre ellas es específica.** (1) **Mod IRAM** (Corpus A). (2) **Documentación del mod**: documentación técnica del mod y de las herramientas de trabajo con IA (Corpus B). (3) **Trabajo de Análisis**, título de trabajo: *"Qué y cómo aprendimos trabajando con IA"* — el análisis comparativo A/B, explícitamente no solo cuantitativo (incluye el "por qué" y el "cómo", no solo conteos — Grupo 3 y las categorías de Framework B ya apuntaban a esto, ahora queda dicho como principio). **La diplomatura y el portfolio no son un cuarto elemento ni dos trabajos separados que consumen el análisis como insumo: son la misma actividad (3) expresada en dos productos distintos**, según audiencia. No se hace el análisis dos veces. Esto no reemplaza DR-11/DR-14 (núcleo único, múltiples audiencias) — les pone nombre y aclara la relación "misma actividad, dos expresiones" explícitamente, porque hasta esta sesión quedaba ambiguo si diplomatura era insumo de portfolio, trabajo paralelo, o la misma cosa. Consecuencia directa para el criterio de cierre (tarea 0, en curso): no puede definirse como "hasta qué grupo de métricas", porque los 3 grupos ya estaban decididos como obligatorios sin recorte (DR-15/DR-16) — el criterio de cierre real es distinto y sigue sin definirse. |

---

## DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO

### Grupo 1 — Métricas directas del corpus (salen de los JSON sin anotación manual)
Aplicar a Corpus A y Corpus B para comparación:

- Horas totales del proyecto
- Horas por sesión
- Duración promedio de sesión
- Picos de intensidad (sesiones con más de X horas)
- Volumen por cuenta (Corpus A: 5 cuentas)
- Distribución temporal (hora del día, día de semana)
- Sesiones cortadas vs. completadas

### Grupo 2 — Requieren categorización asistida + anotación manual
Aplicar a los dos corpus. Incluye métricas que parecen directas pero requieren etiquetado previo:

- **Distribución por fase** (diseño vs. ejecución vs. debugging vs. documentación) — requiere anotación de fase por sesión antes de calcular
- **Ratio mensajes operador/IA por fase** — depende de la anotación de fase
- **Velocidad de respuesta por tipo de tarea** — requiere anotación de tipo de tarea

Categorías de autoría — Framework B (autoridad de decisión, no supervivencia de texto):
- OP_ARCH: operador fijó la dirección
- IA_PROP_AC: IA fijó la dirección, operador ajustó detalles
- IA_PROP_RJ: IA propuso dirección, operador la cambió
- COLAB: dirección emergió de la interacción sin que ninguno la fijara primero
- IA_DIAG_OP_DEC: diagnóstico técnico de IA, decisión de dirección del operador (DR-06 — casos tipo 4B, INC-13)

Métricas DR-08 y DR-09 — como patrones con impacto, no como conteos simples:
- **DR-08 frecuencia:** instancias por cada 100 mensajes de IA
- **DR-08 costo:** turnos de corrección del operador generados por cada instancia
- **DR-08 distribución:** en qué fases aparece más
- **DR-09 frecuencia:** instancias por cada 100 mensajes de IA
- **DR-09 costo:** turnos o artefactos revertidos por instancia
- **DR-09 distribución:** en qué tipo de tarea aparece más (código, documentos, análisis)

### Grupo 3 — Ciclo de vida del sistema de documentación (Corpus B principalmente)
- Cuándo apareció cada práctica, con fecha exacta
- Qué la detonó (pérdida, fricción, decisión explícita)
- El arco completo simple→complejo→intento de vuelta a simple, con timestamps
- Costo de cada transición (sesiones perdidas, trabajo rehecho)

### Tabla de normalización para comparación A/B
| Pregunta | Normalización |
|----------|--------------|
| Intensidad (tiempo, volumen) | Por día calendario |
| Comportamiento típico de sesión | Por sesión/conversación |
| Autoría | Por decisión codificada |
| DR-08 frecuencia | Por 100 mensajes de IA |
| DR-08 costo | Turnos de corrección por instancia |
| DR-09 frecuencia | Por 100 mensajes de IA |
| DR-09 costo | Turnos o artefactos revertidos por instancia |

### Definiciones operacionales
- **Sesión:** conversación individual de Claude (sinónimo: charla). Unidad = conversation_id en el JSON.
- **Corte Corpus B:** el día en que se detuvo simultáneamente el desarrollo del mod y sus herramientas (wiki-active, archive, log) y se pasó a documentar el proceso. Fuente del corte: nombre de la carpeta asignado por el operador — no un timestamp del log.
- **Versionado del análisis:** nombre del script + fecha de ejecución + hash o checksum del input. Obligatorio para reproducibilidad.

---

## EVALUACIÓN DEL OPERADOR — VERIFICADA EN ESTA SESIÓN

Registrado como hecho, no como valoración subjetiva. Fuentes: STRATEGIC LOG 2026-05-27, hitos_v7, SESSION_LOG_DOCUMENTACION_s24, IRAM_C1_final.md S6, sesión de hoy.

### Lo que está verificado con evidencia directa:
- Detectó los dos errores sistémicos del proyecto (democratización + proxy de autoría) rastreando hasta fuente primaria, sin conocer los nombres técnicos de esos errores antes de hacerlo.
- Hitos con autoría "Operador-iniciativa" y colaborativos en el historial — **pendiente verificación con cita de línea en hitos_v7** antes de usar como cifras exactas.
- Decisiones de arquitectura del mod que la IA no pudo resolver (spawn de unidades v1, scope global v3, workaround de rivales v2) — confirmado en STRATEGIC LOG línea 2269.
- Detectó en tiempo real narrativa sin respaldo y acción sin autorización de la IA en la sesión del 19/06 (DR-08, DR-09).
- Trabajo cuantitativo real en el mod: modelo económico, simuladores Optimize, grid search de 17 combinaciones de parámetros — confirmado en STRATEGIC LOG línea 2274.

### Conexión IRAM → data science (verificada en STRATEGIC LOG + paper S6):
- Modelo económico → modelado estadístico
- Simuladores Optimize → simulación y análisis de sensibilidad
- ETL: conversations.json → deduplicación → historial unificado (process_iram_v2.py)
- Interrupted time series: 4 puntos de corte con métricas consistentes
- Grid search: barrido de 17 combinaciones de parámetros
- RAG manual, HITL, deuda técnica en tres formas, ADRs, specification-driven development — todos llegados por fricción, no por conocimiento previo.

### Lo que esta evaluación no puede confirmar todavía:
- Horas reales por sesión y por fase — lo da el Corpus A.
- Cifras exactas de hitos por categoría de autoría — requieren verificación con línea en hitos_v7.
- Comparación contra "alguien con el mismo background" — no hay vara objetiva.
- Novedad real del proyecto vs. ausencia en fuentes revisadas — requiere búsqueda más profunda.

---

## CONTEXTO DE DATA SCIENCE Y MERCADO LABORAL — VERIFICADO EN ESTA SESIÓN

### La diplomatura UTN (Ciencia de Datos e IA, 21 semanas, 157 horas):
- Enfoque no-code/low-code — objetivo explícito: sin necesidad de programar.
- Cubre: pensamiento analítico, cultura data-driven, herramientas visuales, ML conceptual, IA generativa, automatización no-code, NLP introductorio, visión por computadora introductoria.
- No cubre: Python técnico, pandas, SQL, estadística formal, Jupyter notebooks, scikit-learn.
- Valor real: certificado UTN + marco conceptual + proyecto final integrador (usar IRAM como caso real — DR-20).

### Stack técnico pendiente para rol técnico remoto:
| Skill | Estado | Tiempo estimado con ritmo actual |
|-------|--------|----------------------------------|
| Python con pandas | En desarrollo — base en scripts del proyecto | 3-4 meses (condicionado — ver DR-18) |
| SQL básico | No tocado | 1 mes en paralelo (condicionado — ver DR-18) |
| Power BI o Tableau | No tocado | 3-4 semanas (condicionado — ver DR-18) |
| Portfolio con Corpus A presentable | Depende de los anteriores | 1 mes adicional (condicionado — ver DR-18) |

### Mercado laboral Mendoza / remoto (verificado en búsqueda de esta sesión):
- Mendoza presencial: ~12 ofertas activas de analista de datos, 1 sin experiencia.
- Mercado relevante: remoto Argentina + exterior — ahí está el volumen real.
- Lo que piden los puestos remotos entry-level: SQL, Python con pandas, Power BI o Tableau, proyecto propio que mostrar.
- No filtran por título universitario — filtran por stack técnico y evidencia de trabajo real.

### Timeline tentativo (condicionado a números reales del Corpus A — ver DR-18):
- Agosto 2026: cierre diplomatura + Python funcional con pandas (condicionado)
- Septiembre 2026: SQL básico (condicionado)
- Octubre 2026: Power BI o Tableau (condicionado)
- Noviembre/Diciembre 2026: portfolio con Corpus A presentable, listo para postularse (condicionado)

### Portfolio — definición de entregable:
- Formato principal: GitHub repo
- Contenido: specs limpios, outputs del análisis, README con dos versiones del pitch (DS market / AI methodology market)
- Documento: paper C1 enlazado desde el repo como PDF o markdown
- Plataforma secundaria: LinkedIn post de síntesis al cierre — no antes

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-03

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. BUG-1, BUG-3, BUG-4 corregidos en v5.6. Quedan bugs menores — no se tocan en esta fase. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34, con dos afirmaciones sin respaldo (S4A, S5) — se corrigen después del análisis A/B, no antes. |
| WIKI_DOCUMENTACION_v2.md | Sigue con la frase de democratización como "principio central (definitivo)" — no se toca hasta tener base de hechos (DR-12). |
| Corpus A (5 JSON del mod) | Disponible. Sin procesar. Primer paso: diseño de parámetros (DR-21). |
| Corpus B (conversaciones de documentación) | Zips crudos disponibles. El operador los agrupa. No es bloqueo. |
| Specs A/B/C viejos | Reusar lógica de normalización de JSON. Reemplazar heurísticas para cubrir DR-06, DR-16 y Framework B. |
| Diplomatura UTN | Recién empezada. Cierre estimado agosto 2026. Entrega Parte 1: **15/07/2026** (confirmado por el operador el 03/07). |
| Python | Recién empezando. En desarrollo activo. |
| Stack DS restante | SQL, Power BI/Tableau — pendiente después de Python. |
| Origen de "democratización" | Verificado con cita exacta de fuente primaria (DR-22). Pendiente: aplicar la corrección a WIKI_DOCUMENTACION — bloqueado por DR-12 hasta base de hechos A/B. |
| Gaps de conocimiento del mod | Ya mapeados (DR-23), no rehacer. 5 huecos puntuales quedan abiertos dentro de ese mismo documento. |
| 5 ZIPs crudos de Claude (historial hasta 20/06) | Subidos por el operador el 03/07, contienen Corpus A y Corpus B juntos — el corte se aplica al procesar, no al recolectar. **No procesados todavía**: se decidió resolver primero los criterios de forma/fondo pendientes (ver tarea 0 abajo). |
| Processed JSONs (claude_X_processed.json) | Sin confirmar si existen ya en la máquina local del operador, o si hace falta generarlos de nuevo desde los ZIPs. |

---

## PRÓXIMAS TAREAS — en orden de prioridad

0. **[BLOQUEA TODO LO DEMÁS] Definir todos los criterios de forma y fondo pendientes del replanteo, uno por uno, antes de tocar los ZIPs o el pipeline.** Decisión explícita del operador el 03/07: no quiere seguir con nada operativo hasta cerrar esto. Dos puntos concretos, sin resolver, no redebatibles como lista pero sí como contenido a definir:
   - **Criterio de cierre de esta fase** — cuándo se considera completo el análisis A/B (ya estaba en la lista como tarea, se eleva a bloqueante).
   - **Nota de vínculo diplomatura↔pipeline** — si se agrega al log una aclaración de que Parte 1 de la diplomatura = output intermedio del análisis Corpus A, y Parte 2 = output del análisis completo A/B (para que la diplomatura no aparezca como trabajo paralelo sino como hito dentro de DR-21). Pregunta abierta desde la sesión truncada del 03/07, nunca contestada.
   - Si en la próxima sesión el operador no se acuerda dónde quedó esto: releer solo esta sección, no la sesión truncada completa.

1. **Inventario completo del material de archivo disponible.** Antes de diseñar el análisis en detalle, hacer un inventario ítem por ítem de todo el material existente: qué archivos hay, qué contiene cada uno, qué estado tiene (vigente/histórico/pendiente), y qué corpus corresponde (A, B, o ninguno). Sin este inventario el diseño trabaja sobre una lista parcial de insumos.
2. **Inventario terminológico completo** — sesión dedicada. Nombre formal o terminología temporal `[TEMP]` para cada mecanismo, herramienta, proceso y análisis del proyecto. Plan: ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, Anthropic/OpenAI/DeepMind publications, grey literature. Mínimo 5 queries por ítem, 3 idiomas, umbral de 5 búsquedas + 2 fuentes grises.
3. **Criterio de cierre de esta fase** — definir en sesión de diseño cuándo el análisis A/B está completo.
4. **Verificación de cifras de hitos** — cita de línea exacta en hitos_v7 para los números de autoría "Operador-iniciativa" y colaborativos.

---

## QUÉ NO HACER — VIGENTE + AGREGADOS DE ESTA SESIÓN

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes.
- No tocar el mod.
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual.
- No bajar el estatus de ningún documento sin el inventario de DR-07.
- No asumir que algo "puede avanzar en paralelo" sin confirmación del operador.
- No narrar logros, "calibre", ni dramatizar decisiones propias.
- No llamar a actualizar el log sin instrucción explícita del operador.
- No proponer métricas sin anclarlas a una pregunta concreta.
- No afirmar novedad del proyecto sin búsqueda más profunda — solo "ausencia en fuentes revisadas el 19/06".
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).
- No presentar el timeline como fechas confirmadas — siempre con "(condicionado — ver DR-18)".
- No usar cifras de hitos de autoría sin verificación de línea en hitos_v7.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
