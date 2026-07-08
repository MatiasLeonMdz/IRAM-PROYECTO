---
name: desarrollo-multisesion-con-ia
description: Metodología para proyectos técnicos de larga duración desarrollados con asistencia de IA a través de muchas sesiones o cuentas sin memoria compartida entre ellas. Cubre arquitectura de contexto (por qué la posición de una instrucción importa más que su contenido), protocolo de inicio/cierre de sesión, generación de reglas a partir de errores recurrentes, rotación entre sesiones cuando hay límites de uso, y división de trabajo entre operador e IA. Usar siempre que se inicie, retome o reestructure un proyecto — mod de videojuego, pipeline de datos, automatización, proyecto de código propio — que se va a extender por muchas sesiones de IA, especialmente si ya aparecen señales de que las instrucciones "se olvidan", los mismos errores se repiten entre sesiones, o el sistema de documentación empieza a competir con el trabajo real. Derivado empíricamente del proyecto IRAM (mod de Imperator: Rome, 101+ conversaciones, 5 cuentas de Claude, ~7300 mensajes analizados).
---

# Desarrollo técnico con IA a través de muchas sesiones sin memoria compartida
### Metodología destilada del proyecto IRAM

> Este documento no es un manual de "buenas prácticas con IA" escrito desde la teoría. Es el resultado de un proyecto real — un mod para Imperator: Rome 2.0.4, construido en más de 101 conversaciones a través de 5 cuentas de Claude durante aproximadamente dos meses — analizado retrospectivamente para extraer qué problemas aparecieron, en qué orden, y qué prácticas los resolvieron. Cada sección sigue la misma forma: qué se hacía antes, qué problema generaba, qué se hizo en cambio, y qué evidencia respalda que funcionó. El mod fue el vehículo. Esto es el resultado.

---

## 1. Cuándo usar esto

Esto aplica cuando un proyecto va a extenderse por **muchas sesiones de IA que no comparten memoria entre sí** — ya sea porque el trabajo dura semanas o meses, porque hay un límite de mensajes o de uso que eventualmente va a forzar un reinicio, o simplemente porque el proyecto tiene suficiente complejidad interna como para que "volver a explicar todo cada vez" deje de funcionar.

No es necesario que el proyecto sea grande desde el día uno. IRAM empezó como una pregunta de una línea ("¿se puede redistribuir población automáticamente en este juego?") sin ningún sistema detrás. El sistema completo — capas de documentación, protocolo de sesión, reglas numeradas — emergió de forma reactiva, a medida que cada falta de estructura generaba un problema concreto. La señal de que esto aplica no es "el proyecto es ambicioso": es que algo ya está empezando a perderse entre sesiones.

Dos cosas se construyen en paralelo en un proyecto así, y vale la pena tenerlas en mente desde el principio: el entregable técnico (el mod, el pipeline, el script) y el sistema que permitió construirlo de forma sostenida. El segundo no es un subproducto accidental — en IRAM, la sesión estratégica que reformuló el sentido del proyecto lo dijo explícitamente: *"el mod exitoso es el entregable, el aprendizaje es el objetivo real."* Las dos cosas son el mismo objetivo visto desde dos ángulos.

---

## 2. Las dos historias del proyecto

Un proyecto largo con IA acumula dos historias distintas, y conviene no mezclarlas en los mismos documentos ni en los mismos párrafos.

La primera es la historia técnica: qué se construyó, en qué versión, con qué bugs y qué soluciones. En IRAM eso es la progresión v1 → v5, las funciones del mod, los errores de scripting. Es específica del dominio — a casi nadie le va a importar cómo se resolvió un bug de scope en Imperator: Rome.

La segunda es la historia de cómo el equipo (operador + IA) aprendió a trabajar. Cuándo apareció cada documento de contexto, qué problema resolvió, cómo cambió el protocolo de sesión. Esta es la historia que generaliza — es la que está detrás de este documento.

La razón práctica para separarlas no es estética. Cuando las dos se mezclan en el mismo log o la misma sección, dos cosas pasan: la IA no puede priorizar (¿esto es contexto técnico que necesito para programar, o es una regla sobre cómo trabajamos?) y, más importante, el patrón de la segunda historia — que es el que vale la pena formalizar — queda diluido entre detalles técnicos que no lo son. Mantenerlas separadas, aunque un mismo hito pertenezca a ambas, es lo que permite ver la segunda historia como una historia en sí misma.

---

## 3. El sistema de capas — por qué existe cada una (y la cuarta que no estaba contada)

El sistema de contexto de IRAM no se diseñó de arriba hacia abajo. Creció por presión: un único documento de respaldo ("SUPERBACKUP") fue acumulando todo — instrucciones de trabajo, historial de versiones, decisiones de diseño, contexto técnico — hasta llegar a unas 220KB. En ese tamaño, la IA dejó de poder priorizar: reglas que estaban ahí, documentadas, quedaban sepultadas entre contenido técnico y se ignoraban. Los mismos bugs volvían a aparecer aunque la solución ya estuviera escrita en el mismo archivo.

La respuesta fue separar por función, no por cronología:

- **Instrucciones de trabajo** (cómo operar, qué reglas seguir) — un documento corto, pegado al principio de cada sesión, que crece solo cuando un error real genera una regla nueva.
- **Estado actual** (qué es el proyecto *ahora*, qué es vigente) — lo que la IA necesita para trabajar hoy, sin el peso de versiones anteriores.
- **Historial / legacy** — todo lo que ya no es operativo pero vale la pena conservar (versiones descartadas, decisiones que se evaluaron y no se tomaron). Se consulta si hace falta, nunca se carga por defecto.
- **Registro de sesión** — qué se hizo la última vez, qué falta, qué quedó abierto. Cubre el hueco entre "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó ayer", que son cosas distintas.

Hay una quinta pieza que el sistema tenía desde temprano pero que nunca se nombró como capa aparte: un documento dirigido **al operador, no a la IA** — protocolo de reanudación, qué verificar para confirmar que el sistema seguía funcionando, ese tipo de cosas. Las instrucciones de trabajo le dicen a la IA cómo operar; este documento le dice al humano cómo verificar que la IA está operando bien. Son audiencias distintas, y por eso evolucionaron distinto. Vale la pena nombrar esta cuarta pieza desde el diseño, en lugar de descubrir más tarde que estaba ahí sin nombre.

---

## 4. Protocolo de sesión: arranque, trabajo, cierre

**Arranque.** Las instrucciones de trabajo se *pegan* como primer mensaje de la sesión — no se adjuntan como archivo, no van mezcladas con el resto del contexto. La sección 5 explica por qué esto no es un detalle cosmético. Junto con eso, se carga el estado actual y el registro de la última sesión, y se indica el objetivo concreto de esta sesión.

**Durante el trabajo,** un puñado de hábitos baratos evitan los errores más caros:
listar qué archivos hay disponibles antes de asumir nada; no truncar código fuente (solo truncar logs de error, que son ruido); trabajar a nivel de mensaje individual cuando se reconstruye una cronología, porque una sola conversación puede cubrir horas y varios temas distintos; y, si algo se va a fechar, preguntar la fecha/hora real en lugar de inferirla — los timestamps automáticos de las herramientas no siempre coinciden con el momento real del trabajo.

Cuando aparece algo que parece un hito (una decisión que va a importar después), documentarlo con cinco datos a la vez, sin estimarlos después: quién tuvo la iniciativa, qué problema lo generó, a qué historia pertenece (sección 2), si es permanente o situacional, y si está atado a una transición de sesión/cuenta. Hacerlo en el momento es mucho más barato que reconstruirlo después.

**Cierre.** Antes de terminar, una sola pregunta: *¿qué se decidió hoy que no estaba documentado antes?* La respuesta — aunque sea una línea — se registra como qué / cuándo / por qué. Esta pregunta es la que mantiene viva la segunda historia del proyecto (sección 2): sin ella, decisiones reales quedan solo en el historial de chat, donde son recuperables pero no van a ser leídas otra vez.

Este protocolo no es una imposición externa — es, literalmente, cómo se generó este mismo documento: una secuencia de sesiones, cada una cerrando con esa pregunta, hasta que hubo suficiente material acumulado para esta síntesis.

---

## 5. Arquitectura de contexto vs. contenido del prompt

Esta es la idea más transferible de todo el proyecto, y la menos intuitiva.

El problema no era que las instrucciones estuvieran mal escritas. Una regla podía estar documentada, correcta, sin ambigüedad — y la IA la seguía igual de mal que si no existiera, simplemente porque estaba en el lugar equivocado del contexto. Con suficiente contenido técnico cargado, una regla enterrada en un documento de respaldo recibía menos "peso" que el contenido técnico que la rodeaba. No es que la IA "olvidara" la regla — es que, al competir por atención contra miles de líneas de código y contexto, perdía.

El ejemplo más claro del proyecto: un error de scripting (usar una referencia inválida desde un cierto alcance del código) estaba documentado como error conocido desde una versión temprana del backup — y siguió apareciendo en código nuevo, sesión tras sesión, *a pesar de* estar documentado. La solución no fue reescribir la regla — ya estaba escrita con claridad. Fue cambiar *dónde vivía*: de estar embebida en un documento de contexto, a ser parte de un bloque corto pegado como primer mensaje de cada sesión nueva.

El efecto es medible, no anecdótico:

| Momento del proyecto | Mecanismo de contexto | Mensajes promedio hasta trabajo productivo |
|---|---|---|
| Antes de instrucciones formales | Contexto mezclado, sin estructura | 35.0 |
| Instrucciones pegadas como primer mensaje | Documento corto al inicio | 18.4 |
| + separación estado actual / histórico | Carga estructurada en capas | 14.1 |

La caída no se explica por tareas más simples — se explica por el costo de inicializar el contexto. Y ese costo depende de la arquitectura, no del contenido.

**Principio general:** si una instrucción se sigue de forma inconsistente a pesar de estar clara y bien escrita, el diagnóstico por defecto no debería ser "hay que explicarlo mejor". Debería ser "¿dónde vive esto en el contexto, y qué está compitiendo con eso por atención?". Lo primero que entra en un contexto nuevo pesa más que lo mismo enterrado más adentro.

---

## 6. División de trabajo operador/IA — qué delegar, qué no

La forma más precisa de describir la división de trabajo en IRAM no es "el operador dirige, la IA ejecuta" en abstracto — es una analogía concreta: **el operador fue el arquitecto, la IA fue una herramienta de precisión con capacidad de lenguaje.** Un obrero de construcción tiene criterio propio y avisa si el plano está mal. La IA no. Coloca exactamente lo que se le indica, con el material que se le da, siguiendo el plano aunque el plano tenga un error. Eso no es una limitación menor — es la base de todo lo demás en esta sección.

En la práctica, esto se tradujo en un patrón consistente: las decisiones de arquitectura (qué alcance usar, cómo estructurar una función, qué convención adoptar) y los criterios de diseño (costos, experiencia de usuario, qué documentar) los originó el operador. La implementación dado ese diseño, y el reconocimiento de patrones de error a través de muchas sesiones, los hizo la IA de forma consistente y rápida. La identificación de problemas técnicos del motor del juego fue, en la mayoría de los casos, colaborativa — ninguno de los dos tenía toda la información por separado.

Hay un modo de falla específico de la IA que vale la pena conocer de antemano, porque aparece con la misma confianza tanto cuando tiene razón como cuando no: **confunde "esto no está documentado" con "esto no es posible"**, y lo dice en el mismo tono en ambos casos. Dos casos del proyecto, con el mismo patrón exacto:

Primero, sobre una función de interfaz: la IA afirmó que cierto panel del juego no admitía un tipo de elemento de interfaz, que era imposible agregar lo que se pedía ahí. El operador cuestionó la afirmación. La IA investigó los archivos reales del juego — no su conocimiento general sobre el motor — y encontró que ese tipo de elemento *sí existe* para un alcance del mapa, pero no para el alcance específico del panel en cuestión. El "no" final fue correcto, pero por una razón mucho más estrecha que la primera respuesta, y solo la investigación contra el archivo real la reveló.

Segundo, sobre operaciones a nivel de todo el mapa: la IA afirmó que iterar sobre miles de elementos del mapa en cada pulso mensual no era viable por rendimiento. El operador insistió en que, si el motor tenía esa estructura, debía existir alguna forma de filtrar. La solución resultó ser iterar solo sobre los elementos que tuvieran una marca específica activa — un puñado, no miles. Ese mecanismo desbloqueó *todas* las operaciones globales del mod.

En ambos casos el patrón es idéntico: la IA responde "no" desde su conocimiento documentado, el operador cuestiona desde lógica ("si esta estructura existe, debe ser accesible de alguna forma"), y lo que decide no es ninguno de los dos — es probar contra el sistema real. **El árbitro nunca fue la IA. Siempre fue el motor.**

**Principio general:** tratar cada "no es posible" de la IA como una hipótesis verificable, no como un veredicto — pero solo cuando existe algo contra lo que verificarla (la sección 13 vuelve sobre esto). No es "no confiar en la IA"; es más preciso que eso: confiar en ella para lo que está dentro del problema planteado y del conocimiento documentado, y reservar el resto para el sistema real.

---

## 7. Sistema de versiones y entrega

Tres decisiones de diseño de IRAM ilustran un patrón sobre cómo se tomaron — y se documentaron — decisiones reversibles.

Un mecanismo de espera entre usos de una función se diseñó, se implementó y se probó — y se descubrió que la variable que lo controlaba nunca expiraba, porque el motor del juego no tiene una forma nativa de hacerlo. El operador propuso directamente eliminarlo: que las opciones se rehabiliten cuando la operación anterior termine, sin espera adicional. La IA confirmó que era la solución más limpia. La restricción que ya existía por otro lado era suficiente; el mecanismo de espera no aportaba nada jugable y era una fuente de bugs. Es un ejemplo limpio de "decisión empírica con árbitro claro": la pregunta era si el mecanismo era necesario, y la respuesta fue que no, sin ambigüedad.

Por otro lado, un esquema de identificadores numéricos (legible para el operador, opaco para la IA y para cualquier verificación automática) se reemplazó por identificadores descriptivos durante el rediseño mayor del proyecto — el código pasó a ser autoexplicativo sin necesitar una tabla de referencia aparte. Y una convención de costos ("se cobra al confirmar, no al activar") respondió a una razón de experiencia de usuario muy concreta: si se cobra al activar, se paga sin saber si la operación se va a ejecutar; si se cobra al confirmar, ya se tuvo toda la información antes del costo.

Lo que las tres comparten no es el contenido de la decisión, sino que **la razón quedó registrada junto con el resultado**. Una sección de "alternativas descartadas" que solo dice *qué* se descartó, sin el *por qué*, tiene un costo oculto: cuando alguien — humano o IA — vuelve a proponer la misma idea seis semanas después, no hay manera de responder rápido "ya lo evaluamos, y esto es lo que encontramos". La convención de nombres con fecha y hora para cada entrega, y un sistema de control de versiones como respaldo adicional a los archivos comprimidos, son la misma lógica aplicada al código: que el estado de cualquier momento sea recuperable, y que el porqué de cada cambio sea recuperable junto con él.

---

## 8. Herramientas situacionales: cuándo activarlas y cuándo no

No todas las prácticas de este documento son permanentes. Dos, específicamente, nacieron para una situación puntual y están marcadas explícitamente como tales: registros intermedios por tarea, y entregas parciales descargables después de cada tarea completada (en lugar de un único paquete al final de la sesión).

Las dos nacieron el mismo día, durante un rediseño grande con más de diez tareas interdependientes, cuando el operador preguntó algo muy simple: *"¿y si la sesión se corta, qué pasa con el trabajo de las tareas anteriores?"* La respuesta fue: sin ningún registro intermedio, ese trabajo vivía solo en la memoria de la sesión activa, y se perdía completo si la sesión se cortaba. La solución — un registro corto después de cada tarea, y una entrega descargable después de cada tarea — resuelve exactamente ese riesgo y ningún otro.

Por eso están marcadas como *temporal/situacional*, no como *permanente*: aplican cuando hay una secuencia larga de tareas dependientes en una sola sesión y el costo de perderlas sería alto. No aplican al desarrollo del día a día, y activarlas por defecto sería puro overhead. La misma lógica se aplica a una versión más elaborada del registro de sesión: para reworks grandes, el registro simple (qué pasó, qué falta) se expandió a cuatro partes — estado de ejecución, decisiones de diseño ya cerradas, plan con instrucciones exactas, material de referencia — porque para esos casos otra sesión de IA necesitaba poder *ejecutar* sin tener que *decidir*. Para trabajo normal, esa versión expandida es ruido.

**Principio general:** el overhead de documentación debe corresponder al riesgo específico que mitiga, no al tamaño del proyecto en general. Las herramientas pesadas son un seguro contra un modo de falla concreto (perder trabajo en un corte de sesión, o necesitar que otra sesión ejecute sin contexto de diseño). Se activan cuando ese riesgo está presente y se retiran cuando no — sin que eso implique que el sistema "falló" en algún sentido.

---

## 9. Rotación de contextos (no "cuentas paralelas")

Cuando un proyecto excede el límite de uso de una sola cuenta o conversación, la tentación es pensar el problema como "coordinar varios contextos en paralelo". En IRAM eso no es lo que pasó — y vale la pena ser preciso sobre el modelo correcto, porque el incorrecto sugiere una solución mucho más complicada de la que realmente hace falta.

El modelo real, verificado con la marca de tiempo de cada mensaje individual a lo largo de más de 7.300 mensajes: **cero** casos de mensajes a dos cuentas distintas intercalados dentro de una ventana corta. Cada cambio de cuenta fue un cierre y una apertura, no una superposición — la mayoría de los cambios ocurrieron entre 2 y 5 minutos después de la última interacción con la cuenta anterior. En el 87.8% de los días hubo más de una cuenta activa *en algún momento del día*, pero nunca al mismo tiempo. Cinco cuentas activas en un mes no es paralelismo — es rotación rápida y secuencial.

La causa fue simple: el límite de mensajes por cuenta forzaba el cambio. Lo que hizo que esa restricción se volviera un sistema funcional, en lugar de un caos, fue que el *estado del proyecto vivía afuera de la conversación* — en los documentos de las secciones 3 y 4. Cualquier cuenta, al cargar esos documentos como primer mensaje, podía retomar el trabajo desde donde había quedado, sin importar qué cuenta lo hubiera dejado ahí. Las cuentas eran intercambiables porque las instrucciones eran portables; lo único que las distinguía era su historial específico de conversación, que dejó de ser necesario.

Vale la pena notar, además, que la conclusión anterior — "son cuentas paralelas, un sistema distribuido" — se sostuvo durante un tiempo, basada en una métrica más gruesa (cuántas sesiones por cuenta hubo en un mes). No sobrevivió al pasar a la marca de tiempo de cada mensaje. Es, de hecho, una instancia más del patrón de la sección 6: una afirmación hecha con confianza desde una evidencia indirecta, cuestionada, y revisada al medir contra algo más directo.

**Principio general, y muy vigente:** si una herramienta de IA tiene límites de uso —por conversación, diarios, lo que sea— la respuesta no es coordinar sesiones "en paralelo". Es hacer que cada sesión sea descartable, manteniendo el estado del proyecto en un documento portable y no en el historial de la conversación. Cualquier sesión nueva se convierte entonces en un reemplazo directo de la que llegó a su límite.

---

## 10. Patrones de error comunes — con su historia de origen

No todos los errores recurrentes se resuelven igual, y distinguir el tipo de error determina si la solución es una herramienta o un cambio de arquitectura.

Un error de codificación de archivos apareció repetidamente, en distintas versiones y distintas cuentas, porque el método para crear esos archivos lo introducía de forma casi inevitable — editar el archivo y luego agregar manualmente la marca correcta dejaba el resultado corrupto la mayoría de las veces. La solución que lo eliminó para siempre no fue "tener más cuidado": fue un script que genera los archivos con la marca correcta desde el momento de creación, sin depender de que nadie se acuerde de un paso adicional. Esto es el primer tipo de error: **el proceso permite que ocurra, y la solución es hacer que el proceso lo impida estructuralmente.**

El error de la sección 5 (la referencia inválida desde un alcance incorrecto) es el segundo tipo: la regla ya estaba documentada, correcta, y siguió sin seguirse — no porque faltara información, sino porque esa información no tenía suficiente peso en el contexto donde se generaba el código nuevo. La solución no fue una herramienta. Fue arquitectura de contexto.

Hay un tercer tipo, más silencioso: un error de configuración (un espacio de nombres faltante) que no rompía nada visible — el mod cargaba sin errores, pero la función simplemente no existía en el juego. Apareció temprano, en varias cuentas distintas, y se volvió raro rápidamente — no porque el proceso cambiara, sino porque una vez que se sabía qué buscar, el síntoma (la función ausente) era fácil de reconocer.

Y hay un caso límite que vale la pena documentar aparte porque es sobre el sistema mismo, no sobre el código: en un momento del proyecto, las cinco cuentas pasaron un día entero — diez cambios de cuenta, cero líneas de código nuevas — exportando y consolidando historial de conversaciones. El sistema de documentación, por un día, *fue* el trabajo, en lugar de soportar el trabajo. Se detectó, se nombró, y generó reglas explícitas sobre cuándo y cuánto documentar. No volvió a pasar. La lección no es "documentar menos" — es que el trabajo de documentación necesita su propio presupuesto y criterio, igual que cualquier otra tarea, porque de lo contrario puede desplazar silenciosamente al trabajo que pretende apoyar.

---

## 11. Conexión con desarrollo de habilidades de análisis de datos

Esta conexión no fue un efecto secundario casual — fue, en retrospectiva, el punto central. La sesión que reformuló la visión del proyecto lo dijo así: el modding fue el camino ameno hacia programación y ciencia de datos, y la IA se usó deliberadamente para saltear trabajo mecánico y de sintaxis fina — no para evitar el trabajo difícil.

El mapa de habilidades que el proyecto efectivamente ejercitó incluye pensamiento computacional, diseño de sistemas, modelado cuantitativo, documentación técnica reproducible, colaboración estructurada con IA, gestión de proyecto, debugging sistemático y arquitectura de decisiones bajo incertidumbre. Las conexiones directas son concretas: el modelado económico del mod es modelado estadístico con otro vocabulario; los simuladores de las funciones de optimización son análisis de sensibilidad; la gestión del contexto de IA (secciones 3 a 5) es, en esencia, el mismo problema que aparece en cualquier flujo de análisis asistido por IA; y la disciplina de documentación reproducible de este proyecto es la misma disciplina que sostiene un notebook o un pipeline de datos.

La razón por la que *este* proyecto entrenó esas habilidades, específicamente, no es casual — depende de las mismas tres condiciones que la sección 13 identifica como las que hacen que todo este sistema funcione: un problema acotado, un árbitro claro (el motor del juego corre o no corre), y un registro sistemático del proceso. Esas tres condiciones juntas son, precisamente, las condiciones de entrenamiento que la mayoría de los entornos de aprendizaje de ciencia de datos no ofrecen de entrada. El ciclo empírico de la sección 6 — hipótesis, prueba contra el sistema real, resultado — *es* el método científico, aplicado a mecánicas de un videojuego en lugar de a datos; y transfiere porque transfiere el ciclo, no el dominio.

Hay además una evidencia cuantitativa de que el sistema, como tal, mejoró: la velocidad de trabajo pasó de menos de dos sesiones por día en las primeras versiones a más de nueve por día en la versión final, mientras el costo en mensajes por sesión bajó a una cuarta parte. La versión final no fue más rápida porque el problema fuera más simple — de hecho, su alcance era mayor. Fue más rápida porque el sistema se había internalizado. Eso, en sí mismo, es un resultado de mejora de proceso medido cuantitativamente — producido por el mismo proyecto que es el objeto de este documento.

---

## 12. Cómo evoluciona el sistema con el tiempo

El mecanismo que genera reglas nuevas (sección 4) cambió de naturaleza durante el proyecto, no solo de contenido. Al principio, las reglas aparecían de forma reactiva: un error se repetía las veces suficientes para que alguien dijera "esto necesita una regla". Hacia el final, el operador empezó a preguntar proactivamente, después de resolver *cualquier* problema — no solo los repetidos — "¿qué regla evita que esto vuelva a pasar?". La cadena (error → patrón → regla → documento de instrucciones) es la misma; lo que cambió es el disparador: de "pasó varias veces" a "pasó una vez, que no pase otra".

El registro de sesión tuvo una evolución parecida, de naturaleza más que de forma. Nació como lo que su nombre sugiere: un registro de qué pasó y qué sigue. Para el rediseño mayor del proyecto, con más de diez tareas interdependientes, se volvió otra cosa — una especificación con suficiente detalle (estado, decisiones ya cerradas, plan con comandos exactos, material de referencia) para que otra sesión de IA pudiera *ejecutar* sin tener que *decidir*. Esa transición — de registro a especificación ejecutable — no se planeó como tal; ocurrió porque la complejidad de ese rediseño específico lo exigió, y se quedó porque funcionó.

Hubo un día, hacia mitad del proyecto, que concentró un número desproporcionado de cambios estructurales: la adopción de un nombre más profesional para el documento de referencia técnica, la separación entre estado vigente e histórico, y la sesión estratégica que reformuló el sentido del proyecto — los tres el mismo día, con la inicialización de un sistema de control de versiones la mañana siguiente. Fue, además, el día de mayor intensidad de todo el proyecto. Probablemente no es casualidad: la intensidad genera la fricción, y la fricción es lo que dispara la consolidación. El sistema no evoluciona por calendario — evoluciona cuando el costo de seguir sin estructura supera, de forma visible, al costo de pararse a estructurar.

A lo largo del proyecto hubo alrededor de diez versiones del documento de instrucciones de trabajo. Cada una fue, en efecto, una hipótesis sobre qué arquitectura de contexto produciría resultados más consistentes — validada (o no) por la calidad del trabajo en las sesiones siguientes. El sistema que gestiona el proyecto se actualiza con el mismo criterio empírico que el proyecto mismo: el output es el árbitro.

---

## 13. Qué no es transferible

Para que este documento sea honesto, tiene que ser explícito sobre sus límites. Tres condiciones, presentes en IRAM, definen el perfil de proyecto donde este sistema rinde al máximo — y su ausencia no significa que el sistema falle, sino que necesita adaptación que este documento no cubre.

**Un criterio lógico preexistente.** Lo que este documento puede transferir es conocimiento sobre la herramienta — arquitectura de contexto, protocolos de sesión, cómo nacen y se mantienen las reglas. Lo que no puede transferir es el *pensamiento* que construyó todo esto. El criterio que lo hizo posible — descomponer problemas, buscar evidencia antes de aceptar una explicación, pedir el razonamiento detrás de una respuesta — no se desarrolló durante el proyecto: se trajo de antes y se aplicó a un dominio nuevo. Sin ese criterio previo, este sistema se puede copiar, pero no se puede operar con el mismo resultado.

**Un árbitro claro.** El ciclo de hipótesis-y-prueba de la sección 6 funcionó porque había un árbitro inequívoco: el motor del juego corre o no corre, hace lo que se espera o no lo hace. En dominios donde la retroalimentación es lenta, ambigua o subjetiva — estrategia, investigación abierta, diseño organizacional — el mismo ciclo tiene un costo radicalmente distinto, porque no hay un cierre tan claro para cada iteración.

**Un problema acotado.** Alcance definible, resultado verificable, criterio de éxito observable. Eso es lo que permitió iterar rápido y saber, sin ambigüedad, cuándo algo estaba resuelto. Proyectos más difusos carecen de ese cierre, y eso cambia el cálculo de cuánto vale la pena formalizar y cuándo.

Hay un límite adicional, más concreto: este sistema se construyó *para* esta herramienta específica. La arquitectura de contexto de la sección 5, los hábitos de carga, la forma de las instrucciones — todo asume el comportamiento particular de este modelo. No hay garantía de que se transfiera sin cambios a otra herramienta de IA.

Estas condiciones cierran el círculo con el principio que abrió todo esto: la IA no democratiza la programación. Permite ejecutar pensamiento estructurado en dominios técnicos sin dominar la mecánica de esos dominios — pero el límite no es la herramienta, es la calidad del pensamiento que la opera. La herramienta, además, tiene techo propio: no tiene memoria entre sesiones, no sale del problema tal como se lo planteó, y le da menos peso a las instrucciones cuando el contexto es largo. Ese techo es estructural y no se mueve. El techo del operador, en cambio, se mueve con la experiencia. Este documento es, en el fondo, sobre cómo gestionar el primero lo suficientemente bien para que el segundo sea el único que importe.

---

*Desarrollo multisesión con IA — v1.0 — destilado del proyecto IRAM, 2026-06-12*
