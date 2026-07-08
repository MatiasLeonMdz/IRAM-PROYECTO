WIKI_DOCUMENTACION_v1.md
176 líneas

md


SESSION_LOG_DOCUMENTACION_s23.md
200 líneas

md


METODOLOGIA_DOCUMENTACION_v1.md
118 líneas

md


TEMPLATES_DOCUMENTACION_v1.md
215 líneas

md


# PROMPT — REGLAS DE DOCUMENTACIÓN IRAM v2.0 ## Pegar como primer mensaje al inicio de cada sesión de documentación *Actualizado: 2026-06-17 | Extraído de PROMPT_MAESTRO_DOCUMENTACION v1.9 + correcciones s21* --- ``` ⚠ AVISO DE CARGA — LEER PRIMERO Este bloque llega como mensaje pegado p

pasted

20:19
Entendido. Ejecuto el protocolo de la IA ejecutora.


R1 — verificar archivos disponibles
R1 — verificar archivos disponibles

R1 — verificar archivos disponibles
bash

ls /mnt/user-data/uploads/
Salida

METODOLOGIA_DOCUMENTACION_v1.md
SESSION_LOG_DOCUMENTACION_s23.md
TEMPLATES_DOCUMENTACION_v1.md
WIKI_DOCUMENTACION_v1.md
Listo
R1 ejecutado. Archivos disponibles: los cuatro del sistema de documentación (WIKI, SESSION_LOG s23, METODOLOGIA, TEMPLATES). Todos están renderizados en el contexto — R20 verificado, no hay que leer nada adicional con bash_tool.

Lectura del SESSION_LOG s23: completa. Decisiones confirmadas leídas (DEC-01 a DEC-15). No redebato ninguna.

Estado de situación:

Sistema de cuatro archivos: ✅ completo (DEC-13, DEC-14, DEC-15)
Marco Conceptual: ✅ recuperado en WIKI (DEC-15)
TAREA 0 paso 0.1: ✅ ejecutada en s23
Archivos necesarios para TAREA 1 (draft S4) que NO están en este upload:

IRAM_C1_esqueleto_s17.md (estructura)
IRAM_C1_s1_draft_s20.md y IRAM_C1_s3_draft_s20.md (consistencia de voz)
IRAM_SKILL_desarrollo_con_IA_v1_0.md (hechos técnicos, secciones 6, 7, 10)
Tarea 0 paso 0.2 (auditoría SKILL v1.0 secciones 6, 7, 10) también requiere ese archivo.

Pregunta para el operador:

¿Qué querés hacer en esta sesión?

Las opciones según el SESSION_LOG:

A) TAREA 1 — Draft Sección 4 — para esto necesito que subas IRAM_C1_s1_draft_s20.md, IRAM_C1_s3_draft_s20.md, IRAM_C1_esqueleto_s17.md. El MATERIAL S4 ya está en el SESSION_LOG, así que puedo arrancar con la S4 aunque no esté el SKILL v1.0 (lo usaría solo para hechos técnicos opcionales).

B) TAREA 0 paso 0.2 — auditoría SKILL v1.0 secciones 6, 7, 10 — para esto necesito IRAM_SKILL_desarrollo_con_IA_v1_0.md.

C) Otra tarea del backlog (TAREA 3 — WIKI ACTIVE Sec 12, TAREA 2 — análisis JSONs si los tenés disponibles).

¿Qué tenés para subir esta sesión?


IRAM_SKILL_desarrollo_con_IA_v1_0 (2).md
md


IRAM_C1_esqueleto_s17.md
248 líneas

md


IRAM_C1_s1_draft_s20.md
53 líneas

md


IRAM_C1_s3_draft_s20.md
76 líneas

md

20:21
Archivos cargados. Verificando R20 — el SKILL v1.0 no está renderizado en contexto.


Ejecutó 3 comandos
Ejecutó 3 comandos

verificar estructura del SKILL v1.0 antes de leer secciones específicas
bash

cat /mnt/user-data/uploads/IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md | head -50
Salida

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

ver índice de secciones del SKILL v1.0
bash

grep -n "^## " /mnt/user-data/uploads/IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md
Salida

13:## 1. Cuándo usar esto
23:## 2. Las dos historias del proyecto
35:## 3. El sistema de capas — por qué existe cada una (y la cuarta que no estaba contada)
50:## 4. Protocolo de sesión: arranque, trabajo, cierre
65:## 5. Arquitectura de contexto vs. contenido del prompt
87:## 6. División de trabajo operador/IA — qué delegar, qué no
105:## 7. Sistema de versiones y entrega
117:## 8. Herramientas situacionales: cuándo activarlas y cuándo no
129:## 9. Rotación de contextos (no "cuentas paralelas")
143:## 10. Patrones de error comunes — con su historia de origen
157:## 11. Conexión con desarrollo de habilidades de análisis de datos
169:## 12. Cómo evoluciona el sistema con el tiempo
181:## 13. Qué no es transferible

leer secciones 6, 7, 10 del SKILL v1.0
bash

sed -n '87,200p' /mnt/user-data/uploads/IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md
Salida

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
Listo
Tengo todo el material necesario. Voy a ejecutar TAREA 0 paso 0.2 (auditoría SKILL v1.0 secciones 6, 7, 10) y luego TAREA 1 (draft S4) en la misma sesión, ya que la auditoría es insumo directo del draft.

TAREA 0 paso 0.2 — Auditoría SKILL v1.0 secciones 6, 7, 10
Resultado: tabla "válido como hecho / superado como framing"
Sección	Afirmación	Estado	Notas para S4
6 — División de trabajo	"La IA coloca exactamente lo que se le indica aunque el plano tenga un error"	✅ Hecho válido	Usar literalmente en 4A — es la formulación más precisa del SKILL
6	"confunde 'no documentado' con 'no posible', con la misma confianza en ambos casos"	✅ Hecho válido	Núcleo de 4B
6	Caso scripted_gui (panel de interfaz)	✅ Hecho válido	Caso canónico 4B
6	Caso scopes globales (iteración sobre miles de elementos)	✅ Hecho válido	Caso canónico 4B
6	"El árbitro nunca fue la IA. Siempre fue el motor."	✅ Hecho válido	Cierre de 4B — usar esta formulación
6	Framing: "qué delegar, qué no" como categoría de decisión	⚠ Superado	DEC-10: no es "delegar vs no delegar" sino descripción matizada de división real. En S4 no organizar por "qué delegar"
7 — Sistema de versiones	Caso mecanismo de espera (variable que no expiraba)	✅ Hecho válido	Ejemplo para 4C — decisión descartada con razón documentada
7	Caso identificadores descriptivos vs numéricos	✅ Hecho válido	Ejemplo para 4C
7	Caso convención de costos (cobrar al confirmar, no al activar)	✅ Hecho válido	Ejemplo para 4C
7	"la razón quedó registrada junto con el resultado"	✅ Hecho válido	Principio central de 4C
7	Framing: sección como "sistema de versiones y entrega"	⚠ Superado	El contenido real es sobre ADRs orientados a IA, no sobre sistema de versiones. El título de la sección desvía. En S4 reorganizar bajo 4C (ADRs)
7	"cuando alguien — humano o IA — vuelve a proponer la misma idea seis semanas después"	✅ Hecho válido	Esto sí nombra la función real de los ADRs orientados a IA. Usar en 4C.
10 — Patrones de error	Error de codificación de archivos → solución estructural (script)	✅ Hecho válido	Tipo 1 de failure mode (proceso permite el error)
10	Error de referencia inválida → solución de arquitectura de contexto	✅ Hecho válido	Tipo 2 de failure mode (problema de posición, ya cubierto en S3)
10	Error silencioso de namespace	✅ Hecho válido	Tipo 3 — síntoma sin crash visible
10	"las cinco cuentas pasaron un día entero — diez cambios de cuenta, cero líneas de código"	✅ Hecho válido	Esto pertenece a S5, no a S4 (es datos del proceso, no hallazgo sobre cómo trabaja la IA)
10	Framing: "patrones de error comunes" como categoría unificada	⚠ Superado en parte	En S4 solo va Tipo 2 (epistémico, 4B). Tipos 1 y 3 son técnicos — pertenecen a S2 o S5. No mezclar en 4B
Síntesis de la auditoría: Los hechos y casos concretos del SKILL v1.0 secciones 6, 7, 10 son sólidos y usables. Los tres framings superados son: (a) "qué delegar" como organizador de 4A, (b) "sistema de versiones" como etiqueta de lo que en realidad es ADRs orientados a IA, (c) mezcla de tipos de error en un solo bloque cuando solo el tipo epistémico va en S4.

Ahora el draft.


Draft Sección 4 del paper C1
Draft Sección 4 del paper C1

Draft Sección 4 del paper C1
IRAM_C1_s4_draft_s24.md
Listo
Ahora el SESSION_LOG actualizado.


Archivo creado, leyó un archivo
Archivo creado, leyó un archivo

SESSION LOG s24 actualizado
SESSION_LOG_DOCUMENTACION_s24.md

Presented 2 files
Listo
Lo que se hizo en esta sesión:

TAREA 0 paso 0.2 — completada. Los hechos y casos de las secciones 6, 7 y 10 del SKILL v1.0 son todos válidos y usables. Los tres framings superados: "qué delegar" como organizador de 4A, "sistema de versiones" como etiqueta de lo que son ADRs, y mezcla de tipos de error cuando solo el epistémico va en S4.

TAREA 1 — completada. Draft S4 con cuatro subsecciones:

4A (división de trabajo): el operador es el arquitecto, la IA es una herramienta de precisión con capacidad de lenguaje. El SESSION_LOG_CONSOLIDADO de 75 mensajes → 13 tareas sin decisiones pendientes como evidencia concreta.
4B (modo de falla epistémico): los dos casos canónicos del SKILL más el caso INC-13. Árbitro siempre fue el motor.
4C (ADRs orientados a IA): las decisiones descartadas están escritas para la instancia futura sin memoria, no para el operador. El "por qué" es lo que cierra la conversación la próxima vez.
4D (tiering): diseño en alto / ejecución en bajo. Techo empírico: ~1 tarea mediana o 2 ligeras por sesión.
Una deuda técnica que quedó abierta: el caso INC-13 en 4B está construido desde el MATERIAL S4 del log, no desde el SESSION_LOG v5.6 del proyecto. Si ese archivo está disponible en una sesión siguiente, conviene verificar que la descripción del caso es fiel a la fuente primaria.

Próximo paso: S2, S6 o S7 — ninguna de las tres está bloqueada. El SESSION_LOG s24 tiene las tres operacionalizadas con sus fuentes.


Iram c1 s4 draft s24
Documento · MD 

Session log documentacion s24
Documento · MD 
go

20:26

R1 — verificar archivos disponibles
R1 — verificar archivos disponibles

R1 — verificar archivos disponibles
bash

ls /mnt/user-data/uploads/
Salida

IRAM_C1_esqueleto_s17.md
IRAM_C1_s1_draft_s20.md
IRAM_C1_s3_draft_s20.md
IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md
METODOLOGIA_DOCUMENTACION_v1.md
SESSION_LOG_DOCUMENTACION_s23.md
TEMPLATES_DOCUMENTACION_v1.md
WIKI_DOCUMENTACION_v1.md
Listo
Todo renderizado en contexto. Arranco con S2.

El esqueleto s17 dice que S2 usa SKILL v1.0 secciones 3, 4, 8, 12 — las secciones 3 y 8 ya las leí, necesito 4 y 12.


Ejecutó 2 comandos
Ejecutó 2 comandos

leer secciones 4 y 12 del SKILL v1.0
bash

sed -n '65,130p' /mnt/user-data/uploads/IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md
Salida

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


leer sección 12 del SKILL v1.0
bash

sed -n '169,200p' /mnt/user-data/uploads/IRAM_SKILL_desarrollo_con_IA_v1_0__2_.md
Salida

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
Listo
Tengo todo el material. Escribo S2.


Draft Sección 2 del paper C1
Draft Sección 2 del paper C1

Draft Sección 2 del paper C1
IRAM_C1_s2_draft_s24.md
Listo
Ahora actualizo el SESSION_LOG.


Ejecutó un comando, archivo creado, leyó un archivo
Ejecutó un comando, archivo creado, leyó un archivo

verificar que el s24 está en outputs
bash

cat /mnt/user-data/outputs/SESSION_LOG_DOCUMENTACION_s24.md | head -5
Salida

# SESSION LOG — Documentación IRAM s24
**Fecha:** 2026-06-17
**Tipo:** Spec ejecutable — reemplaza SESSION_LOG_DOCUMENTACION_s23.md como fuente de verdad operativa
**Reemplaza:** SESSION_LOG_DOCUMENTACION_s23.md


SESSION LOG s25 actualizado con S2 completada
SESSION_LOG_DOCUMENTACION_s25.md

Presented 2 files
Listo
S2 completa. Seis secciones:

El problema que forzó el primer cambio — el SUPERBACKUP monolítico llegando a su límite funcional. La respuesta — separación en capas por función. El día que concentró todo — 2026-05-27 como evidencia de que el sistema evolucionó por presión, no por diseño. La cuarta pieza que no tenía nombre — la capa del operador, identificada como capa propia. Las herramientas que aparecieron y desaparecieron — las temporales/situacionales como evidencia del principio de overhead proporcional al riesgo. Y el cierre que lista las cinco piezas explícitamente.

Una nota que quedó en R14: S2 tiene riesgo de leerse como historia descriptiva. La voz de las otras secciones (S1, S3, S4) tiene argumento explícito en cada párrafo — S2 también lo tiene, pero vale la pena verificarlo en revisión final.

Estado actual del draft: S1 ✅ S2 ✅ S3 ✅ S4 ✅ — faltan S5 (bloqueada por JSONs), S6 y S7.

¿Seguimos con S6?


Iram c1 s2 draft s24
Documento · MD 

Session log documentacion s25
Documento · MD 
go

20:30
S6 usa el marco conceptual de la WIKI. Ya lo tengo en contexto — arranco directo.


Se crearon 2 archivos, leyó un archivo
Se crearon 2 archivos, leyó un archivo

Draft Sección 6 del paper C1
IRAM_C1_s6_draft_s25.md

SESSION LOG s26
SESSION_LOG_DOCUMENTACION_s26.md

Presented 2 files
Listo
S6 completa. Estructura: tabla de 13 entradas → tres subsecciones.

"Lo que el proyecto llegó al mismo lugar" cubre RAG manual, interrupted time series y deuda técnica en sus tres formas — los tres casos donde la práctica empírica llegó exactamente al concepto estándar. "Lo que el proyecto hizo distinto" cubre los dos casos donde hay una variante propia: ADRs con audiencia de IA (no equipo humano) y RAG manual como elección deliberada de proporcionalidad, no como limitación. "Lo que no ejercitó" nombra las dos áreas ausentes.

Una tensión que quedó en R14 para que el operador decida: la tabla tiene 13 entradas pero el marco conceptual de la WIKI tiene 12 clusters. Hay 3 entradas nuevas que emergen directamente de S2/S3/S4 pero no estaban explícitamente en la WIKI. Si querés alinear los números, avisá — se puede hacer antes de cerrar el paper.

Estado del draft: S1 ✅ S2 ✅ S3 ✅ S4 ✅ S6 ✅ — falta S7 (cierre, disponible) y S5 (bloqueada por JSONs).

¿Seguimos con S7?


Iram c1 s6 draft s25
Documento · MD 

Session log documentacion s26
Documento · MD 
hacemos las correcciones que sugeriste en esta sesion y pasamos a s7

20:39
Las correcciones pendientes son tres:

S4 4B — INC-13: descripción aproximada, necesita verificación contra fuente primaria. El SESSION_LOG v5.6 del proyecto no está disponible en este upload — no puedo verificar. Voy a marcar la descripción como "pendiente de verificación" con nota inline y seguir.
S2 — riesgo de voz descriptiva: revisar que cada párrafo tenga argumento explícito, no solo narración.
S6 — tabla con 13 entradas vs 12 clusters de la WIKI: decisión del operador. ¿Querés alinear a 12 o dejar las 13?
Mientras respondés eso, arranco con S2 y S4.


Leer S2 para revisar voz
Leer S2 para revisar voz

leer S2 para revisar voz
bash

cat /mnt/user-data/outputs/IRAM_C1_s2_draft_s24.md
Salida

# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 2 — Lo que tuvimos que construir (y por qué)

*Draft s24 — 2026-06-17*

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

Al final del proyecto, el sistema de documentación tenía cuatro capas:

Las instrucciones de trabajo — un documento corto de reglas numeradas, pegado como primer mensaje de cada sesión, que crece solo cuando un error real genera una regla nueva.

El estado actual del proyecto — lo que la IA necesita para trabajar hoy: qué existe, qué está vigente, qué versión es canónica. Sin el peso del historial.

El historial — todo lo que ya no es operativo pero vale la pena conservar. Se consulta si hace falta; no se carga por defecto.

El registro de sesión — qué se hizo la última vez, qué falta, qué decisiones ya están cerradas. El handoff entre instancias.

Más la capa para el operador — que no recibe las instrucciones de la IA, pero necesita saber cómo verificar que el sistema está funcionando.

Cinco piezas con cinco funciones distintas. Ninguna es redundante con las demás. Y todas emergieron de problemas reales, en el orden en que esos problemas aparecieron.

---

*Sección 2 — draft s24 — 2026-06-17*
Listo
S2 está bien — el argumento está explícito en cada sección. El riesgo que identifiqué era real pero el texto ya lo resuelve: cada subsección tiene un "por qué importa" claro, no solo descripción. No necesita cambios de voz.

Lo que sí veo en S2: la sección de cierre ("Lo que el sistema terminó siendo") lista las piezas con párrafos separados de una sola oración cada uno — queda fragmentado comparado con el resto del paper. Lo consolido en prosa corrida.

Ahora S4 — reviso 4B para marcar el INC-13 correctamente.


Leer S4 para revisar 4B
Leer S4 para revisar 4B

leer S4 para revisar 4B
bash

cat /mnt/user-data/outputs/IRAM_C1_s4_draft_s24.md
Salida

# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 4 — Cómo trabaja la IA: cuatro hallazgos con casos

*Draft s24 — 2026-06-17*

---

Si la sección anterior documentó que *dónde* vive una instrucción importa más que qué dice, esta sección documenta lo que está debajo de eso: cómo trabaja la IA como herramienta, observada desde adentro de un proyecto que duró dos meses.

Los cuatro hallazgos son independientes — cada uno tiene evidencia propia y consecuencias operacionales propias. Pero comparten una forma: en todos los casos, el patrón se volvió visible porque el proyecto fue lo suficientemente largo para que apareciera más de una vez, y lo suficientemente documentado para que cuando apareció, hubiera registro de cuándo había pasado antes.

---

### 4A — La IA ejecuta. No diseña.

La forma más precisa de describir la división de trabajo en IRAM no es "el operador dirige, la IA ejecuta" en abstracto. Es una analogía más concreta: el operador fue el arquitecto; la IA fue una herramienta de precisión con capacidad de lenguaje. Un obrero de construcción tiene criterio propio y avisa si el plano está mal. La IA no. Coloca exactamente lo que se le indica, con el material que se le da, siguiendo el plano aunque el plano tenga un error.

Eso no es una limitación menor — es la base de la división de trabajo de todo el proyecto.

En la práctica, el patrón fue consistente. Las decisiones de arquitectura — qué alcance usar, cómo estructurar una función, qué convención adoptar — las originó el operador. La implementación dado ese diseño, la generación de código a partir de especificaciones, el reconocimiento de patrones de error a través de muchas sesiones: eso lo hizo la IA de forma rápida y confiable. La identificación de problemas técnicos del motor del juego fue, en la mayoría de los casos, colaborativa: ninguno de los dos tenía toda la información por separado.

Esta distribución no fue una decisión tomada al principio del proyecto. Emergió del proceso, y se volvió visible en retrospectiva. Hay un momento en el que se vuelve explícita: cuando el sistema de documentación alcanzó suficiente madurez para que una sesión de diseño de 75 mensajes pudiera traducirse en un SESSION_LOG_CONSOLIDADO — una especificación ejecutable de 13 tareas, sin decisiones pendientes, que la IA podía ejecutar sin tener que decidir nada. El número de mensajes del SESSION_LOG no era eficiencia de escritura. Era la evidencia de cuánto trabajo de diseño se había hecho antes de delegar la ejecución.

El concepto formal que nombra esto es *specification-driven development* con un componente de *Human-in-the-Loop* (HITL): el ciclo no es "pedirle a la IA que resuelva un problema", sino "diseñar la solución hasta que sea especificable, y después pedirle a la IA que la implemente". La calidad del output de la IA depende de la calidad de la especificación — y la especificación es trabajo del operador.

---

### 4B — La IA confunde "no documentado" con "no posible"

Hay un modo de falla específico de la IA que vale la pena conocer de antemano porque aparece con la misma confianza tanto cuando tiene razón como cuando no: afirma que algo es imposible, y lo dice en el mismo tono independientemente de si la imposibilidad es real o es solo la frontera de su conocimiento documentado.

El proyecto lo encontró dos veces, con el mismo patrón exacto.

El primer caso ocurrió sobre una función de interfaz del juego. La IA afirmó que cierto panel no admitía un tipo específico de elemento de interfaz — que lo que se pedía era imposible de implementar ahí. El operador cuestionó la afirmación. La IA investigó los archivos reales del juego — no su conocimiento general sobre el motor — y encontró que ese tipo de elemento sí existe, pero para un alcance distinto del mapa. El "no" final fue correcto, pero por una razón mucho más estrecha que la primera respuesta, y solo la investigación contra el archivo real la reveló.

El segundo caso ocurrió sobre operaciones a escala global. La IA afirmó que iterar sobre miles de elementos del mapa en cada pulso mensual no era viable por razones de rendimiento. El operador insistió: si el motor tiene esa estructura, debe existir alguna forma de filtrar. La solución resultó ser iterar solo sobre los elementos que tuvieran una marca específica activa — un subconjunto pequeño, no miles. Ese mecanismo de filtro desbloqueó todas las operaciones globales del mod.

En ambos casos el patrón es idéntico: la IA responde "no" desde su conocimiento documentado; el operador cuestiona desde lógica ("si esta estructura existe, debe ser accesible de alguna forma"); y lo que decide no es ninguno de los dos — es probar contra el sistema real. El árbitro nunca fue la IA. Siempre fue el motor.

El tercer caso es más sutil y más importante para el paper, porque documenta el mismo patrón con una fuente distinta. En una auditoría técnica durante el desarrollo, la IA recomendó remover cierto elemento del código por razones de limpieza. El operador cuestionó la recomendación: si el elemento estaba ahí, probablemente cumplía una función. La verificación contra el motor del juego confirmó que sí — removerlo rompía el comportamiento esperado. La auditoría había sido correcta en identificar el elemento como candidato a revisar, pero equivocada en el diagnóstico. El árbitro, de nuevo, no fue la IA.

El concepto formal que nombra esto es *failure mode classification por fuente*: hay fallas epistémicas (la IA no sabe algo y lo afirma como imposible) y hay fallas técnicas (hay un bug real en el código). El tratamiento correcto es diferente para cada tipo. Una falla epistémica no se resuelve corrigiendo el código — se resuelve verificando contra el sistema real. Tratar cada "no es posible" de la IA como una hipótesis verificable, no como un veredicto, no es desconfianza generalizada: es el diagnóstico correcto del tipo de falla más frecuente.

La condición para que ese diagnóstico funcione es la misma que aparece en la sección 1: hace falta un árbitro claro. En un dominio donde la retroalimentación es ambigua o lenta, verificar se vuelve caro, y el costo de tratar cada "no" como hipótesis sube. Ese límite se retoma en la sección 7.

---

### 4C — Las decisiones descartadas tienen su propia audiencia

Un detalle de la documentación del proyecto pasó desapercibido durante meses, hasta que se lo miró de cerca: la sección de "alternativas evaluadas" — qué se consideró, qué se descartó, y por qué — no estaba dirigida al operador. Estaba dirigida a la IA futura.

Su función no era registrar historia. Era evitar que, seis semanas después, la IA volviera a proponer algo que ya había sido evaluado y descartado — con los mismos argumentos, con la misma confianza, sin saber que la conversación ya había ocurrido. El costo de re-proponer una idea descartada es asimétrico: el operador tiene el contexto completo de por qué se descartó; la IA, en una sesión nueva, no tiene nada. Sin registro, el ciclo se repite.

El proyecto produjo tres casos que ilustran por qué el "por qué" es tan importante como el "qué":

Un mecanismo de espera entre usos de una función se diseñó, implementó y probó — y se descubrió que la variable que lo controlaba nunca expiraba, porque el motor del juego no tiene una forma nativa de manejar ese tipo de tiempo. La decisión fue eliminarlo. Quedan documentados: qué era, por qué se creyó necesario, y por qué el motor lo hacía inviable. Cualquier sesión que quiera proponer algo similar tiene ese diagnóstico disponible.

Un esquema de identificadores numéricos (legible para el operador, opaco para cualquier verificación automática) se reemplazó por identificadores descriptivos en el rediseño mayor del proyecto. El código pasó a ser autoexplicativo sin necesitar una tabla de referencia aparte. La razón quedó documentada: no fue una preferencia estética.

Una convención sobre cuándo cobrar el costo de una operación (al confirmarla, no al activarla) respondió a una razón de experiencia de usuario muy concreta: si se cobra al activar, el jugador paga sin saber si la operación va a ejecutarse; si se cobra al confirmar, ya tuvo toda la información antes del costo. Esa razón, documentada, cierra la conversación la próxima vez que alguien proponga cobrar al activar.

El concepto formal que nombra esto es *Architecture Decision Records* (ADRs) — pero con una diferencia importante respecto al uso estándar: en IRAM los ADRs no estaban escritos para el operador humano. Estaban escritos para la instancia de IA que llegaría sin memoria a esa parte del proyecto. Esa diferencia de audiencia cambia cómo se escriben: la razón tiene que ser suficientemente explícita para que alguien sin contexto previo la entienda sin preguntar. Una sección de "alternativas descartadas" que solo dice *qué* se descartó, sin el *por qué*, no cumple esa función.

---

### 4D — El tiering no es opcional

A lo largo del proyecto se volvió evidente que no todas las tareas son equivalentes en términos de costo cognitivo para la IA, y que tratarlas como equivalentes genera un patrón de falla específico: la sesión empieza bien y empieza a degradarse.

El patrón tiene nombre operacional: hay tareas de diseño (alto nivel — decidir qué hacer, cómo estructurarlo, qué trade-offs aceptar) y tareas de ejecución (bajo nivel — implementar lo que ya fue diseñado, refactorizar código con instrucciones claras, aplicar reglas conocidas). Las dos tipos de tarea no se mezclan bien en la misma sesión, por una razón que conecta directamente con la sección 3: el contexto de una sesión de diseño acumula incertidumbre, alternativas abiertas y decisiones a mitad de camino — todo lo cual compite por atención cuando la misma sesión tiene que ejecutar código de precisión después.

Lo que el proyecto aprendió, documentado en la sesión 12, fue más específico que "no mezcles diseño con ejecución". Fue: el techo operacional por sesión, en modo de trabajo máximo, es aproximadamente una tarea mediana o dos tareas ligeras antes de que la calidad del output empiece a caer de forma visible. Ese techo no es una regla de estilo — es un límite empírico que apareció con suficiente consistencia para generar una regla explícita.

La consecuencia práctica es que el tiering es una decisión de planificación, no de preferencia. Si una sesión tiene que producir tanto el diseño de una función como su implementación, lo razonable no es pedirle a la IA que haga ambas cosas seguidas — es hacer la parte de diseño primero, cerrarla en una especificación escrita, y arrancar la parte de implementación desde esa especificación. El SESSION_LOG_CONSOLIDADO de la sección 4A es la misma idea: la sesión de 75 mensajes de diseño no termina con código. Termina con una especificación que la sesión de ejecución puede usar sin tener que decidir nada.

El concepto formal más cercano es la distinción entre *sistema 1* y *sistema 2* aplicada a la IA: hay outputs que salen de reconocimiento de patrones rápido y son muy confiables, y hay outputs que requieren razonamiento secuencial y son más frágiles bajo carga de contexto. Tiering es gestionar esa distinción de forma deliberada.

---

*Sección 4 — draft s24 — 2026-06-17*
*Condición de completitud: 4A, 4B, 4C, 4D completos.*
*Siguiente: Sección 2 (Lo que tuvimos que construir) o Sección 6 (Conceptos formales).*
Listo
Bien. Las correcciones concretas son:

S2: consolidar el cierre fragmentado en prosa corrida.
S4 4B: el tercer caso (INC-13) está bien escrito pero la descripción es aproximada — lo señalo con una nota inline sin cambiar el argumento.

Genero las versiones corregidas.


Ejecutó 2 comandos
Ejecutó 2 comandos

generar S2 corregida
bash

cat > /mnt/user-data/outputs/IRAM_C1_s2_draft_s25.md << 'EOF'
# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 2 — Lo que tuvimos que construir (y por qué)

*Draft s25 — corrección de s24 — 2026-06-17*

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

Al final del proyecto, el sistema de documentación tenía cinco piezas con cinco funciones distintas, ninguna redundante con las demás: las instrucciones de trabajo (reglas numeradas, pegadas como primer mensaje, que crecen solo cuando un error real genera una regla nueva), el estado actual del proyecto (lo que la IA necesita para trabajar hoy, sin el peso del historial), el historial (todo lo que ya no es operativo pero vale la pena conservar, consultado si hace falta, nunca cargado por defecto), el registro de sesión (qué se hizo, qué falta, qué decisiones ya están cerradas — el handoff entre instancias), y la capa para el operador (que no recibe las instrucciones de la IA, pero necesita saber cómo verificar que el sistema está funcionando). Todas emergieron de problemas reales, en el orden en que esos problemas aparecieron.

---

*Sección 2 — draft s25 — corrección de s24 — 2026-06-17*
EOF
Salida

exit code 0

generar S4 corregida con nota inline en INC-13
bash

cat > /mnt/user-data/outputs/IRAM_C1_s4_draft_s25.md << 'EOF'
# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 4 — Cómo trabaja la IA: cuatro hallazgos con casos

*Draft s25 — corrección de s24 — 2026-06-17*

---

Si la sección anterior documentó que *dónde* vive una instrucción importa más que qué dice, esta sección documenta lo que está debajo de eso: cómo trabaja la IA como herramienta, observada desde adentro de un proyecto que duró dos meses.

Los cuatro hallazgos son independientes — cada uno tiene evidencia propia y consecuencias operacionales propias. Pero comparten una forma: en todos los casos, el patrón se volvió visible porque el proyecto fue lo suficientemente largo para que apareciera más de una vez, y lo suficientemente documentado para que cuando apareció, hubiera registro de cuándo había pasado antes.

---

### 4A — La IA ejecuta. No diseña.

La forma más precisa de describir la división de trabajo en IRAM no es "el operador dirige, la IA ejecuta" en abstracto. Es una analogía más concreta: el operador fue el arquitecto; la IA fue una herramienta de precisión con capacidad de lenguaje. Un obrero de construcción tiene criterio propio y avisa si el plano está mal. La IA no. Coloca exactamente lo que se le indica, con el material que se le da, siguiendo el plano aunque el plano tenga un error.

Eso no es una limitación menor — es la base de la división de trabajo de todo el proyecto.

En la práctica, el patrón fue consistente. Las decisiones de arquitectura — qué alcance usar, cómo estructurar una función, qué convención adoptar — las originó el operador. La implementación dado ese diseño, la generación de código a partir de especificaciones, el reconocimiento de patrones de error a través de muchas sesiones: eso lo hizo la IA de forma rápida y confiable. La identificación de problemas técnicos del motor del juego fue, en la mayoría de los casos, colaborativa: ninguno de los dos tenía toda la información por separado.

Esta distribución no fue una decisión tomada al principio del proyecto. Emergió del proceso, y se volvió visible en retrospectiva. Hay un momento en el que se vuelve explícita: cuando el sistema de documentación alcanzó suficiente madurez para que una sesión de diseño de 75 mensajes pudiera traducirse en un SESSION_LOG_CONSOLIDADO — una especificación ejecutable de 13 tareas, sin decisiones pendientes, que la IA podía ejecutar sin tener que decidir nada. El número de mensajes del SESSION_LOG no era eficiencia de escritura. Era la evidencia de cuánto trabajo de diseño se había hecho antes de delegar la ejecución.

El concepto formal que nombra esto es *specification-driven development* con un componente de *Human-in-the-Loop* (HITL): el ciclo no es "pedirle a la IA que resuelva un problema", sino "diseñar la solución hasta que sea especificable, y después pedirle a la IA que la implemente". La calidad del output de la IA depende de la calidad de la especificación — y la especificación es trabajo del operador.

---

### 4B — La IA confunde "no documentado" con "no posible"

Hay un modo de falla específico de la IA que vale la pena conocer de antemano porque aparece con la misma confianza tanto cuando tiene razón como cuando no: afirma que algo es imposible, y lo dice en el mismo tono independientemente de si la imposibilidad es real o es solo la frontera de su conocimiento documentado.

El proyecto lo encontró dos veces, con el mismo patrón exacto.

El primer caso ocurrió sobre una función de interfaz del juego. La IA afirmó que cierto panel no admitía un tipo específico de elemento de interfaz — que lo que se pedía era imposible de implementar ahí. El operador cuestionó la afirmación. La IA investigó los archivos reales del juego — no su conocimiento general sobre el motor — y encontró que ese tipo de elemento sí existe, pero para un alcance distinto del mapa. El "no" final fue correcto, pero por una razón mucho más estrecha que la primera respuesta, y solo la investigación contra el archivo real la reveló.

El segundo caso ocurrió sobre operaciones a escala global. La IA afirmó que iterar sobre miles de elementos del mapa en cada pulso mensual no era viable por razones de rendimiento. El operador insistió: si el motor tiene esa estructura, debe existir alguna forma de filtrar. La solución resultó ser iterar solo sobre los elementos que tuvieran una marca específica activa — un subconjunto pequeño, no miles. Ese mecanismo de filtro desbloqueó todas las operaciones globales del mod.

En ambos casos el patrón es idéntico: la IA responde "no" desde su conocimiento documentado; el operador cuestiona desde lógica ("si esta estructura existe, debe ser accesible de alguna forma"); y lo que decide no es ninguno de los dos — es probar contra el sistema real. El árbitro nunca fue la IA. Siempre fue el motor.

Hay un tercer caso con una variante del mismo patrón. Durante una auditoría técnica, la IA recomendó remover un elemento del código por razones de limpieza. El operador cuestionó la recomendación: si el elemento estaba ahí, probablemente cumplía una función. La verificación contra el motor confirmó que sí — removerlo rompía el comportamiento esperado. Aquí la IA no dijo "imposible" sino "innecesario", pero la estructura es la misma: una afirmación hecha desde conocimiento parcial, cuestionada por el operador, resuelta por el sistema real. El árbitro, de nuevo, no fue la IA. [⚠ verificar descripción exacta del caso contra SESSION_LOG v5.6 del proyecto cuando esté disponible]

El concepto formal que nombra esto es *failure mode classification por fuente*: hay fallas epistémicas (la IA no sabe algo y lo afirma como imposible o innecesario) y hay fallas técnicas (hay un bug real en el código). El tratamiento correcto es diferente para cada tipo. Una falla epistémica no se resuelve corrigiendo el código — se resuelve verificando contra el sistema real. Tratar cada "no es posible" de la IA como una hipótesis verificable, no como un veredicto, no es desconfianza generalizada: es el diagnóstico correcto del tipo de falla más frecuente.

La condición para que ese diagnóstico funcione es la misma que aparece en la sección 1: hace falta un árbitro claro. En un dominio donde la retroalimentación es ambigua o lenta, verificar se vuelve caro, y el costo de tratar cada "no" como hipótesis sube. Ese límite se retoma en la sección 7.

---

### 4C — Las decisiones descartadas tienen su propia audiencia

Un detalle de la documentación del proyecto pasó desapercibido durante meses, hasta que se lo miró de cerca: la sección de "alternativas evaluadas" — qué se consideró, qué se descartó, y por qué — no estaba dirigida al operador. Estaba dirigida a la IA futura.

Su función no era registrar historia. Era evitar que, seis semanas después, la IA volviera a proponer algo que ya había sido evaluado y descartado — con los mismos argumentos, con la misma confianza, sin saber que la conversación ya había ocurrido. El costo de re-proponer una idea descartada es asimétrico: el operador tiene el contexto completo de por qué se descartó; la IA, en una sesión nueva, no tiene nada. Sin registro, el ciclo se repite.

El proyecto produjo tres casos que ilustran por qué el "por qué" es tan importante como el "qué":

Un mecanismo de espera entre usos de una función se diseñó, implementó y probó — y se descubrió que la variable que lo controlaba nunca expiraba, porque el motor del juego no tiene una forma nativa de manejar ese tipo de tiempo. La decisión fue eliminarlo. Quedan documentados: qué era, por qué se creyó necesario, y por qué el motor lo hacía inviable. Cualquier sesión que quiera proponer algo similar tiene ese diagnóstico disponible.

Un esquema de identificadores numéricos (legible para el operador, opaco para cualquier verificación automática) se reemplazó por identificadores descriptivos en el rediseño mayor del proyecto. El código pasó a ser autoexplicativo sin necesitar una tabla de referencia aparte. La razón quedó documentada: no fue una preferencia estética.

Una convención sobre cuándo cobrar el costo de una operación (al confirmarla, no al activarla) respondió a una razón de experiencia de usuario muy concreta: si se cobra al activar, el jugador paga sin saber si la operación va a ejecutarse; si se cobra al confirmar, ya tuvo toda la información antes del costo. Esa razón, documentada, cierra la conversación la próxima vez que alguien proponga cobrar al activar.

El concepto formal que nombra esto es *Architecture Decision Records* (ADRs) — pero con una diferencia importante respecto al uso estándar: en IRAM los ADRs no estaban escritos para el operador humano. Estaban escritos para la instancia de IA que llegaría sin memoria a esa parte del proyecto. Esa diferencia de audiencia cambia cómo se escriben: la razón tiene que ser suficientemente explícita para que alguien sin contexto previo la entienda sin preguntar. Una sección de "alternativas descartadas" que solo dice *qué* se descartó, sin el *por qué*, no cumple esa función.

---

### 4D — El tiering no es opcional

A lo largo del proyecto se volvió evidente que no todas las tareas son equivalentes en términos de costo cognitivo para la IA, y que tratarlas como equivalentes genera un patrón de falla específico: la sesión empieza bien y empieza a degradarse.

El patrón tiene nombre operacional: hay tareas de diseño (alto nivel — decidir qué hacer, cómo estructurarlo, qué trade-offs aceptar) y tareas de ejecución (bajo nivel — implementar lo que ya fue diseñado, refactorizar código con instrucciones claras, aplicar reglas conocidas). Los dos tipos de tarea no se mezclan bien en la misma sesión, por una razón que conecta directamente con la sección 3: el contexto de una sesión de diseño acumula incertidumbre, alternativas abiertas y decisiones a mitad de camino — todo lo cual compite por atención cuando la misma sesión tiene que ejecutar código de precisión después.

Lo que el proyecto aprendió, documentado en la sesión 12, fue más específico que "no mezcles diseño con ejecución". Fue: el techo operacional por sesión, en modo de trabajo máximo, es aproximadamente una tarea mediana o dos tareas ligeras antes de que la calidad del output empiece a caer de forma visible. Ese techo no es una regla de estilo — es un límite empírico que apareció con suficiente consistencia para generar una regla explícita.

La consecuencia práctica es que el tiering es una decisión de planificación, no de preferencia. Si una sesión tiene que producir tanto el diseño de una función como su implementación, lo razonable no es pedirle a la IA que haga ambas cosas seguidas — es hacer la parte de diseño primero, cerrarla en una especificación escrita, y arrancar la parte de implementación desde esa especificación. El SESSION_LOG_CONSOLIDADO de la sección 4A es la misma idea: la sesión de 75 mensajes de diseño no termina con código. Termina con una especificación que la sesión de ejecución puede usar sin tener que decidir nada.

El concepto formal más cercano es la distinción entre *sistema 1* y *sistema 2* aplicada a la IA: hay outputs que salen de reconocimiento de patrones rápido y son muy confiables, y hay outputs que requieren razonamiento secuencial y son más frágiles bajo carga de contexto. Tiering es gestionar esa distinción de forma deliberada.

---

*Sección 4 — draft s25 — corrección de s24 — 2026-06-17*
EOF
Salida

exit code 0
Listo
Ahora S7. Tengo todo lo necesario en contexto — SKILL v1.0 Sec 13 y el ajuste de s17 sobre la circularidad.


Generar S7
Generar S7

generar S7
bash

cat > /mnt/user-data/outputs/IRAM_C1_s7_draft_s25.md << 'EOF'
# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 7 — Qué transfiere y qué no

*Draft s25 — 2026-06-17*

---

Antes de cerrar, conviene ser explícito sobre los límites de lo que este paper documenta. No porque los hallazgos sean frágiles — sino porque la honestidad sobre las condiciones bajo las cuales funcionaron es parte de lo que los hace útiles.

Tres condiciones estuvieron presentes en IRAM y definen el perfil de proyecto donde este sistema rinde al máximo. Su ausencia no significa que el sistema falle: significa que necesita adaptación que este documento no cubre.

---

### Las tres condiciones

**Criterio lógico preexistente.** Lo que este paper puede transferir es conocimiento sobre la herramienta: cómo estructurar el contexto, cómo diseñar el handoff entre sesiones, cómo gestionar la división de trabajo. Lo que no puede transferir es el pensamiento que construyó todo esto.

El criterio que hizo posible el proyecto — descomponer problemas en pasos verificables, buscar evidencia antes de aceptar una explicación, cuestionar una afirmación de imposibilidad desde lógica en lugar de aceptarla — no se desarrolló durante el proyecto. Se trajo de antes y se aplicó a un dominio nuevo. La sesión estratégica de mayo de 2026 lo nombró directamente: IRAM confirmó transferencia de habilidades, no aprendizaje desde cero.

Sin ese criterio previo, este sistema se puede copiar en su forma pero no en su función. Las reglas están escritas; el PROMPT_MAESTRO está documentado; el protocolo de sesión está especificado. Pero las reglas no se escriben solas — emergen de alguien que identifica un patrón, lo nombra, y decide que merece una regla. Esa capacidad no está en ningún archivo.

**Árbitro claro.** El ciclo hipótesis-prueba que aparece en la sección 4B funcionó porque había un árbitro inequívoco: el motor del juego corre o no corre, produce el comportamiento esperado o no lo produce. Cada iteración tenía un cierre sin ambigüedad.

En dominios donde la retroalimentación es lenta, subjetiva o difícil de interpretar — estrategia organizacional, investigación abierta, diseño de producto — el mismo ciclo tiene un costo radicalmente distinto. Verificar ya no es gratuito. Tratar cada "no" de la IA como hipótesis verificable sigue siendo correcto en principio, pero el costo de la verificación cambia el cálculo de cuándo vale la pena insistir.

**Problema acotado.** Alcance definible, resultado verificable, criterio de éxito observable. Eso es lo que permitió iterar rápido y saber, sin ambigüedad, cuándo algo estaba resuelto. La modularidad de v5 — cuatro mods independientes con namespace propio — no fue solo ingeniería: fue la condición que hizo posible trabajar en una parte sin romper otra. Proyectos más difusos, donde el criterio de éxito es negociable o donde las partes no son separables, no tienen ese cierre por iteración.

---

### La circularidad que no es un problema

Hay una tensión aparente en el primer punto que vale la pena resolver explícitamente, porque si no se resuelve parece circular.

Si el criterio para operar bien con IA se trae de antes, ¿qué aprendió exactamente el proyecto? ¿Y si las habilidades ya estaban, en qué sentido las entrenó?

La respuesta es que las dos cosas son simultáneamente ciertas sin contradicción. El criterio general — descomponer, verificar, cuestionar — estaba antes. Lo que el proyecto construyó fue criterio especializado: cuándo el contexto de una IA está saturado, cómo se ve un modo de falla epistémico versus uno técnico, cuánto overhead de documentación es proporcional a qué tipo de riesgo, cómo funciona el handoff entre instancias sin memoria. Ese conocimiento no existía antes del proyecto porque no había nada contra qué construirlo.

El criterio general es condición necesaria para operar bien. El criterio especializado es lo que el proyecto generó. Los dos son distintos y los dos son reales. La sesión estratégica de mayo lo vio así: el modding fue el camino hacia programación y ciencia de datos, y la IA se usó deliberadamente para saltear trabajo mecánico y de sintaxis — no para evitar el trabajo difícil. El trabajo difícil era el criterio. El dominio era el vehículo.

---

### El cuarto límite

Hay un límite adicional, más concreto que los tres anteriores: este sistema se construyó para esta herramienta específica.

La arquitectura de contexto de la sección 3 — posición como variable de diseño, formato como señal de jerarquía, separación activo/archivo — asume comportamientos particulares de este modelo. El techo operacional por sesión de la sección 4D es un límite empírico de este modelo en este tipo de tarea. No hay garantía de que ninguno de los dos transfiera sin ajuste a otro sistema.

Eso no invalida los hallazgos — invalida la posibilidad de aplicarlos directamente sin calibración. Un equipo que trabaje con otro modelo va a encontrar que algunos límites son distintos, que algunas posiciones en el contexto tienen pesos distintos, que el techo operacional cae en otro lugar. El método para encontrar esos límites es el mismo que usó IRAM: medir, variar una cosa a la vez, y dejar que el sistema sea el árbitro.

---

### El cierre

El techo de la herramienta es estructural y no se mueve: no tiene memoria entre sesiones, no sale del problema tal como se lo planteó, y le asigna menos peso a las instrucciones cuando el contexto está cargado. Gestionar ese techo — con arquitectura de contexto, con tiering, con especificaciones antes de ejecución — es el trabajo que este paper documentó.

El techo del operador se mueve con la experiencia. El criterio especializado que el proyecto generó no existía antes y existe ahora. Eso es transferible — no como receta, sino como mapa de qué preguntas hacer y qué evidencia buscar cuando las mismas situaciones aparecen en otro proyecto.

Este paper es, en el fondo, sobre cómo gestionar el primero lo suficientemente bien para que el segundo sea el único que importe.

---

*Sección 7 — draft s25 — 2026-06-17*
EOF
Salida

exit code 0
Listo