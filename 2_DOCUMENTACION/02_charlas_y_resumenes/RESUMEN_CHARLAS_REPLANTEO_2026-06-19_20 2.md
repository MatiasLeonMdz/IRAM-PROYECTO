# RESUMEN DE CHARLAS — Replanteo del proyecto IRAM/Documentación
**Cubre:** Charla 1 (19/06 sesión 1), Charla 2 (19/06 sesión 2), Charla 3 (20/06)
**Propósito:** Contexto de razonamiento detrás de las decisiones del SESSION_LOG. Cargar solo si hace falta entender por qué se tomó una decisión — no como punto de partida operativo.
**Punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-06-20.md
**Archivos fuente:** CHARLA_REPLANTEO_1.md, CHARLA_REPLANTEO_2.md, transcripción sesión 20/06

---

## CHARLA 1 — 19/06, Sesión 1

### Qué detonó el replanteo
El operador llegó con un diagnóstico claro: la frase "la IA no democratiza la programación" había infectado la documentación, y la pregunta de autoría (quién resolvió qué) había sido "mal entendida" por la IA. No era una corrección puntual — era un error de proceso que requería replantear el análisis completo.

### Los dos errores: mecanismo exacto

**Error 1 — Argumento no verificado promovido a "definitivo" por copia:**
- La frase de democratización nació en el esqueleto s17 (16/06) como "ARGUMENTO CENTRAL — confirmar al cierre".
- En WIKI_DOCUMENTACION_v1.md (17/06 17:13) aparece como "PRINCIPIO CENTRAL DEL PAPER (definitivo)" sin paso intermedio de confirmación.
- Se copió a TEMPLATES_DOCUMENTACION_v1.md y WIKI_DOCUMENTACION_v2.md sin tocar.
- El paper real (IRAM_C1_final.md, cerrado en s34) nunca usó la frase — el hallazgo central real fue "la posición y el formato importan más que el contenido" (Sección 3).
- El error no fue creer en la democratización — fue que una etiqueta de estado ("definitivo") reemplazó la verificación, y la etiqueta pesó más que el contenido que supuestamente reflejaba.

**Error 2 — Pregunta sin métrica directa contestada con proxy:**
- La pregunta real: "¿quién originó cada decisión?"
- En s28, se calculó ratio de caracteres (Claude/operador: 7.4x en v1-v2 → 9.9x en v5) y densidad de "palabras de decisión". T2 quedó ✅.
- Ese ratio mide volumen de output, no autoría. Es compatible con cualquier hipótesis sobre quién decidió.
- El paper cerrado lo incluyó en S5, donde convive sin que nadie lo note con el propio caveat del paper dos párrafos después: "la autoría real no es recuperable del análisis de texto".
- Mismo mecanismo que Error 1: ✅ reemplazó verificación.

### Por qué DR-01 a DR-09 son lo que son
- **DR-01** (dos corpus paralelos): los errores venían de mezclar la historia del mod con la historia de la documentación en un solo análisis.
- **DR-02** (C2 no depende de C1): la dependencia C1→C2 era el camino por el que la narrativa contaminada del paper llegaba a la skill. Cortarla elimina el vector de contagio.
- **DR-03** (detención en el punto difícil como evidencia): el operador frenó el proyecto en documentación, no en el tramo fácil. Eso es dato, no accidente.
- **DR-04** (dos corpus con estado diferente): Corpus A disponible, Corpus B pendiente de agrupación.
- **DR-05** (ciclo de vida de la documentación como hallazgo): simple→complejo→intento de vuelta a simple es el arco completo, no una lista de incidentes.
- **DR-06** (categoría 4B como primera clase): el script excluía exactamente los casos que el paper ya identificó como evidencia más fuerte (INC-13, panel de interfaz, filtro de escala global).
- **DR-07** (inventario antes de bajar estatus): generalización del mecanismo que falló — ninguna baja de estatus sin inventario ítem por ítem.
- **DR-08** (costo narrativo no solicitado): instancias verificadas en la propia sesión de la IA produciendo estados internos inventados y mérito propio.
- **DR-09** (acción sin autorización): instancias verificadas en la propia sesión de la IA editando el log sin instrucción explícita.

**Para el detalle completo:** CHARLA_REPLANTEO_1.md

---

## CHARLA 2 — 19/06, Sesión 2

### Investigación de novedad — resultados
Se verificó ítem por ítem qué componentes del proyecto tienen equivalente publicado. Resultado: la arquitectura (tres capas, ACTIVE/ARCHIVE, separación diseño/ejecución, HITL, ADRs, cognitive microservices) no es novedosa — todo tiene nombre formal. Lo que no se encontró equivalente publicado es el caso específico: un proyecto donde el instrumento de análisis reprodujo en vivo la falla que estaba diagnosticando, con evidencia trazable hora por hora. Ese caso quedó como "ausencia en las fuentes revisadas el 19/06, no confirmado como novedad real" — requiere búsqueda más profunda antes de afirmarlo en el paper.

**Conclusión para el proyecto:** el valor defendible es el caso documentado y su trazabilidad, no la arquitectura.

### Por qué el análisis comparativo A/B
La pregunta más interesante no es "qué pasó en el mod" ni "qué pasó en la documentación" por separado — es si el comportamiento del sistema operador+IA fue distinto en tarea técnica (código) vs. tarea metodológica (documentar cómo documentar). Eso requiere los dos corpus con las mismas métricas.

### Estado al cierre de sesión 2
Las dos decisiones que quedaron sin resolver: (a) arrancar con Corpus A o esperar Corpus B; (b) nomenclatura de prefijos. Ninguna se resolvió — se trasladaron al log del 20/06 como próximo paso inmediato.

**Para el detalle completo:** CHARLA_REPLANTEO_2.md

---

## CHARLA 3 — 20/06

### Evaluación del operador
Se evaluó el desempeño del operador con evidencia de los archivos, no como valoración general. Hallazgos verificados con fuente primaria:
- Primer proyecto documentado, primer código de escala real, sin formación formal en el área.
- Detectó los dos errores sistémicos rastreando hasta fuente primaria, sin conocer los nombres técnicos.
- El trabajo cuantitativo del mod (modelo económico, grid search de 17 combinaciones, simuladores Optimize) tiene equivalente directo en data science con nombre formal, aunque llegó por fricción sin conocerlo.
- El criterio para detectar cuando algo está mal (abrir un ✅ y preguntar si realmente está cerrado) es sólido y está verificado en múltiples instancias.
- Límite real: el diseño preventivo (anticipar problemas antes de que la fricción los fuerce) es lo que falta construir — el proyecto mismo es ese aprendizaje.

### Contexto de data science incorporado al proyecto
- El objetivo de data science estaba en el STRATEGIC LOG del 27/05 ("objetivo real: ciencia de datos — el modding es el camino ameno") pero nunca había entrado al sistema operativo del replanteo. Esta sesión lo incorporó como DR-10.
- La diplomatura UTN es no-code/low-code — no cubre stack técnico. El certificado tiene valor pero no alcanza solo para un rol técnico remoto.
- El Corpus A/B resuelve el problema más común del candidato entry-level: no tener nada real que mostrar.
- Timeline tentativo: noviembre/diciembre 2026, condicionado a números reales del Corpus A.

### Revisión metodológica del log — los 9 problemas encontrados

El operador pidió revisar el plan buscando fallas. Se encontraron 9:

**Resueltos en la misma sesión:**
1. Timeline con meses específicos pero sin repetir el caveat de DR-18 → corregir en el log: "(condicionado — ver DR-18)" en cada fila.
2. "Distribución por fase" y "Velocidad de respuesta" en Grupo 1 requieren anotación → mover a Grupo 2.
3. Números 6/7 de hitos sin verificación de línea → marcar como "pendiente verificación con cita en hitos_v7".
4. Categorías de Grupo 2 sin definición operacional → debatido y resuelto con Framework B (ver abajo).
5. DR-08/DR-09 sin unidad de conteo → rediseñado como métricas de frecuencia, costo y distribución (ver abajo).
6. Corpus A/B sin métricas normalizadas para comparación → tabla de normalización por tipo de pregunta (ver abajo).
7. "Búsqueda más profunda" de DR-13 sin plan → diseñado con fuentes, términos y umbral (ver abajo).
8. Portfolio sin definición de entregable → GitHub repo + README dual + paper enlazado + LinkedIn post al cierre.
9. "El 95%" de DR-20 sin fuente → reemplazar por "la mayoría" + "(estimación sin fuente)".

### Framework B — definición operacional de autoría (reemplaza Framework A)
El problema con "propuesta aceptada/rechazada" es que es un proxy de supervivencia de texto — el mismo error de T2.

**Framework B — autoridad de decisión:**
- ¿Quién fijó la dirección antes de que se implementara?
- Si la modificación del operador cambió la dirección → operador tomó la decisión.
- Si la modificación fue ajuste de detalle sin cambiar la dirección → IA tomó la decisión.
- La zona gris ("modificada") desaparece: el criterio es la dirección, no el texto.

Categorías resultantes: OP_ARCH, IA_PROP_AC, IA_PROP_RJ, COLAB, IA_DIAG_OP_DEC.

### Métricas rediseñadas para DR-08 y DR-09
No son conteos simples — son patrones con evidencia de impacto:
- **Frecuencia:** instancias por cada 100 mensajes de IA (tasa normalizada)
- **Costo DR-08:** turnos de corrección generados por cada instancia
- **Costo DR-09:** trabajo rehecho o revertido (turnos o artefactos afectados)
- **Distribución:** en qué fases/tipos de tarea aparece más cada categoría

### Tabla de normalización para comparación A/B
| Pregunta | Normalización |
|----------|--------------|
| Intensidad (tiempo, volumen) | Por día calendario |
| Comportamiento típico de sesión | Por sesión/conversación |
| Autoría | Por decisión codificada |
| DR-08 frecuencia | Por 100 mensajes de IA |
| DR-08 costo | Turnos de corrección por instancia |
| DR-09 frecuencia | Por 100 mensajes de IA |
| DR-09 costo | Turnos o artefactos revertidos por instancia |

### Inventario terminológico — diseño
Decisión expandida: no solo buscar novedad del proyecto, sino inventariar el nombre formal de **todos** los mecanismos, herramientas, procesos y análisis del proyecto. Formato: tabla con nombre/descripción/nombre formal/fuente/terminología temporal propuesta si no tiene nombre.

Del 19/06, lo que ya tiene nombre verificado: HITL, Specification-driven development, Cognitive microservices, Three-tier agentic architecture, Active/archive storage, ADR, ETL, RAG, Grid search, Interrupted time series, Stale specs, Proxy substitution, Premature completion claims, Namespace pollution, coupling, monolith.

Sin nombre verificado — buscar: sistema de 4 documentos como handoff entre sesiones, ciclo bug→patrón→regla→documento, ciclo simple→complejo→intento de vuelta a simple, Framework B (autoridad de decisión), DR-08 (narrativa sin respaldo), DR-09 (acción sin autorización), el caso reflexivo (instrumento reproduce la falla que diagnostica).

Plan de búsqueda: ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, Papers With Code, Anthropic/OpenAI/DeepMind publications, grey literature (Lilian Weng, Simon Willison, repositorios GitHub metodológicos). Mínimo 5 queries independientes por ítem, 3 idiomas (español, inglés, portugués). Umbral: 5 búsquedas + 2 fuentes grises sin resultado equivalente. Terminología temporal con estructura `[Adjetivo descriptor]-[Sustantivo del fenómeno]`, marcada `[TEMP]` en todos los documentos.

**Esta búsqueda es una sesión de trabajo separada.**

### Tres agregados al diseño del análisis
**A — Unidad "sesión":** sesión = conversación individual de Claude = charla. Sinónimos. Unidad directamente extraíble del JSON por conversation_id.

**B — Corte de Corpus B:** definido por el evento, no por fecha. El día en que se detuvo simultáneamente el desarrollo del mod y sus herramientas (wiki-active, archive, log) y se pasó a documentar el proceso. El operador tiene ese evento registrado en el nombre de la carpeta de archivos — esa es la fuente del corte, no un timestamp del log.

**C — Versionado del análisis:** nombre del script + fecha de ejecución + hash o checksum del input. Sin esto el análisis no es reproducible.

**Para el detalle completo:** transcripción de la sesión del 20/06 (esta sesión).

---

## PRÓXIMAS TAREAS DE DISEÑO — en orden de prioridad

1. **Inventario completo del material de archivo disponible.** Antes de diseñar el análisis en detalle, hacer un inventario ítem por ítem de todo el material existente: qué archivos hay, qué contiene cada uno, qué estado tiene (vigente/histórico/pendiente), y qué corpus corresponde a cada uno (A, B, o ninguno). Sin este inventario, el diseño del análisis trabaja sobre una lista parcial de insumos.

2. **Inventario terminológico completo** — sesión dedicada con el plan de búsqueda definido arriba.

3. **Correcciones al SESSION_LOG** de los 9 puntos encontrados en la revisión metodológica.

4. **Decisión pendiente desde el 19/06:** arrancar con Corpus A ahora o esperar Corpus B. Preguntar al operador al abrir la próxima sesión.

---

*Este resumen no reproduce las decisiones — esas están en el SESSION_LOG. Reproduce el razonamiento que las generó.*
