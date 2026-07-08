# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 5 — Los datos del proceso

*Draft s28 — 2026-06-17*

---

Las secciones anteriores describieron cómo funciona el sistema. Esta sección documenta si funcionó — con los números del proceso real.

Los datos vienen del historial completo: 336 conversaciones IRAM, 7345 mensajes post-deduplicación, 5 cuentas, procesados desde los archivos de exportación originales. Cuatro métricas, todas calculadas sobre el mismo corpus.

---

### El sistema se volvió más rápido mientras el problema se volvía más complejo

La velocidad de trabajo aumentó de forma monótona a lo largo del proyecto, sin excepción por fase:

| Fase | Días | Conv/día | Msg/conv | Costo de arranque (mediana) |
|------|------|----------|----------|-----------------------------|
| v1-v2 | 13 | 1.8 | 37.0 | 14 mensajes |
| v3 | 30 | 5.1 | 24.4 | 9 mensajes |
| v4 | 13 | 7.2 | 22.3 | 7 mensajes |
| v5 | 7 | 9.4 | 9.6 | 5 mensajes |

"Costo de arranque" es el número de mensajes antes del primer output productivo (primer `create_file` o `str_replace`) en las conversaciones que tuvieron trabajo concreto. Cayó de 14 mensajes en v1-v2 a 5 en v5.

Eso no se explica porque v5 fuera más simple. El alcance del mod en v5 era mayor que en cualquier versión anterior — cuatro módulos independientes con namespace propio, después de un rediseño completo desde v4. Lo que cambió fue el costo de inicializar el contexto: el SESSION_LOG de v5 era una especificación ejecutable; el operador en v1-v2 todavía estaba explicando el proyecto desde cero en cada sesión.

La duración mediana de conversación cayó en la misma dirección: de 3757 minutos en v1-v2 a 60 en v5. El número no refleja abandono de trabajo largo — refleja que cada sesión tenía un alcance más acotado y arrancaba con más contexto estructurado.

---

### La investigación creció más rápido que el código — y eso es evidencia de planificación

El ratio entre operaciones de investigación (leer archivos, verificar estado, inspeccionar el motor) y operaciones de código (crear o modificar archivos) creció de forma consistente:

| Fase | Ratio Inv/Cód |
|------|---------------|
| v1-v2 | 1.8x |
| v3 | 2.0x (+12%) |
| v4 | 2.4x (+22%) |
| v5 | 2.9x (+22%) |

Una lectura posible es que el proyecto tuvo más bugs en las fases tardías. Los datos la descartan: las operaciones categorizadas como respuesta a errores se mantuvieron estables entre 1% y 3% en todas las fases. El tipo de investigación que creció fue distinto.

En v1-v2 y v3, la mayor parte de la investigación era exploración de mecánicas del juego — grep por términos como `heir_weight`, `succession`, `treasury`. Buscar cómo funciona el motor. En v4 y v5, ese tipo desapareció casi por completo y fue reemplazado por investigación sobre la estructura del propio proyecto: verificar el estado de archivos, confirmar que los cambios anteriores habían quedado bien, auditar antes de avanzar. Las sesiones de mayor investigación en v5 tienen nombres como "audit 5.2", "Confirmación de cambios en archivos IRAM", "Plan de ejecución unificado v5.0" — planificación y verificación deliberadas, no debugging reactivo.

El ratio creciente no refleja un proyecto con más problemas. Refleja un proyecto donde verificar antes de modificar se volvió parte del proceso.

---

### El operador escribió más — y Claude produjo más por palabra

Dos indicadores del cambio en la división de trabajo:

La longitud promedio de los mensajes del operador creció de 108 caracteres en v3 a 183 en v5 — un 70% de aumento. En paralelo, el porcentaje de mensajes del operador con lenguaje explícito de decisión y diseño subió de 4.5% en v3 a 7.0% en v5. El operador en v5 no estaba escribiendo más para explicar más: estaba especificando más antes de ejecutar.

El ratio de producción de Claude — caracteres producidos por carácter recibido del operador — fue de 7.4x en v1-v2 y de 9.9x en v4 y v5. Claude produjo proporcionalmente más texto por unidad de input del operador en las fases tardías que en las tempranas. Eso es consistente con el argumento de la sección 4A: en las fases maduras, el operador entregaba especificaciones más precisas, y Claude ejecutaba contra ellas con menos iteración de ajuste.

El porcentaje de mensajes de Claude con lenguaje de decisión y diseño también subió: de 48% en v3 a 66% en v5. Ese número refleja que Claude generaba más texto de tipo razonamiento y planificación en v5 — lo que corresponde a sesiones de auditoría y verificación, no de codificación mecánica.

---

### El tamaño de las entregas creció con la madurez

La longitud promedio de los mensajes de Claude creció de 983 caracteres en v1-v2 a 1659 en v5 — un 69% de aumento. Más entrega por mensaje en las fases tardías.

Eso se puede leer de dos formas. Una: Claude se volvió más prolijo. Otra: las tareas de v5 eran más complejas per mensaje, precisamente porque el sistema de tiering separaba diseño de ejecución — y cuando Claude ejecutaba, lo hacía contra especificaciones que requerían outputs más completos y estructurados.

Los dos efectos probablemente coexisten. Lo que los datos permiten afirmar con certeza es que la productividad agregada creció: más conversaciones por día, menos mensajes por conversación, más output por mensaje. El sistema produjo más en menos tiempo con sesiones más cortas y mejor acotadas.

---

### Lo que los datos no cubren

Dos métricas que habrían completado este cuadro no están disponibles:

La distribución de autoría real dentro de las decisiones de diseño — qué fracción de las propuestas de arquitectura vino del operador versus fue generada por Claude y aceptada. El análisis de texto captura el lenguaje de decisión en los mensajes, pero no puede distinguir sistemáticamente quién inició la propuesta. Resolver eso requeriría anotación manual de una muestra.

La complejidad técnica por fase como variable independiente del esfuerzo. El análisis actual usa el esfuerzo (mensajes, tiempo, herramientas) como proxy de complejidad, pero complejidad y esfuerzo no son lo mismo. Una especificación más corta que habilita código más complejo es exactamente el efecto que buscaba medir T1 — pero medirlo directamente requeriría una métrica de complejidad del código producido que este análisis no tiene.

Lo que sí está disponible — velocidad, costo de arranque, ratio investigación/código, densidad de lenguaje de diseño — converge en la misma dirección: el sistema mejoró su throughput de forma consistente a lo largo del proyecto, y los indicadores de planificación deliberada crecieron junto con esa mejora, no a pesar de ella.

---

*Sección 5 — draft s28 — 2026-06-17*
