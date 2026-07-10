# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK
## SUPERBACKUP TÉCNICO UNIFICADO — v2.1
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | zip activo: mod_pack_IRAM_v4_0.zip (v4.0 — canónico)

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0 — INSTRUCCIONES PARA LA IA
# LEER COMPLETO ANTES DE ESCRIBIR CUALQUIER LÍNEA
# ══════════════════════════════════════════════════════════

## 0.1 QUÉ ES ESTE DOCUMENTO

Este documento es la **única fuente de verdad** de todo el proyecto IRAM.
Cubre la historia completa del proyecto (IRAM v1 → v2 → v3 → v4), el código fuente
completo de todas las versiones (v1, v2 y v3), y el diseño completo de IRAM v4.

**Un zip canónico activo:**
- `mod_pack_IRAM_v4_0.zip` — **IRAM v4.0** (versión activa de v4). Contiene Gather Global con capital exclusion, Distribute 4 rangos, Relics (tokens corregidos), sin scripted_gui, sin unidades marcadoras para Gather Global.

Para comparación histórica con v3: `mod_pack_IRAM_15.zip` (v3 FINAL, cerrado). Para análisis de la arquitectura experimental descartada: `mod_pack_IRAM_v4_3.zip` (rama experimental, ver Sección 18.4).

El documento es autónomo para diseño, decisiones y referencia. Para el código exacto de v4 usar el zip v4 — el documento documenta el diseño, el zip es la implementación.

**Regla de comparación de fuentes:** si el zip contradice el documento en diseño, el documento manda. Si el zip contradice el documento en código v4, el zip manda. Si difieren en algo no registrado en Sección 19, preguntar antes de asumir. Para entender diferencias entre zips, ver Sección 21.

**Si algo está documentado aquí: no preguntar. Está resuelto.**
**Si algo no está documentado: preguntar al usuario antes de asumir o inventar.**

---

## 0.2 CHECKLIST OBLIGATORIO — EJECUTAR EN ORDEN ANTES DE RESPONDER

- [ ] **1.** Leer este documento completo de principio a fin.
- [ ] **2.** Abrir `mod_pack_IRAM_v4_0.zip` — es el zip canónico activo de v4.
- [ ] **3.** No asumir sintaxis del engine de memoria. Verificar contra archivos fuente o la Sección 6.
- [ ] **4.** Revisar la Sección 0.5 (Estado actual del proyecto) antes de escribir una sola línea de código.
- [ ] **5.** Preguntar al usuario qué quiere hacer en esta sesión. No empezar a codear hasta confirmar.

### Protocolo de arranque para sesiones de código

```
PASO 1 — Leer este documento completo.
PASO 2 — Listar el zip correcto (v3 o v4) con unzip -l para verificar qué archivos hay.
PASO 3 — Revisar Sección 0.5: estado real de cada componente.
PASO 4 — Revisar Sección 13: qué pasos de v4 están hechos y qué falta.
PASO 5 — Preguntar al usuario: "¿Qué querés hacer hoy?"
PASO 6 — Sólo después de confirmar: leer el archivo fuente específico del zip antes de modificarlo.
PASO 7 — Entregar archivos individuales + zip final con BOM validado.
PASO 8 — Nunca entregar código sin haber verificado la Sección 6 para la sintaxis usada.
```

**Regla de oro:** Si no estás seguro de si algo existe en IR 2.0.4, buscarlo en `game.zip` o preguntar. No inventar sintaxis.

---

## 0.3 MAPA DEL DOCUMENTO

| Necesito saber... | Ir a sección |
|---|---|
| Estado actual del proyecto — qué está hecho, qué falta, bugs pendientes | **0.5** |
| Glosario — términos del proyecto | **0.6** |
| Historia del proyecto, evolución v1→v4 | 1 |
| Qué está hecho y qué falta en v4 | 2 |
| Nomenclatura del engine (province vs territory, etc.) | 3.1 |
| Estructura de archivos, BOM requerido | 3.2 |
| Tabla de funciones y estados | 3.3 |
| Tabla de costos completa de todo el ecosistema | 3.4 |
| Tabla de unidades marcadoras v3 y v4 | 3.5 |
| Variables de estado v3 y v4 | 3.6 |
| Panel de decisiones — qué aparece cuándo | 3.7 |
| Flujo completo de cada operación (Gather, Distribute, Optimize, Transfer) | 4 |
| Flujo completo de BOM, IHA, TLV, TGL, Heredero del Rival | 5 |
| Gotchas del engine + severidad + FAQ de patrones frecuentes | **6** |
| Guía de diagnóstico — error.log | 7 |
| Código fuente completo v1 (Estable v1.3.5) | 8-A |
| Código fuente completo v2 (ALT v1.3) | 8-B |
| Código fuente completo v3 (todos los archivos) | 8 |
| **Código fuente real v4 (extraído del zip v4_3)** | **8-C** |
| Diseño v4 — on_action lógica, scripted_guis diseño | 9 |
| Diseño v4 — localización ES y EN (reescrita) | 10 |
| Diseño v4 — cancel_all exhaustivo (código completo) | 11 |
| Optimizador provincial — referencia de parámetros | 12 |
| Orden de pasos para codear v4 | 13 |
| Historial completo + resumen ejecutivo por versión | **14** |
| Información pendiente de encontrar | 15 |
| Exodos: Repartir Esclavos (Slave Distributor) | 16 |
| Tabla económica — valores de pop, equivalencias, justificación de costos | 17 |
| Decisiones de diseño descartadas | 18 |
| Log de decisiones por sesión — qué se decidió, qué quedó abierto, premisas activas | **19** |
| Protocolo de actualización del superbackup — cuándo versionar, qué secciones tocar | **20** |
| Tabla de equivalencia de zips — nombre → versión → estado → diferencia clave | **21** |

---

## 0.4 ERRORES FRECUENTES DE IA — LEER CON ATENCIÓN ANTES DE ESCRIBIR CÓDIGO

Estos son errores documentados de sesiones anteriores. Están aquí para no repetirlos.

### ERROR 1 — Confundir v3 con v4
IRAM v3 (`mod_pack_IRAM_15.zip`) y v4 (`mod_pack_IRAM_v4_0.zip`) son versiones distintas con arquitecturas distintas. No mezclar código de una en la otra. v4 usa decisions + on_action puro, sin scripted_gui, sin unidades marcadoras para Gather Global. Ver tabla completa de diferencias en Sección 0.4b.

### ERROR 2 — Usar variables de unidad legacy (SOLO APLICA A OPERACIONES CON MARCADOR — v4 legacy)
*(Movido a Sección 18.4 para preservación histórica — aplica únicamente a la rama experimental con scripted_gui)*
En v4 estable las operaciones Gather, Distribute, Optimize, Transfer siguen usando las variables legacy de unidad de v3. Gather Global no usa unidades marcadoras en absoluto.

### ERROR 3 — Agregar activates o pendings (SOLO APLICA A LA RAMA scripted_gui DESCARTADA)
*(Movido a Sección 18.4 — no aplica a la arquitectura activa de v4)*
En v4 estable las decisiones confirm son siempre visibles. No existen activates. No existen pendings.

### ERROR 4 — Agregar `is_moving` en allows
En v4 no existen chequeos `is_moving` en ningún `allow`. Gather Global no usa unidades marcadoras.
En Exodos legacy (Gather/Distribute/Optimize/Transfer por área), las unidades marcadoras de v3 están vigentes tal cual — sin cambios de `movement_speed`.
*(La variante con `movement_speed = 0` corresponde a la rama scripted_gui descartada — ver Sección 18.4)*

### ERROR 5 — Agregar el rival en operaciones Exodos
El rival fue eliminado de Concentrate, Distribute, Optimize y Transfer en v4.
Solo existe en Heredero del Rival y BOM/IHA. No agregar condición de rival a Exodos.

### ERROR 6 — Asumir que la localización v4 está cerrada
La localización fue **reescrita completamente para v4**. Los textos de v3 describen el flujo
de activates y posicionamiento manual — flujo que no existe en v4. Ver Sección 10.

### ERROR 7 — Confundir el rol de `exodos_confirm_optimize`
`exodos_confirm_optimize` **no cobra costos**. Su único rol es abrir el submenu de 17 rangos
seteando `exodos_optimize_active`. El costo (2000 oro / 5000 manpower / +10 tyranny) se cobra
en la decisión de rango que el jugador elige — esa es la última decisión y la que desata la función.

### ERROR 8 — Duplicar chequeos en on_action
El chequeo de ancla destruida es **un solo bloque**, sin distinción por operación activa.
Ver Sección 9.2 para el patrón correcto.

### ERROR 9 — Usar `count = var:X` en while
`while { count = var:exodos_optimize_count }` devuelve `Value of wrong type: 'none'` en IR 2.0.4.
El while no itera. Distribute usa 17 bloques `else_if` con `count` literal. Sin excepción.

### ERROR 10 — cancel_all incompleto
`exodos_cancel_all` limpia absolutamente todo — incluyendo variables legacy de v3 y anteriores.
El jugador puede migrar desde cualquier versión. Ver Sección 11 para la lista exhaustiva.

### ERROR 11 — Preguntar cosas ya respondidas en este documento
Si está documentado aquí, está resuelto. No preguntar. Buscar en el mapa de secciones.

### ERROR 12 — Omitir guards cruzados en allows de confirms
Los allows de `exodos_confirm_gather`, `exodos_confirm_distribute`, `exodos_confirm_transfer`
y `exodos_confirm_optimize` deben incluir AMBOS guards:
```pdxscript
NOT = { has_variable = exodos_operation_active }
NOT = { has_variable = exodos_optimize_active }
```
Sin estos guards, una operación puede iniciarse mientras `exodos_optimize_active` está flotando
(o viceversa), corrompiendo el estado. Ver Sección 9.1 para el patrón correcto de cada confirm.
**Historial:** BUGs 1–3 corregidos en v4_1 para gather/distribute/transfer. BUG de `confirm_optimize`
(faltaba el segundo guard `NOT = exodos_optimize_active`) corregido en v4_2. ✓ CERRADO en v4_2.

### ERROR 13 — Keys `_desc` de decisiones: no usar un key genérico compartido
El engine de IR resuelve la descripción de cada decisión buscando exactamente `<decision_id>_desc`.
Un key genérico como `exodos_opt_range_desc` (sin número) **nunca aparece en pantalla** — ninguna
decisión se llama `exodos_opt_range`, entonces el engine no lo resuelve.

Patrón correcto para los 17 rangos de Optimize:
```yaml
 exodos_opt_range_03_desc:0 "Texto..."
 exodos_opt_range_04_desc:0 "Texto..."
 # ... uno por cada decisión, con el número exacto
 exodos_opt_range_19_desc:0 "Texto..."
```
Aplica a cualquier grupo de decisiones con nombre numerado. ✓ CORREGIDO en v4_2 (ambos yml).

### ERROR 17 — `set_province_flag`, `set_unit_flag`, `remove_province_flag` no existen en IR 2.0.4
El engine usa `set_variable` / `remove_variable` / `has_variable` para **todo**, incluyendo
flags de province y de unidad. `has_province_flag`, `set_province_flag`, `remove_province_flag`,
`set_unit_flag` y `has_unit_flag` no existen — el engine los ignora silenciosamente o genera error.
El scope determina a qué objeto pertenece la variable: desde scope province → variable de province;
desde scope unit → variable de unit. No hay comandos separados por tipo.
**Historial:** Exodus bug 4, confirmado al migrar de flags a variables en versión temprana.

### ERROR 18 — `var:X >= var:Y` es ilegal cuando ambos lados son variables
La comparación entre dos variables en un trigger no usa `var:` en ambos lados.
- ❌ `var:exodos_pulse_counter >= var:exodos_limit` — sintaxis inválida
- ✓ `exodos_pulse_counter >= 0` — nombre directo, valor literal
`var:` solo se usa para asignar el valor de una variable a otra, no para comparar dos entre sí.
**Historial:** Exodus bug 3.

### ERROR 19 — `ruler = {}` falla en scope `country` en IR 2.0.4
En `country_decisions`, el scope de entrada de `potential`, `allow` y `effect` es `country`.
El trigger `ruler = { condición }` lanza `Wrong scope for trigger: country, expected character`.
El effect `ruler = { efecto }` lanza `Wrong scope for effect: country, expected character`.
**Fixes confirmados:**
```pdxscript
# En potential/allow:
any_character = { is_ruler = yes  condición }
# En effect:
every_character = { limit = { is_ruler = yes }  efecto }
```
**Historial:** BOM v2.5, TLV v1.3 — 1454 hits en error.log.

### ERROR 20 — `every_owned_province` desde scope `pop` no itera provincias
Desde scope `pop`, llamar `every_owned_province` falla silenciosamente — el iterador espera scope
`country`. El engine no lanza error; simplemente no itera. El patrón correcto es hacer
`save_scope_as` de la province destino **antes** de entrar al scope pop, y referenciarla con
`scope:nombre` dentro del bloque de movimiento.
**Historial:** Gather temprano (Diseñador 1 Sesión 3).

### ERROR 21 — `change_variable` explota si la variable nunca fue seteada
Si se llama `change_variable = { name = X add = -1 }` sobre una variable que no existe
(nunca se ejecutó `set_variable` para ella), el engine lanza:
`Variable not of the 'value' scope type. Type: empty`
La variable debe inicializarse con `set_variable` explícitamente antes de que el pulso
intente modificarla. No asumir que existe porque fue definida en otra sesión o save anterior.
**Historial:** `exodus_operation_counter` — eliminado en favor de condición de población.

### ERROR 22 — `namespace` obligatorio al inicio del archivo de eventos
Sin la línea `namespace = X` como primera declaración del archivo de eventos, el engine lanza:
`'namespace.1' does not have a valid namespace`
Los eventos no se registran en absoluto — el mod carga sin errores pero los eventos no existen.
No confundir con un error de sintaxis interno: el archivo puede estar perfectamente formado
y aun así fallar si falta el namespace.
**Historial:** Diseñador 1 Sesión 2, Agente 5 Sesión 1.

### ERROR 23 — `dlc_load.json` debe incluir el mod explícitamente
Si `dlc_load.json` no lista el mod, el juego no lo carga aunque esté correctamente instalado
y aparezca activo en Irony. Síntoma: mod activo en el launcher, sin errores de estructura,
cero efectos ingame, error.log sin ninguna referencia al mod.
El archivo debe estar en `Documents/Paradox Interactive/Imperator/` y listar todas las entradas
`mod/nombre.mod` del ecosistema.
**Historial:** Agente 2, múltiples sesiones.

### ERROR 24 — Carpeta interna del mod no puede renombrarse entre versiones
Si la carpeta interna cambia de nombre (ej: `conspiracion` → `conspiracion_v2`), el juego
falla en cargar el mod aunque el `.mod` externo sea correcto. La carpeta siempre debe
mantener el mismo nombre interno independientemente de la versión del mod.
Solo el `descriptor.mod` y el `.mod` externo llevan el número de versión.
**Historial:** Agente 2 Sesión 20.

### ERROR 25 — `add_health = -100` desde scope `commander` de unidad no funciona
`commander` en IR 2.0.4 es un scope de **solo lectura** para efectos de muerte y salud.
`death = { }` desde scope `commander` también falla silenciosamente.
**Fix confirmado:** iterar desde country scope:
```pdxscript
every_character = {
    limit = { is_ruler = yes }
    add_health = -100
}
```
O para matar al commander de una unidad específica: capturar al personaje con
`save_scope_as` antes del loop y aplicar `add_health = -100` sobre ese scope.
**Historial:** BOM Kill Ruler, Diseñador 1 Sesión 6.

### ERROR 14 — R1 tiene una excepción documentada: `exodos_cancel_all`
`exodos_cancel_all`, que usa `allow = { always = yes }` por diseño — debe poder ejecutarse en
cualquier estado de corrupción, incluso si el guard de `potential` falla. **No agregar `is_ai = no`
en el `allow` de `cancel_all`.** El `potential` sí lo tiene.

### ERROR 15 — `exodos_spawn_anchor_button`: guard faltante en `is_valid` (RAMA scripted_gui DESCARTADA)
*(Este error y su corrección corresponden a la arquitectura experimental descartada — ver Sección 18.4. No aplica al zip v4.0 activo.)*
El botón A de la scripted_gui requería `NOT = exodos_optimize_active` en `is_valid`. Corregido en v4_3 de la rama experimental.

### ERROR 16 — `exodos_spawn_destination_button`: guard faltante en `is_valid` (RAMA scripted_gui DESCARTADA)
*(Este error y su corrección corresponden a la arquitectura experimental descartada — ver Sección 18.4. No aplica al zip v4.0 activo.)*
El botón B de la scripted_gui requería `NOT = exodos_operation_active` en `is_valid`. Corregido en v4_3 de la rama experimental.

**Corrección aplicada en v4_3 — `exodos_spawn_destination_button.is_valid`:**
```pdxscript
is_valid = {
    scope:player = {
        NOT = { has_variable = exodos_operation_active }   # ← AGREGAR
        NOT = { any_unit = { has_variable = exodos_unit_destination } }
    }
}
```

---

### ERROR 26 — Asumir que el zip activo no tiene bugs pendientes
El zip `mod_pack_IRAM_v4_3.zip` tiene dos bugs conocidos documentados en Sección 21.
Antes de trabajar en cualquier archivo de localización de Optimize, verificar Sección 21
para conocer el estado exacto del zip. No asumir que el zip está limpio.
Bugs pendientes en v4_3: crossover rango 11 en ambos yml (dice "163–176", debe ser "163–177")
y comentario en `exodos_decisions_optimize.txt` (dice `11→12:176/177`, debe ser `177/178`).

### ERROR 27 — `save_scope_as` dentro de `random_holdings` no persiste fuera del bloque
El scope guardado con `save_scope_as` dentro de un bloque `random_holdings` no existe fuera
de ese bloque. El engine no lanza error — simplemente no encuentra el scope y el efecto no corre.
Patrón correcto:
```pdxscript
while = {
    limit = { num_holdings_owned > 0 }
    random_holdings = { save_scope_as = iha_holding }
    remove_holding = scope:iha_holding   # fuera de random_holdings, dentro del while
}
```
**Historial:** IHA Seize — `remove_holding = scope:iha_holding` estaba fuera del `while`.
Sesión 051. Ver también Sección 6.1.

---

## 0.4b DIFERENCIAS CRÍTICAS ENTRE v3 Y v4

| Concepto | IRAM v3 (`mod_pack_IRAM_15.zip`) | IRAM v4 (`mod_pack_IRAM_v4_0.zip`) |
|---|---|---|
| Rival en Exodos operaciones | Requerido en Gather y Distribute | **Eliminado de todas las operaciones Exodos** |
| Spawn de unidades | Decisiones `exodos_activate_X` en panel | **Eliminados — decisions + on_action puro** |
| Unidades marcadoras (Exodos por área) | 5 unidades, 5 variables distintas | Sin cambios — igual que v3 |
| Gather Global | No existe | **Implementado** — sin unidades marcadoras, decisions puras |
| Distribute | 17 rangos (count 3–19) | **4 rangos simplificados** (count 4/9/14/19) |
| Relics | No existe | **Implementado** — `iram_create_divine_relic` / `iram_remove_divine_relic` |
| `global_migration_speed` en Relic | No existe | ⚠ PENDIENTE v4.1 — token confirmado, código no escrito |
| Visibilidad de confirms | Ocultos hasta tener pending | Sin cambios estructurales — mismo modelo que v3 |
| Cancel particular | `exodos_cancel` por operación | **Eliminado — solo `exodos_cancel_all`** (igual que en v3 final) |
| `exodos_scripted_guis.txt` | No existe | **No existe** en v4 estable (ver Sección 18.4 para la rama experimental) |
| Optimize rangos | 4 rangos (count 4/9/14/19) | 4 rangos — sin cambios |
| Optimize Global | No existe | ⚠ PENDIENTE diseño — Optimize por área + Distribute automático |

> **Nota histórica:** la rama experimental `mod_pack_IRAM_v4_3.zip` implementó una arquitectura alternativa con scripted_gui, 2 unidades inmóviles, y eliminación de activates/pendings. Esa rama fue descartada. Ver Sección 18.4 para el conocimiento de investigación preservado.

---

## 0.4c REGLAS ABSOLUTAS — VIOLAR CUALQUIERA ES UN ERROR QUE INVALIDA EL ARCHIVO

**R1** — `is_ai = no` en `potential` Y en `allow` de toda decisión. En ambos bloques. Siempre.

**R2** — No existen activates en v4. Sin excepción. *(La variante scripted_gui con botones A/B fue descartada — ver Sección 18.4)*

**R3** — No existen pendings en v4. Sin excepción.

**R4** — No existe `exodos_cancel`. Solo `exodos_cancel_all`. Sin excepción.

**R5** — No existen chequeos `is_moving` en ningún `allow`. Sin excepción.

**R6** — El rival no existe en Concentrate, Distribute, Optimize ni Transfer. Sin excepción.

**R7** — `ai_will_do = { factor = 0 }` en toda decisión. Sin excepción.

**R8** — El costo NO se escribe en localización. El engine lo muestra automáticamente desde el `effect`.

**R9** — BOM UTF-8 (`EF BB BF`) en todos los `.txt` y `.yml`. Sin BOM en `.mod` y `descriptor.mod`.
⚠ Verificar que el BOM sea bytes reales `EF BB BF`, no texto literal `\xef\xbb\xbf`. Si el archivo se abre y guarda con un editor que no maneja bien UTF-8-sig, puede escribir el BOM como texto visible — esto genera `Corrupt Decision Table Entry` en el log. Bug no de diseño, de tooling.

**R10** — El ecosistema habilita, no castiga. No agregar restricciones artificiales.

**R11** — Las secciones marcadas CERRADO no se reabren salvo pedido explícito del usuario.

**R12** — `destroy_unit` siempre dentro de `limit`. `destroy_unit` en unidad inexistente genera error en log.

**R13** — `count = var:X` en `while` no funciona en IR 2.0.4. Usar count literal hardcodeado. Sin excepción.

**R14** — Los chequeos de error en on_action son bloques únicos (no duplicar por operación). En Exodos por área: un bloque de chequeo de unidad destruida. En Gather Global: un bloque de cleanup de área sin procesadas. Ver Sección 9.2 y Sección del backup v3 para los patrones correctos.

---

## 0.4d FLUJO DE TRABAJO

1. El usuario sube al inicio de la sesión: este documento + `mod_pack_IRAM_12.zip`.
2. La IA ejecuta el checklist del 0.2 antes de responder.
3. La IA trabaja siguiendo el orden de pasos de la Sección 13.
4. La IA entrega el zip final con BOM validado y listo para instalar.
5. Instalación: extraer en `C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\`
6. **Primer paso obligatorio al cargar la partida: ejecutar "Cancelar todo".**

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0.5 — ESTADO ACTUAL DEL PROYECTO
# ══════════════════════════════════════════════════════════

**Última actualización:** 2026-05-21 (v2.1)

## 0.5.0 DASHBOARD — ESTADO DE UN VISTAZO

| Dimensión | Estado |
|---|---|
| Zip activo | `mod_pack_IRAM_v4_0.zip` |
| Versión | IRAM v4.0 |
| Hito de cierre v4 | Optimize Global + Reliquia migración implementados |
| Bloqueadores activos | Ver Sección 19.0 |
| Bugs conocidos en zip activo | Ninguno documentado en v4.0 |
| Última sesión | 2026-05-21 |

**Semáforo rápido:**
- 🟡 Optimize Global — diseño en curso (ver Sección 19.0 y entrada 2026-05-21)
- 🟡 Reliquia migración (`global_migration_speed = 2.5`) — pendiente de implementar en v4.1 (token cerrado, código no escrito — ver backup v3 Sección 5.5)
- 🟡 Heredero del Rival — condición `has_spouse` pendiente de confirmar token (ver Sección 2.2)
- 🟢 Gather Global con capital exclusion — implementado v4.0
- 🟢 Relics tokens — corregidos en v4.0 (`treasury`, `add_treasury`)
- 🟢 BOM-como-texto — corregido en v4.0 (ambos archivos afectados)

*Actualizar este dashboard al inicio de cada sesión que cambie el estado del proyecto.*

## Estado por componente

| Componente | Estado | Zip canónico | Pendiente |
|---|---|---|---|
| **Exodos v3** | ✅ CERRADO | `mod_pack_IRAM_15.zip` | — |
| **Exodos v4 (por área)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_0.zip` | Condición `has_spouse` en Heredero del Rival (token pendiente) |
| **Gather Global** | ✅ IMPLEMENTADO v4.0 | `mod_pack_IRAM_v4_0.zip` | ⚠ TESTEAR en partida — ver backup v3 Sección 3.7 |
| **Distribute simplificado** | ✅ IMPLEMENTADO v4.0 | `mod_pack_IRAM_v4_0.zip` | — |
| **Relics** | ✅ IMPLEMENTADO v4.0 (tokens corregidos) | `mod_pack_IRAM_v4_0.zip` | `global_migration_speed = 2.5` pendiente v4.1 |
| **BOM / IHA** | ✅ CERRADO | ambos zips | — |
| **TLV** | ✅ CERRADO | ambos zips | — |
| **TGL** | ✅ CERRADO | ambos zips | — |
| **Heredero del Rival** | ✅ IMPLEMENTADO (igual que v3) | `mod_pack_IRAM_v4_0.zip` | Condición `has_spouse` — ver Sección 2.2 |
| **Optimize Global** | 🔧 DISEÑO EN CURSO | — | Dos variantes: Población + Económico — ver entrada 2026-05-21 |
| **Reliquia migración** | 🔧 TOKEN CERRADO, código pendiente | — | `global_migration_speed = 2.5` — ver backup v3 Sección 5.5 |

## Bugs conocidos pendientes en el zip v4.0

Ninguno documentado al momento de esta actualización.

## Próximos pasos

1. Diseñar e implementar Optimize Global (dos variantes: Población y Económico)
2. Implementar `global_migration_speed = 2.5` en Relic (v4.1) — proceder directo al código
3. Confirmar token para condición `has_spouse` en Heredero del Rival y agregar condición al allow

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0.6 — GLOSARIO DEL PROYECTO
# ══════════════════════════════════════════════════════════

Terminología propia del proyecto. Cuando este documento usa estos términos, se refiere a estas definiciones — no al uso general.

| Término | Definición |
|---|---|
| **Ancla** | Province donde se concentran pops (Gather) o desde donde se distribuyen (Distribute/Optimize). Marcada con `exodos_is_anchor = 1`. En v4, la unidad `exodos_anchor` spawna ahí. |
| **Destino** | Province objetivo de Transfer. Marcada con `exodos_is_destination = 1`. En v4, la unidad `exodos_marker` (Destino) spawna ahí. |
| **Operación activa** | Estado en que `exodos_operation_active` está seteado. Solo una operación puede estar activa a la vez. |
| **Pulso** | Ejecución del `monthly_country_pulse` — ocurre una vez por mes. Cada operación avanza un paso por pulso. |
| **Cleanup** | Ejecución de `exodos_cleanup_effect` — limpia todas las variables y destruye todas las unidades. Se llama al finalizar o cancelar cualquier operación. |
| **Piso de fuentes** | Condición mínima de población en cada province fuente para que el `while` siga iterando. En Gather: `total_population >= 2`. En Distribute ancla: `total_population >= 30`. |
| **Count** | Número de pops que se mueven por province por pulso en cada iteración del `while`. Literal hardcodeado — no puede ser variable. |
| **Legacy** | Variables o unidades de versiones anteriores (v1, v2, v3) que el cleanup de v4 también limpia para compatibilidad. |
| **Territory** | Forma humana de decir "province" — en el engine siempre es `province` (scope). |
| **Área** | `area` en el engine — una agrupación de provinces. Equivalent a "provincia" geográfica. |
| **Región** | `region` en el engine — agrupación de áreas. |
| **Marcador** | Unidad invisible (`build_cost = 0`, `movement_speed = 0`) usada para que el jugador señale un territorio. En v3 hay un solo tipo (`exodos_marker`). En v4 hay dos (`exodos_anchor` y `exodos_marker`). |
| **Panel de tácticas** | `scripted_gui` del engine que aparece al hacer click en una province con el panel de tácticas abierto. En v4 contiene los botones A (Ancla) y B (Destino). |
| **BOM** | "By Other Means" — módulo de eliminación/gestión de rivales y gobernante. |
| **IHA** | "Iron Hand Ascendant" — módulo de confiscación y transferencia de propiedades. |
| **TLV** | "The Last Vote" — módulo de disolución de la república. |
| **TGL** | "The Great Leap" — módulo de compra instantánea del árbol de innovations. |
| **One-shot** | Decisión que solo puede usarse una vez por partida, bloqueada por una variable tras el primer uso (ej: `tgl_purchased`, `bom_ego_sum_mars_used`). |
| **Stateless** | Módulo sin variables de estado persistentes entre sesiones de juego. BOM, IHA, TLV, TGL y Heredero del Rival son stateless. |
| **Guard** | Condición en `is_valid` o `allow` que bloquea una acción en estados inválidos. Ej: `NOT = { has_variable = exodos_operation_active }`. |
| **Crossover** | Punto de corte entre dos rangos de Optimize (ej: el crossover 11/12 está en 177/178 — 177 pops va a rango 11, 178 pops va a rango 12). |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 1 — HISTORIA DEL PROYECTO
# ══════════════════════════════════════════════════════════

## 1.1 Cronología de versiones

| Versión | Nombre histórico | Zip | Estado | Característica principal |
|---|---|---|---|---|
| IRAM v1 | Drago Mod Pack Estable v1.3.5 | `mod.zip` | Histórico | Spawn en capital, rival requerido, `war = no` obligatorio |
| IRAM v2 | Drago Mod Pack ALT v1.3 | `mod_alt.zip` | Histórico | Spawn en posición del rival, `war = no` eliminado |
| IRAM v3 | IRAM v1.21 ALT / mod_pack_IRAM_15 | `mod_pack_IRAM_15.zip` | **✅ CERRADO** | Unificado en `exodos/`, Heredero del Rival v1.6, herencia matrilineal |
| IRAM v4 | IRAM v4.0 | `mod_pack_IRAM_v4_0.zip` | **🔧 EN DESARROLLO** | Decisions + on_action puro, sin rival en Exodos, Gather Global, Distribute 4 rangos, Relics |

## 1.2 Evolución de las funciones por versión

| Función | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Gather (por área) | ✓ spawn en capital, rival req. | ✓ spawn en rival, sin war | ✓ igual que v2 | ✓ igual que v3, sin rival |
| Distribute (por área) | ✓ spawn en capital, rival req. | ✓ spawn en rival, sin war | ✓ igual que v2 | ✓ 4 rangos simplificados, sin rival |
| Transfer | ✓ spawn en capital, war req. | ✓ spawn en capital, sin war | ✓ igual que v2 | ✓ sin cambios |
| Optimize (por área) | ✗ | ✗ | ✓ 4 rangos (count 4/9/14/19), rival req. | ✓ 4 rangos, sin rival |
| Gather Global | ✗ | ✗ | ✗ | ✓ decisions puras, capital exclusion, 10 áreas/pulso |
| Optimize Global | ✗ | ✗ | ✗ | 🔧 diseño en curso |
| Relics (Un Pueblo, Una Fe) | ✗ | ✗ | ✗ | ✓ implementado — migración pendiente v4.1 |
| BOM Eliminar Rivales | ✓ | ✓ | ✓ | ✓ sin cambios |
| BOM Bacanal | ✓ | ✓ | ✓ | ✓ sin cambios |
| BOM Kill Ruler | ✓ en TLV | ✓ en BOM | ✓ en BOM | ✓ sin cambios |
| IHA Confiscar / Fill the Void | ✗ | ✗ | ✓ | ✓ sin cambios |
| BOM Ego Sum | ✓ | ✓ | ✓ | ✓ sin cambios |
| The Last Vote | ✓ | ✓ | ✓ | ✓ sin cambios |
| The Great Leap | ✓ | ✓ | ✓ | ✓ sin cambios |
| Heredero del Rival | ✗ | ✗ | ✓ v1.6 matrilineal | ✓ sin cambios — condición spouse pendiente |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 2 — ESTADO ACTUAL
# ══════════════════════════════════════════════════════════

## 2.1 Estado de IRAM v4

| Item | Estado |
|---|---|
| Versión activa | v4.0 — `mod_pack_IRAM_v4_0.zip` |
| Base de código | IRAM v3 (`mod_pack_IRAM_15.zip`) + Gather Global v1.2 |
| Diseño global | CERRADO (arquitectura decisions + on_action puro) |
| `exodos_scripted_effects.txt` | ✅ SIN CAMBIOS vs v3 |
| `exodos_units.txt` | ✅ SIN CAMBIOS vs v3 |
| `exodos_decisions_gather_distribute.txt` | ✅ IMPLEMENTADO — sin rival |
| `exodos_decisions_transfer.txt` | ✅ IMPLEMENTADO — sin rival |
| `exodos_decisions_optimize.txt` | ✅ IMPLEMENTADO — 4 rangos simplificados, sin rival |
| `exodos_on_action.txt` | ✅ IMPLEMENTADO — Gather Global + capital exclusion |
| `exodos_decisions_relics.txt` | ✅ IMPLEMENTADO — tokens corregidos |
| `common/modifiers/iram_relic_modifiers.txt` | ✅ IMPLEMENTADO (sin `global_migration_speed` aún) |
| Localización Relics ES y EN | ✅ IMPLEMENTADA |
| `exodos_decisions_cancel.txt` | ✅ IMPLEMENTADO — cleanup exhaustivo incluyendo Global |
| BOM, IHA, TLV, TGL, Heredero del Rival | ✅ SIN CAMBIOS vs v3 |
| Optimize Global | 🔧 DISEÑO EN CURSO — ver entrada sesión 2026-05-21 |
| `global_migration_speed = 2.5` en Relic | 🔧 PENDIENTE v4.1 — token y valor cerrados, código no escrito |

## 2.2 Fixes y pendientes en v4

| Item | Descripción | Estado |
|---|---|---|
| Chequeo ancla destruida en on_action | Bloque único de chequeo de error | ✅ IMPLEMENTADO en v4.0 |
| Guards cruzados en `allow` de confirms | `NOT = exodos_operation_active` en todos los confirms | ✅ IMPLEMENTADO en v4.0 |
| Rival eliminado de Exodos | Sin condición de rival en Gather/Distribute/Optimize/Transfer | ✅ IMPLEMENTADO en v4.0 |
| Relics tokens | `gold` → `treasury`, `add_gold` → `add_treasury`, `picture` eliminado | ✅ CORREGIDO en v4.0 |
| BOM-como-texto | BOM literal `\xef\xbb\xbf` en `exodos_on_action.txt` y `exodos_decisions_optimize.txt` | ✅ CORREGIDO en v4.0 |
| Gather Global capital exclusion | `NOT = { is_capital = yes }` en los 21 bloques de on_action | ✅ IMPLEMENTADO en v4.0 |
| `tlv_confirm` — `current_ruler` | `current_ruler` desde country scope en trigger puede no resolver | ⚠ TESTEAR |
| `family` del rival en Heredero del Rival | `family = scope:exodos_rival.family` puede fallar si el rival no tiene familia | ✅ Comportamiento aceptado — el hijo spawna sin familia si no existe (no es bug) |
| Condición `has_spouse` en Heredero del Rival | La decisión no debería aparecer si el rival no tiene esposa/esposo | ⚠ PENDIENTE — token correcto sin confirmar; no codear hasta validar |
| `global_migration_speed = 2.5` en Relic | Token confirmado en game.zip, valor definido, código no escrito | 🔧 PENDIENTE v4.1 |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 3 — ARQUITECTURA DEL ECOSISTEMA
# ══════════════════════════════════════════════════════════

## 3.1 Terminología engine vs diseño

| Diseño | Engine (pdxscript) |
|---|---|
| "territory" / "location" | `province` (scope) |
| "provincia geográfica" | `area` (scope) |
| "región" | `region` (scope) |
| "gobernante" en effect | `every_character = { limit = { is_ruler = yes } ... }` |
| "gobernante" en trigger | `any_character = { is_ruler = yes ... }` |
| "rivales del gobernante" | `every_character = { limit = { is_ruler = yes } every_rival = { } }` |

## 3.2 Estructura de archivos — IRAM v4

```
mod/
├── build_mods.py                                            ← script generación zip con BOM
├── exodos.mod                                               ← sin BOM
├── by_other_means.mod                                       ← sin BOM (TEST SHELL)
├── the_last_vote.mod                                        ← sin BOM (TEST SHELL)
├── the_great_leap.mod                                       ← sin BOM (TEST SHELL)
│
├── exodos/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/
│   │   ├── exodos_decisions_gather_distribute.txt           ← BOM UTF-8
│   │   ├── exodos_decisions_transfer.txt                    ← BOM UTF-8
│   │   ├── exodos_decisions_optimize.txt                    ← BOM UTF-8
│   │   ├── exodos_decisions_rival_heir.txt                  ← BOM UTF-8 (sin cambios)
│   │   ├── exodos_decisions_cancel.txt                      ← BOM UTF-8
│   │   ├── exodos_decisions_relics.txt                      ← BOM UTF-8 (NUEVO v4)
│   │   ├── exodos_decisions_bom.txt                         ← BOM UTF-8 (sin cambios)
│   │   ├── exodos_decisions_bom_ego_sum.txt                 ← BOM UTF-8 (sin cambios)
│   │   ├── exodos_decisions_tgl.txt                         ← BOM UTF-8 (sin cambios)
│   │   └── exodos_decisions_tlv.txt                         ← BOM UTF-8 (sin cambios)
│   ├── events/
│   │   ├── exodos_events.txt                                ← BOM UTF-8 (sin cambios)
│   │   └── tlv_events.txt                                   ← BOM UTF-8 (sin cambios)
│   ├── common/
│   │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8
│   │   ├── units/exodos_units.txt                           ← BOM UTF-8 (sin cambios)
│   │   ├── modifiers/iram_relic_modifiers.txt               ← BOM UTF-8 (NUEVO v4)
│   │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8 (sin cambios)
│   └── localization/
│       ├── english/
│       │   ├── exodos_l_english.yml                         ← BOM UTF-8
│       │   ├── relics_l_english.yml                         ← BOM UTF-8 (NUEVO v4)
│       │   ├── bom_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       │   ├── bom_l_english_ego_sum.yml                    ← BOM UTF-8 (sin cambios)
│       │   ├── tlv_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       │   └── tgl_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       └── spanish/
│           ├── exodos_l_spanish.yml                         ← BOM UTF-8
│           ├── relics_l_spanish.yml                         ← BOM UTF-8 (NUEVO v4)
│           ├── bom_l_spanish.yml                            ← BOM UTF-8 (sin cambios)
│           ├── bom_l_spanish_ego_sum.yml                    ← BOM UTF-8 (sin cambios)
│           ├── tlv_l_spanish.yml                            ← BOM UTF-8 (sin cambios)
│           └── tgl_l_spanish.yml                            ← BOM UTF-8 (sin cambios)
│
├── by_other_means/ └── descriptor.mod                       ← sin BOM (TEST SHELL)
├── the_last_vote/  └── descriptor.mod                       ← sin BOM (TEST SHELL)
└── the_great_leap/ └── descriptor.mod                       ← sin BOM (TEST SHELL)

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

## 3.3 Tabla de funciones

| Función | Prefijo | Archivo | v4 |
|---|---|---|---|
| Exodos: Concentrate (Gather por área) | `exodos_` | exodos_decisions_gather_distribute.txt | MODIFICADO — sin rival |
| Exodos: Distribute (por área, 4 rangos) | `exodos_` | exodos_decisions_gather_distribute.txt | MODIFICADO — 4 rangos, sin rival |
| Exodos: Transfer | `exodos_` | exodos_decisions_transfer.txt | MODIFICADO — sin rival |
| Exodos: Optimize (por área, 4 rangos) | `exodos_` | exodos_decisions_optimize.txt | MODIFICADO — 4 rangos, sin rival |
| Exodos: Gather Global | `exodos_` | exodos_on_action.txt + exodos_decisions_gather_distribute.txt | NUEVO |
| Exodos: Optimize Global | `exodos_` | TBD | PENDIENTE DISEÑO |
| Relics: Un Pueblo, Una Fe | `iram_` | exodos_decisions_relics.txt + iram_relic_modifiers.txt | NUEVO |
| Heredero del Rival | `exodos_` | exodos_decisions_rival_heir.txt | SIN CAMBIOS |
| Cancel All | `exodos_` | exodos_decisions_cancel.txt | MODIFICADO — limpia vars Global y Relic |
| By Other Means (BOM + IHA) | `bom_` / `iha_` | exodos_decisions_bom.txt | SIN CAMBIOS |
| Ego Sum | `bom_` | exodos_decisions_bom_ego_sum.txt | SIN CAMBIOS |
| The Great Leap | `tgl_` | exodos_decisions_tgl.txt | SIN CAMBIOS |
| The Last Vote | `tlv_` | exodos_decisions_tlv.txt | SIN CAMBIOS |

## 3.4 Tabla de costos y condiciones — ecosistema completo v4

| Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | Condiciones extra |
|---|---|---|---|---|---|---|
| Exodos: Concentración (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Distribución (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Optimizar (confirm → sin costo) | — | — | — | — | — | ancla existente, área 100% propia |
| Exodos: Opt. Rango (decisión final) | 2000 | 10 | 5000 | +10 | ≤90 | exodos_optimize_active seteado |
| Exodos: Transferencia | 2000 | 10 | 5000 | +20 | ≤80 | ancla + destino existentes, owner=ROOT |
| Exodos: Gather Global | — | — | — | +100 tyranny | — | -100 popularidad gobernante, sin op. activa |
| Exodos: Optimize Global | TBD | TBD | TBD | TBD | TBD | PENDIENTE DISEÑO |
| Heredero — Hijo del Rival | — | — | — | — | — | 1 rival exacto, ≥16, is_male, employer=ROOT |
| Heredero — Hija del Rival | — | — | — | — | — | 1 rival exacto, ≥16, is_male, employer=ROOT |
| Relics: Crear (Un Pueblo, Una Fe) | 5000 | — | — | — | — | NOT has_country_modifier = iram_divine_relic |
| Relics: Disolver | — | — | — | — | — | has_country_modifier = iram_divine_relic |
| BOM: Eliminar Rivales | 2000 | 1 | 500 | +40 | ≤80 | rivals ≥ 1 |
| BOM: Bacanal | 500 | — | — | +10 | ≤90 | rivals ≥ 1 |
| BOM: Et tu Brute? | 2000 | 1 | 500 | +40 | ≤60 | stability ≥ 50 |
| IHA: Confiscar Propiedades | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| IHA: Fill the Void | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| TLV: Confirm | 2000 | — | — | +40 | ≤60 | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL: Purchase | dinámico | — | — | +100 | ≤0 | one-shot |

> Manpower: valor en script = valor pantalla / 500. El engine multiplica ×500 al mostrar.

## 3.5 Unidades marcadoras

### v3 y v4 Exodos por área (sin cambios)
| sub_unit | Nombre ES | Variable | movement_speed |
|---|---|---|---|
| `exodos_marker` | "Exodos - Concentrar" | `exodos_unit_concentrate` | 5 |
| `exodos_marker` | "Exodos - Distribuir" | `exodos_unit_distribute` | 5 |
| `exodos_marker` | "Exodos - Optimizar" | `exodos_unit_optimize` | 5 |
| `exodos_marker` | "Exodos - Origen" | `exodos_unit_transfer_origin` | 5 |
| `exodos_marker` | "Exodos - Destino" | `exodos_unit_transfer_dest` | 5 |

### v4 Gather Global
Sin unidades marcadoras. El Gather Global opera por decisions + on_action puro — no usa ni spawna unidades.

> **Nota histórica:** la rama experimental `mod_pack_IRAM_v4_3.zip` introdujo `exodos_anchor` (sub_unit nueva, `movement_speed = 0`) y redujo las marcadoras a 2 unidades. Esa arquitectura fue descartada. Ver Sección 18.4.

## 3.6 Variables de estado

### Variables de país

| Variable | v3 | v4 | Uso |
|---|---|---|---|
| `exodos_operation_active` | ✓ | ✓ | Guard global — bloquea nueva operación |
| `exodos_gather_active` | ✓ | ✓ | Gather en ejecución |
| `exodos_distribute_active` | ✓ | ✓ | Distribute en ejecución |
| `exodos_transfer_active` | ✓ | ✓ | Transfer en ejecución |
| `exodos_optimize_active` | ✓ | ✓ | Optimize en ejecución — abre submenu de rangos |
| `exodos_optimize_gather_done` | ✓ | ✓ | Señal: Gather completado, disparar Distribute |
| `exodos_optimize_count` | ✓ | ✓ | Count por asentamiento (3–19, literal) |
| `exodos_anchor_province` | ✓ | ✓ | Province del ancla, guardada en confirm |
| `exodos_destination_province` | ✓ | ✓ | Province destino Transfer |
| `exodos_pulse_counter` | ✓ | ✓ | Contador Transfer (10 pulsos) |
| `exodos_gather_pending` | ✓ v3 | ✗ eliminada | Legacy — limpiar en cancel_all |
| `exodos_distribute_pending` | ✓ v3 | ✗ eliminada | Legacy — limpiar en cancel_all |
| `exodos_transfer_pending` | ✓ v3 | ✗ eliminada | Legacy — limpiar en cancel_all |
| `exodos_optimize_pending` | ✓ v3 | ✗ eliminada | Legacy — limpiar en cancel_all |
| `tgl_purchased` | ✓ | ✓ | One-shot TGL |
| `bom_ego_sum_mars_used` | ✓ | ✓ | One-shot Ego Sum Mars |
| `bom_ego_sum_iovis_used` | ✓ | ✓ | One-shot Ego Sum Iovis |
| `bom_ego_sum_mercurii_used` | ✓ | ✓ | One-shot Ego Sum Mercurii |
| `bom_ego_sum_minervae_used` | ✓ | ✓ | One-shot Ego Sum Minervae |

### Variables de province

| Variable | Uso |
|---|---|
| `exodos_is_anchor` | Province del ancla — excluida de iteración |
| `exodos_is_destination` | Province destino Transfer |

### Variables de unidad (v4 únicamente)

| Variable | Uso |
|---|---|
| `exodos_unit_anchor` | Unidad ancla |
| `exodos_unit_destination` | Unidad destino |

## 3.7 Panel de decisiones — qué aparece cuándo — v4

**Siempre visible (`potential = { is_ai = no }`):**
- Cancelar Todo — `exodos_cancel_all`

**Siempre visible, en gris hasta que exista ancla:**
- Exodos: Concentración — `exodos_confirm_gather`
- Exodos: Distribución — `exodos_confirm_distribute`
- Exodos: Optimizar — `exodos_confirm_optimize` (sin costo — abre submenu de rangos)

**Siempre visible, en gris hasta que existan ancla Y destino:**
- Exodos: Transferencia — `exodos_confirm_transfer`

**Con `exodos_optimize_active` seteado:**
- Las 4 decisiones de rango (`exodos_opt_range_04`, `_09`, `_14`, `_19`)

**Sin operación activa:**
- Exodos: Gather Global — `exodos_confirm_gather_global`

**Con `exodos_global_active` activo (visible para monitoreo/cancelación):**
- El panel muestra estado pendiente — Cancel All limpia

**Con rivals ≥ 1:**
- BOM: Eliminar Rivales, Bacanal, Et tu Brute?

**Con rivals = 1 exacto, employer=ROOT, is_male=yes, age≥16:**
- IHA: Confiscar, IHA: Fill the Void, Heredero: Hijo del Rival, Heredero: Hija del Rival

**Con tyranny = 0:**
- The Great Leap

**Con is_republic + condiciones TLV:**
- The Last Vote

**Con `bom_ego_sum_X_used` ausente:**
- Filius Martis, Filius Iovis, Filius Mercurii, Filius Minervae

**Sin `has_country_modifier = iram_divine_relic`:**
- Relics: Un Pueblo, Una Fe (crear)

**Con `has_country_modifier = iram_divine_relic`:**
- Relics: Disolver la Reliquia

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 4 — FLUJO COMPLETO DE OPERACIONES — v4
# ══════════════════════════════════════════════════════════

**Principios comunes a todas las operaciones:**
- El jugador posiciona el ancla usando la decisión `exodos_confirm_X` — la ancla es la province donde se concentrará el trabajo.
- Solo una operación activa a la vez — guard: `exodos_operation_active`.
- El jugador paga en la última decisión que desata la función.
- Sin cooldown — se rehabilitan inmediatamente tras éxito o cancelación.

## 4.1 Concentrate (Gather)

```
1. Jugador posiciona la unidad ancla en el territorio donde quiere CONCENTRAR pops
2. exodos_confirm_gather se habilita
   allow: ancla existente + área 100% propia + treasury/manpower/tyranny
3. Jugador clickea confirm → cobra 1000 oro / 2500 manpower / +10 tyranny
   → guarda unit_location → exodos_anchor_province
   → set exodos_is_anchor en esa province
   → set exodos_gather_active + exodos_operation_active
5. monthly_country_pulse corre Gather:
   → mueve pops de todas las fuentes del área hacia ancla (count=20, piso fuentes ≥ 2)
6. Cleanup cuando todas las fuentes llegan a < 2 pops
```

## 4.2 Distribute

```
1. Jugador abre panel de tácticas del territorio que quiere VACIAR
2. Botón A → spawna "Exodos - Ancla" en ese territorio
3. exodos_confirm_distribute se habilita
   allow: ancla existente + área 100% propia + treasury/manpower/tyranny
4. Jugador clickea confirm → cobra 1000 oro / 2500 manpower / +10 tyranny
   → guarda unit_location → exodos_anchor_province
   → set exodos_is_anchor en esa province
   → set exodos_distribute_active + exodos_operation_active
5. monthly_country_pulse corre Distribute:
   → mueve pops desde ancla hacia todas las provinces del área (count=10, piso ancla ≥ 30)
6. Cleanup cuando ancla llega a < 30 pops
```

## 4.3 Transfer

```
1. Jugador abre panel de tácticas del territorio ORIGEN
   → Botón A → spawna "Exodos - Ancla" en ese territorio
2. Jugador abre panel de tácticas del territorio DESTINO
   → Botón B → spawna "Exodos - Destino" (exodos_marker) en ese territorio
   (Botón B visible solo cuando existe ancla y NO existe destino)
3. exodos_confirm_transfer se habilita
   allow: ancla existente + destino existente + ambos owner=ROOT + treasury/manpower/tyranny
4. Jugador clickea confirm → cobra 2000 oro / 5000 manpower / +20 tyranny
   → guarda locations → exodos_anchor_province, exodos_destination_province
   → set exodos_is_anchor y exodos_is_destination
   → set exodos_pulse_counter = 10
   → set exodos_transfer_active + exodos_operation_active
5. monthly_country_pulse corre Transfer:
   → mueve 10 pops/mes desde ancla hacia destino
6. Cleanup cuando contador ≤ 0 O ancla llega a < 2 pops
```

## 4.4 Optimize — flujo crítico y específico

```
1. Jugador abre panel de tácticas de la CIUDAD PRINCIPAL del área
   → Botón A → spawna "Exodos - Ancla" en esa ciudad
2. exodos_confirm_optimize se habilita (en gris hasta que exista ancla)
   allow: ancla existente + área 100% propia
   → SIN COSTO — su único rol es abrir el submenu de rangos
   → efecto: set exodos_optimize_active
   → esto oculta exodos_confirm_optimize y hace aparecer las 17 decisiones de rango
3. Las 17 decisiones de rango aparecen (potential: has_variable = exodos_optimize_active)
   → El jugador verifica el total de pops del área y elige el rango correcto
4. Jugador clickea la decisión de rango → ESA decisión cobra el costo completo:
   2000 oro / 5000 manpower / +10 tyranny
   → set exodos_optimize_count = N (count literal correspondiente al rango)
   → set exodos_operation_active
   → Gather comienza automáticamente en el siguiente pulso
5. monthly_country_pulse — Fase Gather:
   → mueve pops de todas las fuentes del área hacia ancla (count=30, piso fuentes ≥ 2)
   → cuando todas las fuentes < 2 pops: set exodos_optimize_gather_done (NO cleanup aún)
6. monthly_country_pulse — Fase Distribute (siguiente pulso tras gather_done):
   → distribuye desde ancla hacia todas las provinces del área
   → count LITERAL hardcodeado según exodos_optimize_count (17 bloques else_if)
   → corre 1 solo pulso — cleanup automático al final de cada bloque
```

### Tabla de 17 rangos — Optimize — CERRADO v1.2

| Decisión | Rango pops del área | Count por asentamiento |
|---|---|---|
| exodos_opt_range_03 | 45–58 | 3 |
| exodos_opt_range_04 | 59–73 | 4 |
| exodos_opt_range_05 | 74–88 | 5 |
| exodos_opt_range_06 | 89–103 | 6 |
| exodos_opt_range_07 | 104–117 | 7 |
| exodos_opt_range_08 | 118–132 | 8 |
| exodos_opt_range_09 | 133–147 | 9 |
| exodos_opt_range_10 | 148–162 | 10 |
| exodos_opt_range_11 | 163–177 | 11 |
| exodos_opt_range_12 | 178–192 | 12 |
| exodos_opt_range_13 | 193–209 | 13 |
| exodos_opt_range_14 | 210–223 | 14 |
| exodos_opt_range_15 | 224–238 | 15 |
| exodos_opt_range_16 | 239–254 | 16 |
| exodos_opt_range_17 | 255–268 | 17 |
| exodos_opt_range_18 | 269–284 | 18 |
| exodos_opt_range_19 | 285–300 | 19 |

**Puntos de cruce:** 3→4: 58/59 | 4→5: 73/74 | 5→6: 88/89 | 6→7: 103/104 | 7→8: 117/118 | 8→9: 132/133 | 9→10: 147/148 | 10→11: 162/163 | **11→12: 177/178** ✓ CORREGIDO v1.6 | 12→13: 192/193 | 13→14: 209/210 | 14→15: 223/224 | 15→16: 238/239 | 16→17: 254/255 | 17→18: 268/269 | 18→19: 284/285

**Por qué estos valores — CERRADO:** los rangos v1.0–v1.1 fueron calculados con scipy.brentq sin
considerar que el Gather deja 1 pop en cada asentamiento (piso `total_population >= 2`).
El count que recibe cada asentamiento del Distribute es `settPops_óptimo − 1`, no `settPops_óptimo`.
Al corregir esto, los puntos de cruce se desplazan 1–6 pops hacia abajo. Verificado con búsqueda
discreta exhaustiva para todos los totales 45–300. Error máximo: ≤ 4.9m por rango (rango 19
acepta hasta 7.8m en t=299–300 porque count=20 no existe). Progresión de anchos: 14–17 pops,
uniforme.

**Parámetros del optimizador:** N_SETT=9, SPD city_conv_ph1=11.59, city_assim_ph1=5.52,
city_assim_ph2=6.87, sett_conv_ph1=6.77, sett_assim_ph1=0.43, sett_assim_ph2=1.80,
FLAT_CONV_CIUDAD=5.15, MULT_CONV_4DEIF=2.25, FLAT_ASSIM_CIUDAD=3.35.

### Mecánica del Gather y resultado del ancla — CERRADO

**El Gather deja 1 pop en cada asentamiento** — el piso es `total_population >= 2` para evitar
errores del engine al vaciar completamente un asentamiento.

**Flujo de pops para un área de N pops totales con count C:**

```
Antes del Gather:  ancla = cityPops (variable) | cada asent. = settPops (variable)
Después del Gather: ancla = N − 9  | cada asent. = 1
Después del Distribute: ancla = N − 9×(C+1) | cada asent. = 1 + C
```

**Fórmula del ancla final:** `ancla_final = total − 9 × (count + 1)`

| Count | Rango | Ancla @ lo | Ancla @ mid | Ancla @ hi | Cada asent. |
|---|---|---|---|---|---|
| 3 | 45–58 | 9 | 16 | 22 | 4 |
| 4 | 59–73 | 14 | 21 | 28 | 5 |
| 5 | 74–88 | 19 | 26 | 34 | 6 |
| 6 | 89–103 | 25 | 32 | 39 | 7 |
| 7 | 104–117 | 31 | 38 | 44 | 8 |
| 8 | 118–132 | 37 | 44 | 51 | 9 |
| 9 | 133–147 | 43 | 50 | 57 | 10 |
| 10 | 148–162 | 49 | 56 | 63 | 11 |
| 11 | 163–177 | 54 | 61 | 67 | 12 |
| 12 | 177–192 | 60 | 67 | 75 | 13 |
| 13 | 193–209 | 67 | 75 | 83 | 14 |
| 14 | 210–223 | 74 | 81 | 88 | 15 |
| 15 | 224–238 | 80 | 87 | 95 | 16 |
| 16 | 239–254 | 86 | 93 | 101 | 17 |
| 17 | 255–268 | 93 | 100 | 107 | 18 |
| 18 | 269–284 | 98 | 107 | 115 | 19 |
| 19 | 285–300 | 105 | 113 | 120 | 20 |

Ningún ancla queda en 0 o negativo — el mínimo es 9 pops (count=3, total=45).

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 5 — FLUJO DE BOM, IHA, TLV, TGL, HEREDERO DEL RIVAL
# ══════════════════════════════════════════════════════════

## 5.1 BOM: Eliminar Rivales (`bom_confirm`)
- Mata a todos los rivales del gobernante (hasta 4 — límite del engine) con `add_health = -100`
- Stateless — sin variables de estado
- Costo: 2000 oro, 500 manpower, +40 tyranny, cap ≤80, rivals ≥ 1

## 5.2 BOM: Bacanal (`bom_bacanal`)
- `remove_trait = chaste` → `add_trait = lustful` en todos los rivales del gobernante
- Costo: 500 oro, +10 tyranny, cap ≤90, rivals ≥ 1

## 5.3 BOM: Et tu, Brute? (`bom_kill_ruler`)
- Mata al gobernante actual con `add_health = -100`
- Disponible en cualquier tipo de gobierno — no requiere república
- Costo: 2000 oro, 500 manpower, +40 tyranny, cap ≤60, stability ≥ 50

## 5.4 IHA: Confiscar Propiedades (`iha_seize_holdings`)
- Confisca todos los holdings del rival único del gobernante
- El rival sobrevive con `family_property_seized_l` (-40 loyalty por 20 años)
- Patrón validado: `while { limit { num_holdings_owned > 0 } random_holdings { save_scope_as = X } remove_holding = scope:X }`
  (`remove_holding` va dentro del `while` pero FUERA del bloque `random_holdings`)
- Costo: 2000 oro, +40 tyranny, cap ≤60, rivals=1 exacto, employer=ROOT

## 5.5 IHA: Fill the Void (`iha_fill_the_void`)
- Transfiere todas las propiedades sin dueño al rival único
- La capital está excluida automáticamente (el engine no le asigna holding slot)
- Usa `save_scope_as = iha_rival_scope` → `scope:iha_rival_scope = { add_holding = PREV }`
- Costo: 2000 oro, +40 tyranny, cap ≤60, rivals=1 exacto, employer=ROOT

## 5.6 BOM: Ego Sum (4 decisiones one-shot)

| ID | Nombre | Stat | Variable one-shot |
|---|---|---|---|
| `bom_ego_sum_mars` | Filius Martis — Path of War | martial +10 | `bom_ego_sum_mars_used` |
| `bom_ego_sum_iovis` | Filius Iovis — Path of Piety | zeal +10 | `bom_ego_sum_iovis_used` |
| `bom_ego_sum_mercurii` | Filius Mercurii — Path of Oratory | charisma +10 | `bom_ego_sum_mercurii_used` |
| `bom_ego_sum_minervae` | Filius Minervae — Path of Wisdom | finesse +10 | `bom_ego_sum_minervae_used` |

## 5.7 The Last Vote (`tlv_confirm`)
- Disuelve república → dictadura — IRREVERSIBLE
- Orden obligatorio: `clearup` → `law_variable` → `change_government` → `law_change`
- `dictatorship` es `type = monarchy` — `nominated_heir` funciona sin restricciones
- Costo: 2000 oro, +40 tyranny, -50 stability, cap ≤60, is_republic, stability ≥ 50, popularity ≥ 50
- ⚠ TESTEAR: `current_ruler` desde country scope en trigger — puede no resolver.
  Alternativa documentada (no verificada si es necesaria):
  `any_character = { is_ruler = yes  popularity >= 50 }` — ver Sección 6.1 y 6.6

## 5.8 The Great Leap (`tgl_confirm`)
- Otorga 320 innovations (árbol completo) — one-shot
- Costo dinámico: 516 oro/metrópolis + 258 oro/ciudad, +100 tyranny, cap ≤0, piso ≥258
- Bloqueado por `tgl_purchased` tras uso

## 5.9 Heredero del Rival (v1.6 — sin cambios en v4)

**Condiciones:** 1 rival exacto, is_male=yes, age≥16, employer=ROOT

**Flujo:**
1. Captura rival → `save_scope_as = exodos_rival`
2. Si el rival es casado → captura esposa → `save_scope_as = exodos_rival_spouse`
3. `create_character` con `father = scope:exodos_rival` + `mother = scope:exodos_rival_spouse` (si existe)
4. Herencia patrilineal: hereda los 7 traits dinásticos del padre si los tiene
5. Herencia matrilineal: hereda los 7 traits dinásticos de la madre (con `limit = { exists = scope:exodos_rival_spouse }`)

**7 traits dinásticos:** `antigonids`, `antipatrid`, `lagids`, `seleucids`, `argeads`, `aeacidae`, `alcimachid`

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 6 — GOTCHAS DEL ENGINE
# ══════════════════════════════════════════════════════════

**Leyenda de severidad:**
- 💀 **Silencioso** — el engine no reporta nada, el código simplemente no funciona. El más peligroso.
- ⚠️ **Error en log** — aparece en `error.log`, fácil de detectar.
- ℹ️ **Ignorable** — genera warning pero no afecta el funcionamiento.

## 6.1 Scopes

| Severidad | Problema | Solución correcta | Confirmado en |
|---|---|---|---|
| ⚠️ | `ruler = { }` desde country scope en effect | `every_character = { limit = { is_ruler = yes } ... }` | BOM v2.5 |
| ⚠️ | `ruler = { }` desde country scope en trigger | `any_character = { is_ruler = yes ... }` | BOM v2.5 |
| 💀 | `every_rival = { }` directo desde country scope | `every_character = { limit = { is_ruler = yes } every_rival = { } }` | BOM v2.5 |
| 💀 | `move_pop = prev` desde scope pop | `save_scope_as` antes del bucle + `move_pop = scope:nombre` | Exodus bug 1 |
| 💀 | `current_ruler` desde province scope | No resuelve — guardar con `every_character = { is_ruler = yes save_scope_as = X }` antes | IHA Fill the Void v1.3.1 |
| 💀 | `current_ruler` desde country scope en trigger | ⚠ TESTEAR — puede no resolver. Alternativa: `any_character = { is_ruler = yes  popularity >= 50 }` | tlv_confirm |
| 💀 | Iterar holdings y remover en el mismo loop | `while { limit { num_holdings_owned > 0 } random_holdings { save_scope_as = x } remove_holding = scope:x }` — `remove_holding` fuera de `random_holdings` | IHA Seize v1.3.3 |
| ℹ️ | `save_scope_as` entre ticks | No persiste — no necesita cleanup | Exodus alt |
| 💀 | `save_scope_as` dentro de `random_holdings` no persiste fuera del bloque | Mover el efecto que usa el scope (ej: `remove_holding`) fuera de `random_holdings` pero dentro del `while` | IHA Seize v1.3.3, Sesión 051 |
| 💀 | `every_owned_province` desde scope `pop` | No itera — usar `save_scope_as` antes de entrar al scope pop | Gather temprano |

## 6.2 Variables y flags

| Severidad | Problema | Solución correcta | Confirmado en |
|---|---|---|---|
| 💀 | `set_country_flag` / `has_country_flag` / `clr_country_flag` | `set_variable` / `has_variable` / `remove_variable` | Exodus bug 4 |
| 💀 | `set_province_flag` / `has_province_flag` / `remove_province_flag` | `set_variable` / `has_variable` / `remove_variable` en scope province | Exodus bug 4 |
| 💀 | `set_unit_flag` / `has_unit_flag` | `set_variable` / `has_variable` en scope unit | Exodus bug 4 |
| 💀 | `check_variable = { ... }` | `var:nombre >= valor` directo | Exodus bug 4 |
| ⚠️ | `count = var:X` en `while` | **NO FUNCIONA** — devuelve `Value of wrong type: 'none'`. Usar count literal. | IRAM Distribute |
| 💀 | `var:X >= var:Y` | Contador descendente, comparar contra 0 | Exodus bug 3 |
| ⚠️ | `change_variable` sobre variable no seteada | Inicializar con `set_variable` antes del primer pulso | Exodus bug (counter) |
| ⚠️ | BOM doble en archivo de units: si el BOM queda dentro del nombre del tipo (`\xEF\xBB\xBFexodus_marker`), el unit type se registra con nombre corrupto y `create_unit` no lo encuentra | Reescribir el archivo limpio con BOM solo al inicio, verificar con hex editor que el primer token sea el nombre del tipo sin prefijo | Sesión 104, Agente 5 |

## 6.3 Sintaxis que no existe en IR 2.0.4

| Severidad | Sintaxis errónea | Reemplazo correcto | Confirmado en |
|---|---|---|---|
| ⚠️ | `every_owned_territory` | `every_owned_province` | TGL v1.1 |
| ⚠️ | `province_rank = city_metropolis` | `has_province_rank = city_metropolis` | TGL v1.1 |
| ⚠️ | `num_of_pops` | No funciona — devuelve `Cannot read [num_of_pops] as a script value` en log. Usar `total_population >= N` en scope province | Sesión 104, Agente 5 — confirmado con error.log real |
| ⚠️ | `disband_unit = yes` | `destroy_unit = yes` | Exodus bug 4 |
| 💀 | `is_triggered_only = yes` en eventos de mod | Eliminar | Exodus bug 8 |
| ⚠️ | `ai_will_do = { value = 0 }` | `ai_will_do = { factor = 0 }` | Exodus bug 4 |
| 💀 | `death = { death_reason = ... }` desde ruler scope | No funciona, silencioso — usar `add_health = -100` | BOM, TLV |
| ⚠️ | `has_holding` como trigger directo | `num_holdings_owned > 0` en character scope | IHA design |
| ⚠️ | `namespace` ausente en archivo de eventos | Agregar `namespace = X` como primera línea | Exodus bug (eventos) |

## 6.4 Localización

| Severidad | Problema | Solución | Confirmado en |
|---|---|---|---|
| ⚠️ | Corchetes `[ ]` en texto libre de yml | Usar paréntesis `( )` | TGL v1.3, Exodus bug 24, Sesión 118 (`tgl_purchase_cost_tt`) |
| ⚠️ | BOM ausente en .txt o .yml | Agregar BOM `EF BB BF` con `build_mods.py` o Python `utf-8-sig` | Todos |
| ⚠️ | BOM presente en .mod o descriptor.mod | Eliminar — van sin BOM | Todos |
| 💀 | Key `_desc` genérico compartido entre decisiones numeradas | Un key `_desc` por cada decisión con el número exacto en el key | ERROR 13 |

## 6.5 Miscelánea

| Severidad | Regla | Detalle | Confirmado en |
|---|---|---|---|
| ℹ️ | Manpower x500 | Valor en script = valor pantalla / 500 | Exodus |
| 💀 | `country_event` | Siempre dispara en `root` — no en país objetivo | BOM v2.1 |
| 💀 | Cooldown con variables de tiempo | Genera fallos en delay — no usar | BOM v2.3 |
| ⚠️ | IDs de eventos | Deben ser numéricos: `exodos.1`, no `exodos.fail` | Exodus bug 10 |
| ⚠️ | `destroy_unit` en unidad inexistente | Genera error en log — siempre usar dentro de `limit` | IRAM cancel_all |
| ℹ️ | Slots de edificios | `floor(pops/10) + local_building_slot` del rank. Define: `POPS_PER_BUILDING = 10` | game files |
| 💀 | Carpeta interna del mod renombrada | El juego no carga — mantener nombre de carpeta fijo | Exodus bug (carpeta) |
| ⚠️ | `dlc_load.json` sin el mod | El mod no carga aunque esté en Irony | Exodus bug (dlc_load) |

## 6.6 Preguntas frecuentes — patrones más consultados

**¿Cómo muevo un pop de province A a province B?**
```pdxscript
# Desde scope country, antes del loop:
var:exodos_anchor_province = { save_scope_as = exodos_dest }
# Desde scope province A:
random_pops_in_province = { move_pop = scope:exodos_dest }
# Con while y piso:
while = { count = 20  limit = { total_population >= 2 }
    random_pops_in_province = { move_pop = scope:exodos_dest } }
```

**¿Cómo itero todas las provinces de un área?**
```pdxscript
var:exodos_anchor_province = {
    area = { every_area_province = { limit = { owner = ROOT } ... } }
}
```

**¿Por qué no aparece mi decisión en el panel?**
Causas en orden de frecuencia: (1) `potential` no se cumple — verificar variables de estado, (2) BOM ausente en el `.txt`, (3) `dlc_load.json` no lista el mod, (4) namespace faltante en eventos, (5) carpeta del mod renombrada.

**¿Cómo mato al gobernante?**
```pdxscript
every_character = { limit = { is_ruler = yes }  add_health = -100 }
```

**¿Cómo mato a todos los rivales del gobernante?**
```pdxscript
every_character = { limit = { is_ruler = yes }  every_rival = { add_health = -100 } }
```

**¿Cómo itero y remuevo holdings de un personaje?**
```pdxscript
# Desde scope character del rival:
while = {
    limit = { num_holdings_owned > 0 }
    random_holdings = { save_scope_as = iha_holding }
    remove_holding = scope:iha_holding   # fuera de random_holdings
}
```

**¿Cómo verifico si el área está 100% bajo mi control?**
```pdxscript
any_unit = {
    has_variable = exodos_unit_anchor
    unit_location = {
        area = { NOT = { any_area_province = { NOT = { owner = ROOT } } } }
    }
}
```

**¿Qué pasa si uso `count = var:X` en un `while`?**
El engine devuelve `Value of wrong type: 'none'` y el `while` no corre. Siempre usar literales.

**¿Cómo bloqueo una decisión durante una operación activa?**
```pdxscript
allow = {
    NOT = { has_variable = exodos_operation_active }
    NOT = { has_variable = exodos_optimize_active }
    ...
}
```

**¿Cómo agrego una variable a una province desde scope country?**
```pdxscript
var:exodos_anchor_province = {
    set_variable = { name = exodos_is_anchor  value = 1 }
}
```

**¿Cómo limpio todas las variables al finalizar?**
Llamar `exodos_cleanup_effect = yes` — limpia todo (variables de país, province y unidades). Ver Sección 9 para el código completo.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 7 — GUÍA DE DIAGNÓSTICO — error.log
# ══════════════════════════════════════════════════════════

```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\logs\error.log
```

Sobreescribe en cada sesión. Cerrarlo antes de leerlo para lectura completa.

**Buscar después de cargar la partida — si no aparecen, el ecosistema está limpio:**
```
exodos_   bom_   tlv_   tgl_   iha_
Wrong scope   Data error in loc key   Corrupt Decision
```

**Errores críticos del ecosistema:**

| Mensaje | Causa | Solución |
|---|---|---|
| `Wrong scope for effect: country, expected character` | `ruler = { }` en effect desde country | `every_character = { limit = { is_ruler = yes } ... }` |
| `Wrong scope for trigger: country, expected character` | `ruler = { }` en trigger desde country | `any_character = { is_ruler = yes ... }` |
| `Data error in loc key` | Corchetes `[ ]` en yml | Reemplazar por `( )` |
| `Corrupt Decision Table Entry - '\xEF\xBB\xBF...'` | BOM pegado al token | Regenerar con `build_mods.py` |
| `Value of wrong type: 'none'` en while | `count = var:X` — no funciona | Usar count literal |
| `could not find unit type exodos_anchor` | `exodos_units.txt` sin BOM o ruta incorrecta | Verificar BOM y ruta |

**Errores de vanilla — ignorar siempre:**

| Mensaje | Causa |
|---|---|
| `has_province_modifier` Wrong scope (~118 hits) | Game files vanilla — ignorar |
| `Missing Icon for Modifier: exodos_marker_*` (19 hits) | Sub_unit sin íconos GFX — permanente e ignorable |
| `Widget (id 'NNNNN') has not been destroyed` | Engine base al cerrar el juego — ignorar siempre |
| `No valid pantheon for [país]` | Países sin religión politeísta definida — ignorar |
| `Invalid achievement: ach_X` | Logros desactivados por mods — ignorar |
| `GetCanChangeGameSpeedString` | Función de GUI vanilla no encontrada — ignorar |
| `local_commerce_value_modifier: unknown token` en archivos vanilla | Token de versión anterior en game files — ignorar en 2.0.4 |
| `Undefined event target 'iha_holding'` en `exodos_decisions_bom.txt` línea 114 | Cosmético permanente — funciona correctamente en partida |
| `install_philokles_egypt` (cualquier mensaje relacionado) | Función vanilla — no es del mod, ignorar siempre |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 8 — CÓDIGO FUENTE COMPLETO — IRAM v3
# ══════════════════════════════════════════════════════════

Esta sección contiene el código fuente completo de todos los archivos de IRAM v3
(`mod_pack_IRAM_12.zip`). Es la base de código para construir v4.

---

## 8.1 exodos_units.txt

```pdxscript
exodos_marker = {
    army = yes
    levy_tier = none
    movement_speed = 5
    build_cost = { gold = 0  manpower = 0 }
    food_consumption = 0
    light_infantry = 0.0   heavy_infantry = 0.0   heavy_cavalry = 0.0
    warelephant = 0.0      horse_archers = 0.0    archers = 0.0
    chariots = 0.0         camels = 0.0           light_cavalry = 0.0
    supply_train = 0.0     attrition_weight = 0.0
    morale_damage_taken = 0.0   setup_fraction = 0.0
    ai_max_percentage = 0
}
```

---

## 8.2 exodos_scripted_effects.txt

```pdxscript
exodos_cleanup_effect = {

    # Variables de operacion
    remove_variable = exodos_operation_active
    remove_variable = exodos_gather_active
    remove_variable = exodos_transfer_active
    remove_variable = exodos_distribute_active
    remove_variable = exodos_transfer_pending
    remove_variable = exodos_gather_pending
    remove_variable = exodos_distribute_pending
    remove_variable = exodos_anchor_province
    remove_variable = exodos_destination_province
    remove_variable = exodos_pulse_counter

    # Variables Optimizar
    remove_variable = exodos_optimize_pending
    remove_variable = exodos_optimize_active
    remove_variable = exodos_optimize_gather_done
    remove_variable = exodos_optimize_count

    # Variables de province
    every_owned_province = {
        limit = {
            OR = {
                has_variable = exodos_is_anchor
                has_variable = exodos_is_destination
            }
        }
        remove_variable = exodos_is_anchor
        remove_variable = exodos_is_destination
    }

    # Disolver unidades Exodos
    every_unit = {
        limit = {
            OR = {
                has_variable = exodos_unit_transfer_origin
                has_variable = exodos_unit_transfer_dest
                has_variable = exodos_unit_concentrate
                has_variable = exodos_unit_distribute
                has_variable = exodos_unit_optimize
            }
        }
        destroy_unit = yes
    }
}
```

---

## 8.3 exodos_decisions_gather_distribute.txt (v3)

```pdxscript
country_decisions = {

    exodos_activate_gather = {
        potential = {
            is_ai = no
            NOT = { has_variable = exodos_transfer_pending }
            NOT = { has_variable = exodos_gather_pending }
            NOT = { has_variable = exodos_distribute_pending }
            NOT = { has_variable = exodos_operation_active }
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  in_command = yes }
            }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  in_command = yes }
            }
            tyranny <= 90
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT  is_male = yes  in_command = yes }
                    every_unit = {
                        limit = { commander = prev }
                        unit_location = {
                            ROOT = {
                                create_unit = {
                                    name = "Exodos - Concentrar"
                                    location = prev
                                    sub_unit = exodos_marker
                                    save_scope_as = exodos_unit_scope
                                }
                            }
                        }
                    }
                }
            }
            scope:exodos_unit_scope = {
                set_variable = { name = exodos_unit_concentrate value = 1 }
            }
            set_variable = { name = exodos_gather_pending value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_confirm_gather = {
        potential = {
            is_ai = no
            has_variable = exodos_gather_pending
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            custom_tooltip = exodos_tt_unit_stopped
            NOT = { any_unit = { has_variable = exodos_unit_concentrate  is_moving = yes } }
            any_unit = {
                has_variable = exodos_unit_concentrate
                unit_location = { owner = ROOT }
            }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_concentrate
                unit_location = {
                    area = { NOT = { any_area_province = { NOT = { owner = ROOT } } } }
                }
            }
            treasury >= 1000
            manpower >= 5
            tyranny <= 90
        }
        effect = {
            add_treasury = -1000
            add_manpower = -5
            add_tyranny = 10
            every_unit = {
                limit = { has_variable = exodos_unit_concentrate }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            remove_variable = exodos_gather_pending
            set_variable = { name = exodos_operation_active  value = 1 }
            set_variable = { name = exodos_gather_active  value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_activate_distribute = {
        potential = {
            is_ai = no
            NOT = { has_variable = exodos_transfer_pending }
            NOT = { has_variable = exodos_gather_pending }
            NOT = { has_variable = exodos_distribute_pending }
            NOT = { has_variable = exodos_operation_active }
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  in_command = yes }
            }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  in_command = yes }
            }
            tyranny <= 90
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT  is_male = yes  in_command = yes }
                    every_unit = {
                        limit = { commander = prev }
                        unit_location = {
                            ROOT = {
                                create_unit = {
                                    name = "Exodos - Distribuir"
                                    location = prev
                                    sub_unit = exodos_marker
                                    save_scope_as = exodos_dist_scope
                                }
                            }
                        }
                    }
                }
            }
            scope:exodos_dist_scope = {
                set_variable = { name = exodos_unit_distribute  value = 1 }
            }
            set_variable = { name = exodos_distribute_pending  value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_confirm_distribute = {
        potential = {
            is_ai = no
            has_variable = exodos_distribute_pending
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            custom_tooltip = exodos_tt_unit_stopped
            NOT = { any_unit = { has_variable = exodos_unit_distribute  is_moving = yes } }
            any_unit = {
                has_variable = exodos_unit_distribute
                unit_location = { owner = ROOT }
            }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_distribute
                unit_location = {
                    area = { NOT = { any_area_province = { NOT = { owner = ROOT } } } }
                }
            }
            treasury >= 1000
            manpower >= 5
            tyranny <= 90
        }
        effect = {
            add_treasury = -1000
            add_manpower = -5
            add_tyranny = 10
            every_unit = {
                limit = { has_variable = exodos_unit_distribute }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            remove_variable = exodos_distribute_pending
            set_variable = { name = exodos_operation_active  value = 1 }
            set_variable = { name = exodos_distribute_active  value = 1 }
        }
        ai_will_do = { factor = 0 }
    }
}
```

---

## 8.4 exodos_decisions_transfer.txt (v3)

```pdxscript
country_decisions = {

    exodos_activate_transfer = {
        potential = {
            is_ai = no
            NOT = { has_variable = exodos_transfer_pending }
            NOT = { has_variable = exodos_gather_pending }
            NOT = { has_variable = exodos_distribute_pending }
            NOT = { has_variable = exodos_operation_active }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            tyranny <= 80
        }
        effect = {
            create_unit = {
                name = "Exodos - Origen"
                location = capital_scope
                sub_unit = exodos_marker
                save_scope_as = exodos_origin_scope
            }
            scope:exodos_origin_scope = {
                set_variable = { name = exodos_unit_transfer_origin  value = 1 }
            }
            create_unit = {
                name = "Exodos - Destino"
                location = capital_scope
                sub_unit = exodos_marker
                save_scope_as = exodos_dest_scope
            }
            scope:exodos_dest_scope = {
                set_variable = { name = exodos_unit_transfer_dest  value = 1 }
            }
            set_variable = { name = exodos_transfer_pending  value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_confirm_transfer = {
        potential = {
            is_ai = no
            has_variable = exodos_transfer_pending
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            custom_tooltip = exodos_tt_unit_stopped
            NOT = { any_unit = { has_variable = exodos_unit_transfer_origin  is_moving = yes } }
            NOT = { any_unit = { has_variable = exodos_unit_transfer_dest  is_moving = yes } }
            any_unit = { has_variable = exodos_unit_transfer_origin  unit_location = { owner = ROOT } }
            any_unit = { has_variable = exodos_unit_transfer_dest  unit_location = { owner = ROOT } }
            treasury >= 2000
            manpower >= 10
            tyranny <= 80
        }
        effect = {
            add_treasury = -2000
            add_manpower = -10
            add_tyranny = 20
            every_unit = {
                limit = { has_variable = exodos_unit_transfer_origin }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            every_unit = {
                limit = { has_variable = exodos_unit_transfer_dest }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_destination_province  value = prev } }
                    set_variable = { name = exodos_is_destination  value = 1 }
                }
            }
            set_variable = { name = exodos_pulse_counter  value = 10 }
            remove_variable = exodos_transfer_pending
            set_variable = { name = exodos_operation_active  value = 1 }
            set_variable = { name = exodos_transfer_active  value = 1 }
        }
        ai_will_do = { factor = 0 }
    }
}
```

---

## 8.5 exodos_decisions_optimize.txt (v3 — primeros bloques, el resto es el mismo patrón)

Ver Sección 4.4 para la tabla completa de 17 rangos. El archivo en v3 tiene el activate con
condición de rival, igual que Gather y Distribute. El código de on_action tiene los 17 bloques
`else_if` con count literal del rango 3 al 19 — el patrón es idéntico al de on_action.

---

## 8.6 exodos_decisions_cancel.txt (v3)

```pdxscript
country_decisions = {

    exodos_cancel_all = {
        potential = { is_ai = no }
        highlight = { scope:province = { always = yes } }
        allow = { always = yes }
        effect = { exodos_cleanup_effect = yes }
        ai_will_do = { factor = 0 }
    }
}
```

---

## 8.7 exodos_on_action.txt (v3 — completo)

```pdxscript
monthly_country_pulse = {
    effect = {
        if = {
            limit = {
                is_ai = no
                has_variable = exodos_operation_active
            }

            # ── 1. CHEQUEOS DE ERROR ──────────────────────────────────

            if = {
                limit = {
                    has_variable = exodos_optimize_active
                    NOT = { any_unit = { has_variable = exodos_unit_optimize } }
                }
                trigger_event = { id = exodos.1 }
            }
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
            else_if = {
                limit = { var:exodos_anchor_province = { NOT = { owner = ROOT } } }
                trigger_event = { id = exodos.1 }
            }
            else_if = {
                limit = {
                    has_variable = exodos_transfer_active
                    var:exodos_destination_province = { NOT = { owner = ROOT } }
                }
                trigger_event = { id = exodos.1 }
            }
            else_if = {
                limit = {
                    has_variable = exodos_optimize_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }
            else_if = {
                limit = {
                    has_variable = exodos_gather_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }
            else_if = {
                limit = {
                    has_variable = exodos_distribute_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            else = {

                # ── 2. OPTIMIZE — FASE GATHER ─────────────────────────
                if = {
                    limit = {
                        has_variable = exodos_optimize_active
                        NOT = { has_variable = exodos_optimize_gather_done }
                    }
                    var:exodos_anchor_province = {
                        save_scope_as = exodos_dest
                        area = {
                            every_area_province = {
                                limit = {
                                    owner = ROOT
                                    total_population >= 2
                                    NOT = { has_variable = exodos_is_anchor }
                                }
                                while = {
                                    count = 30
                                    limit = { total_population >= 2 }
                                    random_pops_in_province = { move_pop = scope:exodos_dest }
                                }
                            }
                        }
                    }
                    if = {
                        limit = {
                            var:exodos_anchor_province = {
                                area = {
                                    NOT = {
                                        any_area_province = {
                                            NOT = { has_variable = exodos_is_anchor }
                                            total_population >= 2
                                        }
                                    }
                                }
                            }
                        }
                        set_variable = { name = exodos_optimize_gather_done  value = 1 }
                    }
                }

                # ── 3. OPTIMIZE — FASE DISTRIBUTE — 17 bloques else_if ──
                # Patrón idéntico para count = 3, 4, 5 … 19
                # (el código completo está en el zip — ver exodos_on_action.txt)

                # ── 4. GATHER legacy ──────────────────────────────────
                else_if = {
                    limit = { has_variable = exodos_gather_active }
                    var:exodos_anchor_province = {
                        save_scope_as = exodos_dest
                        area = {
                            every_area_province = {
                                limit = {
                                    owner = ROOT
                                    total_population >= 2
                                    NOT = { has_variable = exodos_is_anchor }
                                }
                                while = {
                                    count = 20
                                    limit = { total_population >= 2 }
                                    random_pops_in_province = { move_pop = scope:exodos_dest }
                                }
                            }
                        }
                    }
                    if = {
                        limit = {
                            var:exodos_anchor_province = {
                                area = {
                                    NOT = {
                                        any_area_province = {
                                            NOT = { has_variable = exodos_is_anchor }
                                            total_population >= 2
                                        }
                                    }
                                }
                            }
                        }
                        exodos_cleanup_effect = yes
                    }
                }

                # ── 5. TRANSFER ───────────────────────────────────────
                else_if = {
                    limit = { has_variable = exodos_transfer_active }
                    var:exodos_destination_province = { save_scope_as = exodos_dest }
                    var:exodos_anchor_province = {
                        while = {
                            count = 10
                            limit = { total_population >= 2 }
                            random_pops_in_province = { move_pop = scope:exodos_dest }
                        }
                    }
                    change_variable = { name = exodos_pulse_counter  add = -1 }
                    if = {
                        limit = {
                            OR = {
                                var:exodos_pulse_counter <= 0
                                var:exodos_anchor_province = { total_population < 2 }
                            }
                        }
                        exodos_cleanup_effect = yes
                    }
                }

                # ── 6. DISTRIBUTE legacy ──────────────────────────────
                else_if = {
                    limit = { has_variable = exodos_distribute_active }
                    var:exodos_anchor_province = {
                        save_scope_as = exodos_origin
                        area = {
                            every_area_province = {
                                limit = {
                                    owner = ROOT
                                    total_population >= 1
                                    NOT = { has_variable = exodos_is_anchor }
                                }
                                save_scope_as = exodos_dist_target
                                while = {
                                    count = 10
                                    limit = { scope:exodos_origin = { total_population >= 30 } }
                                    scope:exodos_origin = {
                                        random_pops_in_province = { move_pop = scope:exodos_dist_target }
                                    }
                                }
                            }
                        }
                    }
                    if = {
                        limit = { var:exodos_anchor_province = { total_population < 30 } }
                        exodos_cleanup_effect = yes
                    }
                }
            }
        }
    }
}
```

---

## 8.8 exodos_decisions_rival_heir.txt (v3 — completo, sin cambios en v4)

```pdxscript
country_decisions = {

    exodos_spawn_rival_son = {
        potential = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  age >= 16 }
            }
        }
        allow = {
            is_ai = no
            custom_tooltip = exodos_tt_rival_unique
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  age >= 16 }
            }
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT  is_male = yes  age >= 16 }
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
                    age = 0  female = no
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
                    age = 0  female = no
                    save_scope_as = exodos_newborn
                    family = scope:exodos_rival.family
                    religion = scope:exodos_rival.religion
                    culture = scope:exodos_rival.culture
                    father = scope:exodos_rival
                }
            }
            scope:exodos_newborn = {
                # Patrilineal — padre
                if = { limit = { scope:exodos_rival = { has_trait = antigonids } }  add_trait = antigonids }
                if = { limit = { scope:exodos_rival = { has_trait = antipatrid  } }  add_trait = antipatrid  }
                if = { limit = { scope:exodos_rival = { has_trait = lagids      } }  add_trait = lagids      }
                if = { limit = { scope:exodos_rival = { has_trait = seleucids   } }  add_trait = seleucids   }
                if = { limit = { scope:exodos_rival = { has_trait = argeads     } }  add_trait = argeads     }
                if = { limit = { scope:exodos_rival = { has_trait = aeacidae    } }  add_trait = aeacidae    }
                if = { limit = { scope:exodos_rival = { has_trait = alcimachid  } }  add_trait = alcimachid  }
                # Matrilineal — madre
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = antigonids } }  add_trait = antigonids }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = antipatrid  } }  add_trait = antipatrid  }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = lagids      } }  add_trait = lagids      }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = seleucids   } }  add_trait = seleucids   }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = argeads     } }  add_trait = argeads     }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = aeacidae    } }  add_trait = aeacidae    }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = alcimachid  } }  add_trait = alcimachid  }
            }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_spawn_rival_daughter = {
        potential = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  age >= 16 }
            }
        }
        allow = {
            is_ai = no
            custom_tooltip = exodos_tt_rival_unique
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT  is_male = yes  age >= 16 }
            }
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT  is_male = yes  age >= 16 }
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
                    age = 0  female = yes
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
                    age = 0  female = yes
                    save_scope_as = exodos_newborn
                    family = scope:exodos_rival.family
                    religion = scope:exodos_rival.religion
                    culture = scope:exodos_rival.culture
                    father = scope:exodos_rival
                }
            }
            scope:exodos_newborn = {
                # Patrilineal — padre
                if = { limit = { scope:exodos_rival = { has_trait = antigonids } }  add_trait = antigonids }
                if = { limit = { scope:exodos_rival = { has_trait = antipatrid  } }  add_trait = antipatrid  }
                if = { limit = { scope:exodos_rival = { has_trait = lagids      } }  add_trait = lagids      }
                if = { limit = { scope:exodos_rival = { has_trait = seleucids   } }  add_trait = seleucids   }
                if = { limit = { scope:exodos_rival = { has_trait = argeads     } }  add_trait = argeads     }
                if = { limit = { scope:exodos_rival = { has_trait = aeacidae    } }  add_trait = aeacidae    }
                if = { limit = { scope:exodos_rival = { has_trait = alcimachid  } }  add_trait = alcimachid  }
                # Matrilineal — madre
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = antigonids } }  add_trait = antigonids }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = antipatrid  } }  add_trait = antipatrid  }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = lagids      } }  add_trait = lagids      }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = seleucids   } }  add_trait = seleucids   }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = argeads     } }  add_trait = argeads     }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = aeacidae    } }  add_trait = aeacidae    }
                if = { limit = { exists = scope:exodos_rival_spouse  scope:exodos_rival_spouse = { has_trait = alcimachid  } }  add_trait = alcimachid  }
            }
        }
        ai_will_do = { factor = 0 }
    }
}
```

---

## 8.9 exodos_decisions_bom.txt (v3 — sin cambios en v4)

```pdxscript
country_decisions = {

    bom_confirm = {
        potential = {
            is_ai = no
            any_character = { is_ruler = yes  num_of_rivals >= 1 }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = { is_ruler = yes  num_of_rivals >= 1 }
            treasury >= 2000
            manpower >= 1
            tyranny <= 80
        }
        effect = {
            add_treasury = -2000  add_manpower = -1  add_tyranny = 40
            every_character = {
                limit = { is_ruler = yes }
                every_rival = { add_health = -100 }
            }
        }
        ai_will_do = { factor = 0 }
    }

    bom_bacanal = {
        potential = {
            is_ai = no
            any_character = { is_ruler = yes  num_of_rivals >= 1 }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = { is_ruler = yes  num_of_rivals >= 1 }
            treasury >= 500
            tyranny <= 90
        }
        effect = {
            add_treasury = -500  add_tyranny = 10
            every_character = {
                limit = { is_ruler = yes }
                every_rival = { remove_trait = chaste  add_trait = lustful }
            }
        }
        ai_will_do = { factor = 0 }
    }

    bom_kill_ruler = {
        potential = { is_ai = no }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            tyranny <= 60  stability >= 50  treasury >= 2000  manpower >= 1
        }
        effect = {
            add_tyranny = 40  add_stability = -50  add_treasury = -2000  add_manpower = -1
            every_character = {
                limit = { is_ruler = yes }
                add_health = -100
            }
        }
        ai_will_do = { factor = 0 }
    }

    iha_seize_holdings = {
        potential = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT }
            }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT }
            }
            treasury >= 2000
            tyranny <= 60
        }
        effect = {
            add_treasury = -2000  add_tyranny = 40
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT }
                    while = {
                        limit = { num_holdings_owned > 0 }
                        random_holdings = { save_scope_as = iha_holding }
                        remove_holding = scope:iha_holding
                    }
                    add_loyalty = family_property_seized_l
                }
            }
        }
        ai_will_do = { factor = 0 }
    }

    iha_fill_the_void = {
        potential = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT }
            }
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            any_character = {
                is_ruler = yes
                num_of_rivals >= 1
                NOT = { num_of_rivals >= 2 }
                any_rival = { employer = ROOT }
            }
            treasury >= 2000
            tyranny <= 60
        }
        effect = {
            add_treasury = -2000  add_tyranny = 40
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT }
                    save_scope_as = iha_rival_scope
                }
            }
            every_owned_province = {
                limit = { NOT = { exists = holding_owner } }
                scope:iha_rival_scope = { add_holding = PREV }
            }
        }
        ai_will_do = { factor = 0 }
    }
}
```

---

## 8.10 exodos_events.txt (v3)

```pdxscript
namespace = exodos

exodos.1 = {
    type = country_event
    title = "exodos.1.t"
    desc = "exodos.1.d"
    immediate = { exodos_cleanup_effect = yes }
    option = { name = "exodos.1.ok" }
}
```

---

## 8.11 Localización v3 (exodos — inglés y español)

> Nota: los textos a continuación son de v3 y describen el flujo legacy (activates y
> posicionamiento manual). En v4 están completamente reescritos — ver Sección 10.

**exodos_l_english.yml (v3):**
```yaml
l_english:
 exodos_activate_gather:0 "Exodos: Gather"
 exodos_activate_gather_desc:0 "The scattered shall be brought together. Deploy the Concentrate unit to mark the destination territory, then confirm the operation. The entire area must be under your control. Cost is paid upon confirmation."
 exodos_activate_distribute:0 "Exodos: Distribute"
 exodos_activate_distribute_desc:0 "The crowded shall be dispersed across the land. Deploy the Distribute unit to mark the source territory, then confirm the operation. The entire area must be under your control. Cost is paid upon confirmation."
 exodos_activate_transfer:0 "Exodos: Transfer"
 exodos_activate_transfer_desc:0 "By decree of the state, the people shall be moved. Deploy the Origin and Destination units to mark the source and destination territories, then confirm the operation. Both units must be stationary and positioned in territories under your control. Cost is paid upon confirmation."
 exodos_confirm_gather:0 "Exodos: Confirm Gather"
 exodos_confirm_gather_desc:0 "Sound the call. The scattered shall converge. The unit must be stationary and the entire area must be under your control."
 exodos_confirm_distribute:0 "Exodos: Confirm Distribute"
 exodos_confirm_distribute_desc:0 "Open the gates. The people shall spread across the land. The unit must be stationary and the entire area must be under your control."
 exodos_confirm_transfer:0 "Exodos: Confirm Transfer"
 exodos_confirm_transfer_desc:0 "The order is given. The people will march for ten months. Both units must be stationary before the operation can begin."
 exodos_cancel_all:0 "Cancel All"
 exodos_cancel_all_desc:0 "Rescinds all active state decrees. Clears any ongoing operation and any residual state from previous mod installations. Costs already paid will not be refunded. Use as a first step when migrating from a previous installation."
 exodos.1.t:0 "The Exodos Has Failed"
 exodos.1.d:0 "The movement of the people has been brought to an abrupt end."
 exodos.1.ok:0 "So be it."
 exodos_tt_rival_unique:0 "Requires exactly one rival, male, aged 16 or older, from your nation."
 exodos_tt_unit_stopped:0 "The units must reach their destination before the operation can begin. (Unit still moving)"
 exodos_tt_area_owner:0 "The entire area must be under the authority of the state. (Area not fully controlled)"
```

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 8-C — CÓDIGO FUENTE COMPLETO — IRAM v4 (mod_pack_IRAM_v4_3.zip)
# ══════════════════════════════════════════════════════════

Esta sección contiene el código fuente real extraído directamente del zip `mod_pack_IRAM_v4_3.zip`.
Es la implementación canónica de v4. Las Secciones 9, 10 y 11 documentan el diseño — esta sección
tiene el código exacto como está en el zip.

### Última sincronización con zip

| Archivo | Última sincronización | Zip de referencia |
|---|---|---|
| `exodos_units.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_scripted_effects.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_on_action.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_gather_distribute.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_optimize.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_cancel.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_transfer.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_bom.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_decisions_rival_heir.txt` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_l_spanish.yml` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |
| `exodos_l_english.yml` | 2026-05-19 | `mod_pack_IRAM_v4_3.zip` |

> ⚠️ Si actualizás el zip sin actualizar el SUPERBACKUP, marcá la fecha como `DESACTUALIZADO — ver zip` hasta que se sincronice.

**⚠️ Bugs conocidos presentes en este zip (pendientes de corregir):**
- Crossover rango 11 en localización: `exodos_opt_range_11` dice "163–176" — debería ser "163–177"
- Comentario en `exodos_decisions_optimize.txt`: dice `11→12:176/177` — debería ser `177/178`

## 8-C.1 Estructura de archivos v4

```
mod_pack_IRAM_v4/
├── exodos.mod                                                    ← sin BOM
├── by_other_means.mod                                            ← sin BOM (TEST SHELL)
├── the_last_vote.mod                                             ← sin BOM (TEST SHELL)
├── the_great_leap.mod                                            ← sin BOM (TEST SHELL)
└── exodos/
    ├── descriptor.mod                                            ← sin BOM
    ├── common/
    │   ├── scripted_guis/exodos_scripted_guis.txt               ← BOM UTF-8 (NUEVO v4)
    │   ├── units/exodos_units.txt                               ← BOM UTF-8
    │   ├── scripted_effects/exodos_scripted_effects.txt         ← BOM UTF-8
    │   └── on_action/exodos_on_action.txt                       ← BOM UTF-8
    ├── decisions/
    │   ├── exodos_decisions_gather_distribute.txt               ← BOM UTF-8
    │   ├── exodos_decisions_transfer.txt                        ← BOM UTF-8
    │   ├── exodos_decisions_optimize.txt                        ← BOM UTF-8
    │   ├── exodos_decisions_cancel.txt                          ← BOM UTF-8
    │   ├── exodos_decisions_bom.txt                             ← BOM UTF-8
    │   ├── exodos_decisions_bom_ego_sum.txt                     ← BOM UTF-8
    │   ├── exodos_decisions_tlv.txt                             ← BOM UTF-8
    │   ├── exodos_decisions_tgl.txt                             ← BOM UTF-8
    │   └── exodos_decisions_rival_heir.txt                      ← BOM UTF-8
    ├── events/
    │   ├── exodos_events.txt                                    ← BOM UTF-8
    │   └── tlv_events.txt                                       ← BOM UTF-8
    └── localization/
        ├── english/exodos_l_english.yml                         ← BOM UTF-8
        └── spanish/exodos_l_spanish.yml                         ← BOM UTF-8
```

## 8-C.2 exodos_units.txt (v4)

```pdxscript
exodos_anchor = {
    army = yes
    levy_tier = none
    movement_speed = 0
    build_cost = { gold = 0 manpower = 0 }
    food_consumption = 0
    light_infantry = 0.0  heavy_infantry = 0.0  heavy_cavalry = 0.0
    warelephant = 0.0  horse_archers = 0.0  archers = 0.0
    chariots = 0.0  camels = 0.0  light_cavalry = 0.0
    supply_train = 0.0  attrition_weight = 0.0
    morale_damage_taken = 0.0  setup_fraction = 0.0
    ai_max_percentage = 0
}

exodos_marker = {
    army = yes
    levy_tier = none
    movement_speed = 0
    build_cost = { gold = 0 manpower = 0 }
    food_consumption = 0
    light_infantry = 0.0  heavy_infantry = 0.0  heavy_cavalry = 0.0
    warelephant = 0.0  horse_archers = 0.0  archers = 0.0
    chariots = 0.0  camels = 0.0  light_cavalry = 0.0
    supply_train = 0.0  attrition_weight = 0.0
    morale_damage_taken = 0.0  setup_fraction = 0.0
    ai_max_percentage = 0
}
```

## 8-C.3 exodos_scripted_guis.txt (v4)

```pdxscript
exodos_spawn_anchor_button = {
    scope = province
    saved_scopes = { player }

    is_shown = {
        owner = scope:player
        scope:player = { is_ai = no }
    }

    is_valid = {
        scope:player = {
            NOT = { has_variable = exodos_operation_active }
            NOT = { has_variable = exodos_optimize_active }
            NOT = { any_unit = { has_variable = exodos_unit_anchor } }
        }
    }

    effect = {
        create_unit = {
            name = "Exodos - Ancla"
            location = ROOT
            sub_unit = exodos_anchor
            save_scope_as = exodos_anchor_scope
        }
        scope:exodos_anchor_scope = {
            set_variable = { name = exodos_unit_anchor  value = 1 }
        }
    }
}

exodos_spawn_destination_button = {
    scope = province
    saved_scopes = { player }

    is_shown = {
        owner = scope:player
        scope:player = {
            is_ai = no
            any_unit = { has_variable = exodos_unit_anchor }
        }
    }

    is_valid = {
        scope:player = {
            NOT = { has_variable = exodos_operation_active }
            NOT = { any_unit = { has_variable = exodos_unit_destination } }
        }
    }

    effect = {
        create_unit = {
            name = "Exodos - Destino"
            location = ROOT
            sub_unit = exodos_marker
            save_scope_as = exodos_dest_scope
        }
        scope:exodos_dest_scope = {
            set_variable = { name = exodos_unit_destination  value = 1 }
        }
    }
}
```

## 8-C.4 exodos_scripted_effects.txt (v4)

```pdxscript
exodos_cleanup_effect = {

    # ── VARIABLES DE PAÍS — v4 ────────────────────────────────
    remove_variable = exodos_operation_active
    remove_variable = exodos_gather_active
    remove_variable = exodos_distribute_active
    remove_variable = exodos_transfer_active
    remove_variable = exodos_optimize_active
    remove_variable = exodos_optimize_gather_done
    remove_variable = exodos_optimize_count
    remove_variable = exodos_anchor_province
    remove_variable = exodos_destination_province
    remove_variable = exodos_pulse_counter

    # ── VARIABLES LEGACY — v3 y anteriores ───────────────────
    remove_variable = exodos_gather_pending
    remove_variable = exodos_distribute_pending
    remove_variable = exodos_transfer_pending
    remove_variable = exodos_optimize_pending

    # ── VARIABLES DE PROVINCE ─────────────────────────────────
    every_owned_province = {
        limit = {
            OR = {
                has_variable = exodos_is_anchor
                has_variable = exodos_is_destination
            }
        }
        remove_variable = exodos_is_anchor
        remove_variable = exodos_is_destination
    }

    # ── UNIDADES — v4 ─────────────────────────────────────────
    every_unit = {
        limit = {
            OR = {
                has_variable = exodos_unit_anchor
                has_variable = exodos_unit_destination
            }
        }
        destroy_unit = yes
    }

    # ── UNIDADES — legacy v3 y anteriores ────────────────────
    every_unit = {
        limit = {
            OR = {
                has_variable = exodos_unit_concentrate
                has_variable = exodos_unit_distribute
                has_variable = exodos_unit_optimize
                has_variable = exodos_unit_transfer_origin
                has_variable = exodos_unit_transfer_dest
            }
        }
        destroy_unit = yes
    }
}
```

## 8-C.5 exodos_decisions_gather_distribute.txt (v4)

```pdxscript
country_decisions = {

    exodos_confirm_gather = {
        potential = { is_ai = no }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            NOT = { has_variable = exodos_operation_active }
            NOT = { has_variable = exodos_optimize_active }
            any_unit = { has_variable = exodos_unit_anchor }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_anchor
                unit_location = {
                    area = { NOT = { any_area_province = { NOT = { owner = ROOT } } } }
                }
            }
            treasury >= 1000
            manpower >= 5
            tyranny <= 90
        }
        effect = {
            add_treasury = -1000
            add_manpower = -5
            add_tyranny = 10
            every_unit = {
                limit = { has_variable = exodos_unit_anchor }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            set_variable = { name = exodos_operation_active  value = 1 }
            set_variable = { name = exodos_gather_active     value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    exodos_confirm_distribute = {
        potential = { is_ai = no }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            NOT = { has_variable = exodos_operation_active }
            NOT = { has_variable = exodos_optimize_active }
            any_unit = { has_variable = exodos_unit_anchor }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_anchor
                unit_location = {
                    area = { NOT = { any_area_province = { NOT = { owner = ROOT } } } }
                }
            }
            treasury >= 1000
            manpower >= 5
            tyranny <= 90
        }
        effect = {
            add_treasury = -1000
            add_manpower = -5
            add_tyranny = 10
            every_unit = {
                limit = { has_variable = exodos_unit_anchor }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            set_variable = { name = exodos_operation_active    value = 1 }
            set_variable = { name = exodos_distribute_active   value = 1 }
        }
        ai_will_do = { factor = 0 }
    }
}
```

## 8-C.6 exodos_decisions_transfer.txt (v4)

```pdxscript
country_decisions = {

    exodos_confirm_transfer = {
        potential = { is_ai = no }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            NOT = { has_variable = exodos_operation_active }
            NOT = { has_variable = exodos_optimize_active }
            any_unit = { has_variable = exodos_unit_anchor }
            any_unit = { has_variable = exodos_unit_anchor  unit_location = { owner = ROOT } }
            any_unit = { has_variable = exodos_unit_destination }
            any_unit = { has_variable = exodos_unit_destination  unit_location = { owner = ROOT } }
            treasury >= 2000
            manpower >= 10
            tyranny <= 80
        }
        effect = {
            add_treasury = -2000
            add_manpower = -10
            add_tyranny = 20
            every_unit = {
                limit = { has_variable = exodos_unit_anchor }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_anchor_province  value = prev } }
                    set_variable = { name = exodos_is_anchor  value = 1 }
                }
            }
            every_unit = {
                limit = { has_variable = exodos_unit_destination }
                unit_location = {
                    ROOT = { set_variable = { name = exodos_destination_province  value = prev } }
                    set_variable = { name = exodos_is_destination  value = 1 }
                }
            }
            set_variable = { name = exodos_pulse_counter      value = 10 }
            set_variable = { name = exodos_operation_active   value = 1 }
            set_variable = { name = exodos_transfer_active    value = 1 }
        }
        ai_will_do = { factor = 0 }
    }
}
```

## 8-C.7 exodos_decisions_cancel.txt (v4) — ver Sección 11 para código completo

El archivo contiene `exodos_cancel_all` con cleanup exhaustivo (v4 + legacy v3). Código completo en Sección 11.

## 8-C.8 exodos_on_action.txt (v4) — 884 líneas

Ver Sección 9 para la lógica del pulso. El archivo corre en orden:
1. Chequeos de error (ancla destruida, destino destruido, ancla perdida, destino perdido, área perdida)
2. Optimize Fase Gather (si `optimize_active` y NOT `optimize_gather_done`)
3. Optimize Fase Distribute — 17 bloques `else_if` por rango (3→19)
4. Gather
5. Transfer
6. Distribute

## 8-C.9 Localización v4 — cambios clave vs v3

| Aspecto | v3 | v4 |
|---|---|---|
| Botones de spawn | No existen | `exodos_spawn_anchor_button`, `exodos_spawn_destination_button` |
| Nombres de decisiones | Con "Activate/Confirm" | Solo "Confirm" (sin activates) |
| `exodos_cancel` | Cubre 3 operaciones | `exodos_cancel_all` — cubre todo + legacy |
| Tooltips | `exodos_tt_no_war`, `exodos_tt_unit_stopped`, `exodos_tt_owner` | `exodos_tt_area_owner`, `exodos_tt_rival_unique` |
| Heredero del Rival | Presentes en v3 | Presentes también en v4 yml |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 9 — DISEÑO v4 — ON_ACTION Y SCRIPTED_GUI
# ══════════════════════════════════════════════════════════

## 9.1 exodos_scripted_guis.txt (NUEVO — v4)

```pdxscript
exodos_spawn_anchor_button = {
    scope = province
    saved_scopes = { player }

    is_shown = {
        owner = scope:player
        scope:player = { is_ai = no }
    }

    is_valid = {
        scope:player = {
            NOT = { has_variable = exodos_operation_active }
            NOT = { has_variable = exodos_optimize_active }   # guard v4_3 — evita spawn con optimize_active flotando
            NOT = { any_unit = { has_variable = exodos_unit_anchor } }
        }
    }

    effect = {
        create_unit = {
            name = "Exodos - Ancla"
            location = ROOT
            sub_unit = exodos_anchor
            save_scope_as = exodos_anchor_scope
        }
        scope:exodos_anchor_scope = {
            set_variable = { name = exodos_unit_anchor  value = 1 }
        }
    }
}

exodos_spawn_destination_button = {
    scope = province
    saved_scopes = { player }

    is_shown = {
        owner = scope:player
        scope:player = {
            is_ai = no
            any_unit = { has_variable = exodos_unit_anchor }
        }
    }

    is_valid = {
        scope:player = {
            NOT = { has_variable = exodos_operation_active }   # guard v4_3 — evita spawn durante operación activa
            NOT = { any_unit = { has_variable = exodos_unit_destination } }
        }
    }

    effect = {
        create_unit = {
            name = "Exodos - Destino"
            location = ROOT
            sub_unit = exodos_marker
            save_scope_as = exodos_dest_scope
        }
        scope:exodos_dest_scope = {
            set_variable = { name = exodos_unit_destination  value = 1 }
        }
    }
}
```

> `scope = province` — ROOT es el territorio seleccionado en el panel de tácticas.
> `saved_scopes = { player }` — necesario para acceder al estado del país desde scope province.
> `is_shown` filtra visibilidad. `is_valid` habilita o pone en gris.
> Botón A spawna en el territorio clickeado — inmóvil por `movement_speed = 0`.
> Botón B spawna en el territorio clickeado — inmóvil en v4 por `movement_speed = 0`.

### Guards cruzados en los 4 confirms — patrón correcto (v4 corregido)

Los 4 confirms deben incluir en su `allow` los dos guards siguientes. Sin ellos el estado se puede corromper
(operación activa + optimize_active flotando simultáneamente, o viceversa).

**confirm_gather y confirm_distribute — allow completo:**
```pdxscript
allow = {
    is_ai = no
    NOT = { has_variable = exodos_operation_active }
    NOT = { has_variable = exodos_optimize_active }
    any_unit = { has_variable = exodos_unit_anchor }
    any_unit = {
        has_variable = exodos_unit_anchor
        unit_location = { area = { all_area_province = { owner = ROOT } } }
    }
    treasury >= 1000
    manpower >= 5
    tyranny <= 90
}
```

**confirm_transfer — allow completo:**
```pdxscript
allow = {
    is_ai = no
    NOT = { has_variable = exodos_operation_active }
    NOT = { has_variable = exodos_optimize_active }
    any_unit = { has_variable = exodos_unit_anchor }
    any_unit = { has_variable = exodos_unit_destination }
    any_unit = { has_variable = exodos_unit_anchor  unit_location = { owner = ROOT } }
    any_unit = { has_variable = exodos_unit_destination  unit_location = { owner = ROOT } }
    treasury >= 2000
    manpower >= 10
    tyranny <= 80
}
```

**confirm_optimize — allow completo:**
```pdxscript
allow = {
    is_ai = no
    NOT = { has_variable = exodos_operation_active }
    NOT = { has_variable = exodos_optimize_active }
    any_unit = { has_variable = exodos_unit_anchor }
    any_unit = {
        has_variable = exodos_unit_anchor
        unit_location = { area = { all_area_province = { owner = ROOT } } }
    }
}
```
> `confirm_optimize` no tiene costos — esos van en las decisiones de rango.

## 9.2 exodos_on_action.txt — Diseño v4

**Patrón correcto — chequeo de ancla destruida (un solo bloque):**
```pdxscript
# CORRECTO — v4
if = {
    limit = { NOT = { any_unit = { has_variable = exodos_unit_anchor } } }
    trigger_event = { id = exodos.1 }
}
```

**Estructura completa del bloque de chequeos de error — v4:**
```pdxscript
monthly_country_pulse = {
    effect = {
        if = {
            limit = {
                is_ai = no
                has_variable = exodos_operation_active
            }

            # 1. Ancla destruida
            if = {
                limit = { NOT = { any_unit = { has_variable = exodos_unit_anchor } } }
                trigger_event = { id = exodos.1 }
            }
            # 2. Destino destruido (solo Transfer)
            else_if = {
                limit = {
                    has_variable = exodos_transfer_active
                    NOT = { any_unit = { has_variable = exodos_unit_destination } }
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
            # 5. Área no 100% propia (Optimize)
            else_if = {
                limit = {
                    has_variable = exodos_optimize_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }
            # 6. Área no 100% propia (Gather)
            else_if = {
                limit = {
                    has_variable = exodos_gather_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }
            # 7. Área no 100% propia (Distribute)
            else_if = {
                limit = {
                    has_variable = exodos_distribute_active
                    var:exodos_anchor_province = {
                        area = { any_area_province = { NOT = { owner = ROOT } } }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            else = {
                # Bloque de operaciones — igual que v3
                # Ver Sección 8.7 para el código completo
            }
        }
    }
}
```

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 10 — LOCALIZACIÓN v4 — REESCRITA COMPLETAMENTE
# ══════════════════════════════════════════════════════════

## 10.1 Reglas de localización v4

- Los confirms aparecen **siempre en gris**. El tooltip explica exactamente qué falta.
- El jugador **no posiciona ni mueve** nada. Spawna desde el panel de tácticas de provincia.
  No usar "posicioná", "mové", "desplazá" ni variantes.
- No escribir el costo — el engine lo muestra automáticamente.
- Advertencias críticas e irreversibles en MAYÚSCULAS.
- Textos cortos y directos.

## 10.2 Textos ES — v4

```yaml
l_spanish:
 # Botones scripted_gui
 exodos_spawn_anchor_button:0 "Exodos: Crear Ancla"
 exodos_spawn_destination_button:0 "Exodos: Crear Destino"

 # Confirms — siempre visibles, en gris hasta tener ancla
 exodos_confirm_gather:0 "Exodos: Concentración"
 exodos_confirm_gather_desc:0 "Concentra toda la población del área en el territorio ancla. Para habilitar esta operación, creá el ancla desde el panel de tácticas de provincia en el territorio de destino."
 exodos_confirm_distribute:0 "Exodos: Distribución"
 exodos_confirm_distribute_desc:0 "Distribuye la población del territorio ancla hacia todo el área. Para habilitar esta operación, creá el ancla desde el panel de tácticas de provincia en el territorio a vaciar."
 exodos_confirm_optimize:0 "Exodos: Optimizar"
 exodos_confirm_optimize_desc:0 "Redistribuye los pops del área de manera óptima para conversión religiosa y asimilación cultural. Para habilitar esta operación, creá el ancla desde el panel de tácticas en la ciudad principal del área. SIN COSTO — abre el menú de rangos."
 exodos_confirm_transfer:0 "Exodos: Transferencia"
 exodos_confirm_transfer_desc:0 "Transfiere pops entre dos territorios durante diez meses. Para habilitar, creá el ancla en el territorio origen y el destino en el territorio destino desde el panel de tácticas de provincia."

 # Decisiones de rango — Optimize
 exodos_opt_range_03:0 "Optimizar — Rango 3 (45–58 pops)"
 exodos_opt_range_04:0 "Optimizar — Rango 4 (59–73 pops)"
 exodos_opt_range_05:0 "Optimizar — Rango 5 (74–88 pops)"
 exodos_opt_range_06:0 "Optimizar — Rango 6 (89–103 pops)"
 exodos_opt_range_07:0 "Optimizar — Rango 7 (104–117 pops)"
 exodos_opt_range_08:0 "Optimizar — Rango 8 (118–132 pops)"
 exodos_opt_range_09:0 "Optimizar — Rango 9 (133–147 pops)"
 exodos_opt_range_10:0 "Optimizar — Rango 10 (148–162 pops)"
 exodos_opt_range_11:0 "Optimizar — Rango 11 (163–177 pops)"
 exodos_opt_range_12:0 "Optimizar — Rango 12 (177–192 pops)"
 exodos_opt_range_13:0 "Optimizar — Rango 13 (193–209 pops)"
 exodos_opt_range_14:0 "Optimizar — Rango 14 (210–223 pops)"
 exodos_opt_range_15:0 "Optimizar — Rango 15 (224–238 pops)"
 exodos_opt_range_16:0 "Optimizar — Rango 16 (239–254 pops)"
 exodos_opt_range_17:0 "Optimizar — Rango 17 (255–268 pops)"
 exodos_opt_range_18:0 "Optimizar — Rango 18 (269–284 pops)"
 exodos_opt_range_19:0 "Optimizar — Rango 19 (285–300 pops)"
 exodos_opt_range_03_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_04_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_05_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_06_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_07_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_08_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_09_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_10_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_11_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_12_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_13_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_14_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_15_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_16_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_17_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_18_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."
 exodos_opt_range_19_desc:0 "Verificá el total de pops del área antes de confirmar. ESTA ACCIÓN NO PUEDE DESHACERSE NI REEMBOLSARSE Y PUEDE TARDAR VARIOS MESES. GUARDÁ LA PARTIDA Y HACÉ UNA COPIA DE RESPALDO."

 # Cancel
 exodos_cancel_all:0 "Cancelar Todo"
 exodos_cancel_all_desc:0 "Rescinde todos los decretos activos del estado. Limpia toda operación en curso y cualquier estado residual de instalaciones anteriores del mod. Los costos ya pagados no serán reembolsados. Usar como primer paso al migrar desde una instalación anterior."

 # Evento de fallo
 exodos.1.t:0 "El Exodo Ha Fracasado"
 exodos.1.d:0 "El movimiento del pueblo ha llegado a un abrupto fin. Los esfuerzos del estado han sido en vano."
 exodos.1.ok:0 "Que así sea."

 # Heredero del Rival
 exodos_spawn_rival_son:0 "Heredero del Rival — Hijo"
 exodos_spawn_rival_son_desc:0 "El rival deja un heredero varón. Hereda los rasgos dinásticos del padre y de la madre."
 exodos_spawn_rival_daughter:0 "Heredero del Rival — Hija"
 exodos_spawn_rival_daughter_desc:0 "El rival deja una heredera. Hereda los rasgos dinásticos del padre y de la madre."

 # Custom tooltips
 exodos_tt_rival_unique:0 "Requiere exactamente un rival varón, mayor de 16 años, de tu nación."
 exodos_tt_area_owner:0 "El área completa debe estar bajo la autoridad del estado. (Área no controlada en su totalidad)"
```

## 10.3 Textos EN — v4

```yaml
l_english:
 # Scripted GUI buttons
 exodos_spawn_anchor_button:0 "Exodos: Spawn Anchor"
 exodos_spawn_destination_button:0 "Exodos: Spawn Destination"

 # Confirms — always visible, grayed until anchor exists
 exodos_confirm_gather:0 "Exodos: Concentrate"
 exodos_confirm_gather_desc:0 "Concentrates all population in the area toward the anchor territory. To enable, spawn the anchor from the tactics panel in the destination territory."
 exodos_confirm_distribute:0 "Exodos: Distribute"
 exodos_confirm_distribute_desc:0 "Distributes population from the anchor territory across the entire area. To enable, spawn the anchor from the tactics panel in the territory to empty."
 exodos_confirm_optimize:0 "Exodos: Optimize"
 exodos_confirm_optimize_desc:0 "Optimally redistributes the area's pops for religious conversion and cultural assimilation. To enable, spawn the anchor from the tactics panel in the main city of the area. NO COST — opens the range selection menu."
 exodos_confirm_transfer:0 "Exodos: Transfer"
 exodos_confirm_transfer_desc:0 "Transfers pops between two territories over ten months. To enable, spawn the anchor in the origin territory and the destination in the target territory from the tactics panel."

 # Range decisions — Optimize
 exodos_opt_range_03:0 "Optimize — Range 3 (45–58 pops)"
 exodos_opt_range_04:0 "Optimize — Range 4 (59–73 pops)"
 exodos_opt_range_05:0 "Optimize — Range 5 (74–88 pops)"
 exodos_opt_range_06:0 "Optimize — Range 6 (89–103 pops)"
 exodos_opt_range_07:0 "Optimize — Range 7 (104–117 pops)"
 exodos_opt_range_08:0 "Optimize — Range 8 (118–132 pops)"
 exodos_opt_range_09:0 "Optimize — Range 9 (133–147 pops)"
 exodos_opt_range_10:0 "Optimize — Range 10 (148–162 pops)"
 exodos_opt_range_11:0 "Optimize — Range 11 (163–176 pops)"
 exodos_opt_range_12:0 "Optimize — Range 12 (177–192 pops)"
 exodos_opt_range_13:0 "Optimize — Range 13 (193–209 pops)"
 exodos_opt_range_14:0 "Optimize — Range 14 (210–223 pops)"
 exodos_opt_range_15:0 "Optimize — Range 15 (224–238 pops)"
 exodos_opt_range_16:0 "Optimize — Range 16 (239–254 pops)"
 exodos_opt_range_17:0 "Optimize — Range 17 (255–268 pops)"
 exodos_opt_range_18:0 "Optimize — Range 18 (269–284 pops)"
 exodos_opt_range_19:0 "Optimize — Range 19 (285–300 pops)"
 exodos_opt_range_03_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_04_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_05_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_06_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_07_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_08_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_09_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_10_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_11_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_12_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_13_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_14_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_15_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_16_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_17_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_18_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."
 exodos_opt_range_19_desc:0 "Verify the area's total pop count before confirming. THIS ACTION CANNOT BE UNDONE OR REFUNDED AND MAY TAKE SEVERAL MONTHS. MAKE A SAVE AND KEEP A BACKUP."

 # Cancel
 exodos_cancel_all:0 "Cancel All"
 exodos_cancel_all_desc:0 "Rescinds all active state decrees. Clears any ongoing operation and any residual state from previous mod installations. Costs already paid will not be refunded. Use as a first step when migrating from a previous installation."

 # Failure event
 exodos.1.t:0 "The Exodos Has Failed"
 exodos.1.d:0 "The movement of the people has been brought to an abrupt end. The state's efforts have come to nothing."
 exodos.1.ok:0 "So be it."

 # Rival Heir
 exodos_spawn_rival_son:0 "Rival Heir — Son"
 exodos_spawn_rival_son_desc:0 "The rival leaves a male heir. Inherits dynastic traits from both father and mother."
 exodos_spawn_rival_daughter:0 "Rival Heir — Daughter"
 exodos_spawn_rival_daughter_desc:0 "The rival leaves a female heir. Inherits dynastic traits from both father and mother."

 # Custom tooltips
 exodos_tt_rival_unique:0 "Requires exactly one rival, male, aged 16 or older, from your nation."
 exodos_tt_area_owner:0 "The entire area must be under the authority of the state. (Area not fully controlled)"
```

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 11 — CANCEL_ALL EXHAUSTIVO — v4
# ══════════════════════════════════════════════════════════

`exodos_cancel_all` limpia absolutamente todo — estado actual de v4 más variables legacy
de v3 y versiones anteriores. El jugador puede migrar desde cualquier versión anterior.

```pdxscript
exodos_cancel_all = {
    potential = { is_ai = no }
    highlight = { scope:province = { always = yes } }
    allow = { always = yes }
    effect = {

        # ── VARIABLES DE PAÍS — v4 ────────────────────────────────
        remove_variable = exodos_operation_active
        remove_variable = exodos_gather_active
        remove_variable = exodos_distribute_active
        remove_variable = exodos_transfer_active
        remove_variable = exodos_optimize_active
        remove_variable = exodos_optimize_gather_done
        remove_variable = exodos_optimize_count
        remove_variable = exodos_anchor_province
        remove_variable = exodos_destination_province
        remove_variable = exodos_pulse_counter

        # ── VARIABLES LEGACY — v3 y anteriores ───────────────────
        remove_variable = exodos_gather_pending
        remove_variable = exodos_distribute_pending
        remove_variable = exodos_transfer_pending
        remove_variable = exodos_optimize_pending

        # ── VARIABLES ONE-SHOT ────────────────────────────────────
        # NOTA: tgl_purchased y bom_ego_sum_X_used NO se limpian aquí
        # cancel_all no debe resetear one-shots — son decisiones del jugador

        # ── SLAVE DISTRIBUTOR (EN DESARROLLO) ────────────────────
        # Cuando se implemente, agregar aquí:
        # remove_variable = exodos_slave_dist_pending
        # remove_variable = exodos_slave_dist_active
        # remove_variable = exodos_slave_dist_count
        # remove_variable = exodos_slave_dist_gather_done
        # Y en el bloque de unidades: has_variable = exodos_unit_slave_dist

        # ── VARIABLES DE PROVINCE ─────────────────────────────────
        every_owned_province = {
            limit = {
                OR = {
                    has_variable = exodos_is_anchor
                    has_variable = exodos_is_destination
                }
            }
            remove_variable = exodos_is_anchor
            remove_variable = exodos_is_destination
        }

        # ── UNIDADES — v4 (con limit obligatorio) ─────────────────
        every_unit = {
            limit = {
                OR = {
                    has_variable = exodos_unit_anchor
                    has_variable = exodos_unit_destination
                }
            }
            destroy_unit = yes
        }

        # ── UNIDADES — legacy v3 y anteriores ────────────────────
        every_unit = {
            limit = {
                OR = {
                    has_variable = exodos_unit_concentrate
                    has_variable = exodos_unit_distribute
                    has_variable = exodos_unit_optimize
                    has_variable = exodos_unit_transfer_origin
                    has_variable = exodos_unit_transfer_dest
                }
            }
            destroy_unit = yes
        }
    }
    ai_will_do = { factor = 0 }
}
```

> ⚠ Verificar contra archivos fuente si `remove_variable` de variable inexistente
> genera error en log. Si lo hace, envolver en `limit = { has_variable = X }`.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 12 — OPTIMIZADOR PROVINCIAL — REFERENCIA
# ══════════════════════════════════════════════════════════

El optimizador es una herramienta HTML separada del mod. El jugador la abre en el
navegador para calcular la distribución óptima de pops antes de elegir el rango.

**Parámetros del optimizador que generan los 17 counts:**
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

**Fix pendiente en el optimizador (baja prioridad):**
`calcPlan` — usar `Math.ceil(switchMonth)` y `Math.floor` en los pops completados.
No implementar salvo pedido explícito del usuario.

Para los cálculos completos y el código fuente del optimizador: ver su backup dedicado.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 13 — PENDIENTES — ORDEN DE PASOS — v4
# ══════════════════════════════════════════════════════════

Seguir este orden exacto. No saltear pasos ni reordenar sin pedido explícito del usuario.

| Paso | Tarea | Archivo | Notas |
|---|---|---|---|
| ✓ 1 | Codear `exodos_scripted_effects.txt` | exodos_scripted_effects.txt | Actualizar variables de unidad, agregar unit_anchor y unit_destination al cleanup, mantener legacy |
| ✓ 2 | Codear `exodos_units.txt` | exodos_units.txt | Agregar `exodos_anchor` con `movement_speed = 0` |
| ✓ 3 | Codear `exodos_scripted_guis.txt` | exodos_scripted_guis.txt | NUEVO — ver Sección 9.1 |
| ✓ 4 | Codear `exodos_decisions_gather_distribute.txt` | exodos_decisions_gather_distribute.txt | Eliminar activates, actualizar confirms — sin is_moving, sin rival, siempre visibles. Guards cruzados corregidos (BUG 1). |
| ✓ 5 | Codear `exodos_decisions_transfer.txt` | exodos_decisions_transfer.txt | Eliminar activate, actualizar confirm. Guards cruzados corregidos (BUG 3). |
| ✓ 6 | Codear `exodos_decisions_optimize.txt` | exodos_decisions_optimize.txt | Eliminar activate, confirm sin costo, 17 rangos cobran el costo. Guards cruzados corregidos (BUG 2). |
| ✓ 7 | Codear `exodos_on_action.txt` | exodos_on_action.txt | Actualizar chequeos — ver Sección 9.2 |
| ✓ 8 | Codear `exodos_decisions_cancel.txt` | exodos_decisions_cancel.txt | Cancel_all exhaustivo — ver Sección 11 |
| ✓ 9 | Codear localización ES y EN | exodos_l_spanish.yml / exodos_l_english.yml | Ver Sección 10 |
| ✓ 10 | Generar zip con BOM validado | mod_pack_IRAM_v4.zip | Ejecutar `build_mods.py` → renombrar |

**✓ SECCIÓN 13 CERRADA — todos los pasos de v4 completados.**

**Archivos sin cambios — copiar tal cual desde v3:**
`exodos_decisions_rival_heir.txt`, `exodos_decisions_bom.txt`, `exodos_decisions_bom_ego_sum.txt`,
`exodos_decisions_tgl.txt`, `exodos_decisions_tlv.txt`, `exodos_events.txt`, `tlv_events.txt`,
`bom_l_english.yml`, `bom_l_spanish.yml`, `bom_l_english_ego_sum.yml`, `bom_l_spanish_ego_sum.yml`,
`tlv_l_english.yml`, `tlv_l_spanish.yml`, `tgl_l_english.yml`, `tgl_l_spanish.yml`

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 14 — HISTORIAL COMPLETO
# ══════════════════════════════════════════════════════════

## Resumen ejecutivo por versión

| Versión | Nombre | Característica clave | Estado |
|---|---|---|---|
| **IRAM v1** | Drago Mod Pack Estable v1.3.5 | Spawn en `capital_scope`, `war=no` obligatorio, sin rival | ✅ Histórico cerrado |
| **IRAM v2** | Drago Mod Pack ALT v1.3 | Spawn en posición del rival, `war=no` eliminado, BOM absorbe TLV kill + agrega IHA | ✅ Histórico cerrado |
| **IRAM v3** | IRAM v1.13 (mod_pack_IRAM_15) | Optimize 17 rangos, Heredero del Rival, todo consolidado en un zip, panel de decisiones unificado, Rival Heir | ✅ CERRADO — zip final |
| **IRAM v4** | En desarrollo (mod_pack_IRAM_v4_3) | Panel de tácticas (scripted_gui), sin activates, unidades inmóviles, cancel_all exhaustivo | 🔧 En desarrollo |

## SUPERBACKUP v2.0 — 2026-05-19

- **Sistema de control actualizado a v3.0** — generados `IRAM_PROMPT_MAESTRO_v3_0.md` e `IRAM_INSTRUCCIONES_HUMANO.md`. Reglas R centralizadas en PASO 1, clasificación 🔴🟡🔵, confirmación previa antes de tocar código, formato de entrega estandarizado, protocolo de sesión interrumpida.
- **Dashboard Sección 0.5.0 agregado** — estado de un vistazo con semáforo rápido, actualizable al inicio de cada sesión.
- **Entrada de sesión 2026-05-19 (meta-análisis) en Sección 19** — decisiones de arquitectura del sistema de control, hito de cierre v4 definido.
- **Hito de cierre v4 definido:** Slave Distributor funcionando.
- **Header y footer actualizados** — versión v1.9 → v2.0.

## SUPERBACKUP v1.9 — 2026-05-19

- **Fix Sección 4.4** — tabla de anclas fila count=11 corregida: `163–176` → `163–177` (el cruce 11/12 ya estaba corregido en la tabla de rangos y en la localización, pero no se había propagado a esta tabla)
- **Sección 6 ampliada** — 3 gotchas nuevos extraídos del historial de 135 sesiones: BOM doble en unit types (⚠️), `save_scope_as` fuera de `random_holdings` (💀), `num_of_pops` con mensaje de error exacto del log (⚠️). Entrada existente de `[ ]` en localización actualizada con referencia de sesión.
- **Sección 5.7 (TLV) actualizada** — alternativa a `current_ruler` enlazada desde la advertencia `⚠ TESTEAR`
- **Sección 19.0 agregada** — índice navegable de temas abiertos, actualizable in-place
- **Sección 8-C — timestamps de sincronización** — tabla de fecha de última sincronización por archivo de código
- **Sección 16 completa** — integrado el contenido íntegro de `backup_slave_distributor_v2_1_.md` v2.1: thresholds verificados ingame, modificadores globales de `game.zip`, 5 tiers de distribución, localización cerrada, pseudocódigo del pulso, 4 temas críticos antes de codear
- **Sección 0.4 ampliada** — ERROR 26 (zip con bugs pendientes) y ERROR 27 (`save_scope_as` en `random_holdings`)
- **Prompt Maestro v2.1** — verificación de Sección 21 agregada al checklist de PASO 1

**IRAM v1→v2:** diferencia central es el mecanismo de spawn de Gather/Distribute (capital vs posición rival) y la eliminación de `war=no`. BOM/TLV/TGL son idénticos entre v1 y v2.

**IRAM v2→v3:** incorporación de Optimize (17 rangos), Heredero del Rival, IHA, unificación de archivos en una sola carpeta `exodos/`, builds Python automatizados.

**IRAM v3→v4:** eliminación de los activates (el jugador ya no posiciona unidades manualmente), reemplazo por `scripted_gui` con botones A/B en el panel de tácticas de province. Las unidades pasan de `movement_speed = 5` a `movement_speed = 0`. El flujo es: botón en panel → confirm en panel de decisiones → pulso mensual.

---

- **ERROR 15 implementado en zip** — agregado `NOT = { has_variable = exodos_optimize_active }` al `is_valid` de `exodos_spawn_anchor_button`. Cierra el escenario de corrupción donde el jugador hace `confirm_optimize`, destruye el ancla, y el botón A quedaba válido spawneando una nueva ancla en province distinta a la guardada en `exodos_anchor_province`.
- **ERROR 16 implementado en zip** — agregado `NOT = { has_variable = exodos_operation_active }` al `is_valid` de `exodos_spawn_destination_button`. Cierra el escenario de estado inválido donde el jugador podía spawnear un destino durante una operación activa.
- **Zip actualizado a `mod_pack_IRAM_v4_3.zip`** — contiene ambas correcciones aplicadas.
- **Secciones 0.1, 0.2, 0.4, 0.5 y 2.2 actualizadas** — ERROR 15 y ERROR 16 marcados ✓ CORREGIDO en v4_3.

## SUPERBACKUP v1.5 — 2026-05

- **ERROR 15 agregado a Sección 0.4** — documenta el escenario de corrupción en `exodos_spawn_anchor_button`: si el jugador hace `confirm_optimize` (setea `exodos_optimize_active`) y luego destruye manualmente la unidad ancla antes de elegir un rango, el botón A queda válido (no hay operación activa, no hay ancla), permitiendo spawnear una nueva ancla en province distinta a la guardada en `exodos_anchor_province`. Corrección pendiente en v4_3: agregar `NOT = { has_variable = exodos_optimize_active }` al `is_valid` del botón A.
- **ERROR 16 agregado a Sección 0.4** — documenta el escenario de estado inválido en `exodos_spawn_destination_button`: si hay una operación activa (Gather corriendo) y el ancla existe, el botón B aparece habilitado porque no hay destino. El jugador podría spawnear un destino inútil durante una operación activa; se limpiaría con el siguiente cancel pero es estado innecesario. Corrección pendiente en v4_3: agregar `NOT = { has_variable = exodos_operation_active }` al `is_valid` del botón B.
- **Sección 0.5 actualizada** — nueva fila "Guards en `is_valid` de botones scripted_gui" documentando ambas correcciones pendientes para v4_3.
- **Sección 2.2 actualizada** — dos nuevas filas marcadas `⚠ PENDIENTE v4_3`: guard en botón A y guard en botón B.

## SUPERBACKUP v1.4 — 2026-05

- **BUG corregido en zip — `confirm_optimize` guard faltante:** agregado `NOT = { has_variable = exodos_optimize_active }` al `allow` de `exodos_confirm_optimize`. Era el único de los 4 confirms sin el segundo guard. Todos los confirms tienen ahora ambos guards completos. Zip actualizado a `mod_pack_IRAM_v4_3.zip`.
- **BUG corregido en zip — 17 keys `_desc` huérfanos:** reemplazado el key genérico `exodos_opt_range_desc` por 17 keys individuales `exodos_opt_range_03_desc` … `exodos_opt_range_19_desc` en ambos yml (ES y EN). El engine de IR resuelve descripciones por `<decision_id>_desc` exacto — el key genérico nunca aparecía en pantalla.
- **ERROR 13 agregado a Sección 0.4** — documenta la convención obligatoria de keys `_desc` individuales por decisión. Un key genérico compartido es invisible al engine.
- **ERROR 14 agregado a Sección 0.4** — documenta la excepción de R1 para `exodos_cancel_all`: su `allow = { always = yes }` es intencional, no agregar `is_ai = no` ahí.
- **Sección 0.5 actualizada** — fila de guards cruzados actualizada a "corregido completamente en v4_2".
- **Sección 2.2 actualizada** — fila de guards corregida a v4_2; nueva fila para fix de `_desc` y nueva fila para excepción R1 de `cancel_all`.
- **Secciones de localización (ES y EN) actualizadas** — keys de referencia corregidos de `exodos_opt_range_desc` a los 17 keys `_desc` individuales.
- **Header y referencias de zip actualizados** — de `mod_pack_IRAM_v4.zip` a `mod_pack_IRAM_v4_3.zip`.

## SUPERBACKUP v1.3 — 2026-05

- **Bugs 1–3 corregidos en zip** — `exodos_confirm_gather`, `exodos_confirm_distribute`, `exodos_confirm_transfer` y `exodos_confirm_optimize` ahora incluyen `NOT = { has_variable = exodos_operation_active }` y `NOT = { has_variable = exodos_optimize_active }` en su `allow`. Sin estos guards, una operación podía iniciarse con `exodos_optimize_active` flotando (o viceversa), corrompiendo el estado. Zip renombrado de `mod_pack_v4/` a `mod_pack_IRAM_v4/`.
- **ERROR 12 agregado a Sección 0.4** — documenta el patrón de guards cruzados requerido en los 4 confirms.
- **Sección 0.5 actualizada** — nueva fila "Guards cruzados en allow de confirms" en tabla de diferencias v3 vs v4.
- **Sección 2.2 actualizada** — fix de guards cruzados marcado como ✓ CORREGIDO en v4.
- **Sección 7 actualizada** — `Missing Icon for Modifier: exodos_anchor_*` agregado a tabla de warnings ignorables.
- **Sección 9.1 actualizada** — documentados los `allow` completos y correctos de los 4 confirms con sus guards cruzados.
- **Sección 13 cerrada** — todos los pasos 1–10 marcados ✓. Zip `mod_pack_IRAM_v4.zip` entregado.
- **Header y referencias de zip actualizados** — de `mod_pack_IRAM_12.zip` a `mod_pack_IRAM_v4.zip`.

## SUPERBACKUP v1.2 — 2026-05

- **Rangos de Optimize corregidos** — los 17 rangos en sección 4.4, localización ES y EN (sección 10) actualizados considerando que el Gather deja 1 pop por asentamiento (piso `total_population >= 2`). El count del Distribute es `settPops_óptimo − 1`, no `settPops_óptimo`. Puntos de cruce desplazados 1–6 pops hacia abajo respecto a v1.1. Verificado por búsqueda discreta exhaustiva 45–300. Error máximo: ≤ 4.9m. Rango 19 acepta hasta 7.8m en t=299–300 (aceptable — count=20 no existe).
- **Nueva subsección 4.4 "Mecánica del Gather y resultado del ancla"** — documenta el piso de 1 pop por asentamiento, la fórmula `ancla_final = total − 9×(count+1)`, y la tabla completa de pops del ancla en lo/mid/hi de cada rango. Mínimo del ancla: 9 pops (count=3, total=45). Ningún ancla queda en 0 o negativo.
- **Tabla de rangos marcada CERRADO v1.2.**

## SUPERBACKUP v1.1 — 2026-05

- **Rangos de Optimize corregidos** — el superbackup v1.0 tenía los rangos desplazados (03 = 30–44 en lugar de 45–59, etc.). Corregidos comparando contra la localización del zip `mod_pack_IRAM_12.zip`, que es la fuente de verdad.
- **movement_speed del exodos_marker en v4 unificado a 0** — el backup v2.0.1 indicaba 5 (movible). El diseño final es que ambas unidades sean inmóviles (`movement_speed = 0`). Corregido en tabla 3.5 y 0.5.
- **`exodos_decisions_bom_ego_sum.txt` agregado a tabla de funciones 3.3** — estaba omitido.
- **Slave Distributor documentado** — agregado en tabla de funciones (3.3), tabla de costos (3.4), panel de decisiones (3.7), cancel_all (Sección 11, variables comentadas), y nueva Sección 16 con descripción, estado y archivos involucrados.

## IRAM v3 — mod_pack_IRAM_12.zip — 2026-05

- **Heredero del Rival v1.6** — herencia matrilineal implementada en `exodos_spawn_rival_son`
  y `exodos_spawn_rival_daughter`. `mother = scope:exodos_rival_spouse` con `limit = { exists }`
- Todos los mods unificados en `exodos/` — by_other_means, the_last_vote, the_great_leap como TEST SHELL
- Exodos Optimize: 17 rangos (count=3 a 19) con `else_if` literales
- IHA: Confiscar y Fill the Void implementados en BOM
- `is_ai = no` en `allow` de todos los activates
- `tyranny <= 80` corregido en Transfer activate
- Nombres de unidades en español
- 21 íconos `.dds` eliminados (warnings permanentes e ignorables)

## IRAM v2 — Drago Mod Pack ALT v1.3 — 2026-05

- Spawn en posición del rival (army en command) en lugar de capital
- `war = no` eliminado de todas las operaciones — Exodos operable en guerra
- BOM Kill Ruler movido desde TLV a BOM
- IHA Seize e IHA Fill the Void agregados
- TLV reducido a solo `tlv_confirm`
- Popup de BOM eliminado — solo `exodos.1` y `tlv.2`

## IRAM v1 — Drago Mod Pack Estable v1.3.5 — 2026-05

- Spawn en `capital_scope` para todas las operaciones
- Rival requerido en Gather y Distribute (`in_command = yes`)
- `war = no` obligatorio en Gather, Distribute y Transfer
- `exodos_cancel` ampliado a las 3 operaciones
- `ai_will_do = { factor = 0 }` en todos
- TGL `supported_version = "2.0.*"` corregido
- Documentación unificada creada

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 8-A — CÓDIGO FUENTE COMPLETO — IRAM v1 (Estable v1.3.5)
# ══════════════════════════════════════════════════════════

Zip: `mod___SUPERBACKUP_.zip` | Fecha: 2026-05
Diferencias clave vs v2: spawn en `capital_scope`, `war = no` obligatorio en las 3 operaciones,
sin condición de rival en Gather/Distribute (Transfer tampoco lo tenía), `exodos_cancel` ampliado
a las 3 operaciones. Sin Optimize. Sin Heredero del Rival. BOM/TLV/TGL idénticos a v2.

## 8-A.1 Estructura de archivos v1

```
exodos.mod           ← sin BOM
by_other_means.mod   ← sin BOM
the_last_vote.mod    ← sin BOM
the_great_leap.mod   ← sin BOM
exodos/
├── descriptor.mod
├── common/
│   ├── units/exodos_units.txt
│   ├── scripted_effects/exodos_scripted_effects.txt
│   └── on_action/exodos_on_action.txt
├── events/exodos_events.txt
├── decisions/exodos_decisions.txt        ← un solo archivo, 3 operaciones + cancel
└── localization/
    ├── english/exodos_l_english.yml
    └── spanish/exodos_l_spanish.yml
by_other_means/
├── descriptor.mod
├── events/bom_events.txt
├── decisions/bom_decisions.txt
├── decisions/bom_decisions_ego_sum.txt
└── localization/english|spanish/
the_last_vote/
├── descriptor.mod
├── events/tlv_events.txt
├── decisions/tlv_decisions.txt
└── localization/english|spanish/
the_great_leap/
├── descriptor.mod
└── localization/english|spanish/
```

## 8-A.2 Diferencias de código Exodos v1 vs v3

| Aspecto | v1 | v3 |
|---|---|---|
| Spawn Gather/Distribute | `location = capital_scope` | `location = <posición rival>` |
| `war = no` | En allow de las 3 operaciones | Eliminado |
| Rival en Gather/Distribute | No requerido | Requerido (1 exacto, in_command) |
| Optimize | No existe | 17 rangos |
| `exodos_cancel` | Cubre las 3 operaciones | Ídem (en v3 es `exodos_cancel_all`) |
| Nombres unidades | Español (Concentrar, Distribuir, Origen, Destino) | Igual |
| `count` por while Gather | 20 por fuente | 20 por fuente |
| `count` por while Distribute | 10 por destino | 10 por destino |
| Piso fuentes Gather | `total_population >= 2` | Igual |
| Piso ancla Distribute | `total_population >= 30` | Igual (v3 ALT) |

**Nota sobre `exodos_cancel` v1:** en v1 `exodos_cancel` cubría las 3 operaciones (Transfer + Gather + Distribute). En v3 se renombró a `exodos_cancel_all` y se expandió para limpiar también Optimize y variables legacy. El código de `exodos_cleanup_effect` de v1 es idéntico en lógica al de v3 salvo por la ausencia de variables de Optimize.

## 8-A.3 exodos_scripted_effects.txt (v1)

```pdxscript
exodos_cleanup_effect = {

    # Variables de operacion
    remove_variable = exodos_operation_active
    remove_variable = exodos_gather_active
    remove_variable = exodos_transfer_active
    remove_variable = exodos_distribute_active
    remove_variable = exodos_transfer_pending
    remove_variable = exodos_gather_pending
    remove_variable = exodos_distribute_pending
    remove_variable = exodos_anchor_province
    remove_variable = exodos_destination_province
    remove_variable = exodos_pulse_counter

    # Limpiar variables de province
    every_owned_province = {
        limit = {
            OR = {
                has_variable = exodos_is_anchor
                has_variable = exodos_is_destination
            }
        }
        remove_variable = exodos_is_anchor
        remove_variable = exodos_is_destination
    }

    # Disolver unidades Exodos
    every_unit = {
        limit = {
            OR = {
                has_variable = exodos_unit_transfer_origin
                has_variable = exodos_unit_transfer_dest
                has_variable = exodos_unit_concentrate
                has_variable = exodos_unit_distribute
            }
        }
        destroy_unit = yes
    }
}
```

## 8-A.4 Activate v1 — patrón Gather (spawn en capital, war=no, sin rival)

```pdxscript
exodos_activate_gather = {
    potential = {
        is_ai = no
        NOT = { has_variable = exodos_transfer_pending }
        NOT = { has_variable = exodos_gather_pending }
        NOT = { has_variable = exodos_distribute_pending }
        NOT = { has_variable = exodos_operation_active }
    }
    highlight = { scope:province = { always = yes } }
    allow = {
        is_ai = no
        custom_tooltip = exodos_tt_no_war
        war = no
        tyranny <= 90
    }
    effect = {
        create_unit = {
            name = "Exodos - Concentrar"
            location = capital_scope
            sub_unit = exodos_marker
            save_scope_as = exodos_unit_scope
        }
        scope:exodos_unit_scope = {
            set_variable = { name = exodos_unit_concentrate value = 1 }
        }
        set_variable = { name = exodos_gather_pending value = 1 }
    }
    ai_will_do = { factor = 0 }
}
```

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 8-B — CÓDIGO FUENTE COMPLETO — IRAM v2 (ALT v1.3)
# ══════════════════════════════════════════════════════════

Zip: `mod_alt___SUPERBACKUP_.zip` | Fecha: 2026-05
Diferencias clave vs v1: spawn en posición del rival (army en command), `war = no` eliminado
de todas las operaciones, Gather y Distribute requieren exactamente 1 rival en `in_command`.
BOM absorbe `bom_kill_ruler` desde TLV. IHA Confiscar e IHA Fill the Void agregados.
TLV reducido a solo `tlv_confirm`. Sin Optimize. Sin Heredero del Rival.

## 8-B.1 Diferencias de código Exodos v2 (ALT) vs v1

| Aspecto | v1 | v2 ALT |
|---|---|---|
| Spawn Gather/Distribute | `capital_scope` | Posición del ejército del rival |
| `war = no` | Obligatorio en las 3 | **Eliminado** — operable en guerra |
| Rival en Gather/Distribute | No requerido | **1 exacto, in_command=yes, employer=ROOT** |
| Nombres unidades EN | "Exodos - Concentrate" | Igual |
| Nombres unidades ES | "Exodos - Concentrar" | Igual |
| BOM Kill Ruler | En TLV | **Movido a BOM** |
| IHA Confiscar | No existe | **Nuevo** |
| IHA Fill the Void | No existe | **Nuevo** |

## 8-B.2 Activate v2 — patrón Gather (spawn en posición rival)

```pdxscript
exodos_activate_gather = {
    potential = {
        is_ai = no
        NOT = { has_variable = exodos_transfer_pending }
        NOT = { has_variable = exodos_gather_pending }
        NOT = { has_variable = exodos_distribute_pending }
        NOT = { has_variable = exodos_operation_active }
        any_character = {
            is_ruler = yes
            num_of_rivals >= 1
            NOT = { num_of_rivals >= 2 }
            any_rival = {
                employer = ROOT
                in_command = yes
            }
        }
    }
    highlight = { scope:province = { always = yes } }
    allow = {
        is_ai = no
        custom_tooltip = exodos_tt_rival_commander
        any_character = {
            is_ruler = yes
            num_of_rivals >= 1
            NOT = { num_of_rivals >= 2 }
            any_rival = { employer = ROOT  in_command = yes }
        }
        tyranny <= 90
    }
    effect = {
        every_character = {
            limit = { is_ruler = yes }
            every_rival = {
                limit = { employer = ROOT  in_command = yes }
                save_scope_as = exodos_rival
            }
        }
        random_unit = {
            limit = { commander = scope:exodos_rival }
            unit_location = { save_scope_as = exodos_rival_loc }
        }
        create_unit = {
            name = "Exodos - Concentrate"
            location = scope:exodos_rival_loc
            sub_unit = exodos_marker
            save_scope_as = exodos_unit_scope
        }
        scope:exodos_unit_scope = {
            set_variable = { name = exodos_unit_concentrate value = 1 }
        }
        set_variable = { name = exodos_gather_pending value = 1 }
    }
    ai_will_do = { factor = 0 }
}
```

**Nota clave:** `save_scope_as = exodos_rival` y `save_scope_as = exodos_rival_loc` **no persisten
entre ticks** — no necesitan cleanup en `exodos_cleanup_effect`. Son scopes temporales del mismo
efecto. Esto está confirmado en IR 2.0.4.

## 8-B.3 Confirm v2 — sin war=no, igual en lo demás que v1/v3

El `exodos_confirm_gather` de v2 es idéntico al de v3 **excepto** que no tiene el check
`war = no` en su `allow`. Todo lo demás (cobro, guardado de province, flags) es igual.

---

## 15.1 Tabla de equivalencia económica

✓ **ENCONTRADA Y CERRADA en v1.6** — ver Sección 17 para el estudio completo.

El estudio fue localizado en el Historial Agente 4, Sesión 05 ("Equivalencia entre manpower y oro").
Los valores de la Sección 17 son los valores canónicos del proyecto y justifican todos los costos
del ecosistema (Gather/Distribute: 1000 oro, Transfer: 2000 oro, Optimize rangos: 2000 oro).

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 16 — EXODOS: REPARTIR ESCLAVOS (SLAVE DISTRIBUTOR)
# ══════════════════════════════════════════════════════════

## 16.0 — Reglas de trabajo para esta función

Estas reglas son obligatorias antes de escribir cualquier código del Slave Distributor:

1. Los thresholds de la sección 16.3 fueron verificados **ingame por el usuario con capturas**. Son verdad absoluta — no recalcular, no reemplazar con valores de memoria ni de la wiki.
2. Los modificadores globales de la sección 16.4 fueron extraídos directamente de `game.zip`. Son verdad absoluta.
3. La wiki (`wiki_imperator.txt`) tiene errores de interpretación sobre esta mecánica — NO usarla como fuente para los thresholds. Solo para contexto general.
4. Las decisiones marcadas como **CERRADO** no se reabren salvo pedido explícito del usuario.
5. El mod opera sobre IR 2.0.4. No asumir compatibilidad con otras versiones.
6. Ciudades y metrópolis son siempre el ancla — **nunca son destino** del Slave Distributor.
7. Misiones, eventos y exclusivas de nación (ej: ANU) **no se consideran** para el diseño de los tiers. Solo modificadores genéricos disponibles para cualquier jugador.
8. El diseño de los tiers está **CERRADO**. No recalcular salvo pedido explícito del usuario con nuevas capturas.
9. La localización está **CERRADA**. Ver sección 16.6.
10. Seguir las convenciones del ecosistema IRAM en todo momento — ver sección 16.7.

## 16.1 — Archivos necesarios para continuar el desarrollo

| Archivo | Por qué es necesario |
|---|---|
| `IRAM_SUPERBACKUP_v2_0.md` | **Este documento** — fuente de verdad del módulo |
| `mod_pack_IRAM_v4_3.zip` | Código fuente actual del mod — base a modificar |
| `game.zip` | Engine IR 2.0.4 — verificar triggers y sintaxis si hay dudas |

Los siguientes archivos son opcionales (solo si surge una duda específica):

| Archivo | Cuándo pedirlo |
|---|---|
| `wiki_imperator.txt` | Solo para contexto general — NO para thresholds de slaves |

## 16.2 Estado actual

| Item | Estado |
|---|---|
| Versión del módulo | v0.2 |
| Diseño de thresholds | **CERRADO** — verificados ingame con capturas (sección 16.3) |
| Diseño de modificadores globales | **CERRADO** — extraídos de `game.zip` (sección 16.4) |
| Diseño de los 5 tiers | **CERRADO** (sección 16.5) |
| Localización ES y EN | **CERRADA** (sección 16.6) |
| Implementación (código) | **PENDIENTE** — no se escribió código |
| 4 temas críticos antes de codear | **ABIERTOS** — ver Sección 16.8 (URGENTE) |

## 16.2b Posición en el ecosistema

**Posición en el flujo del ecosistema:**
```
1. GATHER / OPTIMIZE  → concentra pops en el ancla, distribuye para conversión/asimilación
2. [tiempo — conversión y asimilación ocurren]
3. REPARTIR ESCLAVOS  → reúne slaves de los asentamientos → los reparte según tier y building
                        para maximizar la producción de trade goods (pasar de 1 a 2 goods)
```

**Premisa de partida:** todos los territorios del área ya producen 1 trade good. El objetivo es llevarlos a **2 trade goods** (surplus), que es lo que habilita rutas de comercio de exportación. No se diseña para llegar a 3 o más.

**El ancla:** la ciudad o metrópolis del área. Es siempre el territorio desde donde se reparten los slaves. **Nunca es destino** — el Slave Distributor no toca los pops del ancla, solo los usa como reservorio.

## 16.3 Thresholds verificados ingame — verdad absoluta

> ⚠️ Estos valores fueron confirmados por el usuario con capturas ingame. Son la verdad absoluta para el diseño de los tiers. No recalcular.

**Configuración de partida del usuario (referencia):**
- Roma, dictadura (tipo monarquía)
- Todas las techs genéricas activas (incluyendo inv cívica `global_goods_from_slaves_inv` −1)
- Ley Roma activa (−2 global)
- Total modificadores globales activos: **−3**

**Slaves necesarios para pasar de 1 a 2 trade goods** (con la configuración del usuario, −3 modificadores globales):

| Tipo de asentamiento | Slaves necesarios para 2do good |
|---|---|
| Con Mina o Asentamiento Agrícola | **9** |
| Otros (sin building o con Finca de Esclavos) | **14** |

Estos son los valores del **tier 2** en la tabla de la sección 16.5.

### Mecánica del engine — base teórica (extraída de game.zip)

> ⚠️ Esta sección es base teórica. Los valores prácticos verificados ingame (sección 16.3 arriba) son los que mandan.

```
NTrade = {
    SLAVE_POPS_TO_PRODUCE_EXTRA = 20   # slaves adicionales para pasar de 1 a 2 goods
    MINIMUM_SLAVES_PER_GOOD = 3        # base mínima antes de modificadores
}
```

Buildings con `local_goods_from_slaves` (solo asentamientos):

| Building | local_goods_from_slaves | Notas |
|---|---|---|
| `slave_mine_building` (Mina) | −5 | Solo asentamientos con trade good mineable |
| `basic_settlement_infratructure_building` (Asentamiento Agrícola) | −5 | Solo asentamientos con trade good de comida |
| `foundry_building` (Fundición) | −4 | Solo ciudades — **irrelevante, el ancla no es destino** |
| `latifundia_building` (Finca de Esclavos) | **0** | No afecta goods_from_slaves |

## 16.4 Modificadores globales genéricos — fuente: game.zip

> Solo se consideran modificadores genéricos disponibles para cualquier jugador. Misiones, exclusivas de nación y eventos están excluidos del diseño.

| Fuente | Archivo fuente | Valor | Tipo de gobierno |
|---|---|---|---|
| Inv cívica `global_goods_from_slaves_inv` | `common/inventions/00_civic_inventions.txt` | −1 | Todos |
| Ley Roma (civic_tech ≥ 12) | `common/laws/00_rome.txt` | −2 | Roma/Monarquía |
| Ley República (equivalente) | `common/laws/00_republic.txt` | −2 | República |
| Ley tribal `formalized_industry_law_tribal` | `common/laws/00_tribal.txt` | −1 | Tribal |
| Gran obra tier 4 `gw_effect_slave_work_tier_4` | `common/great_work_effects/00_default.txt` | −1 | Todos |

**Nota:** Los tiers 1, 2 y 3 de la gran obra tienen `global_goods_from_slaves` comentado (`#`) en el código — están desactivados. Solo el tier 4 aplica.

**Máximo acumulable por tipo de gobierno:**

| Gobierno | Modificadores acumulables | Total máximo |
|---|---|---|
| Roma / Monarquía / República | Inv cívica (−1) + Ley (−2) + Gran obra t4 (−1) | **−4** |
| Tribal | Inv cívica (−1) + Ley tribal (−1) + Gran obra t4 (−1) | **−3** |

## 16.5 Tiers de distribución — CERRADO

Cada tier define cuántos slaves se mandan por tipo de asentamiento. El jugador elige el tier que corresponde a sus modificadores globales activos.

| Decisión | Mina / Asentamiento Agrícola | Otros | Modificadores globales activos |
|---|---|---|---|
| `exodos_slave_dist_t1` | **8** | **13** | −4 (inv + ley mon/rep + gran obra t4) |
| `exodos_slave_dist_t2` | **9** | **14** | −3 (inv + ley mon/rep) ← config usuario |
| `exodos_slave_dist_t3` | **10** | **15** | −2 (solo ley) |
| `exodos_slave_dist_t4` | **11** | **16** | −1 (solo inv) |
| `exodos_slave_dist_t5` | **12** | **17** | 0 (ningún modificador) |

**Regla de branching por building:**

```
si has_building = slave_mine_building
    → count = COUNT_MINA_AGRICOLA del tier elegido
si has_building = basic_settlement_infratructure_building
    → count = COUNT_MINA_AGRICOLA del tier elegido
sino (cualquier otro asentamiento, incluyendo los que tienen latifundia)
    → count = COUNT_OTROS del tier elegido
```

La `latifundia_building` cae en "Otros" — no tiene `local_goods_from_slaves` y no modifica el threshold.

## 16.6 Localización — CERRADA

### Decisión de activación

| Clave | Español | Inglés |
|---|---|---|
| `exodos_activate_slave_dist` | `"Exodos: Repartir Esclavos"` | `"Exodos: Distribute Slaves"` |

**Texto descripción (ES):**
```
"Se reuniran todos los esclavos de los asentamientos de la provincia en la ciudad ancla
y luego se distribuiran segun el tier elegido para maximizar la produccion de trade goods.
Recluta o mueve un ejercito o leva bajo el mando del rival del gobernante en cualquier
territorio de la provincia — la unidad marcadora sera generada ahi automaticamente,
usala para marcar tu ciudad principal en la provincia. Podes moverla antes de elegir
la cantidad, el costo de la operacion se cobra en la siguiente decision."
```

**Texto descripción (EN):**
```
"All slaves from the province's settlements will be gathered into the anchor city,
then distributed according to the chosen amount to maximize trade good production.
Raise or move an army or levy under the ruler's rival in any territory of the province
— the marker unit will be generated there automatically, use it to mark your main city
in the province. You may move it before choosing the amount, the operation cost is
charged in the next decision."
```

### Decisiones de tier

| Clave | Español | Inglés |
|---|---|---|
| `exodos_slave_dist_t1` | `"Mina/Asentamiento Agricola: 8 esclavos — Otros: 13 esclavos"` | `"Mine/Farming Settlement: 8 slaves — Other: 13 slaves"` |
| `exodos_slave_dist_t2` | `"Mina/Asentamiento Agricola: 9 esclavos — Otros: 14 esclavos"` | `"Mine/Farming Settlement: 9 slaves — Other: 14 slaves"` |
| `exodos_slave_dist_t3` | `"Mina/Asentamiento Agricola: 10 esclavos — Otros: 15 esclavos"` | `"Mine/Farming Settlement: 10 slaves — Other: 15 slaves"` |
| `exodos_slave_dist_t4` | `"Mina/Asentamiento Agricola: 11 esclavos — Otros: 16 esclavos"` | `"Mine/Farming Settlement: 11 slaves — Other: 16 slaves"` |
| `exodos_slave_dist_t5` | `"Mina/Asentamiento Agricola: 12 esclavos — Otros: 17 esclavos"` | `"Mine/Farming Settlement: 12 slaves — Other: 17 slaves"` |

Los `_desc` de las decisiones de tier replican el mismo texto que Optimize — advertencia de guardado, MAYÚSCULAS para acciones irreversibles. Ver `exodos_opt_range_03_desc` como plantilla exacta.

## 16.7 Convenciones del ecosistema IRAM — obligatorio respetar

1. `is_ai = no` va siempre en `potential` **Y** en `allow`. Sin excepción.
2. No existe `exodos_cancel` particular — solo `exodos_cancel_all`. No agregar cancels particulares.
3. Los costos **no se escriben en los textos de localización** — el engine los muestra automáticamente desde el `effect`.
4. BOM UTF-8 en todos los `.txt` y `.yml`. Sin BOM en los `.mod`.
5. Todo el código nuevo va en el mod `exodos/`.
6. El archivo de decisiones del módulo va en `exodos/decisions/exodos_decisions_slave_dist.txt` (archivo nuevo).
7. El pulso mensual va en `exodos/common/on_action/exodos_on_action.txt` (agregar bloques al existente).
8. La localización va en `exodos/localization/spanish/exodos_l_spanish.yml` y `exodos/localization/english/exodos_l_english.yml` (agregar al existente).
9. El cleanup de variables nuevas va en `exodos/common/scripted_effects/exodos_scripted_effects.txt` (modificar el existente).

### Patrón de scope del pulso mensual (referencia de Optimize)

El patrón verificado y funcional para iterar territorios del área desde el ancla es:

```pdxscript
var:exodos_anchor_province = {
    save_scope_as = exodos_origin
    area = {
        every_area_province = {
            limit = {
                owner = ROOT
                NOT = { has_variable = exodos_is_anchor }
            }
            save_scope_as = exodos_dist_target
            # lógica de distribución acá
        }
    }
}
```

Para el Gather (reunir en el ancla), el patrón es:

```pdxscript
var:exodos_anchor_province = {
    save_scope_as = exodos_dest
    area = {
        every_area_province = {
            limit = {
                owner = ROOT
                total_population >= 2
                NOT = { has_variable = exodos_is_anchor }
            }
            while = {
                count = 30
                limit = { total_population >= 2 }
                random_pops_in_province = {
                    move_pop = scope:exodos_dest
                }
            }
        }
    }
}
```

**Para el Slave Distributor**, el Gather filtra por `pop_type = slaves` y el corte es cuando los asentamientos no-ancla tienen menos de 2 slaves — TEMA 1 pendiente de resolver (ver sección 16.8).

## 16.8 — Temas críticos antes de codear (URGENTE)

Estos temas deben resolverse **antes de escribir cualquier línea de código**. Presentar al usuario en orden y esperar respuesta a cada uno.

### TEMA 1 — Condición de corte del Gather ⚠️

**Problema:** En Optimize, el Gather para cuando `total_population < 2` en los no-ancla. Acá solo movemos slaves. Si el ancla tiene otros tipos de pops (nobles, freemen después de la asimilación), `total_population` siempre va a ser ≥ 2 aunque no queden slaves.

**Opciones:**
- A) Usar `num_of_slaves_in_province < 2` como condición de corte (si ese trigger existe en IR 2.0.4 — verificar en `game.zip`)
- B) El jugador garantiza que el ancla es todo slaves antes de ejecutar → usar `total_population < 2` igual que Optimize

**Acción requerida:** Confirmar cuál de las dos opciones aplica, o verificar el trigger en `game.zip`.

### TEMA 2 — Slaves insuficientes en el ancla ⚠️

**Problema:** Si el ancla no tiene suficientes slaves para cubrir todos los asentamientos al count del tier elegido, el `while` simplemente para cuando se queda sin slaves, sin avisar al jugador. Algunos asentamientos recibirán menos slaves de los necesarios.

**Opciones:**
- A) Dejarlo así — el jugador es responsable de tener suficientes slaves. Advertir en el `_desc` de la decisión.
- B) Agregar lógica de verificación previa en el `allow` de las decisiones de tier.

**Acción requerida:** Decidir comportamiento.

### TEMA 3 — Variables nuevas y cleanup ⚠️

**Problema:** La función necesita variables nuevas que deben agregarse al cleanup en `exodos_scripted_effects.txt` y al chequeo de unidad destruida en `exodos_on_action.txt`.

**Variables nuevas a agregar al cleanup:**
```
exodos_slave_dist_pending
exodos_slave_dist_active
exodos_slave_dist_count
exodos_slave_dist_gather_done
exodos_unit_slave_dist  (variable de la unidad marcadora)
```

**Acción requerida:** Confirmar que el patrón de cleanup es idéntico al de Optimize antes de implementar. Verificar en `mod_pack_IRAM_v4_3.zip` → `exodos_scripted_effects.txt`.

### TEMA 4 — Unidad marcadora ⚠️

**Problema:** La función necesita su propia unidad marcadora (`exodos_unit_slave_dist`), igual que Optimize tiene `exodos_unit_optimize`. Hay que agregarla al chequeo de "unidad destruida = error" en el `monthly_country_pulse` de `exodos_on_action.txt`.

**Acción requerida:** Confirmar que el patrón de activación/destrucción de la unidad es idéntico al de Optimize. El bloque a agregar en `on_action` sería:

```pdxscript
# Unidad Slave Dist destruida
if = {
    limit = {
        has_variable = exodos_slave_dist_active
        NOT = { any_unit = { has_variable = exodos_unit_slave_dist } }
    }
    trigger_event = { id = exodos.1 }
}
```

## 16.9 Esquema del pulso mensual (diseño — no implementado)

Este es el pseudocódigo del comportamiento esperado. No es código real del mod — es el diseño a implementar una vez resueltos los temas de la sección 16.8.

```pdxscript
# FASE GATHER — reúne slaves de asentamientos al ancla
if = {
    limit = {
        has_variable = exodos_slave_dist_active
        NOT = { has_variable = exodos_slave_dist_gather_done }
    }

    var:exodos_anchor_province = {
        save_scope_as = exodos_dest
        area = {
            every_area_province = {
                limit = {
                    owner = ROOT
                    NOT = { has_variable = exodos_is_anchor }
                    # condición de "tiene slaves" — TEMA 1 pendiente
                }
                while = {
                    count = 30
                    limit = { # tiene slaves — TEMA 1 pendiente }
                    random_pops_in_province = {
                        limit = { pop_type = slaves }
                        move_pop = scope:exodos_dest
                    }
                }
            }
        }
    }

    # Corte del Gather — TEMA 1 pendiente
    if = {
        limit = { # todos los no-ancla sin slaves }
        set_variable = { name = exodos_slave_dist_gather_done value = 1 }
    }
}

# FASE DISTRIBUTE — reparte slaves según tier y building
else_if = {
    limit = {
        has_variable = exodos_slave_dist_active
        has_variable = exodos_slave_dist_gather_done
        var:exodos_slave_dist_count = 1   # tier 1: 8/13
    }

    var:exodos_anchor_province = {
        save_scope_as = exodos_origin
        area = {
            every_area_province = {
                limit = {
                    owner = ROOT
                    NOT = { has_variable = exodos_is_anchor }
                }
                save_scope_as = exodos_dist_target
                if = {
                    limit = {
                        OR = {
                            has_building = slave_mine_building
                            has_building = basic_settlement_infratructure_building
                        }
                    }
                    while = {
                        count = 8   # COUNT para mina/agrícola tier 1
                        limit = { scope:exodos_origin = { total_population >= 2 } }
                        scope:exodos_origin = {
                            random_pops_in_province = {
                                limit = { pop_type = slaves }
                                move_pop = scope:exodos_dist_target
                            }
                        }
                    }
                }
                else = {
                    while = {
                        count = 13  # COUNT para otros tier 1
                        limit = { scope:exodos_origin = { total_population >= 2 } }
                        scope:exodos_origin = {
                            random_pops_in_province = {
                                limit = { pop_type = slaves }
                                move_pop = scope:exodos_dist_target
                            }
                        }
                    }
                }
            }
        }
    }

    exodos_cleanup_effect = yes
}

# [repetir bloque distribute para tiers 2, 3, 4, 5 con sus counts]
```

## 16.10 Referencias técnicas rápidas

### Counts por tier (para copiar al escribir código)

```
# Tier 1: inv cívica + ley mon/rep + gran obra t4 (−4 total)
COUNT_MINA_AGRICOLA_T1 = 8
COUNT_OTROS_T1 = 13

# Tier 2: inv cívica + ley mon/rep (−3 total) ← config usuario
COUNT_MINA_AGRICOLA_T2 = 9
COUNT_OTROS_T2 = 14

# Tier 3: solo ley (−2 total)
COUNT_MINA_AGRICOLA_T3 = 10
COUNT_OTROS_T3 = 15

# Tier 4: solo inv cívica (−1 total)
COUNT_MINA_AGRICOLA_T4 = 11
COUNT_OTROS_T4 = 16

# Tier 5: sin modificadores (0 total)
COUNT_MINA_AGRICOLA_T5 = 12
COUNT_OTROS_T5 = 17
```

### Triggers clave (para copiar al escribir código)

```pdxscript
# Detectar building en territory scope:
has_building = slave_mine_building
has_building = basic_settlement_infratructure_building

# Filtrar slaves en random_pops_in_province:
limit = { pop_type = slaves }

# Excluir ancla del loop:
NOT = { has_variable = exodos_is_anchor }

# Verificar owner del área completa:
area = {
    NOT = {
        any_area_province = {
            NOT = { owner = ROOT }
        }
    }
}
```

### Nombres de decisiones y variables

```
# Decisiones
exodos_activate_slave_dist   ← activación (posiciona unidad)
exodos_slave_dist_t1         ← tier 1 (8/13)
exodos_slave_dist_t2         ← tier 2 (9/14)
exodos_slave_dist_t3         ← tier 3 (10/15)
exodos_slave_dist_t4         ← tier 4 (11/16)
exodos_slave_dist_t5         ← tier 5 (12/17)

# Variables de estado
exodos_slave_dist_pending    ← seteada por activate, cleared por tier
exodos_slave_dist_active     ← seteada por tier, cleared por cleanup
exodos_slave_dist_count      ← valor 1-5 según tier elegido
exodos_slave_dist_gather_done ← seteada cuando Gather termina

# Variable de unidad
exodos_unit_slave_dist       ← en la unidad marcadora
```

### Estado de integración
Integrado al SUPERBACKUP el 2026-05-19 desde `backup_slave_distributor_v2_1_.md` v2.1.
El backup original sigue siendo válido como referencia histórica pero este documento es ahora la fuente de verdad para el Slave Distributor.

---

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 17 — TABLA ECONÓMICA — VALORES CANÓNICOS
# ══════════════════════════════════════════════════════════

**Fuente:** Historial Agente 4, Sesión 05 — "Equivalencia entre manpower y oro".
**Estado:** CERRADO. No recalcular salvo pedido explícito del usuario.

## 17.1 Valor canónico del manpower

**Método:** comparación mercenario vs tropa estatal (cohort light infantry como unidad base),
horizonte 50 años, promedio bruto/neto.

| Parámetro | Valor | Derivación |
|---|---|---|
| `valor_manpower` | **1.9483 oro/manpower** | (92 + 1.50×50) / 75 mp neto, promedio bruto/neto |
| Precio recurso prom. ponderado | **0.2758 oro/mes** | Ponderado por 6.196 territorios del mapa |
| Ingreso ruta interna | **0.0552 oro/mes** | `0.2758 × ROUTE_BASE_INTERNAL_COMMERCE (0.20)` |

## 17.2 Distribución de metrópolis maxeada

| Tipo de pop | Cantidad (max edificios) |
|---|---|
| Noble | 14N |
| Citizen | 33C |
| Freeman | 34F |
| Slave | 19S |

Edificios usados: Academy / Court / Forum / Mill en niveles máximos.

## 17.3 Valor por tipo de pop (horizonte 50 años)

| Pop | Tax | Comercio/Surplus | Manpower | RP | **Total (50 años)** |
|---|---|---|---|---|---|
| Slave | 2.48 | 2.21 | — | — | **4.69** |
| Freemen | 0.83 | — | 9.35 | — | **10.18** |
| Citizen | — | 0.99 | 4.68 | 2.83 | **8.50** |
| Noble | — | 4.96 | — | 7.09 | **12.05** |
| **Promedio ponderado** | | | | | **8.81 oro/pop** |

**Componente RP:** `valor_rp = 0.023223` oro/RP — es una **premisa documentada**, no un dato
verificado del engine. Rango válido del engine: `[0.000542, 0.083352]` oro/RP. La premisa cae
dentro del rango pero no fue cerrada con ancla externa. El componente RP de Noble (7.09) y
Citizen (2.83) usa este valor.

## 17.4 Modelo A vs Modelo B (sin/con tech)

| Modelo | Base | Valor por pop | Fuente |
|---|---|---|---|
| Modelo A (sin tech) | 933 oro/50 años / 100 pops | **9.33 oro/pop** | Metrópolis base |
| Modelo B (tech completo) | 1450 oro/50 años / 100 pops | **14.51 oro/pop** | Con Innovations |
| Delta (B−A) | — | **5.16 oro/pop** | Base del costo de Innovations en TGL |

## 17.5 Valor de referencia para Exodos

| Valor | Descripción |
|---|---|
| **~10 oro/pop** | Valor de referencia conservador para costear operaciones de Exodos |

Este valor es deliberadamente conservador: está por debajo del Modelo A (9.33) para no
sobreestimar el beneficio de mover pops. El estudio usó el promedio ponderado (8.81) como
piso y 10 como número operativo redondo.

## 17.6 Justificación de costos del ecosistema

| Operación | Pops máx. | Costo base (10/pop) | Costo final | Factor extra |
|---|---|---|---|---|
| Gather | ~100 (1 pulso típico) | 1.000 | **1.000 oro** | — |
| Distribute | ~100 (1 pulso típico) | 1.000 | **1.000 oro** | — |
| Transfer | ~100 (10 pulsos × 10 pops) | 1.000 | **2.000 oro** | ×2 por conveniencia temporal |
| Optimize rangos | ~100 (Gather + Distribute) | 2.000 | **2.000 oro** | Operación compuesta |

**Manpower y tyranny:** no derivan del estudio económico — son costos de equilibrio de gameplay:
- Gather/Distribute: 5 mp (2500 pantalla), +10 tyranny, cap ≤90
- Transfer: 10 mp (5000 pantalla), +20 tyranny, cap ≤80
- Optimize rangos: 10 mp (5000 pantalla), +10 tyranny, cap ≤90

**Decisión de diseño:** el costo se cobra al `confirm`, no al `activate`. El jugador paga solo
cuando está seguro de ejecutar. No hay costo por pulso mensual.

## 17.7 Datos del mapa usados en el estudio

| Dato | Valor | Nota |
|---|---|---|
| Territorios totales | ~7.000 | Estimado del mapa de IR 2.0.4 |
| Regiones | 74 | |
| Áreas | 553 | |
| Promedio áreas por región | 7.5 | |
| Territorios habitables por área | ~10 | Excluyendo intransitables |
| Pops promedio por territorio | ~12 | |
| Territorios por ruta ponderada | 6.196 | Ponderado por rutas de comercio |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 18 — DECISIONES DE DISEÑO DESCARTADAS
# ══════════════════════════════════════════════════════════

**Propósito:** evitar que una IA futura re-proponga alternativas ya evaluadas y descartadas.
Las decisiones marcadas CERRADO no se reabren salvo pedido explícito del usuario.

## 18.1 Exodos — descartadas

| Alternativa descartada | Por qué se descartó | Versión |
|---|---|---|
| Costo por pulso mensual (pagar cada mes que corre la operación) | Asimetría entre operaciones (Transfer tiene pulsos fijos, Gather/Distribute no). Complejidad innecesaria. | v1→v2 |
| Contador `exodus_operation_counter` de pops movidos | `count = var:X` en `while` no funciona en IR 2.0.4 — devuelve `Value of wrong type: none`. Eliminado en favor de condición de población (`total_population >= N`). | v1→v2 |
| Condición de área no necesariamente 100% propia | Fue decisión explícita de diseño: el jugador debe controlar el área completa. No es default del engine. | v2 |
| `war = no` en las 3 operaciones de Exodos ALT | Eliminado deliberadamente en la distribución ALT para permitir operaciones en guerra. La distribución estable lo conserva. | v1→v2-ALT |
| Cancelación automática separada por operación (`exodos_cancel_gather`, `exodos_cancel_transfer`, etc.) | Una sola decisión `exodos_cancel` / `exodos_cancel_all` cubre todo. Más simple, menos decisiones en el panel. | v1 |
| Rival en Exodos v1 (Gather/Distribute) | v1 no tenía condición de rival — el jugador posicionaba manualmente. Se agregó en v2-ALT para mejorar UX. No se porta a v3/v4 estable por diseño. | v1 |
| Pops mínimos por fuente en Distribute (como en Gather) | Distribute no tiene piso por fuente — solo piso en el ancla (`total_population >= 30`). Decisión consciente: Distribute vacía el ancla, no balancea. | v2→v3 |

## 18.2 BOM — descartadas

| Alternativa descartada | Por qué se descartó | Versión |
|---|---|---|
| Evento en el país del objetivo tras BOM | Imposible: `country_event` siempre dispara en `root`, no en el país objetivo. Confirmado en BOM v2.1. | v2.1 |
| Cooldown temporal entre usos de BOM | Variables de tiempo generan fallos en delay en IR 2.0.4. `is_ai = no` es la única restricción de abuso. | v2.3 |
| Costo dinámico por rango del objetivo (más caro matar rival de mayor rango) | Complejidad excesiva. Costo fijo 2000 oro es suficiente. | diseño |
| Fallo aleatorio en la ejecución (BOM falla con X% de probabilidad) | El ecosistema es determinista por diseño. El jugador paga y el efecto ocurre siempre. | diseño |
| Popup de éxito `bom.2` ("El Trabajo Está Hecho") | Eliminado en v1.2 — todos los mods son silenciosos excepto errores y TLV Confirm. | v1.2 |

## 18.3 General — descartadas

| Alternativa descartada | Por qué se descartó | Versión |
|---|---|---|
| `death = { death_reason = ... }` para matar personajes | No funciona desde ningún scope de personaje en IR 2.0.4 — silencioso. `add_health = -100` es el único mecanismo confirmado. | BOM, TLV |
| Costs cobrados en `activate` | El jugador paga en `confirm`. Convención fija del ecosistema. | v1 |
| `is_triggered_only = yes` en eventos del mod | No existe en IR 2.0.4 — genera error. Todos los eventos del mod van sin este flag. | Exodus bug 8 |

## 18.4 Arquitectura experimental scripted_gui (rama `mod_pack_IRAM_v4_3.zip`) — DESCARTADA

**Contexto:** antes de v4.0, se desarrolló una rama experimental que reimplementó Exodos con scripted_gui. El conocimiento de esa investigación se preserva aquí.

**Qué tenía esa rama:**
- `scripted_guis/exodos_scripted_guis.txt` — panel de decisiones con botones A (Ancla) y B (Destino) en el panel de tácticas de provincia
- 2 unidades marcadoras: `exodos_anchor` (sub_unit nueva, `movement_speed = 0`) y `exodos_marker` (`movement_speed = 0` — inmóvil)
- Variables de unidad reducidas a solo `exodos_unit_anchor` y `exodos_unit_destination`
- Activates y pendings eliminados — los confirms siempre visibles
- `exodos_decisions_rival_heir.txt` — nota indicando necesidad de portar la función a v4
- `exodos_decisions_cancel.txt` mucho más extenso — cleanup exhaustivo de variables nuevas y legacy
- Guards cruzados en `allow` de confirms: `NOT = exodos_operation_active` + `NOT = exodos_optimize_active`
- Guard `NOT = exodos_optimize_active` en `is_valid` del botón A
- Guard `NOT = exodos_operation_active` en `is_valid` del botón B

**Por qué se descartó:**
- La arquitectura de v3 (decisions + on_action) ya era más simple y funcional
- Gather Global, Distribute simplificado y Relics se implementaron sobre la base de v3 sin necesidad de scripted_gui
- El Optimize Global puede lograrse como operación automática sin botones ni unidades adicionales
- El riesgo `movement_speed = 0` (si el engine permite arrastrar igualmente las unidades, el mecanismo de botones A/B queda inútil) nunca fue testeado — la arquitectura v3 no tiene ese riesgo

**Conocimiento recuperado:**
- La lógica de guards cruzados (`NOT = exodos_operation_active` + `NOT = exodos_optimize_active`) es válida y fue portada a v4.0.
- El cleanup exhaustivo de legacy variables fue portado a `exodos_decisions_cancel.txt` de v4.0.
- La idea de "el sistema cuenta los pops del ancla y ejecuta el Distribute correspondiente automáticamente" (sin input del jugador) inspira el diseño del Optimize Global de Población pendiente.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 19 — LOG DE DECISIONES POR SESIÓN
# ══════════════════════════════════════════════════════════

**Propósito:** registrar qué se decidió y qué quedó abierto al cierre de cada sesión de trabajo.
Una IA nueva que retoma el proyecto puede leer esta sección para saber el estado exacto del debate,
sin tener que inferirlo del historial completo.

**Formato de entrada:**

```
## [AAAA-MM-DD] — [tema principal de la sesión]

### ✅ Decidido
- [decisión concreta — no parafrasear, ser específico]

### ❓ Quedó abierto
- [pregunta o debate sin cerrar] — contexto: [una línea de contexto]

### ⚠️ Premisas no verificadas activas
- [premisa] — usada en: [sección/archivo] — riesgo si es falsa: [una línea]
```

---

## 19.0 — Índice de temas abiertos

Actualizar esta tabla in-place en cada sesión. Para detalle completo, ir a la entrada de sesión correspondiente.

| Tema | Estado | Riesgo si no se resuelve | Última sesión |
|---|---|---|---|
| `movement_speed = 0` — ¿el engine permite igualmente arrastrar la unidad? | ✅ CERRADO — arquitectura descartada, ya no aplica | — | 2026-05-21 |
| `current_ruler` desde country scope en trigger (TLV) | ⚠️ Sin testear | `tlv_confirm` puede fallar silenciosamente al verificar condiciones del gobernante | 2026-05-19 |
| Heredero del Rival — ¿se porta a v4? | ✅ CERRADO — sin cambios vs v3 | — | 2026-05-21 |
| Condición `has_spouse` en Heredero del Rival | ⚠️ Sin codear — token pendiente | La decisión puede aparecer aunque el rival no tenga esposa | 2026-05-21 |
| Optimize Global — diseño | ⚠️ En curso — dos variantes: Población y Económico | Última función mayor pendiente de v4 | 2026-05-21 |
| Reliquia migración `global_migration_speed = 2.5` | 🔧 Token cerrado, código pendiente | Relic incompleto — fácil de implementar | 2026-05-21 |
| `valor_rp = 0.023223` — nunca verificado contra el engine | ⚠️ Sin verificar | Debilita el argumento del modelo económico (no bloquea código) | 2026-05-19 |

**Regla de uso:** cuando un tema se cierra, reemplazar ⚠️/❓ por ✅ y agregar fecha de cierre. No eliminar filas — el historial sirve de referencia.

---

## 2026-05-21 — Definición de v4, diseño de Optimize Global, actualización SUPERBACKUP v2.1

### ✅ Decidido
- v4 canónico es `mod_pack_IRAM_v4_0.zip` — renombrado desde `mod_pack_IRAM_15_GATHER_GLOBAL_v1_2.zip`.
- Arquitectura de v4: decisions + on_action puro, sin scripted_gui, sin unidades marcadoras para Gather Global.
- La rama experimental `mod_pack_IRAM_v4_3.zip` (scripted_gui) se descarta — conocimiento preservado en Sección 18.4.
- Heredero del Rival: sin cambios vs v3. Se porta tal cual. Condición `has_spouse` agregada como pendiente (token a confirmar).
- `family = scope:exodos_rival.family` sin esposa: el hijo spawna igual sin familia. Comportamiento aceptado, no es bug.
- Optimize Global: dos variantes — Población (Gather por área + Distribute automático según pops) y Económico (itera asentamientos por tipo de edificio, asigna slaves). El Distribute del Global de Población usa los 4 rangos del Distribute simplificado — el sistema elige el rango automáticamente según pops del ancla, sin input del jugador.
- Relics tokens corregidos en v4.0: `gold` → `treasury`, `add_gold` → `add_treasury`, `picture` eliminado.
- BOM-como-texto corregido en v4.0 en ambos archivos afectados.
- Gather Global capital exclusion (`NOT = { is_capital = yes }`) implementado en v4.0.
- `install_philokles_egypt` es función vanilla — agregado a errores a ignorar siempre.
- SUPERBACKUP actualizado a v2.1. Prompt Maestro actualizado a v3.1. Instrucciones Humano actualizadas.

### ❓ Quedó abierto
- Optimize Global — diseño conceptual cerrado, implementación pendiente de sesión futura.
- Condición `has_spouse` en Heredero del Rival — token correcto sin confirmar. No codear hasta validar.
- Reliquia migración `global_migration_speed = 2.5` — token y valor cerrados, código no escrito. Ir directo al código en próxima sesión.

### ⚠️ Premisas activas
- `valor_rp = 0.023223` — sin verificar, no bloquea código (sin cambios desde sesión anterior).
- `current_ruler` desde country scope en trigger (TLV) — sin testear.

---

### ✅ Decidido
- Aplicar 6 mejoras al SUPERBACKUP: log de sesiones (Sección 19), protocolo de actualización (Sección 20), tabla de zips (Sección 21), checklist QA, triggers frecuentes de game.zip, log de enfoques descartados de engine.
- Separar el Prompt Maestro en Plantilla A (trabajo cotidiano) y Plantilla B (revisión integral).
- El log de enfoques descartados de engine se integra como subsección de la Sección 18 (decisiones descartadas ya existente).
- El checklist QA y los triggers de game.zip se agregan como subsecciones de Sección 7 (diagnóstico) y Sección 6 (gotchas) respectivamente.

### ❓ Quedó abierto
- `valor_rp = 0.023223` — nunca fue verificado contra el engine. Ver Sección 17.3. Afecta el valor calculado de Noble (7.09/50 años) y Citizen (2.83/50 años). No bloquea ningún código actual.
- `movement_speed = 0` — no hay precedente confirmado de que el engine impida mover la unidad con el cursor. Es el riesgo de arquitectura más alto de v4. Ver Sección 2.2 y ERROR 4.
- Heredero del Rival — ¿se porta a v4 o se deja en v3 sin cambios? No definido. Ver Sección 0.5.
- Slave Distributor — 4 temas abiertos antes de codear. Ver backup dedicado `backup_slave_distributor_v2_1_.md` Sección 8.

### ⚠️ Premisas no verificadas activas
- `valor_rp = 0.023223` — usada en: Sección 17.3 (valor de Noble y Citizen) — riesgo: los costos de Exodos están justificados por el valor por pop; si valor_rp es significativamente distinto, el argumento de diseño se debilita (pero los costos ya están fijados por gameplay, no por el modelo).

---

## 2026-05-19 — Meta-análisis del sistema de control y generación de v3.0

### ✅ Decidido
- SUPERBACKUP se mantiene como monolito (D1 — descartada separación en capas).
  Razón: los problemas del proyecto se conectan entre sí; separar el contexto
  agrega fricción sin reducir carga real.
- Las reglas R no son desconfianza sino economía de contexto: lo documentado no
  se rediscute, lo no documentado es espacio de colaboración.
- Hito de cierre de v4: Slave Distributor funcionando.
- Generados IRAM_PROMPT_MAESTRO_v3_0.md e IRAM_INSTRUCCIONES_HUMANO.md.
  Cambios respecto a v2.1: reglas centralizadas en PASO 1 (no duplicadas),
  clasificación 🔴🟡🔵, confirmación previa antes de tocar código, formato de
  entrega estandarizado, cierre en Plantilla B, smoke test en instrucciones humano,
  protocolo de reanudación desde pausa larga.
- Dashboard de estado agregado como Sección 0.5.0.
- D4 (checklist revisión humana post-sesión) descartado — ya cubierto por
  formato de entrega de la IA en v3.0.

### ❓ Quedó abierto
- Fase 3 del análisis de mejoras — no implementada, decisión postergada.
- Fase 4 — preguntas conceptuales (F3, G6, J3) sin responder, no urgentes.

### ⚠️ Premisas activas sin cambios
- `valor_rp = 0.023223` — sin verificar, no bloquea código
- `movement_speed = 0` — riesgo de arquitectura, sin testear

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 20 — PROTOCOLO DE ACTUALIZACIÓN DEL SUPERBACKUP
# ══════════════════════════════════════════════════════════

**Regla general:** el superbackup documenta diseño y decisiones. El zip documenta implementación.
Cuando divergen: el zip manda para código v4, el superbackup manda para diseño.

## 20.1 Cuándo crear versión nueva vs editar in-place

| Situación | Acción |
|---|---|
| Se corrige un bug en el zip | Editar in-place: actualizar Sección 0.5, marcar ✓ en Sección 2.2, agregar entrada en Sección 14 |
| Se agrega una feature nueva | Nueva versión menor (v1.X): actualizar Secciones 0.5, 2.1, 3.3, 3.4, 13, agregar sección nueva si aplica |
| Se cierra un tema pendiente (⚠️ TESTEAR) | Editar in-place: actualizar Sección 2.2, agregar resultado en Sección 14, eliminar ⚠️ |
| Se documenta un nuevo gotcha del engine | Editar in-place: agregar entrada en Sección 6, agregar ERROR numerado en Sección 0.4 |
| Cambio de arquitectura mayor | Nueva versión mayor (v2.X): actualizar todas las secciones afectadas, registrar en Sección 14 |
| Se actualiza el zip sin cambios de diseño | Solo actualizar header, Sección 0.1 y Sección 0.5 |

## 20.2 Qué secciones tocar por tipo de cambio

### Al corregir un bug en el zip
1. **Sección 0.4** — agregar ERROR numerado si es nuevo patrón
2. **Sección 0.5** — marcar bug como corregido en tabla de bugs pendientes
3. **Sección 2.2** — marcar fix como ✓ CORREGIDO en vX_Y
4. **Sección 8-C** — actualizar el código fuente real si el archivo cambió
5. **Sección 14** — agregar entrada de historial con la corrección
6. **Sección 19** — agregar entrada de sesión con lo decidido

### Al agregar una feature nueva
1. **Sección 0.5** — agregar fila en tabla de componentes
2. **Sección 2.1** — actualizar estado de v4
3. **Sección 3.3** — agregar a tabla de funciones
4. **Sección 3.4** — agregar costos a tabla económica
5. **Sección 3.7** — actualizar panel de decisiones
6. **Sección 13** — agregar pasos de implementación
7. **Sección 14** — agregar entrada de historial
8. Nueva sección de diseño si aplica (ej: Sección 16 para Slave Distributor)

### Al cerrar un ⚠️ TESTEAR
1. **Sección 0.4b** — actualizar celda de la tabla
2. **Sección 2.2** — marcar como ✓ CERRADO con resultado
3. **Sección 6** — agregar gotcha si el test reveló comportamiento inesperado
4. **Sección 14** — registrar resultado del test
5. **Sección 19** — actualizar premisas no verificadas

## 20.3 Regla de consistencia — checklist mínimo antes de guardar

Antes de guardar una nueva versión del superbackup, verificar:
- [ ] El header refleja la versión correcta y la fecha de hoy
- [ ] El footer (`*IRAM SUPERBACKUP vX.Y*`) está actualizado
- [ ] Los cambios están registrados en Sección 14
- [ ] Los bugs pendientes en Sección 0.5 están al día
- [ ] No hay crossovers entre secciones (ej: tabla de rangos vs localización vs comentarios del zip)
- [ ] La entrada de Sección 19 documenta lo decidido y lo que quedó abierto

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 21 — TABLA DE EQUIVALENCIA DE ZIPS
# ══════════════════════════════════════════════════════════

Referencia rápida de todos los zips del proyecto. Usar esta tabla para decidir cuál cargar.

| Nombre de archivo | Versión | Fecha | Estado | Diferencia clave vs anterior |
|---|---|---|---|---|
| `mod___SUPERBACKUP_.zip` | IRAM v1 (Estable v1.3.5) | 2026-05 | Histórico — no usar para trabajo activo | Spawn en `capital_scope`, `war=no` obligatorio, sin Optimize, sin Heredero |
| `mod_alt___SUPERBACKUP_.zip` | IRAM v2 (ALT v1.3) | 2026-05 | Histórico — no usar para trabajo activo | Spawn en posición rival, `war=no` eliminado, BOM absorbe kill_ruler, IHA nuevo |
| `mod_pack_IRAM_13__SUPERBACKUP_.zip` | IRAM v1.3 (histórico) | 2026-05 | Histórico — referencia de versión intermedia | Versión intermedia entre v2 y v3 |
| `mod_pack_IRAM_15.zip` | IRAM v3 FINAL | 2026-05 | ✅ CERRADO — zip canónico de v3 | Optimize 4 rangos, Heredero del Rival v1.6, herencia matrilineal, todo en `exodos/` |
| `mod_pack_IRAM_v4_3.zip` | IRAM v4 experimental | 2026-05-19 | 🗃 DESCARTADO — rama experimental | scripted_gui, 2 unidades inmóviles, sin activates — ver Sección 18.4 |
| `mod_pack_IRAM_15_GATHER_GLOBAL_v1_2.zip` | IRAM v4.0 (pre-renombrado) | 2026-05-21 | 🗃 RENOMBRADO — base de v4.0 | Gather Global v1.2 con capital exclusion, Distribute 4 rangos, Relics tokens corregidos |
| `mod_pack_IRAM_v4_0.zip` | IRAM v4.0 | 2026-05-21 | 🔧 ACTIVO — zip canónico de v4 | Mismo contenido que GATHER_GLOBAL_v1_2, renombrado como versión oficial v4 |

**Regla de uso:**
- Para trabajo en v4: cargar `mod_pack_IRAM_v4_0.zip`
- Para referencia de v3 estable: cargar `mod_pack_IRAM_15.zip`
- Para análisis histórico: cargar el zip de la versión específica
- Para investigación de la arquitectura scripted_gui: `mod_pack_IRAM_v4_3.zip` — ver Sección 18.4
- Nunca mezclar código de zips distintos sin verificar diferencias en Sección 0.4b

## 21.1 Qué cambió en cada versión de v4

| Zip v4 | Cambio principal | Bug corregido |
|---|---|---|
| `mod_pack_IRAM_15_GATHER_GLOBAL_v1_0.zip` | Gather Global + Distribute 4 rangos | — |
| `mod_pack_IRAM_15_GATHER_GLOBAL_v1_2.zip` | Capital exclusion + Fix BOM-como-texto + Fix relics tokens | BOM literal en on_action y decisions_optimize ✓ |
| `mod_pack_IRAM_v4_0.zip` | Renombrado como v4.0 canónico | Mismo contenido que v1_2 |

**Bugs pendientes en zip activo (`mod_pack_IRAM_v4_0.zip`):**
Ninguno documentado al cierre de la sesión 2026-05-21.

---

*IRAM SUPERBACKUP v2.1 — 2026-05-21*
*Drago Mod Pack (v1→v3) + IRAM v4 en desarrollo*
*Engine: Imperator Roma 2.0.4*
*Zips: mod___SUPERBACKUP_.zip (v1) | mod_alt___SUPERBACKUP_.zip (v2) | mod_pack_IRAM_15.zip (v3-FINAL) | mod_pack_IRAM_v4_0.zip (v4 activo)*
*Cambios v2.1 (2026-05-21): Zip canónico renombrado a mod_pack_IRAM_v4_0.zip. Sección 0.1 unificada (un zip). Sección 0.2 sin distinción v3/v4. ERROREs 2/3/4/15/16 actualizados y remitidos a Sección 18.4. ERROR 1 actualizado. R2/R3/R5 actualizadas. R9 con nota BOM-como-texto. R14 actualizada. Sección 0.4b nueva tabla v3→v4 real. Sección 0.5 dashboard actualizado (v4.0, sin semáforos de scripted_gui). Secciones 1.1 y 1.2 actualizadas (v4 con Gather Global, Distribute 4 rangos, Relics). Sección 2.1 estado real de v4.0. Sección 2.2 reescrita con fixes reales y pendientes actuales. Sección 3.2 estructura de archivos v4. Sección 3.3 tabla de funciones actualizada. Sección 3.4 costos: relics + Gather Global, sin scripted_gui. Sección 3.5 unidades v4 sin exodos_anchor. Sección 3.7 panel sin scripted_gui, con Gather Global y Relics. Sección 7 errores a ignorar: install_philokles_egypt e iha_holding agregados, exodos_anchor removido. Sección 18.3 actualizada. Sección 18.4 nueva: arquitectura experimental descartada preservada como investigación. Sección 19.0 temas abiertos actualizados. Entrada sesión 2026-05-21 agregada. Sección 21 tabla de zips actualizada con v4.0 como activo y v4_3 como descartado.*
que cargamos en la proxima sesion?

En orden de carga:

Obligatorio siempre:
SESSION_LOG_REPLANTEO_2026-06-20.md — único punto de partida operativo.

Solo si hace falta entender el razonamiento detrás de una decisión:
RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20.md

Solo si hace falta el detalle completo de algo puntual:
CHARLA_REPLANTEO_1.md, CHARLA_REPLANTEO_2.md, SESSION_LOG_REPLANTEO_2026-06-19_2.md

Para la primera tarea de diseño — inventario de archivo:
El zip fuentes_de_documentacion.zip — para listar y clasificar el material disponible.

No cargar:
La serie SESSION_LOG_ANALISIS_C1_2026-06-18_v1 a v5 — son archivo histórico, no insumo activo.

Una sola instrucción para abrir la próxima sesión: "Lee el SESSION_LOG, la primera tarea es el inventario del material de archivo."


Check what JSON and ZIP files are available in uploads
Check what JSON and ZIP files are available in uploads
The user is asking where they stand with the processed JSON files after the replanteo. Let me check what's available in the uploads and what we know from the session logs.

From the SESSION_LOG and the conversation, I know:

Corpus A: 5 JSON del mod (claude_1_processed.json through claude_5_processed.json) - described as "Disponible. Sin procesar con categorización corregida (DR-06)"
The bloque3_analysis_v2.py script loads from '/mnt/user-data/uploads/claude_{i}_processed.json' - so it seems like processed files existed at some point
Now I need to verify whether those processed files are actually present in the uploads directory right now, or if they need to be regenerated by running process_iram_v2.py again.
Mostrar menos

Check what JSON and ZIP files are available in uploads
bash

ls /mnt/user-data/uploads/*.json 2>/dev/null | head -20 && echo "---" && ls /mnt/user-data/uploads/*.zip 2>/dev/null
Salida

---
/mnt/user-data/uploads/fuentes_de_documentacion.zip
Listo
Eso aclara el estado exacto. No hay processed JSONs en esta sesión — solo el zip de fuentes y los scripts.

Lo que el SESSION_LOG dice sobre el estado real del Corpus A: "Disponible. Sin procesar con categorización corregida (DR-06). Primer paso del análisis."

O sea los conversations.json crudos existen en tu máquina local, pero los processed JSONs (claude_1_processed.json al claude_5_processed.json) o no se corrieron todavía, o se corrieron en una sesión anterior pero no los subiste acá.

Dos preguntas concretas para saber dónde estamos:

¿Los 5 processed JSONs existen en tu máquina local? Si sí, los subís y arrancamos directo con el exportador CSV para la diplomatura. Si no, hay que correr process_iram_v2.py sobre cada conversations.json primero.

¿Los conversations.json crudos de las 5 cuentas están en tu máquina? Eso confirma que el Corpus A está disponible para procesar.

en que afecta n las consignas al plan de trabajo que ya teniamos?

No lo afecta negativamente. Lo complementa.

Lo que la consigna requiere es un subconjunto del trabajo que ya teníamos planificado. Nada de lo que pide contradice o desvía el plan — lo que hace es ponerle una fecha límite concreta a una parte del análisis.

Lo que coincide exactamente:

La Parte 1 pide dataset limpio + EDA + 3 preguntas + 2 gráficos + propuesta conceptual de ML. Eso es el Grupo 1 de métricas que ya diseñamos, corrido sobre Corpus A, con una capa de visualización encima.

La Parte 2 pide flujo documentado (entrada → proceso → salida) + prototipo de IA generativa + métrica de impacto + reflexión ética. Eso es el sistema de 4 archivos ya documentado + DR-08/DR-09 como hallazgos con costo medido + la reflexión sobre HITL real vs. instrucción.

El único efecto real en el plan:

Agrega una fecha intermedia que antes no existía. Parte 1 vence en 10 días, lo que significa que el diseño de parámetros del Corpus A y el exportador CSV tienen que estar listos esta semana — antes de lo que teníamos pensado.

No cambia el diseño, no cambia las métricas, no cambia el pipeline DR-21. Solo acelera la primera etapa.

Lo que habría que agregar al log:

Una nota que vincule las entregas de la diplomatura con las fases del plan — Parte 1 = output intermedio del análisis Corpus A, Parte 2 = output del análisis completo A/B. Así la diplomatura no es trabajo paralelo sino un hito dentro del mismo pipeline.

¿Lo incorporamos al log, o eso lo dejamos para la próxima sesión?


SESSION_LOG_REPLANTEO_2026-06-20 5.md
md


CHARLA REPLANTEO 2.md
md


CHARLA REPLANTEO 1.md
md


SESSION_LOG_REPLANTEO_2026-06-19.md
78 líneas

md


RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20 2.md
157 líneas

md


SESSION_LOG_REPLANTEO_2026-06-20 4.md
176 líneas

md


RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20.md
157 líneas

md


SESSION_LOG_REPLANTEO_2026-06-20 3.md
176 líneas

md


SESSION_LOG_REPLANTEO_2026-06-19 2.md
102 líneas

md

eso es el ultimo estado el replanteo , aparte tengo los 5 zip de claudes al dia 20/06


Reading the latest session log version 5
Reading the latest session log version 5
The user is clarifying the current state. They have:

The session logs uploaded (the latest being SESSION_LOG_REPLANTEO_2026-06-20_5.md which I need to check)
The 5 Claude ZIP files with raw conversation data up to 20/06
Let me check which log file is the actual latest one. The user uploaded:

SESSION_LOG_REPLANTEO_2026-06-20_5.md (this seems to be the latest)
SESSION_LOG_REPLANTEO_2026-06-20_4.md
SESSION_LOG_REPLANTEO_2026-06-20_3.md
SESSION_LOG_REPLANTEO_2026-06-19_2.md
SESSION_LOG_REPLANTEO_2026-06-19.md
RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20_2.md
RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20.md
I notice the _5 version wasn't shown in the documents list, so I need to verify if it actually exists or if the latest is actually the _4 version. The ZIPs extending through June 20th mean Corpus B content might already be included in them—I just need to extract and properly segment it at the right cutoff. Let me check what SESSION_LOG_REPLANTEO_2026-06-20_5.md actually contains to see the current state.

Mostrar menos

Reading the latest session log version 5
Listo
Bien. El _5 es el log correcto y completo — es el que produjimos en esta sesión con todas las correcciones aplicadas. DR-01 a DR-21, métricas rediseñadas, Framework B, definiciones operacionales, todo.

Ahora hay un dato nuevo que cambia algo: tenés los 5 ZIPs de Claude al día 20/06, no al 10/06.

Eso significa que los ZIPs ya contienen tanto Corpus A como Corpus B en el mismo archivo. No hay que esperar ni agrupar nada por separado — el corte entre A y B se aplica al momento de procesar, usando la fecha de la carpeta que ya registraste como evento de corte.

El estado real entonces es:

Tenés: los 5 ZIPs crudos con todo el historial hasta 20/06. Los scripts de procesamiento. El diseño completo del análisis en el log _5.

No tenés todavía: los processed JSONs. Hay que correr process_iram_v2.py sobre cada ZIP para generarlos.

Lo que cambia para la diplomatura: con los ZIPs al 20/06, el dataset que le subís a la entrega incluye tanto el desarrollo del mod como la fase de documentación. Eso es más rico que solo Corpus A — y encaja mejor con lo que la consigna pide como "problema real con datos propios".

La primera tarea concreta es procesar los 5 ZIPs. ¿Los podés subir acá para correrlos, o son demasiado pesados?

que pasos nos quedan a seguir para el trabajo?


Inventarió tareas pendientes: procesar datos, exportar análisis, redactar diplomatura
Inventarió tareas pendientes: procesar datos, exportar análisis, redactar diplomatura
The user is asking what steps remain to complete the work - specifically the diplomatura assignment (Parte 1 due in 10 days) and the broader project. Let me think about this clearly based on everything we know.

Current state:

Have: 5 ZIPs with raw conversation data up to 20/06
Have: Scripts (process_iram_v2.py, bloque3_analysis_v2.py, spec_a_authorship.py, etc.)
Have: SESSION_LOG_REPLANTEO_2026-06-20_5.md as the operative document
Missing: processed JSONs, CSV exports, visualizations, and the diplomatura document itself
For the diplomatura Parte 1 in the next 10 days, I need to process those 5 ZIPs through the pipeline to generate the analysis tables, then export everything to CSV format and create the required document. Beyond that, there's the broader project work involving the paper, skill development, and portfolio pieces.

The diplomatura is essentially the analysis phase of Corpus A with a presentation layer on top, so it fits within the larger pipeline structure I've already mapped out.

Mostrar menos
Listo
Los separo en dos tracks porque tienen timelines distintos pero comparten trabajo.

Track 1 — Diplomatura Parte 1 (10 días)

Procesar los 5 ZIPs con process_iram_v2.py → genera los processed JSONs
Correr bloque3_analysis_v2.py sobre los processed JSONs → genera las tablas A, B, C, D
Escribir un exportador CSV (~30 líneas) que convierta los processed JSONs a tabla por sesión
Con el CSV en Excel: armar los 2 gráficos requeridos
Redactar el documento: descripción del problema, 3 preguntas con respuesta, propuesta conceptual de ML
Pasos 1 y 3 requieren código. Pasos 4 y 5 son manuales.

Track 2 — Proyecto completo (sin fecha fija)

Siguiendo DR-21 (Diseño → Limpieza → Análisis → Comparativa):

Inventario del material de archivo — primera tarea de diseño pendiente
Inventario terminológico — sesión dedicada
Limpieza: procesar los ZIPs separando Corpus A y B por el corte de evento
Análisis Corpus A (el mismo trabajo del Track 1, más profundo)
Análisis Corpus B
Comparativa A/B
Correcciones del paper (S4A, S5)
Skill C2
Portfolio en GitHub
Lo que los dos tracks comparten:

El paso 1 del Track 1 (procesar los ZIPs) es el mismo que el paso 3 del Track 2. Si lo hacés bien ahora, no se rehace después.

La decisión concreta para arrancar:

¿Subís los ZIPs acá para procesar ahora, o preferís hacerlo en tu máquina local?