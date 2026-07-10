# Diplomatura en Ciencia de Datos e Inteligencia Artificial

## Módulo 2: Fundamentos de análisis y preparación de datos
## Unidad 2: Limpieza de datos (Data Cleaning)

---

## Presentación

La limpieza de datos es una etapa crítica en cualquier proceso de análisis, ya que la calidad de los resultados depende directamente de la calidad de la información utilizada. En la práctica, los conjuntos de datos reales suelen presentar problemas como valores faltantes, registros duplicados o inconsistencias en los formatos, lo que dificulta su análisis directo. Esta unidad introduce los conceptos y prácticas fundamentales para identificar y tratar estos problemas de manera sistemática.

A lo largo de la unidad, se abordarán técnicas básicas para detectar datos incompletos, duplicados o inconsistentes, comprendiendo cómo estos errores impactan en la interpretación de la información. Se pondrá el foco en desarrollar criterios analíticos que permitan decidir cuándo corregir, eliminar o conservar determinados datos, evitando soluciones automáticas que puedan distorsionar los resultados del análisis.

Finalmente, la unidad propone buenas prácticas para preparar los datos antes de realizar un análisis exploratorio. Estas prácticas permiten mejorar la coherencia, confiabilidad y legibilidad de la información, sentando las bases para análisis más profundos y decisiones informadas. El enfoque será práctico y accesible, utilizando herramientas comunes y sin requerir conocimientos de programación.

## Objetivos

Que los participantes logren…

- Adquirir los conocimientos y habilidades básicas para identificar y tratar problemas frecuentes de calidad de datos.
- Comprender la importancia de la limpieza de datos como una etapa previa indispensable al análisis, y que pueda aplicar criterios simples para mejorar la confiabilidad de la información.
- Desarrollar una actitud crítica y responsable frente al uso de datos, fomentando prácticas de estandarización, corrección y depuración de información.
- Contar con herramientas conceptuales y prácticas para preparar conjuntos de datos de manera adecuada, facilitando análisis exploratorios más precisos y decisiones basadas en datos de mejor calidad.

## Bloques temáticos

1. Detección y tratamiento de datos incompletos, duplicados o inconsistentes.
2. Principios generales para estandarizar, corregir y depurar información.
3. Buenas prácticas para preparar datos antes de un análisis exploratorio.

---

## Detección y tratamiento de datos incompletos, duplicados o inconsistentes

En el trabajo con datos reales, uno de los desafíos más frecuentes es la presencia de errores que afectan la calidad de la información. Los datos incompletos, duplicados o inconsistentes son situaciones habituales en conjuntos de datos provenientes de sistemas administrativos, registros manuales, formularios digitales o múltiples fuentes integradas. Identificar y tratar adecuadamente estos problemas es una etapa fundamental dentro del proceso de limpieza de datos, ya que impacta directamente en la confiabilidad del análisis y en las decisiones que se toman a partir de él.

Los **datos incompletos** se presentan cuando faltan valores en una o más variables de un conjunto de datos. Esto puede ocurrir por errores en la carga de información, por fallas en los sistemas de recolección o porque ciertos datos no estaban disponibles en el momento del registro. La presencia de datos faltantes puede distorsionar los resultados del análisis, especialmente si no se detectan o se tratan de manera adecuada. Por ejemplo, calcular promedios o totales sin considerar valores faltantes puede generar conclusiones erróneas sobre una situación analizada.

Detectar datos incompletos implica revisar sistemáticamente las columnas y registros para identificar celdas vacías, valores nulos o información incompleta. Una vez detectados, el tratamiento de estos datos requiere criterio analítico. En algunos casos, puede ser adecuado completar los valores faltantes utilizando información disponible, como promedios o valores frecuentes. En otros casos, puede ser preferible excluir determinados registros si la falta de datos compromete la calidad del análisis. La decisión dependerá del contexto, del volumen de datos faltantes y del objetivo del análisis.

Otro problema frecuente en los conjuntos de datos reales es la presencia de **datos duplicados**, es decir, registros que se repiten total o parcialmente dentro de una tabla. Los duplicados suelen generarse por errores de carga, por integraciones de múltiples fuentes o por registros repetidos de una misma operación. La existencia de datos duplicados puede inflar artificialmente los resultados, generando sobreestimaciones en conteos, sumas o indicadores clave.

La detección de duplicados implica identificar registros idénticos o muy similares según ciertos criterios, como combinaciones de variables clave. Una vez detectados, el tratamiento suele consistir en eliminar los duplicados, conservando un único registro válido. Sin embargo, también es importante verificar si los registros aparentemente duplicados no corresponden en realidad a eventos distintos que comparten características similares. Este análisis evita la eliminación indebida de información relevante.

Los **datos inconsistentes** representan otro tipo de problema común en la limpieza de datos. La inconsistencia se manifiesta cuando los datos no siguen un criterio uniforme, presentan contradicciones internas o utilizan formatos distintos para representar la misma información. Ejemplos habituales incluyen diferencias en el formato de fechas, variaciones en nombres de categorías o valores que no coinciden con el tipo de dato esperado. Estas inconsistencias dificultan el análisis y pueden generar errores en cálculos o segmentaciones.

Detectar datos inconsistentes requiere observar patrones, revisar formatos y comparar valores dentro de una misma variable. El tratamiento de inconsistencias suele implicar la estandarización de formatos, la corrección de errores evidentes o la unificación de categorías. Por ejemplo, convertir todas las fechas a un mismo formato o unificar distintas denominaciones para una misma categoría mejora la coherencia del conjunto de datos y facilita su análisis posterior.

Un aspecto clave en el tratamiento de datos incompletos, duplicados o inconsistentes es evitar decisiones automáticas sin análisis previo. La limpieza de datos no debe entenderse como una tarea mecánica, sino como un proceso que requiere comprensión del contexto y de los objetivos del análisis. Eliminar datos sin criterio o realizar correcciones arbitrarias puede introducir nuevos errores o sesgos en la información.

En síntesis, la detección y el tratamiento de datos incompletos, duplicados o inconsistentes constituyen una etapa esencial para garantizar la calidad de los datos antes de avanzar en el análisis. Desarrollar estas habilidades permite trabajar con información más confiable, reducir riesgos de interpretaciones erróneas y fortalecer la toma de decisiones basadas en datos. Esta etapa sienta las bases para un análisis exploratorio más sólido y para el uso responsable de la información en contextos reales y profesionales.

---

## Principios generales para estandarizar, corregir y depurar información

Luego de identificar datos incompletos, duplicados o inconsistentes, el siguiente paso en el proceso de limpieza de datos consiste en aplicar principios generales que permitan **estandarizar, corregir y depurar** la información. Esta etapa busca mejorar la coherencia y calidad del conjunto de datos, asegurando que la información sea comprensible, comparable y adecuada para el análisis. La estandarización y depuración no solo corrigen errores evidentes, sino que también preparan los datos para un uso analítico más confiable.

La **estandarización de datos** implica establecer criterios uniformes para representar la información dentro de un conjunto de datos. En la práctica, los datos pueden estar registrados con diferentes formatos, unidades o denominaciones, incluso cuando refieren a la misma variable. Por ejemplo, una fecha puede aparecer en distintos formatos, o una categoría puede escribirse de múltiples maneras. Estas diferencias dificultan el análisis y pueden generar errores en filtros, cálculos o segmentaciones. Estandarizar los datos permite reducir esta variabilidad y facilitar su interpretación.

Un principio central de la estandarización es la **coherencia interna**. Esto implica que los valores de una misma columna deben seguir el mismo criterio de formato y significado. Aplicar este principio puede requerir transformar valores, unificar categorías o redefinir formatos. Por ejemplo, convertir todas las fechas a un mismo formato, normalizar el uso de mayúsculas y minúsculas o unificar abreviaturas contribuye a una mayor claridad y consistencia en los datos.

La **corrección de datos** se refiere a la identificación y ajuste de errores evidentes dentro del conjunto de datos. Estos errores pueden incluir valores fuera de rango, datos mal cargados o inconsistencias lógicas, como cantidades negativas cuando no corresponden. Corregir estos errores requiere atención y criterio, ya que no siempre es posible determinar el valor correcto sin información adicional. En algunos casos, la corrección puede implicar reemplazar valores incorrectos; en otros, puede ser más adecuado marcar o excluir esos registros del análisis.

Un aspecto importante de la corrección de datos es evitar suposiciones injustificadas. Modificar datos sin una base clara puede introducir sesgos o distorsionar la información original. Por este motivo, las correcciones deben realizarse de manera consciente y documentada, considerando el impacto que pueden tener en el análisis. En contextos reales, muchas veces es preferible conservar un dato imperfecto antes que introducir un valor incorrecto por suposición.

La **depuración de información** consiste en eliminar datos que no aportan valor al análisis o que pueden generar ruido en los resultados. Esto puede incluir columnas irrelevantes, registros incompletos que no pueden ser corregidos o información redundante que no contribuye a los objetivos del análisis. Depurar no significa eliminar datos de forma indiscriminada, sino seleccionar de manera estratégica qué información resulta útil y cuál puede descartarse sin afectar la calidad del análisis.

Depurar datos también implica simplificar la estructura del conjunto de datos, facilitando su lectura y manipulación. Un conjunto de datos depurado permite trabajar de manera más eficiente, reducir errores y centrar el análisis en las variables relevantes. Esta práctica es especialmente importante cuando se trabaja con volúmenes de datos limitados, donde cada variable debe aportar información significativa.

En conjunto, los principios de estandarización, corrección y depuración constituyen una etapa clave dentro del proceso de limpieza de datos. Aplicarlos de manera consciente permite transformar datos desordenados o inconsistentes en información clara y confiable. Dominar estos principios significa desarrollar una mirada analítica más rigurosa y responsable, sentando las bases para análisis exploratorios sólidos y decisiones informadas basadas en datos de calidad.

---

## Buenas prácticas para preparar datos antes de un análisis exploratorio

Antes de iniciar un análisis exploratorio de datos, resulta fundamental aplicar una serie de buenas prácticas que permitan asegurar que la información esté en condiciones adecuadas para ser analizada. El análisis exploratorio tiene como objetivo comprender el comportamiento general de los datos, identificar patrones, tendencias y posibles relaciones entre variables. Sin embargo, si los datos no han sido correctamente preparados, este análisis puede arrojar resultados engañosos o difíciles de interpretar.

1. **Revisar el conjunto de datos de manera global** antes de profundizar en cálculos o visualizaciones. Esta revisión inicial permite familiarizarse con la estructura del dataset, identificar el número de registros, las variables disponibles y los tipos de datos presentes. Tener una visión general ayuda a detectar problemas evidentes, como columnas irrelevantes, nombres poco claros o formatos inconsistentes, y facilita la planificación del análisis exploratorio.

2. **Verificar la coherencia entre variables.** Esto implica revisar que los valores registrados tengan sentido lógico entre sí y en relación con el contexto del problema analizado. Por ejemplo, fechas que no corresponden al período de estudio, cantidades negativas sin justificación o combinaciones de valores imposibles son señales de alerta que deben atenderse antes de avanzar. Esta verificación contribuye a evitar interpretaciones erróneas durante el análisis exploratorio.

3. **Documentar las decisiones tomadas** durante la limpieza y preparación de datos es también una buena práctica fundamental. Registrar qué datos fueron corregidos, eliminados o transformados permite mantener trazabilidad sobre el proceso y facilita la comprensión del análisis por parte de otras personas. Además, documentar decisiones ayuda al propio analista a reflexionar sobre los criterios utilizados y a justificar los resultados obtenidos.

4. **Definir claramente el objetivo del análisis exploratorio** antes de comenzar. Aunque el análisis exploratorio tiene un carácter abierto, contar con preguntas orientadoras permite enfocar la exploración y evitar un recorrido desordenado por los datos. Estas preguntas pueden estar relacionadas con la distribución de los datos, la identificación de valores atípicos o la comparación entre grupos, y sirven como guía para seleccionar qué variables analizar y qué visualizaciones utilizar.

5. **Trabajar con copias del conjunto de datos original.** Mantener una versión intacta de los datos permite volver atrás en caso de errores o decisiones equivocadas durante la limpieza o preparación. Esta práctica reduce riesgos y brinda mayor seguridad al experimentar con transformaciones, filtros o cálculos durante el análisis exploratorio.

6. **Adoptar una actitud crítica y reflexiva** frente a la información. No se trata únicamente de aplicar técnicas o herramientas, sino de comprender qué representan los datos, cuáles son sus limitaciones y qué preguntas pueden responder de manera confiable. Esta mirada crítica permite interpretar los resultados del análisis exploratorio con mayor profundidad y evita conclusiones apresuradas o infundadas.

En síntesis, aplicar buenas prácticas antes de un análisis exploratorio es una condición esencial para obtener resultados claros y útiles. Estas prácticas permiten ordenar el proceso, reducir errores y fortalecer la calidad del análisis. Incorporar estas pautas significa desarrollar una forma de trabajo más rigurosa y profesional, sentando bases sólidas para avanzar hacia análisis más complejos y decisiones informadas basadas en datos de calidad.

---

## Bibliografía utilizada y sugerida

Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys*, 41(3).

Kimball, R., & Ross, M. (2013). *The data warehouse toolkit: The definitive guide to dimensional modeling* (3rd ed.). Wiley.

Provost, F., & Fawcett, T. (2013). *Data science for business: What you need to know about data mining and data-analytic thinking*. O'Reilly Media.

Redman, T. C. (2001). *Data quality: The field guide*. Digital Press.

Wickham, H. (2014). Tidy data. *Journal of Statistical Software*, 59(10).
