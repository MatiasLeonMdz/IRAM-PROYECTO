# Esqueleto — Nuevo C1
## "Qué aprendimos sobre cómo funciona la IA"
### Proyecto IRAM — Entregable final Módulo 5

*Audiencia: lector con contexto de IA (diplomatura UTN BA), sin contexto del proyecto.*
*Producido: s17. Arco: lo que el proyecto reveló sobre el comportamiento de la IA.*

---

## ARGUMENTO CENTRAL (una línea — confirmar al cierre)
"La IA no democratiza la programación. Permite ejecutar pensamiento estructurado
en dominios técnicos sin dominar la mecánica — pero el límite no es la herramienta,
es la calidad del pensamiento que la opera. La herramienta además tiene techo propio."

---

## Sección 1 — El laboratorio

**Pregunta que responde:** ¿qué fue IRAM y por qué sirve como caso de estudio?

**Argumento:** El mod fue un vehículo. Lo que el proyecto construyó para que la IA
pudiera trabajar de forma sostenida es el objeto real de este documento.

**Evidencia:**
- Escala: 441 conversaciones, 7345 mensajes, 5 cuentas, ~2 meses
- Las dos historias: historia técnica del mod (v1→v5) e historia del sistema
  que permitió construirlo — son paralelas y no se mezclan
- La sesión que reformuló el proyecto: "el mod exitoso es el entregable,
  el aprendizaje es el objetivo real"

**Vocabulario formal:** ninguno todavía — solo establecer el escenario

**Fuente en SKILL v1.0:** Secciones 1 y 2 (casi intactas, cambio de voz mínimo)

---

## Sección 2 — Lo que tuvimos que construir (y por qué)

**Pregunta que responde:** ¿qué problemas aparecieron y cómo los resolvimos?

**Argumento:** Los problemas no eran de contenido sino de arquitectura. El sistema
emergió por presión, no por diseño: el costo de no estructurar superó al de estructurar.

**Evidencia:**
- Evolución del sistema: SUPERBACKUP monolítico (220KB, 4957 líneas) →
  tres capas separadas por función
- El día 2026-05-27: convergencia espontánea — tres cambios estructurales en
  un día, sin plan previo, en el día de mayor intensidad del proyecto
- El cuarto documento que no estaba nombrado: INSTRUCCIONES_HUMANO (para el
  operador, no la IA — audiencias distintas, evolución distinta)
- Las herramientas situacionales como evidencia del principio: overhead de
  documentación proporcional al riesgo que mitiga, no al tamaño del proyecto

**Vocabulario formal:** RAG manual / knowledge management, cognitive load management,
state management (SESSION_LOG como mecanismo de handoff)

**Fuente en SKILL v1.0:** Secciones 3, 4, 8, 12

---

## Sección 3 — El hallazgo central: la posición importa más que el contenido

**Pregunta que responde:** ¿cuál fue el descubrimiento más importante sobre cómo
funciona la IA en la práctica?

**Argumento:** Una instrucción correcta, bien escrita y documentada puede seguir
sin aplicarse — no porque la IA no la "entienda", sino porque su posición en el
contexto determina el peso que le asigna. Esto es medible.

**Evidencia:**
- El caso del error repetido: solución documentada en el backup, seguía
  ocurriendo sesión tras sesión porque estaba enterrada entre miles de líneas
- La tabla de reducción de costo de inicio de sesión:
  sin estructura: 35.0 mensajes promedio hasta trabajo productivo
  instrucciones como primer mensaje: 18.4
  + separación activo/archivo: 14.1
- "Economía de contexto" (cita directa 2026-05-19): "las reglas R no son
  desconfianza sino economía de contexto — lo documentado no se rediscute,
  lo no documentado es espacio de colaboración"

**Vocabulario formal:** context position weighting (empírico), attention mechanism
(sin entrar en arquitectura técnica), few-shot in-context learning (plantillas
del PROMPT_MAESTRO como ejemplos estructurales)

**Nota:** Esta es la sección más contra-intuitiva y más respaldada por evidencia.
La sección 5 del SKILL v1.0 ya tiene la tabla y el argumento — cambio de voz mínimo.

**Fuente en SKILL v1.0:** Sección 5 (casi intacta)

---

## Sección 4 — Cómo trabaja la IA: tres hallazgos con casos

**Pregunta que responde:** más allá del contexto, ¿qué aprendimos sobre el
comportamiento específico de la IA como herramienta de trabajo?

**Argumento:** Tres hallazgos distintos, cada uno con evidencia propia y con
un modo de operación que cambia al conocerlo.

**Hallazgo A — La IA ejecuta, no diseña**
El operador es el arquitecto; la IA es una herramienta de precisión con
capacidad de lenguaje. La coloca exactamente lo que se le indica aunque el
plano tenga un error — eso no es una limitación menor, es la base de la
división de trabajo.
Concepto formal: Human-in-the-Loop (HITL), specification-driven development
(75 msgs de diseño → SESSION_LOG_CONSOLIDADO → 13 TAREAs sin decisiones pendientes)

**Hallazgo B — La IA confunde "no documentado" con "no posible"**
Modo de falla epistémico: afirma imposibilidad con la misma confianza cuando
tiene razón y cuando no. Dos casos canónicos con el mismo patrón:
- scripted_gui: "ese tipo de elemento no existe" → investigación real →
  sí existe, para otro alcance; el "no" fue correcto pero mucho más estrecho
- scopes globales: "iterar sobre miles de elementos no es viable" →
  el operador insiste desde lógica → mecanismo de filtro que desbloqueó
  todas las operaciones globales del mod
El árbitro nunca fue la IA. Siempre fue el motor (o el sistema real).
Concepto formal: failure mode classification por fuente (epistémico vs. técnico)

**Hallazgo C — Las decisiones descartadas tienen audiencia propia**
La sección de alternativas evaluadas (qué se descartó y por qué) no estaba
dirigida al operador — estaba dirigida a la IA futura. Su función era reducir
el costo de re-proponer decisiones ya evaluadas seis semanas después.
Concepto formal: Architecture Decision Records (ADRs) orientados a IA

**Fuente en SKILL v1.0:** Secciones 6, 7, 10 (condensar y reorganizar)

---

## Sección 5 — Los datos del proceso

**Pregunta que responde:** ¿hay evidencia cuantitativa de que el sistema funcionó?

**Argumento:** El proceso mejoró de forma medible. Y los datos también muestran
dónde la medición misma tiene límites.

**Evidencia cuantitativa:**
- Velocidad: < 2 sesiones/día en v1-v2 → 9+ sesiones/día en v5
- Ratio Inv/Cód: 2.9x en v5 (planificación estructurada, no fricción)
- Los 4 puntos de corte: antes/después de cada cambio estructural
- Rotación de contextos verificada con timestamps individuales:
  0 casos de interleaving en 7.313 mensajes — 5 cuentas era rotación
  secuencial, no paralelismo. El modelo "cuentas paralelas" no sobrevivió
  al medir con mayor resolución.

**El límite de la medición:**
- Los scripts miden keywords, no patrones de pensamiento (proxy metrics problem)
- La velocidad en v5 no fue más alta porque el problema fuera más simple
  (su alcance era mayor) — fue más alta porque el sistema se había internalizado

**Vocabulario formal:** interrupted time series (experimento natural con 4 puntos
de corte), pipeline ETL (conversations.json → procesamiento → historial unificado),
proxy metrics problem, sensitivity analysis (valor_rp con rango documentado)

**Fuente en SKILL v1.0:** Secciones 9, 11; datos de paper v1.0 secciones 2 y 4

---

## Sección 6 — Los conceptos formales que nombran lo que hicimos

**Pregunta que responde:** ¿cómo conecta la experiencia del proyecto con el
vocabulario de la diplomatura?

**Argumento:** El proyecto ejercitó conceptos formales sin saber sus nombres.
Nombrarlos retroactivamente no es cosmético — es lo que permite transferir
la experiencia y reconocerla en otros contextos.

**Mapa (condensado — 8 áreas):**

| Lo que hicimos | Nombre formal | Módulo |
|---|---|---|
| conversations.json → procesamiento → historial | Pipeline ETL | M2 |
| "7345 msgs post-dedup" | Deduplicación de dataset | M2 |
| 4 puntos de corte antes/después | Interrupted time series | M3 |
| Barrido de parámetros sección 12 (17 rangos) | Grid search | M3 |
| valor_rp con rango [min, max] no cerrado | Epistemic uncertainty | M3 |
| ACTIVE/ARCHIVE + PROMPT_MAESTRO + SESSION_LOG | RAG manual | M4-U1 |
| Operador diseña / IA ejecuta | HITL | M4-U1 |
| bug → patrón → regla | Blameless post-mortem | Transversal |
| v4 → v5: namespace + contaminación + monolito | Technical debt (3 tipos) | Transversal |

**Lo que faltó genuinamente:**
- Herramientas no-code (Make, Zapier) — M4-U2
- Visión por computadora — M4-U4

**Fuente en SKILL v1.0:** Sección 11 (reestructurar completamente como tabla)

---

## Sección 7 — Qué transfiere y qué no

**Pregunta que responde:** ¿qué de esto es aplicable fuera de este proyecto?

**Argumento:** Tres condiciones estructurales definen el perfil de proyecto donde
este sistema rinde al máximo. Su ausencia no impide usar el sistema — requiere
adaptación que este documento no cubre.

**Las tres condiciones:**
1. Criterio lógico preexistente — lo que no puede transferirse es el pensamiento
   que construyó el sistema. El criterio se trajo de antes y se aplicó a un dominio nuevo.
2. Árbitro claro — el motor del juego corre o no corre. Sin retroalimentación
   inequívoca, el ciclo hipótesis-prueba tiene costo radicalmente distinto.
3. Problema acotado — alcance definible, resultado verificable, criterio de éxito
   observable. Proyectos más difusos no tienen ese cierre por iteración.

**El cuarto límite:** el sistema fue construido para este modelo específico.
La arquitectura de contexto de sección 3 asume comportamientos particulares
que no hay garantía de que transfieran sin cambios a otra herramienta.

**Cierre del paper:**
El techo de la herramienta es estructural y no se mueve.
El techo del operador se mueve con la experiencia.
Este documento es sobre cómo gestionar el primero lo suficientemente bien
para que el segundo sea el único que importe.

**Fuente en SKILL v1.0:** Sección 13 (casi intacta — cambio mínimo de voz)

---

## MAPPING COMPLETO: SKILL v1.0 → C1

| Sección SKILL v1.0 | Destino en C1 | Trabajo necesario |
|---|---|---|
| 1 — Cuándo usar | Sección 1 | Cambio de voz: "usé esto porque" → "el proyecto empezó como" |
| 2 — Dos historias | Sección 1 | Ya es narrativo — solo reencuadrar audiencia |
| 3 — Sistema de capas | Sección 2 | Instructivo → narrativo causal |
| 4 — Protocolo sesión | Sección 2 | "hacer X" → "así fue evolucionando" |
| 5 — Arquitectura contexto | Sección 3 | CASI INTACTO — ya tiene tabla y argumento |
| 6 — División operador/IA | Sección 4A y 4B | Ampliar con casos canónicos detallados |
| 7 — Versiones | Sección 4C + Sección 5 | Dividir en dos destinos |
| 8 — Herramientas situacionales | Sección 2 | Integrar como parte de la evolución |
| 9 — Rotación contextos | Sección 5 | Mover a datos — es evidencia del experimento natural |
| 10 — Patrones de error | Sección 4B | Condensar en failure mode classification |
| 11 — Conexión data science | Sección 6 | Reestructurar completamente como tabla |
| 12 — Evolución del sistema | Sección 2 | Ya es narrativo — integrar |
| 13 — Qué no transfiere | Sección 7 | CASI INTACTO |

**Lo que falta del SKILL v1.0 y hay que agregar:**
- Cluster 1 (ETL, dedup, proxy metrics) → Sección 6
- Cluster 2 (interrupted TS, grid search, sensitivity) → Sección 5 + 6
- INSTRUCCIONES_HUMANO como cuarta capa → Sección 2
- "Economía de contexto" (cita 2026-05-19) → Sección 3
- Modo de falla epistémico con 2 casos canónicos expandidos → Sección 4B

---

*Esqueleto C1 — s17 — 2026-06-16*
*Próximo paso: draft sección por sección, empezando por Sección 3 (la más madura — casi intacta).*
