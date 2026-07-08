# IRAM — Nuevo C1: "Qué aprendimos sobre cómo funciona la IA"
## Sección 5 — Los datos del proceso

*Draft s29 — revisión de s28 — 2026-06-17*

---

Las secciones anteriores describieron cómo funciona el sistema. Esta sección documenta si funcionó — con los números del proceso real.

Los datos vienen del historial completo: 336 conversaciones IRAM, 7345 mensajes post-deduplicación, 5 cuentas, procesados desde los archivos de exportación originales. Cuatro métricas, todas calculadas sobre el mismo corpus.

---

### El sistema se volvió más rápido mientras el problema se volvía más complejo

La velocidad de trabajo aumentó de forma monótona a lo largo del proyecto, sin excepción por fase:

| Fase | Días | Conv/día | Msg/conv | Costo de arranque (mediana) |
|------|------|----------|----------|------------------------------|
| v1-v2 | 13 | 1.8 | 37.0 | 14 mensajes |
| v3 | 30 | 5.1 | 24.4 | 9 mensajes |
| v4 | 13 | 7.2 | 22.3 | 7 mensajes |
| v5 | 7 | 9.4 | 9.6 | 5 mensajes |

"Costo de arranque" es el número de mensajes antes del primer output productivo (primer `create_file` o `str_replace`) en las conversaciones que tuvieron trabajo concreto. Cayó de 14 mensajes en v1-v2 a 5 en v5.

Eso no se explica porque v5 fuera más simple. El alcance del mod en v5 era mayor que en cualquier versión anterior — cuatro módulos independientes con namespace propio, después de un rediseño completo desde v4. Lo que cambió fue el costo de inicializar el contexto: el SESSION_LOG de v5 era una especificación ejecutable; el operador en v1-v2 todavía estaba explicando el proyecto desde cero en cada sesión. La duración mediana de conversación cayó en la misma dirección: de 3757 minutos en v1-v2 a 60 en v5. No porque el trabajo fuera menos — porque cada sesión arrancaba con más contexto estructurado y tenía un alcance más acotado.

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

En v1-v2 y v3, la mayor parte era exploración de mecánicas del juego — grep por términos como `heir_weight`, `succession`, `treasury`. Buscar cómo funciona el motor. En v4 y v5, ese tipo desapareció casi por completo y fue reemplazado por investigación sobre la estructura del propio proyecto: verificar el estado de archivos, confirmar que los cambios anteriores habían quedado bien, auditar antes de avanzar. Las sesiones de mayor investigación en v5 tienen nombres como "audit 5.2", "Confirmación de cambios en archivos IRAM", "Plan de ejecución unificado v5.0" — planificación y verificación deliberadas, no debugging reactivo.

El ratio creciente no refleja un proyecto con más problemas. Refleja un proyecto donde verificar antes de modificar se volvió parte del proceso.

---

### La división de trabajo maduró: el operador especificó más, Claude produjo más por palabra

El argumento de la sección 4A — que la calidad del output de Claude depende de la calidad de la especificación — tiene correlato cuantitativo en las fases tardías del proyecto.

La longitud promedio de los mensajes del operador creció de 108 caracteres en v3 a 183 en v5, un 70% de aumento. El porcentaje de mensajes del operador con lenguaje explícito de decisión y diseño subió de 4.5% a 7.0% en el mismo período. El operador en v5 no estaba escribiendo más para explicar más — estaba especificando más antes de ejecutar.

Del otro lado, el ratio de producción de Claude — caracteres producidos por carácter recibido del operador — pasó de 7.4x en v1-v2 a 9.9x en v5. Claude produjo proporcionalmente más por unidad de input en las fases maduras, con mensajes que crecieron de un promedio de 983 caracteres en v1-v2 a 1659 en v5. El porcentaje de mensajes de Claude con lenguaje de razonamiento y planificación también subió: de 48% en v3 a 66% en v5, consistente con las sesiones de auditoría y verificación que dominaron esa fase.

Los dos efectos juntos son la misma historia contada desde los dos lados: especificaciones más precisas por parte del operador, outputs más sustanciales por parte de Claude, con menos mensajes de ajuste intermedio. Productividad agregada creciente — más conversaciones por día, menos mensajes por conversación, más output por mensaje.

---

### Lo que los datos no cubren

Dos métricas que habrían completado este cuadro no están disponibles. La distribución de autoría real dentro de las decisiones de diseño — qué fracción de las propuestas de arquitectura vino del operador versus fue generada por Claude y aceptada — no es recuperable del análisis de texto: el lenguaje de decisión aparece en ambos lados pero no dice quién inició la propuesta. Resolver eso requeriría anotación manual de una muestra. Y la complejidad técnica por fase como variable independiente del esfuerzo tampoco es directamente medible sin una métrica sobre el código producido: el análisis actual usa el esfuerzo como proxy, pero una especificación más corta que habilita código más complejo — que es el efecto que el sistema buscaba — no se captura por esa vía.

Lo que sí está disponible converge en la misma dirección: velocidad creciente, costo de arranque decreciente, investigación orientada a verificación en lugar de exploración, especificaciones más largas del operador y outputs más sustanciales de Claude. El sistema mejoró su throughput de forma consistente, y los indicadores de planificación deliberada crecieron junto con esa mejora, no a pesar de ella.

---

*Sección 5 — draft s29 — revisión de s28 — 2026-06-17*
