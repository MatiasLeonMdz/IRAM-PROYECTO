# Crítica rigurosa del proyecto IRAM y su documentación
**Tipo:** Análisis crítico independiente
**Objeto de análisis:** C1 (paper), C2 (skill), análisis cuantitativo (v3), SKILL borrador v1.0
**Fecha:** 2026-06-12

---

## Estructura de esta crítica

Diez ángulos organizados de mayor a menor gravedad lógica. Los primeros cuatro
son problemas epistemológicos fundamentales — afectan la validez del argumento
central. Los siguientes tres son problemas metodológicos — afectan la solidez
de la evidencia. Los últimos tres son problemas de ejecución — afectan la
utilidad de los entregables.

Al final: fortalezas genuinas, sin condescendencia.

---

## 1. La tesis central fue presupuesta, no inducida

Este es el problema más serio del proyecto, y el menos visible porque la
documentación es muy coherente internamente.

El principio central —"la IA no democratiza la programación; permite ejecutar
pensamiento estructurado en dominios técnicos sin dominar la mecánica"— aparece
textualmente en el PROMPT_MAESTRO v1.8. El PROMPT_MAESTRO es el documento que
guió el análisis. El análisis luego "confirma" ese principio.

Esto invierte el orden epistemológico de un research narrative genuino. En
inducción real: el análisis produce la conclusión. Aquí: la conclusión estaba
en el documento de instrucciones del análisis antes de que el análisis
comenzara. Lo que el paper hace es respaldar una afirmación preexistente con
datos seleccionados. Eso es deducción presentada como inducción.

El paper dice "la afirmación central de este documento" y la enuncia en el
resumen ejecutivo. En un case study genuino, la afirmación central no aparece
en el resumen — emerge del análisis. El orden aquí es: tesis → evidencia →
"conclusión" que ya era la tesis.

Esto no significa que la tesis sea falsa. Significa que el paper no la prueba
—la ilustra. La distinción importa.

**Implicación práctica:** un lector crítico externo podría preguntar "¿qué
evidencia habría llevado a una conclusión diferente?" y la respuesta no está
en el paper. Un argumento sin condiciones de falsación no es un argumento
científico — es una narrativa coherente. Hay valor en eso, pero es diferente
de lo que el paper afirma ser.

---

## 2. N=1 con condiciones altamente específicas generaliza sin modular la tesis

El proyecto tiene un operador, un dominio, una herramienta, un tipo de tarea.
El paper declara tres condiciones de transferibilidad (criterio preexistente,
árbitro claro, problema acotado) pero la tesis central no está formulada como
condicional — está formulada como universal.

"La IA no democratiza la programación" no es la misma afirmación que "en
proyectos técnicos con árbitro claro, operado por alguien con criterio
preexistente, la IA no democratiza la programación." La primera es una
afirmación sobre la IA. La segunda es una afirmación sobre este tipo específico
de proyecto con este tipo específico de operador.

El paper elige la primera formulación en el resumen ejecutivo y en el cierre
del Bloque 4, y deja la segunda formulación para la Sección 5 (al final). El
efecto retórico: el lector recibe la afirmación fuerte primero y las
condiciones después, cuando la impresión ya está formada.

Un paper riguroso haría lo opuesto: las condiciones de aplicabilidad primero,
la afirmación dentro de esas condiciones después.

**Caso concreto:** ¿qué pasaría con un operador sin criterio preexistente? No
lo sabemos. El paper no tiene ese caso. La Condición 1 lo reconoce —pero
reconocer una condición de no-transferibilidad al final del paper no modula
la tesis que se enunció al principio con lenguaje universal.

---

## 3. Circularidad entre "criterio preexistente" y "habilidades entrenadas"

El paper afirma (Condición 1, Sección 5) que el operador llegó con criterio
preexistente: capacidad de descomponer problemas, buscar evidencia antes de
aceptar explicaciones, cuestionar afirmaciones de la IA. Ese criterio es la
condición de no-transferibilidad más importante.

El SKILL borrador (Sección 11) afirma que el proyecto entrenó habilidades que
incluyen exactamente esas capacidades: "pensamiento computacional, diseño de
sistemas, debugging sistemático, arquitectura de decisiones bajo
incertidumbre." Y dice explícitamente que "el modding fue el camino ameno hacia
programación y ciencia de datos" y que el ciclo hipótesis-prueba-resultado "es
el método científico, aplicado a mecánicas de un videojuego."

Estas dos afirmaciones no pueden ser simultáneamente correctas sin contradicción:

- Si el criterio preexistía → las habilidades ya estaban → el proyecto las
  aplicó a un dominio nuevo, no las desarrolló.
- Si el proyecto entrenó esas habilidades → no preexistían en la forma que el
  proyecto requería → la Condición 1 es más porosa de lo que afirma.

La tensión real probablemente es: el operador tenía criterio general (analítico,
lógico) y el proyecto lo especializó y formalizó en un dominio técnico. Eso es
una afirmación más matizada y más honesta que cualquiera de las dos versiones
que los documentos presentan por separado. Pero esa versión matizada no existe
en ninguno de los dos documentos — la contradicción queda sin resolver porque
C1 y el SKILL borrador coexisten sin haberse leído críticamente el uno al otro.

---

## 4. La confusión entre correlación y causalidad en el Bloque 0

El hallazgo más citado del análisis cuantitativo: el promedio de mensajes por
sesión bajó de 35.0 (P1, sin sistema formal) a 18.4 (P3, PROMPT_MAESTRO) a
14.1 (P4, ACTIVE/ARCHIVE split). El paper atribuye esta caída a la arquitectura
de contexto.

Hay al menos tres explicaciones alternativas que el análisis no descarta:

**Alternativa 1 — tipo de tarea:** P1 (04-17 a 05-13) es el período de
construcción del mod en sus primeras versiones, con mucho más debugging
exploratorio. P3 y P4 son períodos de implementación de funciones ya diseñadas.
Las tareas más maduras producen sesiones más cortas independientemente de la
arquitectura de contexto.

**Alternativa 2 — curva de aprendizaje del operador:** el operador tenía más
experiencia en P4 que en P1. Sesiones más cortas y más eficientes pueden
reflejar que el operador aprendió a usar la herramienta, no solo que la
arquitectura mejoró. Estas dos cosas ocurrieron simultáneamente y el análisis
no las separa.

**Alternativa 3 — el denominador es sensible al corte:** P2 (SUPERBACKUP) tiene
solo 2 días, 10 sesiones, 22.3 msgs/sesión. Un período de 2 días es
estadísticamente ruido — cualquier hallazgo sobre P2 no es generalizable. El
paper no menciona esto.

El interrupted time series es el mejor intento metodológico del análisis, y
vale reconocerlo. Pero el interrupted time series no controla causas
confundidas que cambian al mismo tiempo que la variable de intervención. Aquí,
la experiencia del operador y el tipo de tarea cambiaron junto con la
arquitectura de contexto. La causalidad atribuida al contexto podría ser
parcialmente de las otras dos variables, y no hay forma de saberlo con los
datos disponibles.

---

## 5. Problemas de clasificación en el script que no se reconocen

**bloque3_analysis_v2.py** es reproducible y metodológicamente superior a v1.
Pero tiene problemas de clasificación que no están documentados como
limitaciones.

**is_meta_doc() es frágil:** la exclusión de sesiones de meta-documentación se
hace por keywords en el nombre de la conversación (`'historial'`, `'skill'`,
`'análisis cuantitativo'`). Un nombre mal puesto incluye conversaciones de
mod-dev en meta-doc y viceversa. No hay validación cruzada de este criterio.
La función excluye 4 conversaciones de v5 (112 msgs). Para una fase con solo
523 mensajes, 112 mensajes excluidos con criterio no verificado es un 21% de
impacto potencial en las métricas de v5.

**La categoría "other" en Tabla B:** representa el 50% de la Investigación en
v1-v2 y el 53% en v3. El análisis cuantitativo describe "other" como
"exploración de mecánicas del juego" con vocabulario específico (`heir_weight`,
`treasury`, `succession`). Pero esta descripción es una narrativa propuesta
para explicar "other" —no es el resultado de aplicar el mismo tipo de análisis
objetivo que se usó para las otras categorías. El 50% de la Investigación
inicial queda en una categoría que se interpreta narrativamente, no se
clasifica con señales objetivas.

**DECISION_KW captura falsos positivos:** el regex incluye `\bestructura\b`.
"Estructura" en mensajes de código puede referirse a la estructura de un
archivo, de una función, o de un namespace —no necesariamente a una decisión
de diseño de alto nivel. La densidad de "lenguaje de decisión" en la Tabla C
puede estar inflada por usos técnicos del vocabulario.

**El A-kw% (Claude) es 7-10x mayor que H-kw% (operador) en todas las fases:**
Claude usa lenguaje de propuesta, criterio y estructura en el 48-66% de sus
mensajes, frente al 4.5-7% del operador. Este hecho, que es el más llamativo
de la Tabla C, no se analiza. La explicación más simple: Claude usa ese
vocabulario por defecto al plantear soluciones, independientemente del nivel
de madurez del proceso. Si es así, el A-kw% no mide "rol de arquitecto" —
mide el estilo por defecto de Claude. La tendencia ascendente en A-kw%
(51.9% → 66.5%) podría ser real, pero el baseline ya es muy alto desde v1-v2,
lo que debilita la interpretación como "más rol de arquitecto."

---

## 6. Los sample sizes no están reconocidos como limitación

| Fase | Msgs (mod-dev) |
|------|---------------|
| v1-v2 | 851 |
| v3 | 3.603 |
| v4 | 1.933 |
| v5 | 523 |

v5 tiene el 14.5% de los mensajes de v3. Las métricas de v5 son las que el
paper más cita: ratio Inv/Cód de 2.9x, H-avg-chars de 183, A-kw% de 66.5%.
Con 523 mensajes y 62 conversaciones, una sola sesión atípica tiene impacto
significativo en los promedios. El paper no reporta dispersión, intervalos de
confianza, ni reconoce que los hallazgos de v5 son los más influenciables por
outliers.

Las Top 5 conversaciones de v5 en la Tabla D acumulan el 30% de toda la
Investigación de v5. Eso significa que el ratio Inv/Cód de v5 está muy
concentrado en pocas sesiones ("audit 5.2", "Confirmación de cambios").
Si esas sesiones son representativas del proceso v5, el ratio es un hallazgo
real. Si son excepcionales (auditorías que no ocurrían normalmente), el ratio
está sesgado al alza. El paper supone que son representativas. No lo verifica.

---

## 7. La velocidad de v5 mezcla dos variables causales distintas

El hallazgo de velocidad (1.8 ses/día en v1-v2 → 9.4 ses/día en v5) es
presentado como evidencia de maduración del proceso. Hay una causa alternativa
no mencionada: v5 adoptó una arquitectura de 4 mods independientes.

Cuatro mods separados = cuatro superficies de trabajo distintas = más sesiones
de menor tamaño por diseño arquitectónico. Una sesión que en v3 o v4 era "una
conversación sobre el mod completo" en v5 se divide en "sesión sobre exodos",
"sesión sobre bom", "sesión sobre tgl", "sesión sobre tli". La fragmentación
es estructural, no solo un indicador de eficiencia.

El paper no distingue entre "más sesiones por día porque el proceso es más
eficiente" y "más sesiones por día porque la arquitectura del mod las requiere".
Ambas explicaciones producen el mismo patrón de datos. La primera apoya la
narrativa de maduración; la segunda no.

---

## 8. El paper (C1) no cumple la promesa de "las dos historias en paralelo"

El Bloque 3 promete mostrar las dos historias —del mod y del sistema de
documentación— "sin mezclarlas." La promesa narrativa es que el lector verá
cómo evolucionaban en paralelo, con puntos de cruce donde un hito de una
historia afecta a la otra.

Lo que el Bloque 3 entrega es una descripción secuencial: primero el sistema
de documentación (sin el mod), luego los puntos de corte del análisis
cuantitativo. Las dos historias no se muestran en paralelo —se mencionan por
separado y el lector tiene que inferir la relación.

La promesa narrativa habría requerido una estructura de tabla de tiempo dual
o al menos párrafos que mostraran: "mientras en el mod ocurría X, el sistema
de documentación pasaba por Y, y la relación era Z." Eso no existe en el
Bloque 3. El papel dice que las dos historias son distintas pero no muestra
al lector por qué eso importa para la argumentación.

---

## 9. El skill (C2) evaluado por su propio criterio

El criterio declarado del C2 es: "cada línea debe cambiar lo que Claude hace;
si no, es narrativa." Aplicando ese criterio a cada sección:

**Sección 2 — Arranque de sesión:** mayormente sólida. "Cargar el documento de
instrucciones como primer mensaje pegado, no como adjunto" es una instrucción
que cambia el comportamiento. ✅ El párrafo sobre cuatro capas ("El contexto
tiene cuatro capas... Cargar las primeras dos siempre") es DESCRIPTIVO en su
primera oración y PRESCRIPTIVO en la segunda. La descripción no pertenece
aquí. ⚠️

**Sección 3 — Durante la sesión:** "Si una instrucción no se sigue de forma
consistente a pesar de estar clara: el problema es de posición en el contexto,
no de contenido. Revisar dónde vive la instrucción." Este es un diagnóstico
para el OPERADOR, no una instrucción para Claude. Claude no va a
retroalimentar al operador sobre la arquitectura de contexto de manera
autónoma. La instrucción no cambia el comportamiento de Claude — describe
qué debería hacer el operador cuando el sistema falla. Es narrativa del paper
embebida en el skill. ❌

**Sección 6 — Principio de operación:** "El estado del proyecto vive en
documentos, no en conversaciones. Cada sesión es descartable; los documentos
no." Este es un principio declarativo elegante, pero Claude que lo lee no sabe
qué hacer diferente. El principio no genera un comportamiento observable. ⚠️

**Evaluación general:** el C2 cumple su criterio en el 70-75% de su contenido.
El resto son principios o diagnósticos que pertenecen al paper, no al skill.
El slip más significativo es la Sección 6 completa —es la más poderosa
retóricamente y la menos prescriptiva de todas.

---

## 10. Lo que el paper dejó afuera del borrador

La comparación entre el SKILL borrador (13 secciones) y C1 (5 bloques) muestra
restructuración real —C1 no reformateó el borrador, lo rediseñó. Pero en ese
proceso, contenido con valor propio desapareció sin que quede claro si fue
deliberado o por simplificación excesiva.

**Lo que desapareció completamente:**

*Sección 7 del borrador (sistema de versiones):* el argumento de por qué
documentar el razonamiento junto con la decisión —no solo qué se decidió sino
por qué— no tiene correlato en C1. Esta idea tiene valor independiente del
proyecto IRAM y habría sido uno de los aportes más transferibles del paper.

*Sección 8 del borrador (herramientas situacionales):* la distinción entre
prácticas permanentes y prácticas temporal-situacionales aparece solo como
una nota al final de la Sección 5 de C1 ("Una nota sobre ciclo de vida"). En
el borrador tiene una sección entera con la lógica de activación: cuándo
encender el overhead y cuándo apagarlo. Esa lógica es operacionalmente crítica
y se redujo a dos oraciones.

**Lo que apareció degradado:**

*El protocolo de sesión:* en el borrador (Sección 4), el arranque, el trabajo
y el cierre tienen descripción propia. En C1, el protocolo queda implícito en
el Hallazgo 2 del Bloque 4, mencionado de pasada. Un lector del paper que
quisiera implementar el sistema no tiene instrucciones claras —tiene que
inferirlas de la narrativa histórica.

*Los dos ejemplos canónicos del modo de falla:* en el borrador (Sección 6)
tienen el patrón completo: "Claude dijo X → operador cuestionó → se investigó
→ resultado real." En C1 (Hallazgo 3) están, pero condensados al punto de
perder el patrón explícito. Un lector que no conoce el proyecto puede leerlos
sin captar que la secuencia es el hallazgo, no el resultado técnico.

---

## Fortalezas genuinas

Porque la crítica sin reconocimiento de lo que funciona es también imprecisa.

**La Sección 5 del paper (límites de transferibilidad) es genuinamente
excepcional.** La mayoría de los case studies de metodología terminan con
optimismo genérico. Esta sección termina con condiciones verificables y
concretas. Las tres condiciones (criterio preexistente, árbitro claro,
problema acotado) son testables antes de adoptar el sistema. El párrafo final
—"un sistema copiado sin sus condiciones de operación no produce los mismos
resultados"— es más honesto que la mayoría de lo que se publica sobre
metodología de IA.

**La corrección del Bloque 2 (cuentas paralelas → rotación secuencial)
demuestra autocrítica real.** El error anterior no se minimiza —se documenta
con precisión: qué metodología era incorrecta, por qué, y qué la reemplaza.
La versión incorrecta se preserva con su veredicto ("metodología deficiente").
Esto es rigor documental que pocos proyectos exhiben.

**El script bloque3_analysis_v2.py es reproducible.** Los processed JSON más el
script producen exactamente las tablas del análisis. En el ecosistema de
"metodología de IA" donde la mayoría de las afirmaciones son anecdóticas, tener
un análisis con datos primarios + script + output reproducible es
significativamente más riguroso que la media.

**La distinción C1/C2 está bien ejecutada.** El riesgo de dos documentos para
el mismo material es que uno sea una copia del otro con formato diferente. No
lo son. C1 tiene narrativa causal, historia de origen, y datos. C2 tiene
instrucciones puras, YAML frontmatter, y propósito de cambio de comportamiento.
El test "¿esto cambia lo que Claude hace?" está presente en la mayoría del C2.

**El gap de cuentas paralelas → rotación secuencial también es un argumento
metodológico dentro del paper.** La Sección 9 del borrador lo documenta como
"una instancia más del patrón de la Sección 6": afirmación hecha con confianza
desde evidencia indirecta, cuestionada, revisada al medir con evidencia más
directa. Usar la corrección de un error metodológico propio como evidencia del
principio que el paper defiende es metodológicamente elegante.

---

## Veredicto

El proyecto tiene dos niveles de calidad, y es importante separarlos.

**Como ejercicio de documentación de proceso:** el trabajo es sólido y notable.
Documentar 441 conversaciones, identificar hitos con causalidad explícita,
mantener un sistema de contexto funcional a través de 5 cuentas y 10+ sesiones
de documentación, y producir un análisis cuantitativo reproducible —todo eso es
más riguroso que la mayoría de los proyectos similares.

**Como research narrative con pretensiones de generalización:** el paper tiene
un problema de fondo que los ángulos 1-4 describen en detalle: la tesis central
fue presupuesta, el n=1 no justifica la formulación universal, hay circularidad
no resuelta en la condición más importante, y la causalidad del hallazgo
central (arquitectura de contexto → eficiencia) no está aislada de variables
confundidas.

Esto no invalida el paper —lo reencuadra. El paper funciona bien como:

1. Documentación detallada de cómo un sistema de trabajo emergió en este
   proyecto específico.
2. Un argumento plausible (no demostrado) de que la arquitectura de contexto
   importa más que el contenido del prompt.
3. Una lista honesta y operacionalizable de condiciones bajo las cuales el
   sistema funciona.

El paper no funciona como evidencia de la tesis universal que enuncia en el
resumen ejecutivo. Eso requeriría al menos un caso comparativo (un operador
sin criterio preexistente, o el mismo operador sin el sistema de documentación)
y aislar las variables causales que el análisis actual mezcla.

**Recomendación principal:** reencuadrar la tesis del paper. En lugar de "la IA
no democratiza la programación" (afirmación universal), enunciarla como "este
caso sugiere que la IA no democratiza la programación, al menos bajo estas tres
condiciones verificables." El tono pierde potencia retórica pero gana precisión
epistémica. Para un lector que va a usar el paper para tomar decisiones
sobre cómo trabajar, la versión precisa es más útil que la versión potente.

---

*Crítica rigurosa IRAM — 2026-06-12*
*Objetos analizados: C1, C2, análisis cuantitativo v3, SKILL borrador v1.0, bloque3_analysis_v2.py*
