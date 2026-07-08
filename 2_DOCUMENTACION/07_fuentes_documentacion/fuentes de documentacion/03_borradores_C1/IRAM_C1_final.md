# Qué aprendimos sobre cómo funciona la IA
## Case study: IRAM — Proyecto de modding con IA sostenida durante dos meses

*2026-06-17*

---

## Contenido

1. El laboratorio
2. Lo que tuvimos que construir (y por qué)
3. El hallazgo central: la posición y el formato importan más que el contenido
4. Cómo trabaja la IA: cuatro hallazgos con casos
5. Los datos del proceso
6. Los conceptos formales que nombran lo que hicimos
7. Qué transfiere y qué no

---

## 1 — El laboratorio

En algún momento de abril de 2026, alguien escribió una pregunta de una línea: ¿se puede redistribuir población automáticamente en Imperator: Rome?

De esa pregunta salió un mod para un videojuego de estrategia. Pero eso no es lo que documenta este paper.

### El proyecto

IRAM es un mod para Imperator: Rome 2.0.4 — un juego de estrategia histórica ambientado en la antigüedad clásica. Un mod modifica el comportamiento del juego: en este caso, automatiza decisiones económicas y demográficas que el juego original deja al jugador. El mod se construyó en aproximadamente dos meses, en 441 conversaciones con IA a través de 5 cuentas de Claude, acumulando 7345 mensajes analizados. De esas conversaciones, 336 corresponden al desarrollo activo de IRAM; el resto son sesiones previas o de contexto general del mismo período.

Esos números no describen un proyecto grande en términos de software. Describen un proyecto largo en términos de trabajo con IA — lo suficientemente largo como para que aparecieran, en orden, casi todos los problemas que aparecen cuando se intenta usar IA de forma sostenida en un dominio técnico.

El mod fue el vehículo. Lo interesante no es qué hace el mod — es qué tuvo que construirse para que el mod pudiera existir.

### Las dos historias

Un proyecto así acumula dos historias distintas, y conviene no mezclarlas.

La primera es la historia técnica: qué se construyó, en qué versión, con qué bugs y qué soluciones. En IRAM eso es la progresión de v1 a v5 — cinco versiones con nombres, zips canónicos y decisiones de diseño documentadas. Es específica del dominio. A casi nadie le importa cómo se resolvió un bug de scope en el motor de Imperator: Rome.

La segunda es la historia de cómo el operador y la IA aprendieron a trabajar juntos. Cuándo apareció cada documento de contexto, qué problema lo generó, cómo cambió el protocolo de sesión. Esta es la historia que generaliza — y es la que está detrás de este documento.

La razón para separarlas no es estética. Cuando se mezclan en el mismo log, la IA no puede priorizar: ¿esto es contexto técnico que necesito para programar, o es una regla sobre cómo trabajamos? El patrón de la segunda historia — el que vale la pena formalizar — queda diluido entre detalles técnicos que no lo son.

Este paper documenta la segunda historia. La primera aparece solo cuando da contexto o cuando es la evidencia.

### Por qué sirve como caso de estudio

Tres condiciones hacen de IRAM un caso útil para analizar el trabajo con IA, más allá del dominio específico.

Primero, escala suficiente. Dos meses, cinco cuentas, 441 conversaciones. No es un experimento de laboratorio ni una sesión de prueba — es un proyecto real con presión real de entrega, límites reales de herramienta, y errores reales que costaron tiempo.

Segundo, árbitro claro. El motor del juego corre o no corre. Una función de scripting o produce el comportamiento esperado en el juego, o no lo produce. Esa retroalimentación inequívoca — sin ambigüedad, sin interpretación — acortó radicalmente el ciclo hipótesis-prueba. Sin árbitro claro, muchos de los patrones que se identificaron habrían tardado mucho más en ser visibles.

Tercero, el objetivo estaba reformulado desde adentro. En algún momento del proyecto — no al principio, sino cuando el sistema empezaba a tomar forma — se escribió esto en el propio documento de estado del mod: *"el mod exitoso es el entregable, el aprendizaje es el objetivo real."* No es una conclusión retrospectiva. Es una intención que quedó documentada mientras el trabajo ocurría, en mayo de 2026, en medio del proyecto.

Esa reformulación es el punto de partida de este paper. El mod se terminó. Lo que este documento intenta hacer es responder la pregunta que esa frase dejó abierta: ¿qué se aprendió exactamente?

---

## 2 — Lo que tuvimos que construir (y por qué)

El proyecto empezó sin sistema. Eso no fue un error de planificación — fue lo normal. Nadie diseña un sistema de documentación antes de saber qué problemas va a tener. Los sistemas se construyen cuando el costo de no tenerlos se vuelve visible.

En IRAM, ese costo se volvió visible varias veces, en orden, y cada vez generó una respuesta que se quedó.

### El problema que forzó el primer cambio

Durante los primeros meses, todo el contexto del proyecto vivía en un único documento de respaldo: instrucciones de trabajo, historial de versiones, decisiones de diseño, código de referencia, contexto técnico del motor del juego. Era el lugar natural donde guardar todo — y creció en consecuencia. Al llegar a 220KB y casi 5000 líneas, algo cambió en el comportamiento de la IA que no se podía ignorar: las reglas dejaron de seguirse.

No eran reglas nuevas. Eran las mismas que habían estado ahí desde semanas antes, correctamente escritas, sin ambigüedad. El error que cubrían seguía apareciendo en código nuevo, sesión tras sesión, como si la regla no existiera. El diagnóstico inicial fue el habitual: hay que explicarlo mejor. Se reescribió la regla. No cambió nada.

El problema no era el contenido. Era que una regla enterrada en el medio de 5000 líneas de código y contexto técnico competía por atención contra todo lo demás — y perdía. La sección 3 de este paper desarrolla esa mecánica en detalle. Lo que importa aquí es la consecuencia operacional: el sistema de un solo documento había llegado a su límite funcional. No era un problema de tamaño — era un problema de arquitectura.

### La respuesta: separar por función, no por cronología

La solución que se construyó no fue agregar más estructura al documento único. Fue partir el documento en capas con funciones distintas.

La primera separación fue entre lo que la IA necesita para operar ahora y lo que existe como registro histórico. El documento de trabajo empezó a tener dos versiones: una activa (lo que es el proyecto en este momento, las reglas vigentes, el estado actual) y una de archivo (versiones anteriores, decisiones descartadas, contexto histórico). El archivo existe; no se carga por defecto.

La segunda separación fue extraer las instrucciones de trabajo completamente: un documento corto, exclusivamente de reglas, que va pegado como primer bloque de cada sesión nueva. No adjunto como archivo — pegado, como primer mensaje. La diferencia no es de formato: es de posición en el contexto, y la posición determina el peso.

La tercera pieza que emergió fue el registro de sesión. Cubre un hueco específico que no es evidente hasta que aparece el problema: "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó en la última sesión" son cosas distintas. Sin un registro explícito de qué se hizo, qué quedó abierto y cuáles decisiones ya están cerradas, cada sesión nueva empieza sin saber qué sabe la anterior. El log no es un diario — es el mecanismo de handoff entre instancias sin memoria compartida.

### El día que concentró todo

Los tres cambios estructurales anteriores no se distribuyeron uniformemente a lo largo del proyecto. Hay un día — el 27 de mayo de 2026 — que concentró una cantidad desproporcionada de cambios en muy poco tiempo: el documento técnico de referencia adoptó un nombre más formal, se implementó la separación entre estado vigente e historial, y en la misma jornada ocurrió la sesión estratégica que reformuló el sentido del proyecto. La mañana siguiente se inicializó el sistema de control de versiones.

Ese día fue también el de mayor intensidad de trabajo de todo el proyecto.

La coincidencia no es casual. La fricción generada por un día de trabajo extremadamente intenso hizo visible, al mismo tiempo, todos los costos de seguir sin estructura. Cuando el costo de no estructurar supera al de pararse a estructurar, el sistema evoluciona — no antes. El sistema de documentación de IRAM no se diseñó con anticipación: se consolidó en el momento en que no hacerlo costaba más que hacerlo.

Eso también explica por qué el sistema tiene la forma que tiene. No es el resultado de aplicar un marco teórico sobre buenas prácticas con IA. Es el resultado de resolver problemas concretos, en orden, con el mínimo overhead que los resolvía.

### La cuarta pieza que no tenía nombre

Hay un elemento del sistema que estuvo desde temprano pero que tardó en identificarse como capa aparte: un documento orientado al operador humano, no a la IA.

Las instrucciones de trabajo le dicen a la IA cómo operar. El registro de sesión cubre el estado del proyecto entre instancias. Pero hay un tercer tipo de información que ninguno de los dos cubre: cómo verifica el operador que el sistema está funcionando correctamente. Qué señales indican que algo está degradando. Qué hacer cuando una sesión nueva no arranca bien. Ese es el tipo de contenido que le sirve al humano que trabaja con el sistema — y tiene una audiencia completamente distinta a las instrucciones que recibe la IA.

Este documento apareció en el proyecto bajo nombres distintos en distintas versiones, siempre como algo adjunto al final del PROMPT principal. Cuando finalmente se separó y se nombró como capa propia, la razón por la que había existido todo el tiempo se volvió obvia: las instrucciones para la IA y las instrucciones para el operador evolucionan a ritmos distintos y responden a preguntas distintas. Mezclarlas en el mismo documento no es eficiencia — es ruido para ambos.

### Las herramientas que aparecieron y desaparecieron

No todo lo que se construyó fue permanente. Dos prácticas nacieron para una situación puntual y estaban explícitamente marcadas como tales: registros intermedios después de cada tarea completada, y entregas parciales descargables al terminar cada tarea en lugar de un paquete único al final de la sesión.

Ambas nacieron el mismo día, durante un rediseño con más de diez tareas interdependientes, a partir de una pregunta simple: si la sesión se corta, ¿qué pasa con el trabajo de las tareas anteriores? Sin registro intermedio, ese trabajo vivía solo en la memoria activa de la sesión. La solución resolvió exactamente ese riesgo — y no otro.

Por eso están marcadas como *temporal/situacional*: aplican cuando hay una secuencia larga de tareas dependientes y el costo de perder trabajo parcial es alto. No aplican al desarrollo cotidiano, y activarlas por defecto sería overhead sin beneficio.

El principio general que emerge de esto es más útil que cualquiera de las herramientas específicas: el overhead de documentación tiene que ser proporcional al riesgo concreto que mitiga, no al tamaño del proyecto. Un seguro pesado contra perder trabajo en un corte de sesión tiene sentido cuando ese riesgo está presente. No tiene sentido el resto del tiempo. Distinguir cuándo cada herramienta aplica es parte de lo que el operador tiene que aprender — y no está en ninguna regla escrita, porque depende del contexto de cada sesión.

### Lo que el sistema terminó siendo

Al final del proyecto, el sistema de documentación tenía cinco piezas con cinco funciones distintas. Las instrucciones de trabajo — un documento corto de reglas numeradas, pegado como primer mensaje de cada sesión, que crece solo cuando un error real genera una regla nueva. El estado actual del proyecto — lo que la IA necesita para trabajar hoy: qué existe, qué está vigente, qué versión es canónica, sin el peso del historial. El historial — todo lo que ya no es operativo pero vale la pena conservar, disponible para consulta pero sin cargarse por defecto. El registro de sesión — qué se hizo la última vez, qué falta, qué decisiones ya están cerradas, el handoff entre instancias. Y la capa para el operador — que no recibe las instrucciones de la IA, pero necesita saber cómo verificar que el sistema está funcionando. Ninguna es redundante con las demás. Todas emergieron de problemas reales, en el orden en que esos problemas aparecieron.

---

## 3 — El hallazgo central: la posición y el formato importan más que el contenido

Hay una intuición casi universal sobre cómo mejorar los resultados de la IA: escribir mejor las instrucciones. Si la IA no hace lo que se le pide, el diagnóstico natural es que el prompt estaba mal redactado, era ambiguo, o le faltaba detalle.

IRAM mostró que ese diagnóstico falla en una clase específica de situaciones. Y que la clase es más común de lo que parece.

### El problema que no era de contenido

A lo largo del proyecto, ciertos errores volvían a aparecer sesión tras sesión. No eran errores nuevos — eran exactamente los mismos. Y en todos los casos, la solución ya estaba documentada. La regla que lo cubría existía, estaba bien escrita, no tenía ambigüedad. La IA simplemente no la aplicaba.

El diagnóstico inicial fue el habitual: hay que explicarlo mejor. Se reescribió la regla. No cambió nada. Se agregó más contexto. Tampoco. El problema no era el contenido de la instrucción.

Lo que importaba era dónde vivía esa instrucción dentro del contexto.

El sistema de documentación del proyecto, en sus versiones tempranas, era un único documento de respaldo que acumulaba todo: instrucciones de trabajo, historial de versiones, decisiones de diseño, código, contexto técnico del juego. Al llegar a 220KB y casi 5000 líneas, la IA no podía priorizar. Una regla correctamente escrita, enterrada en el medio de miles de líneas de código y contexto técnico, competía por atención con todo lo demás — y perdía. No porque hubiera sido "olvidada": es que, en esa posición y en ese formato, recibía menos peso que el contenido que la rodeaba.

La solución no fue reescribir nada. Fue mover la regla: extraerla del documento de respaldo y pegarla como primer mensaje de la sesión, en un bloque corto y sin ruido alrededor.

Funcionó.

### El efecto es medible

Esto no es una impresión subjetiva. El proyecto generó datos sobre el costo de inicializar el contexto en distintos momentos de su evolución:

| Momento del proyecto | Mecanismo de contexto | Mensajes promedio hasta trabajo productivo |
|---|---|---|
| Antes de instrucciones formales | Contexto mezclado, sin estructura | 35.0 |
| Instrucciones pegadas como primer mensaje | Documento corto al inicio | 18.4 |
| + separación estado actual / histórico | Carga estructurada en capas | 14.1 |

La caída de 35.0 a 14.1 no se explica por tareas más simples — el proyecto se estaba volviendo más complejo en esa misma dirección. Se explica por el costo de inicializar el contexto. Y ese costo depende de la arquitectura, no del contenido.

Cada paso en la tabla corresponde a un cambio estructural que se puede fechar: el día en que las instrucciones pasaron a pegarse como primer mensaje, y el día en que se separó el estado actual del historial. Los dos cambios son el mismo principio aplicado dos veces: lo que va primero pesa más. Lo que compite con ruido, pierde.

### Posición y formato como variables de diseño

"Economía de contexto" fue la formulación que el propio proyecto usó para nombrar esto, en un meta-análisis escrito mientras el trabajo ocurría: *"las reglas R no son desconfianza sino economía de contexto — lo documentado no se rediscute, lo no documentado es espacio de colaboración."*

La frase nombra algo más preciso que "escribir bien los prompts". Las reglas no existen para restringir — existen para asignar atención. Lo que está documentado en el lugar correcto, con el formato correcto, no necesita ser explicado de nuevo. Le libera al operador y a la IA el espacio para trabajar en lo que todavía no está resuelto.

Dos variables concretas que emergieron del proyecto:

**Posición.** Lo primero que entra en un contexto nuevo pesa más que lo mismo enterrado más adentro. Las instrucciones de trabajo iban pegadas como primer bloque de cada sesión — no adjuntas como archivo, no mezcladas con el código. Esa decisión de posición era funcional, no estética.

**Formato.** Un bloque corto de reglas numeradas sin ruido alrededor recibe más peso que la misma información diluida en prosa. No porque la prosa sea menos clara — sino porque el formato señala jerarquía. La IA no lee un documento de contexto de manera uniforme: la densidad, la estructura y la posición relativa de cada bloque modifican cuánto peso le asigna.

El corolario práctico: si una instrucción se sigue de forma inconsistente a pesar de estar clara y bien escrita, el primer diagnóstico no debería ser "hay que explicarlo mejor". Debería ser "¿dónde vive esto en el contexto, y en qué formato, y qué está compitiendo con eso por atención?".

### Lo que esto implica para el diseño del sistema

Este hallazgo tiene consecuencias directas sobre cómo se construyó todo lo demás.

El PROMPT_MAESTRO — el documento de instrucciones de trabajo del proyecto — no creció de forma lineal. Cada regla que contiene es el residuo de un error real: algo que pasó, se identificó como patrón, y se documentó como regla. Pero la decisión sobre *dónde* poner esa regla, y en *qué formato*, fue tan importante como la regla en sí. Reglas con consecuencias críticas si se violan van marcadas visualmente y primero. Reglas de estilo van al final. La categorización no es cosmética — es arquitectura de atención.

El mismo principio se aplica al SESSION_LOG: existe porque "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó en la última sesión" son cosas distintas. El log es corto, está al final del bloque de inicio, y su único trabajo es cubrir ese hueco específico. Si fuera más largo, o estuviera en otra posición, haría lo mismo con más fricción.

La implicación más amplia: la arquitectura de un sistema de trabajo con IA no se mide solo por qué información contiene. Se mide por cómo está organizada esa información para que llegue al lugar correcto en el contexto, con el formato correcto, en el momento correcto. El contenido es necesario pero no suficiente.

---

## 4 — Cómo trabaja la IA: cuatro hallazgos con casos

Si la sección anterior documentó que *dónde* vive una instrucción importa más que qué dice, esta sección documenta lo que está debajo de eso: cómo trabaja la IA como herramienta, observada desde adentro de un proyecto que duró dos meses.

Los cuatro hallazgos son independientes — cada uno tiene evidencia propia y consecuencias operacionales propias. Pero comparten una forma: en todos los casos, el patrón se volvió visible porque el proyecto fue lo suficientemente largo para que apareciera más de una vez, y lo suficientemente documentado para que cuando apareció, hubiera registro de cuándo había pasado antes.

### 4A — La IA ejecuta. No diseña.

La forma más precisa de describir la división de trabajo en IRAM no es "el operador dirige, la IA ejecuta" en abstracto. Es una analogía más concreta: el operador fue el arquitecto; la IA fue una herramienta de precisión con capacidad de lenguaje. Un obrero de construcción tiene criterio propio y avisa si el plano está mal. La IA no. Coloca exactamente lo que se le indica, con el material que se le da, siguiendo el plano aunque el plano tenga un error.

Eso no es una limitación menor — es la base de la división de trabajo de todo el proyecto.

En la práctica, el patrón fue consistente. Las decisiones de arquitectura — qué alcance usar, cómo estructurar una función, qué convención adoptar — las originó el operador. La implementación dado ese diseño, la generación de código a partir de especificaciones, el reconocimiento de patrones de error a través de muchas sesiones: eso lo hizo la IA de forma rápida y confiable. La identificación de problemas técnicos del motor del juego fue, en la mayoría de los casos, colaborativa: ninguno de los dos tenía toda la información por separado.

Esta distribución no fue una decisión tomada al principio del proyecto. Emergió del proceso, y se volvió visible en retrospectiva. Hay un momento en el que se vuelve explícita: cuando el sistema de documentación alcanzó suficiente madurez para que una sesión de diseño de 75 mensajes pudiera traducirse en un SESSION_LOG_CONSOLIDADO — una especificación ejecutable de 13 tareas, sin decisiones pendientes, que la IA podía ejecutar sin tener que decidir nada. El número de mensajes del SESSION_LOG no era eficiencia de escritura. Era la evidencia de cuánto trabajo de diseño se había hecho antes de delegar la ejecución.

El concepto formal que nombra esto es *specification-driven development* con un componente de *Human-in-the-Loop* (HITL): el ciclo no es "pedirle a la IA que resuelva un problema", sino "diseñar la solución hasta que sea especificable, y después pedirle a la IA que la implemente". La calidad del output de la IA depende de la calidad de la especificación — y la especificación es trabajo del operador.

### 4B — La IA confunde "no documentado" con "no posible"

Hay un modo de falla específico de la IA que vale la pena conocer de antemano porque aparece con la misma confianza tanto cuando tiene razón como cuando no: afirma que algo es imposible, y lo dice en el mismo tono independientemente de si la imposibilidad es real o es solo la frontera de su conocimiento documentado.

El proyecto lo encontró dos veces, con el mismo patrón exacto.

El primer caso ocurrió sobre una función de interfaz del juego. La IA afirmó que cierto panel no admitía un tipo específico de elemento de interfaz — que lo que se pedía era imposible de implementar ahí. El operador cuestionó la afirmación. La IA investigó los archivos reales del juego — no su conocimiento general sobre el motor — y encontró que ese tipo de elemento sí existe, pero para un alcance distinto del mapa. El "no" final fue correcto, pero por una razón mucho más estrecha que la primera respuesta, y solo la investigación contra el archivo real la reveló.

El segundo caso ocurrió sobre operaciones a escala global. La IA afirmó que iterar sobre miles de elementos del mapa en cada pulso mensual no era viable por razones de rendimiento. El operador insistió: si el motor tiene esa estructura, debe existir alguna forma de filtrar. La solución resultó ser iterar solo sobre los elementos que tuvieran una marca específica activa — un subconjunto pequeño, no miles. Ese mecanismo de filtro desbloqueó todas las operaciones globales del mod.

En ambos casos el patrón es idéntico: la IA responde "no" desde su conocimiento documentado; el operador cuestiona desde lógica ("si esta estructura existe, debe ser accesible de alguna forma"); y lo que decide no es ninguno de los dos — es probar contra el sistema real. El árbitro nunca fue la IA. Siempre fue el motor.

El tercer caso es más sutil y más importante para el paper, porque documenta el mismo patrón con una fuente distinta. Durante una auditoría técnica del código, la IA recomendó remover una llamada de limpieza que ejecutaba inline en el on_action del juego, clasificándola como redundante. El operador cuestionó desde lógica de sincronización: `trigger_event` no garantiza ejecución en el mismo tick — si el evento corre en el tick siguiente, las variables siguen activas y el pulso mensual puede reintentarlo. El inline era el cleanup síncrono y garantizado; el redundante era el `immediate` de los eventos de completión. La decisión fue la inversa de lo que recomendó la auditoría: mantener el inline, remover el `immediate`. La auditoría había identificado correctamente que había algo duplicado — pero equivocado qué era lo prescindible. El árbitro, de nuevo, no fue la IA: fue el comportamiento del motor ante distintos órdenes de ejecución.

El concepto formal que nombra esto es *failure mode classification por fuente*: hay fallas epistémicas (la IA no sabe algo y lo afirma como imposible) y hay fallas técnicas (hay un bug real en el código). El tratamiento correcto es diferente para cada tipo. Una falla epistémica no se resuelve corrigiendo el código — se resuelve verificando contra el sistema real. Tratar cada "no es posible" de la IA como una hipótesis verificable, no como un veredicto, no es desconfianza generalizada: es el diagnóstico correcto del tipo de falla más frecuente.

La condición para que ese diagnóstico funcione es la misma que aparece en la sección 1: hace falta un árbitro claro. En un dominio donde la retroalimentación es ambigua o lenta, verificar se vuelve caro, y el costo de tratar cada "no" como hipótesis sube. Ese límite se retoma en la sección 7.

### 4C — Las decisiones descartadas tienen su propia audiencia

Un detalle de la documentación del proyecto pasó desapercibido durante meses, hasta que se lo miró de cerca: la sección de "alternativas evaluadas" — qué se consideró, qué se descartó, y por qué — no estaba dirigida al operador. Estaba dirigida a la IA futura.

Su función no era registrar historia. Era evitar que, seis semanas después, la IA volviera a proponer algo que ya había sido evaluado y descartado — con los mismos argumentos, con la misma confianza, sin saber que la conversación ya había ocurrido. El costo de re-proponer una idea descartada es asimétrico: el operador tiene el contexto completo de por qué se descartó; la IA, en una sesión nueva, no tiene nada. Sin registro, el ciclo se repite.

El proyecto produjo tres casos que ilustran por qué el "por qué" es tan importante como el "qué":

Un mecanismo de espera entre usos de una función se diseñó, implementó y probó — y se descubrió que la variable que lo controlaba nunca expiraba, porque el motor del juego no tiene una forma nativa de manejar ese tipo de tiempo. La decisión fue eliminarlo. Quedan documentados: qué era, por qué se creyó necesario, y por qué el motor lo hacía inviable. Cualquier sesión que quiera proponer algo similar tiene ese diagnóstico disponible.

Un esquema de identificadores numéricos (legible para el operador, opaco para cualquier verificación automática) se reemplazó por identificadores descriptivos en el rediseño mayor del proyecto. El código pasó a ser autoexplicativo sin necesitar una tabla de referencia aparte. La razón quedó documentada: no fue una preferencia estética.

Una convención sobre cuándo cobrar el costo de una operación (al confirmarla, no al activarla) respondió a una razón de experiencia de usuario muy concreta: si se cobra al activar, el jugador paga sin saber si la operación va a ejecutarse; si se cobra al confirmar, ya tuvo toda la información antes del costo. Esa razón, documentada, cierra la conversación la próxima vez que alguien proponga cobrar al activar.

El concepto formal que nombra esto es *Architecture Decision Records* (ADRs) — pero con una diferencia importante respecto al uso estándar: en IRAM los ADRs no estaban escritos para el operador humano. Estaban escritos para la instancia de IA que llegaría sin memoria a esa parte del proyecto. Esa diferencia de audiencia cambia cómo se escriben: la razón tiene que ser suficientemente explícita para que alguien sin contexto previo la entienda sin preguntar. Una sección de "alternativas descartadas" que solo dice *qué* se descartó, sin el *por qué*, no cumple esa función.

### 4D — El tiering no es opcional

A lo largo del proyecto se volvió evidente que no todas las tareas son equivalentes en términos de costo cognitivo para la IA, y que tratarlas como equivalentes genera un patrón de falla específico: la sesión empieza bien y empieza a degradarse.

El patrón tiene nombre operacional: hay tareas de diseño (alto nivel — decidir qué hacer, cómo estructurarlo, qué trade-offs aceptar) y tareas de ejecución (bajo nivel — implementar lo que ya fue diseñado, refactorizar código con instrucciones claras, aplicar reglas conocidas). Las dos tipos de tarea no se mezclan bien en la misma sesión, por una razón que conecta directamente con la sección 3: el contexto de una sesión de diseño acumula incertidumbre, alternativas abiertas y decisiones a mitad de camino — todo lo cual compite por atención cuando la misma sesión tiene que ejecutar código de precisión después.

Lo que el proyecto aprendió, documentado en la sesión 12, fue más específico que "no mezcles diseño con ejecución". Fue: el techo operacional por sesión, en modo de trabajo máximo, es aproximadamente una tarea mediana o dos tareas ligeras antes de que la calidad del output empiece a caer de forma visible. Ese techo no es una regla de estilo — es un límite empírico que apareció con suficiente consistencia para generar una regla explícita.

La consecuencia práctica es que el tiering es una decisión de planificación, no de preferencia. Si una sesión tiene que producir tanto el diseño de una función como su implementación, lo razonable no es pedirle a la IA que haga ambas cosas seguidas — es hacer la parte de diseño primero, cerrarla en una especificación escrita, y arrancar la parte de implementación desde esa especificación. El SESSION_LOG_CONSOLIDADO de la sección 4A es la misma idea: la sesión de 75 mensajes de diseño no termina con código. Termina con una especificación que la sesión de ejecución puede usar sin tener que decidir nada.

El concepto formal más cercano es la distinción entre *sistema 1* y *sistema 2* aplicada a la IA: hay outputs que salen de reconocimiento de patrones rápido y son muy confiables, y hay outputs que requieren razonamiento secuencial y son más frágiles bajo carga de contexto. Tiering es gestionar esa distinción de forma deliberada.

---

## 5 — Los datos del proceso

Las secciones anteriores describieron cómo funciona el sistema. Esta sección documenta si funcionó — con los números del proceso real.

Los datos vienen del historial completo: 336 conversaciones IRAM, 7345 mensajes post-deduplicación, 5 cuentas, procesados desde los archivos de exportación originales. Cuatro métricas, todas calculadas sobre el mismo corpus.

### El sistema se volvió más rápido mientras el problema se volvía más complejo

La velocidad de trabajo aumentó de forma monótona a lo largo del proyecto, sin excepción por fase:

| Fase | Días | Conv/día | Msg/conv | Costo de arranque (mediana) |
|------|------|----------|----------|------------------------------|
| v1-v2 | 13 | 1.8 | 37.0 | 14 mensajes |
| v3 | 30 | 5.1 | 24.4 | 9 mensajes |
| v4 | 13 | 7.2 | 22.3 | 7 mensajes |
| v5 | 7 | 9.4 | 9.6 | 5 mensajes |

"Costo de arranque" es el número de mensajes antes del primer output productivo (primer `create_file` o `str_replace`) en las conversaciones que tuvieron trabajo concreto. Cayó de 14 mensajes en v1-v2 a 5 en v5.

Eso no se explica porque v5 fuera más simple. El alcance del mod en v5 era mayor que en cualquier versión anterior — cuatro módulos independientes con namespace propio, después de un rediseño completo desde v4. Lo que cambió fue el costo de inicializar el contexto: el SESSION_LOG de v5 era una especificación ejecutable; el operador en v1-v2 todavía estaba explicando el proyecto desde cero en cada sesión. La duración mediana de conversación cayó en la misma dirección: de 3757 minutos en v1-v2 a 60 en v5. No porque el trabajo fuera menos — porque cada sesión arrancaba con más contexto estructurado y tenía un alcance más acotado.

### La investigación creció más rápido que el código — y eso es evidencia de planificación

El ratio entre operaciones de investigación (leer archivos, verificar estado, inspeccionar el motor) y operaciones de código (crear o modificar archivos) creció de forma consistente:

| Fase | Ratio Inv/Cód |
|------|---------------|
| v1-v2 | 1.8x |
| v3 | 2.0x (+12%) |
| v4 | 2.4x (+22%) |
| v5 | 2.9x (+22%) |

Una lectura posible es que el proyecto tuvo más bugs en las fases tardías. Los datos la descartan: las operaciones categorizadas como respuesta a errores se mantuvieron estables entre 1% y 3% en todas las fases. El tipo de investigación que creció fue distinto.

En v1-v2 y v3, la mayor parte era exploración de mecánicas del juego — grep por términos como `heir_weight`, `succession`, `treasury`. Buscar cómo funciona el motor. En v4 y v5, ese tipo desapareció casi por completo y fue reemplazado por investigación sobre la estructura del propio proyecto: verificar el estado de archivos, confirmar que los cambios anteriores habían quedado bien, auditar antes de avanzar. Las sesiones de mayor investigación en v5 tienen nombres como "audit 5.2", "Confirmación de cambios en archivos IRAM", "Plan de ejecución unificado v5.0" — planificación y verificación deliberadas, no debugging reactivo.

El ratio creciente no refleja un proyecto con más problemas. Refleja un proyecto donde verificar antes de modificar se volvió parte del proceso.

### La división de trabajo maduró: el operador especificó más, Claude produjo más por palabra

El argumento de la sección 4A — que la calidad del output de Claude depende de la calidad de la especificación — tiene correlato cuantitativo en las fases tardías del proyecto.

La longitud promedio de los mensajes del operador creció de 108 caracteres en v3 a 183 en v5, un 70% de aumento. El porcentaje de mensajes del operador con lenguaje explícito de decisión y diseño subió de 4.5% a 7.0% en el mismo período. El operador en v5 no estaba escribiendo más para explicar más — estaba especificando más antes de ejecutar.

Del otro lado, el ratio de producción de Claude — caracteres producidos por carácter recibido del operador — pasó de 7.4x en v1-v2 a 9.9x en v5. Claude produjo proporcionalmente más por unidad de input en las fases maduras, con mensajes que crecieron de un promedio de 983 caracteres en v1-v2 a 1659 en v5. El porcentaje de mensajes de Claude con lenguaje de razonamiento y planificación también subió: de 48% en v3 a 66% en v5, consistente con las sesiones de auditoría y verificación que dominaron esa fase.

Los dos efectos juntos son la misma historia contada desde los dos lados: especificaciones más precisas por parte del operador, outputs más sustanciales por parte de Claude, con menos mensajes de ajuste intermedio. Productividad agregada creciente — más conversaciones por día, menos mensajes por conversación, más output por mensaje.

### Lo que los datos no cubren

Dos métricas que habrían completado este cuadro no están disponibles. La distribución de autoría real dentro de las decisiones de diseño — qué fracción de las propuestas de arquitectura vino del operador versus fue generada por Claude y aceptada — no es recuperable del análisis de texto: el lenguaje de decisión aparece en ambos lados pero no dice quién inició la propuesta. Resolver eso requeriría anotación manual de una muestra. Y la complejidad técnica por fase como variable independiente del esfuerzo tampoco es directamente medible sin una métrica sobre el código producido: el análisis actual usa el esfuerzo como proxy, pero una especificación más corta que habilita código más complejo — que es el efecto que el sistema buscaba — no se captura por esa vía.

Lo que sí está disponible converge en la misma dirección: velocidad creciente, costo de arranque decreciente, investigación orientada a verificación en lugar de exploración, especificaciones más largas del operador y outputs más sustanciales de Claude. El sistema mejoró su throughput de forma consistente, y los indicadores de planificación deliberada crecieron junto con esa mejora, no a pesar de ella.

---

## 6 — Los conceptos formales que nombran lo que hicimos

Una de las cosas que ocurre cuando un proyecto se construye de forma empírica — resolviendo problemas en el orden en que aparecen, sin un marco teórico de partida — es que al final resulta que muchos de esos problemas ya tienen nombre. El nombre no estaba disponible durante el trabajo. Pero el problema, y la solución, sí.

Nombrar retroactivamente no es cosmético. Es lo que permite reconocer el mismo patrón en otro contexto, comunicarlo a alguien que no estuvo en el proyecto, y evaluar qué tan lejos está la práctica empírica de lo que la teoría recomienda. En algunos casos el proyecto llegó exactamente al mismo lugar que el concepto formal. En otros, llegó a una variante que la versión estándar no cubre — y esa diferencia es tan informativa como la coincidencia.

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

### Lo que el proyecto llegó al mismo lugar

**RAG manual.** El sistema de capas de IRAM — documento activo, archivo, instrucciones de trabajo, registro de sesión — resuelve exactamente el problema que RAG resuelve en sistemas más sofisticados: cómo proveer a un modelo de lenguaje información relevante sin saturar el contexto con todo lo disponible. La diferencia es de implementación. RAG automatiza la recuperación mediante embeddings y búsqueda semántica. IRAM lo hizo manualmente: el operador decide qué cargar en cada sesión según el tipo de trabajo. El principio es el mismo — contexto selectivo, no contexto total.

**Experimento natural con interrupted time series.** Los cuatro puntos de corte del proyecto (antes y después de cada cambio estructural mayor) tienen exactamente la forma de un diseño de interrupted time series: una serie temporal de mediciones (costo de inicialización de sesión, velocidad de desarrollo) con interrupciones correspondientes a intervenciones conocidas y fechadas. La tabla de la sección 3 es ese análisis aplicado. No fue diseñado como tal — emergió de que el proyecto tuvo la disciplina de medir consistentemente y de que los cambios estructurales tuvieron fechas exactas documentadas.

**Deuda técnica en sus tres formas.** El salto de v4 a v5 del mod fue, en gran parte, un ejercicio de pagar deuda técnica acumulada. *Namespace pollution*: todos los identificadores del mod compartían el espacio de nombres global del juego — se resolvió adoptando el prefijo `iram_`. *Coupling*: funciones interdependientes que no podían modificarse de forma aislada — se resolvió separando en cuatro módulos independientes. *Monolito*: un archivo único de casi 900 líneas — se resolvió distribuyendo en módulos con responsabilidad clara. Los tres tipos son estándar en la literatura; el proyecto los encontró en ese orden y los resolvió en ese orden.

### Lo que el proyecto hizo distinto

**ADRs orientados a IA.** Los Architecture Decision Records estándar son un artefacto para el equipo humano: registran qué se decidió, qué alternativas se evaluaron, y por qué se eligió lo que se eligió. En IRAM, esa función existía — pero la audiencia principal no era el operador. Era la instancia de IA que iba a llegar sin memoria a esa parte del proyecto y potencialmente iba a volver a proponer lo que ya estaba descartado. Eso cambia cómo se escriben: el nivel de explicitación del razonamiento tiene que ser suficiente para que alguien sin contexto previo lo entienda sin preguntar. Un ADR estándar puede asumir que quien lo lee tiene memoria de la conversación que lo generó. Un ADR orientado a IA no puede asumir nada.

**RAG manual como elección deliberada.** En el contexto de un proyecto de dos meses con un solo operador, implementar RAG automatizado habría sido overhead desproporcionado. La versión manual — el operador carga lo relevante, archiva lo que no lo es, decide qué entra en cada sesión — fue suficiente para el problema que resolvía y no requirió infraestructura adicional. Esto no es una limitación del proyecto: es una instancia del principio de la sección 2 (overhead proporcional al riesgo). La versión automatizada tiene sentido cuando el volumen de información disponible hace inviable la selección manual, o cuando hay múltiples operadores que necesitan consistencia sin coordinación. Ninguna de esas condiciones existía en IRAM.

### Lo que el proyecto no ejercitó

Dos áreas del programa de la diplomatura no tuvieron correlato en IRAM:

Herramientas de automatización no-code (Make, Zapier, n8n). El proyecto no tuvo flujos de trabajo que requirieran integración entre múltiples servicios externos. Todo el trabajo ocurrió dentro de conversaciones con IA y archivos locales.

Visión por computadora. No hubo datos visuales, imágenes, ni procesamiento de video en ninguna parte del proyecto. El dominio era scripting de texto para un motor de juego — sin componente visual más allá del juego mismo.

La ausencia de estas áreas no es un déficit del proyecto: es simplemente que el problema no las requería. Lo que sí ejercitó — en particular el diseño de sistemas, la gestión de estado entre instancias sin memoria compartida, y el análisis causal del proceso — no estaba en el diseño original del proyecto. Emergió de los mismos problemas que generaron todo lo demás.

---

## 7 — Qué transfiere y qué no

Antes de cerrar, conviene ser explícito sobre los límites de lo que este paper documenta. No porque los hallazgos sean frágiles — sino porque la honestidad sobre las condiciones bajo las cuales funcionaron es parte de lo que los hace útiles.

Tres condiciones estuvieron presentes en IRAM y definen el perfil de proyecto donde este sistema rinde al máximo. Su ausencia no significa que el sistema falle: significa que necesita adaptación que este documento no cubre.

### Las tres condiciones

**Criterio lógico preexistente.** Lo que este paper puede transferir es conocimiento sobre la herramienta: cómo estructurar el contexto, cómo diseñar el handoff entre sesiones, cómo gestionar la división de trabajo. Lo que no puede transferir es el pensamiento que construyó todo esto.

El criterio que hizo posible el proyecto — descomponer problemas en pasos verificables, buscar evidencia antes de aceptar una explicación, cuestionar una afirmación de imposibilidad desde lógica en lugar de aceptarla — no se desarrolló durante el proyecto. Se trajo de antes y se aplicó a un dominio nuevo. La sesión estratégica de mayo de 2026 lo nombró directamente: IRAM confirmó transferencia de habilidades, no aprendizaje desde cero.

Sin ese criterio previo, este sistema se puede copiar en su forma pero no en su función. Las reglas están escritas; el PROMPT_MAESTRO está documentado; el protocolo de sesión está especificado. Pero las reglas no se escriben solas — emergen de alguien que identifica un patrón, lo nombra, y decide que merece una regla. Esa capacidad no está en ningún archivo.

**Árbitro claro.** El ciclo hipótesis-prueba que aparece en la sección 4B funcionó porque había un árbitro inequívoco: el motor del juego corre o no corre, produce el comportamiento esperado o no lo produce. Cada iteración tenía un cierre sin ambigüedad.

En dominios donde la retroalimentación es lenta, subjetiva o difícil de interpretar — estrategia organizacional, investigación abierta, diseño de producto — el mismo ciclo tiene un costo radicalmente distinto. Verificar ya no es gratuito. Tratar cada "no" de la IA como hipótesis verificable sigue siendo correcto en principio, pero el costo de la verificación cambia el cálculo de cuándo vale la pena insistir.

**Problema acotado.** Alcance definible, resultado verificable, criterio de éxito observable. Eso es lo que permitió iterar rápido y saber, sin ambigüedad, cuándo algo estaba resuelto. La modularidad de v5 — cuatro mods independientes con namespace propio — no fue solo ingeniería: fue la condición que hizo posible trabajar en una parte sin romper otra. Proyectos más difusos, donde el criterio de éxito es negociable o donde las partes no son separables, no tienen ese cierre por iteración.

### La circularidad que no es un problema

Hay una tensión aparente en el primer punto que vale la pena resolver explícitamente, porque si no se resuelve parece circular.

Si el criterio para operar bien con IA se trae de antes, ¿qué aprendió exactamente el proyecto? ¿Y si las habilidades ya estaban, en qué sentido las entrenó?

La respuesta es que las dos cosas son simultáneamente ciertas sin contradicción. El criterio general — descomponer, verificar, cuestionar — estaba antes. Lo que el proyecto construyó fue criterio especializado: cuándo el contexto de una IA está saturado, cómo se ve un modo de falla epistémico versus uno técnico, cuánto overhead de documentación es proporcional a qué tipo de riesgo, cómo funciona el handoff entre instancias sin memoria. Ese conocimiento no existía antes del proyecto porque no había nada contra qué construirlo.

El criterio general es condición necesaria para operar bien. El criterio especializado es lo que el proyecto generó. Los dos son distintos y los dos son reales. La sesión estratégica de mayo lo vio así: el modding fue el camino hacia programación y ciencia de datos, y la IA se usó deliberadamente para saltear trabajo mecánico y de sintaxis — no para evitar el trabajo difícil. El trabajo difícil era el criterio. El dominio era el vehículo.

### El cuarto límite

Hay un límite adicional, más concreto que los tres anteriores: este sistema se construyó para esta herramienta específica.

La arquitectura de contexto de la sección 3 — posición como variable de diseño, formato como señal de jerarquía, separación activo/archivo — asume comportamientos particulares de este modelo. El techo operacional por sesión de la sección 4D es un límite empírico de este modelo en este tipo de tarea. No hay garantía de que ninguno de los dos transfiera sin ajuste a otro sistema.

Eso no invalida los hallazgos — invalida la posibilidad de aplicarlos directamente sin calibración. Un equipo que trabaje con otro modelo va a encontrar que algunos límites son distintos, que algunas posiciones en el contexto tienen pesos distintos, que el techo operacional cae en otro lugar. El método para encontrar esos límites es el mismo que usó IRAM: medir, variar una cosa a la vez, y dejar que el sistema sea el árbitro.

### El cierre

El techo de la herramienta es estructural y no se mueve: no tiene memoria entre sesiones, no sale del problema tal como se lo planteó, y le asigna menos peso a las instrucciones cuando el contexto está cargado. Gestionar ese techo — con arquitectura de contexto, con tiering, con especificaciones antes de ejecución — es el trabajo que este paper documentó.

El techo del operador se mueve con la experiencia. El criterio especializado que el proyecto generó no existía antes y existe ahora. Eso es transferible — no como receta, sino como mapa de qué preguntas hacer y qué evidencia buscar cuando las mismas situaciones aparecen en otro proyecto.

Este paper es, en el fondo, sobre cómo gestionar el primero lo suficientemente bien para que el segundo sea el único que importe.
