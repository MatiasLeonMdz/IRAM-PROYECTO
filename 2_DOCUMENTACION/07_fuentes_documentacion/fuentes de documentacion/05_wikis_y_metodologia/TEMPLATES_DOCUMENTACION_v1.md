# TEMPLATES — Documentación IRAM v1.0
## Solo PASO 2 — el PASO 1 (PROMPT_REGLAS) ya fue pegado como primer mensaje

*Actualizado: 2026-06-17 | Solo pegar la template relevante para la sesión*

---

## INSTRUCCIONES DE USO (para el operador)

1. Pegar PROMPT_REGLAS_DOCUMENTACION_v2.md como primer mensaje de la sesión.
2. Adjuntar WIKI_DOCUMENTACION_v1.md y SESSION_LOG_DOCUMENTACION_s[N].md.
3. Pegar el PASO 2 de la template correspondiente como segundo bloque en el mismo mensaje, o en el segundo mensaje.
4. Las otras cuatro templates no entran en contexto.

---

## TEMPLATE A — Sesión de procesamiento de historial

**Estado: ✅ EJECUTADA (2026-06-12). Solo re-ejecutar si llegan nuevos conversations.json.**

```
PASO 2 — PROCESAMIENTO DE HISTORIAL

NOTA: Plantilla A ya fue ejecutada. El historial unificado existe.
Si se recibe un nuevo conversations.json, seguir el protocolo de abajo.
De lo contrario, esta template no aplica — usar C1.

JSON recibidos esta sesión: [listar cuáles subió el operador]

PROTOCOLO

1. R1: ls /mnt/user-data/uploads/ — confirmar archivos.
2. R20: identificar cuáles están renderizados en contexto. Leer los no renderizados con bash_tool.
3. Por cada JSON nuevo: procesar con process_iram_v2.py etiquetando la cuenta.
4. Fusionar con generate_iram_docs.py — output: historial unificado + hitos + session log.
5. Identificar bloques temáticos dentro de conversaciones largas.
6. Marcar hitos metodológicos encontrados con fecha y sesión exacta.
7. Para cada hito: documentar las 5 dimensiones (R15 del PROMPT_REGLAS).
8. Marcar a qué cuenta pertenece cada hito. RECORDAR R18: rotación secuencial, no paralelismo.

PRIORIDADES DE BÚSQUEDA (deuda residual):
A. Migración Forzada — buscar primera sesión con iram_decisions_migracion.txt antes de 2026-05-22
B. iram_11 (Distribute Global) — CLAUDE_3 2026-05-29 msg 35+
C. Transiciones de cuenta: primera sesión con PROMPT_MAESTRO completo por cuenta

FORMATO DE ENTREGA

1. IRAM_historial_unificado_[fecha].md
2. IRAM_hitos_metodologicos_[fecha]_v[N].md
3. SESSION_LOG_DOCUMENTACION_s[N+1].md — actualización para próxima sesión
4. Respuesta a R14
```

---

## TEMPLATE B — Sesión de análisis de conocimiento perdido

**Estado: ✅ EJECUTADA (2026-06-12). 18 gaps, 6 categorías. Solo re-ejecutar si hay material nuevo.**

```
PASO 2 — ANÁLISIS DE GAPS

NOTA: Plantilla B ya fue ejecutada. El documento de gaps existe (IRAM_gaps_conocimiento_2026-06-12.md).
Si se quiere profundizar categorías específicas, continuar desde ese documento.

CATEGORÍAS

A. CONOCIMIENTO PERDIDO — en chats, no en wiki
B. DECISIONES REVERTIDAS — se tomaron y luego se cambiaron (¿por qué?)
C. CÓDIGO DESCARTADO — se escribió pero no llegó al zip canónico
D. PATRONES DE ERROR RECURRENTES — mismo problema en múltiples sesiones
E. EVOLUCIÓN DEL PROCESO — cuándo y por qué cambió la metodología
F. DIVISIÓN DE TRABAJO REAL — para cada hito: ¿quién tuvo la iniciativa? ¿quién encontró la solución?
   Fuente prioritaria: STRATEGIC LOG 2026-05-27 (en ARCHIVE Sección 19).

FORMATO DE ENTREGA

1. IRAM_gaps_conocimiento_[fecha].md — actualización
2. SESSION_LOG_DOCUMENTACION_s[N+1].md
3. Respuesta a R14
```

---

## TEMPLATE C1 — Sesión de construcción del paper (research narrative)

**Estado: ACTIVA. S1 ✅ S3 ✅ — S4 es la siguiente tarea.**

```
PASO 2 — CONSTRUCCIÓN DEL PAPER

ESTADO ACTUAL DEL DRAFT
S1 — El laboratorio              ✅ IRAM_C1_s1_draft_s20.md
S3 — Hallazgo central            ✅ IRAM_C1_s3_draft_s20.md
S4 — Tres hallazgos con casos    ❌ PENDIENTE — PRÓXIMA TAREA
S2 — Lo que tuvimos que construir ❌ PENDIENTE
S5 — Los datos del proceso       ❌ PENDIENTE bloqueada parcialmente
S6 — Conceptos formales          ❌ PENDIENTE
S7 — Qué transfiere y qué no     ❌ PENDIENTE

FUENTE DE VERDAD PARA EL DRAFT (DEC-11, DEC-12)
- MAPPING CORRECCIONES s18→s19: en SESSION_LOG s[N] sección MATERIAL S4
- El SKILL v1.0 es fuente de hechos y ejemplos técnicos — no la base estructural
- Para S4: no usar SKILL v1.0 como base. Usar MATERIAL S4 del SESSION_LOG

ARCHIVOS A CARGAR PARA ESTA SESIÓN
- Este log (SESSION_LOG) — ya cargado
- IRAM_C1_esqueleto_s17.md — para estructura
- IRAM_C1_s1_draft_s20.md y IRAM_C1_s3_draft_s20.md — para consistencia de voz
- IRAM_SKILL_desarrollo_con_IA_v1_0.md — solo secciones relevantes si se necesitan hechos

AUDIENCIA DEL PAPER
Lector con contexto de IA (diplomatura UTN BA), sin contexto del proyecto.
No conoce IRAM. No conoce al operador. La causalidad es explícita.

ESTRUCTURA — 7 SECCIONES (ver IRAM_C1_esqueleto_s17.md para detalle)
1. El laboratorio
2. Lo que tuvimos que construir (y por qué)
3. El hallazgo central: posición y formato importan más que el contenido
4. Cómo trabaja la IA: tres hallazgos con casos + tiering (4A, 4B, 4C, 4D)
5. Los datos del proceso
6. Los conceptos formales que nombran lo que hicimos
7. Qué transfiere y qué no

AJUSTES AL ESQUELETO s17 (incorporar durante el draft):
- S4D: tiering como hallazgo operacional propio (diseño en alto / ejecución en bajo)
- S7: resolución circularidad criterio-preexistente / habilidades-entrenadas
- Razón-junto-con-decisión: lugar propio en el paper

PRINCIPIO GENERAL DEL PAPER
"La IA no democratiza la programación. Permite ejecutar pensamiento estructurado
en dominios técnicos sin dominar la mecánica de esos dominios.
El límite no es la herramienta — es la calidad del pensamiento que la opera.
Pero la herramienta también tiene techo propio."

FORMATO DE ENTREGA
- Un archivo por sección: IRAM_C1_s[N]_draft_s[sesión].md
- SESSION_LOG_DOCUMENTACION_s[N+1].md
- Respuesta a R14
```

---

## TEMPLATE C2 — Sesión de construcción del skill operacional

**Estado: ⏸ BLOQUEADA — espera C1 completo. C2 vigente como v2.0 provisional.**

```
PASO 2 — CONSTRUCCIÓN DEL SKILL OPERACIONAL

PRERREQUISITO: C1 (paper) completo. No ejecutar antes.
El skill se extrae del paper terminado, no del SKILL.md v1.0 directamente.

AUDIENCIA: Claude. No un humano.
El skill se carga al inicio de una sesión para que Claude opere distinto.
Cada línea debe cambiar el comportamiento — no explicar historia.

LONGITUD OBJETIVO: 40-60 líneas de contenido + YAML frontmatter.
Si supera 80 líneas: hay narrativa que no pertenece aquí → moverla al paper.

YAML FRONTMATTER OBLIGATORIO
  name: desarrollo-multisesion-con-ia
  description: [descripción precisa para triggering]
  version: 2.0

CRITERIO DE CALIDAD
Cada línea responde: "¿esto cambia lo que Claude hace?"
Si no → es narrativa → pertenece al paper.

FORMATO DE ENTREGA
1. IRAM_skill_desarrollo_ia_v2_0.md — versión revisada
2. SESSION_LOG_DOCUMENTACION_s[N+1].md
3. Respuesta a R14
```

---

## TEMPLATE D — Sesión de análisis cuantitativo

**Estado: ✅ BLOQUES 0-3 COMPLETOS. Bloques 4-5 opcionales, no bloquean C1.**

```
PASO 2 — ANÁLISIS CUANTITATIVO

NOTA: Bloques 0-3 completos en IRAM_analisis_cuantitativo_2026-06-12_v3.md.
No re-ejecutar bloques 0-3. Si se quieren Bloques 4 o 5, continuar desde v3.

REQUIERE: claude_N_processed.json ×5. No cargar por defecto.

BLOQUES PENDIENTES (opcionales)
Bloque 4 — Calidad del proceso
Bloque 5 — Conexión IRAM → data science

MÉTRICAS COMPLETADAS (no re-ejecutar)
Bloque 0 — Evolución del contexto ✅
Bloque 1 — Velocidad de desarrollo por fase ✅
Bloque 2 — Rotación de contextos ✅ (0 interleavings en 7.313 msgs — R18)
Bloque 3 — [ver v3] ✅

TAREAS PENDIENTES QUE REQUIEREN JSON ×5 (no son Bloque 4/5):
T1 — Complejidad habilitada por cambios metodológicos → destino S5
T2 — Autoría real operador vs Claude → destino S4A

FORMATO DE ENTREGA
1. IRAM_analisis_cuantitativo_[fecha]_v[N].md
2. SESSION_LOG_DOCUMENTACION_s[N+1].md
3. Respuesta a R14
```

---

*TEMPLATES DOCUMENTACIÓN v1.0 — 2026-06-17*
*Generado en s23 al separar las templates del PROMPT_MAESTRO (DEC-03, DEC-04).*
*Usar junto con PROMPT_REGLAS_DOCUMENTACION_v2.md (PASO 1) y SESSION_LOG_DOCUMENTACION_s[N].md.*
