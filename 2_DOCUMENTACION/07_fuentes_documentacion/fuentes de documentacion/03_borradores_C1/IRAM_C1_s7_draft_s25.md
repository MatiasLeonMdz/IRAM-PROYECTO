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
