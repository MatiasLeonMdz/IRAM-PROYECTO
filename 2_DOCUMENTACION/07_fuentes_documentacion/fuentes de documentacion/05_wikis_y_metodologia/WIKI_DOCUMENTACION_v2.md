# WIKI — Documentación IRAM v2.0
## Contexto histórico y estado de todos los documentos

*Actualizado: 2026-06-17 (s30) | Adjuntar en cada sesión — no pegar*
*Versión anterior: WIKI_DOCUMENTACION_v1.md*

---

## DESCRIPCIÓN DEL PROYECTO

**IRAM** es un mod pack para Imperator: Roma 2.0.4, construido en ~2 meses usando 5 cuentas de Claude en rotación secuencial. El proyecto tiene dos productos finales:

**PRODUCTO 1 — El mod IRAM**
Versiones v1→v5.5. Recuperable desde cero usando wikis + zips + historial de conversaciones.

**PRODUCTO 2 — Metodología de trabajo con IA**
- C1 — Research narrative / paper (para humanos). 7 secciones. Estructura: case study técnico con evidencia cuantitativa. Audiencia: lector con contexto de IA (diplomatura UTN BA), sin contexto del proyecto.
- C2 — Skill operacional (para Claude). ~40-60 líneas. Formato compatible con /mnt/skills/. Se extrae de C1, no del SKILL v1.0 directamente.

**PRINCIPIO CENTRAL DEL PAPER (definitivo):**
"La IA no democratiza la programación. Permite ejecutar pensamiento estructurado en dominios técnicos sin dominar la mecánica de esos dominios. El límite no es la herramienta — es la calidad del pensamiento que la opera. Pero la herramienta también tiene techo propio."

**LAS DOS HISTORIAS DEL PROYECTO (no mezclar):**
- Historia del mod técnico: v1 → v2 → v3 → v4.x → v5. Sujeto: el mod y sus funciones.
- Historia del sistema de documentación: backup → SUPERBACKUP → PROMPT_MAESTRO → SESSION_LOG → ACTIVE/ARCHIVE split. Sujeto: cómo el equipo aprendió a trabajar.

---

## ESTADO DE TODOS LOS DOCUMENTOS

| Documento | Versión | Estado | Notas |
|-----------|---------|--------|-------|
| IRAM_TECHNICAL_WIKI_ACTIVE | v3.10 (2026-06-09) | ✅ LEÍDO PARCIAL (s19) | Sec 0.1b, 0.1c, 17, encabezados. Sec 12 leída en s28 para S5. |
| IRAM_TECHNICAL_WIKI_ARCHIVE | v3.7 | ✅ LEÍDO COMPLETO (s16+s19) | s16: Sec 19 + STRATEGIC LOG. s19: cadena SUPERBACKUP, Sec 18.4, 18.5, 19b. |
| IRAM_SESSION_LOG mod | v5.6 (2026-06-09) | ✅ LEÍDO (s19) | 35 hallazgos auditados. INC-13 NOTA. PROTOCOLO IA EJECUTORA. Fuente primaria para S4. |
| IRAM_PROMPT_MAESTRO mod | v5.2 (2026-06-06) | ✅ LEÍDO (s19) | Estructura de referencia para el sistema de documentación. |
| IRAM_HISTORIA_COMPLETA | v1.2 | ✅ LEÍDA (s14) | Secciones 6, 12, 17, 18, 19 analizadas. Sec 18.4: terminología "conocimiento recuperado" (fuente para 4C). |
| IRAM_hitos_metodologicos | v7 (2026-06-12) | ✅ LEÍDO (s16) | Cadenas causales completas. |
| IRAM_historial_unificado | 2026-06-12 | ✅ VIGENTE | 441 convs, 7345 msgs post-dedup, 5 cuentas, 3.6MB |
| IRAM_analisis_cuantitativo | 2026-06-12 v3 | ✅ DISPONIBLE | Bloques 0-3. Datos de s28 usados para S5. |
| IRAM_gaps_conocimiento | 2026-06-12 | ✅ LEÍDO (s16) | 18 gaps, 6 categorías. A.4 = principio más transferible. |
| IRAM_SKILL_desarrollo_con_IA | v1.0 (2026-06-12) | ✅ LEÍDO (s20) | ⚠ FRAMING SUPERADO EN S18. Usar solo como fuente de hechos técnicos y ejemplos. No como base estructural del paper. Auditado en s24 (DEC-16). |
| IRAM_paper_metodologia | v1.0 (2026-06-12) | ✅ LEÍDO COMPLETO (s19) | Bien ejecutado, mal enmarcado. Rescatar: datos sec 2/4, estructura "qué transfiere". |
| IRAM_skill_desarrollo_ia | v2.0 (2026-06-12) | ✅ VIGENTE por ahora | C2 — revisar después de nuevo C1. |
| IRAM_critica_rigurosa | 2026-06-12 | ✅ VIGENTE como insumo | 10 ángulos. Marco académico mal aplicado. No leer antes del esqueleto. |
| IRAM_C1_esqueleto | s17 (2026-06-16) | ✅ VIGENTE | 7 secciones con argumento y evidencia. Estructura definitiva. |
| IRAM_C1_s1_draft | s20 (2026-06-17) | ✅ GENERADO | Sección 1 completa. |
| IRAM_C1_s2_draft | s30 (2026-06-17) | ✅ GENERADO | Sección 2 completa. Cierre en prosa corrida (DEC-18). |
| IRAM_C1_s3_draft | s20 (2026-06-17) | ✅ GENERADO | Sección 3 completa. Ajuste: "posición y formato" incorporado. |
| IRAM_C1_s4_draft | s30 (2026-06-17) | ✅ GENERADO | Sección 4 completa. 4A, 4B, 4C, 4D. INC-13 pendiente verificación. |
| IRAM_C1_s5_draft | s29 (2026-06-17) | ✅ GENERADO | Sección 5 completa. Tres subsecciones (DEC-22). |
| IRAM_C1_s6_draft | s30 (2026-06-17) | ✅ GENERADO | Sección 6 completa. 13 entradas (DEC-19, DEC-20). |
| IRAM_C1_s7_draft | s30 (2026-06-17) | ✅ GENERADO | Sección 7 completa. Corrección referencia 4B aplicada. |
| claude_N_processed.json (×5) | 2026-06-12 | ✅ DISPONIBLES | Usados en s28 para S5. |
| bloque3_analysis_v2.py | 2026-06-12 | ✅ VIGENTE | Script reproducible del Bloque 3. |
| Programa_Diplomatura_UTN_BA.pdf | 2026-06-16 | ✅ LEÍDO (s13) | 5 módulos, 21 semanas — contrastado completo contra IRAM. |
| METODOLOGIA_DOCUMENTACION_v1.md | 2026-06-17 | ✅ GENERADO (s23) | Guía del operador. Cuarta capa del sistema de meta-documentación. DEC-14. |

---

## SECUENCIA DE TRABAJO — ESTADO ACTUAL

| Tarea | Estado | Notas |
|-------|--------|-------|
| A — Historial unificado | ✅ EJECUTADA | 441 convs, 7345 msgs, 5 cuentas |
| D — Análisis cuantitativo | ✅ EJECUTADA (v3) | Bloques 0-3. Datos usados para S5 en s28. |
| B — Análisis de gaps | ✅ EJECUTADA | 18 gaps, 6 categorías |
| C — Borrador metodología | ✅ EJECUTADA | SKILL v1.0 = fuente de hechos técnicos (framing superado) |
| Mapa conceptual completo | ✅ EJECUTADO | 13 clusters — ver MARCO CONCEPTUAL abajo |
| Lectura documentos fuente | ✅ EJECUTADA | 10+ documentos leídos en s16 y s19 |
| Esqueleto nuevo C1 | ✅ EJECUTADO (s17) | IRAM_C1_esqueleto_s17.md — 7 secciones |
| C1 Sección 1 | ✅ DRAFT s20 | IRAM_C1_s1_draft_s20.md |
| C1 Sección 2 | ✅ DRAFT s30 | IRAM_C1_s2_draft_s30.md |
| C1 Sección 3 | ✅ DRAFT s20 | IRAM_C1_s3_draft_s20.md |
| C1 Sección 4 | ✅ DRAFT s30 | IRAM_C1_s4_draft_s30.md |
| C1 Sección 5 | ✅ DRAFT s29 | IRAM_C1_s5_draft_s29.md |
| C1 Sección 6 | ✅ DRAFT s30 | IRAM_C1_s6_draft_s30.md |
| C1 Sección 7 | ✅ DRAFT s30 | IRAM_C1_s7_draft_s30.md |
| C2 — Skill operacional | ✅ VIGENTE por ahora | Revisar después de nuevo C1 |
| Correcciones finales paper | ✅ EJECUTADAS (s30) | S2, S4, S6, S7 corregidas. INC-13 pendiente fuente primaria. |
| T1 — Complejidad habilitada | ✅ COMPLETADA en s28 | Incorporada en S5 |
| T2 — Autoría real | ✅ COMPLETADA en s28 | Incorporada en S5 y S4A |

---

## HITOS METODOLÓGICOS — ESTADO AL 2026-06-12

*(Fuente: IRAM_hitos_metodologicos_2026-06-12_v7.md — documento definitivo)*

**Historia del mod técnico:**
- [✅] primeros_scripts — 2026-04-16 (CLAUDE_1) — Colaborativo
- [✅] distribucion_alt — v2: dos cambios (spawn rival + war=no)
- [✅] rename_IRAM — No cosmético — cambio de categoría del objeto
- [✅] sistema_de_versiones — formalizado ~2026-05-26, primer zip ~2026-05-27
- [✅] primera_auditoria_formal — 2026-05-30, CLAUDE_1, Optimize cleanup visible en v4.3.13/14

**Historia del sistema de documentación:**
- [✅] primera_wiki — 2026-04-17 (CLAUDE_2) — `exodus_backup_tecnico_v5.md`
- [✅] technical_wiki_split — 2026-05-27 (CLAUDE_3) — SUPERBACKUP→TECHNICAL_WIKI + ACTIVE/ARCHIVE
- [✅] primer_PROMPT_MAESTRO — 2026-05-16 (CLAUDE_1, conv_45)
- [✅] primer_SESSION_LOG — concepto: 2026-05-23; archivo: 2026-05-25; formalizado: 2026-05-26
- [✅] separacion_ACTIVE_ARCHIVE — 2026-05-27 20:28 (CLAUDE_3)
- [✅] tres_capas_lenguaje — hito metodológico confirmado
- [✅] mecanismo_generador_reglas — visible en backup IRAM 1.5.1 — bug→patrón→regla
- [✅] git_init — 2026-05-28 (CLAUDE_1)
- [✅] session_log_consolidado — 2026-06-04 (CLAUDE_4) — Temporal/situacional
- [✅] zips_wip_por_tarea — 2026-06-06 (CLAUDE_3) — Temporal/situacional
- [✅] minilogs_por_tarea — 2026-06-06 (CLAUDE_3) — Temporal/situacional
- [✅] RD1_potential_minimo — 2026-06-04 (CLAUDE_4) — Permanente
- [✅] R19_confirm_before_modify — 2026-05-30 (CLAUDE_1) — Permanente
- [✅] RE6_building_names — 2026-05-27 (CLAUDE_2) — Permanente

**Pendientes de formalizar:**
- [⚠️] rotacion_de_contextos — sistema multi-cuenta como solución al límite de tokens
- [🔍] contrafactico_experimento_natural — 4 puntos de corte, interrupted time series
- [🔍] origen_backup_causalidad_operativa — el backup creció por pérdidas concretas, no por diseño

**Falsos positivos confirmados:**
- [❌] cuentas_paralelas — descartado. Modelo correcto: rotación secuencial (R18)
- [❌] ZIPs_WIP y MINILOGs fecha_script — script detectó 2026-05-05, evidencia directa: 2026-06-06

**Transiciones de cuenta:**
- [✅] CLAUDE_1 → conv_45 → PROMPT_MAESTRO (2026-05-16)
- [⚠️] CLAUDE_1→2, 2→3, 3→4, 4→5: fechas exactas pendientes

---

## FASES DEL PROYECTO

| Versión | Nombre | Cambio definitorio | Evidencia |
|---------|--------|-------------------|-----------|
| v1 | Drago stable | Spawn en capital, war=no | zip + backup 1.3.5 |
| v2 | Drago alt | Spawn rival + war opcional | zip + backup alt 1.3 |
| v3 | IRAM | Rename + Optimize + unificación técnica | zip + backup IRAM 1.5.1 |
| v4.0 | IRAM expansión | Modelo económico, demografía, constructor | zip v4.1 + SUPERBACKUP v2.1 |
| v4.3.16 | IRAM expansión | Última v4 — cierre 2026-05-30 03:14 | zip v4.3.16 + conversations.json |
| v5.0→v5.5 | IRAM final | Modularidad 4 mods + namespace iram_ | conversations.json + SESSION_LOGs |

Salto arquitectónico mayor: v2→v3 (on_action 199→896 líneas, 4.5x). V1-V4 = prototipado. V5 = ingeniería deliberada.

---

## ESTADO DE LOS DATOS (al 2026-06-17)

| Dato | Estado |
|------|--------|
| JSON disponibles | CLAUDE_1 a CLAUDE_5 (procesados 2026-06-12) |
| Processed JSON | ✅ claude_N_processed.json ×5 — Plantilla D ejecutada, usados en s28 |
| Wiki ACTIVE | v3.10 |
| Wiki ARCHIVE | v3.7 |
| Zip canónico | v5.5 |
| Historia completa | IRAM_HISTORIA_COMPLETA_v1_2.md (v1→v5.5 completo) |
| Hitos | IRAM_hitos_metodologicos_2026-06-12_v7.md (definitivo) |
| Historial unificado | 441 convs / 7345 msgs post-dedup / 5 cuentas / 3.6MB |
| Análisis cuantitativo | Bloques 0-3 completos; datos de S5 calculados en s28 |
| Marco teórico | ✅ COMPLETO — 13 clusters (ver abajo) |

---

## MARCO CONCEPTUAL — 13 CLUSTERS

*(Recuperado de SESSION_LOG s19 en s23. Actualizado a 13 en s27 con DEC-20.)*

1. Pipeline ETL — conversations.json → deduplicación → historial unificado
2. Deduplicación de dataset — eliminación de mensajes duplicados antes del análisis
3. Interrupted time series / experimento natural — 4 puntos de corte estructurales
4. Grid search — barrido de parámetros en función de optimización
5. Incertidumbre epistémica / sensitivity analysis — valor_rp con rango [min, max]
6. RAG manual — contexto cargado por capas (ACTIVE/ARCHIVE + PROMPT + SESSION_LOG)
7. Human-in-the-Loop (HITL) — operador diseña arquitectura, IA implementa
8. Blameless post-mortem / mejora de proceso — bug → patrón → regla → documento
9. Deuda técnica (tres tipos) — namespace pollution, coupling, monolith → v4→v5
10. State management / context passing — SESSION_LOG como handoff entre instancias
11. Prompt engineering: posición como variable de diseño — primer mensaje vs adjunto
12. Specification-driven development — 75 msgs diseño → 13 tareas sin decisiones pendientes
13. Architecture Decision Records (ADRs) orientados a IA — audiencia sin memoria

---

## ARCHIVOS OBSOLETOS A ELIMINAR

| Archivo | Razón |
|---------|-------|
| SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s20.md | Reemplazado por SESSION_LOG_DOCUMENTACION_s29.md |
| SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md | Reemplazado por SESSION_LOG_DOCUMENTACION_s29.md |
| SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19.md | Reemplazado desde s20 |
| PROMPT_DOCUMENTACION_IRAM_v1.9.md | Reemplazado por los cuatro archivos del nuevo sistema |
| WIKI_DOCUMENTACION_v1.md | Reemplazado por este archivo |

---

*WIKI DOCUMENTACIÓN v2.0 — 2026-06-17 (s30)*
*Correcciones respecto a v1: pie actualizado a s29; Marco Conceptual 13 clusters completo; tabla SECUENCIA DE TRABAJO actualizada (todas las secciones del paper ✅); METODOLOGIA_DOCUMENTACION_v1.md agregada a tabla de documentos; DEC-03 sesión de origen corregida a s22.*
*Decisiones ejecutables en SESSION_LOG_DOCUMENTACION_s30.md.*
