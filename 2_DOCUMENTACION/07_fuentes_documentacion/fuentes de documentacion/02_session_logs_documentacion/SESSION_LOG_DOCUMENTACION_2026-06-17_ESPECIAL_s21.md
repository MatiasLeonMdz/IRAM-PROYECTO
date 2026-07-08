# SESSION LOG — Documentación IRAM — ESPECIAL s21
**Fecha:** 2026-06-17
**Tipo:** Log de diagnóstico — reemplaza SESSION_LOG s20 como fuente de verdad operativa
**Propósito:** Este log documenta el diagnóstico completo del sistema de documentación descubierto en s21, las correcciones pendientes, y el estado del draft C1. La próxima IA lo usa como spec ejecutable — no como registro histórico.

**La próxima IA recibe:** este LOG + esqueleto s17 + SKILL v1.0 (solo secciones 6, 7, 10) + drafts S1 y S3.
No hace falta cargar el SESSION_LOG s20 ni el s19 — este documento los reemplaza operativamente.

---

## DECISIONES CONFIRMADAS — NO REDEBATIR

| ID | Decisión | Sesión |
|----|----------|--------|
| DEC-01 | El SESSION_LOG de documentación debe ser spec ejecutable para la próxima IA, no registro histórico. Modelo: SESSION_LOG v5.6 del proyecto. | s21 |
| DEC-02 | Las decisiones críticas van en sección DECISIONES CONFIRMADAS con IDs. No en celdas de tabla de estado de documentos. | s21 |
| DEC-03 | El PROMPT_MAESTRO de documentación debe separarse en tres capas: reglas / templates / estado. Las tres cosas no van en el mismo archivo. | s21 |
| DEC-04 | Las templates (A, B, C1, C2, D) salen del PROMPT_MAESTRO. Solo se pega la relevante en PASO 2 de cada sesión. | s21 |
| DEC-05 | El R14 necesita un mecanismo de promoción: las decisiones capturadas en R14 que sean críticas migran a DECISIONES CONFIRMADAS con ID antes de cerrar el log. | s21 |
| DEC-06 | Las reglas del PROMPT deben ser atómicas y causales. Formato: regla + razón en paréntesis + fecha de origen si aplica. Sin prosa narrativa mezclada. | s21 |
| DEC-07 | Cada SESSION_LOG necesita PROTOCOLO DE LA IA EJECUTORA: pasos ordenados, confirmaciones explícitas, condiciones de completitud. | s21 |
| DEC-08 | El PROMPT necesita REGLA DE CONTRADICCIÓN explícita: qué fuente gana cuando SKILL v1.0, SESSION_LOG y esqueleto difieren. | s21 |
| DEC-09 | Estado de documentos, hitos metodológicos y fases del proyecto son contenido de WIKI, no de PROMPT. Sacarlos del PROMPT. | s21 |
| DEC-10 | El Hallazgo A de Sección 4 no es "la IA no diseña" como principio absoluto. Es descripción matizada de la división real de trabajo con casos concretos. | s21 |
| DEC-11 | Fuente de verdad para el draft de Sección 4: SESSION_LOG s19 (MAPPING CORRECCIONES + fuentes primarias), no SKILL v1.0 directamente. El framing del SKILL v1.0 está superado desde s18. | s21 |
| DEC-12 | El SKILL v1.0 es fuente de hechos y ejemplos técnicos. Su framing estructural está superado. El eje del nuevo C1 son las 9 correcciones de s18 y las fuentes primarias de s19. | s18→s21 |

---

## CONTENIDO PERDIDO EN EL PASAJE s19 → s20

Documentado para no repetir el error. Causa raíz: la celda de SKILL v1.0 en la tabla de estado fue reescrita limpia, eliminando la advertencia inline.

| Qué se perdió | Dónde estaba en s19 | Impacto |
|---|---|---|
| ⚠️ SUPERADO EN S18 — el framing del SKILL v1.0 está superado, el eje es las 9 correcciones s18 + fuentes primarias s19 | Celda SKILL v1.0 en tabla de documentos (línea 22, con tachado) | El draft podría haberse basado en el SKILL v1.0 como base estructural — error de criterio |
| MAPPING CORRECCIONES S18 → EVIDENCIA PRIMARIA S19 | Sección completa del s19 (9 filas con corrección + fuente primaria) | Sin este mapa, las 9 correcciones de s18 quedan sin respaldo de fuente |
| 4 hallazgos materiales nuevos de s19 para C1 | DECISIONES CLAVE s19, entradas marcadas [s19] | Información de fuentes primarias (WIKI 0.1c, INC-13, STRATEGIC LOG, cadena SUPERBACKUP) |
| Ajustes al esqueleto identificados en s18 | Sesión 17 del resumen de trabajo s19 | 3 ajustes: Sección 4D (tiering), Sección 7 (circularidad), razón-junto-con-decisión |

---

## DIAGNÓSTICO COMPLETO — SISTEMA DE DOCUMENTACIÓN

### Problema raíz
El sistema de documentación documentó cómo funciona el proyecto pero no aplicó esas lecciones a su propio diseño. Reproduce exactamente los errores que el proyecto resolvió.

### 5 problemas estructurales (comparación directa con proyecto)

**P1 — SESSION_LOG es registro histórico, no spec ejecutable**
- Proyecto: "La próxima IA recibe: PROMPT_MAESTRO + este LOG + ACTIVE + ARCHIVE + zip. No hace falta cargar los archivos originales." La IA siguiente sabe exactamente qué hacer.
- Documentación: narrativa de qué pasó. La IA siguiente tiene que inferir qué hacer.

**P2 — Decisiones viven en celdas de tabla, no en sección protegida**
- Proyecto: DECISIONES CONFIRMADAS — NO REDEBATIR. Tabla separada, IDs, inamovible.
- Documentación: decisiones en celdas de tabla de estado, en notas inline con tachado, en R14. Al actualizar la celda, la decisión desaparece.

**P3 — Reglas narrativas, no atómicas**
- Proyecto: R3 — "R3 anterior decía X — era incorrecto. Corregido 2026-06-04 03:33." Una regla, una corrección, fecha, razón.
- Documentación: párrafos que mezclan instrucción, historia y razonamiento. Una IA de bajo nivel no puede ejecutar sin interpretar.

**P4 — No hay PROTOCOLO DE LA IA EJECUTORA**
- Proyecto: 7 pasos idempotentes. La IA sabe en qué orden hacer las cosas y qué confirmar.
- Documentación: "PENDIENTES" descriptivos que requieren traducción a acciones.

**P5 — No hay REGLA DE CONTRADICCIÓN**
- Proyecto: explícita sobre qué fuente gana cuando zip, WIKI y LOG difieren.
- Documentación: cuando SKILL v1.0 y SESSION_LOG s19 contradicen el enfoque del draft, la IA no tiene criterio para resolver.

### 3 problemas adicionales

**P6 — El PROMPT_MAESTRO es el SUPERBACKUP problem reencarnado**
El PROMPT v1.9 tiene ~500 líneas mezclando: reglas, 5 templates completas (~150 líneas de ruido constante), estado de documentos, hitos metodológicos, fases del proyecto, estado de datos. Es el monolito que el propio proyecto documentó como falla. Nunca se aplicó la separación PROMPT / WIKI / SESSION_LOG al sistema de documentación.

**P7 — Templates dentro del PROMPT generan ruido constante**
Al draftear Sección 3, la IA tiene en contexto las instrucciones completas de Plantilla A, B, C2 y D — irrelevantes para esa tarea. ~150 líneas compitiendo con las instrucciones relevantes.

**P8 — R14 captura decisiones pero no las protege**
El R14 genera texto narrativo en tabla. No hay mecanismo para promover esas decisiones a estado protegido. La decisión "posición y formato" de s20 está en el R14 pero no en ninguna sección que garantice que no se rediscuta.

---

## MAPPING CORRECCIONES S18 → EVIDENCIA PRIMARIA S19
*(recuperado del s19 — no perder de nuevo)*

| Corrección (s18) | Fuente primaria (s19) |
|---|---|
| C1: IA ejecuta pensamiento estructurado, no democratiza | WIKI 0.1c: "saltear boilerplate, no evitar el trabajo difícil" |
| C2: instrucción mal seguida = posición y formato, no contenido | AVISO DE CARGA: primera instrucción del PROMPT_MAESTRO v5.2 |
| C3: "no es posible" = hipótesis verificable | INC-13 NOTA del SESSION_LOG v5.6: auditoría recomendó lo contrario, engine fue el árbitro |
| C4: rotación secuencial, no paralelo | "La próxima IA recibe: PROMPT_MAESTRO + este LOG" — handoff textualmente documentado |
| C5: ratio creciente = planificación deliberada | FASE 1/2/3 del SESSION_LOG v5.6 + tabla Inv/Código del paper v1.0 |
| C6: rol arquitecto se articuló más, no se delegó | STRATEGIC LOG: "La IA no pudo resolver esos problemas" — fuente primaria 2026-05-27 |
| C7: sistema evolucionó por presión | Cadena SUPERBACKUP v1.1→v2.0 con fechas exactas y versiones |
| C8: criterio se trajo de antes | STRATEGIC LOG: "IRAM confirma transferencia de habilidades, no aprendizaje desde cero" |
| C9: práctica sin condición = overhead | Paper v1.0 Sec 5: ciclo de vida + condiciones de activación ya documentadas |

---

## AJUSTES AL ESQUELETO s17 — INCORPORAR DURANTE EL DRAFT
*(recuperados del s19, perdidos en s20)*

1. **Sección 4D** — tiering como hallazgo operacional propio (diseño en alto / ejecución en bajo)
2. **Sección 7** — resolución a la circularidad criterio-preexistente / habilidades-entrenadas: criterio general → especializado por el proyecto. Ambas cosas son simultáneamente ciertas sin contradicción.
3. **Razón-junto-con-decisión** — lugar propio en el paper, no solo mención en ADRs.

---

## ESTADO DEL DRAFT C1

| Sección | Estado | Notas |
|---------|--------|-------|
| S1 — El laboratorio | ✅ DRAFT s20 | IRAM_C1_s1_draft_s20.md |
| S2 — Lo que tuvimos que construir | ❌ PENDIENTE | — |
| S3 — Hallazgo central (posición y formato) | ✅ DRAFT s20 | IRAM_C1_s3_draft_s20.md — ajuste "posición y formato" incorporado |
| S4 — Tres hallazgos con casos | ❌ PENDIENTE — próxima | Ver PROTOCOLO abajo |
| S5 — Los datos del proceso | ❌ PENDIENTE — bloqueada parcialmente | Requiere T1, T2 (JSONs ×5) + WIKI ACTIVE Sec 12 |
| S6 — Conceptos formales | ❌ PENDIENTE | — |
| S7 — Qué transfiere y qué no | ❌ PENDIENTE | Tiene fuente primaria: STRATEGIC LOG 2026-05-27 |

---

## DOS OPCIONES PARA PRÓXIMA SESIÓN

**Opción A — Corregir el sistema primero, luego draft**
Generar PROMPT_MAESTRO de documentación v2.0 con las correcciones de DEC-03 a DEC-09.
Ventaja: el draft de S4 en adelante se produce con el sistema correcto.
Costo: una sesión entera sin avance en el draft.

**Opción B — Draft S4 ahora, corregir el sistema al cierre**
Usar este log como fuente de verdad operativa y continuar.
Ventaja: avance concreto en el paper.
Costo: el sistema sigue roto hasta que se corrija.

Recomendación: Opción B — este log es suficientemente robusto para operar correctamente. El PROMPT se corrige cuando el draft esté más avanzado.

---

## PROTOCOLO PARA PRÓXIMA SESIÓN — DRAFT SECCIÓN 4

**Qué cargar:**
1. Este log (SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md)
2. IRAM_C1_esqueleto_s17.md
3. IRAM_SKILL_desarrollo_con_IA_v1_0.md — solo Secciones 6, 7, 10 (hechos y ejemplos técnicos)
4. IRAM_C1_s1_draft_s20.md y IRAM_C1_s3_draft_s20.md — para consistencia de voz

**Fuente de verdad para S4:** MAPPING CORRECCIONES s18→s19 (tabla arriba) + DECISIONES CONFIRMADAS de este log. No el SKILL v1.0 como base estructural.

**Para cada hallazgo:**

*4A — División de trabajo operador/IA*
- No es principio absoluto (DEC-10). Es descripción matizada con casos concretos.
- Fuente primaria: WIKI 0.1c ("La IA no pudo resolver esos problemas" + "saltear boilerplate, no evitar el trabajo difícil")
- Caso concreto: INC-13 NOTA del SESSION_LOG v5.6 — auditoría recomendó remover inline, operador cuestionó, engine fue el árbitro.
- Concepto formal: HITL + spec-driven development (75 msgs diseño → 13 TAREAs atómicas sin decisiones pendientes)

*4B — Modo de falla epistémico*
- 2 casos canónicos: scripted_gui (gaps A.1) + scopes globales (gaps A.2)
- Caso más específico: INC-13 (ver arriba) — el más concreto de todo el proyecto
- Patrón idéntico en los tres: "no" desde conocimiento documentado → operador cuestiona desde lógica → árbitro es el sistema real, nunca la IA
- Concepto formal: failure mode classification por fuente (epistémico vs. técnico)

*4C — Decisiones descartadas con audiencia propia*
- Fuente primaria: HISTORIA_COMPLETA Sección 18 — terminología "conocimiento recuperado" (ARCHIVE Sec 18.4)
- La sección de alternativas evaluadas estaba dirigida a la IA futura, no al operador
- Concepto formal: Architecture Decision Records (ADRs) orientados a IA

*4D — Tiering como hallazgo operacional (ajuste s18)*
- Diseño en alto / ejecución en bajo
- Techo por sesión: ~1 consigna mediana o 2 ligeras en modo max
- No era principio vago — es límite operacional concreto documentado en s12

**Formato de entrega:** IRAM_C1_s4_draft_s21.md — archivo único con las 4 subsecciones.

---

## CORRECCIONES PENDIENTES AL PROMPT_MAESTRO DE DOCUMENTACIÓN
*(para cuando se aborde — no bloquean el draft)*

1. Separar en tres archivos: PROMPT_REGLAS (reglas puras) / PROMPT_TEMPLATES (una por sesión) / WIKI_DOCUMENTACION (estado, hitos, fases)
2. Agregar REGLA DE CONTRADICCIÓN: SESSION_LOG especial s21 > SESSION_LOG s19 > SKILL v1.0 en framing; SKILL v1.0 > todo en hechos técnicos y ejemplos concretos
3. Convertir reglas narrativas en atómicas con causalidad en paréntesis
4. Agregar regla de consolidación: al generar SESSION_LOG nuevo, comparar sección por sección contra el anterior — toda sección presente debe aparecer o estar marcada como "incorporada en X" / "descartada porque Y" — nunca reescribir celdas existentes de tabla, solo agregar al final
5. Agregar PROTOCOLO DE LA IA EJECUTORA a cada SESSION_LOG
6. Agregar mecanismo de promoción R14 → DECISIONES CONFIRMADAS

---

*SESSION_LOG ESPECIAL s21 — 2026-06-17*
*Generado para corregir pérdida de información s19→s20 y diagnosticar fallas estructurales del sistema de documentación.*
*Este log opera como fuente de verdad hasta que se genere PROMPT_MAESTRO documentación v2.0.*
