# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK (IRAM)
## Backup Técnico Unificado
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | mod_pack_IRAM.zip | v1.11

---

## INSTRUCCIONES PARA LA IA QUE LEA ESTE DOCUMENTO

Este documento es el backup técnico completo del proyecto **Imperator: Rome — Alternative Mechanics MOD PACK (IRAM)**.
Es **completamente autónomo** — contiene todo lo necesario para continuar el desarrollo sin ningún otro archivo de contexto.
Si no tenés acceso a ningún archivo previo, este documento es suficiente para arrancar.

### Contexto del proyecto

IRAM es una **reorganización y ampliación** del ecosistema de mods previo (Drago Mod Pack Alt v1.3).
El cambio fundamental es estructural: todos los mods se unifican dentro de un único mod `exodos`,
eliminando la necesidad de múltiples entradas en `dlc_load.json`. Los mods anteriores
(`by_other_means`, `the_last_vote`, `the_great_leap`) se mantienen como carpetas vacías "TEST SHELL"
para compatibilidad con partidas existentes.

La nueva función principal es **Exodos: Optimizar** — una operación que reemplaza y unifica
Gather y Distribute en un solo flujo de dos fases guiado por los resultados del optimizador provincial.
Las funciones Concentrate (Gather) y Distribute se mantienen en el mod como legacy.

### Archivos necesarios para continuar el desarrollo

La IA debe pedir al usuario que suba estos archivos al inicio de cada sesión:

| Archivo | Por qué es necesario |
|---|---|
| `backup_mod_pack_IRAM_1_.md` | **Este documento** — fuente de verdad del proyecto |
| `mod_alt.zip` | Código fuente legacy — base de todos los archivos a modificar |
| `mod.zip` | Código fuente estable — referencia para verificar variables y convenciones |
| `drago_mod_pack_alt_1_3_.md` | Backup técnico del ecosistema ALT v1.3 — referencia de convenciones legacy |
| `imperator_optimizer_v4.html` | Optimizador provincial — herramienta de cálculo (no modificar) |
| `optimizador_provincial_backup_v4.md` | Documentación del optimizador — referencia de parámetros |

**El usuario tiene una partida de pruebas activa.** El `dlc_load.json` lista los cuatro mods originales.
No modificar ese archivo — las carpetas vacías TEST SHELL mantienen la compatibilidad.

**Nota:** `game.zip` (scripts vanilla de Imperator 2.0.4) puede ser necesario para verificar sintaxis
del engine. Pedirlo al usuario solo si surge una duda específica de sintaxis no cubierta en la
sección 4 de este documento.

### Reglas de trabajo

1. Leer este documento completo antes de escribir cualquier línea de código.
2. Leer también `mod_alt.zip` para verificar el estado real de los archivos fuente.
3. No asumir valores del engine de memoria — verificar contra archivos fuente o las secciones de código de este documento.
4. Las decisiones marcadas como **CERRADO** no se reabren salvo pedido explícito del usuario.
5. El modelo económico del optimizador está **CERRADO** en su totalidad. No recalcular salvo pedido explícito.
6. El ecosistema no castiga al jugador — habilita lo que el juego no permite. No agregar restricciones artificiales.
7. Las descripciones de las decisiones son la segunda línea de defensa — usar MAYÚSCULAS para advertencias críticas.
8. `is_ai = no` va siempre en `potential` Y en `allow`. Sin excepción.
9. El cancel particular (`exodos_cancel`) **no existe en IRAM**. Solo existe `exodos_cancel_all`. No agregar cancels particulares por función bajo ninguna circunstancia.
10. El costo de las operaciones **no se escribe en los textos de localización** — el engine lo muestra automáticamente desde el `effect` en el tooltip de la decisión.

### Flujo de trabajo con la IA

1. El usuario sube todos los archivos listados en la tabla de material de referencia al inicio de la sesión.
2. La IA lee todo, se pone al día.
3. La IA trabaja sobre los archivos fuente y entrega el zip final listo para instalar.

### build_mods.py — herramienta accesoria

`build_mods.py` es un script Python que genera `mod.zip` desde los archivos fuente del mod.
**Es una herramienta de desarrollo — el usuario instala el zip directamente, no necesita ejecutar este script.**
La IA lo usa internamente durante el proceso de codeo para generar el zip entregable.

**Qué hace:**
- Recorre las carpetas `exodos/`, `by_other_means/`, `the_last_vote/`, `the_great_leap/` y los `.mod` raíz
- Valida BOM antes de empaquetar: `.txt` y `.yml` deben tener BOM `EF BB BF`; `.mod` no deben tenerlo
- Si hay errores de BOM, aborta sin generar el zip y lista los archivos con problema
- Si todo está OK, genera `mod.zip` en el mismo directorio que el script

**Uso:**
```bash
python build_mods.py
# Salida: mod.zip en el directorio actual
# Renombrar manualmente a mod_pack_IRAM.zip antes de entregar al usuario
```

**Nota:** el script genera `mod.zip` con ese nombre fijo. Renombrarlo a `mod_pack_IRAM.zip` es el último paso antes de entregar.

---

## ESTADO ACTUAL

| Item | Valor |
|---|---|
| Versión IRAM | v1.11 |
| Fecha | 2026-05 |
| Estado | EN DESARROLLO — Optimizar implementado, rangos corregidos v1.11, Distribute corregido, Rival Heir v1.4 implementado |
| Exodus ALT | 1.21 ALT (base) |
| By Other Means | 3.0 |
| The Last Vote | 1.7 |
| The Great Leap | 1.5 |
| Exodos: Optimizar | DISEÑO CERRADO — localización CERRADA — código pendiente |
| Exodos: Heredero del Rival | v1.6 IMPLEMENTADO — entregado en mod_pack_IRAM_12.zip |
| Cancel particular (`exodos_cancel`) | ELIMINADO — reemplazado íntegramente por `exodos_cancel_all` |
| Localización ES | CERRADA — ver sección 2.11 |
| Localización EN | CERRADA — ver sección 2.11 |

---

## 1. ECOSISTEMA

### 1.1 Estructura de mods

**Cambio fundamental respecto al ecosistema anterior:**
Todo el ecosistema se unifica dentro del mod `exodos/`. Los otros tres mods pasan a ser
carpetas vacías con descriptor TEST SHELL — el engine los carga vacíos sin error.

```
dlc_load.json (NO MODIFICAR):
{
    "enabled_mods": [
        "mod/exodos.mod",
        "mod/by_other_means.mod",
        "mod/the_last_vote.mod",
        "mod/the_great_leap.mod"
    ]
}
```

Los mods `by_other_means`, `the_last_vote` y `the_great_leap` contienen solo su `descriptor.mod`
con texto `"TEST SHELL — funcionalidad migrada a exodos"`. Sus carpetas de decisiones,
eventos y localización son vacías o no existen.

### 1.2 Estructura de archivos IRAM

```
mod/
├── exodos.mod                                               ← sin BOM
├── by_other_means.mod                                       ← sin BOM (TEST SHELL)
├── the_last_vote.mod                                        ← sin BOM (TEST SHELL)
├── the_great_leap.mod                                       ← sin BOM (TEST SHELL)
│
├── exodos/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/
│   │   ├── exodos_decisions_transfer.txt                    ← BOM UTF-8
│   │   ├── exodos_decisions_optimize.txt                    ← BOM UTF-8 (NUEVO)
│   │   ├── exodos_decisions_gather_distribute.txt           ← BOM UTF-8 (Concentrate + Distribute legacy)
│   │   ├── exodos_decisions_rival_heir.txt                  ← BOM UTF-8 (NUEVO)
│   │   ├── exodos_decisions_bom.txt                         ← BOM UTF-8
│   │   ├── exodos_decisions_tgl.txt                         ← BOM UTF-8
│   │   └── exodos_decisions_tlv.txt                         ← BOM UTF-8
│   ├── events/
│   │   ├── exodos_events.txt                                ← BOM UTF-8
│   │   └── tlv_events.txt                                   ← BOM UTF-8
│   ├── common/
│   │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8
│   │   ├── units/exodos_units.txt                           ← BOM UTF-8
│   │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8
│   └── localization/
│       ├── english/
│       │   ├── exodos_l_english.yml                         ← BOM UTF-8
│       │   ├── bom_l_english.yml                            ← BOM UTF-8
│       │   ├── bom_l_english_ego_sum.yml                    ← BOM UTF-8
│       │   ├── tlv_l_english.yml                            ← BOM UTF-8
│       │   └── tgl_l_english.yml                            ← BOM UTF-8
│       └── spanish/
│           ├── exodos_l_spanish.yml                         ← BOM UTF-8
│           ├── bom_l_spanish.yml                            ← BOM UTF-8
│           ├── bom_l_spanish_ego_sum.yml                    ← BOM UTF-8
│           ├── tlv_l_spanish.yml                            ← BOM UTF-8
│           └── tgl_l_spanish.yml                            ← BOM UTF-8
│
├── by_other_means/
│   └── descriptor.mod                                       ← sin BOM (TEST SHELL)
├── the_last_vote/
│   └── descriptor.mod                                       ← sin BOM (TEST SHELL)
└── the_great_leap/
    └── descriptor.mod                                       ← sin BOM (TEST SHELL)
```

### 1.3 Tabla de funciones

| Función | Prefijo | Archivo decisiones | Estado |
|---|---|---|---|
| Exodos: Transfer | `exodos_` | exodos_decisions_transfer.txt | ✓ implementado (sin cambios) |
| Exodos: Concentrate (Gather legacy) | `exodos_` | exodos_decisions_gather_distribute.txt | ✓ implementado (sin cambios) |
| Exodos: Distribute (legacy) | `exodos_` | exodos_decisions_gather_distribute.txt | ✓ implementado (sin cambios) |
| Exodos: Optimizar | `exodos_` | exodos_decisions_optimize.txt | ⚠ PENDIENTE |
| Exodos: Heredero del Rival | `exodos_` | exodos_decisions_rival_heir.txt | ✓ implementado — mod_pack_IRAM_6.zip |
| By Other Means | `bom_` / `iha_` | exodos_decisions_bom.txt | ✓ migrado sin cambios |
| The Great Leap | `tgl_` | exodos_decisions_tgl.txt | ✓ migrado sin cambios |
| The Last Vote | `tlv_` | exodos_decisions_tlv.txt | ✓ migrado sin cambios |
| Cancel general | `exodos_` | exodos_decisions_optimize.txt | ⚠ PENDIENTE |

### 1.4 Tabla de unidades Exodus

| Código (`decisions.txt`) | Interfaz EN | Interfaz ES |
|---|---|---|
| `"Exodos - Origin"` | Exodos - Origin | Exodos - Origen |
| `"Exodos - Destination"` | Exodos - Destination | Exodos - Destino |
| `"Exodos - Concentrate"` | Exodos - Concentrate | Exodos - Concentrar |
| `"Exodos - Distribute"` | Exodos - Distribute | Exodos - Distribuir |
| `"Exodos - Optimize"` | Exodos - Optimize | Exodos - Optimizar |

### 1.5 Panel de decisiones en juego

Orden de aparición en la UI según condiciones activas:

**Siempre visible (is_ai = no):**
- Cancelar todo — `exodos_cancel_all`

**Con rivals ≥ 2:**
- By Other Means: Eliminar Rivales

**Con rivals = 1:**
- By Other Means: Bacanal
- By Other Means: Et tu, Brute?
- Iron Hand: Confiscar Propiedades
- Iron Hand: Llenar el Vacío
- Exodos: Transfer (activate)
- Exodos: Concentrar (activate)
- Exodos: Distribuir (activate)
- Exodos: Optimizar (activate)
- Exodos: Hijo del Rival (`exodos_spawn_rival_son`) — rival ≥ 16 años, al servicio del jugador
- Exodos: Hija del Rival (`exodos_spawn_rival_daughter`) — rival ≥ 16 años, al servicio del jugador

**Con exodos_optimize_pending (después de activar Optimizar):**
- Las 17 decisiones de rango (exodos_opt_range_3 … exodos_opt_range_19)

**Con tyranny = 0:**
- The Great Leap

**Con is_republic + condiciones TLV:**
- The Last Vote

**Con bom_ego_sum_X_used ausente:**
- Filius Martis, Filius Iovis, Filius Mercurii, Filius Minervae

### 1.6 Tabla de costos y condiciones — ecosistema completo

| Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | Condiciones extra |
|---|---|---|---|---|---|---|
| Exodos: Optimize activate | — | — | — | — | — | 1 rival exacto, employer=ROOT, in_command=yes |
| Exodos: Optimize (rango elegido) | 2000 | 10 | 5000 | +10 | ≤90 | unidad spawneada, área 100% propia |
| Exodos: Gather activate | — | — | — | — | — | 1 rival exacto, employer=ROOT, in_command=yes |
| Exodos: Gather confirm | 1000 | 5 | 2500 | +10 | ≤90 | unidad detenida, área 100% propia |
| Exodos: Distribute activate | — | — | — | — | — | 1 rival exacto, employer=ROOT, in_command=yes |
| Exodos: Distribute confirm | 1000 | 5 | 2500 | +10 | ≤90 | unidad detenida, área 100% propia |
| Exodos: Transfer activate | — | — | — | — | — | — |
| Exodos: Transfer confirm | 2000 | 10 | 5000 | +20 | ≤80 | unidades detenidas, territories owner=ROOT |
| Exodos: Hijo del Rival | — | — | — | — | — | 1 rival exacto ≥16 años, employer=ROOT, is_male=yes |
| Exodos: Hija del Rival | — | — | — | — | — | 1 rival exacto ≥16 años, employer=ROOT, is_male=yes |
| BOM: Eliminar | 2000 | 1 | 500 | +40 | ≤80 | rivals ≥ 1 |
| BOM: Bacanal | 500 | — | — | +10 | ≤90 | rivals ≥ 1 |
| BOM: Kill Ruler | 2000 | 1 | 500 | +40 | ≤60 | stability ≥ 50 |
| IHA: Confiscar | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| IHA: Fill the Void | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| TLV: Confirm | 2000 | — | — | +40 | ≤60 | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL: Purchase | dinámico | — | — | +100 | ≤0 | one-shot |

---

## 2. EXODOS: OPTIMIZAR — DISEÑO COMPLETO

### 2.1 Descripción

Optimizar reemplaza y unifica las operaciones Gather y Distribute (que se mantienen como legacy).
El usuario elige el rango de pops de su área, el mod ejecuta Gather completo y luego Distribute
en la cantidad óptima calculada por el optimizador provincial, en un flujo continuo sin intervención
adicional del usuario.

### 2.2 Flujo de usuario

```
1. Usuario recluta leva del rival en el territory ancla (activa in_command)
   → Aparece "Exodos: Optimizar" en el panel de decisiones

2. Usuario activa Optimizar
   → Spawna unidad "Exodos - Optimize" en la province del rival
   → Aparecen las 17 decisiones de rango (exodos_opt_range_3 … exodos_opt_range_19)

3. Usuario elige el rango que corresponde a su total de pops
   → Cobra costos (2000 oro, 5000 manpower, +10 tyranny)
   → set_variable: exodos_optimize_count = N
   → set exodos_optimize_active, exodos_operation_active
   → Comienza Gather automático

4. Gather corre N pulsos (count=30 por asentamiento, piso total_population >= 2)
   → Cuando todas las fuentes llegan a < 2 pops: set exodos_optimize_gather_done

5. Detect exodos_optimize_gather_done → corre Distribute 1 pulso
   → count = var:exodos_optimize_count por cada asentamiento del área

6. Cleanup automático
```

**Advertencias en descripción de decisiones de rango (EN MAYÚSCULAS):**
- Esta operación puede tardar varios meses
- Se cancela automáticamente si cualquier territorio del área es perdido
- ESTA ACCIÓN NO PUEDE DESHACERSE — verificá tu conteo de pops antes de confirmar
- ELEGÍ EL RANGO CORRECTO — si elegís mal, la distribución quedará subóptima sin posibilidad de corrección

### 2.3 Variables de estado — Optimizar

**País:**
| Variable | Uso |
|---|---|
| `exodos_optimize_pending` | Activate ejecutado, esperando elección de rango |
| `exodos_optimize_active` | Guard — operación en ejecución |
| `exodos_optimize_gather_done` | Gather completado, señal para disparar Distribute |
| `exodos_optimize_count` | Count por asentamiento elegido por el usuario (3–19) — usado solo en el `limit` del `else_if` de Distribute para seleccionar el bloque correcto |

**IMPORTANTE — `count = var:X` no funciona en IR 2.0.4:**
`var:exodos_optimize_count` NO puede usarse como valor de `count` en un `while`.
El engine devuelve `Value of wrong type: 'none'` y el while no itera.
El Distribute usa 17 bloques `else_if` con `count` literal hardcodeado — ver sección 2.7 y 2.8.

**Nota:** `exodos_operation_active` actúa como guard global que bloquea el inicio de
cualquier otra operación de Exodus mientras Optimizar está corriendo. Es compartido
con Transfer, Gather y Distribute legacy.

**Nota:** `save_scope_as` NO persiste entre ticks — no necesita cleanup.

### 2.4 Unidad marcadora

| Propiedad | Valor |
|---|---|
| Nombre (código) | `"Exodos - Optimize"` |
| Nombre (ES) | `"Exodos - Optimizar"` |
| Nombre (EN) | `"Exodos - Optimize"` |
| Variable de unidad | `exodos_unit_optimize` |
| Spawn | En province del rival (mismo mecanismo que Gather/Distribute legacy) |

### 2.5 Tabla de decisiones de rango — CERRADO

Los puntos de cruce exactos fueron calculados con scipy.optimize.brentq sobre la función de
tiempo total del optimizador. Son el punto exacto (con decimales) donde el óptimo cambia de
sett_pops=N a sett_pops=N+1. Los totales enteros usan ceil del cruce.

| Decisión | Rango total | Count/asent | Título UI ES | Título UI EN |
|---|---|---|---|---|
| exodos_opt_range_3 | 45–58 | 3 | "Entre 45 y 58 pops en la provincia" | "Between 45 and 58 pops in the province" |
| exodos_opt_range_4 | 59–73 | 4 | "Entre 59 y 73 pops en la provincia" | "Between 59 and 73 pops in the province" |
| exodos_opt_range_5 | 74–88 | 5 | "Entre 74 y 88 pops en la provincia" | "Between 74 and 88 pops in the province" |
| exodos_opt_range_6 | 89–103 | 6 | "Entre 89 y 103 pops en la provincia" | "Between 89 and 103 pops in the province" |
| exodos_opt_range_7 | 104–117 | 7 | "Entre 104 y 117 pops en la provincia" | "Between 104 and 117 pops in the province" |
| exodos_opt_range_8 | 118–132 | 8 | "Entre 118 y 132 pops en la provincia" | "Between 118 and 132 pops in the province" |
| exodos_opt_range_9 | 133–147 | 9 | "Entre 133 y 147 pops en la provincia" | "Between 133 and 147 pops in the province" |
| exodos_opt_range_10 | 148–162 | 10 | "Entre 148 y 162 pops en la provincia" | "Between 148 and 162 pops in the province" |
| exodos_opt_range_11 | 163–176 | 11 | "Entre 163 y 176 pops en la provincia" | "Between 163 and 176 pops in the province" |
| exodos_opt_range_12 | 177–192 | 12 | "Entre 177 y 192 pops en la provincia" | "Between 177 and 192 pops in the province" |
| exodos_opt_range_13 | 193–209 | 13 | "Entre 193 y 209 pops en la provincia" | "Between 193 and 209 pops in the province" |
| exodos_opt_range_14 | 210–223 | 14 | "Entre 210 y 223 pops en la provincia" | "Between 210 and 223 pops in the province" |
| exodos_opt_range_15 | 224–238 | 15 | "Entre 224 y 238 pops en la provincia" | "Between 224 and 238 pops in the province" |
| exodos_opt_range_16 | 239–254 | 16 | "Entre 239 y 254 pops en la provincia" | "Between 239 and 254 pops in the province" |
| exodos_opt_range_17 | 255–268 | 17 | "Entre 255 y 268 pops en la provincia" | "Between 255 and 268 pops in the province" |
| exodos_opt_range_18 | 269–284 | 18 | "Entre 269 y 284 pops en la provincia" | "Between 269 and 284 pops in the province" |
| exodos_opt_range_19 | 285–300 | 19 | "Entre 285 y 300 pops en la provincia" | "Between 285 and 300 pops in the province" |

**Puntos de cruce (para referencia):**
3→4: 58/59 | 4→5: 73/74 | 5→6: 88/89 | 6→7: 103/104 | 7→8: 117/118 |
8→9: 132/133 | 9→10: 147/148 | 10→11: 162/163 | 11→12: 176/177 | 12→13: 192/193 |
13→14: 209/210 | 14→15: 223/224 | 15→16: 238/239 | 16→17: 254/255 |
17→18: 268/269 | 18→19: 284/285

**Por qué estos valores son correctos — CERRADO v1.11:** los rangos anteriores (v1.0–v1.10)
fueron calculados con scipy.brentq sobre la función de tiempo total sin considerar que el
Gather deja 1 pop por asentamiento. El count que reciben los asentamientos es `settPops - 1`,
no `settPops`. Al corregir esto, los puntos de cruce se desplazan ~1–6 pops hacia abajo en
todos los rangos. Verificado con búsqueda discreta exhaustiva para todos los totales 45–300.
Error máximo en cualquier total dentro de cada rango: ≤ 4.9 meses (umbral 5m). El rango 19
acepta hasta 7.8m en t=299–300 porque count=20 no existe en el mod (máximo es 19).
Progresión de anchos: 14–17 pops por rango, uniforme, sin saltos bruscos.

### 2.6 Mecánica del Gather en Optimizar

```pdxscript
# Igual que Gather legacy EXCEPTO:
count = 30  # (legacy usa 20)
# El piso es el mismo: total_population >= 2 (deja 1 pop mínimo en cada fuente)
# Cleanup: cuando todas las fuentes llegan a < 2 pops
#   → NO cleanup completo aún → set exodos_optimize_gather_done
```

### 2.7 Mecánica del Distribute en Optimizar

```pdxscript
# Un solo pulso — NO hay loop de pulsos como en Distribute legacy
# IMPORTANTE: count = var:X NO funciona en IR 2.0.4 — devuelve type 'none' y el while no itera.
# Solución: 17 bloques else_if independientes en exodos_on_action.txt, uno por rango,
#   cada uno con su count literal hardcodeado (3, 4, 5 … 19).
# El limit de cada bloque incluye var:exodos_optimize_count = N para seleccionar el rango correcto.
# NO hay piso de ancla — el freno es que el pulso corre 1 sola vez y termina
# Después del único pulso → exodos_cleanup_effect = yes dentro de cada bloque
```

**Por qué un solo pulso:** el piso del ancla variable dentro de cada rango hacía que
un freno fijo causara distribuciones incorrectas. Un solo pulso elimina el problema —
el count está calibrado para el rango exacto y no necesita freno.

**Por qué 17 bloques con count literal y no `count = var:exodos_optimize_count`:**
`count = var:X` es sintaxis inválida en IR 2.0.4 — el engine devuelve `Value of wrong type: 'none'`
y el `while` no itera en absoluto. Confirmado en error.log partida (línea 168 de `exodos_on_action.txt`).
La solución es hardcodear el count en cada bloque — simple, sin variables nuevas, sin patrones nuevos,
a prueba de fallos. Igual que las 17 decisiones de rango en `exodos_decisions_optimize.txt`.

### 2.8 Lógica del pulso mensual — Optimizar

```pdxscript
# En monthly_country_pulse, dentro del bloque exodos_operation_active:

# Fase Gather de Optimizar
if = {
    limit = {
        has_variable = exodos_optimize_active
        NOT = { has_variable = exodos_optimize_gather_done }
    }
    # ... mismo código que Gather legacy ALT con count=30 ...
    # Al terminar (todas fuentes < 2):
    if = {
        limit = { /* todas las fuentes < 2 pops */ }
        set_variable = { name = exodos_optimize_gather_done value = 1 }
        # NO cleanup aún — Distribute corre en el siguiente pulso
    }
}

# Fase Distribute de Optimizar — 17 bloques else_if, uno por rango, count literal
else_if = {
    limit = {
        has_variable = exodos_optimize_active
        has_variable = exodos_optimize_gather_done
        var:exodos_optimize_count = 3
    }
    var:exodos_anchor_province = {
        save_scope_as = exodos_origin
        area = {
            every_area_province = {
                limit = { owner = ROOT  total_population >= 1  NOT = { has_variable = exodos_is_anchor } }
                save_scope_as = exodos_dist_target
                while = {
                    count = 3   # ← literal hardcodeado
                    limit = { scope:exodos_origin = { total_population >= 2 } }
                    scope:exodos_origin = { random_pops_in_province = { move_pop = scope:exodos_dist_target } }
                }
            }
        }
    }
    exodos_cleanup_effect = yes
}
# ... else_if idénticos para count = 4, 5, 6 … 19 ...
```

**GOTCHA CRÍTICO — `count = var:X` no existe en IR 2.0.4:**
`while { count = var:exodos_optimize_count }` devuelve `Value of wrong type: 'none'` —
el while nunca itera y Distribute no mueve ningún pop. Confirmado en error.log partida.
Solución: 17 bloques `else_if` con `count` literal. Simple, sin variables nuevas, a prueba de fallos.

### 2.9 Cancel general — exodos_cancel_all — CERRADO

Siempre visible (`potential = { is_ai = no }`), siempre ejecutable (`allow = { always = yes }`).
Archivo: `exodos_decisions_cancel.txt` (separado de `exodos_decisions_optimize.txt`).

Limpia ABSOLUTAMENTE TODO el estado de TODOS los mods — tanto del ecosistema IRAM como del
ecosistema ALT anterior y del mod base (exodos estable). Sirve como herramienta de emergencia
y como primer paso obligatorio al migrar desde una partida con el mod anterior.

**Cancel particular (`exodos_cancel`) — ELIMINADO en IRAM:**
`exodos_cancel` existía en estable (`mod.zip`) y ALT (`mod_alt.zip`) con estructura idéntica:
aparece solo cuando hay operación activa, llama a `exodos_cleanup_effect`, siempre ejecutable.
Verificado en ambos zips — son idénticos. `exodos_cancel_all` lo reemplaza completamente:
hace lo mismo y además limpia los tres ecosistemas. **No agregar cancels particulares bajo ninguna circunstancia.**

**Variables de país a limpiar (lista exhaustiva):**
```
# IRAM — Optimize
exodos_optimize_pending, exodos_optimize_active, exodos_optimize_gather_done, exodos_optimize_count

# ALT / estable — Transfer
exodos_transfer_pending, exodos_transfer_active, exodos_anchor_province, exodos_destination_province, exodos_pulse_counter

# ALT / estable — Gather (Concentrate)
exodos_gather_pending, exodos_gather_active

# ALT / estable — Distribute
exodos_distribute_pending, exodos_distribute_active

# Guard global
exodos_operation_active

# TGL
tgl_purchased

# BOM Ego Sum
bom_ego_sum_mars_used, bom_ego_sum_iovis_used, bom_ego_sum_mercurii_used, bom_ego_sum_minervae_used
```

**Variables de province a limpiar:**
```
exodos_is_anchor, exodos_is_destination
```

**Unidades a destruir (con protección — solo si existen):**
```pdxscript
any_unit = {
    limit = {
        OR = {
            has_variable = exodos_unit_optimize
            has_variable = exodos_unit_concentrate
            has_variable = exodos_unit_distribute
            has_variable = exodos_unit_transfer_origin
            has_variable = exodos_unit_transfer_dest
        }
    }
    destroy_unit = yes
}
```

**Por qué usar limit:** `destroy_unit` en una unidad que no existe genera error en el log.
El `limit` protege — solo ejecuta si la unidad existe.

### 2.10 Procedimiento de migración desde mod_alt.zip

Al reemplazar `mod_alt.zip` por `mod_pack_IRAM.zip` en una partida existente:

1. Extraer `mod_pack_IRAM.zip` en `C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\`
   (reemplaza todo)
2. **NO modificar `dlc_load.json`** — sigue listando los cuatro mods. Las carpetas TEST SHELL
   hacen que el engine los cargue vacíos sin error.
3. Cargar la partida
4. **PRIMER PASO OBLIGATORIO:** ejecutar "Cancelar todo" inmediatamente
   Esto limpia cualquier variable o unidad del mod anterior que pudiera estar activa en el save.
5. Verificar `error.log` — debe estar limpio de referencias a `exodos_`, `bom_`, `tlv_`, `tgl_`
6. Continuar la partida normalmente

---

### 2.11 Localización — CERRADO

Textos finales de localización para Exodos: Optimizar y Cancel general.
Cerrados en sesión 2026-05. No reabrir salvo pedido explícito del usuario.

#### Decisiones de diseño tomadas en esta sección — fuentes y razonamiento

**D-LOC-1 — Terminología UI (provincia vs área, territorio vs provincia)**
Fuente: verificación en partida + wiki del juego.
El engine usa `province` para la casilla mínima del mapa y `area` para el agrupamiento.
La UI del juego invierte los términos: `territory` = casilla mínima, `province` = agrupamiento.
Todo el texto de localización usa la terminología de la UI del juego, no del código.

**D-LOC-2 — El costo NO se escribe en los textos**
Fuente: comportamiento del engine verificado en partida.
El engine muestra automáticamente los costos del `effect` en el tooltip de la decisión.
Escribir el costo en la descripción genera duplicación. Se eliminó de todos los textos.

**D-LOC-3 — El cancel particular (`exodos_cancel`) se elimina completamente**
Fuente: verificación de `mod.zip` (estable) y `mod_alt.zip` (ALT) — ambos tienen `exodos_cancel` idéntico.
El `exodos_cancel_all` cubre exactamente el mismo caso de uso y además limpia variables de los
tres ecosistemas (estable + ALT + IRAM). No hay ningún caso donde el cancel particular aporte
algo que el general no haga. Decisión: eliminado en IRAM, no migrar desde legacy.

**D-LOC-4 — La advertencia de cancelación involuntaria va en los rangos, no en el activate**
Fuente: decisión de diseño del usuario.
El cancel general cubre la cancelación voluntaria. La cancelación involuntaria (unidad destruida,
territorio perdido) se menciona en los rangos porque es ahí donde el jugador confirma y paga.

**D-LOC-5 — "ciudad principal en la provincia" en lugar de "ciudad capital"**
Fuente: corrección del usuario — "capital" es ambiguo (puede confundirse con la capital del país).
La unidad marca el ancla de la provincia optimizada, no necesariamente la capital nacional.

**D-LOC-6 — Voz del texto: "Se redistribuirán"**
Fuente: corrección del usuario — "Ejecutaremos" era primera persona plural sin antecedente claro.
"Se redistribuirán" es voz pasiva refleja, consistente con el tono impersonal del juego.

**D-LOC-7 — Ejemplo de provincia: "territorio Roma → provincia Latium"**
Fuente: corrección del usuario — "Lacio" no es el nombre exacto en la UI. "Latium" es el nombre
que muestra la UI del juego. Nota: el activate final eliminó el ejemplo explícito para acortar el texto.

**D-LOC-8 — Estructura del texto de rangos: mínimo absoluto (variante C)**
Fuente: decisión del usuario tras revisar tres variantes. Se eligió la más corta.
Eliminados: ejemplo de provincia, frase de distribución óptima, costo explícito.

#### Textos finales — ES (CERRADO)

**exodos_activate_optimize — título:**
`"Exodos: Optimizar"`

**exodos_activate_optimize — descripción:**
`Se redistribuirán los pops de la provincia de manera óptima para la conversión religiosa y asimilación cultural. Recluta o mueve un ejército o leva bajo el mando del rival del gobernante en cualquier territorio de la provincia — la unidad marcadora será generada ahí automáticamente, usala para marcar tu ciudad principal en la provincia. Podés moverla antes de elegir el rango, el costo de la operación se cobra en la siguiente decisión.`

**exodos_opt_range_3 … exodos_opt_range_19 — título (patrón):**
`"Optimizar: Entre X y Y pops en la provincia"` (X e Y según tabla de rangos en sección 2.5)

**exodos_opt_range_3 … exodos_opt_range_19 — descripción (idéntica para todos los rangos):**
`Verificá el total de pops de la provincia antes de confirmar — panel de provincia, entre el botón de gobernador y el de procuradores, o en Resumen / Administración / Gobernaciones. La operación será cancelada si la unidad marcadora es destruida o cualquier territorio de la provincia es perdido. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES.`

**exodos_cancel_all — título:** `"Cancelar Todo"`

**exodos_cancel_all — descripción:**
`Rescinde todos los decretos activos del estado. Limpia toda operación en curso — Exodos, transferencias, y cualquier estado residual de instalaciones anteriores del mod. Los costos ya pagados no serán reembolsados. Usar como primer paso al migrar desde una instalación anterior.`

#### Textos finales — EN (CERRADO)

**exodos_activate_optimize — título:** `"Exodos: Optimize"`

**exodos_activate_optimize — descripción:**
`The province's pops will be optimally redistributed for religious conversion and cultural assimilation. Raise or move an army or levy under the ruler's rival in any territory of the province — the marker unit will be generated there automatically, use it to mark your main city in the province. You may move it before choosing the range, the operation cost is charged in the next decision.`

**exodos_opt_range_3 … exodos_opt_range_19 — título (patrón):**
`"Optimize: Between X and Y pops in the province"` (X e Y según tabla de rangos en sección 2.5)

**exodos_opt_range_3 … exodos_opt_range_19 — descripción (idéntica para todos los rangos):**
`Verify the province's total pop count before confirming — province panel, hover between the governor button and the procurators button, or at Nation Overview / Administration / Governorships. The operation will be cancelled if the marker unit is destroyed or any territory in the province is lost. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS.`

**exodos_cancel_all — título:** `"Cancel All"`

**exodos_cancel_all — descripción:**
`Rescinds all active state decrees. Clears any ongoing operation — Exodos, transfers, and any residual state from previous mod installations. Costs already paid will not be refunded. Use as a first step when migrating from a previous installation.`

#### Cómo encontrar el total de pops en la UI del juego

- **Panel de provincia:** cliqueá cualquier territorio → panel de provincia → posá el mouse entre el botón de gobernador y el botón "Instalar procuradores regionales" → muestra total de pops y porcentaje por tipo.
- **Panel de nación:** Resumen de Nación → Administración → Gobernaciones → lista todas las provincias con su total.

## 3. EXODOS_ON_ACTION.TXT — DISEÑO CERRADO

### 3.1 Estructura general

El archivo reemplaza íntegramente el `exodos_on_action.txt` del ALT. Mismo guard de entrada:
```pdxscript
monthly_country_pulse = {
    effect = {
        if = {
            limit = {
                is_ai = no
                has_variable = exodos_operation_active
            }
            # bloque principal
        }
    }
}
```

### 3.2 Bloque 1 — Chequeos de error (if/else_if encadenados)

**Orden exacto:**

```pdxscript
# 1. Unidad Optimize destruida (solo cuando optimize_active está seteado)
if = {
    limit = {
        has_variable = exodos_optimize_active
        NOT = { any_unit = { has_variable = exodos_unit_optimize } }
    }
    trigger_event = { id = exodos.1 }
}
# 2. Unidad legacy destruida (solo cuando optimize NO está activo)
else_if = {
    limit = {
        NOT = { has_variable = exodos_optimize_active }
        NOT = {
            any_unit = {
                OR = {
                    has_variable = exodos_unit_concentrate
                    has_variable = exodos_unit_distribute
                    has_variable = exodos_unit_transfer_origin
                    has_variable = exodos_unit_transfer_dest
                }
            }
        }
    }
    trigger_event = { id = exodos.1 }
}
# 3. Ancla perdida
else_if = {
    limit = { var:exodos_anchor_province = { NOT = { owner = ROOT } } }
    trigger_event = { id = exodos.1 }
}
# 4. Destino perdido (solo Transfer)
else_if = {
    limit = {
        has_variable = exodos_transfer_active
        var:exodos_destination_province = { NOT = { owner = ROOT } }
    }
    trigger_event = { id = exodos.1 }
}
# 5. Provincia no 100% propia (solo Optimize)
else_if = {
    limit = {
        has_variable = exodos_optimize_active
        var:exodos_anchor_province = {
            area = { any_area_province = { NOT = { owner = ROOT } } }
        }
    }
    trigger_event = { id = exodos.1 }
}
# 6. Provincia no 100% propia (solo Gather legacy)
else_if = {
    limit = {
        has_variable = exodos_gather_active
        var:exodos_anchor_province = {
            area = { any_area_province = { NOT = { owner = ROOT } } }
        }
    }
    trigger_event = { id = exodos.1 }
}
# 7. Provincia no 100% propia (solo Distribute legacy)
else_if = {
    limit = {
        has_variable = exodos_distribute_active
        var:exodos_anchor_province = {
            area = { any_area_province = { NOT = { owner = ROOT } } }
        }
    }
    trigger_event = { id = exodos.1 }
}
```

**Nota D1 — chequeo de unidad por operación activa:** el chequeo es específico por operación, no un OR global. Si `optimize_active` está seteado, solo se verifica `exodos_unit_optimize`. Si no está seteado, se verifica el OR de las 4 variables legacy. Mezclarlos causaría falsos positivos.

**Nota — sin chequeo de guerra:** el estable tiene `war = yes` como primer chequeo. En IRAM (y ALT) ese chequeo no existe — las operaciones son operables en guerra. No agregar.

### 3.3 Bloque 2 — Operaciones (else del bloque de errores)

**Orden del chain if/else_if:**
```
if        → optimize_active + NOT gather_done   → Optimize fase Gather (count=30, piso >=2, al terminar set gather_done)
else_if   → optimize_active + gather_done       → Optimize fase Distribute (count=var:optimize_count, 1 pulso, cleanup)
else_if   → gather_active                       → Gather legacy (count=20, piso >=2, cleanup cuando todas <2)
else_if   → transfer_active                     → Transfer (count=10, 10 pulsos, cleanup por counter o fuente <2)
else_if   → distribute_active                   → Distribute legacy (count=10, piso ancla >=30, cleanup cuando <30)
```

**Optimize fase Gather:** igual que Gather legacy excepto `count = 30`. Al terminar (todas fuentes `< 2`): `set_variable = { name = exodos_optimize_gather_done value = 1 }` — NO cleanup aún.

**Optimize fase Distribute:** `count = var:exodos_optimize_count` por destino. 1 solo pulso, sin piso de ancla. Siempre `exodos_cleanup_effect = yes` al final.

---

## 4. CONVENCIONES DEL ECOSISTEMA — CERRADO

| Convención | Valor | Razón |
|---|---|---|
| `is_ai = no` en `potential` y `allow` | Siempre en ambos | `potential` filtra visualmente, `allow` es segunda línea de defensa |
| Cobro en decisión de rango (Optimizar) | En el efecto de la decisión de rango | El jugador paga cuando confirma el rango, no en activate |
| Cobro en `confirm` (Gather/Distribute/Transfer legacy) | Siempre | El jugador paga solo cuando está seguro |
| Sin cooldown | Siempre | Variables de tiempo generan fallos; `is_ai = no` es la única restricción de abuso |
| UTF-8 BOM en todos los .txt y .yml | Obligatorio | Sin BOM el engine no parsea los archivos del mod |
| Sin BOM en .mod y descriptor.mod | Obligatorio | Con BOM el engine corrompe la entrada |
| `ai_will_do = { factor = 0 }` | Siempre | Excluye a la IA de todas las decisiones |
| Ironman compatible | Obligatorio | Ningún mod usa mecanismos que rompan Ironman |
| Zip unificado | `mod_pack_IRAM.zip` | Un solo archivo de distribución, BOM validado |
| Sin popups de éxito | Heredado de v1.2 | Solo quedan popups de error (exodos.1) y estado (tlv.2) |
| Todo lo visible al usuario en idioma del usuario | Obligatorio | Nombres de decisiones, tooltips, unidades. Código interno siempre en inglés |
| Decisiones de rango aparecen SOLO después de activate | has_variable = exodos_optimize_pending | Evita saturar el panel con 17 botones permanentes |
| Cancel general siempre visible | always = yes | Herramienta de emergencia — no depende de estado activo |
| El ecosistema habilita, no castiga | Sin restricciones artificiales | Las descripciones y `is_ai = no` son suficiente protección |

---

## 4. GOTCHAS DEL ENGINE

*(Heredados íntegramente del backup ALT v1.3 — verificados en partida)*

### 4.1 Scopes

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| `ruler = { }` desde country scope en effect | `every_character = { limit = { is_ruler = yes } ... }` | BOM v2.5 |
| `ruler = { }` desde country scope en trigger | `any_character = { is_ruler = yes ... }` | BOM v2.5 |
| `every_rival = { }` directo desde country scope | `every_character = { limit = { is_ruler = yes } every_rival = { } }` | BOM v2.5 |
| `move_pop = prev` desde scope pop | `save_scope_as` antes del bucle + `move_pop = scope:nombre` | Exodus bug 1 |
| `every_owned_province { limit = { has_variable = X } }` para filtrar área | `var:province = { area = { every_area_province = {} } }` | Exodus bug 2 |
| Iterar holdings y remover en el mismo loop | `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = x } remove_holding = scope:x }` | IHA Seize |
| `current_ruler` desde province scope | No resuelve — guardar con `every_character = { limit = { is_ruler = yes } save_scope_as = X }` | IHA Fill the Void |
| `unit_commander` como trigger en unit scope | No existe — usar `commander = scope:X` en `any_unit`/`random_unit` | game.zip exhaustivo |
| `location = { }` en character scope para posición del ejército | Resuelve capital de gobernación, no posición del ejército | Exodus alt |

### 4.2 Variables y flags

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| `set_country_flag` / `has_country_flag` / `clr_country_flag` | `set_variable` / `has_variable` / `remove_variable` | Exodus bug 4 |
| `set_province_flag` / `has_province_flag` | `set_variable` / `has_variable` en scope province | Exodus bug 4 |
| `set_unit_flag` / `has_unit_flag` | `set_variable` / `has_variable` en scope unit | Exodus bug 4 |
| `check_variable = { ... }` como trigger | `var:nombre >= valor` directo | Exodus bug 4 |
| `var:X >= var:Y` (dos variables en trigger) | Contador descendente, comparar contra 0 | Exodus bug 3 |
| Scopes `save_scope_as` | **No persisten entre ticks** — no necesitan cleanup | Exodus alt |

### 4.3 Localización

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| Corchetes `[ ]` en texto libre de yml | Usar paréntesis `( )` | TGL v1.3, Exodus bug 24 |
| BOM UTF-8 ausente en .txt o .yml del mod | Agregar BOM `EF BB BF` — usar `build_mods.py` o Python `utf-8-sig` | Todos los mods |
| BOM presente en descriptor.mod o .mod raíz | Eliminar — esos archivos van sin BOM | Todos los mods |

### 4.4 Sintaxis que no existe

| Sintaxis errónea | Reemplazo correcto | Confirmado en |
|---|---|---|
| `every_owned_territory` | `every_owned_province` | TGL v1.1 |
| `province_rank = city_metropolis` | `has_province_rank = city_metropolis` | TGL v1.1 |
| `num_of_pops` como script value o trigger | `total_population >= N` en scope province | Exodus bug 9 |
| `disband_unit = yes` | `destroy_unit = yes` | Exodus bug 4 |
| `is_triggered_only = yes` en eventos de mod | Eliminar | Exodus bug 8 |
| `ai_will_do = { value = 0 }` | `ai_will_do = { factor = 0 }` | Exodus bug 4 |
| `death = { death_reason = ... }` desde ruler scope | No funciona, silencioso | BOM, TLV |
| `has_holding` como trigger directo | `num_holdings_owned > 0` en character scope | IHA design |
| `count = var:X` en `while` | No funciona — devuelve `Value of wrong type: 'none'`, el while no itera. Usar count literal hardcodeado. | IRAM Distribute — confirmado en partida 2026-05 |

### 4.5 Miscelánea

| Regla | Detalle | Confirmado en |
|---|---|---|
| Multiplicador manpower x500 | Valor en script = valor pantalla / 500 | Exodus |
| `country_event` siempre dispara en `root` | No dispara en el país del objetivo | BOM v2.1 |
| Cooldown con variables de tiempo | Genera fallos en el delay — no usar | BOM v2.3 |
| IDs de eventos | Deben ser numéricos: `exodos.1`, no `exodos.fail` | Exodus bug 10 |
| `destroy_unit` en unidad inexistente | Genera error en error.log — siempre usar dentro de `limit` | IRAM cancel_all |

---

## 5. GUÍA DE DIAGNÓSTICO — error.log

```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\logs\error.log
```

Buscar después de cargar la partida:
```
exodos_
bom_
tlv_
tgl_
iha_
Wrong scope
Data error in loc key
Corrupt Decision
```

Un error.log limpio no tiene hits en ninguna de estas búsquedas.

**Errores de vanilla — ignorar siempre:**
- `has_province_modifier` Wrong scope (~118 hits) — vanilla puro
- `Missing Icon for Modifier: exodos_marker_*` (19 hits) — permanente e ignorable

**Error cosmético propio — ignorar siempre:**
- `Undefined event target 'iha_holding'` en `decisions/exodos_decisions_bom.txt` línea 114 — cosmético permanente. El patrón `while { random_holdings { save_scope_as = iha_holding } remove_holding = scope:iha_holding }` funciona correctamente en partida (confirmado IHA Seize v2026-05) pero el engine loguea el scope como indefinido al cargarlo. No afecta ninguna mecánica.

---

## 6. EXODUS — FUNCIONES LEGACY (CONCENTRATE Y DISTRIBUTE)

*(Sin cambios respecto al backup ALT v1.3 — ver código completo en ese documento o en mod_alt.zip)*

Las funciones Concentrate (Gather) y Distribute se mantienen en IRAM sin modificaciones.
El código completo está en `mod_alt.zip` → `exodos/decisions/exodos_decisions.txt`
y en `exodos/common/on_action/exodos_on_action.txt`.

**Diferencias IRAM vs ALT que aplican también a legacy:**
- El archivo de decisiones se renombra a `exodos_decisions_gather_distribute.txt`
- El `exodos_cleanup_effect` en `exodos_scripted_effects.txt` agrega las variables nuevas de Optimizar

**exodos_cleanup_effect — variables adicionales a limpiar en IRAM:**
```pdxscript
# Agregar a exodos_scripted_effects.txt junto a las existentes:
remove_variable = exodos_optimize_pending
remove_variable = exodos_optimize_active
remove_variable = exodos_optimize_gather_done
remove_variable = exodos_optimize_count
```

---

## 7. BY OTHER MEANS, THE LAST VOTE, THE GREAT LEAP

*(Sin cambios respecto al backup ALT v1.3 — ver código completo en ese documento o en mod_alt.zip)*

El código de BOM v3.0, TLV v1.7 y TGL v1.5 se migra íntegramente a `exodos/decisions/`
y `exodos/localization/`. No hay cambios de código — solo cambio de ubicación de archivos.

**Verificado: no hay conflictos de keys de localización entre mods.**
Todos los prefijos son únicos: `exodos_*`, `bom_*`, `iha_*`, `tlv_*`, `tgl_*`.

**`bom_events.txt`:** contiene solo `namespace = bom` — se descarta. No hay nada que migrar.

---

## 7. EXODOS: HEREDERO DEL RIVAL — DISEÑO COMPLETO

### 7.1 Descripción

Función de utilidad pura — no setea variables de estado, no genera unidades marcadoras, no tiene cleanup.
Spawnea un hijo o hija recién nacido del rival del gobernante. El personaje hereda familia, religión y cultura del rival.
El nombre es asignado automáticamente por el engine según la cultura. Sin costo. Sin límite de usos.

### 7.2 Condiciones

```
potential:
  is_ai = no
  any_character = {
    is_ruler = yes
    num_of_rivals >= 1
    NOT = { num_of_rivals >= 2 }
    any_rival = {
      employer = ROOT
      is_male = yes
      age >= 16
    }
  }

allow:
  is_ai = no
  custom_tooltip = exodos_tt_rival_unique
  [mismas condiciones que potential]
```

**Nota de diseño:** `is_male = yes` en el rival porque solo el padre puede ser `father =` en `create_character`. Si el rival fuera mujer, no aplica el mecanismo — la decisión simplemente no aparece.

### 7.3 Effect

```pdxscript
effect = {
  every_character = {
    limit = { is_ruler = yes }
    every_rival = {
      limit = {
        employer = ROOT
        is_male = yes
        age >= 16
      }
      save_scope_as = exodos_rival
      if = {
        limit = { is_married = yes }
        spouse = { save_scope_as = exodos_rival_spouse }
      }
    }
  }
  if = {
    limit = { exists = scope:exodos_rival_spouse }
    create_character = {
      age = 0
      female = no   # (o yes para hija)
      save_scope_as = exodos_newborn
      family = scope:exodos_rival.family
      religion = scope:exodos_rival.religion
      culture = scope:exodos_rival.culture
      father = scope:exodos_rival
      mother = scope:exodos_rival_spouse
    }
  }
  else = {
    create_character = {
      age = 0
      female = no   # (o yes para hija)
      save_scope_as = exodos_newborn
      family = scope:exodos_rival.family
      religion = scope:exodos_rival.religion
      culture = scope:exodos_rival.culture
      father = scope:exodos_rival
    }
  }
  scope:exodos_newborn = {
    # Traits patrilineales (los 7)
    if = { limit = { scope:exodos_rival = { has_trait = antigonids  } } add_trait = antigonids  }
    if = { limit = { scope:exodos_rival = { has_trait = antipatrid  } } add_trait = antipatrid  }
    if = { limit = { scope:exodos_rival = { has_trait = lagids      } } add_trait = lagids      }
    if = { limit = { scope:exodos_rival = { has_trait = seleucids   } } add_trait = seleucids   }
    if = { limit = { scope:exodos_rival = { has_trait = argeads     } } add_trait = argeads     }
    if = { limit = { scope:exodos_rival = { has_trait = aeacidae    } } add_trait = aeacidae    }
    if = { limit = { scope:exodos_rival = { has_trait = alcimachid  } } add_trait = alcimachid  }
    # Trait matrilineal (solo argeads — verificado en character_events.35 vanilla)
    if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = argeads } } add_trait = argeads }
  }
}
```

**Por qué herencia explícita y no `character_events.35`:** el evento vanilla que hereda traits dinásticos es `type = character_event` y requiere employer para procesar al personaje. `create_character` no acepta `employer` como parámetro (el engine lo ignora silenciosamente). Sin employer, el evento se descarta y el hijo no hereda nada. La solución es copiar los traits directamente en el `effect` usando `save_scope_as = exodos_newborn` para referenciar al recién nacido.

**Por qué `spouse` se guarda dentro del loop `every_rival`:** vanilla accede a `spouse = { }` siempre con el personaje como scope activo (root o dentro de un loop). Guardar la esposa fuera del loop via `scope:exodos_rival = { spouse = { } }` no tiene precedente confirmado en vanilla. Al guardar dentro del loop, el rival ya es el scope activo — idéntico al patrón vanilla. La condición de salida usa `exists = scope:exodos_rival_spouse` en lugar de `has_spouse = yes` porque el scope puede no existir si el rival no estaba casado.

**Traits matrilineales:** vanilla hereda solo `argeads` de la madre (verificado en `character_events.35`). Los otros 6 traits son exclusivamente patrilineales. El bloque matrilineal usa `exists = scope:exodos_rival_spouse` como guard para el caso sin madre.

**`employer` no es parámetro válido de `create_character` en IR 2.0.4** — confirmado en vanilla: ningún `create_character` del juego usa `employer`. El engine lo ignora sin error en log. Intentado en v1.1 sin efecto.

### 7.4 Variables de estado

**Ninguna.** Esta función no usa variables de estado. No hay nada que limpiar.
`exodos_cancel_all` no necesita modificarse.

### 7.5 Archivos modificados

| Archivo | Cambio |
|---|---|
| `exodos/decisions/exodos_decisions_rival_heir.txt` | CREADO — contiene `exodos_spawn_rival_son` y `exodos_spawn_rival_daughter` |
| `exodos/localization/spanish/exodos_l_spanish.yml` | Keys agregadas al final |
| `exodos/localization/english/exodos_l_english.yml` | Keys agregadas al final |

### 7.6 Localización — CERRADA

**Español:**
```yaml
 # ── HEREDERO DEL RIVAL ────────────────────────────────────────────
 exodos_spawn_rival_son:0 "Exodos: Hijo del Rival"
 exodos_spawn_rival_son_desc:0 "Nacera un hijo varon del rival del gobernante. El nino heredara la familia, religion y cultura del rival — y los rasgos dinasticos de ambos padres si los tienen. Su nombre sera asignado segun la cultura."
 exodos_spawn_rival_daughter:0 "Exodos: Hija del Rival"
 exodos_spawn_rival_daughter_desc:0 "Nacera una hija mujer del rival del gobernante. La nina heredara la familia, religion y cultura del rival — y los rasgos dinasticos de ambos padres si los tienen. Su nombre sera asignado segun la cultura."
 exodos_tt_rival_unique:0 "Se requiere exactamente un rival del gobernante al servicio del jugador, mayor de 16 anos. (Condicion de rival no cumplida)"
```

**English:**
```yaml
 # ── RIVAL HEIR ────────────────────────────────────────────────────
 exodos_spawn_rival_son:0 "Exodos: Rival's Son"
 exodos_spawn_rival_son_desc:0 "A son of the ruler's rival will be born. The child will inherit the rival's family, religion, and culture — and dynastic traits from both parents if they have them. His name will be assigned according to the rival's culture."
 exodos_spawn_rival_daughter:0 "Exodos: Rival's Daughter"
 exodos_spawn_rival_daughter_desc:0 "A daughter of the ruler's rival will be born. The child will inherit the rival's family, religion, and culture — and dynastic traits from both parents if they have them. Her name will be assigned according to the rival's culture."
 exodos_tt_rival_unique:0 "Exactly one rival of the ruler is required — in the player's service, aged 16 or older. (Rival condition not met)"
```

### 7.7 Estado

**v1.6 IMPLEMENTADO.** Entregado en `mod_pack_IRAM_12.zip`. BOM validado.

**Historial de correcciones:**
- v1.0 — `create_character` sin employer ni herencia explícita. Traits dinásticos no heredados.
- v1.1 — `employer = ROOT` agregado a `create_character`. Sin efecto — parámetro ignorado silenciosamente por el engine. Traits dinásticos no heredados.
- v1.2 — Herencia explícita con `save_scope_as = exodos_newborn` + 7 bloques `if/add_trait`. No depende del evento vanilla.
- v1.3 — `mother` asignada: si el rival tiene esposa (`has_spouse = yes`), se guarda con `spouse = { save_scope_as = exodos_rival_spouse }` y se pasa como `mother = scope:exodos_rival_spouse` en `create_character`. Si no tiene esposa, el personaje se crea sin madre (branch `else`). Aplica a hijo y hija.
- v1.4 — `spouse` guardada dentro del loop `every_rival` (patrón vanilla confirmado). Condición de madre cambiada a `exists = scope:exodos_rival_spouse`. Herencia matrilineal de `argeads` agregada desde la madre (único trait matrilineal en vanilla, verificado en `character_events.35`).
- v1.5 — Herencia matrilineal extendida en `exodos_spawn_rival_daughter`: los 7 traits dinásticos se heredan de la madre si existe, igual que del padre. Antes solo `argeads` era matrilineal. Ahora todas las dinastías funcionan como `argeads` en ambas direcciones.
- v1.6 — Herencia matrilineal extendida en `exodos_spawn_rival_son`: mismo cambio que v1.5 aplicado al hijo. Ambas decisiones son ahora simétricas — los 7 traits se heredan del padre Y de la madre independientemente.

---

## 8. OPTIMIZADOR PROVINCIAL — REFERENCIA

*(Backup completo en `optimizador_provincial_backup_v3.md`)*

El optimizador es una herramienta separada del mod — es un archivo HTML que el usuario
abre en el navegador para calcular la distribución óptima de pops antes de ejecutar Optimizar.

### 8.1 Parámetros clave del optimizador

```javascript
const N_SETT = 9;
const SPD = {
    city_conv_ph1:  11.59,
    city_assim_ph1:  5.52,
    city_assim_ph2:  6.87,
    sett_conv_ph1:   6.77,
    sett_assim_ph1:  0.43,
    sett_assim_ph2:  1.80,
};
const FLAT_CONV_CIUDAD  = 5.15;
const MULT_CONV_4DEIF   = 2.25;
const FLAT_ASSIM_CIUDAD = 3.35;
```

### 8.2 Relación entre optimizador y Optimizar

El optimizador calcula qué distribución (ciudad/asentamientos) minimiza el tiempo total.
La función Optimizar ejecuta esa distribución en el juego mediante Gather + Distribute.
Las 17 decisiones de rango están calibradas sobre los resultados del optimizador —
los puntos de cruce exactos determinan dónde cambia el count óptimo.

El usuario consulta el optimizador, cuenta los pops del área en el juego, e ingresa el total.
El optimizador le dice la distribución óptima. El usuario elige la decisión de rango correspondiente.
El mod hace el resto.

### 8.3 Nota de corrección pendiente — calcPlan (BAJA PRIORIDAD)

En `calcPlan`, los valores `settAssimDone` y `cityAssimDone` se calculan con flotantes,
pero el simulador avanza de a 1 pop entero por mes. Esto genera diferencias de pocos meses
entre el tiempo calculado en el plan y el tiempo real del simulador.

**Fix:** usar `Math.ceil(switchMonth)` y `Math.floor` en los pops completados.
Esta corrección es de consistencia, no de lógica. No afecta las decisiones de rango.
**No implementar salvo pedido explícito del usuario.**

---

## 9. INSTALACIÓN

Extraer `mod_pack_IRAM.zip` en:
```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\
```

Extracción limpia — reemplaza todo lo que hubiera.
**NO modificar `dlc_load.json`** — debe quedar igual que antes de la migración.

Al cargar la partida por primera vez: **ejecutar "Cancelar todo" inmediatamente.**

---

## 10. PENDIENTES

### Orden óptimo de codeo — SEGUIR ESTE ORDEN

Las tareas tienen dependencias reales. Ejecutar fuera de orden puede generar código que referencia
variables o efectos que aún no existen.

| Paso | Tarea | Depende de | Notas |
|---|---|---|---|
| 1 | Codear `exodos_scripted_effects.txt` | Nada | Define `exodos_cleanup_effect` — todos los demás archivos lo llaman. Ir primero. Ver sección 6 |
| 2 | Codear `exodos_units.txt` | Nada | Independiente. Agregar "Exodos - Optimize" / "Exodos - Optimizar". Sin decisiones pendientes |
| 3 | Codear `exodos_on_action.txt` | Paso 1 | Llama a `exodos_cleanup_effect`. Diseño cerrado — ver sección 3 |
| 4 | Codear `exodos_decisions_optimize.txt` | Paso 1, 2 | activate + 17 rangos. Archivo generado en sesión anterior — revisar y corregir si es necesario. Localización cerrada en sección 2.11. Ver sección 2 |
| 5 | Codear `exodos_decisions_cancel.txt` | Paso 1 | Solo `exodos_cancel_all`. Cancel particular legacy ELIMINADO. Ver sección 2.9 |
| 6 | Codear localización ES y EN | Pasos 4, 5 | Textos CERRADOS — usar exactamente los de sección 2.11 sin modificar. Títulos de rangos en tabla 2.5 |
| 7 | Migrar BOM/TLV/TGL a `exodos/` + TEST SHELL | Nada | Copiar archivos de `mod_alt.zip`. Crear `descriptor.mod` vacíos para TEST SHELL |
| 8 | Actualizar `exodos.mod` y `descriptor.mod` | Paso 7 | Nombre IRAM, versión 1.0. Ver sección 1.2. Sin BOM |
| 9 | Generar `mod_pack_IRAM.zip` con BOM validado | Todos | Ejecutar `build_mods.py` → renombrar salida a `mod_pack_IRAM.zip` |

### Tareas de menor prioridad

| Tarea | Prioridad | Notas |
|---|---|---|
| Auditar `exodos_on_action.txt` — verificar que Gather y Distribute legacy usan código ALT y no estable | **ALTA** | Riesgo real: el código del estable (count=20 Gather, piso=10 Distribute) y el ALT (count=20 Gather, piso=30 Distribute) son similares pero distintos. IRAM hereda del ALT. Verificar contra `mod_alt.zip` sección 4.7 antes del próximo build. |
| Evaluar contador de pulsos como límite secundario para Gather/Distribute legacy | **MEDIA** | Heredado de ALT pendientes |
| Fix calcPlan del optimizador (Math.ceil/Math.floor) | **BAJA** | Ver sección 8.3 — no afecta rangos |
| Publicar en Steam Workshop | **BAJA** | — |

---

## 11. HISTORIAL

### v1.11 — 2026-05
- **EXODOS: OPTIMIZAR — Rangos corregidos** — Los 17 rangos de las decisiones de rango fueron recalculados considerando que el Gather deja 1 pop por asentamiento (no 0). El count que recibe cada asentamiento es `settPops - 1`, por lo que los puntos de cruce reales se desplazan ~1–6 pops hacia abajo respecto a los valores anteriores (calculados con scipy.brentq sin esta corrección). Los nuevos rangos fueron verificados por búsqueda discreta exhaustiva para todos los totales 45–300. Error máximo dentro de cada rango: ≤ 4.9 meses. Progresión de anchos uniforme: 14–17 pops por rango.
- **Archivos modificados:** `exodos/localization/spanish/exodos_l_spanish.yml` (17 títulos de rango), `exodos/localization/english/exodos_l_english.yml` (17 títulos de rango). BOM validado. El `exodos_on_action.txt` y `exodos_decisions_optimize.txt` no cambian — los counts (3–19) son correctos. Entregado como `mod_pack_IRAM_13.zip`.

### v1.10 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.6** — Herencia matrilineal extendida en `exodos_spawn_rival_son`: los 7 traits dinásticos se heredan de la madre si existe, igual que del padre. Antes solo `argeads` era matrilineal en el hijo. Ahora hijo y hija son simétricos — todas las dinastías funcionan como `argeads` en ambas líneas.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`, `exodos/localization/spanish/exodos_l_spanish.yml`, `exodos/localization/english/exodos_l_english.yml`. BOM validado. Entregado como `mod_pack_IRAM_12.zip`.

### v1.9 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.5** — Herencia matrilineal extendida en `exodos_spawn_rival_daughter`: los 7 traits dinásticos (`antigonids`, `antipatrid`, `lagids`, `seleucids`, `argeads`, `aeacidae`, `alcimachid`) se heredan de la madre si existe y tiene el trait, además de los del padre. Antes solo `argeads` era matrilineal. Ahora todas las dinastías funcionan como `argeads` — ambas líneas transmiten de forma independiente.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`, `exodos/localization/spanish/exodos_l_spanish.yml`, `exodos/localization/english/exodos_l_english.yml`. BOM validado. Entregado como `mod_pack_IRAM_11.zip`.

### v1.8 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.4** — Corrección de scope: `spouse` ahora se guarda dentro del loop `every_rival` mientras el rival es el scope activo, siguiendo el patrón vanilla confirmado. Condición para asignar madre cambiada de `has_spouse = yes` a `exists = scope:exodos_rival_spouse`. Herencia matrilineal agregada: `argeads` desde la madre si existe y tiene el trait (único trait matrilineal en vanilla, verificado en `character_events.35`).
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`. BOM validado. Entregado como `mod_pack_IRAM_10.zip`.

### v1.7 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.3** — Corrección: `mother` no era asignada al personaje creado. Fix: si `scope:exodos_rival` tiene esposa (`has_spouse = yes`), se guarda como `scope:exodos_rival_spouse` y se pasa como `mother =` en `create_character`. Si el rival no tiene esposa, el personaje se crea sin madre (branch `else`). Aplica a `exodos_spawn_rival_son` y `exodos_spawn_rival_daughter`.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`. BOM validado. Entregado como `mod_pack_IRAM_9.zip`.

### v1.6 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.2** — Corrección de bug: herencia explícita de traits dinásticos. `employer = ROOT` dentro de `create_character` (v1.1) era inválido — el engine lo ignora silenciosamente, confirmado contra vanilla. Solución: `save_scope_as = exodos_newborn` dentro de `create_character` + 7 bloques `if/add_trait` sobre `scope:exodos_newborn` para los traits `antigonids`, `antipatrid`, `lagids`, `seleucids`, `argeads`, `aeacidae`, `alcimachid`. No depende del evento vanilla `character_events.35`. Alternativa `move_country` documentada en sección 12.9.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`. BOM validado. Entregado como `mod_pack_IRAM_8.zip`.

### v1.5 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL v1.1** — Corrección de bug: `employer = ROOT` agregado a `create_character` en ambas decisiones (hijo y hija). Sin él, `character_events.35` (herencia de traits dinásticos del padre) no procesaba al recién nacido por falta de employer y se descartaba silenciosamente. Confirmado en partida con 2 hijos y 1 hija sin trait dinástico. Con el fix el evento vanilla corre correctamente al día siguiente del nacimiento.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt`. BOM validado. Entregado como `mod_pack_IRAM_7.zip`.

### v1.4 — 2026-05
- **EXODOS: HEREDERO DEL RIVAL** — Nueva función implementada. Dos decisiones: `exodos_spawn_rival_son` y `exodos_spawn_rival_daughter`. Spawnea hijo o hija recién nacido del rival del gobernante — hereda familia, religión y cultura del rival. Sin costo, sin variables de estado, sin unidades marcadoras, sin cancel particular. `exodos_cancel_all` sin modificaciones.
- **Archivos creados/modificados:** `exodos/decisions/exodos_decisions_rival_heir.txt` (nuevo), `exodos/localization/spanish/exodos_l_spanish.yml` (5 keys agregadas), `exodos/localization/english/exodos_l_english.yml` (5 keys agregadas). BOM validado. Entregado como `mod_pack_IRAM_6.zip`.

### v1.3 — 2026-05
- **EXODOS: OPTIMIZAR — Localización** — Títulos de los 17 rangos: eliminado el prefijo "Optimizar: " / "Optimize: " en ES y EN. Títulos quedan como "Entre X y Y pops en la provincia" / "Between X and Y pops in the province".
- **EXODOS: OPTIMIZAR — Localización** — Descripción de los 17 rangos reestructurada en tres párrafos separados por línea en blanco (`\n\n`): (1) instrucción de verificación, (2) advertencia de cancelación en minúsculas, (3) advertencia de irreversibilidad en mayúsculas con frase final agregada: "GUARDA LA PARTIDA Y HAZ UNA COPIA DE RESPALDO." / "MAKE A SAVE AND KEEP A BACKUP."
- **Archivos modificados:** `exodos/localization/spanish/exodos_l_spanish.yml`, `exodos/localization/english/exodos_l_english.yml`. BOM validado en ambos. Entregado como `mod_pack_IRAM_4.zip`.

### v1.2 — 2026-05
- **EXODOS: OPTIMIZAR** — Renombradas las 7 keys de decisión de rango de un dígito: `exodos_opt_range_3` … `exodos_opt_range_9` → `exodos_opt_range_03` … `exodos_opt_range_09`. Objetivo: que el orden alfabético en el panel de decisiones coincida con el orden de menor a mayor pops.
- **Archivos modificados:** `exodos/decisions/exodos_decisions_optimize.txt` (8 ocurrencias), `exodos/localization/spanish/exodos_l_spanish.yml` (14 ocurrencias), `exodos/localization/english/exodos_l_english.yml` (14 ocurrencias).
- **No tocado:** `exodos/common/on_action/exodos_on_action.txt` — no contenía referencias a estas keys. Keys `exodos_opt_range_10` … `exodos_opt_range_19` sin cambios.
- **BOM validado:** los 3 archivos `.txt`/`.yml` modificados mantienen BOM `EF BB BF`. Los 4 `.mod` raíz sin BOM. Entregado como `mod_pack_IRAM_4.zip`.

### v1.1 — 2026-05
- **EXODOS: OPTIMIZAR** — Distribute corregido: `count = var:exodos_optimize_count` no funciona en IR 2.0.4 (`Value of wrong type: 'none'`). Reemplazado por 17 bloques `else_if` en `exodos_on_action.txt`, uno por rango, cada uno con `count` literal hardcodeado (3–19) y `var:exodos_optimize_count = N` en el `limit`.
- **EXODOS: OPTIMIZAR** — Orden de las decisiones de rango verificado: 3→19 (menor a mayor pops), correcto en decisiones y localización.
- **Doc** — Sección 2.3: `exodos_distribute_iter` eliminado — no necesario con el approach de 17 bloques literales. Gotcha `count = var:X` documentado.
- **Doc** — Sección 2.7: mecánica del Distribute actualizada — 17 bloques literales explicados.
- **Doc** — Sección 2.8: pseudocódigo del pulso actualizado con el approach correcto.
- **Doc** — Sección 5 (diagnóstico): error cosmético `iha_holding` documentado como permanente e ignorable.
- **Doc** — Sección 10 pendientes: auditoría de funciones legacy ALT vs estable agregada como tarea ALTA.
- **Doc** — Sección 4.2 gotchas: `count = var:X` agregado como sintaxis inválida en IR 2.0.4.

### v1.0 — 2026-05
- Proyecto IRAM creado desde Drago Mod Pack Alt v1.3
- Unificación de todos los mods dentro de `exodos/`
- Diseño completo de Exodos: Optimizar (pendiente de implementación)
- 17 decisiones de rango calculadas con scipy.brentq (puntos de cruce exactos)
- Cancel general `exodos_cancel_all` diseñado — limpia todo el ecosistema IRAM + ALT + estable
- Procedimiento de migración desde partidas con mod_alt.zip documentado
- Funciones Concentrate y Distribute mantenidas como legacy
- Backup del optimizador provincial integrado como sección de referencia
- Localización ES y EN cerrada (sección 2.11) — textos finales de Optimizar y Cancel general
- Cancel particular (exodos_cancel) eliminado — reemplazado íntegramente por exodos_cancel_all
- Reglas de trabajo actualizadas: costo fuera de textos, cancel particular prohibido
- Lista de archivos necesarios para continuar documentada en instrucciones para la IA

---

## 12. NOTAS Y DUDAS ABIERTAS

Observaciones surgidas durante el desarrollo — no bloquean funcionalidad actual pero pueden ser relevantes en sesiones futuras. Las marcadas **TESTEAR** requieren verificación en partida antes de poder cerrarlas.

### 12.1 `exodos_tt_rival_unique` — riesgo de colisión futura

La key `exodos_tt_rival_unique` (Heredero del Rival) es distinta de `exodos_tt_rival_commander` (Optimizar/Gather/Distribute). No hay colisión actual. Pero si se agrega una función nueva con condición de rival similar, hay riesgo de reutilizar mal la key. Verificar que cualquier función nueva con condición de rival use o cree su propia tooltip si las condiciones difieren.

### 12.2 Rival mujer — decisiones de Heredero del Rival no aparecen

`is_male = yes` en el rival es requerido porque `create_character` acepta `father =` (y `mother =`) pero el mecanismo está diseñado para usar al rival masculino como padre. Si el jugador tiene una rival mujer, las dos decisiones simplemente no aparecen en el panel — comportamiento correcto por diseño, no un bug. No hay decisión equivalente para rival mujer. Esta limitación es de diseño, no del engine. Documentar si el usuario reporta confusión.

### 12.3 `exodos_rival` scope — no necesita cleanup en `exodos_cancel_all`

`save_scope_as = exodos_rival` no persiste entre ticks (confirmado en sección 2.3). Por eso no aparece en la lista de variables a limpiar en `exodos_cancel_all`. Si en el futuro alguien audita el cancel y no encuentra `exodos_rival`, es correcto — no es un olvido.

### 12.4 Orden alfabético en panel — `exodos_spawn_*` entre rangos y transfer

Las decisiones `exodos_spawn_rival_daughter` y `exodos_spawn_rival_son` aparecen alfabéticamente después de `exodos_opt_range_XX` y antes de `exodos_transfer_*`. El orden visual en pantalla no fue verificado en partida. Si el orden importa, testear y ajustar los nombres de key si es necesario.

### 12.5 Fuente de verdad para funciones post-v1.0

El backup indica `mod_alt.zip` como archivo base para continuar el desarrollo. Esto es correcto para las funciones legacy (Transfer, Gather, Distribute, BOM, TGL, TLV). Para funciones nuevas implementadas en IRAM (Optimizar, Heredero del Rival), la fuente de verdad es el último `mod_pack_IRAM_X.zip`. La IA que lea las instrucciones debe tener esto en cuenta — pedir `mod_alt.zip` solo si trabaja sobre código legacy.

### 12.6 Sexo del hijo — fijo por diseño, no por limitación del engine ⚠ DOCUMENTAR

El sexo del hijo/hija está hardcodeado en `create_character` (`female = no` / `female = yes`). Una versión con sexo aleatorio sería posible usando `random_list` o similar, pero no está implementada. Esta fue una decisión de diseño explícita — dos decisiones separadas, una por sexo — no una limitación del engine.

### 12.7 `family` del rival puede ser null — comportamiento no verificado ⚠ TESTEAR

`create_character` con `family = scope:exodos_rival.family` asume que el rival tiene familia asignada. Los personajes generados proceduralmente en IR 2.0.4 a veces no tienen familia. Si `scope:exodos_rival.family` es null, el engine puede ignorar el campo silenciosamente o generar un error en `error.log`. **Testear en partida con un rival sin familia antes de dar la función por completamente estable.** Si es un problema, la solución es un `if = { limit = { scope:exodos_rival = { has_family = yes } } }` wrapper o simplemente omitir el campo `family`.

**Nota:** el bug de herencia de traits dinásticos (v1.0 → v1.2) no estaba relacionado con `family`. Esta duda sigue abierta independientemente.

### 12.9 Alternativa para asignar employer al recién nacido — `move_country`

Si en el futuro se necesita que el hijo tenga employer (por ejemplo, para que `character_events.35` corra automáticamente o para otras mecánicas del engine), la forma correcta en IR 2.0.4 es `move_country` después del `create_character`, usando `save_scope_as` para referenciar al personaje:

```pdxscript
create_character = {
    age = 0
    save_scope_as = exodos_newborn
    ...
}
scope:exodos_newborn = {
    move_country = ROOT
}
```

`employer` dentro de `create_character` no es un parámetro válido — el engine lo ignora silenciosamente sin error en log. Confirmado en vanilla: ningún `create_character` del juego base usa `employer`. `move_country` es el mecanismo correcto y está ampliamente usado en vanilla para asignar/mover personajes entre países.

### 12.8 `exodos_decisions_bom_ego_sum.txt` ausente en tabla de funciones (sección 1.3)

La sección 1.3 no lista BOM Ego Sum como función separada. El archivo `exodos_decisions_bom_ego_sum.txt` existe en el zip y tiene sus propias keys (`bom_ego_sum_*`). No es algo introducido en v1.4 — ya estaba antes — pero la tabla de funciones queda incompleta. Agregar fila en próxima sesión si se trabaja sobre esa sección.

---

*Imperator: Rome — Alternative Mechanics MOD PACK — Backup Técnico v1.10 — 2026-05*
*Proyecto continúa desde: Drago Mod Pack Alt v1.3 (mod_alt.zip) + Optimizador Provincial v3.0 (imperator_optimizer_v4.html)*
