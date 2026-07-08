# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 1 — El laboratorio

*Draft s31 — correcciones finales — 2026-06-17*

---

En algún momento de abril de 2026, alguien escribió una pregunta de una línea: ¿se puede redistribuir población automáticamente en Imperator: Rome?

De esa pregunta salió un mod para un videojuego de estrategia. Pero eso no es lo que documenta este paper.

---

### El proyecto

IRAM es un mod para Imperator: Rome 2.0.4 — un juego de estrategia histórica ambientado en la antigüedad clásica. Un mod modifica el comportamiento del juego: en este caso, automatiza decisiones económicas y demográficas que el juego original deja al jugador. El mod se construyó en aproximadamente dos meses, en 441 conversaciones con IA a través de 5 cuentas de Claude, acumulando 7345 mensajes analizados. De esas conversaciones, 336 corresponden al desarrollo activo de IRAM; el resto son sesiones previas o de contexto general del mismo período.

Esos números no describen un proyecto grande en términos de software. Describen un proyecto largo en términos de trabajo con IA — lo suficientemente largo como para que aparecieran, en orden, casi todos los problemas que aparecen cuando se intenta usar IA de forma sostenida en un dominio técnico.

El mod fue el vehículo. Lo interesante no es qué hace el mod — es qué tuvo que construirse para que el mod pudiera existir.

---

### Las dos historias

Un proyecto así acumula dos historias distintas, y conviene no mezclarlas.

La primera es la historia técnica: qué se construyó, en qué versión, con qué bugs y qué soluciones. En IRAM eso es la progresión de v1 a v5 — cinco versiones con nombres, zips canónicos y decisiones de diseño documentadas. Es específica del dominio. A casi nadie le importa cómo se resolvió un bug de scope en el motor de Imperator: Rome.

La segunda es la historia de cómo el operador y la IA aprendieron a trabajar juntos. Cuándo apareció cada documento de contexto, qué problema lo generó, cómo cambió el protocolo de sesión. Esta es la historia que generaliza — y es la que está detrás de este documento.

La razón para separarlas no es estética. Cuando se mezclan en el mismo log, la IA no puede priorizar: ¿esto es contexto técnico que necesito para programar, o es una regla sobre cómo trabajamos? El patrón de la segunda historia — el que vale la pena formalizar — queda diluido entre detalles técnicos que no lo son.

Este paper documenta la segunda historia. La primera aparece solo cuando da contexto o cuando es la evidencia.

---

### Por qué sirve como caso de estudio

Tres condiciones hacen de IRAM un caso útil para analizar el trabajo con IA, más allá del dominio específico.

Primero, escala suficiente. Dos meses, cinco cuentas, 441 conversaciones. No es un experimento de laboratorio ni una sesión de prueba — es un proyecto real con presión real de entrega, límites reales de herramienta, y errores reales que costaron tiempo.

Segundo, árbitro claro. El motor del juego corre o no corre. Una función de scripting o produce el comportamiento esperado en el juego, o no lo produce. Esa retroalimentación inequívoca — sin ambigüedad, sin interpretación — acortó radicalmente el ciclo hipótesis-prueba. Sin árbitro claro, muchos de los patrones que se identificaron habrían tardado mucho más en ser visibles.

Tercero, el objetivo estaba reformulado desde adentro. En algún momento del proyecto — no al principio, sino cuando el sistema empezaba a tomar forma — se escribió esto en el propio documento de estado del mod: *"el mod exitoso es el entregable, el aprendizaje es el objetivo real."* No es una conclusión retrospectiva. Es una intención que quedó documentada mientras el trabajo ocurría, en mayo de 2026, en medio del proyecto.

Esa reformulación es el punto de partida de este paper. El mod se terminó. Lo que este documento intenta hacer es responder la pregunta que esa frase dejó abierta: ¿qué se aprendió exactamente?

---

*Sección 1 — draft s31 — correcciones finales — 2026-06-17*
