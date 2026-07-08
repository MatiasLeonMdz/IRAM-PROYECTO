# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 6 — Los conceptos formales que nombran lo que hicimos

*Draft s30 — correcciones finales — 2026-06-17*

---

Una de las cosas que ocurre cuando un proyecto se construye de forma empírica — resolviendo problemas en el orden en que aparecen, sin un marco teórico de partida — es que al final resulta que muchos de esos problemas ya tienen nombre. El nombre no estaba disponible durante el trabajo. Pero el problema, y la solución, sí.

Nombrar retroactivamente no es cosmético. Es lo que permite reconocer el mismo patrón en otro contexto, comunicarlo a alguien que no estuvo en el proyecto, y evaluar qué tan lejos está la práctica empírica de lo que la teoría recomienda. En algunos casos el proyecto llegó exactamente al mismo lugar que el concepto formal. En otros, llegó a una variante que la versión estándar no cubre — y esa diferencia es tan informativa como la coincidencia.

---

### El mapa

| Lo que hicimos en IRAM | Nombre formal | Área |
|---|---|---|
| conversations.json → deduplicación → historial unificado de 7345 mensajes | Pipeline ETL (Extract, Transform, Load) | Ingeniería de datos |
| "7345 msgs post-dedup" — eliminar mensajes duplicados antes del análisis | Deduplicación de dataset | Preprocesamiento |
| 4 puntos de corte (antes/después de cada cambio estructural) → medir efecto | Interrupted time series / experimento natural | Estadística causal |
| Barrido sistemático de 17 combinaciones de parámetros en la función de optimización económica para encontrar el rango que producía el comportamiento deseado | Grid search | Optimización / ML |
| valor_rp documentado con rango [min, max] sin cerrar | Incertidumbre epistémica / sensitivity analysis | Estadística |
| ACTIVE/ARCHIVE + PROMPT_MAESTRO + SESSION_LOG — contexto cargado por capas | RAG manual (Retrieval-Augmented Generation) | IA aplicada |
| Operador diseña la arquitectura / IA implementa dado el diseño | Human-in-the-Loop (HITL) | IA aplicada |
| bug → patrón → regla → documento de instrucciones | Blameless post-mortem / mejora de proceso | Ingeniería de software |
| v4 → v5: namespace propio, separación de módulos, eliminación de dependencias cruzadas | Deuda técnica — tres tipos: namespace pollution, coupling, monolith | Ingeniería de software |
| SESSION_LOG como handoff entre instancias sin memoria compartida | State management / context passing | Sistemas distribuidos |
| Documento corto de reglas pegado como primer mensaje — no adjunto | Prompt engineering: posición como variable de diseño | IA aplicada |
| 75 mensajes de diseño → SESSION_LOG_CONSOLIDADO → 13 tareas sin decisiones pendientes | Specification-driven development | Ingeniería de software |
| Alternativas descartadas documentadas con razón, para IA futura | Architecture Decision Records (ADRs) | Ingeniería de software |

---

### Lo que el proyecto llegó al mismo lugar

**RAG manual.** El sistema de capas de IRAM — documento activo, archivo, instrucciones de trabajo, registro de sesión — resuelve exactamente el problema que RAG resuelve en sistemas más sofisticados: cómo proveer a un modelo de lenguaje información relevante sin saturar el contexto con todo lo disponible. La diferencia es de implementación. RAG automatiza la recuperación mediante embeddings y búsqueda semántica. IRAM lo hizo manualmente: el operador decide qué cargar en cada sesión según el tipo de trabajo. El principio es el mismo — contexto selectivo, no contexto total.

**Experimento natural con interrupted time series.** Los cuatro puntos de corte del proyecto (antes y después de cada cambio estructural mayor) tienen exactamente la forma de un diseño de interrupted time series: una serie temporal de mediciones (costo de inicialización de sesión, velocidad de desarrollo) con interrupciones correspondientes a intervenciones conocidas y fechadas. La tabla de la sección 3 es ese análisis aplicado. No fue diseñado como tal — emergió de que el proyecto tuvo la disciplina de medir consistentemente y de que los cambios estructurales tuvieron fechas exactas documentadas.

**Deuda técnica en sus tres formas.** El salto de v4 a v5 del mod fue, en gran parte, un ejercicio de pagar deuda técnica acumulada. *Namespace pollution*: todos los identificadores del mod compartían el espacio de nombres global del juego — se resolvió adoptando el prefijo `iram_`. *Coupling*: funciones interdependientes que no podían modificarse de forma aislada — se resolvió separando en cuatro módulos independientes. *Monolito*: un archivo único de casi 900 líneas — se resolvió distribuyendo en módulos con responsabilidad clara. Los tres tipos son estándar en la literatura; el proyecto los encontró en ese orden y los resolvió en ese orden.

---

### Lo que el proyecto hizo distinto

**ADRs orientados a IA.** Los Architecture Decision Records estándar son un artefacto para el equipo humano: registran qué se decidió, qué alternativas se evaluaron, y por qué se eligió lo que se eligió. En IRAM, esa función existía — pero la audiencia principal no era el operador. Era la instancia de IA que iba a llegar sin memoria a esa parte del proyecto y potencialmente iba a volver a proponer lo que ya estaba descartado. Eso cambia cómo se escriben: el nivel de explicitación del razonamiento tiene que ser suficiente para que alguien sin contexto previo lo entienda sin preguntar. Un ADR estándar puede asumir que quien lo lee tiene memoria de la conversación que lo generó. Un ADR orientado a IA no puede asumir nada.

**RAG manual como elección deliberada.** En el contexto de un proyecto de dos meses con un solo operador, implementar RAG automatizado habría sido overhead desproporcionado. La versión manual — el operador carga lo relevante, archiva lo que no lo es, decide qué entra en cada sesión — fue suficiente para el problema que resolvía y no requirió infraestructura adicional. Esto no es una limitación del proyecto: es una instancia del principio de la sección 2 (overhead proporcional al riesgo). La versión automatizada tiene sentido cuando el volumen de información disponible hace inviable la selección manual, o cuando hay múltiples operadores que necesitan consistencia sin coordinación. Ninguna de esas condiciones existía en IRAM.

---

### Lo que el proyecto no ejercitó

Dos áreas del programa de la diplomatura no tuvieron correlato en IRAM:

Herramientas de automatización no-code (Make, Zapier, n8n). El proyecto no tuvo flujos de trabajo que requirieran integración entre múltiples servicios externos. Todo el trabajo ocurrió dentro de conversaciones con IA y archivos locales.

Visión por computadora. No hubo datos visuales, imágenes, ni procesamiento de video en ninguna parte del proyecto. El dominio era scripting de texto para un motor de juego — sin componente visual más allá del juego mismo.

La ausencia de estas áreas no es un déficit del proyecto: es simplemente que el problema no las requería. Lo que sí ejercitó — en particular el diseño de sistemas, la gestión de estado entre instancias sin memoria compartida, y el análisis causal del proceso — no estaba en el diseño original del proyecto. Emergió de los mismos problemas que generaron todo lo demás.

---

*Sección 6 — draft s30 — correcciones finales — 2026-06-17*
*Corrección aplicada: fila grid search — reemplazada referencia "(Sec 12 wiki)" por descripción del barrido real de parámetros.*
