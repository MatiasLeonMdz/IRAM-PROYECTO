# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 2 — Lo que tuvimos que construir (y por qué)

*Draft s30 — correcciones finales — 2026-06-17*

---

El proyecto empezó sin sistema. Eso no fue un error de planificación — fue lo normal. Nadie diseña un sistema de documentación antes de saber qué problemas va a tener. Los sistemas se construyen cuando el costo de no tenerlos se vuelve visible.

En IRAM, ese costo se volvió visible varias veces, en orden, y cada vez generó una respuesta que se quedó.

---

### El problema que forzó el primer cambio

Durante los primeros meses, todo el contexto del proyecto vivía en un único documento de respaldo: instrucciones de trabajo, historial de versiones, decisiones de diseño, código de referencia, contexto técnico del motor del juego. Era el lugar natural donde guardar todo — y creció en consecuencia. Al llegar a 220KB y casi 5000 líneas, algo cambió en el comportamiento de la IA que no se podía ignorar: las reglas dejaron de seguirse.

No eran reglas nuevas. Eran las mismas que habían estado ahí desde semanas antes, correctamente escritas, sin ambigüedad. El error que cubrían seguía apareciendo en código nuevo, sesión tras sesión, como si la regla no existiera. El diagnóstico inicial fue el habitual: hay que explicarlo mejor. Se reescribió la regla. No cambió nada.

El problema no era el contenido. Era que una regla enterrada en el medio de 5000 líneas de código y contexto técnico competía por atención contra todo lo demás — y perdía. La sección 3 de este paper desarrolla esa mecánica en detalle. Lo que importa aquí es la consecuencia operacional: el sistema de un solo documento había llegado a su límite funcional. No era un problema de tamaño — era un problema de arquitectura.

---

### La respuesta: separar por función, no por cronología

La solución que se construyó no fue agregar más estructura al documento único. Fue partir el documento en capas con funciones distintas.

La primera separación fue entre lo que la IA necesita para operar ahora y lo que existe como registro histórico. El documento de trabajo empezó a tener dos versiones: una activa (lo que es el proyecto en este momento, las reglas vigentes, el estado actual) y una de archivo (versiones anteriores, decisiones descartadas, contexto histórico). El archivo existe; no se carga por defecto.

La segunda separación fue extraer las instrucciones de trabajo completamente: un documento corto, exclusivamente de reglas, que va pegado como primer bloque de cada sesión nueva. No adjunto como archivo — pegado, como primer mensaje. La diferencia no es de formato: es de posición en el contexto, y la posición determina el peso.

La tercera pieza que emergió fue el registro de sesión. Cubre un hueco específico que no es evidente hasta que aparece el problema: "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó en la última sesión" son cosas distintas. Sin un registro explícito de qué se hizo, qué quedó abierto y cuáles decisiones ya están cerradas, cada sesión nueva empieza sin saber qué sabe la anterior. El log no es un diario — es el mecanismo de handoff entre instancias sin memoria compartida.

---

### El día que concentró todo

Los tres cambios estructurales anteriores no se distribuyeron uniformemente a lo largo del proyecto. Hay un día — el 27 de mayo de 2026 — que concentró una cantidad desproporcionada de cambios en muy poco tiempo: el documento técnico de referencia adoptó un nombre más formal, se implementó la separación entre estado vigente e historial, y en la misma jornada ocurrió la sesión estratégica que reformuló el sentido del proyecto. La mañana siguiente se inicializó el sistema de control de versiones.

Ese día fue también el de mayor intensidad de trabajo de todo el proyecto.

La coincidencia no es casual. La fricción generada por un día de trabajo extremadamente intenso hizo visible, al mismo tiempo, todos los costos de seguir sin estructura. Cuando el costo de no estructurar supera al de pararse a estructurar, el sistema evoluciona — no antes. El sistema de documentación de IRAM no se diseñó con anticipación: se consolidó en el momento en que no hacerlo costaba más que hacerlo.

Eso también explica por qué el sistema tiene la forma que tiene. No es el resultado de aplicar un marco teórico sobre buenas prácticas con IA. Es el resultado de resolver problemas concretos, en orden, con el mínimo overhead que los resolvía.

---

### La cuarta pieza que no tenía nombre

Hay un elemento del sistema que estuvo desde temprano pero que tardó en identificarse como capa aparte: un documento orientado al operador humano, no a la IA.

Las instrucciones de trabajo le dicen a la IA cómo operar. El registro de sesión cubre el estado del proyecto entre instancias. Pero hay un tercer tipo de información que ninguno de los dos cubre: cómo verifica el operador que el sistema está funcionando correctamente. Qué señales indican que algo está degradando. Qué hacer cuando una sesión nueva no arranca bien. Ese es el tipo de contenido que le sirve al humano que trabaja con el sistema — y tiene una audiencia completamente distinta a las instrucciones que recibe la IA.

Este documento apareció en el proyecto bajo nombres distintos en distintas versiones, siempre como algo adjunto al final del PROMPT principal. Cuando finalmente se separó y se nombró como capa propia, la razón por la que había existido todo el tiempo se volvió obvia: las instrucciones para la IA y las instrucciones para el operador evolucionan a ritmos distintos y responden a preguntas distintas. Mezclarlas en el mismo documento no es eficiencia — es ruido para ambos.

---

### Las herramientas que aparecieron y desaparecieron

No todo lo que se construyó fue permanente. Dos prácticas nacieron para una situación puntual y estaban explícitamente marcadas como tales: registros intermedios después de cada tarea completada, y entregas parciales descargables al terminar cada tarea en lugar de un paquete único al final de la sesión.

Ambas nacieron el mismo día, durante un rediseño con más de diez tareas interdependientes, a partir de una pregunta simple: si la sesión se corta, ¿qué pasa con el trabajo de las tareas anteriores? Sin registro intermedio, ese trabajo vivía solo en la memoria activa de la sesión. La solución resolvió exactamente ese riesgo — y no otro.

Por eso están marcadas como *temporal/situacional*: aplican cuando hay una secuencia larga de tareas dependientes y el costo de perder trabajo parcial es alto. No aplican al desarrollo cotidiano, y activarlas por defecto sería overhead sin beneficio.

El principio general que emerge de esto es más útil que cualquiera de las herramientas específicas: el overhead de documentación tiene que ser proporcional al riesgo concreto que mitiga, no al tamaño del proyecto. Un seguro pesado contra perder trabajo en un corte de sesión tiene sentido cuando ese riesgo está presente. No tiene sentido el resto del tiempo. Distinguir cuándo cada herramienta aplica es parte de lo que el operador tiene que aprender — y no está en ninguna regla escrita, porque depende del contexto de cada sesión.

---

### Lo que el sistema terminó siendo

Al final del proyecto, el sistema de documentación tenía cinco piezas con cinco funciones distintas. Las instrucciones de trabajo — un documento corto de reglas numeradas, pegado como primer mensaje de cada sesión, que crece solo cuando un error real genera una regla nueva. El estado actual del proyecto — lo que la IA necesita para trabajar hoy: qué existe, qué está vigente, qué versión es canónica, sin el peso del historial. El historial — todo lo que ya no es operativo pero vale la pena conservar, disponible para consulta pero sin cargarse por defecto. El registro de sesión — qué se hizo la última vez, qué falta, qué decisiones ya están cerradas, el handoff entre instancias. Y la capa para el operador — que no recibe las instrucciones de la IA, pero necesita saber cómo verificar que el sistema está funcionando. Ninguna es redundante con las demás. Todas emergieron de problemas reales, en el orden en que esos problemas aparecieron.

---

*Sección 2 — draft s30 — correcciones finales — 2026-06-17*
