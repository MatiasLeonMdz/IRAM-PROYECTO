# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 3 — El hallazgo central: la posición y el formato importan más que el contenido

*Draft s20 — 2026-06-17 16:16*

---

Hay una intuición casi universal sobre cómo mejorar los resultados de la IA: escribir mejor las instrucciones. Si la IA no hace lo que se le pide, el diagnóstico natural es que el prompt estaba mal redactado, era ambiguo, o le faltaba detalle.

IRAM mostró que ese diagnóstico falla en una clase específica de situaciones. Y que la clase es más común de lo que parece.

---

### El problema que no era de contenido

A lo largo del proyecto, ciertos errores volvían a aparecer sesión tras sesión. No eran errores nuevos — eran exactamente los mismos. Y en todos los casos, la solución ya estaba documentada. La regla que lo cubría existía, estaba bien escrita, no tenía ambigüedad. La IA simplemente no la aplicaba.

El diagnóstico inicial fue el habitual: hay que explicarlo mejor. Se reescribió la regla. No cambió nada. Se agregó más contexto. Tampoco. El problema no era el contenido de la instrucción.

Lo que importaba era dónde vivía esa instrucción dentro del contexto.

El sistema de documentación del proyecto, en sus versiones tempranas, era un único documento de respaldo que acumulaba todo: instrucciones de trabajo, historial de versiones, decisiones de diseño, código, contexto técnico del juego. Al llegar a 220KB y casi 5000 líneas, la IA no podía priorizar. Una regla correctamente escrita, enterrada en el medio de miles de líneas de código y contexto técnico, competía por atención con todo lo demás — y perdía. No porque hubiera sido "olvidada": es que, en esa posición y en ese formato, recibía menos peso que el contenido que la rodeaba.

La solución no fue reescribir nada. Fue mover la regla: extraerla del documento de respaldo y pegarla como primer mensaje de la sesión, en un bloque corto y sin ruido alrededor.

Funcionó.

---

### El efecto es medible

Esto no es una impresión subjetiva. El proyecto generó datos sobre el costo de inicializar el contexto en distintos momentos de su evolución:

| Momento del proyecto | Mecanismo de contexto | Mensajes promedio hasta trabajo productivo |
|---|---|---|
| Antes de instrucciones formales | Contexto mezclado, sin estructura | 35.0 |
| Instrucciones pegadas como primer mensaje | Documento corto al inicio | 18.4 |
| + separación estado actual / histórico | Carga estructurada en capas | 14.1 |

La caída de 35.0 a 14.1 no se explica por tareas más simples — el proyecto se estaba volviendo más complejo en esa misma dirección. Se explica por el costo de inicializar el contexto. Y ese costo depende de la arquitectura, no del contenido.

Cada paso en la tabla corresponde a un cambio estructural que se puede fechar: el día en que las instrucciones pasaron a pegarse como primer mensaje, y el día en que se separó el estado actual del historial. Los dos cambios son el mismo principio aplicado dos veces: lo que va primero pesa más. Lo que compite con ruido, pierde.

---

### Posición y formato como variables de diseño

"Economía de contexto" fue la formulación que el propio proyecto usó para nombrar esto, en un meta-análisis escrito mientras el trabajo ocurría: *"las reglas R no son desconfianza sino economía de contexto — lo documentado no se rediscute, lo no documentado es espacio de colaboración."*

La frase nombra algo más preciso que "escribir bien los prompts". Las reglas no existen para restringir — existen para asignar atención. Lo que está documentado en el lugar correcto, con el formato correcto, no necesita ser explicado de nuevo. Le libera al operador y a la IA el espacio para trabajar en lo que todavía no está resuelto.

Dos variables concretas que emergieron del proyecto:

**Posición.** Lo primero que entra en un contexto nuevo pesa más que lo mismo enterrado más adentro. Las instrucciones de trabajo iban pegadas como primer bloque de cada sesión — no adjuntas como archivo, no mezcladas con el código. Esa decisión de posición era funcional, no estética.

**Formato.** Un bloque corto de reglas numeradas sin ruido alrededor recibe más peso que la misma información diluida en prosa. No porque la prosa sea menos clara — sino porque el formato señala jerarquía. La IA no lee un documento de contexto de manera uniforme: la densidad, la estructura y la posición relativa de cada bloque modifican cuánto peso le asigna.

El corolario práctico: si una instrucción se sigue de forma inconsistente a pesar de estar clara y bien escrita, el primer diagnóstico no debería ser "hay que explicarlo mejor". Debería ser "¿dónde vive esto en el contexto, y en qué formato, y qué está compitiendo con eso por atención?".

---

### Lo que esto implica para el diseño del sistema

Este hallazgo tiene consecuencias directas sobre cómo se construyó todo lo demás.

El PROMPT_MAESTRO — el documento de instrucciones de trabajo del proyecto — no creció de forma lineal. Cada regla que contiene es el residuo de un error real: algo que pasó, se identificó como patrón, y se documentó como regla. Pero la decisión sobre *dónde* poner esa regla, y en *qué formato*, fue tan importante como la regla en sí. Reglas con consecuencias críticas si se violan van marcadas visualmente y primero. Reglas de estilo van al final. La categorización no es cosmética — es arquitectura de atención.

El mismo principio se aplica al SESSION_LOG: existe porque "la IA tiene todo el contexto técnico" y "la IA sabe qué pasó en la última sesión" son cosas distintas. El log es corto, está al final del bloque de inicio, y su único trabajo es cubrir ese hueco específico. Si fuera más largo, o estuviera en otra posición, haría lo mismo con más fricción.

La implicación más amplia: la arquitectura de un sistema de trabajo con IA no se mide solo por qué información contiene. Se mide por cómo está organizada esa información para que llegue al lugar correcto en el contexto, con el formato correcto, en el momento correcto. El contenido es necesario pero no suficiente.

---

*Sección 3 — draft s20 — 2026-06-17 16:16*
*Siguiente: Sección 1 (El laboratorio) o Sección 4 (Tres hallazgos) — confirmar con operador.*
