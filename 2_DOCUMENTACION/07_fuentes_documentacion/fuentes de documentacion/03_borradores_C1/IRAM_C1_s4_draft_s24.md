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
