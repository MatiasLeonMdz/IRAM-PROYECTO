# IRAM — Cierre de deuda documental: gap v4.1→v4.3.16
**Estado:** ✅ GAP CERRADO — fuente primaria: conversations.json (5 cuentas)
**Generado:** 2026-06-11
**Reemplaza a:** `IRAM_gap_v4_1_a_v4_3_16_nota_deuda.md`

---

## Resumen ejecutivo

El gap v4.1→v4.3.16 se cerró procesando los 5 conversations.json (CLAUDE_1 a CLAUDE_5, ~441 conversaciones totales). La nota de deuda original era correcta en sus implementaciones confirmadas pero incompleta en fechas, autoría y secuencia. El período involucra trabajo distribuido entre **5 cuentas simultáneamente** — no solo CLAUDE_1 y CLAUDE_3 como estimaba la nota.

**Corrección crítica:** v4.3.16 no fue generada por "Tarea de sesión con archivos" (82 msgs) sino por "ESTADO ACTUAL 30/05" (50 msgs). Ambas son de CLAUDE_1 el 2026-05-30, pero son sesiones distintas.

---

## Timeline completo v4.1 → v4.3.16

### Pre-período — Diseño base (contexto necesario)

| Fecha | Cuenta | Sesión | Resultado |
|---|---|---|---|
| 2026-05-11 | CLAUDE_4 | 'Diseño de decisiones de optimización para IRAM mod' (38 msgs) | Diseño on_action completo del Optimize ORIGINAL (17 rangos). Este es el sistema v3, **no** Optimize Global. |
| 2026-05-12 | CLAUDE_4 | 'Renombrar keys de decisiones en Exodos: Optimizar' (52 msgs) | Nomenclatura del optimize legacy cerrada. |
| 2026-05-15 | CLAUDE_5 | 'Revisión de superbackup del ecosistema' (26 msgs) | Primera mención documentada de `iram_13` — el ID del Optimize Global ya estaba planeado. |
| ~2026-05-16 | CLAUDE_2 | 'Revisión integral de IRAM v4' (6 msgs) | Segunda mención de `iram_13`. El nombre de función global ya estaba en el SUPERBACKUP. |

### Período central (2026-05-22 → 2026-05-30)

#### 2026-05-22

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_1 | 'v4' (72 msgs) | → v3.3/v3.4 backup | Fix Gather Global capital exclusion (`NOT = { is_capital = yes }` en 21 bloques de `exodos_on_action.txt`). Fix BOM-como-texto en `exodos_decisions_optimize.txt`. Fix relics tokens (`picture`→delete, `gold`→`treasury`, `add_gold`→`add_treasury`). **No es la primera implementación de Optimize Global** — Optimize ya existía, esto es refinamiento. |
| CLAUDE_2 | 'v4.0' (6 msgs) | — | Sesión corta de contexto, continuación. |

#### 2026-05-23

| Cuenta | Sesión | Qué ocurrió |
|---|---|---|
| CLAUDE_3 | '23/05/2026 2:48 am' (130 msgs) | **Demografía — Ascenso/Descenso forzado.** La migración forzada ya estaba en el zip (`mod_pack_IRAM_15_GATHER_GLOBAL_v1_3.zip`, con `iram_decisions_migracion.txt`). Esta sesión **agregó** los modificadores de movilidad social (`global_pop_promotion_speed`, `global_pop_demotion_speed`) al modifier existente de migración. Origen de Ascenso/Descenso Forzado confirmado. |

#### 2026-05-25–26

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_1 | 'Actualización de documentación y logs de superbackup' (22 msgs) | v4.3.2 | Primer registro de versión v4.3.x en el historial. |
| CLAUDE_1 | **'Cálculo incorrecto de thresholds de esclavos' (50 msgs)** | — | **Diseño final de Optimize Global.** Calibración del threshold por province: `(minas × 10) + (basic_settlement × 10) + (latifundia × 15)`. Identificación de error: se estaba usando base 15 para cities, el correcto es 20. Diseño de `iram_script_values.txt` (dinámico, no hardcoded). Operación en 2 pasos: validación del ancla + distribución por building. Diseño CERRADO. |

#### 2026-05-27 — Día de alta densidad (múltiples cuentas)

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_2 | 'Qué sigue' ×3 (0, 12, 32 msgs) | v4.3.4/5 | Sesiones cortas de coordinación post-corte. |
| **CLAUDE_2** | **'Ejecución de tareas pendientes IRAM' (58 msgs)** | → v4.3.6 | **Diseño del Constructor Automático (iram_12).** Clarificación del mecanismo de buildings: `fortress_building` (no `hill_fort`) es el fuerte real. Error crítico de nomenclatura descubierto y corregido. **RE6 agregado al PROMPT_MAESTRO**: "verificar nombre exacto de building en `00_default.txt` antes de codear". |
| **CLAUDE_3** | **'Prioridades del proyecto: constructor automático o reestructuración' (30 msgs)** | → v4.3.7 | **HITO: Origen del TECHNICAL_WIKI y split ACTIVE/ARCHIVE.** Sesión estratégica que decide: SUPERBACKUP → TECHNICAL_WIKI (nombre más profesional), split en ACTIVE (sesiones v4 completas) + ARCHIVE (historial v1-v3). Discusión sobre git history reconstruction con conversations.json descargados. SUPERBACKUP v2.5 → v2.6 generado. |
| CLAUDE_4 | 'Implementación de iram_12_constructor_auto' ×2 (2, 24 msgs) | — | Constructor iram_12 en progreso — stubs. |
| CLAUDE_5 | 'Implementar constructor automático iram_12' (28 msgs) | — | Más trabajo en iram_12. |

#### 2026-05-28

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_1 | 'Falta bloque PASO 1 del prompt maestro' (46 msgs) | → v4.3.8 | **Git inicializado por primera vez.** `git init` con v4.3.7 como commit inicial. Usuario identificado: Matia (`matia@DESKTOP-HKF1O8U`). Diseño de iram_11 (Distribute Global) e iram_13 (Optimize Global on_action) en progreso. `iram_script_values.txt` confirmado en contexto. |
| CLAUDE_2 | 'LOG NO COMPLETADO' | → v4.3.9 | Sesión que generó v4.3.9. Log truncado. |
| CLAUDE_4 | 'IRAM v4.3.8 carga completada' (6 msgs) | v4.3.8 confirmado | Auditoría: iram_11, iram_12, iram_13 son **stubs** en v4.3.8. El código de las 3 funciones aún no estaba escrito. |

#### 2026-05-29

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_3 | **'Orden de ejecución para optimización iram_13' (104 msgs)** | v4.3.9 → v4.3.10+ | **HITO: Implementación de iram_13 Optimize Global.** Desde v4.3.9. Pasos: (1) Limpieza de `exodos_gather_global_completed` (variable obsoleta + `on_yearly_pulse` eliminado + `exodos.3` prep). (2) iram_13 on_action: 5 bloques `monthly_country_pulse`, estructura idéntica a DG pero con lógica de slaves de `iram_optimize_threshold`. (3) Textos finales de iram_11/12/13 en ES y EN (ciclo IRAM documentado en UI). |
| CLAUDE_4 | 'Sesión de análisis de archivos técnicos' | → v4.3.12 | Versiones intermedias v4.3.10/11/12 generadas en esta cadena. |
| CLAUDE_1 | 'Actualizar wiki técnico con logs de sesión' (22 msgs) | → v4.3.11 | Actualización de wiki con los logs del período. |

#### 2026-05-30 — Cierre de v4

| Cuenta | Sesión | Versiones | Qué ocurrió |
|---|---|---|---|
| CLAUDE_1 | **'Tarea de sesión con archivos' (82 msgs)** | → v4.3.13 | Code review y cleanup de código. Análisis de bloat en on_action. Fixes: `trigger_event = { id = exodos.2 }` en Distribute Global y Optimize Global. |
| CLAUDE_1 | **'ESTADO ACTUAL 30/05' (50 msgs)** | → **v4.3.14 / v4.3.15 / v4.3.16** | **Sesión de cierre de v4.** 4 fixes finales (BUG A/B/C + estructural). **R19 agregado al PROMPT_MAESTRO**: "Antes de modificar cualquier archivo: describir el cambio en una oración y esperar confirmación explícita." `exodos.3` eliminado en v4.3.14 (limpieza definitiva del mecanismo anual). **`mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` — versión canónica final.** Hora: 03:14. |

---

## Implementaciones — fechas y autoría confirmadas

### Optimize Global (`iram_13`)

| Dimensión | Dato |
|---|---|
| **Diseño del threshold** | 2026-05-26, CLAUDE_1 ('Cálculo incorrecto de thresholds') |
| **`iram_script_values.txt`** | Primer registro: 2026-05-28 (CLAUDE_1/CLAUDE_2) |
| **Implementación on_action** | 2026-05-29, CLAUDE_3 ('Orden de ejecución para optimización iram_13') |
| **Versión de implementación** | v4.3.10+ (post v4.3.9) |
| **Autoría** | Colaborativo — Operador diseñó threshold, CLAUDE_3 implementó 5 bloques |

### Constructor Automático (`iram_12`)

| Dimensión | Dato |
|---|---|
| **Diseño** | 2026-05-27, CLAUDE_2 ('Ejecución de tareas pendientes') + CLAUDE_4 |
| **Error clave descubierto** | `hill_fort` ≠ fuerte real — el fuerte es `fortress_building` |
| **Estado en v4.3.8** | Stub (código no escrito) |
| **Implementación completa** | Entre v4.3.8 y v4.3.13 (requiere verificación exacta) |
| **Autoría** | Colaborativo — Operador corrigió terminología, Claude implementó |

### Distribute Global (`iram_11`)

| Dimensión | Dato |
|---|---|
| **Diseño** | 2026-05-28, CLAUDE_1 ('Falta bloque PASO 1') |
| **Estado en v4.3.8** | Stub |
| **Autoría** | Colaborativo |

### Demografía — Migración Forzada

| Dimensión | Dato |
|---|---|
| **Primera evidencia** | 2026-05-23 CLAUDE_3: ya estaba en `mod_pack_IRAM_15_GATHER_GLOBAL_v1_3.zip` |
| **Fecha de implementación** | **Antes de 2026-05-23** — sesión de origen no identificada en este análisis |
| **Deuda residual** | Buscar en CLAUDE_1-5 antes de 2026-05-22 la primera sesión con `iram_decisions_migracion.txt` |

### Demografía — Ascenso/Descenso Forzado

| Dimensión | Dato |
|---|---|
| **Primera evidencia** | 2026-05-23, CLAUDE_3 ('23/05/2026 2:48 am', 130 msgs) |
| **Qué se hizo** | Se agregaron `global_pop_promotion_speed` y `global_pop_demotion_speed` al modifier de migración existente |
| **Trigger** | Pregunta del operador: "y la velocidad de ascenso descenso de pops?" |
| **Autoría** | Operador (inició idea), Colaborativo (implementación) |

---

## Hitos metodológicos confirmados (nuevos respecto a hitos_v5)

### TECHNICAL_WIKI — fecha y origen exactos

| Dimensión | Dato |
|---|---|
| **Fecha exacta** | 2026-05-27 (tarde) |
| **Cuenta** | CLAUDE_3 |
| **Sesión** | 'Prioridades del proyecto: constructor automático o reestructuración' |
| **Autoría** | Colaborativo — Claude analizó el SUPERBACKUP v2.5 (4957 líneas) y propuso la reestructuración; Operador eligió nombre y aprobó split |
| **Causalidad** | SUPERBACKUP crecía sin estructura → split ACTIVE (operativo) / ARCHIVE (legacy) |
| **Ciclo de vida** | Permanente |
| **Transición de cuenta** | No detonado por transición — fue una decisión estratégica durante sesión activa |

### Git — primer inicialización

| Dimensión | Dato |
|---|---|
| **Fecha exacta** | 2026-05-28 |
| **Cuenta** | CLAUDE_1 |
| **Sesión** | 'Falta bloque PASO 1 del prompt maestro' |
| **Primer commit** | IRAM v4.3.7 — "Historial completo en TECHNICAL_WIKI Secciones 14 y 19" |
| **Herramienta** | Git Bash → GitHub Desktop (simplificación) |
| **Causalidad** | Necesidad de backup robusto y control de versiones |
| **Ciclo de vida** | Permanente |

### R19 — confirm before modifying

| Dimensión | Dato |
|---|---|
| **Fecha exacta** | 2026-05-30 (sesión 03:14) |
| **Cuenta** | CLAUDE_1 |
| **Sesión** | 'ESTADO ACTUAL 30/05' |
| **Texto** | "Antes de modificar cualquier archivo: describir el cambio en una oración y esperar confirmación explícita del operador. Sin excepción." |
| **Causalidad** | Claude ejecutó 4 fixes sin confirmación; Operador lo detectó y preguntó "¿en qué fallan las instrucciones?" → Claude diagnosticó que el protocolo estaba en la Plantilla A pero no en las reglas numeradas → R19 creada y numerada |
| **Autoría** | Claude (diagnóstico + texto), Operador (aprobación) |
| **Ciclo de vida** | Permanente |

### RE6 — building names from source

| Dimensión | Dato |
|---|---|
| **Fecha exacta** | 2026-05-27 |
| **Cuenta** | CLAUDE_2 |
| **Sesión** | 'Ejecución de tareas pendientes IRAM' |
| **Texto** | "Antes de usar cualquier nombre de building en código o diseño: verificar el nombre exacto en `common/buildings/00_default.txt` del game.zip." |
| **Causalidad** | Claude usó `hill_fort` como nombre del fuerte durante toda la sesión; el fuerte real es `fortress_building`. Errores de nomenclatura → tokens desperdiciados |
| **Autoría** | Colaborativo — Operador señaló error, Claude propuso regla |
| **Ciclo de vida** | Permanente |

---

## Correcciones a la nota de deuda original

| Ítem en nota original | Realidad confirmada |
|---|---|
| "Primera sesión de v4.3.16: CLAUDE_1 'Tarea de sesión con archivos' (82 msgs)" | v4.3.13 fue 'Tarea de sesión con archivos'. v4.3.16 fue 'ESTADO ACTUAL 30/05' (50 msgs). Ambas en CLAUDE_1 el 2026-05-30, pero son sesiones distintas. |
| "Sesiones identificadas: solo CLAUDE_1 y CLAUDE_3" | El período involucra los 5 Claudes simultáneamente. CLAUDE_2: diseño iram_12 + RE6. CLAUDE_4: Constructor + auditorías. CLAUDE_5: iram_12 paralelo. |
| "Constructor automático diseñado ~2026-05-27" | ✅ CONFIRMADO — CLAUDE_2 y CLAUDE_4 en 2026-05-27 |
| "Optimize Global — diseño cerrado en SUPERBACKUP v2.1" | El threshold final se cerró en CLAUDE_1 2026-05-26, DESPUÉS del SUPERBACKUP v2.1 |
| "Transición CLAUDE_3 — sesión estratégica 2026-05-27" | ✅ CONFIRMADO — pero no era transición de cuenta, era sesión activa de CLAUDE_3 |

---

## Deuda residual (lo que sigue faltando)

| Qué | Por qué falta | Cómo resolver |
|---|---|---|
| Fecha exacta de migración forzada (`iram_decisions_migracion.txt`) | La evidencia muestra que ya existía el 2026-05-23 pero el origen está antes de la ventana analizada | Buscar en CLAUDE_1-5 antes del 2026-05-22 con keyword `iram_decisions_migracion` |
| Versión exacta donde iram_11 (DG) se implementó (no stub) | Se sabe que era stub en v4.3.8 y estaba en v4.3.14; la sesión de implementación es v4.3.9-v4.3.13 | Leer CLAUDE_3 2026-05-29 desde msg 35+ para ver si DG se implementó ahí |
| Transiciones de cuenta CLAUDE_1→2, 2→3, 3→4, 4→5 (fechas exactas) | El análisis se enfocó en el gap técnico, no en las transiciones | Buscar en cada JSON la primera sesión cargando el PROMPT_MAESTRO completo |

---

## Mapa de versiones v4.3 — completado

| Versión | Fecha | Cuenta(s) | Cambio principal |
|---|---|---|---|
| v4.3.2 | 2026-05-25 | CLAUDE_1 | Primera v4.3 documentada |
| v4.3.3 | 2026-05-27 | CLAUDE_1 | — |
| v4.3.4/5 | 2026-05-27 | CLAUDE_2 | Sesiones cortas post-corte |
| v4.3.6 | 2026-05-27 | CLAUDE_1/2 | Auditoría + bugs. SUPERBACKUP v2.5 |
| v4.3.7 | 2026-05-27 | CLAUDE_2/3 | TECHNICAL_WIKI creado. Git init. |
| v4.3.8 | 2026-05-28 | CLAUDE_1 | Diseño iram_11/13. iram_12 stub. |
| v4.3.9 | 2026-05-28 | CLAUDE_2 | (LOG NO COMPLETADO) |
| v4.3.10 | 2026-05-29 | CLAUDE_3/4 | iram_13 on_action implementado |
| v4.3.11 | 2026-05-29 | CLAUDE_1 | Wiki actualizada |
| v4.3.12 | 2026-05-29 | CLAUDE_4 | Análisis técnico |
| v4.3.13 | 2026-05-30 | CLAUDE_1 | Code review, bloat cleanup, bug fixes |
| **v4.3.14** | 2026-05-30 | CLAUDE_1 | `exodos.3` eliminado, legacy cleanup |
| v4.3.15 | 2026-05-30 | CLAUDE_1/2 | Costos eliminados para test |
| **v4.3.16** | 2026-05-30 | CLAUDE_1 | Fixes A/B/C + R19 + cierre definitivo |

---

## Dónde incorporar en los documentos existentes

| Documento | Sección | Qué agregar |
|---|---|---|
| `IRAM_HISTORIA_COMPLETA_v1_1.md` | Parte II — Sección 1 (gap) | Reemplazar el placeholder con la narrativa completa de este documento |
| `IRAM_hitos_metodologicos_2026-06-10_v5.md` | Hitos con ⚠️ | Resolver: `primera_auditoria_formal` (v4.3.13/14), `technical_wiki` (2026-05-27 CLAUDE_3), transiciones de cuenta |
| `IRAM_hitos_metodologicos_2026-06-10_v5.md` | Hitos metodológicos nuevos | Agregar: Git inicialización (2026-05-28), R19 (2026-05-30), RE6 (2026-05-27) |

---

*Gap v4.1→v4.3.16 — CERRADO*
*Fuente primaria: conversations.json CLAUDE_1 a CLAUDE_5*
*Período analizado: 2026-05-08 → 2026-05-30*
*Sesiones revisadas en profundidad: 12 | Keyword searches: 5*
