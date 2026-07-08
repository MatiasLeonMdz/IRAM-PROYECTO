# IRAM — INSTRUCCIONES DE USO PARA EL OPERADOR
## Guía de carga y uso del sistema de control

*Actualizado: 2026-05-27 20:55 | Proyecto: IRAM v4.3.7 | Engine: Imperator Roma 2.0.4*

---

## ARCHIVOS DEL SISTEMA DE CONTROL

Los nombres exactos de cada archivo activo están siempre en **Sección 22 del TECHNICAL_WIKI ACTIVE**.
No están hardcodeados aquí para no tener que actualizar este archivo cada vez que se genera una versión nueva.

| Archivo | Para quién | Función |
|---|---|---|
| TECHNICAL_WIKI ACTIVE | IA + humano | Fuente de verdad operativa — diseño v4, reglas, estado del proyecto |
| TECHNICAL_WIKI ARCHIVE | IA + humano | Historial narrativo, código fuente v1/v2/v3, decisiones descartadas — cargar solo si es necesario |
| PROMPT_MAESTRO | IA | Instrucciones de sesión — **pegar como mensaje, no solo subir como archivo** |
| INSTRUCCIONES_HUMANO | Humano | Este archivo — cómo operar el sistema |
| SESSION_LOG | IA + humano | Registro de sesión — contexto reciente para la próxima sesión |
| Zip canónico | IA | Código fuente activo del mod |

---

## CÓMO ARRANCAR UNA SESIÓN NUEVA

**Orden de carga obligatorio:**

1. Subir el TECHNICAL_WIKI ACTIVE (nombre exacto: Sección 22 del TECHNICAL_WIKI ACTIVE)
2. Subir el zip canónico activo (nombre exacto: Sección 22 del TECHNICAL_WIKI ACTIVE)
3. Subir el SESSION_LOG más reciente si existe (no es bloqueante si no hay)
4. Copiar y pegar el bloque PASO 1 del PROMPT_MAESTRO como mensaje en el chat

⚠ **El paso 4 es crítico y no es opcional.**
Subir el PROMPT_MAESTRO como archivo no es suficiente — la IA lo procesa como contexto
pasivo y no ejecuta las reglas. El PASO 1 pegado como mensaje es lo que activa las reglas.
Sin ese mensaje, la IA viola R18, RE1, RE5 y otras reglas sistemáticamente.

**El TECHNICAL_WIKI ARCHIVE:** cargar solo si la sesión requiere historial narrativo,
código fuente v1/v2/v3, o decisiones descartadas. Para sesiones de código habituales
no es necesario.

**Elegir plantilla:**

| Situación | Plantilla |
|---|---|
| Fix, feature, corrección puntual, codeo | **Plantilla A** |
| Revisión integral del proyecto, análisis comparativo | **Plantilla B** |
| Meta-análisis del sistema de control | Sesión libre — no usar plantillas |

---

## AL TERMINAR UNA SESIÓN

1. La IA genera el SESSION_LOG automáticamente al cierre — guardarlo
2. Si se resolvió algo con impacto en el diseño: propagar el SESSION_LOG al TECHNICAL_WIKI ACTIVE
3. Si se generó un zip nuevo: actualizar la Sección 22 del TECHNICAL_WIKI ACTIVE
4. Si hubo cambios en el sistema de control: actualizar este archivo (INSTRUCCIONES_HUMANO)

**Nota:** la IA pregunta la hora antes de generar cualquier archivo. Tenerla a mano.

---

## SMOKE TEST — USAR ANTES DE DEPENDER DE UNA VERSIÓN NUEVA DEL PROMPT

Antes de usar una versión nueva del PROMPT_MAESTRO en producción, hacé estas preguntas a la IA en una sesión limpia:

1. ¿Qué hace R1 y por qué existe?
2. ¿Qué pasa si el zip contradice el TECHNICAL_WIKI en algo no registrado en Sección 19?
3. ¿Cuándo se usa Plantilla B en lugar de Plantilla A?
4. ¿Qué tres cosas hacés antes de tocar cualquier archivo?
5. ¿Qué hacés antes de generar el zip final?

Si responde bien: el prompt funciona. Si no: ajustar antes de usar en trabajo real.

---

## PROTOCOLO DE REANUDACIÓN DESDE PAUSA LARGA

Si no tocaste el proyecto por semanas o meses:

1. Leer Sección 22 del TECHNICAL_WIKI ACTIVE — qué archivos están activos
2. Leer Sección 0.5 del TECHNICAL_WIKI ACTIVE — estado actual de cada componente
3. Leer Sección 19.0 — índice de temas abiertos
4. Leer la última entrada de Sección 19 — qué quedó pendiente en la última sesión
5. Recién entonces: arrancar sesión nueva con el prompt habitual

Esos cinco puntos en diez minutos devuelven el contexto completo.

---

## ARCHIVOS DE HISTORIAL (cargar solo si son necesarios)

- `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_0_2026-05-27_20-28.md` — historial narrativo, código fuente v1/v2/v3, decisiones descartadas
- Zips históricos: ver Sección 21 del TECHNICAL_WIKI ACTIVE para tabla completa

---

*Sistema de control IRAM v3.5 — 2026-05-27 20:55*
