PLAN DE TRABAJO INTEGRADO — IRAM / Documentación / Diplomatura UTN
Versión: 1.3 (Corregido con hipótesis de origen)
Fecha: 2026-07-05 04:30
Base: Logs de replanteo hasta DR-54, reorganización física completada (DR-51), inventario completado (DR-45–49)
Próximo hito crítico: Entrega Parte 1 UTN → 2026-07-15
NOTA DE CORRECCIÓN CRÍTICA: Esta versión reconoce que los conceptos DTI y FCC NO están documentados en los historiales previos. Son propuestas conceptuales nuevas generadas en la conversación del 2026-07-05. El objetivo de la Tarea 1.7 es encontrar evidencia empírica que respalde o refute las hipótesis sobre su origen.
1. ESTADO ACTUAL RESUMIDO

    Estructura física: APLICADA (DR-51) - carpetas 1_MOD/, 2_DOCUMENTACION/, 3_PORTAFOLIO_UTN/, _CUARENTENA_DUPLICADOS/
    Inventario de archivos: COMPLETADO (DR-45–49) - 1991 archivos, corpus A/B identificados
    Corpus A crudo: EN 1_MOD/corpus_A_crudo/ - 5 archivos data-*-batch-0000.zip de enero 2026
    Corpus B crudo: EN 2_DOCUMENTACION/05_corpus_B_crudo/ - 5 archivos documentacion claude 1-5.zip de 10-20/06
    Corpus B procesado parcial: EXISTEN claude_1_processed.json hasta claude_5_processed.json en 07_fuentes_documentacion/ - sin abrir (DR-47)
    Paper C1: CERRADO en s34, pero con S4A y S5 sin respaldo cuantitativo - pendiente de corrección
    Skill C2: NO EXISTE - pendiente de generación
    DR-54 (diseño de tabla): BLOQUEANTE - sin resolver
    Diplomatura UTN Parte 1: VENCE 2026-07-15 - requiere tabla de análisis para responder

2. OBJETIVOS FINALES DEL PROYECTO
Objetivo 1: Mod IRAM

    Producto: Código jugable v5.6 (bugs menores)
    Estado: CERRADO - no tocar en esta fase

Objetivo 2: Documentación del proceso

    Productos: (a) Paper C1 corregido, (b) Skill C2 operacional
    Estado: PENDIENTE

Objetivo 3: Análisis A/B + Diplomatura UTN

    Productos: (a) Base de hechos verificada, (b) Entregas Parte 1 y 2, (c) Portafolio GitHub
    Estado: EN DISEÑO - DR-54 bloquea

3. ARQUITECTURA DEL PROYECTO: LOS 3 NIVELES
IMPORTANTE: El mod IRAM no es el producto final. Es el vehículo para un proyecto de aprendizaje en 3 niveles.
Nivel 1 — Vehículo (el mod)

    Qué es: El mod IRAM para Imperator: Rome
    Propósito: Campo de práctica para aprender a usar IA en algo complejo y de largo plazo
    Valor: Bajo como producto (mod gratuito, sin usuarios reales)
    Destino: Descartable como producto, valioso como experiencia de aprendizaje

Nivel 2 — Habilidad técnica (la documentación)

    Qué es: El sistema de documentación de 5 capas (wikis ACTIVE/ARCHIVE, session logs, prompt maestro)
    Propósito: Aprender a documentar un primer proyecto real
    Valor: Alto como metodología replicable
    Destino: Parte central del portafolio y del paper

Nivel 3 — Habilidad metacognitiva (el análisis)

    Qué es: El estudio de caso de colaboración humano-IA basado en los 101 sesiones documentadas
    Propósito: Estudiar patrones de fricción y mecanismos de mitigación
    Valor: Alto como caso de estudio académico
    Destino: Trabajo de diplomatura UTN y paper

Conclusión: El valor real del proyecto está en los niveles 2 y 3, no en el nivel 1.
4. DEPENDENCIAS CRÍTICAS
DR-54 (diseño de tabla)
  ↓
Fase 1 (procesamiento de datos → tabla CSV)
  ↓
  ├──→ Fase 2 (Parte 1 UTN)
  ├──→ Fase 4 (Paper/Skill)
  └──→ Fase 3 (Parte 2 UTN)
DR-54 es el único bloqueo que impide arrancar todo lo demás.
Resuelto DR-54 → las fases 1, 2, 3 y 4 pueden ejecutarse en paralelo con supervisión.
5. FASES DE TRABAJO DETALLADAS
FASE 0 — Resolución de DR-54 (Diseño de la tabla de análisis)
Objetivo: Definir la estructura exacta de la tabla que servirá de insumo para todos los análisis posteriores y para la Entrega 1 de la UTN.
Duración estimada: 1 sesión (con operador).
Bloquea: Fases 1, 2, 3 y 4.
Tareas:
Tarea 0.1: Releer Consigna_1.md y Consigna_2.md completas

    Herramienta: Lectura
    Entregable: Notas de requisitos

Tarea 0.2: Releer sección "DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO" de SESSION_LOG_REPLANTEO_2026-07-03_02-43.md

    Herramienta: Lectura
    Entregable: Framework B repasado

Tarea 0.3: Confirmar unidad de fila → decisión codificada según Framework B

    Herramienta: Discusión
    Entregable: Definición acordada

Tarea 0.4: Definir columnas mínimas de la tabla

    Herramienta: Discusión
    Entregable: Lista de columnas

Tarea 0.5: Definir 3 preguntas de EDA (ancladas a DR-16)

    Herramienta: Discusión
    Entregable: Preguntas formuladas

Tarea 0.6: Definir enfoque de ML (clasificación) y variables de entrada

    Herramienta: Discusión
    Entregable: Enfoque definido

Tarea 0.7: Registrar decisiones en nuevo DR (DR-55)

    Herramienta: Edición
    Entregable: DR-55_TABLA_ANALISIS.md

Tarea 0.8: Definir marco conceptual para análisis de fricción

    Herramienta: Discusión
    Entregable: Definiciones operativas
    NOTA CRÍTICA: Los conceptos de "deuda técnica de interacción" y "fricción cognitiva colaborativa" son PROPUESTAS CONCEPTUALES NUEVAS generadas en la conversación del 2026-07-05. NO están documentados en los historiales previos. Son extensiones conceptuales basadas en literatura existente (Cunningham 1992 para deuda técnica, Cooper 1999 para fricción cognitiva) aplicadas al contexto de colaboración humano-IA. La decisión sobre si usar estos términos o descripciones más simples se tomará en esta tarea.

Hipótesis sobre el origen de los conceptos (a validar en Fase 1):
Hipótesis 1 — Origen de DTI (Deuda Técnica de Interacción):

    El concepto podría haber emergido de las discusiones sobre costos en tokens y gestión de contexto
    Evidencia a buscar: Conversaciones donde se discutió el tamaño del SUPERBACKUP (4160 líneas, ~80-120k tokens), optimización de contexto, y el costo de cargar documentos completos en cada sesión
    En el historial aparecen discusiones sobre "la fricción que mencioné es esto: antes de cada sesión tenés que decidir qué cargar" y análisis del costo de tokens

Hipótesis 2 — Origen de FCC (Fricción Cognitiva Colaborativa):

    El concepto podría haber emergido del primer meta-análisis de documentación de IRAM donde se examinaron numerosos niveles de investigación y documentación
    Evidencia a buscar: Conversaciones donde se analizaron las múltiples capas de documentación (Sección 0-7, 9-13, etc.), la estructura de niveles del SUPERBACKUP, y las discusiones sobre "capas que faltan" para entender el código
    En el historial aparece análisis de "las tres capas que faltan" y discusiones sobre niveles de profundidad en la documentación

Columnas propuestas (a confirmar en Fase 0):

    id (string): Identificador único (ej. A_v3_001)
    corpus (string): A o B
    fase (string): v1-v2 / v3 / v4 / v5 / doc
    origen_propuesta (string): HUMANO / IA_AC / IA_MOD / IA_RECH / EMERGENTE
    nivel_friccion (string): AT / ACCM / ACCS / RE / CS
    fecha_sesion (datetime): Timestamp de la conversación
    duracion_sesion_min (int): Duración en minutos (si está disponible)
    presencia_DR08 (boolean): ¿Hubo narrativa sin respaldo?
    costo_DR08_turnos (int): Turnos de corrección generados
    presencia_DR09 (boolean): ¿Hubo acción sin autorización?
    costo_DR09_turnos (int): Turnos o artefactos revertidos
    texto_evidencia (text): Cita textual de la decisión/diagnóstico
    contexto_previo (text): 2 mensajes anteriores (resumidos)
    contexto_posterior (text): 2 mensajes posteriores (resumidos)

Categorías de origen_propuesta (a confirmar en Fase 0):

    HUMANO: Humano propuso acción/directiva explícitamente. Ejemplo: "Hagamos una tabla con 50 logros"
    IA_AC: IA propuso proactivamente, humano aceptó sin cambios. Ejemplo: IA dice "Propongo usar eventos", Humano dice "Dale"
    IA_MOD: IA propuso, humano aceptó con modificaciones. Ejemplo: IA dice "Usemos eventos", Humano dice "Sí, pero agrega columna rareza"
    IA_RECH: IA propuso, humano rechazó. Ejemplo: IA dice "Usemos eventos", Humano dice "No, mejor tick directo"
    EMERGENTE: Decisión co-construida, no atribuible a uno solo. Ejemplo: Intercambio largo donde ambos aportan elementos

Escala de fricción (a confirmar en Fase 0):

    AT (Aceptación Total): Humano no modifica nada, solo confirma. Sobrevive 100% del código IA.
    ACCM (Aceptación con Cambio Mínimo): Cambios cosméticos (nombres, formato), no cambia lógica. Sobrevive más del 80% del código IA.
    ACCS (Aceptación con Cambios Sustantivos): Modifica lógica/condiciones, conserva arquitectura general. Sobrevive 40-80% del código IA.
    RE (Rechazo Estructural): Descarta arquitectura propuesta, cambia enfoque. Sobrevive menos del 40% del código IA.
    CS (Colapso de Sistema): Implementación falla, requiere rollback/backup. Sobrevive 0% (se descarta).

Árbol de decisión para codificación:

    ¿Aceptó sin cambios? → SÍ = AT
    ¿Cambió solo nombres/formato? → SÍ = ACCM
    ¿Se mantiene arquitectura general? → SÍ = ACCS
    ¿Hubo que restaurar backup? → SÍ = CS, NO = RE

Preguntas de EDA propuestas (a confirmar en Fase 0):

    P1: ¿Qué proporción de categorías de origen de propuesta hay en Corpus A vs. Corpus B? (Anclaje: DR-16)
    P2: ¿En qué fase del proyecto aparecen más patrones DR-08 (narrativa sin respaldo) y DR-09 (acción sin autorización)? (Anclaje: DR-08/DR-09)
    P3: ¿Cómo varía la intensidad de trabajo (sesiones/día) y los picos de fricción a lo largo del ciclo de vida del proyecto? (Anclaje: DR-05 / DR-16)

Enfoque de ML propuesto (a confirmar en Fase 0):

    Tipo: Clasificación supervisada.
    Variable objetivo: origen_propuesta (5 clases).
    Variables de entrada (features):
        Longitud del mensaje (caracteres).
        Presencia de keywords de decisión (decidir, optar, rechazar, etc.).
        Fase del proyecto.
        Corpus (A/B).
        Presencia de DR-08/DR-09 en la sesión.
        Posición del mensaje dentro de la sesión.
    Beneficio: Automatizar parcialmente la clasificación de origen de propuesta en futuros proyectos, reduciendo el tiempo de anotación manual.

FASE 1 — Procesamiento de datos (Generación de la tabla de análisis)
Objetivo: Generar tabla_analisis.csv con mínimo 50 filas, a partir de los archivos crudos.
Dependencia: Fase 0 completada.
Duración estimada: 2–3 sesiones (IA de bajo nivel).
Tareas:
Tarea 1.1: Extraer los 5 ZIPs de Corpus A y los 5 de Corpus B en carpeta de trabajo

    Herramienta: Bash / Python
    Entregable: Archivos extraídos

Tarea 1.2: Ejecutar process_iram_v2.py sobre cada ZIP para generar JSONs procesados

    Herramienta: Python
    Entregable: JSONs unificados

Tarea 1.3: Aplicar corte de evento (10/06 00:30) para separar A y B

    Herramienta: Python
    Entregable: JSONs etiquetados por corpus

Tarea 1.4: Escribir exportar_tabla_analisis.py que lea JSONs, extraiga decisiones, clasifique origen, genere CSV

    Herramienta: Python
    Entregable: tabla_analisis.csv

Tarea 1.5: Revisión manual de casos ambiguos (regla de 2 minutos: si toma más de 2 minutos, marcar como NO_CLASIFICABLE)

    Herramienta: Operador / IA
    Entregable: CSV corregido

Tarea 1.6: Verificar integridad: ≥50 filas, columnas pobladas, checksum

    Herramienta: Python / Manual
    Entregable: tabla_analisis_checksum.txt

Tarea 1.7: OBJETIVO PRINCIPAL: Encontrar el origen documental de los conceptos DTI y FCC

    Herramienta: Python + grep semántico sobre los 5 JSONs del corpus B
    Entregable: origen_conceptos_DT_FCC.md con citas textuales, fechas y sesión donde cada concepto apareció por primera vez (si es que aparece)
    Procedimiento:
        Buscar términos relacionados con DTI: "tokens", "contexto", "costo", "cargar", "ventana", "límite", "optimizar contexto", "tamaño del backup", "cuántos tokens"
        Buscar términos relacionados con FCC: "meta-análisis", "niveles", "capas", "profundidad", "documentación", "estructura", "organización", "secciones", "arquitectura de documentación"
        Para cada hit encontrado, extraer: fecha, sesión, contexto completo (5 mensajes antes y después), y clasificar si corresponde a DTI, FCC, o ambos
        Si NO se encuentran los términos exactos DTI/FCC, buscar conceptos equivalentes: "pérdida de contexto", "esfuerzo mental", "carga cognitiva", "fricción", "deuda", "costo acumulado"
        Documentar hallazgos: ¿Los conceptos estaban implícitos antes de ser nombrados explícitamente? ¿Hay evidencia de las hipótesis de origen?

FASE 2 — Entrega Parte 1 de la diplomatura UTN
Objetivo: Redactar el documento de la Parte 1 siguiendo Consigna_1.md.
Dependencia: Fase 1 completada.
Duración estimada: 1 sesión de redacción + 1 de revisión.
Fecha límite: 2026-07-15.
Tareas:
Tarea 2.1: Cargar tabla_analisis.csv en Excel / Google Sheets

    Herramienta: Excel / Sheets
    Entregable: Dataset visible

Tarea 2.2: Generar 2 gráficos profesionales para las preguntas P1 y P3

    Herramienta: Excel / Sheets
    Entregable: Gráficos (imágenes)

Tarea 2.3: Redactar respuestas a las 3 preguntas de EDA

    Herramienta: Word / Markdown
    Entregable: Texto de análisis

Tarea 2.4: Redactar propuesta conceptual de ML (clasificación)

    Herramienta: Word / Markdown
    Entregable: Texto de propuesta

Tarea 2.5: Integrar todo en documento con título, contexto, capturas, preguntas, gráficos, propuesta ML

    Herramienta: Word / PDF
    Entregable: Entrega1_IRAM_UTN.pdf

Tarea 2.6: Revisar ortografía, formato, requisitos de mínimo 50 filas

    Herramienta: Manual
    Entregable: Documento final

FASE 3 — Entrega Parte 2 de la diplomatura UTN
Objetivo: Diseñar prototipo de IA generativa / automatización y reflexión ética.
Dependencia: Fase 2 completada (puede avanzar en paralelo parcialmente).
Duración estimada: 2 sesiones.
Tareas:
Tarea 3.1: Diseñar flujo de trabajo: Entrada (decisión) → Proceso IA (clasificación) → Salida (diagnóstico)

    Herramienta: Diagrama
    Entregable: Esquema visual (captura)

Tarea 3.2: Diseñar prompt avanzado para asistente IA que clasifique origen de propuesta

    Herramienta: ChatGPT / Claude
    Entregable: Prompt exacto

Tarea 3.3: Probar prompt con 2 ejemplos reales de la tabla

    Herramienta: ChatGPT / Claude
    Entregable: Capturas de pantalla

Tarea 3.4: Definir métrica de éxito (ej. reducción de tiempo de anotación)

    Herramienta: Manual
    Entregable: Métrica definida

Tarea 3.5: Redactar reflexión ética: privacidad, sesgo, necesidad de validación humana

    Herramienta: Manual
    Entregable: Texto de reflexión

Tarea 3.6: Integrar en documento siguiendo Consigna_2.md

    Herramienta: Word / PDF
    Entregable: Entrega2_IRAM_UTN.pdf

FASE 4 — Corrección del Paper C1 y generación de Skill C2
Objetivo: Usar la tabla de análisis para corregir las afirmaciones de autoría (S4A, S5) y extraer una skill operacional.
Dependencia: Fase 1 completada.
Duración estimada: 2 sesiones.
Tareas:
Tarea 4.1: Analizar distribución de categorías de origen de propuesta en la tabla

    Herramienta: Python / Excel
    Entregable: Estadísticas

Tarea 4.2: Revisar S4A del paper: contrastar con datos

    Herramienta: Edición
    Entregable: IRAM_C1_final_corregido.md

Tarea 4.3: Revisar S5: separar ratio de producción de origen real, añadir limitación explícita

    Herramienta: Edición
    Entregable: IRAM_C1_final_corregido.md

Tarea 4.4: Aplicar tareas A, C, E, F del paper

    Herramienta: Edición
    Entregable: IRAM_C1_final_corregido.md

Tarea 4.5: Agregar sección S4B: Mecanismos de documentación como respuesta a problemas prácticos

    Herramienta: Edición
    Entregable: IRAM_C1_final_corregido.md
    NOTA: Esta sección describe los mecanismos de documentación (wikis ACTIVE/ARCHIVE, session logs, prompt maestro) que EMERGIERON como respuesta a problemas prácticos observados durante el desarrollo (pérdida de contexto, acciones sin autorización, etc.). NO presenta estos mecanismos como solución a conceptos teóricos predefinidos. Los conceptos teóricos (si se usan) son etiquetas posteriores para describir los problemas observados.

Tarea 4.6: Generar Skill C2 (~40-60 líneas) extrayendo reglas directas de la tabla

    Herramienta: Edición
    Entregable: IRAM_skill_C2_v1.md

Sección S4B propuesta (a redactar en Fase 4):
S4B — Mecanismos de mitigación: la documentación como respuesta adaptativa

    Origen de los mecanismos: Las herramientas de documentación (WIKI ACTIVE/ARCHIVE, SESSION_LOG, PROMPT_MAESTRO) no fueron diseñadas a priori. Emergieron como respuesta adaptativa a fricciones y deudas técnicas de interacción acumuladas durante el desarrollo.
    Tabla de correspondencia tensión → respuesta:

    Pérdida de contexto entre sesiones: IA pierde contexto, hay que re-explicar → SUPERBACKUP → WIKI ACTIVE → Primera aparición: [cita del historial]
    Propuestas ya descartadas: IA propone soluciones ya rechazadas → WIKI ARCHIVE + Sección 19 → Primera aparición: [cita]
    Acciones sin autorización: IA modifica sin permiso → PROMPT_MAESTRO con reglas R → Primera aparición: [cita]
    Sesiones cortadas: Se pierde trabajo al cortar sesión → SESSION_LOG → Primera aparición: [cita]
    Alucinaciones: IA inventa datos → Reglas de verificación en PROMPT → Primera aparición: [cita]

    Sugerencias para futuros proyectos:
    Documentación viva desde día 1: No esperar a que la fricción aparezca.
    Separación ACTIVE/ARCHIVE: Conocimiento vigente e histórico en archivos separados.
    Log de decisiones abiertas: Documentar explícitamente qué quedó sin resolver.
    Reglas de agencia explícitas: Definir qué puede y qué no puede hacer la IA sin autorización.
    Protocolo de corte de sesión: Instruir a la IA para sugerir generar log al acercarse al límite.
    Auditorías periódicas: Comparar lo documentado vs lo implementado cada N sesiones.

FASE 5 — Tareas de limpieza y cierre (no urgentes)
Objetivo: Resolver pendientes estructurales y de organización.
Tareas:
Tarea 5.1: Ejecutar plan de 3 capas de DR-32 sobre 2_DOCUMENTACION/07_fuentes_documentacion/

    Herramienta: Bash / Python
    Entregable: Archivos renombrados + guía maestra

Tarea 5.2: Decidir destino de _CUARENTENA_DUPLICADOS/ (borrar o conservar)

    Herramienta: Operador
    Entregable: Decisión registrada

Tarea 5.3: Inventario terminológico (DR-35a)

    Herramienta: Búsqueda web
    Entregable: Tabla terminológica

Tarea 5.4: Verificación de cifras de hitos (DR-35b)

    Herramienta: Lectura
    Entregable: Cita exacta

Tarea 5.5: Cierre del tema memoria en claude_5

    Herramienta: Manual
    Entregable: Registro de cierre

6. CRONOGRAMA TENTATIVO

    Fase 0: DR-54 (diseño de tabla) → Fecha límite: 2026-07-06 → Responsable: Operador + IA
    Fase 1: Procesamiento → CSV + rastreo de origen → Fecha límite: 2026-07-08 → Responsable: IA de bajo nivel
    Fase 2: Entrega Parte 1 UTN → Fecha límite: 2026-07-12 → Responsable: IA + Operador (revisión)
    Fase 3: Entrega Parte 2 UTN → Fecha límite: 2026-07-20 → Responsable: IA + Operador
    Fase 4: Paper C1 + Skill C2 → Fecha límite: 2026-07-25 → Responsable: IA de bajo nivel
    Fase 5: Limpieza y cierre → Fecha límite: Sin fecha → Responsable: Según disponibilidad

7. ENTREGABLES ESPERADOS (POR FASE)

    Fase 0: DR-55_TABLA_ANALISIS.md (formato Markdown)
    Fase 1: tabla_analisis.csv + tabla_analisis_checksum.txt + origen_conceptos_DT_FCC.md (formatos CSV + TXT + MD)
    Fase 2: Entrega1_IRAM_UTN.pdf (formato PDF)
    Fase 3: Entrega2_IRAM_UTN.pdf (formato PDF)
    Fase 4: IRAM_C1_final_corregido.md + IRAM_skill_C2_v1.md (formato Markdown)
    Fase 5: Archivos renombrados, tabla terminológica, etc. (formatos varios)

8. NOTAS OPERATIVAS PARA LA IA DE BAJO NIVEL

    Convención de nombres: AAAA-MM-DD_HH-MM (DR-24). Siempre preguntar la hora al operador antes de nombrar un archivo.
    Reproducibilidad: cada script debe incluir checksum del input y fecha de ejecución (DR-16).
    Logs: cada paso debe generar un log breve (qué se hizo, qué archivos se generaron, errores encontrados).
    Casos ambiguos: cuando la clasificación automática no sea clara, marcar para revisión manual. Si la revisión toma más de 2 minutos, marcar como NO_CLASIFICABLE.
    No tocar el mod: 1_MOD/ está fuera de alcance – solo se usan los archivos de corpus.
    Tono académico: el trabajo es un estudio de caso exploratorio. Usar lenguaje descriptivo ("observamos", "documentamos", "en este caso se manifiesta como"), no claims de novedad o revolución.
    CRÍTICO para Tarea 1.7: Al buscar el origen de los conceptos, NO asumir que los términos exactos "DTI" o "FCC" aparecen en los historiales. Buscar conceptos equivalentes y patrones de discusión. Documentar honestamente si se encuentran o no.

9. PRÓXIMO PASO INMEDIATO
Iniciar Fase 0: sesión de diseño para resolver DR-54.
Materiales necesarios:

    Consigna_1.md y Consigna_2.md
    SESSION_LOG_REPLANTEO_2026-07-03_02-43.md (sección de métricas y Framework B)
    SESSION_LOG_REPLANTEO_2026-07-05_01-37.md (DR-52, DR-53, DR-54)

ANEXO A — ESTRUCTURA DE CARPETAS ACTUAL
IRAM PROYECTO/
├── 1_MOD/ (1320 archivos – fuera de alcance)
│   ├── game/
│   ├── IRAM mod v5/
│   ├── IRAM_legacy v1 v2 v3 v4/
│   ├── corpus_A_crudo/ (5 data--batch-0000.zip)
│   ├── achievements_imperator.xlsx
│   └── wiki_imperator.txt
│
├── 2_DOCUMENTACION/ (241 archivos)
│   ├── 01_logs_replanteo/
│   ├── 02_charlas_y_resumenes/
│   ├── 03_prueba_fuga_memoria/
│   ├── 04_corpus_A_mod_docs/
│   ├── 05_corpus_B_crudo/
│   ├── 06_historial_desarrollo_mod/
│   ├── 07_fuentes_documentacion/
│   └── 08_documentacion_respaldo/
│
├── 3_PORTAFOLIO_UTN/ (6 archivos)
│   └── consignas/
│
└── _CUARENTENA_DUPLICADOS/ (424 archivos)
ANEXO B — CONCEPTOS TEÓRICOS
Declaración de co-autoría:
Los conceptos de [nombre final Concepto 1] y [nombre final Concepto 2] fueron propuestos por el sistema de IA durante la conversación del 2026-07-05, y validados críticamente por el investigador humano. Esta co-construcción es consistente con el objeto de estudio del trabajo: la colaboración humano-IA en proyectos de largo plazo.
Hipótesis sobre el origen de los conceptos (a validar en Tarea 1.7):
Hipótesis 1 — DTI (Deuda Técnica de Interacción):

    Podría haber emergido de discusiones sobre costos en tokens y gestión de contexto
    Evidencia preliminar en historial: discusiones sobre tamaño del SUPERBACKUP (4160 líneas, ~80-120k tokens), optimización de contexto, costo de cargar documentos completos

Hipótesis 2 — FCC (Fricción Cognitiva Colaborativa):

    Podría haber emergido del primer meta-análisis de documentación de IRAM donde se examinaron numerosos niveles de investigación y documentación
    Evidencia preliminar en historial: análisis de múltiples capas de documentación (Sección 0-7, 9-13), discusiones sobre "las tres capas que faltan", análisis de niveles de profundidad

Definiciones operativas provisorias:
Concepto 1 (provisorio: DTI - Deuda Técnica de Interacción): Costo acumulado de interacciones subóptimas con la IA que generan trabajo correctivo futuro.
Concepto 2 (provisorio: FCC - Fricción Cognitiva Colaborativa): Esfuerzo mental extra que el humano debe realizar para compensar las limitaciones de la IA.
Relación causal: El Concepto 2 es la causa, el Concepto 1 es el efecto.
Citas bibliográficas de referencia:

    Cunningham, Ward (1992). "The WyCash Portfolio Management System". OOPSLA 92.
    Cooper, Alan (1999). "The Inmates Are Running the Asylum".
    Gulliksen, J., et al. (2003). "Cognitive Friction in Human-Computer Interaction".

ANEXO C — COMPARACIÓN CON SISTEMAS ENTERPRISE
Sistemas enterprise (automatizados):

    RAG (Retrieval-Augmented Generation): Busca información relevante automáticamente.
    Vector Databases + Embeddings: Búsqueda semántica a escala.
    Fine-tuning: Modelo especializado con documentos del proyecto.
    Context Management Systems: Decide automáticamente qué contexto cargar.
    Memory Layers: Mantiene memoria persistente entre sesiones.

Sistema manual IRAM (5 capas):

    TECHNICAL_WIKI ACTIVE: Archivo markdown con todo lo vigente.
    TECHNICAL_WIKI ARCHIVE: Archivo markdown con histórico.
    PROMPT_MAESTRO: Instrucciones permanentes.
    SESSION_LOG: Registro de cada sesión.
    (SUPERBACKUP fue el sistema anterior monolítico, reemplazado por wikis separadas)

Diferencias clave:

    Automatización: Enterprise → Sistema decide; IRAM → Humano decide
    Escalabilidad: Enterprise → Millones de documentos; IRAM → Miles de líneas
    Costo infraestructura: Enterprise → $100-$10,000/mes; IRAM → $0
    Costo humano: Enterprise → Bajo; IRAM → Alto
    Control: Enterprise → Rígido, opaco; IRAM → Flexible, transparente
    Aprendizaje: Enterprise → Bajo; IRAM → Alto

ANEXO D — EVALUACIÓN HONESTA DEL PROYECTO
Importancia académica: Media-Alta
Fortalezas:

    Estudio de caso longitudinal riguroso (6 meses, 101 sesiones)
    Dataset empírico raro
    Metodología replicable
    Métricas operacionales
    Mecanismos de mitigación documentados

Limitaciones:

    N=1
    Sin grupo de control
    Sesgo de autoetnografía
    No generalizable estadísticamente

Importancia económica: Media
Valor real:

    Habilidades adquiridas
    Credencial académica
    Metodología documentada
    Skill de automatización (potencial)

Valor como portafolio: Alto (con enfoque correcto)
Presentar como:

    "Desarrollé un proyecto complejo de 6 meses trabajando 100% con IA generativa"
    "Documenté 101 sesiones de colaboración para estudiar patrones de fricción humano-IA"
    "Creé un sistema de documentación de 5 capas que evolucionó orgánicamente bajo presión"

No presentar como:

    "Hice un mod de Imperator: Rome" (eso es el vehículo, no el producto)

Fin del plan integrado.
Próxima acción: Iniciar Fase 0 con los materiales necesarios para resolver DR-54. La Tarea 1.7 será crítica para validar o refutar las hipótesis sobre el origen de los conceptos DTI y FCC.