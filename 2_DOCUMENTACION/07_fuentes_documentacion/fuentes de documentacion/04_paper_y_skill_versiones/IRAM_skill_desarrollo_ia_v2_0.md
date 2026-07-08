---
name: desarrollo-multisesion-con-ia
description: Cargar al inicio de proyectos técnicos que se extienden por muchas sesiones sin memoria compartida entre ellas — mod, pipeline, script, automatización. Señales de activación: instrucciones que se olvidan entre sesiones, errores que se repiten, o el sistema de documentación compitiendo con el trabajo real. No cargar para tareas de sesión única.
version: 2.0
---

# Desarrollo multisesión con IA — skill operacional

## 1. Cuándo usar

Activar cuando el proyecto dura más de una sesión, hay un límite de uso que va a forzar cambios de sesión, o ya se perdió contexto al menos una vez.

No activar para tareas de respuesta única sin continuidad.

---

## 2. Arranque de sesión

1. Verificar qué archivos están disponibles antes de asumir cualquier cosa.
2. Cargar el documento de instrucciones (PROMPT_MAESTRO o equivalente) como **primer mensaje pegado**, no como adjunto ni embebido en otro archivo. La posición determina el peso: lo primero en el contexto recibe más atención que lo mismo enterrado más adentro.
3. Leer el SESSION_LOG antes de cualquier otra acción. No preguntar al operador qué falta — está ahí.
4. Confirmar con el operador el objetivo concreto de esta sesión.
5. No modificar ni crear nada hasta que el plan esté confirmado.

El contexto tiene cuatro capas: instrucciones de trabajo (cómo operar) + estado actual del proyecto (qué es vigente hoy) + historial/legacy (consultar si hace falta, nunca cargar por defecto) + registro de sesión (qué pasó la última vez, qué sigue). Cargar las primeras dos siempre; la tercera solo si se pide explícitamente.

---

## 3. Durante la sesión

- Leer el archivo fuente antes de modificarlo. Sin excepción.
- Ante cambios que afecten más de un archivo o la arquitectura del proyecto: confirmar el plan primero.
- Cuando vayas a decir "no es posible": marcarlo como hipótesis, no como veredicto. El árbitro es el sistema real. Pedir verificación contra el entorno antes de cerrar la pregunta.
- El operador diseña la arquitectura. Claude implementa. No proponer rediseños estructurales no pedidos.
- Si una instrucción no se sigue de forma consistente a pesar de estar clara: el problema es de posición en el contexto, no de contenido. Revisar dónde vive la instrucción antes de reescribirla.
- Si un error aparece por segunda vez: proponer una regla para el PROMPT_MAESTRO, no solo corregirlo.
- Si el contexto se acerca al límite: generar SESSION_LOG parcial antes de continuar. No esperar al cierre.
- No crear archivos nuevos sin informar al operador qué se va a crear y por qué.
- Registros intermedios y entregas parciales por tarea son herramientas situacionales: activarlos solo cuando hay muchas tareas dependientes en sesión larga con riesgo real de corte. No activarlos por defecto — son overhead cuando ese riesgo no está presente.

---

## 4. Cierre de sesión

1. Actualizar SESSION_LOG: qué se hizo, qué falta, qué quedó abierto, qué archivos se generaron.
2. Si apareció un error recurrente: proponer la regla nueva para el PROMPT_MAESTRO.
3. Pregunta de cierre obligatoria: **"¿qué se decidió hoy que no estaba documentado antes?"** Registrar la respuesta como entrada plana: qué / cuándo / por qué importa.
4. Verificar que el SESSION_LOG resultante es suficiente para que otra sesión, en otra cuenta, retome sin necesitar el historial de esta conversación.

---

## 5. Si la sesión falla o se corta

- Primera acción al retomar: reconstruir el SESSION_LOG si no estaba actualizado.
- Retomar cargando: instrucciones + estado actual + SESSION_LOG. No el historial de la conversación anterior.
- Estado incierto → verificar contra los archivos, no contra la memoria de la sesión.
- Si algo importante quedó solo en el chat: documentarlo antes de seguir.

---

## 6. Principio de operación

El estado del proyecto vive en documentos, no en conversaciones. Cada sesión es descartable; los documentos no.

Claude implementa. El operador diseña. No invertir ese orden.

Cada regla del PROMPT_MAESTRO es un problema real resuelto. Cada error que se repite es una regla que falta.

---

*IRAM skill operacional v2.0 — 2026-06-12*
*Extraído de: IRAM_paper_metodologia_v1_0.md*
*Reemplaza: IRAM_SKILL_desarrollo_con_IA_v1_0.md (borrador del paper — audiencia distinta)*
