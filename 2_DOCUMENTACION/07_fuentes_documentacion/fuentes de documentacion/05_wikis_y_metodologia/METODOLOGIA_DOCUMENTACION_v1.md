# METODOLOGÍA DE DOCUMENTACIÓN — IRAM v1.0
## Guía del operador — cómo trabajar con el sistema de documentación

*Generado: s23 — 2026-06-17*
*Audiencia: el operador humano. No la IA.*
*Para las instrucciones que la IA debe ejecutar → ver PROMPT_REGLAS_DOCUMENTACION_v2.md*

---

## QUÉ HACE CADA ARCHIVO

El sistema de documentación tiene cuatro archivos. Tres son para la IA; uno es este documento (para el operador).

| Archivo | Quién lo usa | Para qué |
|---------|-------------|----------|
| PROMPT_REGLAS_DOCUMENTACION_v2.md | IA — se pega como primer mensaje | Reglas de trabajo, contexto del proyecto, REGLA DE CONTRADICCIÓN |
| SESSION_LOG_DOCUMENTACION_s[N].md | IA — se adjunta | Spec ejecutable: qué hacer esta sesión, decisiones inamovibles, estado del draft |
| WIKI_DOCUMENTACION_v1.md | IA — se adjunta | Referencia histórica: estado de documentos, hitos, fases, marco conceptual |
| TEMPLATES_DOCUMENTACION_v1.md | Operador + IA | El operador pega el PASO 2 relevante; las otras 4 templates no entran en contexto |
| METODOLOGIA_DOCUMENTACION_v1.md | Operador | Este archivo — razones, protocolo, señales de alarma |

---

## CÓMO ARRANCAR UNA SESIÓN (pasos del operador)

1. Abrir conversación nueva.
2. Pegar el contenido completo de PROMPT_REGLAS_DOCUMENTACION_v2.md como **primer mensaje** (no adjuntar — pegar).
3. En el mismo mensaje o en el segundo: pegar el PASO 2 de la template que corresponde a esta sesión (A / B / C1 / C2 / D).
4. Adjuntar como archivos: SESSION_LOG_DOCUMENTACION_s[N].md + WIKI_DOCUMENTACION_v1.md.
5. Si la sesión necesita documentos de referencia del proyecto (SKILL v1.0, esqueleto, drafts anteriores): adjuntarlos también.
6. No pegar el SESSION_LOG ni la WIKI — solo adjuntar. La IA los lee con bash_tool si no están renderizados (R20).

**Por qué pegar el PROMPT y adjuntar el resto:**
Lo que entra como mensaje pegado recibe más peso que lo que entra como archivo adjunto. Las reglas de trabajo deben ser el primer bloque de la sesión. El log y la wiki son referencia — pueden llegar adjuntos.

---

## CÓMO CERRAR UNA SESIÓN (pasos del operador)

1. Antes de terminar la sesión: pedir a la IA que responda R14 ("¿qué se decidió hoy que no estaba documentado antes?").
2. Revisar si alguna entrada de R14 es crítica → pedir a la IA que la promueva a DECISIONES CONFIRMADAS con ID.
3. Pedir a la IA que genere el SESSION_LOG_DOCUMENTACION_s[N+1].md actualizado.
4. Si la WIKI cambió (nuevo estado de documentos, Marco Conceptual, etc.): pedir que genere WIKI_DOCUMENTACION_v1.md actualizada.
5. Guardar los archivos generados. Son los insumos de la próxima sesión.

**Lo que el SESSION_LOG debe ser:**
Una spec ejecutable. La IA que lo reciba debe saber exactamente qué hacer sin inferir nada. Modelo: SESSION_LOG del proyecto (v5.6).
Si el SESSION_LOG narra qué pasó en lugar de decirle a la próxima IA qué ejecutar, está mal — corregir antes de cerrar la sesión.

---

## LO QUE NO HAY QUE HACER (lecciones de s21-s22)

Estos son los errores que destruyeron información entre sesiones:

**Error 1 — Reescribir celdas de tabla al actualizar**
Al actualizar la tabla de estado de documentos, nunca reescribir celdas existentes. Solo agregar notas al final de la celda. Una celda reescrita limpia borra advertencias críticas.
→ Señal: si una celda cambia de "⚠️ SUPERADO EN S18" a solo "Fuente de hechos técnicos", algo se perdió.

**Error 2 — No verificar sección por sección al consolidar**
Al generar un SESSION_LOG nuevo, comparar sección por sección contra el anterior. Toda sección presente en el log anterior debe aparecer en el nuevo, o estar explícitamente marcada como "incorporada en X" o "descartada porque Y".
→ Señal: si el nuevo log es más corto que el anterior sin razón explícita, se perdió contenido.

**Error 3 — Guardar decisiones críticas solo en celdas de tabla**
Las decisiones que no deben rediscutirse van en DECISIONES CONFIRMADAS — NO REDEBATIR con ID único. Las celdas de tabla se actualizan; la sección DECISIONES no se toca.
→ Señal: si una decisión solo aparece en la tabla de estado (no en DECISIONES CONFIRMADAS), está en riesgo.

**Error 4 — Tratar el SESSION_LOG como registro histórico**
El SESSION_LOG no es un diario de qué pasó. Es una spec para la próxima IA. El resumen histórico de sesiones pertenece a la WIKI, no al log.
→ Señal: si el log comienza con "En esta sesión se hizo..." en lugar de "La próxima IA recibe...", está mal orientado.

**Error 5 — Dejar las templates dentro del PROMPT**
Las cinco templates en el mismo archivo que las reglas significan que la IA tiene en contexto instrucciones para sesiones de tipo A, B, C2, D cuando está ejecutando una sesión de tipo C1. Ruido constante que compite con las instrucciones relevantes.
→ Señal: si el PROMPT supera 120 líneas, probablemente tiene contenido que no corresponde ahí.

---

## SEÑALES DE ALARMA — cuándo el sistema está degradando

| Señal | Causa probable | Acción |
|-------|---------------|--------|
| El SESSION_LOG nuevo es más corto que el anterior sin explicación | Consolidación que perdió secciones | Comparar contra anterior; recuperar antes de continuar |
| Una decisión de DECISIONES CONFIRMADAS aparece en debate de nuevo | No se leyó el SESSION_LOG completo | Re-enforcer DEC-06: leer DECISIONES antes de ejecutar |
| Una regla del PROMPT está siendo ignorada | Está enterrada en el PROMPT, no es la primera instrucción | Revisar posición y formato (el hallazgo central del paper aplica al propio sistema) |
| La IA asume qué archivos están disponibles sin ejecutar ls | R1 no se ejecutó | La primera acción de la IA debe ser ls /mnt/user-data/uploads/ |
| El log crece a 200+ líneas | Tiene contenido histórico que no es spec ejecutable | Mover historial a WIKI; el log debe ser corto y operacional |

---

## HISTORIA DE POR QUÉ EXISTE ESTE SISTEMA

*(Para entender las decisiones de diseño, no para incluir en el paper.)*

El sistema de documentación reprodujo exactamente el problema que el proyecto IRAM documentó: el SUPERBACKUP problem. El PROMPT_MAESTRO de documentación v1.9 llegó a ~575 líneas mezclando reglas, cinco templates, estado de todos los documentos, hitos metodológicos y fases del proyecto. Era el mismo monolito que el proyecto resolvió separando PROMPT_MAESTRO / WIKI ACTIVE / SESSION_LOG.

El diagnóstico se hizo en s21 comparando el PROMPT_MAESTRO v5.2 del proyecto (que funciona para IA de bajo nivel) contra el PROMPT de documentación v1.9 (que fallaba). La diferencia central: el SESSION_LOG del proyecto es una spec ejecutable; el de documentación era un registro histórico. Las decisiones críticas en el proyecto viven en DECISIONES CONFIRMADAS con IDs inamovibles; en documentación vivían en celdas de tabla que se reescribían al actualizar.

La corrección se implementó en s22 y s23: separación en cuatro archivos, DECISIONES CONFIRMADAS con IDs, PROTOCOLO DE LA IA EJECUTORA, REGLA DE CONTRADICCIÓN. El sistema de documentación ahora tiene la misma arquitectura de capas que el proyecto que documenta.

---

## EQUIVALENCIA CON EL SISTEMA DEL PROYECTO

| Sistema del proyecto | Sistema de documentación |
|---------------------|--------------------------|
| PROMPT_MAESTRO v5.2 | PROMPT_REGLAS_DOCUMENTACION_v2.md |
| TECHNICAL_WIKI ACTIVE | WIKI_DOCUMENTACION_v1.md |
| SESSION_LOG v5.6 | SESSION_LOG_DOCUMENTACION_s[N].md |
| INSTRUCCIONES_HUMANO | Este archivo |
| Plantillas A/B/C1/C2/D (PASO 2) | TEMPLATES_DOCUMENTACION_v1.md |

La diferencia principal: el proyecto tiene dos tipos de sesión (bug fix / feature); el sistema de documentación tiene cinco (A, B, C1, C2, D). Por eso las templates van en un archivo separado en lugar de estar inline en el PROMPT.

---

*METODOLOGÍA DOCUMENTACIÓN v1.0 — 2026-06-17*
*Generado en s23. Actualizar cuando cambie la arquitectura del sistema de documentación.*
