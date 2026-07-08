# IRAM: Desarrollo de software con IA sin dominar programación
## Un estudio de caso sobre los límites reales del desarrollador asistido por IA

*2026-06-12 · Versión 1.0*

---

## Resumen ejecutivo

IRAM es una modificación (mod) para *Imperator: Roma 2.0.4*, un videojuego de estrategia histórica ambientado en la Roma antigua. Lo construyó una sola persona sin experiencia previa en programación, usando exclusivamente Claude —un asistente de inteligencia artificial— como herramienta de desarrollo. El proyecto duró aproximadamente dos meses, generó 441 conversaciones y 7.345 mensajes, e involucró cinco cuentas de Claude en rotación. El resultado es un mod funcional de cinco versiones que agrega al juego sistemas económicos, demográficos y de construcción.

La tesis convencional sobre IA y programación sostiene que la IA democratiza el acceso al desarrollo: cualquiera puede construir software sin saber programar. Este proyecto pone esa tesis a prueba con datos reales y documentación sistemática de cada decisión.

Lo que se encontró no confirma la tesis. La IA no democratiza la programación. Lo que hace es permitir que alguien ejecute pensamiento estructurado en un dominio técnico sin dominar la mecánica de ese dominio. El límite no está en la herramienta: está en la calidad del pensamiento del operador. Pero la herramienta también tiene un techo propio que no se puede ignorar.

El hallazgo no es optimista ni pesimista. Es condicional: el sistema funciona bajo tres condiciones específicas. Sin esas tres condiciones, colapsa de formas predecibles. Este documento identifica esas condiciones, las ilustra con evidencia cuantitativa del proyecto, y señala con honestidad qué puede y qué no puede replicarse en otros contextos.

---

## 1. El proyecto en números

### Qué es IRAM

Imperator: Roma es un videojuego de estrategia histórica que permite a los jugadores controlar civilizaciones del período helenístico. El juego incluye un motor de scripting que permite a usuarios externos modificar sus mecánicas: crear nuevas unidades, eventos, dinámicas económicas o personajes. Estas modificaciones se llaman mods. IRAM es uno de ellos.

El mod agrega al juego un conjunto de mecánicas que no existen en la versión base: un sistema de spawn de personajes históricos con comportamiento condicionado, un modelo económico extendido, un sistema demográfico y un módulo de construcción. Nada de esto requirió modificar el código fuente del juego —el motor de scripting lo permite desde afuera— pero sí requirió escribir miles de líneas de código en el lenguaje interno del juego, un lenguaje que el operador no dominaba.

### La escala del proyecto

| Métrica | Valor |
|---------|-------|
| Conversaciones totales | 441 |
| Mensajes totales (post-deduplicación) | 7.345 |
| Duración | ~2 meses (abril–junio 2026) |
| Cuentas de Claude utilizadas | 5 |
| Versiones del mod | v1 → v5.5 |
| Tamaño del historial procesado | 3,6 MB |

El desarrollo comenzó el 9 de abril de 2026. Las conversaciones anteriores a esa fecha son pre-IRAM: exploraciones del lenguaje del juego sin un proyecto definido.

### Por qué cinco cuentas

Claude tiene un límite de mensajes por cuenta dentro de un período determinado. Cuando ese límite se agota, la cuenta queda temporalmente bloqueada. La solución del operador fue usar cinco cuentas en rotación secuencial: una activa a la vez, con transiciones frecuentes de dos a cinco minutos entre una y otra.

Este sistema no era paralelismo —no había trabajo simultáneo real en múltiples cuentas. Era rotación forzada por el límite, manejada como infraestructura. De los días activos del proyecto, el 87,8% tuvo múltiples cuentas usadas en distintos momentos del día. En 7.313 mensajes analizados con timestamps individuales, no se encontró ningún caso de interleaving real (secuencia A-B-A en menos de cinco minutos): las cuentas operaban estrictamente en secuencia.

El problema central que generó este sistema de rotación no era técnico sino de coherencia: ¿cómo lograr que la cuenta que toma el trabajo sepa exactamente qué hizo la cuenta anterior? La solución a ese problema es la historia más importante de este proyecto.

### Un dato que anticipa todo

Cuando el sistema alcanzó su madurez, los mensajes del operador se volvieron más largos, no más cortos. En la última versión del mod (v5), los mensajes del operador eran los más extensos del proyecto —183 caracteres en promedio— y los más densos en lenguaje de decisión: 7,0% de las palabras correspondían a verbos y frases de decisión explícita. La hipótesis de que el operador "se volvió más dependiente de la IA" es falsa. La dependencia no creció: creció la articulación.

---

## 2. Las dos historias en paralelo

El proyecto tiene dos narrativas simultáneas que no deben mezclarse: la historia del mod técnico y la historia del sistema de documentación. Son distintas, pero cada hito de una tiene un correlato en la otra.

---

### Historia 1: El mod técnico (v1 → v5)

**v1 — Drago stable (abril 2026)**
El mod en su forma más básica: un personaje llamado Drago aparecía en la capital del jugador al inicio de la partida. La mecánica era simple —spawn condicional, sin guerra. Prueba de concepto más que producto.

**v2 — Drago alt**
Primera bifurcación de diseño: el spawn se trasladó al territorio del rival, y la guerra pasó a ser opcional. No era un avance técnico mayor —era la primera decisión de diseño real, tomada deliberadamente.

**v3 — IRAM (mayo 2026)**
El punto de quiebre. Tres cambios simultáneos: rename del proyecto (de Drago a IRAM), primera auditoría formal de código (llamada Optimize), y unificación técnica de las mecánicas existentes.

El dato que mide este salto: el archivo `on_action`, que contiene los disparadores de eventos del mod, pasó de 199 líneas en v2 a 896 líneas en v3. Un aumento de 4,5 veces. El proyecto dejó de ser un experimento.

**v4.0 → v4.3.16 (mayo 2026)**
Período de expansión rápida: modelo económico extendido, sistema demográfico, módulo de constructor. La última versión de v4 —v4.3.16— se cerró el 30 de mayo de 2026 a las 03:14. Era el techo del enfoque monolítico: un solo archivo de mod que crecía con cada adición.

**v5.0 → v5.5 (junio 2026)**
El rediseño arquitectónico. En lugar de un mod monolítico, v5 separó las funcionalidades en cuatro módulos independientes con namespace propio (`iram_`). El namespace eliminó conflictos entre sistemas y permitió desarrollar cada módulo de forma aislada.

La distinción clave: v1 a v4 fue prototipado. v5 fue ingeniería deliberada. El verdadero IRAM 1.0 es v5.

---

### Historia 2: El sistema de documentación

**Sin backup (inicio)**
Las primeras sesiones no tenían ningún mecanismo de persistencia. Cada nueva conversación empezaba desde cero: el operador reexplicaba el proyecto, redescubría las mismas decisiones, cometía los mismos errores.

**El primer backup (2026-04-17)**
Cuatro días después del inicio del proyecto, apareció el primer documento de contexto: `exodus_backup_tecnico_v5.md`, creado en la segunda cuenta (CLAUDE_2). No fue un plan —fue una reacción. Algo se perdió; el backup nació para que no se volviera a perder.

Este patrón —la regla surge del error, no del diseño— se repetiría a lo largo de todo el proyecto.

**El PROMPT_MAESTRO (2026-05-16)**
Un mes después, en la conversación 45 de la primera cuenta (CLAUDE_1), el operador formalizó algo que había estado haciendo de forma ad hoc: un bloque de instrucciones permanentes que cualquier cuenta podía cargar al inicio de una sesión para retomar el trabajo sin rework.

*Antes*: cada nueva cuenta —o cada nueva sesión— requería reexplicar el proyecto, sus decisiones, su estado actual.
*Generaba*: rework en cada transición. El tiempo de arranque era proporcional al tiempo desde la última sesión documentada.
*Por eso*: un documento canónico, permanente, que respondía las preguntas que Claude inevitablemente hacía al inicio: qué es el proyecto, cuáles son las reglas, cuál es el estado.
*Resultado*: las 441 conversaciones de cinco cuentas distintas se comportaron, desde ese punto, como si fueran una sola.

**El SESSION_LOG (2026-05-23 — 2026-05-25)**
El concepto nació el 23 de mayo: un documento de estado de cierre que registra qué se hizo, qué falta, cuál es el próximo paso. El primer archivo apareció el 25. Se formalizó como práctica el 26.

La diferencia con el backup era de audiencia: el backup le hablaba a Claude sobre el proyecto. El SESSION_LOG le hablaba a la próxima sesión sobre qué hacer.

**El split ACTIVE / ARCHIVE (2026-05-27, 20:28)**
El documento de contexto había crecido hasta el punto en que el peso del historial consumía tokens que el proyecto necesitaba para trabajo activo.

*Antes*: un solo documento de contexto que acumulaba todo.
*Generaba*: al acercarse al límite del contexto, el documento era demasiado pesado. Las secciones obsoletas competían con las activas por espacio en la ventana.
*Por eso*: dos documentos. Uno activo —lo que cambia con cada sesión. Uno archivado —lo que ya no cambia. Las secciones en ARCHIVE se consultan solo si se necesitan; nunca se cargan por defecto.
*Resultado*: el sistema de tres capas completo: instrucciones permanentes (PROMPT_MAESTRO) + contexto activo (WIKI ACTIVE) + estado volátil (SESSION_LOG).

**La maduración del SESSION_LOG (v5)**
En las fases finales del proyecto, el SESSION_LOG dejó de ser un registro de lo que había pasado y se convirtió en una especificación de lo que debía pasar. El operador lo usaba para dictar el orden y los criterios de cada sesión antes de que Claude empezara. El documento de cierre era, al mismo tiempo, el documento de apertura de la siguiente sesión.

---

### El correlato entre las dos historias

Cada hito del sistema de documentación tuvo una causa en el mod técnico:
- La primera pérdida de contexto ocurrió durante el desarrollo de v3, cuando el proyecto se volvió suficientemente complejo para que una sesión no fuera suficiente.
- El PROMPT_MAESTRO se formalizó justo antes del período más intenso de v4, cuando las transiciones de cuenta se volvieron más frecuentes.
- El split ACTIVE/ARCHIVE coincidió con el cierre de v4.3.16 y el rediseño hacia v5: el momento en que la arquitectura del mod cambió también fue el momento en que la arquitectura de la documentación cambió.

---

## 3. Los hallazgos con evidencia

### Hallazgo 1: El operador fue el arquitecto — con respaldo cuantitativo

La narrativa convencional del desarrollo asistido por IA coloca al usuario en el rol de "quien pide" y a la IA en el rol de "quien decide técnicamente". Los datos de este proyecto contradicen esa narrativa.

En v5, los mensajes del operador fueron los más largos del proyecto (183 caracteres en promedio) y los más densos en lenguaje de decisión (7,0%). No hubo ninguna fase anterior donde ambas métricas fueran más altas simultáneamente.

Esto tiene una interpretación directa: el rol de arquitecto no se transfirió a Claude con el tiempo. Se articuló más explícitamente. Mientras el sistema se volvía más complejo, el operador se volvía más preciso en sus instrucciones —no más delegante.

### Hallazgo 2: El ratio Investigación / Código creciente no es fricción — es planificación

En v4, la proporción entre mensajes de Investigación (exploración, análisis, auditoría) y mensajes de Código (implementación directa) era de 1,8x. En v5, esa proporción creció a 2,9x.

La lectura intuitiva de ese dato sería: "más investigación significa más problemas, más debugging, más fricción en v5."

Los datos desmienten esa lectura. La tasa de errores directos (mensajes clasificados con target `error`) estuvo plana en aproximadamente 2% en todas las fases del proyecto —incluyendo v5. El debugging no aumentó.

Lo que sí aumentó fue el peso de la planificación deliberada: en v4, las conversaciones con target `doc_plan` representaban el 3% del total de investigación. En v5, representaban el 32%. Las conversaciones de investigación más extensas de v5 no eran "Fix bug X" sino auditorías de calidad: "audit", "Confirmación de estructura", "Plan de ejecución unificado".

La conclusión: la madurez del sistema se manifestó como más planificación antes de actuar, no como más reparación después. El ratio Inv/Cód creciente es una señal de ingeniería deliberada, no de fricción acumulada.

### Hallazgo 3: La arquitectura de contexto supera al contenido del prompt

Durante el proyecto se cortaron varias sesiones antes de completar su trabajo. En cada caso, el sistema de tres capas fue suficiente para recuperar el estado completo y retomar sin rework.

La prueba no es anecdótica: el contenido de ningún documento individual era suficiente por sí solo. Lo que fue suficiente fue la estructura: PROMPT_MAESTRO (qué es el proyecto y cómo trabajar) + WIKI ACTIVE (cuál es el estado técnico actual) + SESSION_LOG (qué se hizo y qué sigue). Tres documentos con audiencias distintas, actualizados en distintos momentos, por razones distintas.

La implicación es contraintuitiva: optimizar el contenido de los prompts sin resolver la arquitectura de contexto es optimizar el ingrediente equivocado. Un prompt perfecto en una sesión sin SESSION_LOG actualizado produce más rework que un prompt imperfecto con SESSION_LOG preciso.

### Hallazgo 4: Claude tiene modos de falla específicos y predecibles

Se documentaron dos instancias concretas de falla de Claude con impacto en el proyecto:

**Caso 1 — scripted_gui**: Claude afirmó que una funcionalidad era imposible de implementar con el motor de scripting del juego. La funcionalidad era posible. No estaba en la documentación que Claude había indexado. El patrón: Claude confunde "no documentado" con "no posible". La fuente del error no es aleatoria —es estructural.

**Caso 2 — scopes globales**: Claude dio una respuesta incorrecta sobre el alcance de variables en el lenguaje del juego. La respuesta era plausible, técnicamente coherente, y errónea. El operador detectó el error porque sabía qué resultado esperaba del juego —no porque supiera que Claude había fallado.

El patrón de ambos casos es el mismo: el operador necesita saber suficiente para reconocer cuando Claude falla. No para implementar —para detectar. Sin ese mínimo de criterio, los errores de Claude pasan como válidos.

---

### Principio central

Estos cuatro hallazgos convergen en un punto:

> *La IA no democratiza la programación. Permite ejecutar pensamiento estructurado en dominios técnicos sin dominar la mecánica de esos dominios. El límite no es la herramienta: es la calidad del pensamiento que la opera. Pero la herramienta también tiene techo propio.*

Los dos techos son distintos. El techo del operador (calidad del pensamiento) puede mejorar con experiencia. El techo de la herramienta (capacidad estructural de Claude para manejar cierta complejidad en una sesión) es, por ahora, inamovible. La arquitectura de v5 —cuatro módulos separados en lugar de un monolito— fue en parte una respuesta a ese techo: si Claude no puede manejar todo en una sesión, se divide el problema para que nunca tenga que hacerlo.

---

## 4. Qué transfiere y qué no

### Las tres condiciones de no-transferibilidad

El sistema funcionó porque el operador llegó al proyecto con tres condiciones que no son universales:

**1. Criterio preexistente**
El operador sabía qué hacía un buen mod para este juego antes de empezar. No era criterio técnico —no sabía programar el motor de scripting. Era criterio de dominio: sabía cómo debería comportarse el juego, qué mecánicas tenían sentido, cuándo una implementación era incorrecta aunque compilara.

Sin ese criterio, el sistema colapsa en el Hallazgo 4: los errores de Claude pasan sin detección. La IA produce output técnicamente coherente pero funcionalmente incorrecto, y nadie puede distinguirlo.

**2. Árbitro claro**
El veredicto era binario e inmediato: el juego funcionaba o no funcionaba. No había criterio subjetivo, no había usuarios que pudieran reportar problemas de forma diferida, no había ambigüedad sobre si algo estaba correcto.

En proyectos donde el criterio de éxito es subjetivo o diferido —una interfaz de usuario, un análisis de datos, un informe— el árbitro no es claro. El sistema de validación de este proyecto no se puede trasladar directamente a esos contextos.

**3. Problema contenido**
IRAM era un proyecto cerrado: sin equipo, sin usuarios externos, sin dependencias de producción, sin presión de entrega. El operador tuvo libertad total para rediseñar la arquitectura completa entre v4 y v5 sin ninguna consecuencia externa.

En proyectos con equipos, con código en producción, o con plazos fijos, el costo de ese tipo de rediseño es distinto.

---

### Qué sí transfiere

Los patrones transfieren. Los documentos específicos no.

**La estructura de tres capas** (permanente / activo / volátil): cualquier proyecto multi-sesión con IA puede implementar esta separación. Los nombres —PROMPT_MAESTRO, WIKI ACTIVE, SESSION_LOG— son específicos de este proyecto. La distinción entre lo que no cambia, lo que cambia lentamente, y lo que cambia en cada sesión es generalizable a cualquier contexto.

**El mecanismo de aprendizaje** (bug → patrón → regla): cada error que se repite indica una regla que falta. El proceso de convertir errores recurrentes en restricciones explícitas en el documento de instrucciones permanentes es independiente del proyecto. Funciona en cualquier dominio donde el error tenga causa identificable.

**El SESSION_LOG como especificación ejecutable**: el documento de cierre de cada sesión no es un diario —es el input de la próxima sesión. Esta diferencia de propósito cambia cómo se escribe el documento: no se registra lo que pasó para recordarlo, se especifica lo que sigue para que la próxima sesión no tenga que inferirlo.

**Saber qué no delegar a la IA**: los Hallazgos 3 y 4 tienen una implicación práctica directa. La arquitectura de contexto es trabajo del operador. La detección de fallas de Claude es trabajo del operador. Delegar esas dos responsabilidades a Claude es el error más costoso del proceso, porque sus consecuencias se acumulan silenciosamente.

---

### Los límites honestos

Este estudio de caso termina con honestidad, no con optimismo.

**El techo de la herramienta no desapareció**. Hacia mediados del proyecto, la complejidad del mod superó lo que Claude podía manejar en una sesión sin perder coherencia. La solución no fue prompting más sofisticado —fue arquitectura modular. El techo no desapareció: se desplazó hacia la derecha al dividir el problema. En algún punto, la complejidad de cada módulo también llegará a ese techo.

**El sistema de documentación fue tan laborioso como el mod**. Las 441 conversaciones incluyen trabajo técnico en el mod y trabajo de gestión del contexto. El PROMPT_MAESTRO, el SESSION_LOG, el split ACTIVE/ARCHIVE —ninguno de esos artefactos se creó solo. Quien replique este enfoque debe contar ese costo en su estimación del proyecto.

**Los errores no detectados no están en los datos**. Los Casos 1 y 2 del Hallazgo 4 fueron detectados y documentados. Cuántos errores de Claude pasaron sin detección —especialmente en las fases rápidas de v4, donde el operador priorizaba velocidad— no se puede saber con certeza. El historial registra lo que se resolvió, no lo que se dejó pasar.

---

La pregunta útil no es "¿puedo construir software con IA sin saber programar?" Esa pregunta depende de qué software, bajo qué condiciones, con cuánto criterio previo.

La pregunta útil es: *¿tengo el criterio para saber si lo que la IA produce es correcto?*

Si la respuesta es sí —y solo si—, el sistema descrito en este documento puede funcionar.

---

*IRAM_paper_metodologia_v1_0.md · Research narrative · Producto 2, entregable C1*
*Materia prima: IRAM_SKILL_desarrollo_con_IA_v1_0.md + IRAM_analisis_cuantitativo_2026-06-12_v3.md*
*Versión derivada para C2 (skill operacional): PENDIENTE*
