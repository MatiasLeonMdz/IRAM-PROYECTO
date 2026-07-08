# Desarrollo técnico sostenido con IA: lecciones de un mod de videojuego

**Tipo:** Research narrative — case study técnico
**Fuente:** Proyecto IRAM (Imperator: Roma 2.0.4), 2026-04-09 → 2026-06-10
**Versión:** 1.0 — 2026-06-12

---

## 1. Resumen ejecutivo

Durante dos meses, una persona construyó una modificación para un videojuego de estrategia histórica usando un asistente de IA como herramienta central. El proyecto acumuló 441 conversaciones, más de 7.300 mensajes y cinco cuentas de Claude operadas en rotación secuencial. El resultado técnico es verificable: cinco versiones del mod, cada una con un archivo comprimido y un documento técnico. El proceso también es verificable: el historial de conversaciones es completo, con marca de tiempo en cada mensaje individual.

El mod no es el hallazgo. El hallazgo es lo que el análisis del proceso revela: que trabajar con IA a lo largo de muchas sesiones sin memoria compartida entre ellas requiere una arquitectura específica —no mejores instrucciones, sino una relación diferente entre el estado del proyecto y el lugar donde ese estado vive. El sistema de documentación que hizo esto posible evolucionó de un único archivo de respaldo a una estructura de cuatro tipos de documentos con funciones distintas, cada uno cargado en un momento específico de cada sesión. Cada cambio estructural en ese sistema tuvo un efecto medible en la eficiencia del trabajo.

La afirmación central de este documento: la IA no democratiza la programación. Permite ejecutar pensamiento estructurado en dominios técnicos sin dominar la mecánica de esos dominios. El límite no es la herramienta —es la calidad del pensamiento que la opera. Pero la herramienta también tiene techo propio: no tiene memoria entre sesiones, no sale del problema tal como se lo planteó, y sus instrucciones pierden peso cuando el contexto es largo. Ambos techos importan. Este documento trata principalmente de cómo gestionar el primero lo suficientemente bien para que el segundo sea el único que cuente.

---

## 2. El proyecto en números

Antes de la narrativa, los datos que establecen la escala.

**El proyecto:**
- Tipo: mod para Imperator: Roma 2.0.4 (videojuego de estrategia histórica de Paradox Interactive)
- Qué hace el mod: redistribuye población entre provincias de forma automática según criterios económicos y demográficos configurables
- Período: 2026-04-09 → 2026-06-10 (62 días)
- Versiones del mod: 5 (v1 → v5.5), cada una con su archivo comprimido
- Herramienta: Claude (asistente de IA de Anthropic), cinco cuentas

**La escala del trabajo:**

| Métrica | Valor |
|---------|-------|
| Conversaciones totales (período IRAM) | 441 |
| Mensajes post-deduplicación | 7.345 |
| Cuentas de Claude | 5 |
| Días activos | 62 |
| Días con más de una cuenta activa | 43 de 49 días con actividad (87.8%) |

**Las cinco cuentas no trabajaban en paralelo.** El análisis de marca de tiempo de cada mensaje individual —no de inicio de sesión— muestra cero casos de mensajes intercalados entre dos cuentas dentro de una ventana corta. El gap típico entre cambio de cuenta era de 2 a 5 minutos. El 87.8% de los días con actividad hubo más de una cuenta activa, pero siempre en momentos distintos del día, nunca simultáneamente. La causa fue técnica: el límite de mensajes por cuenta forzaba el cambio. Lo que convirtió esa restricción en un sistema funcional fue que el estado del proyecto vivía fuera de las conversaciones, en documentos portables que cualquier cuenta podía cargar y retomar.

**La evolución de la velocidad:**

| Fase del mod | Sesiones/día | Mensajes/sesión |
|-------------|-------------|----------------|
| v1-v2 (Drago, inicio del proyecto) | 1.8 | 37.0 |
| v5 (IRAM final, última fase) | 9.4 | 9.6 |

La versión final no fue más rápida porque el problema fuera más simple —de hecho, su alcance era mayor, con cuatro módulos independientes en lugar de uno. Fue más rápida porque el sistema de trabajo se había consolidado. La velocidad de trabajo se multiplicó por 5.2, mientras el costo en mensajes por sesión cayó a poco más de un cuarto. Eso, en sí mismo, es un resultado medible de mejora de proceso.

---

## 3. Las dos historias en paralelo

Hay dos historias distintas en este proyecto, y conviene mantenerlas separadas —aunque comparten cronología y, en algunos momentos, los mismos hitos pertenecen a las dos.

La primera es la historia del mod: qué se construyó, en qué versión, con qué bugs y qué soluciones. Es específica del dominio y, por sí misma, no generaliza.

La segunda es la historia de cómo el equipo —operador e IA— aprendió a trabajar. Qué sistema de documentación emergió, cuándo apareció cada pieza, qué problema resolvió. Esta es la historia que generaliza. Es la que importa aquí.

### 3.1 La historia del mod

El proyecto empezó con una pregunta de una línea: ¿se puede redistribuir población automáticamente en este juego? No había plan más allá de eso.

**v1 — Drago stable** (2026-04-09 → 04-21): Una función simple. Un colono nacía en la capital y migraba a otra provincia. El parámetro de guerra estaba desactivado por defecto. Funcionaba.

**v2 — Drago alt** (solapado con v1): Una variante. El colono nacía en una provincia rival, la migración era opcional y configurable. Dos cambios, no uno —distinción que importaría para la historia técnica posterior.

**v3 — IRAM** (2026-04-22 → 05-21): El salto arquitectónico mayor del proyecto. El mod cambió de nombre y de categoría (de `character modifier` a `province modifier`). El archivo central de lógica pasó de 199 líneas a 896 —un factor 4.5x. La lógica que disparaba los efectos del mod se reescribió por completo para operar sobre provincias en lugar de personajes.

**v4 — IRAM expansión** (2026-05-22 → 06-03): El período más ambicioso. Se incorporó un modelo económico (costos configurables, cobro al confirmar en lugar de al activar), demografía diferenciada por tipo de población, y un sistema de construcción. Esta versión fue también la que concentró la mayor cantidad de deuda técnica: el alcance creció sin que la arquitectura del código acompañara el crecimiento.

**v5 — IRAM final** (2026-06-04 → 06-10): El rediseño deliberado. Los cuatro sistemas del mod se separaron en módulos independientes con un espacio de nombres unificado (`iram_`). El resultado fue más mantenible, más verificable, y con menos interdependencias implícitas. V1 a V4 fueron prototipado. V5 fue ingeniería. El verdadero IRAM 1.0 es V5.

### 3.2 La historia del sistema de documentación

Mientras el mod evolucionaba, otra historia ocurría en paralelo. Esta es la que importa para quien lea esto sin ningún interés en modificar videojuegos.

**Sin sistema (hasta 2026-04-16):** Las primeras sesiones no tenían ninguna estructura de contexto. Cada sesión nueva comenzaba desde cero: había que re-explicar qué era el proyecto, qué se había hecho, en qué estado estaba el código. Los problemas eran predecibles: los mismos errores volvían a aparecer entre sesiones, porque las reglas para evitarlos vivían solo en el historial de conversaciones anteriores, al que la sesión nueva no tenía acceso.

**El primer backup propio (2026-04-17):** Un único archivo de referencia que condensaba el estado técnico actual. El problema que resolvió fue concreto: ya no había que re-explicar la estructura del mod en cada sesión. El problema que creó fue diferido: el archivo creció sin límite. Acumuló todo —instrucciones de trabajo, historial de versiones, decisiones de diseño, contexto técnico activo— hasta llegar a 220KB. A ese tamaño, la IA dejó de poder priorizar: reglas documentadas quedaban sepultadas bajo contenido técnico, y los mismos errores volvían a aparecer aunque la solución ya estuviera escrita en el mismo documento.

**PROMPT_MAESTRO v1.0 (2026-05-16):** La solución al problema de prioridad no fue reescribir el documento grande. Fue crear un documento corto —solo las instrucciones de trabajo— y pegarlo como *primer mensaje* de cada sesión nueva, no adjuntarlo como archivo. La distinción es técnica pero no es un detalle cosmético: lo que entra primero en el contexto de una sesión recibe más peso que lo mismo enterrado más adentro. El efecto fue inmediato y medible.

**ACTIVE/ARCHIVE split (2026-05-27):** El documento de referencia técnica se separó en dos: el estado vigente (lo que la IA necesita hoy para trabajar) y el histórico (versiones anteriores, decisiones descartadas, contexto que ya no es operativo). El histórico se consulta si hace falta, pero no se carga por defecto. Ese mismo día se inició un sistema de control de versiones que complementó el sistema de archivos comprimidos ya existente.

**El registro de sesión:** Una quinta pieza que surgió para cubrir un hueco específico: hay una diferencia entre "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó ayer". El registro de sesión —qué se hizo en la última sesión, qué quedó abierto, cuál es el próximo paso— cubre ese hueco. Con el tiempo, para reworks complejos con muchas tareas interdependientes, evolucionó de registro a especificación ejecutable: suficiente detalle para que una nueva sesión pudiera ejecutar sin tener que decidir.

**El paralelo entre las dos historias:** La documentación no evolucionó por calendario —evolucionó cuando el costo de seguir sin estructura superó, de forma visible, al costo de pararse a estructurar. El primer backup nació de la frustración de re-explicar lo mismo. El PROMPT_MAESTRO nació de ver los mismos errores reaparecer en presencia de reglas documentadas. El ACTIVE/ARCHIVE split nació de un documento tan grande que había dejado de servir. Cada pieza respondió a un problema real, y el momento en que apareció lo confirma.

---

## 4. Los hallazgos con evidencia

Cuatro hallazgos, cada uno con la evidencia que lo respalda.

### Hallazgo 1: la posición de las instrucciones importa más que su contenido

El hallazgo más contraintuitivo del proyecto —y, probablemente, el más transferible— es que una instrucción puede estar documentada, clara y sin ambigüedad, y la IA la seguirá igual de mal que si no existiera. No porque sea mala la instrucción. Sino porque está en el lugar equivocado del contexto.

Un error de scripting (usar una referencia inválida desde un alcance incorrecto) estaba documentado en el backup desde versiones tempranas. Siguió apareciendo en código nuevo, sesión tras sesión, hasta que las instrucciones que lo prohibían se extrajeron del documento grande y se pusieron al principio de cada sesión. El error desapareció. El contenido de la instrucción no cambió. Su posición en el contexto, sí.

El efecto es medible en tres puntos de corte:

| Período | Mecanismo de contexto | Mensajes promedio por sesión |
|---------|----------------------|------------------------------|
| P1 — Backup simple | Contexto mezclado, sin estructura | 35.0 |
| P3 — PROMPT_MAESTRO pegado al inicio | Instrucciones cortas como primer mensaje | 18.4 |
| P4 — ACTIVE/ARCHIVE | Carga estructurada: vigente + histórico separados | 14.1 |

La caída de 35.0 a 18.4 mensajes promedio no se explica por tareas más simples. El trabajo era el mismo. Se explica por el costo de inicializar el contexto: sin instrucciones claras al inicio, los primeros mensajes de cada sesión se consumen en reorientar a la IA. Con instrucciones al inicio, ese costo casi desaparece. La caída adicional, de 18.4 a 14.1, viene de separar el estado vigente del histórico: el contenido de versiones anteriores —código descartado, decisiones que ya no aplican— dejó de ocupar espacio y atención en cada sesión nueva.

**Principio general:** si una instrucción se sigue de forma inconsistente a pesar de estar clara y bien escrita, el diagnóstico por defecto no debería ser "hay que explicarlo mejor". Debería ser: ¿dónde vive esto en el contexto, y qué está compitiendo con eso por atención?

### Hallazgo 2: el sistema multi-cuenta era rotación secuencial, no paralelismo

Durante parte del proyecto operó una afirmación sin cuestionarse: que las cinco cuentas trabajaban en paralelo, como workers distribuidos en un sistema concurrente. La afirmación era plausible —en el 87.8% de los días con actividad había más de una cuenta activa.

No sobrevivió al pasar de "sesiones por cuenta por mes" a "marca de tiempo de cada mensaje individual". El análisis de 7.313 mensajes con timestamp encontró cero casos de mensajes a dos cuentas distintas intercalados dentro de una ventana corta. El gap típico entre cambio de cuenta era de 2 a 5 minutos. El día más intenso del proyecto —15 cambios de cuenta— la secuencia fue completamente serial: una cuenta terminaba, otra empezaba, sin superposición. Los datos corregían la afirmación, no la confirmaban.

La causa del sistema multi-cuenta fue técnica: el límite de mensajes por cuenta forzaba el cambio. Lo que convirtió esa restricción en un sistema funcional fue que el estado del proyecto vivía fuera de las conversaciones. Cualquier cuenta, al cargar los mismos documentos de instrucciones y estado actual, podía retomar el trabajo desde donde otra lo había dejado. Las cuentas eran intercambiables porque las instrucciones eran portables.

Este hallazgo es, además, una instancia del patrón del Hallazgo 3: una afirmación sostenida con confianza desde una métrica indirecta, cuestionada, y revisada al medir contra algo más granular. El árbitro no fue la intuición —fue el dato.

**Principio general:** si una herramienta tiene límites de uso —por conversación, por cuenta, los que sean— la respuesta no es coordinar sesiones en paralelo. Es hacer que cada sesión sea descartable, con el estado del proyecto en un documento portable que cualquier sesión nueva puede cargar.

### Hallazgo 3: el rol de arquitecto del operador no se delegó con el tiempo —se articuló más explícitamente

Hay una descripción precisa de la división de trabajo en este proyecto: el operador fue el arquitecto, la IA fue una herramienta de precisión con capacidad de lenguaje. Las decisiones de arquitectura (qué estructura usar, qué convención adoptar) y los criterios de diseño (costos, experiencia de uso, qué documentar) los originó el operador. La implementación dado ese diseño, y el reconocimiento de patrones de error a través de muchas sesiones, los hizo la IA de forma consistente.

Hay un modo de falla específico de la IA que vale la pena conocer de antemano, porque aparece con la misma confianza tanto cuando tiene razón como cuando no: confunde "esto no está documentado en mi conocimiento" con "esto no es posible". Dos casos del proyecto ilustran el patrón exacto.

Primero, sobre un elemento de interfaz: la IA afirmó que cierto panel del juego no admitía un tipo de elemento, que agregar lo que se pedía era imposible. El operador cuestionó la afirmación. La IA investigó los archivos reales del juego —no su conocimiento general sobre el motor— y encontró que el elemento sí existía para un alcance distinto. La restricción real era más estrecha que "es imposible", y solo la investigación contra el archivo real la reveló.

Segundo, sobre operaciones a nivel de todo el mapa: la IA afirmó que iterar sobre miles de elementos del mapa en cada pulso mensual no era viable por rendimiento. El operador insistió en que, si esa estructura existía en el motor, debía haber alguna forma de filtrar. La solución fue iterar solo sobre los elementos con una marca específica activa —un mecanismo que desbloqueó todas las operaciones globales del mod.

En ambos casos, lo que decidió no fue la IA ni el operador. Fue probar contra el sistema real. El árbitro nunca fue la IA.

**El respaldo cuantitativo:** en la fase final (v5), los mensajes del operador son los más largos del proyecto —183 caracteres en promedio, frente a 105–141 en fases anteriores— y los más ricos en lenguaje de decisión y diseño (7.0% de mensajes con vocabulario de propuesta, criterio o estructura, frente a 4.5–5.9% en fases previas). Las respuestas de Claude también: 66.5% de mensajes de Claude con lenguaje de propuesta y estructura, frente a aproximadamente 50% en fases anteriores. El rol de arquitecto del operador no se delegó con la experiencia —se articuló más explícitamente.

### Hallazgo 4: la Investigación antes de actuar no fue fricción —fue maduración del proceso

Este es el hallazgo más contraintuitivo del análisis cuantitativo. La primera lectura de los datos lleva a una conclusión incorrecta. La segunda lectura, con más desagregación, lleva a una conclusión que los datos anteriores refuerzan.

El análisis de las herramientas usadas en cada conversación permite clasificar las interacciones en tres tipos: **Código** (crear o modificar archivos del mod), **Investigación** (leer archivos, ejecutar búsquedas antes de actuar), y **Build** (operaciones de empaquetado y entrega). El ratio entre Investigación y Código —cuánta lectura hay por cada unidad de escritura— crece de forma monótona a lo largo del proyecto:

| Fase | Ratio Investigación/Código |
|------|---------------------------|
| v1-v2 | 1.8x |
| v3 | 2.0x |
| v4 | 2.4x |
| v5 | 2.9x |

Primera lectura: ¿más debugging a medida que el proyecto madura? La evidencia la refuta directamente. El porcentaje de Investigación orientada a archivos de error (`error.log`, logs de crash) se mantiene en 1–3% en **todas** las fases, sin ninguna tendencia creciente. Si el ratio creciente reflejara más debugging reactivo, ese porcentaje debería crecer. No lo hace.

Lo que sí crece es distinto: en la fase v5, el 32% de las búsquedas apuntan a documentos de planificación propios —wikis, registros de sesión, planes de ejecución— antes de tocar código, frente a un 3% en v1-v2. Los nombres de las conversaciones con mayor Investigación en v5 son "audit 5.2", "Confirmación de cambios en archivos IRAM", "Plan de ejecución unificado v5.0". No hay conversaciones del estilo "Fix bug X" entre las de mayor Investigación.

La Investigación en v5 fue lectura-antes-de-escribir, no debugging-después-de-fallar. El operador llegaba a cada sesión con instrucciones más articuladas (183 chars vs. 105–141 en fases anteriores), y la IA respondía con más lenguaje de propuesta y estructura (66.5% de mensajes de Claude con vocabulario de decisión, frente a ~50% en fases anteriores). El proceso no se volvió más lento —se volvió más deliberado.

---

La suma de estos cuatro hallazgos apunta a la misma conclusión, enunciada explícitamente durante el proyecto y confirmada por los datos desde distintos ángulos:

> La IA no democratiza la programación. Permite ejecutar pensamiento estructurado en dominios técnicos sin dominar la mecánica de esos dominios. El límite no es la herramienta —es la calidad del pensamiento que la opera. Pero la herramienta también tiene techo propio.

---

## 5. Qué transfiere y qué no

Este documento no sería honesto si terminara sin declarar sus límites.

**Una nota sobre ciclo de vida de las prácticas.** No todas las que emergieron en el proyecto tienen el mismo alcance de aplicación. Las capas de contexto (documento de instrucciones + estado actual + histórico + registro de sesión), el protocolo de arranque y cierre, y la cadena bug→patrón→regla son permanentes: aplican en cualquier sesión, en cualquier momento del proyecto. Otras son situacionales: los registros intermedios por tarea y las entregas parciales después de cada tarea completada nacieron para un rework con más de diez tareas interdependientes, cuando el costo de perder trabajo por un corte de sesión era alto. Activarlas por defecto es overhead innecesario. Activarlas cuando ese riesgo específico está presente es lo que las hace útiles. Copiar las prácticas sin copiar la condición de activación es la forma más común de importar overhead sin importar el beneficio.

Tres condiciones, presentes en este proyecto, definen el perfil donde el sistema rinde al máximo. Su ausencia no significa que el sistema falle —significa que necesita adaptación que este documento no cubre.

### Condición 1: un criterio lógico preexistente

Lo que este documento puede transferir es conocimiento sobre la herramienta: cómo estructurar el contexto, cuándo cargar qué, cómo generar reglas desde errores, cómo rotar entre sesiones sin perder estado. Lo que no puede transferir es el pensamiento que construyó todo esto.

El operador llegó al proyecto con capacidad de descomponer problemas, buscar evidencia antes de aceptar una explicación, y cuestionar afirmaciones de la IA cuando no pasaban el test de coherencia lógica. Esas habilidades no se desarrollaron durante el proyecto —se aplicaron a un dominio nuevo. El ciclo de hipótesis-y-prueba funcionó porque había alguien capaz de formular hipótesis antes de probar. Sin ese criterio previo, el sistema se puede copiar, pero no se puede operar con el mismo resultado.

### Condición 2: un árbitro claro

El árbitro de este proyecto fue el motor del juego: corre o no corre, hace lo que se espera o no lo hace. Esa claridad hizo que cada iteración tuviera un cierre inequívoco. Se podía probar una hipótesis y saber, en segundos, si era correcta.

En dominios donde la retroalimentación es lenta, ambigua o subjetiva —estrategia organizacional, investigación abierta, diseño sin criterio de éxito observable— el mismo ciclo tiene un costo radicalmente distinto, porque no hay un cierre tan claro para cada iteración. El sistema funciona, pero el presupuesto de tiempo y atención de cada hipótesis es mayor.

### Condición 3: un problema acotado

Alcance definible, resultado verificable, criterio de éxito observable. En IRAM, eso significaba: el mod tiene una función específica, y cualquier versión nueva o la cumple o no la cumple. Sin ambigüedad sobre cuándo algo estaba terminado.

Proyectos más difusos —sin un criterio claro de cuándo algo está "resuelto"— tienen un cálculo distinto sobre cuánto vale la pena formalizar y cuándo. El sistema de capas descripto en la sección 3 asume que hay algo definido que mantener en estado actual. Si el propio alcance del proyecto es una variable, el sistema necesita adaptaciones no cubiertas aquí.

### Un cuarto límite, más concreto

Este sistema fue construido para esta herramienta específica. La arquitectura de contexto, la forma de las instrucciones, el protocolo de carga —todo asume el comportamiento particular de Claude. No hay garantía de que se transfiera sin cambios a otra herramienta de IA. Las partes que sí transfieren son las más abstractas: el principio de separar lo que la IA necesita ahora del historial, el hábito de documentar la razón junto con la decisión, la lógica de hacer el estado del proyecto portable e independiente del historial de conversación específico.

### Cierre

Los hallazgos de este documento son reales y están documentados. Pero dependen de condiciones que también son reales y están documentadas. El valor de declarar ambas cosas explícitamente no es modestia —es precisión. Un sistema de trabajo copiado sin sus condiciones de operación no produce los mismos resultados. Verificar cuántas de las tres condiciones aplican al caso específico es el paso cero antes de adoptar cualquier práctica de este documento.

La herramienta tiene su propio techo —no tiene memoria entre sesiones, no sale del problema tal como se lo planteó, y le da menos peso a las instrucciones cuando el contexto es largo. Ese techo es estructural y no se mueve. El techo del operador se mueve con la experiencia. Todo el sistema descripto aquí es, en el fondo, una respuesta a la pregunta de cómo gestionar el primero lo suficientemente bien para que el segundo sea el único que importe.

---

*IRAM — Metodología de desarrollo con IA — Research narrative v1.0*
*Construido desde: IRAM_SKILL_desarrollo_con_IA_v1_0.md + IRAM_analisis_cuantitativo_2026-06-12_v3.md*
*2026-06-12*
