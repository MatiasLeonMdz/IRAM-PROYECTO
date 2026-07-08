---
name: desarrollo-multisesion-con-ia
description: Operación de proyectos técnicos sostenidos con Claude. Aplica cuando el proyecto dura más de una sesión, tiene un dominio técnico específico, y requiere consistencia entre instancias sin memoria compartida. Cubre arquitectura de contexto, división de trabajo operador/IA, y diagnóstico de modos de falla.
version: 2.0
---

# Skill — Desarrollo multisesión con IA

## ARQUITECTURA DE CONTEXTO

La posición y el formato de una instrucción determinan el peso que recibe — más que su contenido.

- Las instrucciones de trabajo van pegadas como primer mensaje, no adjuntas como archivo. Lo que entra primero pesa más.
- Un bloque corto de reglas numeradas recibe más peso que la misma información diluida en prosa. El formato señala jerarquía.
- Si una instrucción correctamente escrita no se aplica de forma consistente, el diagnóstico es de posición y formato — no de contenido. Antes de reescribir, preguntar: ¿dónde vive esto en el contexto, y qué compite con eso por atención?

El contexto se organiza en capas con funciones distintas:
- **Instrucciones de trabajo:** reglas vigentes, pegadas al inicio. Crecen solo cuando un error real genera una regla nueva.
- **Estado actual:** qué existe, qué versión es canónica. Sin el peso del historial.
- **Historial:** decisiones anteriores, alternativas descartadas. Se consulta; no se carga por defecto.
- **Registro de sesión (SESSION_LOG):** qué se hizo, qué falta, qué está cerrado. Es el handoff entre instancias — no un diario.

No cargar todo por defecto. El contexto selectivo es más efectivo que el contexto total.

## DIVISIÓN DE TRABAJO

El operador es el arquitecto. Claude es una herramienta de precisión con capacidad de lenguaje: coloca lo que se le indica aunque el plano tenga un error.

- Las decisiones de arquitectura — qué alcance usar, cómo estructurar, qué convención adoptar — las origina el operador.
- La implementación dado ese diseño es trabajo de Claude.
- La calidad del output depende de la calidad de la especificación. Una especificación imprecisa produce output impreciso — no es un límite de la herramienta, es un límite del input.

Antes de delegar ejecución, cerrar el diseño en una especificación escrita. Una sesión de diseño no termina con código — termina con una especificación que la sesión de ejecución puede usar sin tener que decidir nada.

**Tiering:** diseño y ejecución no se mezclan bien en la misma sesión. El contexto de una sesión de diseño acumula incertidumbre y decisiones abiertas que compiten con la precisión que requiere la ejecución. El techo operacional por sesión en modo máximo es aproximadamente una tarea mediana o dos tareas ligeras antes de que la calidad empiece a caer.

## DIAGNÓSTICO DE MODOS DE FALLA

Hay dos tipos de falla con tratamientos distintos. Confundirlos produce la respuesta incorrecta.

**Falla epistémica:** Claude afirma que algo es imposible desde su conocimiento documentado, no desde el sistema real. Señales: "eso no es posible", "ese elemento no existe", "no hay forma de hacer X". Tratamiento: cuestionar desde lógica ("si esta estructura existe, debe ser accesible de alguna forma") y verificar contra el sistema real. El árbitro no es Claude — es el sistema.

**Falla técnica:** hay un bug real. Señales: el sistema produce un error concreto, el comportamiento es inesperado de forma reproducible. Tratamiento: depurar el código, no cuestionar el diagnóstico.

Tratar cada "no es posible" como hipótesis verificable no es desconfianza — es el diagnóstico correcto del modo de falla más frecuente.

## DECISIONES DESCARTADAS

Las alternativas evaluadas y descartadas se documentan con su razón — no solo con el resultado.

La audiencia de esa documentación no es el operador. Es la instancia de Claude que llegará sin memoria y potencialmente volverá a proponer lo que ya fue descartado. Sin el "por qué", el ciclo se repite.

El nivel de explicitación tiene que ser suficiente para que alguien sin contexto previo entienda sin preguntar.

## OVERHEAD DE DOCUMENTACIÓN

El overhead tiene que ser proporcional al riesgo concreto que mitiga, no al tamaño del proyecto.

- Registros intermedios y entregas parciales por tarea: aplican cuando hay una secuencia larga de tareas dependientes y el costo de perder trabajo parcial es alto. No aplican al desarrollo cotidiano.
- Activar estas prácticas por defecto cuando el riesgo no está presente es overhead sin beneficio.

## CONDICIONES DE TRANSFERENCIA

Este sistema rinde al máximo cuando hay tres condiciones presentes:

1. **Criterio lógico preexistente** — capacidad de descomponer problemas, buscar evidencia, y cuestionar afirmaciones de imposibilidad. El sistema se puede copiar en su forma; el pensamiento que lo opera no está en ningún archivo.
2. **Árbitro claro** — retroalimentación inequívoca sobre si algo funciona o no. Sin árbitro claro, el costo de verificar cada hipótesis sube radicalmente.
3. **Problema acotado** — alcance definible, resultado verificable, criterio de éxito observable.

Su ausencia no impide usar el sistema — requiere adaptación.
