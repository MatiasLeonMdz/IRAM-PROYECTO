# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK
## TECHNICAL WIKI ACTIVE — v3.10
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | archivos activos: ver Sección 22

**Este documento es el ACTIVE del TECHNICAL WIKI.** Contiene todo lo necesario para sesiones de código.
El historial narrativo, código fuente v1/v2/v3, y decisiones descartadas están en el **TECHNICAL_WIKI_ARCHIVE_v3_4**.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0 — INSTRUCCIONES PARA LA IA
# LEER COMPLETO ANTES DE ESCRIBIR CUALQUIER LÍNEA
# ══════════════════════════════════════════════════════════

## 0.1 QUÉ ES ESTE DOCUMENTO

Este documento (ACTIVE) es la **fuente de verdad operativa** del proyecto IRAM para sesiones de código.
Cubre el diseño completo de IRAM v4, gotchas del engine, estado del proyecto, flujos, localizaciones y log de decisiones v4.

El historial narrativo (v1→v3), código fuente v1/v2/v3, y decisiones descartadas están en el **TECHNICAL_WIKI_ARCHIVE_v3_4** — cargar ese archivo solo cuando sea explícitamente necesario.

**Archivos activos del proyecto:** ver Sección 22.

Para comparación histórica con v3: `mod_pack_IRAM_15.zip` (v3 FINAL, cerrado).
Para código fuente v1/v2/v3 o historial detallado: ver TECHNICAL_WIKI_ARCHIVE_v3_4.

El documento es autónomo para diseño, decisiones y referencia. Para el código exacto de v4 usar el zip v4 — el documento documenta el diseño, el zip es la implementación.

**Regla de comparación de fuentes:** si el zip contradice el documento en diseño, el documento manda. Si el zip contradice el documento en código v4, el zip manda. Si difieren en algo no registrado en Sección 19, preguntar antes de asumir. Para entender diferencias entre zips, ver Sección 21.

**Si algo está documentado aquí: no preguntar. Está resuelto.**
**Si algo no está documentado: preguntar al usuario antes de asumir o inventar.**

---

## 0.1b VISIÓN DEL PROYECTO

**El mod exitoso es el entregable. El aprendizaje es el objetivo real.**

IRAM es un proyecto de software con dominio de videojuego, usado deliberadamente como campo de práctica de arquitectura, problem-solving y AI collaboration, y como puente hacia data science y desarrollo profesional.

Toda decisión de diseño refleja esto: claridad sobre exhaustividad, el ecosistema habilita no castiga, la IA implementa lo que el operador diseña.

## 0.1c PERFIL DEL OPERADOR

- Domina scopes, effects y triggers básicos — experiencia previa en EU4 modding
- Las soluciones arquitectónicas difíciles de IRAM fueron diseñadas por el operador, no por la IA
- División de roles: el operador diseña, la IA implementa — no invertir este orden
- Nivel técnico alto: no sobre-explicar conceptos básicos del engine ni de programación
- Usa la IA deliberadamente para saltear boilerplate y mecánica fina, no para evitar el trabajo difícil

---

## 0.2 CHECKLIST OBLIGATORIO — EJECUTAR EN ORDEN ANTES DE RESPONDER

- [ ] **1.** Leer este documento completo de principio a fin.
- [ ] **2.** Abrir el zip canónico activo (ver Sección 22) con `unzip -l` para verificar qué archivos hay.
- [ ] **3.** Si se subió un SESSION_LOG reciente, leerlo después del TECHNICAL_WIKI y antes del zip.
- [ ] **4.** No asumir sintaxis del engine de memoria. Verificar contra archivos fuente o la Sección 6.
- [ ] **5.** Revisar la Sección 0.5 (Estado actual del proyecto) antes de escribir una sola línea de código.
- [ ] **6.** Preguntar al usuario qué quiere hacer en esta sesión. No empezar a codear hasta confirmar.

### Protocolo de arranque para sesiones de código

```
PASO 1 — Leer este documento completo.
PASO 2 — Abrir el zip canónico activo (Sección 22) con unzip -l para verificar qué archivos hay.
PASO 3 — Si existe SESSION_LOG reciente: leerlo para contexto de la última sesión.
PASO 4 — Revisar Sección 0.5: estado real de cada componente.
PASO 5 — Revisar Sección 13: qué pasos de v4 están hechos y qué falta.
PASO 6 — Preguntar al usuario: "¿Qué querés hacer hoy?"
PASO 7 — Sólo después de confirmar: leer el archivo fuente específico del zip antes de modificarlo.
PASO 8 — Antes de generar el zip final: preguntar la hora al operador.
PASO 9 — Entregar archivos individuales + zip final con BOM validado y nombre con fecha y hora.
PASO 10 — Nunca entregar código sin haber verificado la Sección 6 para la sintaxis usada.
```

**Regla de oro:** Si no estás seguro de si algo existe en IR 2.0.4, buscarlo en `game.zip` o preguntar. No inventar sintaxis.

---

## 0.3 MAPA DEL DOCUMENTO

**Este archivo (ACTIVE)** contiene lo necesario para trabajo en sesión. Las secciones marcadas
con 📦 están en el **TECHNICAL_WIKI_ARCHIVE_v3_4** — cargar ese archivo solo si son necesarias.

| Necesito saber... | Ir a |
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
| Código fuente completo v1 (Estable v1.3.5) | 📦 ARCHIVE Sección 8-A |
| Código fuente completo v2 (ALT v1.3) | 📦 ARCHIVE Sección 8-B |
| Código fuente completo v3 (todos los archivos) | 📦 ARCHIVE Sección 8 |
| Código fuente real v4 (extraído del zip v4_3) | 📦 ARCHIVE Sección 8-C |
| Diseño v4 — on_action lógica, scripted_guis diseño | 9 |
| Diseño v4 — localización ES y EN (reescrita) | 10 |
| Diseño v4 — cancel_all exhaustivo (código completo) | 11 |
| Optimizador provincial — referencia de parámetros | 12 |
| Orden de pasos para codear v4 | 13 |
| Historial completo + resumen ejecutivo por versión | 📦 ARCHIVE Sección 14 |
| Información pendiente de encontrar | 15 |
| Exodos: Repartir Esclavos (Slave Distributor) | 16 |
| Tabla económica — valores de pop, equivalencias, justificación de costos | 17 |
| Decisiones de diseño descartadas | 📦 ARCHIVE Sección 18 |
| Log de decisiones por sesión (v4) — qué se decidió, qué quedó abierto | **19** |
| Log de sesiones pre-v4 | 📦 ARCHIVE Sección 19 |
| Protocolo de actualización del wiki — cuándo versionar, qué secciones tocar | **20** |
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

### ERROR 32 — Desc keys desacopladas de IDs de decisión (silent bug en v4.3.16)
El engine busca `<decision_id>_desc` para mostrar la descripción de una decisión.
En v4.3.16, la mayoría de las desc keys usan el patrón `exodos_X_desc` o `bom_X_desc`,
completamente desacoplado del ID. El engine no las encuentra y la descripción aparece vacía
— sin error en log.
Las únicas desc que funcionaban en v4.3.16: `iram_11_distribute_global_desc`,
`iram_12_constructor_auto_desc`, `iram_13_activate_optimize_global_desc`, y las de navegación
del menú en `iram_menu_l_english.yml`.
Corregido en v5.0 (TAREA 3d): todas las desc keys renombradas al patrón `<id_v5>_desc`.

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

### ERROR 28 — `global_pop_promotion_speed` y `global_pop_demotion_speed` NO son barras acumulativas

`global_pop_promotion_speed = 100` y `global_pop_demotion_speed = 100` NO funcionan como `global_pop_migration_speed`. El engine evalúa Ascenso/Descenso contra un threshold (`PROMOTE_DEMOTE_THRESHOLD = 0.005` en `defines/00_defines.txt`), no una barra que se llena. Un valor de 100 puede no tener el efecto esperado de forzar ascenso/descenso inmediato. **Comportamiento real sin testear en partida — verificar antes de documentar como funcional.**

### ERROR 29 — `remove_building_level` con llaves no existe en el engine
La sintaxis correcta es `remove_building_level = basic_settlement_infratructure_building` — sin llaves.
La variante `remove_building_level = { building = X }` no existe en IR 2.0.4 — el engine la ignora silenciosamente.
Confirmado en `common/scripted_effects/00_event_effects.txt` (`destroy_building_effect`).

### ERROR 30 — `remove_building_level` sin guard sobre building con 0 niveles genera error en log
Llamar `remove_building_level = X` sobre una province que no tiene ese building genera error en log.
Siempre envolver con guard: `if = { limit = { num_of_X > 0 } remove_building_level = X }`.
El engine vanilla usa este patrón en `destroy_building_effect` para todos los buildings.

### ERROR 31 — Usar `else_if` para demoler múltiples buildings
`destroy_building_effect` vanilla usa `if/else_if` porque destruye **uno solo** (el primero que encuentra).
El Constructor Automático necesita demoler **todos** — usar `if` independientes, uno por building.
`else_if` encadenado detiene la demolición en el primer building encontrado.
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
| Optimize Global | No existe | ✅ IMPLEMENTADO v4.3.16 — on_action completo (5 bloques/pulso, rangos auto) |

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

**R14** — Los chequeos de error en on_action son bloques únicos (no duplicar por operación). En Transfer: un bloque de chequeo de unidad destruida/perdida. En Gather Global: un bloque de cleanup de área sin procesadas. Ver Sección 9.2 del ARCHIVE para los patrones correctos.

**R19** — Antes de modificar cualquier archivo: describir el cambio en una oración y esperar confirmación explícita del operador. Sin excepción.

---

## 0.4d FLUJO DE TRABAJO

1. El usuario sube al inicio de la sesión: este documento + zip canónico activo (ver Sección 22) + SESSION_LOG reciente si existe.
2. La IA ejecuta el checklist del 0.2 antes de responder.
3. La IA trabaja siguiendo el orden de pasos de la Sección 13.
4. Antes de generar el zip final: la IA pregunta la hora al operador.
5. La IA entrega el zip final con BOM validado, nombre con fecha y hora (ver Sección 3.2.1), y SESSION_LOG de la sesión.
6. Instalación: extraer en `C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\`
7. **Primer paso obligatorio al cargar la partida: ejecutar "Cancelar todo".**

**Modelo a usar:**
- Sonnet sin pensamiento extendido: actualizaciones de documentos y codeo de decisiones de diseño ya cerradas.
- Sonnet con pensamiento extendido: solo para problemas de arquitectura sin solución clara.
- Haiku: no usar para trabajo de código.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0.5 — ESTADO ACTUAL DEL PROYECTO
# ══════════════════════════════════════════════════════════

**Última actualización:** 2026-06-03 (v3.4)

## 0.5.0 DASHBOARD — ESTADO DE UN VISTAZO

| Dimensión | Estado |
|---|---|
| Zip activo | ver Sección 22 |
| Versión | IRAM v4.3.16 |
| Hito de cierre v4 | ✅ ALCANZADO — GG + DG + OG + Constructor implementados |
| Bloqueadores activos | Ninguno — ver pendientes post-testeo en Sección 19.0 |
| Bugs conocidos en zip activo | Ninguno — 3 bugs corregidos en v4.3.16 |
| Última sesión | 2026-06-03 01:09 |

**Semáforo rápido:**
- ✅ Optimize Global — on_action implementado v4.3.16 (5 bloques/pulso, rangos auto)
- ✅ Distribute Global — on_action implementado v4.3.16 (5 bloques/pulso, rangos auto)
- ✅ Constructor Automático (`iram_12`) — implementado v4.3.16 (en `iram_decisions_menu.txt`)
- ✅ Sistema de menú navegable — implementado v4.2 (`iram_01` a `iram_21`)
- ✅ Demografía (Migración / Ascenso / Descenso Forzados) — implementado v4.1 (⚠ TESTEAR Ascenso/Descenso — ver ERROR 0.4 nuevo)
- ✅ Reliquia Un Pueblo Una Fe — implementada v4.0, renombrada en v4.3.2
- ✅ Gather Global con capital exclusion — implementado v4.0, costo reducido en v4.3.2, bugs corregidos en v4.3.7
- ✅ Heredero del Rival — integrado al menú en v4.3, condición `has_spouse` CERRADA (diseño aceptado: spawna sin familia si rival no tiene esposa)
- ✅ Refactor 44 IDs `iram_` con numeración — implementado v4.3.2
- ✅ BOM-como-texto — corregido en v4.0, reincidencia corregida en v4.3.7

*Actualizar este dashboard al inicio de cada sesión que cambie el estado del proyecto.*

## Estado por componente

| Componente | Estado | Zip canónico | Pendiente |
|---|---|---|---|
| **Constructor Automático (`iram_12`)** | ✅ IMPLEMENTADO v4.3.16 | `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` | — |
| **Exodos v3** | ✅ CERRADO | `mod_pack_IRAM_15.zip` | — |
| **IRAM v4 (Gather por área)** | ✅ DESCARTADA — reemplazada por Gather Global | — | — |
| **IRAM v4 (Distribute por área, 4 rangos)** | ✅ DESCARTADA — reemplazada por Distribute Global | — | — |
| **IRAM v4 (Transfer)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **IRAM v4 (Optimize por área, 4 rangos)** | ✅ DESCARTADA — reemplazada por Optimize Global | — | — |
| **Gather Global** | ✅ IMPLEMENTADO v4.0 — bugs corregidos v4.3.16 | `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` | ⚠ TESTEAR en partida |
| **Distribute Global** | ✅ IMPLEMENTADO v4.3.16 — on_action completo | `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` | — |
| **Optimize Global** | ✅ IMPLEMENTADO v4.3.16 — on_action completo | `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` | — |
| **Sistema de menú navegable** | ✅ IMPLEMENTADO v4.2 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Demografía — Relics (Un Pueblo, Una Fe)** | ✅ IMPLEMENTADO v4.0 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Demografía — Migración Forzada** | ✅ IMPLEMENTADO v4.1 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | ⚠ TESTEAR — 1 pop/tick/territorio, slaves no migran |
| **Demografía — Ascenso Forzado** | ✅ IMPLEMENTADO v4.1 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | ⚠ TESTEAR — sistema usa threshold, no barra 0→100 |
| **Demografía — Descenso Forzado** | ✅ IMPLEMENTADO v4.1 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | ⚠ TESTEAR — sistema usa threshold, no barra 0→100 |
| **Heredero del Rival** | ✅ IMPLEMENTADO — integrado al menú v4.3 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **BOM / IHA** | ✅ CERRADO | ambos zips | — |
| **TLV** | ✅ CERRADO | ambos zips | — |
| **TGL** | ✅ CERRADO | ambos zips | — |
| **Slave Distributor** | ✅ DESCARTADO | — | Optimize Global cubre la función |

## Bugs conocidos pendientes en el zip activo

Ninguno. Los 3 bugs de eventos GG/DG/OG (BUG A/B/C) fueron corregidos en v4.3.16 — ver Sección 19 entrada 2026-05-30 03:14.

## Próximos pasos

1. Testeo exhaustivo en partida — GG → DG → OG → Constructor → Demografía
2. Verificar comportamiento Ascenso/Descenso Forzado — threshold vs barra (protocolo en SESSION_LOG 2026-06-03 01:40 Parte 2)

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

## 3.2 Estructura de archivos — IRAM v5.1

**4 mods independientes.** Cada uno es activable por separado. Sin dependencias cruzadas en código.
Las carpetas raíz (`exodos/`, `by_other_means/`, etc.) y los archivos `.mod` raíz son **INTOCABLES** — savegame compatibility + dlc_load.json.

```
mod/
├── exodos.mod                                               ← sin BOM
├── by_other_means.mod                                       ← sin BOM
├── the_last_vote.mod                                        ← sin BOM
├── the_great_leap.mod                                       ← sin BOM
│
├── exodos/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── common/
│   │   ├── decisions/
│   │   │   ├── iram_exodos_menu.txt                         ← BOM UTF-8 (abrir/cerrar menú EXODOS)
│   │   │   ├── iram_exodos_cancel.txt                       ← BOM UTF-8 (cancel_all + cancel_bom)
│   │   │   ├── iram_exodos_gather_global.txt                ← BOM UTF-8 (iram_exodos_gather_global)
│   │   │   ├── iram_exodos_distribute_global.txt            ← BOM UTF-8 (iram_exodos_distribute_global)
│   │   │   ├── iram_exodos_optimize_global.txt              ← BOM UTF-8 (iram_exodos_optimize_global)
│   │   │   ├── iram_exodos_transfer.txt                     ← BOM UTF-8 (activate + confirm)
│   │   │   └── iram_exodos_constructor.txt                  ← BOM UTF-8 (constructor automático)
│   │   ├── on_action/
│   │   │   ├── iram_on_action_transfer.txt                  ← BOM UTF-8 (85 líneas)
│   │   │   ├── iram_on_action_gather_global.txt             ← BOM UTF-8 (597 líneas)
│   │   │   ├── iram_on_action_distribute_global.txt         ← BOM UTF-8 (431 líneas)
│   │   │   └── iram_on_action_optimize_global.txt           ← BOM UTF-8 (397 líneas)
│   │   ├── script_values/
│   │   │   └── iram_script_values.txt                       ← BOM UTF-8
│   │   ├── units/
│   │   │   └── iram_units.txt                               ← BOM UTF-8
│   │   ├── modifiers/
│   │   │   └── iram_relic_modifiers.txt                     ← BOM UTF-8 (4 modifiers)
│   │   └── scripted_effects/
│   │       └── iram_scripted_effects.txt                    ← BOM UTF-8
│   ├── events/
│   │   └── iram_events.txt                                  ← BOM UTF-8 (exodos.1–exodos.4)
│   └── localization/
│       ├── english/
│       │   ├── iram_exodos_l_english.yml                    ← BOM UTF-8
│       │   └── iram_menu_l_english.yml                      ← BOM UTF-8
│       └── spanish/
│           ├── iram_exodos_l_spanish.yml                    ← BOM UTF-8
│           └── iram_menu_l_spanish.yml                      ← BOM UTF-8
│
├── by_other_means/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── common/
│   │   ├── decisions/
│   │   │   ├── iram_bom_menu.txt                            ← BOM UTF-8 (menú BOM y submenús)
│   │   │   ├── iram_bom_decisions.txt                       ← BOM UTF-8 (confirm + bacanal + kill_ruler + seize + fill)
│   │   │   ├── iram_bom_ego_sum.txt                         ← BOM UTF-8 (4 decisiones Ego Sum)
│   │   │   ├── iram_bom_demografia.txt                      ← BOM UTF-8 (relics + migración + ascenso + descenso)
│   │   │   └── iram_bom_rival_heir.txt                      ← BOM UTF-8 (hijo + hija del rival)
│   │   └── scripted_effects/
│   │       └── iram_bom_scripted_effects.txt                ← BOM UTF-8
│   └── localization/
│       ├── english/
│       │   ├── iram_bom_l_english.yml                       ← BOM UTF-8
│       │   ├── iram_bom_menu_l_english.yml                  ← BOM UTF-8
│       │   ├── iram_bom_ego_sum_l_english.yml               ← BOM UTF-8
│       │   ├── iram_bom_demografia_l_english.yml            ← BOM UTF-8
│       │   └── iram_bom_relics_l_english.yml                ← BOM UTF-8
│       └── spanish/
│           ├── iram_bom_l_spanish.yml                       ← BOM UTF-8
│           ├── iram_bom_menu_l_spanish.yml                  ← BOM UTF-8
│           ├── iram_bom_ego_sum_l_spanish.yml               ← BOM UTF-8
│           ├── iram_bom_demografia_l_spanish.yml            ← BOM UTF-8
│           └── iram_bom_relics_l_spanish.yml                ← BOM UTF-8
│
├── the_last_vote/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/
│   │   └── iram_tlv_decisions.txt                           ← BOM UTF-8
│   ├── events/
│   │   └── tlv_events.txt                                   ← BOM UTF-8
│   └── localization/
│       ├── english/tlv_l_english.yml                        ← BOM UTF-8
│       └── spanish/tlv_l_spanish.yml                        ← BOM UTF-8
│
└── the_great_leap/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/
    │   └── iram_tgl_decisions.txt                           ← BOM UTF-8
    └── localization/
        ├── english/tgl_l_english.yml                        ← BOM UTF-8
        └── spanish/tgl_l_spanish.yml                        ← BOM UTF-8

dlc_load.json (NO MODIFICAR — savegame compatibility):
{
    "enabled_mods": [
        "mod/exodos.mod",
        "mod/by_other_means.mod",
        "mod/the_last_vote.mod",
        "mod/the_great_leap.mod"
    ]
}
```

**Cambios arquitectónicos v4 → v5.0:**
- Split en 4 mods independientes (BOM, TGL, TLV dejan de ser shells)
- `exodos/decisions/` → `exodos/decisions/`
- `exodos_on_action.txt` (único) → 4 archivos on_action separados (RE11)
- IDs de decisiones: numéricos (`iram_08`) → descriptivos (`iram_exodos_transfer_activate`)
- Localización modularizada por mod

## 3.2.1 Convención de nombres de archivos

### Zips de entrega

```
mod_pack_IRAM_vX_X_X_AAAA-MM-DD_HH-MM.zip
```

| Componente | Descripción | Ejemplo |
|---|---|---|
| `vX_X_X` | Versión del mod (mayor_menor_patch) | `v4_3_2` |
| `AAAA-MM-DD` | Fecha ISO 8601 | `2026-05-26` |
| `HH-MM` | Hora y minutos de generación (24h) | `01-56` |

Ejemplo completo: `mod_pack_IRAM_v4_3_2_2026-05-26_01-56.zip`

**Reglas:**
- Sin letras de sufijo (`_A`, `_B`, `_E`). La hora y minutos identifican unívocamente cada entrega.
- Sin espacios ni paréntesis. Los paréntesis que genera Windows al duplicar (`(1)`, `(2)`) indican duplicados — ver Sección 21.
- **Antes de generar cualquier archivo con nombre de fecha/hora: preguntar la hora al operador.** No asumir ni usar la hora del sistema.
- Los archivos activos siempre están registrados en Sección 22.

### Archivos del sistema de control

```
IRAM_SUPERBACKUP_vX_X_AAAA-MM-DD_HH-MM.md
IRAM_PROMPT_MAESTRO_vX_X_AAAA-MM-DD_HH-MM.md
IRAM_INSTRUCCIONES_HUMANO_AAAA-MM-DD_HH-MM.md
IRAM_SESSION_LOG_AAAA-MM-DD_HH-MM.md
```

### Logs de sesión

```
IRAM_SESSION_LOG_AAAA-MM-DD_HH-MM.md
```

Ejemplo: `IRAM_SESSION_LOG_2026-05-26_01-56.md`

## 3.3 Tabla de funciones

✅ **NOTA v3.6:** IDs descriptivos v5.0 implementados — zip activo `mod_pack_IRAM_v5_1_2026-06-08_01-28.zip`. Los IDs numéricos iram_01–iram_25 son legacy de v4 — ver ARCHIVE.

### MOD: exodos

| Función | ID v5 | Archivo | Estado |
|---|---|---|---|
| Menú EXODOS — abrir | `iram_exodos_menu_open` | exodos/decisions/iram_exodos_menu.txt | ✅ v5.1 |
| Menú EXODOS — cerrar | `iram_exodos_menu_close` | exodos/decisions/iram_exodos_menu.txt | ✅ v5.1 |
| Cancel All EXODOS | `iram_exodos_cancel_all` | exodos/decisions/iram_exodos_cancel.txt | ✅ v5.1 |
| Gather Global | `iram_exodos_gather_global` | exodos/decisions/iram_exodos_gather_global.txt | ✅ v5.1 |
| Distribute Global | `iram_exodos_distribute_global` | exodos/decisions/iram_exodos_distribute_global.txt | ✅ v5.1 |
| Optimize Global | `iram_exodos_optimize_global` | exodos/decisions/iram_exodos_optimize_global.txt | ✅ v5.1 |
| Constructor Automático | `iram_exodos_constructor_auto` | exodos/decisions/iram_exodos_constructor.txt | ✅ v5.1 |
| Transfer — Activar | `iram_exodos_activate_transfer` | exodos/decisions/iram_exodos_transfer.txt | ✅ v5.1 |
| Transfer — Confirmar | `iram_exodos_confirm_transfer` | exodos/decisions/iram_exodos_transfer.txt | ✅ v5.1 |

### MOD: by_other_means

| Función | ID v5 | Archivo | Estado |
|---|---|---|---|
| Menú BOM — abrir | `iram_bom_menu_open` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Menú BOM — cerrar | `iram_bom_menu_close` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Cancel All BOM | `iram_bom_cancel_all` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú BOM Acciones — abrir | `iram_bom_menu_bom_open` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú BOM Acciones — cerrar | `iram_bom_menu_bom_close` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Ego Sum — abrir | `iram_bom_menu_ego_open` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Ego Sum — cerrar | `iram_bom_menu_ego_close` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Demografía — abrir | `iram_bom_menu_demo_open` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Demografía — cerrar | `iram_bom_menu_demo_close` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Heredero — abrir | `iram_bom_menu_heir_open` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Submenú Heredero — cerrar | `iram_bom_menu_heir_close` | by_other_means/decisions/iram_bom_menu.txt | ✅ v5.1 |
| Eliminar Rival (confirm) | `iram_bom_confirm` | by_other_means/decisions/iram_bom_decisions.txt | ✅ v5.1 |
| Bacanal | `iram_bom_bacanal` | by_other_means/decisions/iram_bom_decisions.txt | ✅ v5.1 |
| Et tu Brute? (kill ruler) | `iram_bom_kill_ruler` | by_other_means/decisions/iram_bom_decisions.txt | ✅ v5.1 |
| Confiscar Propiedades (seize) | `iram_bom_seize_holdings` | by_other_means/decisions/iram_bom_decisions.txt | ✅ v5.1 |
| Fill the Void | `iram_bom_fill_the_void` | by_other_means/decisions/iram_bom_decisions.txt | ✅ v5.1 |
| Ego Sum — Mars | `iram_bom_ego_mars` | by_other_means/decisions/iram_bom_ego_sum.txt | ✅ v5.1 |
| Ego Sum — Iovis | `iram_bom_ego_iovis` | by_other_means/decisions/iram_bom_ego_sum.txt | ✅ v5.1 |
| Ego Sum — Mercurii | `iram_bom_ego_mercurii` | by_other_means/decisions/iram_bom_ego_sum.txt | ✅ v5.1 |
| Ego Sum — Minervae | `iram_bom_ego_minervae` | by_other_means/decisions/iram_bom_ego_sum.txt | ✅ v5.1 |
| Demo — Reliquia Divina | `iram_bom_demo_relic` | by_other_means/decisions/iram_bom_demografia.txt | ✅ v5.1 |
| Demo — Migración Forzada | `iram_bom_demo_migracion` | by_other_means/decisions/iram_bom_demografia.txt | ✅ v5.1 |
| Demo — Ascenso Forzado | `iram_bom_demo_ascenso` | by_other_means/decisions/iram_bom_demografia.txt | ✅ v5.1 |
| Demo — Descenso Forzado | `iram_bom_demo_descenso` | by_other_means/decisions/iram_bom_demografia.txt | ✅ v5.1 |
| Heredero — Hijo del Rival | `iram_bom_heir_son` | by_other_means/decisions/iram_bom_rival_heir.txt | ✅ v5.1 |
| Heredero — Hija del Rival | `iram_bom_heir_daughter` | by_other_means/decisions/iram_bom_rival_heir.txt | ✅ v5.1 |

### MOD: the_great_leap

| Función | ID v5 | Archivo | Estado |
|---|---|---|---|
| The Great Leap | `iram_tgl_purchase` | the_great_leap/decisions/iram_tgl_decisions.txt | ✅ v5.1 |

### MOD: the_last_vote

| Función | ID v5 | Archivo | Estado |
|---|---|---|---|
| The Last Vote | `iram_tlv_confirm` | the_last_vote/decisions/iram_tlv_decisions.txt | ✅ v5.1 |

**IDs numéricos v4 (iram_01–iram_25) — LEGACY.** Ver ARCHIVE. No existen en el zip activo v5.1.
## 3.4 Tabla de costos y condiciones — ecosistema completo v4

| Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | Condiciones extra |
|---|---|---|---|---|---|---|
| Exodos: Concentración (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Distribución (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Optimizar (confirm → sin costo) | — | — | — | — | — | ancla existente, área 100% propia |
| Exodos: Opt. Rango (decisión final) | 2000 | 10 | 5000 | +10 | ≤90 | exodos_optimize_active seteado |
| Exodos: Transferencia | 2000 | 10 | 5000 | +20 | ≤80 | ancla + destino existentes, owner=ROOT |
| Exodos: Gather Global | — | — | — | +50 | ≤90 | -50 popularidad gobernante, sin op. activa |
| Exodos: Optimize Global | — | — | — | +100 | ≤90 | -100 popularidad gobernante |
| Demografía: Crear Reliquia | 5000 | — | — | — | — | NOT has_country_modifier = iram_divine_relic |
| Demografía: Disolver Reliquia | — | — | — | — | — | has_country_modifier = iram_divine_relic |
| Demografía: Activar Migración Forzada | 2000 | — | — | — | — | NOT has_country_modifier = iram_migracion_forzada |
| Demografía: Desactivar Migración Forzada | — | — | — | — | — | has_country_modifier = iram_migracion_forzada |
| Demografía: Activar Ascenso Forzado | 2000 | — | — | — | — | NOT has_country_modifier = iram_ascenso_forzado |
| Demografía: Desactivar Ascenso Forzado | — | — | — | — | — | has_country_modifier = iram_ascenso_forzado |
| Demografía: Activar Descenso Forzado | 2000 | — | — | — | — | NOT has_country_modifier = iram_descenso_forzado |
| Demografía: Desactivar Descenso Forzado | — | — | — | — | — | has_country_modifier = iram_descenso_forzado |
| Heredero — Hijo del Rival | — | — | — | — | — | 1 rival exacto, ≥16, is_male, employer=ROOT |
| Heredero — Hija del Rival | — | — | — | — | — | 1 rival exacto, ≥16, is_male, employer=ROOT |
| BOM: Eliminar Rivales | 2000 | 1 | 500 | +40 | ≤80 | rivals ≥ 1 |
| BOM: Bacanal | 500 | — | — | +10 | ≤90 | rivals ≥ 1 |
| BOM: Et tu Brute? | 2000 | 1 | 500 | +40 | ≤60 | stability ≥ 50 |
| IHA: Confiscar Propiedades | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| IHA: Fill the Void | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, employer=ROOT |
| TLV: Confirm | 2000 | — | — | +40 | ≤60 | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL: Purchase | dinámico | — | — | +100 | ≤0 | one-shot |

> Manpower: valor en script = valor pantalla / 500. El engine multiplica ×500 al mostrar.
> Gather Global: costo reducido de 100/−100 a 50/−50 en v4.3.2.

> ⚠️ **COSTOS ELIMINADOS TEMPORALMENTE PARA TEST (desde v4.3.2)**
> Los siguientes costos y condiciones fueron removidos del zip canónico activo para facilitar el test amplio de las funciones nuevas. Esta tabla es la referencia para restaurarlos una vez completado el testeo.
>
> | Función | Costo/Condición eliminada |
> |---|---|
> | Transfer | 2000 oro, 5000 manpower, tyranny ≤ 80 |
> | Gather Global | tyranny +50, popularidad −50, tyranny ≤ 90, popularidad ≥ −50 |
> | Demografía: Activar Reliquia | 5000 oro |
> | Demografía: Activar Migración Forzada | 2000 oro |
> | Demografía: Activar Ascenso Forzado | 2000 oro |
> | Demografía: Activar Descenso Forzado | 2000 oro |
> | BOM, IHA, TLV, TGL | costos y tyranny caps eliminados |
>
> Condiciones que se mantienen durante el test (guards funcionales, no son costos):
>
> | Función | Condición mantenida |
> |---|---|
> | Relics/Migración/Ascenso/Descenso | `NOT has_country_modifier` / `has_country_modifier` |
> | BOM | rivals ≥ 1, stability, tyranny cap |
> | TLV | is_republic, stability ≥ 50, popularity ≥ 50 |
> | TGL | one-shot |
> | Transfer | ancla + destino existentes, owner=ROOT |

## 3.5 Unidades marcadoras

### v5.1 — Transfer (ACTIVO)

| sub_unit | Nombre ES | Variable de unit | movement_speed | Uso |
|---|---|---|---|---|
| `exodos_marker` | "Exodos - Origen" | `exodos_unit_transfer_origin` | 5 | Unidad ancla origen Transfer |
| `exodos_marker` | "Exodos - Destino" | `exodos_unit_transfer_dest` | 5 | Unidad destino Transfer |

Transfer es la única operación que sigue usando unidades marcadoras en v5.1. GG, DG y OG operan por decisions + on_action puro — sin unidades.

### v3/v4 — Operaciones por área (LEGACY — no existen en v5.1)

| sub_unit | Variable | Uso original |
|---|---|---|
| `exodos_marker` | `exodos_unit_concentrate` | Gather por área — descartado |
| `exodos_marker` | `exodos_unit_distribute` | Distribute por área — descartado |
| `exodos_marker` | `exodos_unit_optimize` | Optimize por área — descartado |

> **Nota histórica:** la rama experimental `mod_pack_IRAM_v4_3.zip` introdujo `exodos_anchor` (`movement_speed = 0`) y redujo las marcadoras a 2 unidades. Esa arquitectura fue descartada. Ver Sección 18.4 del ARCHIVE.
## 3.6 Variables de estado

### Variables de país

| Variable | v3/v4 | v5.1 | Uso |
|---|---|---|---|
| `iram_exodos_menu` | ✗ | ✓ | Menú EXODOS abierto |
| `iram_transfer_pending` | ✗ | ✓ | Transfer: estado intermedio Activar → Confirmar |
| `iram_transfer_active` | ✗ | ✓ | Transfer en ejecución (guard on_action transfer) |
| `iram_global_active` | ✗ | ✓ | Gather Global en ejecución (guard on_action GG) |
| `iram_distribute_global_active` | ✗ | ✓ | Distribute Global en ejecución (guard on_action DG) |
| `iram_optimize_global_active` | ✗ | ✓ | Optimize Global en ejecución (guard on_action OG) |
| `iram_bom_active` | ✗ | ✓ | Agregador: cualquier estado BOM persistente activo |
| `iram_bom_menu` | ✗ | ✓ | Menú BOM abierto |
| `iram_bom_menu_bom` | ✗ | ✓ | Submenú BOM Acciones abierto |
| `iram_bom_menu_ego` | ✗ | ✓ | Submenú Ego Sum abierto |
| `iram_bom_menu_demo` | ✗ | ✓ | Submenú Demografía abierto |
| `iram_bom_menu_heir` | ✗ | ✓ | Submenú Heredero abierto |
| `iram_bom_ego_mars_used` | ✗ | ✓ | One-shot Ego Sum Mars (por partida) |
| `iram_bom_ego_iovis_used` | ✗ | ✓ | One-shot Ego Sum Iovis (por partida) |
| `iram_bom_ego_mercurii_used` | ✗ | ✓ | One-shot Ego Sum Mercurii (por partida) |
| `iram_bom_ego_minervae_used` | ✗ | ✓ | One-shot Ego Sum Minervae (por partida) |
| `tgl_purchased` | ✓ | ✓ | One-shot TGL |
| `exodos_anchor_province` | ✓ | ✗ legacy | Province ancla Transfer — renombrado en v5 |
| `exodos_destination_province` | ✓ | ✗ legacy | Province destino Transfer — renombrado en v5 |
| `exodos_pulse_counter` | ✓ | ✗ legacy | Contador Transfer — renombrado en v5 |
| `exodos_operation_active` | ✓ | ✗ eliminada | Guard global v4 — no existe en v5 |
| `exodos_global_active` | ✗ | ✗ eliminada | Nombre v4 de GG — reemplazado por `iram_global_active` |
| `exodos_distribute_global_active` | ✗ | ✗ eliminada | Nombre v4 de DG — reemplazado por `iram_distribute_global_active` |
| `exodos_optimize_global_active` | ✗ | ✗ eliminada | Nombre v4 de OG — reemplazado por `iram_optimize_global_active` |
| `exodos_transfer_active` | ✓ | ✗ eliminada | Nombre v4 de Transfer — reemplazado por `iram_transfer_active` |
| `iram_menu_open` | ✗ | ✗ eliminada | Menú v4 unificado — no existe en v5 (mods independientes) |
| `iram_menu_management_open` | ✗ | ✗ eliminada | Submenú v4 — no existe en v5 |
| `iram_menu_behavior_open` | ✗ | ✗ eliminada | Submenú v4 — no existe en v5 |
| `iram_menu_political_open` | ✗ | ✗ eliminada | Submenú v4 — no existe en v5 |
| `iram_rival_heir_open` | ✗ | ✗ eliminada | Submenú v4 — reemplazado por `iram_bom_menu_heir` |
| `bom_ego_sum_mars_used` | ✓ | ✗ legacy | Nombre v4 — reemplazado por `iram_bom_ego_mars_used` |
| `bom_ego_sum_iovis_used` | ✓ | ✗ legacy | Nombre v4 — reemplazado |
| `bom_ego_sum_mercurii_used` | ✓ | ✗ legacy | Nombre v4 — reemplazado |
| `bom_ego_sum_minervae_used` | ✓ | ✗ legacy | Nombre v4 — reemplazado |

> Variables legacy (nombres v4 con prefijo `exodos_`): limpiar con `iram_exodos_cancel_all` + `iram_bom_cancel_all` antes de actualizar a v5.

### Variables de gobernante (scope character)

| Variable | v5.1 | Uso |
|---|---|---|
| `iram_bom_ego_gobernante_used` | ✓ | One-shot Ego Sum por gobernante (independiente del one-shot por partida) |

### Variables de province

| Variable | Uso |
|---|---|
| `exodos_gather_global_done` | Province ya procesada por GG (limpiada en cleanup) |
| `exodos_distribute_global_done` | Province ya procesada por DG (limpiada en cleanup) |
| `exodos_optimize_global_done` | Province ya procesada por OG (limpiada en cleanup) |
| `exodos_is_anchor` | Province ancla Transfer — excluida de iteración |
| `exodos_is_destination` | Province destino Transfer |

### Variables de unidad

| Variable | Estado | Uso |
|---|---|---|
| `exodos_unit_transfer_origin` | ✓ activa | Unidad origen Transfer |
| `exodos_unit_transfer_dest` | ✓ activa | Unidad destino Transfer |
| `exodos_unit_concentrate` | ✗ legacy | Gather por área — no existe en v5 |
| `exodos_unit_distribute` | ✗ legacy | Distribute por área — no existe en v5 |
| `exodos_unit_optimize` | ✗ legacy | Optimize por área — no existe en v5 |

### Modifiers de país (iram_relic_modifiers.txt)

| Modifier | Efecto | Activado por |
|---|---|---|
| `iram_divine_relic` | `global_pop_conversion_speed = 50`, `global_pop_assimilation_speed = 50` | `iram_bom_demo_relic` |
| `iram_migracion_forzada` | `global_pop_migration_speed = 100` | `iram_bom_demo_migracion` |
| `iram_ascenso_forzado` | `global_pop_promotion_speed = 100` | `iram_bom_demo_ascenso` |
| `iram_descenso_forzado` | `global_pop_demotion_speed = 100` | `iram_bom_demo_descenso` |
## 3.7 Panel de decisiones — qué aparece cuándo — diseño cerrado v5.0

El sistema de menú usa variables de estado para controlar visibilidad. Cada mod es independiente — no hay menú unificado en v5.1. RD1 vigente: `potential` solo contiene `is_ai = no` + variable de estado del nivel correspondiente.

### MOD: exodos

**Siempre visible (`potential = { is_ai = no }`):**
- `iram_exodos_menu_open` — Abrir Menú EXODOS
- `iram_exodos_cancel_all` — Cancelar Todo EXODOS (botón de pánico, `allow = { always = yes }`)

**Con `iram_exodos_menu` activo:**
- `iram_exodos_menu_close`
- `iram_exodos_gather_global` — en gris si op activa (`iram_tt_exodos_sin_op`)
- `iram_exodos_distribute_global` — ídem
- `iram_exodos_optimize_global` — ídem
- `iram_exodos_constructor_auto` — ídem
- `iram_exodos_activate_transfer` — en gris si op activa o transfer ya pendiente (`iram_tt_exodos_transfer_ya_activa`)

**Con `iram_transfer_pending` activo (EXCEPCIÓN RD1 — estado operacional):**
- `iram_exodos_confirm_transfer`

### MOD: by_other_means

**Siempre visible (`potential = { is_ai = no }`):**
- `iram_bom_menu_open` — Abrir Menú BOM
- `iram_bom_cancel_all` — Cancelar Todo BOM (botón de pánico, `allow = { always = yes }`)

**Con `iram_bom_menu` activo:**
- `iram_bom_menu_close`
- `iram_bom_menu_bom_open`
- `iram_bom_menu_ego_open`
- `iram_bom_menu_demo_open`
- `iram_bom_menu_heir_open`

**Con `iram_bom_menu_bom` activo + NOT ego activo:**
- `iram_bom_menu_bom_close`
- `iram_bom_confirm` — en gris si sin rival (`iram_tt_bom_rival`)
- `iram_bom_bacanal` — ídem
- `iram_bom_kill_ruler` — ídem
- `iram_bom_seize_holdings` — en gris si no rival único (`iram_tt_bom_rival_unico`)
- `iram_bom_fill_the_void` — ídem
- `iram_bom_menu_ego_open` — acceso a Ego Sum
- `iram_bom_menu_heir_open` — acceso a Heredero

**Con `iram_bom_menu_ego` activo:**
- `iram_bom_menu_ego_close`
- `iram_bom_ego_mars` — en gris si ya usado (por partida o por gobernante)
- `iram_bom_ego_iovis` — ídem
- `iram_bom_ego_mercurii` — ídem
- `iram_bom_ego_minervae` — ídem

**Con `iram_bom_menu_demo` activo:**
- `iram_bom_menu_demo_close`
- `iram_bom_demo_relic` — en gris si modifier ya activo
- `iram_bom_demo_migracion` — ídem
- `iram_bom_demo_ascenso` — ídem
- `iram_bom_demo_descenso` — ídem

**Con `iram_bom_menu_heir` activo:**
- `iram_bom_menu_heir_close`
- `iram_bom_heir_son`
- `iram_bom_heir_daughter`

### MOD: the_great_leap

**Con guards propios (`potential = { is_ai = no }`):**
- `iram_tgl_purchase` — one-shot; en gris si ya comprado (`iram_tt_tgl_purchased`) o sin ciudades (`iram_tt_tgl_ciudades`)

### MOD: the_last_vote

**Con guards propios (`potential = { is_ai = no }`):**
- `iram_tlv_confirm` — en gris si no república (`iram_tt_tlv_republic`)

---

> **Panel v4 (IDs iram_01–iram_25, menú unificado):** ver ARCHIVE.
# SECCIÓN 4 — FLUJO COMPLETO DE OPERACIONES — v4
# ══════════════════════════════════════════════════════════

**Principios comunes a todas las operaciones:**
- El jugador posiciona el ancla usando la decisión `exodos_confirm_X` — la ancla es la province donde se concentrará el trabajo.
- Solo una operación activa a la vez — guard: `exodos_operation_active`.
- El jugador paga en la última decisión que desata la función.
- Sin cooldown — se rehabilitan inmediatamente tras éxito o cancelación.

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
| Calibración números Distribute Global (counts 4/9/14) | ✅ CERRADO — counts 4/9/14 confirmados por diseño | — | 2026-06-03 01:40 |
| Caveat `\n\n` en localizaciones | ⚠️ PENDIENTE — verificar en testeo en juego | Puede no renderizar como salto de línea | 2026-05-29 05:49 |
| Ascenso/Descenso Forzado — threshold vs barra | ⚠️ PENDIENTE testeo | Modifier actúa ×100 sobre el umbral, no como barra acumulativa — protocolo en SESSION_LOG 2026-06-03 01:40 Parte 2 | 2026-06-03 01:40 |
| `valor_rp = 0.023223` — nunca verificado contra el engine | ⚠️ Sin verificar | Debilita el argumento del modelo económico (no bloquea código) | 2026-05-19 |
| Operaciones por área | ✅ CERRADO — removidas intencionalmente; GG/DG/OG reemplazan la función globalmente | — | 2026-06-03 01:40 |
| Skill PDX modding (`/mnt/skills/user/pdxscript/SKILL.md`) | ⚠️ PENDIENTE POST-V4 | Reglas genéricas del engine, reutilizable en futuros mods | 2026-05-27 20:06 |
| Template de proyecto basado en sistema IRAM | ⚠️ PENDIENTE POST-V4 | Reutilizable fuera de PDX | 2026-05-27 20:06 |
| `global_pop_migration_speed` — token inválido en IR 2.0.5 | ✅ CERRADO — reemplazado por `global_migration_speed_modifier = 1.0` en v5.3 | — | 2026-06-09 |
| `global_pop_promotion_speed = 100` y `global_pop_demotion_speed = 100` — behavior con values altos | ⚠️ PENDIENTE testeo | Sistema usa threshold (0.005), comportamiento con value 100 sin verificar | 2026-06-09 |
| Bloque nativo `decisions = {}` de IR — inmutable desde el mod | ✅ CERRADO — stubs `potential = { always = no }` en `iram_compat_legacy.txt` (v5.3) | — | 2026-06-09 |

---

## 2026-06-09 03:22b — Versiones .mod actualizadas (v5.5)

### ✅ Cerrado

- **Versión en los 4 `.mod` raíz actualizada a 5.4:**
  Los archivos `exodos.mod`, `by_other_means.mod`, `the_great_leap.mod`, `the_last_vote.mod`
  decían `version = "5.0"` desde el rebuild v5.0. Actualizados a `version = "5.4"`.
  Los `descriptor.mod` internos ya decían `5.0` — se mantienen sin cambio (savegame compat).
  Sin BOM en `.mod` ✅

---

## 2026-06-09 03:22 — Navegación progresiva de menús (v5.4)

### ✅ Cerrado

- **Fix navegación — guards cruzados incompletos en potential:**
  Las 5 decisiones de  tenían guard de ego ()
  pero no de heredero. Al abrir Heredero las acciones políticas seguían visibles en gris.
  Fix 1:  agregado a las 5 decisiones.
  Fix 2:  agregado a 
  — el botón de cerrar ya no aparece durante el flujo de dos pasos de Transfer.
  Resultado: navegación estrictamente progresiva — cada pantalla muestra solo su nivel.

### ⚠️ Premisas no verificadas activas

- Caveat  en localizaciones — verificar en testeo.
-  — sin verificar.
- Ascenso/Descenso threshold — verificar en testeo (ERROR 28).

---

## 2026-06-09 — Diagnóstico error.log + bugfix v5.3

### ✅ Cerrado

- **Bug A — Loc keys de eventos con namespace incorrecto:**
  El rename `namespace = exodos` → `namespace = iram` de v5.0 nunca se propagó a los YMLs.
  Los eventos `iram.1`–`iram.4` esperaban keys `iram.X.t/d/ok`; los YMLs definían `exodos.X.t/d/ok`.
  Resultado en juego: pop-ups de operación completa/fallo en blanco.
  Consecuencia en log: `Unknown formatting tag '.'` × 16 (el punto en la raw key fallback
  era parseado como formatting tag por pdx_text_formatter).
  Fix: 12 renames en `iram_exodos_l_english.yml` e `iram_exodos_l_spanish.yml`.

- **Bug B — `global_pop_migration_speed` no existe en IR 2.0.5:**
  Token verificado en `common/modifiers/00_hardcoded.txt` del juego — no existe.
  Fix: `global_pop_migration_speed = 100` → `global_migration_speed_modifier = 1.0`
  en `iram_relic_modifiers.txt`. Valor 1.0 = +100% velocidad de migración.
  Tokens del mismo archivo auditados:
  - `global_migration_speed_modifier` — VÁLIDO (multiplicador, vanilla: 0.05–0.1)
  - `global_pop_promotion_speed` — VÁLIDO (flat, vanilla base = 2.5)
  - `global_pop_conversion_speed` — asumido válido (sin error en log)
  - `global_pop_assimilation_speed` — asumido válido (sin error en log)
  - `global_pop_demotion_speed` — asumido válido (sin error en log)
  - `global_pop_migration_speed` — **NO EXISTE en IR 2.0.5**

- **Error C — `Failed to read key reference` × 16 (saves antiguas):**
  IR almacena IDs de decisiones tomadas en un bloque nativo `decisions = {}` del gamestate.
  Este bloque es **inmutable desde el mod** — el engine lo escribe, ningún scripted effect
  puede borrar entradas de él. `cancel_all` no puede solucionarlo.
  Save analizada: `ROMA_WC.rome` (IR 2.0.5, Ironman binario) — 16 IDs legacy en línea ~1156097.
  Fix: nuevo archivo `exodos/decisions/iram_compat_legacy.txt` con 16 stubs
  `potential = { always = no }`. Nunca visibles al jugador.
  IDs cubiertos: `tgl_purchase_all_innovations`, `bom_ego_sum_mars/minervae/mercurii/iovis`,
  `exodos_activate_gather/transfer/distribute`, `exodos_spawn_rival_son/daughter`,
  `iram_remove_divine_relic`, `bom_confirm`, `bom_bacanal`, `bom_kill_ruler`,
  `iha_seize_holdings`, `iha_fill_the_void`.

### ❓ Quedó abierto

- `global_pop_promotion_speed = 100` y `global_pop_demotion_speed = 100` — sistema usa
  threshold (0.005), comportamiento con value 100 sin verificar en engine.

### ⚠️ Premisas no verificadas activas

- Caveat `\n\n` en localizaciones — verificar en testeo.
- `valor_rp = 0.023223` — sin verificar.
- Ascenso/Descenso threshold — verificar en testeo (ERROR 28).

---

# SECCIÓN 20 — PROTOCOLO DE ACTUALIZACIÓN DEL TECHNICAL_WIKI
# ══════════════════════════════════════════════════════════

**Regla general:** el TECHNICAL_WIKI documenta diseño y decisiones. El zip documenta implementación.
Cuando divergen: el zip manda para código v4, el TECHNICAL_WIKI manda para diseño.

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

Antes de guardar una nueva versión del TECHNICAL_WIKI, verificar:
- [ ] El header refleja "ver Sección 22" (no un nombre hardcodeado)
- [ ] El footer (`*IRAM TECHNICAL_WIKI vX.Y*`) está actualizado
- [ ] Los cambios están registrados en Sección 14
- [ ] Los bugs pendientes en Sección 0.5 están al día
- [ ] No hay crossovers entre secciones (ej: tabla de rangos vs localización vs comentarios del zip)
- [ ] La entrada de Sección 19 documenta lo decidido y lo que quedó abierto
- [ ] La Sección 22 refleja los nombres actuales de todos los archivos activos
- [ ] INSTRUCCIONES_HUMANO actualizado si hubo cambios en el sistema de control
- [ ] SESSION_LOG generado para esta sesión

## 20.4 Cuándo actualizar INSTRUCCIONES_HUMANO

Actualizar `IRAM_INSTRUCCIONES_HUMANO` cuando cambie cualquiera de estos:
- Nombres de archivos del sistema de control (SUPERBACKUP, PROMPT_MAESTRO, zip)
- Orden de carga al inicio de sesión
- Protocolo de fin de sesión
- Smoke test (preguntas o criterios de validación)
- Protocolo de reanudación desde pausa larga

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
- Para trabajo activo: cargar el zip indicado en Sección 22
- Para referencia de v3 estable: cargar `mod_pack_IRAM_15.zip`
- Para análisis histórico: cargar el zip de la versión específica
- Para investigación de la arquitectura scripted_gui: `mod_pack_IRAM_v4_3.zip` — ver Sección 18.4
- Nunca mezclar código de zips distintos sin verificar diferencias en Sección 0.4b

# SECCIÓN 22 — ARCHIVOS ACTIVOS DEL PROYECTO
# ══════════════════════════════════════════════════════════

**Actualizar esta tabla cada vez que se genera una versión nueva de cualquier archivo.**
Es la única fuente de verdad para nombres de archivos activos. Todos los demás lugares del proyecto referencian esta sección.

| Archivo | Nombre actual | Versión |
|---------|--------------|---------| 
| TECHNICAL_WIKI (ACTIVE) | `IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md` | v3.9 |
| TECHNICAL_WIKI (ARCHIVE) | `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09.md` | v3.7 |
| PROMPT_MAESTRO | `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md` | v5.2 |
| SESSION_LOG (último) | `IRAM_SESSION_LOG_v5_5_2026-06-09_03-22.md` | v5.5 |
| Zip canónico | `mod_pack_IRAM_v5_5_2026-06-09_03-22.zip` | v5.5 |

**Reglas:**
- Esta tabla se actualiza al final de cada sesión que genere un archivo nuevo.
- El SESSION_LOG se carga al inicio de la sesión siguiente si existe. No es bloqueante si no existe.
- Para historial completo de zips: ver Sección 21.
---

*IRAM TECHNICAL WIKI ACTIVE v3.10 — 2026-06-09*
*IRAM v5.5 — listo para testeo en juego | Engine: Imperator Roma 2.0.4*
*Archivos activos: ver Sección 22*
*Cambios v3.10: Secciones 1, 2, 4.1, 4.2, 4.4, 9, 10, 11, 13, 16 eliminadas (contenido en ARCHIVE). Entradas Sec19 pre-v5 movidas al ARCHIVE v3.7. Sección 21.1 eliminada. Rutas decisions/ corregidas (sin common/). Sec22 actualizada.*
