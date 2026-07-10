ï»¿# IRAM SESSION LOG — Auditoría consolidada + plan ejecución v5.6
**Fecha:** 2026-06-09 17:59
**Versión inicio:** v5.5 | **Versión objetivo:** v5.6
**Zip de trabajo:** `mod_pack_IRAM_v5_5_2026-06-09_03-22.zip`
**Wiki:** ACTIVE v3.10 / ARCHIVE v3.7

---

## PROPÓSITO DE ESTE LOG

Fuente única para la próxima sesión. Contiene la auditoría completa (35 hallazgos,
3 rondas deduplicadas), todas las decisiones confirmadas por el operador, y el plan
de ejecución con patrones de código exactos.

La próxima IA recibe: PROMPT_MAESTRO + este LOG + ACTIVE + ARCHIVE + zip.
No hace falta cargar los archivos de auditoría originales.

---

## RUTAS REALES DEL ZIP — VERIFICADAS CON unzip -l

Prefijo `iram_work/` en todas las rutas. El árbol de Sec 3.2 del ACTIVE tiene
`common/decisions/` para exodos y BOM — incorrecto. La tabla Sec 3.3 ya usa rutas
correctas. El árbol se corrige en TAREA 11B.

| Módulo | Tipo | Ruta real en el zip |
|---|---|---|
| exodos | decisions | `iram_work/exodos/decisions/` |
| exodos | on_action | `iram_work/exodos/common/on_action/` |
| exodos | scripted_effects | `iram_work/exodos/common/scripted_effects/` |
| exodos | events | `iram_work/exodos/events/` |
| exodos | loc ES | `iram_work/exodos/localization/spanish/` |
| exodos | loc EN | `iram_work/exodos/localization/english/` |
| by_other_means | decisions | `iram_work/by_other_means/decisions/` |
| by_other_means | scripted_effects | `iram_work/by_other_means/common/scripted_effects/` |
| by_other_means | loc ES | `iram_work/by_other_means/localization/spanish/` |
| by_other_means | loc EN | `iram_work/by_other_means/localization/english/` |
| the_great_leap | decisions | `iram_work/the_great_leap/decisions/` |
| the_last_vote | decisions | `iram_work/the_last_vote/decisions/` |

---

## DECISIONES CONFIRMADAS POR EL OPERADOR — NO REDEBATIR

| ID | Decisión | Fuente |
|---|---|---|
| INC-13 | Mantener `iram_cleanup_exodos = yes` inline en on_action (cleanup síncrono garantizado). Remover del `immediate` de iram.2, iram.3, iram.4. iram.1 (error path, sin inline) conserva su `immediate`. | audit_3.md + operador 17:59 |
| INC-14 | Renombrar `iram_dist_country` → `iram_op_country` en DG y OG on_action. Misma sesión que BUG-4. | operador 17:59 |
| INC-15 | 5 variables dead weight → Opción A: documentar como hooks de trazabilidad en Sec 3.6. No tocar código. | ARCHIVE Sec 19b + operador |
| SUG-6 | Cancel All siempre visible → Opción A: mantener diseño de pánico. Documentar en Sec 3.7. | ARCHIVE Sec 19b + operador |
| GAP-7 | Variables legacy v4 (`exodos_*`) → Opción A: agregar pasada `remove_variable` con guards `has_variable` al final de `iram_cleanup_exodos`. | ARCHIVE Sec 8-C.4 + Sec 11 + operador |
| BUG-4 tooltip | Reutilizar `iram_tt_exodos_transfer_ya_activa`. Texto correcto. No crear loc nueva. | audit_4.md + operador |

NOTA INC-13: la auditoría consolidada recomendaba el approach opuesto (remover inline).
El operador confirmó audit_3.md: `trigger_event` no garantiza ejecución sincrónica — si
el evento corre en el tick siguiente, las variables siguen activas y el pulso mensual
puede reintentarlo. El inline es el cleanup síncrono y garantizado. El redundante es
el `immediate` de los eventos de completión exitosa.

---

## AUDITORÍA COMPLETA — TABLA MAESTRA (35 hallazgos únicos)

**Deduplicaciones:** BUG-2 → INC-1. INC-8 → subsumed INC-15. SUG-1 → INC-9.
**Reclasificación:** BUG-6 → GAP-12 (diseño intencional per RE-table ACTIVE).
**Verificados en código:** BUG-1 ✅ BUG-3 ✅ BUG-4 ✅ INC-9 ✅ INC-11 ✅ INC-13 ✅ GAP-6 ✅ GAP-12 ✅

| ID | Prio | Tipo | Ver. | Hallazgo | Archivo(s) | Acción |
|---|---|---|---|---|---|---|
| BUG-1 | 🔴 | Código | ✅ | `remove_holding = prev` dentro de `random_holdings` en `iram_bom_seize_holdings` — nunca remueve nada, silencioso | `iram_bom_decisions.txt` | Fix: `random_holdings { save_scope_as = iha_holding }` → `remove_holding = scope:iha_holding` |
| BUG-3 | 🔴 | Código | ✅ | `iram_bom_menu_close` le faltan guards NOT ego/heir en `potential` — botón close BOM visible aunque haya submenú abierto | `iram_bom_menu.txt` | Agregar dos guards NOT al `potential` |
| BUG-4 | 🔴 | Código | ✅ | GG/DG/OG/Constructor `allow` solo chequea `iram_operation_active`. Durante `iram_transfer_pending` (activate→confirm), `iram_operation_active` NO está seteado → cuatro operaciones activables en esa ventana → corrupción de estado | 4 archivos de activación | Agregar `NOT = { has_variable = iram_transfer_pending }` en `allow` de los 4 |
| INC-1 | 🟡 | Wiki | ✅ | Sec 3.6: `tgl_purchased` — código usa `iram_tgl_purchased` | ACTIVE Sec 3.6 | Corregir fila |
| INC-2 | 🟡 | Wiki | ✅ | `iram_operation_active` no figura en Sec 3.6 — guard global de GG/DG/OG/Transfer/Constructor | ACTIVE Sec 3.6 | Agregar fila |
| INC-3 | 🟡 | Wiki | ✅ | Dashboard Sec 0.5 dice "IRAM v4.3.16", sesión 2026-06-03 — nunca actualizado desde v5 | ACTIVE Sec 0.5 | Actualizar a v5.6 |
| INC-4 | 🟡 | Wiki | ✅ | Sec 22: versión ACTIVE dice `v3.9` (debe ser `v3.10`); SESSION_LOG dice `_03-22.md` (debe ser `_03-47.md`) | ACTIVE Sec 22 | Corregir (subsumido en actualización a v3.11) |
| INC-5 | 🟡 | Wiki | ✅ | Sec 0.3: secciones 1,2,9,10,11,13,16 sin marca 📦 — pendiente del SESSION_LOG 03:47 | ACTIVE Sec 0.3 | Agregar `📦 → ARCHIVE` a las 7 filas |
| INC-6 | 🟡 | Wiki | ✅ | Sec 4.3 usa variables v4: `exodos_anchor_province` etc. — renombradas en v5 | ACTIVE Sec 4.3 | Ver INC-11 (reescritura completa) |
| INC-7 | 🟡 | Wiki | ✅ | ARCHIVE referenciado como `TECHNICAL_WIKI_ARCHIVE_v3_4` en header/Sec 0.1/Sec 0.3 — ARCHIVE real es v3.7 | ACTIVE header, 0.1, 0.3 | Reemplazar por `TECHNICAL_WIKI_ARCHIVE — ver Sección 22` |
| INC-9 | 🟡 | Loc | ✅ | Keys `iram_exodos_cancel_all` y `_desc` duplicadas en dos archivos. Copias con texto diferente entre sí. | `iram_exodos_l_*.yml` + `iram_menu_l_*.yml` (ES+EN) | Actualizar título en `iram_exodos_l_*`. Eliminar duplicado de `iram_menu_l_*`. |
| INC-10 | 🟡 | Wiki | — | Sec 3.2: comentario de `iram_exodos_cancel.txt` dice "(cancel_all + cancel_bom)" — cancel de BOM está en `iram_bom_menu.txt` | ACTIVE Sec 3.2 | Corregir a "(cancel_all EXODOS)" |
| INC-11 | 🟡 | Wiki | ✅ | Sec 4.3 describe flujo scripted_gui v3: "panel de tácticas", "Botón A/B". v5 usa decisions: `activate_transfer` spawna AMBAS unidades en capital; jugador las mueve; `confirm_transfer` lee `unit_location` | ACTIVE Sec 4.3 | Reescribir con flujo v5 real |
| INC-12 | 🟡 | Wiki | — | Sec 3.4: 4 filas de "desactivar demografía" que no existen en v5 — se desactivan en cancel_all | ACTIVE Sec 3.4 | Eliminar 4 filas fantasma |
| INC-13 | 🟡 | Código | ✅ | Doble llamada a `iram_cleanup_exodos` al completar GG/DG/OG: inline en on_action + `immediate` en eventos iram.1-4. Segundo pase es idempotente pero genera noise en error.log por `remove_variable` sobre variables ya inexistentes | on_action GG/DG/OG + `iram_events.txt` | DECISIÓN OPERADOR: mantener inline en on_action. Remover de `immediate` de iram.2/3/4. iram.1 conserva. |
| INC-14 | 🟡 | Código | — | Scope `iram_dist_country` en DG y OG on_action — "dist" en OG es confuso para mantenibilidad | on_action DG + OG | DECISIÓN OPERADOR: renombrar a `iram_op_country` en ambos archivos |
| INC-15 | 🟡 | Código | — | 5 variables seteadas/limpiadas pero nunca evaluadas en potential/allow: `iram_bom_active`, `iram_divine_relic_active`, `iram_migracion_forzada_active`, `iram_ascenso_forzado_active`, `iram_descenso_forzado_active` | `iram_bom_scripted_effects.txt` + demografia | DECISIÓN OPERADOR Opción A: documentar como hooks de trazabilidad. No tocar código. |
| GAP-1 | 🟢 | Doc | — | `random_owned_province` con limit no-match: no-op silencioso (💀) — no está en Sec 6 | ACTIVE Sec 6 | Agregar a Sec 6 |
| GAP-2 | 🟢 | Doc | — | TGL sin recordatorio "restaurar costos" en el archivo | `iram_tgl_decisions.txt` | Agregar comentario TESTMODE |
| GAP-3 | 🟢 | Doc | — | Throughput no documentado: GG=10 áreas/mes, DG=5, OG=5 | ACTIVE Sec 3.3 | Agregar columna throughput |
| GAP-4 | 🟢 | Doc | — | `iram_optimize_threshold` no ajusta por city rank — ¿intencional? | `iram_script_values.txt` | Documentar decisión en Sec 19 |
| GAP-5 | 🟢 | Doc | — | `iram_compat_legacy.txt` no aclara que v5.0→v5.5 no requiere stubs adicionales | `iram_compat_legacy.txt` | Agregar nota |
| GAP-6 | 🟢 | Doc | ✅ | Transfer no tiene evento de completión exitosa — completión es silenciosa para el jugador | `iram_on_action_transfer.txt` + events | Crear `iram.5` (Transfer completado) + loc. Baja prioridad. |
| GAP-7 | 🟢 | Doc | — | `iram_cleanup_exodos` no limpia variables legacy v4 (`exodos_*`) — jugadores que actualizan sin cancel_all previo quedan con variables v4 colgando | `iram_scripted_effects.txt` | DECISIÓN OPERADOR Opción A: agregar pasada con guards `has_variable` al final del scripted_effect |
| GAP-8 | 🟢 | Doc | — | Convención no documentada: `.mod` dice `version = "5.4"` (último cambio de código), zip es v5.5 (cambio wiki+rutas). Una IA nueva reporta "discrepancia de versión" | ACTIVE Sec 20 | Documentar convención en Sec 20 o Sec 22 |
| GAP-9 | 🟢 | Doc | — | TGL: costo dinámico removido para testing — sin recordatorio en el archivo | `iram_tgl_decisions.txt` | Agregar `# TESTMODE — restaurar costo dinámico` |
| GAP-10 | 🟢 | Doc | — | TLV: stability ≥ 50 y popularity ≥ 50 removidos para testing — sin recordatorio | `iram_tlv_decisions.txt` | Agregar `# TESTMODE — restaurar stability ≥ 50 y popularity ≥ 50` |
| GAP-11 | 🟢 | Doc | — | Ego Sum Sec 5.6 dice "+10 stat" pero código agrega traits con efectos secundarios (Filius Iovis: lunatic+epileptic; Filius Martis: reckless) — no documentados | ACTIVE Sec 5.6 | Actualizar tabla con traits reales |
| GAP-12 | 🟢 | Doc | ✅ | Constructor destruye barracks/hill_fort/port sin reconstruir. **Diseño intencional** per RE-table ACTIVE. El jugador puede sorprenderse sin aviso. | `iram_exodos_constructor.txt` | Agregar comentario en código y nota en Sec 19 |
| SUG-2 | 🔵 | Test | — | Verificar que `family_property_seized_l` existe como modifier en IR 2.0.5 | `iram_bom_decisions.txt` | Checklist de testeo |
| SUG-3 | 🔵 | UX | — | Transfer dispara siempre iram.1 para tres causas — jugador no puede distinguir la causa | `iram_on_action_transfer.txt` | Crear iram.5 e iram.6. Baja prioridad. |
| SUG-4 | 🔵 | Loc | — | GG loc no menciona exclusión de capital | `iram_exodos_l_*.yml` | Agregar "La capital del país no es afectada." |
| SUG-5 | 🔵 | Doc | — | Destruir UNA sola unidad de Transfer post-confirm no cancela la operación — comportamiento no documentado | ACTIVE (ninguna sección) | Documentar en Sec 4.3 reescrita |
| SUG-6 | 🔵 | UX | — | Cancel All `potential = { is_ai = no }` puro — siempre visible aunque no haya nada activo | — | DECISIÓN OPERADOR Opción A: documentar en Sec 3.7. No tocar código. |

---

## PROTOCOLO DE LA IA EJECUTORA

1. Ejecutar `unzip -l` sobre el zip para confirmar rutas (tabla de Rutas Reales arriba).
2. Leer cada archivo completo antes de modificarlo.
3. Describir el cambio en una oración. Esperar confirmación del operador. (R19)
4. Verificar BOM después de cada archivo editado: `xxd archivo | head -1` → debe mostrar `efbb bf`.
5. Preguntar la hora al operador antes de generar el zip final. (R15)
6. No redebatir ningún ítem de la tabla "Decisiones confirmadas".
7. Ejecutar las tareas en el orden indicado. No saltar tareas.

---

## FASE 1 — CÓDIGO (7 tareas, ejecutar en orden)

### TAREA 1 — BUG-1: `remove_holding` en scope incorrecto

**Archivo:** `iram_work/by_other_means/decisions/iram_bom_decisions.txt`
**Decisión:** `iram_bom_seize_holdings`

Bug: `remove_holding = prev` dentro de `random_holdings` — `prev` no es el holding
en ese contexto → nunca remueve nada. Silencioso.

```pdxscript
# ANTES (bug):
while = {
    limit = { num_holdings_owned > 0 }
    random_holdings = {
        remove_holding = prev
    }
}

# DESPUÉS (fix):
while = {
    limit = { num_holdings_owned > 0 }
    random_holdings = {
        save_scope_as = iha_holding
    }
    remove_holding = scope:iha_holding
}
```

`remove_holding = scope:iha_holding` va DENTRO del `while` pero FUERA de `random_holdings`.
**Verificación:** `grep "remove_holding = prev" archivo` → debe devolver 0 resultados.

---

### TAREA 2 — BUG-3: guards faltantes en `iram_bom_menu_close`

**Archivo:** `iram_work/by_other_means/decisions/iram_bom_menu.txt`
**Decisión:** `iram_bom_menu_close`

Agregar DOS líneas NOT al `potential` existente. No crear bloque OR.

```pdxscript
# DESPUÉS (leer el archivo primero para ver el potential actual, luego agregar las dos NOT):
potential = {
    is_ai = no
    has_variable = iram_bom_menu
    NOT = { has_variable = iram_bom_menu_ego }
    NOT = { has_variable = iram_bom_menu_heir }
}
```

Confirmar que `has_variable = iram_bom_menu` sigue presente.

---

### TAREA 3 — BUG-4 + INC-14: Transfer pending guard + rename scope

#### 3A — BUG-4 en GG: `iram_work/exodos/decisions/iram_exodos_gather_global.txt`

En el bloque `allow` de la decisión de activación, agregar ANTES del primer `custom_tooltip`:

```pdxscript
custom_tooltip = iram_tt_exodos_transfer_ya_activa
NOT = { has_variable = iram_transfer_pending }
```

El tooltip ya existe en loc. No crear loc nueva.

#### 3B — BUG-4 en DG: `iram_work/exodos/decisions/iram_exodos_distribute_global.txt`
Mismo fix que 3A.

#### 3C — BUG-4 en OG: `iram_work/exodos/decisions/iram_exodos_optimize_global.txt`
Mismo fix que 3A.

#### 3D — BUG-4 en Constructor: `iram_work/exodos/decisions/iram_exodos_constructor.txt`
Mismo fix que 3A.

#### 3E — INC-14 en DG: `iram_work/exodos/common/on_action/iram_on_action_distribute_global.txt`

Reemplazar TODAS las ocurrencias de `iram_dist_country` por `iram_op_country`.
**Verificación:** `grep -c "iram_dist_country" archivo` → debe devolver `0`.

#### 3F — INC-14 en OG: `iram_work/exodos/common/on_action/iram_on_action_optimize_global.txt`
Mismo rename que 3E. Misma verificación → `0`.

---

### TAREA 4 — INC-9: keys de loc duplicadas en cancel_all

**4A** — `iram_work/exodos/localization/spanish/iram_exodos_l_spanish.yml`:
Actualizar título a `"Cancelar todo — Exodos"`. Mantener desc como está.

**4B** — `iram_work/exodos/localization/spanish/iram_menu_l_spanish.yml`:
Eliminar las dos líneas `iram_exodos_cancel_all:0` y `iram_exodos_cancel_all_desc:0`.

**4C** — `iram_work/exodos/localization/english/iram_exodos_l_english.yml`:
Actualizar título a `"Cancel All — Exodos"`.

**4D** — `iram_work/exodos/localization/english/iram_menu_l_english.yml`:
Eliminar las dos líneas `iram_exodos_cancel_all:0` y `iram_exodos_cancel_all_desc:0`.

---

### TAREA 5 — INC-13: remover doble cleanup de eventos

**Archivo:** `iram_work/exodos/events/iram_events.txt`

En los eventos `iram.2`, `iram.3` e `iram.4`: eliminar `iram_cleanup_exodos = yes` del
bloque `immediate`.

`iram.1` (error path, sin inline en on_action) CONSERVA su `iram_cleanup_exodos = yes`.

Rationale: inline en on_action = cleanup síncrono garantizado. Si se remueve el inline,
`trigger_event` puede disparar en el tick siguiente → ventana donde variables siguen activas.
El redundante es el `immediate` de los eventos de completión exitosa, no el inline.

**Verificación:** después del fix, solo `iram.1` contiene `iram_cleanup_exodos = yes`.

---

### TAREA 6 — GAP-7: cleanup de variables legacy v4

**Archivo:** `iram_work/exodos/common/scripted_effects/iram_scripted_effects.txt`
**Scripted effect:** `iram_cleanup_exodos`

Agregar al FINAL del scripted effect, después de todos los `remove_variable` existentes.
Guard `limit = { has_variable = X }` obligatorio — evita noise en error.log en saves sin v4.

```pdxscript
    # ── LEGACY v4 — variables pre-iram_* prefix (cleanup para saves de v4.x)
    if = { limit = { has_variable = exodos_operation_active }
        remove_variable = exodos_operation_active }
    if = { limit = { has_variable = exodos_gather_active }
        remove_variable = exodos_gather_active }
    if = { limit = { has_variable = exodos_distribute_active }
        remove_variable = exodos_distribute_active }
    if = { limit = { has_variable = exodos_transfer_active }
        remove_variable = exodos_transfer_active }
    if = { limit = { has_variable = exodos_optimize_active }
        remove_variable = exodos_optimize_active }
    if = { limit = { has_variable = exodos_optimize_gather_done }
        remove_variable = exodos_optimize_gather_done }
    if = { limit = { has_variable = exodos_optimize_count }
        remove_variable = exodos_optimize_count }
    if = { limit = { has_variable = exodos_anchor_province }
        remove_variable = exodos_anchor_province }
    if = { limit = { has_variable = exodos_destination_province }
        remove_variable = exodos_destination_province }
    if = { limit = { has_variable = exodos_pulse_counter }
        remove_variable = exodos_pulse_counter }
```

---

### TAREA 7 — GAP-9 + GAP-10: comentarios TESTMODE

**7A** — `iram_work/the_great_leap/decisions/iram_tgl_decisions.txt`:
Agregar al inicio del archivo o en el header de la decisión:
```pdxscript
# TESTMODE — restaurar costo dinámico antes de release
# Fórmula: 516 oro/metrópolis + 258 oro/ciudad — ver ARCHIVE Sec 8 para código v3
```

**7B** — `iram_work/the_last_vote/decisions/iram_tlv_decisions.txt`:
Agregar como comentario en el `allow` de `iram_tlv_confirm`:
```pdxscript
# TESTMODE — restaurar: stability >= 50 y popularity >= 50
```

---

## FASE 2 — WIKI ACTIVE (10 tareas, editar v3.10 → producir v3.11)

Copiar el ACTIVE de uploads a `/home/claude/`, editar ahí.
Nombre de salida: `IRAM_TECHNICAL_WIKI_ACTIVE_v3_11_2026-06-09.md`
Actualizar el footer a `IRAM TECHNICAL WIKI ACTIVE v3.11 — 2026-06-09`.

### TAREA 8 — INC-3: Actualizar dashboard (Sec 0.5)

```
ANTES:
| Versión | IRAM v4.3.16 |
| Última sesión | 2026-06-03 01:09 |
| Bugs conocidos en zip activo | Ninguno — 3 bugs corregidos en v4.3.16 |

DESPUÉS:
| Versión | IRAM v5.6 |
| Última sesión | 2026-06-09 17:59 |
| Bugs conocidos en zip activo | BUG-1, BUG-3, BUG-4 corregidos en v5.6 — ver Sección 19 |
```

En el semáforo rápido, agregar al inicio:
```
- ✅ Auditoría v5.5 completada — BUG-1/BUG-3/BUG-4 corregidos en v5.6. Ver Sección 19.
```

---

### TAREA 9 — INC-7 + header: referencias hardcodeadas al ARCHIVE

Buscar: `grep -n "TECHNICAL_WIKI_ARCHIVE_v3_4" archivo.md`
Reemplazar cada ocurrencia por: `TECHNICAL_WIKI_ARCHIVE — ver Sección 22`
Actualizar header: `## TECHNICAL WIKI ACTIVE — v3.10` → `## TECHNICAL WIKI ACTIVE — v3.11`

---

### TAREA 10 — INC-4 + Sec 22: tabla de archivos activos

Reemplazar tabla completa de Sec 22 con:

| Archivo | Nombre actual | Versión |
|---------|--------------|---------|
| TECHNICAL_WIKI (ACTIVE) | `IRAM_TECHNICAL_WIKI_ACTIVE_v3_11_2026-06-09.md` | v3.11 |
| TECHNICAL_WIKI (ARCHIVE) | `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09.md` | v3.7 |
| PROMPT_MAESTRO | `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` | v5.2 |
| SESSION_LOG (último) | `IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md` | v5.6 |
| Zip canónico | `mod_pack_IRAM_v5_6_2026-06-09_HH-MM.zip` | v5.6 |

(HH-MM se reemplaza con la hora real al generar — preguntar al operador.)

---

### TAREA 11 — INC-5 + INC-10 + corrección árbol (Sec 3.2 y Sec 0.3)

**11A — INC-5: marcas 📦 en Sec 0.3**
Agregar `📦 → ARCHIVE` en las filas de secciones 1, 2, 9, 10, 11, 13, 16.
Ejemplo: `| Historia del proyecto, evolución v1→v4 | 1 |` → `| Historia del proyecto, evolución v1→v4 | 1 📦 → ARCHIVE |`

**11B — INC-10: comentario cancel.txt**
`← BOM UTF-8 (cancel_all + cancel_bom)` → `← BOM UTF-8 (cancel_all EXODOS)`

**11C — Corrección árbol: rutas decisions/**
Para `exodos/` y `by_other_means/`: cambiar `common/decisions/` → `decisions/` directo.
Preservar `common/on_action/` y `common/scripted_effects/` — esos sí tienen `common/`.

---

### TAREA 12 — INC-11 + INC-6: Reescribir Sec 4.3 (Transfer)

Reemplazar el contenido actual de Sec 4.3 con:

```
## 4.3 Transfer

**Flujo v5 (decisions + on_action, sin scripted_gui):**

1. Jugador ejecuta `iram_exodos_activate_transfer`.
   Effect: spawna DOS unidades marcadoras en la capital del país.
   Setea `iram_transfer_pending = yes`.
   NOTA: `iram_operation_active` NO se setea aquí — se setea al confirmar.

2. Jugador mueve las unidades al origen y al destino (movement_speed = 5).

3. Jugador ejecuta `iram_exodos_confirm_transfer`.
   Allow: ambas unidades existen, en territorio propio, ninguna en movimiento
   (NOT any_unit is_moving = yes — excepción documentada a R5).
   Lee `unit_location` de cada marcador para determinar origen y destino.
   Effect: mueve pops, destruye marcadores, limpia `iram_transfer_pending`,
   setea `iram_operation_active`, dispara evento de completión, llama cleanup.

**Variables de estado (v5):**
- `iram_transfer_pending` (country): activo entre activate y confirm — bloquea GG/DG/OG/Constructor.
- `iram_transfer_active` (country): activo durante ejecución del on_action.

**Variables de unidad:** `exodos_unit_transfer_origin` / `exodos_unit_transfer_dest`.

**Excepciones de diseño activas:**
- R5: `confirm_transfer` SÍ verifica NOT any_unit is_moving — intencional.
- R3: Transfer SÍ usa `iram_transfer_pending` como estado intermedio — excepción documentada.
- RD1: `confirm_transfer` usa `iram_transfer_pending` en `potential` — excepción documentada.

**SUG-5:** Destruir UNA sola unidad post-confirm no cancela la operación. Las provincias
ya están guardadas en variables — las unidades son marcadores visuales post-confirm.
La operación cancela solo si AMBAS están destruidas.

**Variables legacy v4** (no existen en v5, limpiadas por `iram_cleanup_exodos`):
`exodos_anchor_province`, `exodos_destination_province`, `exodos_pulse_counter`, `exodos_transfer_active`.
```

---

### TAREA 13 — INC-12: Eliminar filas fantasma en Sec 3.4

Eliminar las filas de "Desactivar" demografía que no existen en v5:
- `Demografía: Desactivar Migración Forzada`
- `Demografía: Desactivar Ascenso Forzado`
- `Demografía: Desactivar Descenso Forzado`
- Verificar si hay una cuarta (buscar "Desactivar" o "Disolver" en la tabla).

---

### TAREA 14 — INC-1 + INC-2 + INC-15: Actualizaciones en Sec 3.6

**14A — INC-1:** Fila `tgl_purchased` → `iram_tgl_purchased`.

**14B — INC-2:** Agregar fila después de `iram_optimize_global_active`:
`| \`iram_operation_active\` | ✗ | ✓ | Guard global — solo una operación activa a la vez (GG, DG, OG, Transfer, Constructor) |`

**14C — INC-15:** Encontrar la fila `iram_bom_active` y agregar en su descripción:
"Hook de trazabilidad. Seteada y limpiada, nunca evaluada en potential/allow.
Diseño intencional — ver ARCHIVE Sec 19b 2026-06-04."
Aplicar la misma nota a las 4 variables demográficas (`iram_divine_relic_active` etc.).
Si no están en la tabla, agregarlas.

---

### TAREA 15 — SUG-6: Documentar Cancel All en Sec 3.7

Bajo "MOD: exodos" → "Siempre visible", después de `iram_exodos_cancel_all`:
"Cancel All: siempre visible por diseño — potential sin guard de variable.
Rol: botón de pánico. Cubre estados corruptos donde ninguna variable reflejaría el
problema. Decisión de diseño cerrada — ARCHIVE Sec 19b 2026-06-05."
Repetir para `iram_bom_cancel_all` en "MOD: by_other_means".

---

### TAREA 16 — GAP-8: convención versión .mod vs zip en Sec 20

Agregar en Sec 20 (o al final de Sec 22):
"Convención de versión: la versión en los archivos .mod refleja el último cambio de
código. La versión del zip refleja cualquier cambio (incluyendo solo wiki o rutas).
Ejemplo: .mod = '5.4', zip = v5.5 (cambio de wiki) — no es una discrepancia."

---

### TAREA 17 — Sec 19: entrada de esta sesión

Agregar al final de Sec 19:

```
### Sesión 2026-06-09 17:59 — Correcciones v5.6 + wiki v3.11

Correcciones de código (v5.6):
BUG-1: remove_holding en scope incorrecto (seize_holdings) — fix aplicado.
BUG-3: guards NOT ego/heir faltantes en iram_bom_menu_close — agregados.
BUG-4: GG/DG/OG/Constructor allow sin guard iram_transfer_pending — guard agregado en los 4.
INC-9: keys cancel_all duplicadas en loc — unificadas en iram_exodos_l_*.
INC-13: doble cleanup GG/DG/OG — removido de immediate de iram.2/3/4. Inline conservado.
INC-14: scope iram_dist_country → iram_op_country en DG y OG on_action.
GAP-7: 10 variables legacy v4 agregadas a iram_cleanup_exodos con guards.
GAP-9/10: comentarios TESTMODE en TGL y TLV.

Wiki (v3.11): dashboard v5.6, Sec 22, 📦 en Sec 0.3, referencias ARCHIVE genéricas,
árbol Sec 3.2 corregido (decisions/ sin common/), 4 filas fantasma Sec 3.4 eliminadas,
Sec 3.6 variables actualizadas, Sec 4.3 reescrita con flujo v5, SUG-5 documentado,
Sec 3.7 Cancel All documentado, convención versión .mod vs zip en Sec 20.

Decisiones cerradas: INC-15→A, SUG-6→A, INC-13→inline, INC-14→rename, GAP-7→A.
```

---

## FASE 3 — Gaps de documentación (si hay tiempo)

| ID | Acción | Archivo |
|---|---|---|
| GAP-1 | Agregar patrón `random_owned_province` con limit no-match a Sec 6 (💀 silencioso) | ACTIVE Sec 6 |
| GAP-3 | Agregar columna throughput en Sec 3.3: GG=10 áreas/mes, DG=5, OG=5 | ACTIVE Sec 3.3 |
| GAP-4 | Documentar en Sec 19 por qué `iram_optimize_threshold` no ajusta por city rank | ACTIVE Sec 19 |
| GAP-5 | Nota en `iram_compat_legacy.txt` sobre que 5.x no requiere stubs adicionales | compat file |
| GAP-6 | Crear `iram.5` (Transfer completado) + loc. Baja prioridad. | events + loc |
| GAP-11 | Actualizar Sec 5.6 con traits reales de Ego Sum (verificar en zip) | ACTIVE Sec 5.6 |
| GAP-12 | Comentario en `iram_exodos_constructor.txt` sobre demolición intencional de barracks/hill_fort/port | constructor file |
| SUG-2 | Verificar `family_property_seized_l` en IR 2.0.5 | checklist testeo |
| SUG-3 | Crear iram.5 e iram.6 con causas distintas de fallo Transfer. Baja prioridad. | events + loc |
| SUG-4 | Loc GG: agregar "La capital del país no es afectada." | `iram_exodos_l_*.yml` |

---

## ESTADO DE PENDIENTES ANTERIORES (SESSION_LOG 03:47)

| Pendiente | Estado |
|---|---|
| Sec 0.3: 📦 en secciones 1,2,9,10,11,13,16 | ✅ Cubierto — TAREA 11A |
| Sec 22: ACTIVE v3.9 → v3.10 | ✅ Subsumido — TAREA 10 actualiza a v3.11 |
| Sec 22: SESSION_LOG `_03-22` → `_03-47` | ✅ Subsumido — TAREA 10 actualiza a v5.6 |

---

## ENTREGABLES ESPERADOS

1. **Zip** `mod_pack_IRAM_v5_6_2026-06-09_HH-MM.zip` — Fase 1 aplicada (7 tareas de código).
2. **Wiki** `IRAM_TECHNICAL_WIKI_ACTIVE_v3_11_2026-06-09.md` — Fase 2 aplicada (10 tareas wiki).
3. **SESSION_LOG** `IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md` (este documento).

---

## SECCIÓN 19 — bloque para pegar en TECHNICAL_WIKI ACTIVE

```
### Sesión 2026-06-09 17:59 — Auditoría consolidada + correcciones v5.6

**Auditoría consolidada — CERRADO**
3 rondas unificadas. 35 hallazgos únicos tras deduplicación y reclasificación.
Confirmados en código: BUG-1 (seize_holdings), BUG-3 (menu_close guards),
BUG-4 (Transfer pending no bloqueado), INC-9 (loc duplicadas), INC-11 (Sec 4.3 obsoleta),
INC-13 (doble cleanup, benigno pero noise en error.log).

Decisiones cerradas: INC-15→A (trazabilidad), SUG-6→A (pánico), GAP-7→A (cleanup legacy),
INC-14→rename (iram_op_country), INC-13→inline en on_action.

Ver IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md para tabla completa y patrones de código.
```

---

## SECCIÓN 22 — tabla actualizada

| Archivo | Nombre actual | Versión |
|---------|--------------|---------|
| TECHNICAL_WIKI (ACTIVE) | `IRAM_TECHNICAL_WIKI_ACTIVE_v3_11_2026-06-09.md` | v3.11 |
| TECHNICAL_WIKI (ARCHIVE) | `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09.md` | v3.7 |
| PROMPT_MAESTRO | `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` | v5.2 |
| SESSION_LOG (último) | `IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md` | v5.6 |
| Zip canónico | `mod_pack_IRAM_v5_6_2026-06-09_HH-MM.zip` | v5.6 |

---

*IRAM SESSION LOG v5.6 — 2026-06-09 17:59*
*35 hallazgos auditados | 7 tareas código | 10 tareas wiki | 10 gaps Fase 3*
*Próxima sesión: ejecutar Fase 1 en orden → Fase 2 → Fase 3 si hay tiempo*
