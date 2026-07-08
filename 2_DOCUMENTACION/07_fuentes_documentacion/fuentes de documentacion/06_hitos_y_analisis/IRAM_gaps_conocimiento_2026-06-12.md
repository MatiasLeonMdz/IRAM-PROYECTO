# IRAM — Análisis de Gaps de Conocimiento
**Plantilla B ejecutada:** 2026-06-12
**Fuente primaria:** IRAM_historial_unificado_2026-06-12.md (7345 msgs) vs TECHNICAL_WIKI_ACTIVE_v3.10 + ARCHIVE v3.7
**Fuente secundaria:** IRAM_hitos_metodologicos_v7, SESSION_LOG_CONSOLIDADO, marcos teóricos 20:27 y 21:32
**Alcance:** conocimiento del proyecto disperso en chats que no llegó completo a los documentos formales

---

## CATEGORÍAS DE ANÁLISIS

A. Conocimiento perdido — en chats, no en wiki
B. Decisiones revertidas — se tomaron y luego se cambiaron
C. Código descartado — se escribió pero no llegó al zip canónico
D. Patrones de error recurrentes — mismo problema en múltiples sesiones
E. Evolución del proceso — cuándo y por qué cambió la metodología
F. División de trabajo real — autoría de hitos y decisiones clave

---

## A — CONOCIMIENTO PERDIDO

### A.1 El botón de scripted_gui — investigación no documentada como proceso

**Qué está en la wiki:** Sección 18.4 del ARCHIVE documenta *qué* tenía la rama scripted_gui y *por qué se descartó técnicamente*. El razonamiento de diseño está correcto.

**Lo que falta:** la narrativa de *cómo ocurrió* la investigación. El historial muestra que Claude afirmó inicialmente que el panel de pops no era modable con scripted_gui, que era imposible agregar botones ahí. El operador cuestionó. Claude investigó leyendo los archivos del juego real. Resultado: el engine sí soporta `scripted_guis` con `scope = province`, pero el panel de provincia (territory) no es el mismo que el panel de área. El scope de área no está soportado en scripted_gui. La decisión de descartar fue técnica (scope de área inexistente) + de diseño (la arquitectura v3 era más simple y ya funcionaba).

**Por qué importa para el SKILL.md:** es el ejemplo canónico del ángulo 9 (modo de falla de Claude: confunde "no está documentado" con "no es posible"). El operador cuestionó la afirmación inicial. Tenía razón en cuestionar. El árbitro fue el game.zip, no Claude.

**Gap:** la wiki tiene el resultado, no el proceso de descubrimiento. Para el SKILL.md, el proceso importa más que el resultado.

---

### A.2 El descubrimiento de los scopes de país para operaciones globales

**Qué está en la wiki:** Sección 18.1 y 0.5 documentan que Gather Global, Distribute Global y Optimize Global existen y funcionan. Las operaciones por área están marcadas como descartadas. La wiki no explica *por qué* fue posible lo global cuando parecía imposible.

**Lo que falta en la wiki:** Claude afirmó que las operaciones sobre "todo el mapa" no eran viables — el engine no podía iterar miles de provincias en cada pulso mensual. El operador insistió. La solución fue el `monthly_country_pulse` con `every_owned_province` filtrada por variable — el engine no itera las ~8000 provincias del mapa, itera solo las que tienen la variable activa (~10 por operación). El costo de performance era manejable. Eso desbloqueó todas las operaciones globales.

**Evidencia en historial:** línea 1237 — "En el pulso mensual: `any_owned_province` con `has_province_flag = exodus_area_member` y `NOT = { owner = ROOT }`. Es una sola query sobre las provincias que tienen el flag activo (~10). El engine no itera las 8000 provincias."

**Por qué importa para el SKILL.md:** segundo ejemplo canónico del ángulo 9. El operador operaba desde lógica ("si el engine itera, debe poder filtrar"); Claude operaba desde conocimiento documentado ("iterar el mapa global es inviable"). El testing contra el engine fue el árbitro.

---

### A.3 El sistema de backup — origen causal, no narrativa de diseño

**Qué está en la wiki:** la wiki documenta *qué es* cada capa (PROMPT_MAESTRO, ACTIVE, ARCHIVE, SESSION_LOG) y *cómo usarla*. La sección 0.1 tiene la visión del proyecto. La sección 20 tiene el protocolo de actualización.

**Lo que falta:** *por qué creció así*. El PROMPT_MAESTRO no fue diseñado top-down. Cada regla tiene un problema real detrás. El operador desarrolló el sistema de backup ante pérdidas concretas de contexto — cuando CLAUDE_1 llegó al límite (conv_45, 2026-05-16), el contexto estaba en 40 conversaciones sin estructura transferible. El SUPERBACKUP creció orgánicamente hasta 220KB mezclando instrucciones y contenido. Claude no podía priorizar — ignoraba reglas sepultadas en el contexto. El split ACTIVE/ARCHIVE fue la respuesta a ese problema específico.

**Lo que está parcialmente documentado:** el ARCHIVE tiene el historial de versiones del SUPERBACKUP (Sección 14) y el STRATEGIC LOG menciona el sistema de control. Pero la causalidad completa (problema → síntoma → solución → por qué funciona) no está concentrada en ningún lugar.

**Para el SKILL.md:** el mecanismo generador del sistema es la cadena: pérdida concreta → patrón identificado → regla creada → regla incorporada al PROMPT_MAESTRO. Está documentado como principio en los hitos (R10: "cada regla del PROMPT_MAESTRO es un problema resuelto"), pero sin los ejemplos que lo demuestran.

---

### A.4 El problema de la arquitectura de contexto vs el contenido del prompt

**Qué está en la wiki:** el PROMPT_MAESTRO existe. Las instrucciones dicen "pegar como primer mensaje, no adjuntar".

**Lo que falta:** *por qué la posición importa*. El historial y el marco teórico documentan que Claude le daba menos peso a las instrucciones cuando el contexto era demasiado largo — las reglas sepultadas entre contenido técnico eran ignoradas. La solución no fue mejorar el contenido del PROMPT_MAESTRO sino cambiar su arquitectura: pegarlo en el primer mensaje le daba mayor peso que cargarlo como adjunto o embebido en el backup. Este conocimiento está en el log 20:27 ("el problema del PROMPT_MAESTRO no era el contenido sino la arquitectura de contexto") pero no en ningún documento operativo.

**Por qué importa:** es el principio más transferible del sistema. "La posición en el contexto afecta el peso que Claude le da a las instrucciones" no está documentado en ninguna guía oficial de uso de IA. Lo descubrieron empíricamente.

---

### A.5 El evento 2026-05-18/19 — el techo del sistema materializado

**Qué está en el análisis cuantitativo (v2):** el Bloque 0 documenta que el 18-19 de mayo todas las cuentas trabajaron en documentación sin producir código, y que eso precipitó el PROMPT_MAESTRO v3.0 con reglas sobre cuándo y cómo documentar.

**Lo que falta en documentos operativos:** la narrativa del evento. Las sesiones del 18/19 muestran C3, C4, C5 con 2 mensajes cada una exportando historiales a markdown. C1 y C2 procesando y unificando el superbackup. Ninguna cuenta produciendo código. El operador detectó el patrón, lo nombró, y generó reglas explícitas. El análisis cuantitativo lo tiene como dato. El SKILL.md necesita la historia, no solo el número.

**Para el SKILL.md:** es el caso donde el sistema se convirtió en su propio problema. Ángulo 10 candidato — el techo no era estructural sino un riesgo gestionable que se manifestó una vez y fue corregido.

---

### A.6 INSTRUCCIONES_HUMANO — archivo referenciado pero no explicado

**Qué está en la wiki:** la Sección 3.2 lista `IRAM_INSTRUCCIONES_HUMANO_AAAA-MM-DD_HH-MM.md` entre los archivos del sistema de control. La Sección 20.4 dice cuándo actualizarlo.

**Lo que falta:** qué contenía, para qué servía, y por qué existe como archivo separado del PROMPT_MAESTRO. El PROMPT_MAESTRO va a la IA. Las INSTRUCCIONES_HUMANO iban al operador — smoke tests, protocolo de reanudación, cómo verificar que el sistema funcionaba. Son documentos para audiencias distintas. Esta distinción no está documentada en ningún lugar con esa claridad.

**Para el SKILL.md:** evidencia de que el sistema de tres capas tenía en realidad una cuarta capa (para el operador), que evolucionó de manera diferente porque su audiencia era diferente.

---

## B — DECISIONES REVERTIDAS

### B.1 El cooldown entre operaciones — ciclo completo no documentado

**Qué está en la wiki:** Sección 18.2 documenta que el cooldown temporal entre usos de BOM fue descartado porque "variables de tiempo generan fallos en delay en IR 2.0.4."

**Lo que falta:** el ciclo completo para Exodos. El historial muestra que el cooldown se diseñó (línea 3611: "cooldown de la desicion de 1 mes"), se implementó, se testeó, se descubrió que `exodus_cooldown` se seteaba pero nunca expiraba porque el engine no tiene `remove_variable_after_days` nativo, y fue eliminado. El operador propuso directamente: "eliminamos el cooldown, que las opciones se rehabiliten luego de terminar las operaciones exitosamente." Claude confirmó que era la solución más limpia. El cooldown fue eliminado.

**Lo que está en la wiki:** el resultado (no hay cooldown en v4/v5). Lo que falta: el razonamiento de por qué no es necesario — el `is_ai = no` en `potential` es la única restricción necesaria; el cooldown no aportaba nada jugable real y era fuente de bugs.

**Para el SKILL.md:** ejemplo del patrón "decisión empírica con árbitro claro". La pregunta era si el cooldown era necesario. El test respondió: no funciona y no aporta nada. Resultado definitivo.

---

### B.2 Operaciones por área → operaciones globales — transición no documentada causalmente

**Qué está en la wiki:** la wiki documenta que las operaciones por área (Gather por área, Distribute por área, Optimize por área) están descartadas y que GG/DG/OG las reemplazan globalmente. La Sección 0.4b tiene la tabla de diferencias.

**Lo que falta:** el *por qué* fue posible y el *cuándo* se tomó la decisión. El historial muestra que las operaciones globales eran consideradas inviables por performance en fases tempranas. El operador propuso "global" como scope. La solución técnica (filtrar por variable en lugar de iterar todo el mapa) convirtió "inviable" en "posible". Esto ocurrió durante el desarrollo de v4, probablemente en mayo 2026, pero la causalidad no está documentada con fecha y sesión exacta.

**Gap abierto:** la fecha y la sesión exacta del desbloqueo. No está en los hitos metodológicos y no está en los logs de sesión de la wiki.

---

### B.3 IDs numéricos `iram_01`–`iram_25` → IDs descriptivos en v5.0

**Qué está en la wiki:** Sección 3.3, nota v3.6 — "IDs descriptivos v5.0 implementados. Los IDs numéricos `iram_01`–`iram_25` son legacy de v4 — ver ARCHIVE."

**Lo que falta:** por qué se hizo el cambio. Los IDs numéricos eran legibles para el operador pero no autoexplicativos para Claude ni para testing. Los IDs descriptivos (`iram_exodos_distribute_global`, `iram_bom_demo_migracion`) hacen el código autoexplicativo sin necesidad de la tabla de referencias. La decisión fue de legibilidad y mantenibilidad, tomada durante el rediseño de v5.0. El razonamiento no está documentado en la wiki.

---

### B.4 Costos cobrados en `activate` → costos cobrados en `confirm`

**Qué está en la wiki (Sección 18.3):** "Costs cobrados en `activate` — el jugador paga en `confirm`. Convención fija del ecosistema."

**Lo que falta:** la discusión que llevó a esa convención. El historial muestra que el operador planteó explícitamente la pregunta de diseño: ¿pagar al activar o al confirmar? El razonamiento fue de UX — el jugador ve la previsualización antes de pagar. Si paga al activar, paga sin saber si va a ejecutar. Si paga al confirmar, tiene toda la información antes del costo. La wiki tiene la regla pero no el argumento de UX detrás.

---

## C — CÓDIGO DESCARTADO

### C.1 Slave Distributor — backup preservado pero no integrado

**Qué está en el ARCHIVE (Sección 18.1):** "Slave Distributor (descartado 2026-05-25): Optimize Global cubre la función."

**Lo que falta:** el historial muestra que el Slave Distributor tuvo un desarrollo real — existe `backup_slave_distributor_v2.md` en el historial de herramientas. Tenía lógica propia de filtrado por `pop_type = slaves` en `random_pops_in_province`. El descarte no fue por falla técnica sino por redundancia funcional: Optimize Global resuelve el problema de distribución óptima sin una función especializada para slaves.

**Gap:** la distinción técnica entre lo que el Slave Distributor hacía (distribuir slaves específicamente por tipo de pop) y lo que Optimize Global hace (redistribuir todos los tipos según thresholds) no está documentada. Para alguien leyendo la wiki, "Optimize Global cubre la función" no explica qué función exactamente ni por qué la cobertura es suficiente.

---

### C.2 Arquitectura scripted_gui — conocimiento de investigación preservado parcialmente

**Qué está en el ARCHIVE (Sección 18.4):** estructura técnica de la rama y por qué se descartó. Conocimiento recuperado: guards cruzados y cleanup exhaustivo de legacy variables fueron portados a v4.

**Lo que falta:** el historial de la investigación muestra que Claude primero negó la viabilidad (el panel de pops no es modable), luego investigó el game.zip real, encontró que `scripted_guis` con `scope = province` sí existe, pero determinó que el scope de área no estaba disponible. Ese proceso de investigación no está documentado — solo el resultado. El valor para el SKILL.md es el proceso: cómo se pasa de "Claude dice que no existe" a "Claude investiga el game.zip" a "descubrimiento del límite real".

---

### C.3 Arquitectura monolítica v4.3.16 — split documentado sin el razonamiento del diseño

**Qué está en el ARCHIVE (Sección 18.5):** los tres problemas de la arquitectura monolítica (cleanup acoplado, BOM sin guard de menú, cleanup_menu monolítico) y sus soluciones en v5.0.

**Lo que falta:** el razonamiento de por qué v5.0 adoptó la arquitectura de 4 mods independientes. La Sección 18.5 explica cómo pero no por qué era mejor. El historial muestra que la decisión fue de mantenibilidad: cada mod puede actualizarse sin romper los demás, el namespace `iram_` evita colisiones entre mods, y el usuario puede activar/desactivar módulos independientemente. Ese razonamiento de diseño modular no está en la wiki.

---

## D — PATRONES DE ERROR RECURRENTES

### D.1 BOM pegado al token — el error que generó el mecanismo de entrega de archivos

**Qué está en la wiki:** Error 0 en Sección 0.4 — BOM corrupto como primer error documentado. La regla R2 dice que `build_mods.py` es obligatorio. La Sección 7 tiene la guía de diagnóstico del error.log.

**Lo que falta:** el *por qué* de la recurrencia. El historial muestra el mismo bug apareciendo múltiples veces en distintas versiones y distintas cuentas. La causa raíz era que al editar archivos con `cat >` y luego agregar el BOM manualmente, el resultado quedaba corrompido. El mecanismo que lo resolvió definitivamente fue el script `build_mods.py` que genera los archivos con BOM correcto desde el principio — no depende de que el operador recuerde agregar el BOM ni del método de creación del archivo.

**Para el SKILL.md:** ejemplo del patrón "bug recurrente → patrón identificado → herramienta que elimina la posibilidad del error". No fue "tener más cuidado" — fue cambiar el proceso para que el error fuera imposible.

---

### D.2 `ruler = {}` desde scope `country` — el bug que se documentó y siguió apareciendo

**Qué está en la wiki:** Error 19 en Sección 0.4 — documentado con historial "BOM v2.5, TLV v1.3 — 1454 hits en error.log."

**Lo que falta:** la razón de la recurrencia después de estar documentado. El historial muestra múltiples sesiones donde Claude generó código con `ruler = { condición }` desde scope `country`, a pesar de que el error estaba documentado en el backup. La causa: Claude le daba menos peso a las instrucciones del backup cuando el contexto era extenso. El problema no era que Claude no "supiera" la regla — era que el contexto arquitectónico no le daba suficiente peso a la regla para que compitiera con el patrón de codeo más intuitivo.

**Para el SKILL.md:** este es el ejemplo más claro del ángulo 2 (gap entre creación de la regla y adopción fiable). La regla estuvo en el backup desde v2.5; siguió apareciendo hasta que la arquitectura del contexto cambió (PROMPT_MAESTRO como primer mensaje).

---

### D.3 Namespace faltante en eventos — error silencioso de alto impacto

**Qué está en la wiki:** Error 22 en Sección 0.4 — "sin namespace, los eventos no se registran. El mod carga sin errores pero los eventos no existen."

**Lo que falta:** el contexto de cuántas veces apareció y en qué momento del proyecto se volvió imposible de repetir. El historial registra "Diseñador 1 Sesión 2, Agente 5 Sesión 1" — apareció temprano en múltiples cuentas. Fue uno de los primeros bugs en llegar a la documentación formal. Su recurrencia fue baja porque era fácil de detectar (síntoma visible: evento completamente ausente en juego).

---

### D.4 Herramientas distintas de IA (Copilot, ChatGPT) — interacción con el proyecto

**Lo que está en el historial:** hay evidencia de al menos un experimento con Copilot (líneas 2235, 2250) — el operador probó Copilot para un cambio en el repositorio, y Claude evaluó el código generado por Copilot encontrándolo "no funcional en Imperator" porque usaba Markdown en lugar de scripting real del engine. Línea 21510: Claude explica estrategias para unificar proyectos generados con múltiples IAs.

**Lo que falta en la wiki:** cualquier mención de esto. El proyecto usó mayoritariamente Claude, pero hubo al menos un test con Copilot y referencias a "la otra IA" en algunos mensajes. La wiki no documenta por qué se eligió Claude como herramienta principal ni qué diferencias concretas se encontraron.

**Para el SKILL.md:** dato relevante para el ángulo 11 (qué no es transferible). El sistema IRAM fue construido para Claude específicamente — las instrucciones, la arquitectura del PROMPT_MAESTRO, la forma de cargar contexto, todo asume el modelo de Claude. No necesariamente funciona igual con otros modelos.

---

## E — EVOLUCIÓN DEL PROCESO

### E.1 El origen del mecanismo generador de reglas — de emergente a deliberado

**Qué está documentado:** el hito `mecanismo_generador_reglas` está en los hitos metodológicos con la cadena completa: bug → debugging sistemático → patrón → regla → PROMPT_MAESTRO.

**Lo que falta:** el punto donde el mecanismo pasó de ser emergente (reglas que aparecían reactivamente) a deliberado (el operador decidía activamente qué convertir en regla). El historial muestra que en las primeras versiones las reglas aparecían cuando un bug se repetía. Hacia v4/v5, el operador había internalizado el mecanismo y lo aplicaba proactivamente: después de resolver un problema, preguntaba "¿qué regla previene que esto vuelva a pasar?" La transición no está marcada con fecha ni sesión.

---

### E.2 La evolución del SESSION_LOG — de registro de decisiones a instrucciones de ejecución

**Qué está documentado:** el hito `primer_session_log` (2026-05-25) y el hito `session_log_consolidado` (2026-06-04). El hito de consolidado tiene la causalidad completa.

**Lo que falta:** la etapa intermedia. El SESSION_LOG nació como registro de estado ("qué pasó, qué falta"). Para v5 se convirtió en instrucciones suficientes para que otra IA ejecutara sin tomar decisiones. El SESSION_LOG_CONSOLIDADO tenía 4 partes: estado, decisiones cerradas, plan con comandos exactos, y material de referencia. Esa evolución de "registro" a "especificación ejecutable" no está documentada como un cambio deliberado — ocurrió al enfrentar la complejidad del rework de v5.0 (13+ tareas con decisiones interdependientes).

---

### E.3 La distinción entre documentación de sesión y documentación de proyecto

**Lo que está en la wiki:** el PROMPT_MAESTRO tiene R19 (único SESSION_LOG). La Sección 20 tiene el protocolo de actualización de la wiki.

**Lo que falta:** la historia de cómo se aprendió a distinguir qué documenta cada capa. El historial muestra sesiones donde Claude mezclaba actualizaciones de wiki con actualizaciones de SESSION_LOG con contenido técnico en el mismo bloque. La separación entre "qué hicimos hoy" (SESSION_LOG), "qué es el proyecto ahora" (ACTIVE), y "qué fue el proyecto antes" (ARCHIVE) no era obvia al principio — emergió de la fricción de encontrar información en el lugar equivocado múltiples veces.

---

### E.4 La sesión estratégica 2026-05-27 — impacto en el sistema de documentación

**Qué está documentado:** el hito `sesion_estrategica_2026-05-27` tiene la evidencia completa del ARCHIVE (Sección 19) y la relevancia para el SKILL.md.

**Lo que falta:** el impacto concreto en el sistema de documentación. La sesión no solo reformuló la visión — fue la misma sesión donde se hizo el split ACTIVE/ARCHIVE, se adoptó el nombre TECHNICAL_WIKI, y se ejecutó el git init el día siguiente. La fecha 2026-05-27 concentra tres hitos de documentación distintos que están documentados por separado pero cuya coincidencia temporal no está explicada. Fue el día de mayor intensidad del proyecto (547 msgs, 17 bloques, 5 cuentas). Probablemente no sea coincidencia.

---

## F — DIVISIÓN DE TRABAJO REAL

### F.1 Qué fue del operador y qué fue de Claude — tabla consolidada

La fuente primaria sobre autoría es el STRATEGIC LOG de 2026-05-27 (ARCHIVE Sección 19). Los hitos metodológicos v7 tienen la dimensión de autoría por hito. Lo que falta es una tabla consolidada para el SKILL.md.

**Patrones encontrados en fuentes:**

| Tipo de contribución | Autoría típica | Evidencia |
|---|---|---|
| Arquitectura del sistema (scopes, flujos, diseño de funciones) | Operador | STRATEGIC LOG: "Las soluciones arquitectónicas difíciles fueron diseñadas por el operador, no por la IA" |
| Implementación de código (dado el diseño) | Claude | Log 20:27: "Claude fue una herramienta de precisión con capacidad de lenguaje" |
| Identificación de problemas técnicos del engine | Colaborativo | Mayoría de los gotchas en Sección 0.4 |
| Decisiones de diseño de gameplay (costos, UX, feedback) | Operador | R19_confirm, RD1_potential_minimo, cooldown descartado |
| Generación de nombres y vocabulario técnico | Colaborativo | `exodos_`, `iram_`, vocabulario del modelo lógico |
| Reconocimiento de patrones de bug | Claude | Diagnóstico en múltiples sesiones de debugging |
| Decisión de convertir patrón en regla | Operador | R10: "cada regla es un problema resuelto" — el operador los numeraba |
| Propuesta de estructura de documentos | Colaborativo | SESSION_LOG propuesto por Claude, adoptado por operador (hitos) |
| Criterio de qué documentar y qué descartar | Operador | Log 20:27: "el operador traía el criterio desde el principio" |

**Gap principal:** la tabla de arriba es inferida. No existe un documento que diga "en la sesión X, el operador propuso Y y Claude implementó Z". Las sesiones largas tienen esta información en el cuerpo de los mensajes pero no está resumida de manera accesible.

---

### F.2 Los desbloqueos técnicos — autoría específica

Los cuatro desbloqueos principales identificados en el log 20:27:

| Desbloqueo | Quién lo identificó | Quién lo implementó | Estado de documentación |
|---|---|---|---
| Decisiones ironman-compatible | Operador (buscó la restricción) | Claude (implementó) | ✅ Documentado en ARCHIVE historial |
| Unidad marcadora como scope | ⚠️ No claro — inferido como colaborativo | Claude | ⚠️ Falta atribución |
| Rival como anchor de funciones | ⚠️ No claro | Claude | ⚠️ Falta atribución |
| Scopes de país para funciones globales | Operador (insistió en la posibilidad) | Claude (encontró la implementación correcta) | ⚠️ Proceso no documentado |

---

## SÍNTESIS — GAPS MÁS RELEVANTES PARA EL SKILL.md

En orden de importancia para el SKILL.md (de mayor a menor):

**1. La arquitectura de contexto vs el contenido del prompt (A.4)**
El principio más transferible del proyecto y el menos documentado en los documentos operativos. Relevancia universal — aplica a cualquier uso de IA, no solo a modding.

**2. Los dos ejemplos canónicos del modo de falla de Claude (A.1, A.2)**
El botón de scripted_gui y los scopes globales. Ambos siguen el mismo patrón: Claude dice que no es posible → operador cuestiona → testing → era posible (o imposible por razón diferente a la citada). El proceso importa más que el resultado para el SKILL.md.

**3. El evento 2026-05-18/19 como materialización del techo del sistema (A.5)**
El único caso donde el sistema se convirtió en su propio problema. Candidato a ángulo 10. Falta la narrativa — los datos están en el análisis cuantitativo pero la historia está en el historial.

**4. El origen causal del sistema de backup (A.3)**
La wiki tiene el qué y el cómo. Falta el por qué emergió así. Para el SKILL.md, la causalidad (pérdida → patrón → regla) es la columna vertebral.

**5. La transición de registro a especificación ejecutable en el SESSION_LOG (E.2)**
Documenta la maduración del sistema. El SESSION_LOG de v5.0 era cualitativamente diferente al de v1 — pero esa diferencia no está nombrada ni fechada.

**6. La tabla consolidada de división de trabajo (F.1)**
El STRATEGIC LOG tiene la visión pero no los ejemplos. El SKILL.md necesita instancias concretas del principio "el operador diseña, la IA implementa" para que sea más que una afirmación.

---

## PENDIENTES Y DEUDA RESIDUAL

### Gaps que requieren búsqueda en el historial para resolver:

1. **Sesión exacta del desbloqueo de scopes globales** — buscar en historial del período 2026-05-13 a 2026-05-21 (ventana de desarrollo de v4.0). Buscar mensajes con "global" + "posible" o "todo el mapa" + fecha.

2. **Sesión del primer uso de rival como anchor** — buscar en el historial de v2/v3 la primera vez que el rival aparece como marcador de posición en lugar de condición de guerra.

3. **Razonamiento del split modular de v5.0** — buscar en las sesiones de diseño de v5.0 (2026-06-04, CLAUDE_4) por qué 4 mods independientes en lugar de un mod único.

4. **INSTRUCCIONES_HUMANO — contenido real** — el archivo no está entre los documentos subidos. Su contenido definiría con precisión la "cuarta capa" del sistema de documentación.

5. **Primera vez que el operador preguntó "¿qué regla previene que esto pase de nuevo?"** — marca la transición de mecanismo emergente a deliberado (E.1). Buscar en historial post-v3.

---

## QUÉ SIGUE

Plantilla B completa. Los gaps identificados alimentan directamente el SKILL.md:

- A.4 → Sección 5 del SKILL.md (gestión del límite de contexto / arquitectura de contexto)
- A.1, A.2 → Sección 10 del SKILL.md (patrones de error comunes — modo de falla de Claude)
- A.3 → Secciones 3 y 4 del SKILL.md (sistema de tres capas, protocolo de sesión)
- A.5 → Sección 10 / ángulo 10 del SKILL.md
- B.1, B.4 → Sección 7 del SKILL.md (sistema de versiones y entrega)
- D.1, D.2 → Sección 10 del SKILL.md (patrones de error)
- E.1, E.2 → Sección 12 del SKILL.md (cómo evoluciona el sistema)
- F.1 → Sección 6 del SKILL.md (división de trabajo operador/IA)

---

*IRAM — Análisis de Gaps de Conocimiento — 2026-06-12*
*Plantilla B ejecutada — 6 categorías, 18 gaps identificados*
*Fuente: historial unificado 7345 msgs vs WIKI ACTIVE v3.10 + ARCHIVE v3.7*
*Próxima plantilla: C — construcción del SKILL.md*
