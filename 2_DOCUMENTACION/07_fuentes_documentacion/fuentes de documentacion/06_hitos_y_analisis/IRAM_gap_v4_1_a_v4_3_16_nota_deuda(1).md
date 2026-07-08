# IRAM — Nota de deuda documental: gap v4.1→v4.3.16
**Para incorporar en:** `IRAM_BACKUP_ESTRATEGICO_v4_1_a_v5_5.md` Sección 1.4
**Generado:** 2026-06-10 22:16
**Estado:** ⚠️ DEUDA PENDIENTE — documentado formalmente

---

## Qué se sabe del período v4.1→v4.3.16

El SUPERBACKUP v2.1 documenta el estado de v4.0 (2026-05-21). La narrativa v5 documenta el estado de v4.3.16 como punto de partida del rebuild. Entre esos dos puntos, la evidencia disponible sin conversations.json permite reconstruir **qué** se implementó pero no **cómo ni cuándo** con precisión sesión a sesión.

**Implementaciones confirmadas por evidencia indirecta:**

| Implementación | Evidencia | Fuente |
|---|---|---|
| Optimize Global | Presente en v4.3.16, diseño cerrado en SUPERBACKUP v2.1 | SUPERBACKUP v2.1 + narrativa v5 |
| Modelo económico | Presente en v4.3.16, no mencionado en SUPERBACKUP v2.1 | narrativa v5 Sección 1.2 |
| Demografía (migración, ascenso, descenso) | Presente en v4.3.16, en carpeta `exodos/` | narrativa v5 Sección 1.2 |
| Constructor automático | Diseñado ~2026-05-27, presente en v4.3.16 | narrativa v5 Sección 1.2 |
| Reliquia migración (`global_migration_speed = 2.5`) | Token cerrado en SUPERBACKUP v2.1, implementado en v4.x | SUPERBACKUP v2.1 pendiente + BACKUP_ESTRATÉGICO Sección 5.2 |
| Cleanup de Optimize (34KB → 10KB) | Visible en delta de versiones | narrativa v5 comparación v4.1 vs v4.3.16 |

**Sesiones identificadas en el período (índice 7.1 del BACKUP_ESTRATÉGICO):**

| Fecha | Cuenta | Sesión | Resultado aproximado |
|---|---|---|---|
| ~2026-05-22 | CLAUDE_1 | 'v4' (70 msgs) | Optimize Global implementado |
| 2026-05-26 | CLAUDE_1 | 'Cálculo incorrecto de thresholds' (50 msgs) | Corrección modelo económico |
| 2026-05-27 | CLAUDE_3 | 'Prioridades: constructor o reestructuración' | Sesión estratégica + constructor |
| 2026-05-30 | CLAUDE_1 | 'Tarea de sesión con archivos' (82 msgs) | v4.3.16 — última v4 canónica |

---

## Qué falta y por qué importa

**Para la Plantilla D (análisis cuantitativo):**

Este período es el de mayor crecimiento en complejidad del proyecto. El SUPERBACKUP creció de ~50KB (v2.0) a 220KB (v2.x) en este tramo — ese número es la evidencia del crecimiento. Pero sin el detalle de sesiones no se puede calcular:

- Mensajes por versión / sesión en el período v4.x
- Tasa de bugs en el período (hallazgos / líneas de código)
- Distribución de trabajo diseño / implementación / debugging
- Velocidad de implementación por función

**Para el SKILL.md (Plantilla C):**

El período v4.x es donde el sistema de documentación maduró (PROMPT_MAESTRO, SESSION_LOG, split ACTIVE/ARCHIVE). Sin la narrativa detallada de ese período, la historia del SISTEMA de documentación tiene un agujero en su momento de mayor evolución.

**Para R10 (trazabilidad de reglas):**

Las reglas visibles en el backup IRAM 1.5.1 (v3) son el origen — pero el PROMPT_MAESTRO siguió creciendo en v4.x. Identificar qué reglas se agregaron en ese período y qué bug las generó requiere leer las sesiones.

---

## Cómo resolverlo

**Archivos necesarios:** conversations.json de CLAUDE_1, CLAUDE_3 (período 2026-05-22 → 2026-05-30)

**Qué buscar:**
- Primera sesión donde se implementó Optimize Global completo (no solo diseño)
- Primera sesión donde apareció el modelo económico
- Primera sesión de auditoría de código en v4 (primera vez que el cleanup fue sistemático, no puntual)
- Reglas del PROMPT_MAESTRO que se agregaron en este período y el bug que las originó
- Cómo creció el SUPERBACKUP de ~50KB a 220KB — qué sesiones lo hicieron crecer

**Dónde incorporar los resultados:**
- `IRAM_BACKUP_ESTRATEGICO_v4_1_a_v5_5.md` Sección 1 — expandir con narrativa completa del período
- `IRAM_hitos_metodologicos_2026-06-10_v4.md` — completar ⚠️ en `primera_auditoria_codigo` y transiciones de cuenta
- `IRAM_analisis_cuantitativo_[fecha].md` (Plantilla D) — Bloque 1 (velocidad de desarrollo) y Bloque 4 (calidad del proceso)

---

*Nota de deuda documental — 2026-06-10 22:16*
*Gap reconocido, evidencia indirecta preservada, fuente primaria pendiente*
