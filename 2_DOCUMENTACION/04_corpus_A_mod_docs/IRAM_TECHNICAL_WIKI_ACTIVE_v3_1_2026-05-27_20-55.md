# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK
## TECHNICAL WIKI ACTIVE — v3.0
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | archivos activos: ver Sección 22

**Este documento es el ACTIVE del TECHNICAL WIKI.** Contiene todo lo necesario para sesiones de código.
El historial narrativo, código fuente v1/v2/v3, y decisiones descartadas están en el **TECHNICAL_WIKI_ARCHIVE_v3_0**.

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 0 — INSTRUCCIONES PARA LA IA
# LEER COMPLETO ANTES DE ESCRIBIR CUALQUIER LÍNEA
# ══════════════════════════════════════════════════════════

## 0.1 QUÉ ES ESTE DOCUMENTO

Este documento (ACTIVE) es la **fuente de verdad operativa** del proyecto IRAM para sesiones de código.
Cubre el diseño completo de IRAM v4, gotchas del engine, estado del proyecto, flujos, localizaciones y log de decisiones v4.

El historial narrativo (v1→v3), código fuente v1/v2/v3, y decisiones descartadas están en el **TECHNICAL_WIKI_ARCHIVE_v3_0** — cargar ese archivo solo cuando sea explícitamente necesario.

**Archivos activos del proyecto:** ver Sección 22.

Para comparación histórica con v3: `mod_pack_IRAM_15.zip` (v3 FINAL, cerrado).
Para código fuente v1/v2/v3 o historial detallado: ver TECHNICAL_WIKI_ARCHIVE_v3_0.

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
con 📦 están en el **TECHNICAL_WIKI_ARCHIVE_v3_0** — cargar ese archivo solo si son necesarias.

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

**Última actualización:** 2026-05-27 (v2.6)

## 0.5.0 DASHBOARD — ESTADO DE UN VISTAZO

| Dimensión | Estado |
|---|---|
| Zip activo | ver Sección 22 |
| Versión | IRAM v4.3.7 |
| Hito de cierre v4 | Optimize Global on_action implementado |
| Bloqueadores activos | Ver Sección 19.0 |
| Bugs conocidos en zip activo | Ninguno — 5 bugs corregidos en v4.3.7 |
| Última sesión | 2026-05-27 17:14 |

**Semáforo rápido:**
- 🔧 Optimize Global — stub corregido (v4.3.7), on_action pendiente (ver Sección 19.0)
- 🔧 Constructor Automático (`iram_12`) — diseño CERRADO, código pendiente (ver Sección 19 sesión 15:12)
- ✅ Sistema de menú navegable — implementado v4.2 (`iram_01` a `iram_41`)
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
| **Constructor Automático (`iram_12`)** | 🔧 DISEÑO CERRADO — código pendiente | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | Codear decisión + localizaciones ES/EN |
| **Exodos v3** | ✅ CERRADO | `mod_pack_IRAM_15.zip` | — |
| **Exodos v4 (Gather por área)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Exodos v4 (Distribute por área, 4 rangos)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Exodos v4 (Transfer)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Exodos v4 (Optimize por área, 4 rangos)** | ✅ IMPLEMENTADO | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | — |
| **Gather Global** | ✅ IMPLEMENTADO v4.0 — bugs corregidos v4.3.7 | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | ⚠ TESTEAR en partida |
| **Optimize Global** | 🔧 STUB CORREGIDO — on_action pendiente | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | on_action (5 bloques/pulso, rangos auto), exodos.3, guards, cleanup — ver Sección 19.0 |
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

Ninguno. Los 5 bugs de v4.3.6 fueron corregidos en v4.3.7 — ver Sección 19 entrada 2026-05-27 17:14.

## Próximos pasos

1. Codear `iram_12_constructor_auto` completo (decisión + localizaciones ES/EN) — diseño CERRADO, ver Sección 19 sesión 15:12
2. Diseñar y codear Distribute Global (`iram_11`) — ver Sección 19 entrada 2026-05-26 16:54
3. Implementar Optimize Global on_action (5 bloques/pulso, rangos automáticos por pops de capital)
4. Agregar `exodos.3` (evento silencioso de cleanup 365 días)
5. Actualizar `exodos_cleanup_effect` con 3 variables nuevas

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
| IRAM v4.0 | IRAM v4.0 | `mod_pack_IRAM_v4_0.zip` | **🗃 HISTÓRICO** | Decisions + on_action puro, sin rival en Exodos, Gather Global, Distribute 4 rangos, Relics |
| IRAM v4.1 | IRAM v4.1 | `mod_pack_IRAM_v4_1_2026-05-23_A.zip` | **🗃 HISTÓRICO** | Separación de archivos por función, iram_decisions_demografia.txt (Relics + Migración + Ascenso + Descenso) |
| IRAM v4.2 | IRAM v4.2 | `mod_pack_IRAM_v4_2_2026-05-25_B.zip` | **🗃 HISTÓRICO** | Sistema de menú navegable (`iram_01`–`iram_11`), iram_decisions_menu.txt nuevo |
| IRAM v4.3 | IRAM v4.3 | `mod_pack_IRAM_v4_3_2026-05-25_C.zip` | **🗃 HISTÓRICO** | Heredero del Rival integrado al menú (`has_variable = iram_rival_heir_open`) |
| IRAM v4.3.2 | IRAM v4.3.2 — canónico activo | `mod_pack_IRAM_v4_3_2_2026-05-25_E.zip` | **🔧 EN DESARROLLO** | Refactor 44 IDs `iram_` con numeración, costo GG reducido, stub Optimize Global, exodos.2 |

## 1.2 Evolución de las funciones por versión

| Función | v1 | v2 | v3 | v4.0 | v4.1 | v4.2 | v4.3 | v4.3.2 |
|---|---|---|---|---|---|---|---|---|
| Gather (por área) | ✓ spawn capital, rival req. | ✓ spawn rival, sin war | ✓ igual v2 | ✓ sin rival | = | = | = | = |
| Distribute (por área, 4 rangos) | ✓ spawn capital, rival req. | ✓ spawn rival | ✓ igual v2 | ✓ 4 rangos, sin rival | = | = | = | = |
| Transfer | ✓ spawn capital, war req. | ✓ sin war | ✓ igual v2 | ✓ sin rival | = | = | = | = |
| Optimize (por área, 4 rangos) | ✗ | ✗ | ✓ 4 rangos, rival req. | ✓ 4 rangos, sin rival | = | = | = | = |
| Gather Global | ✗ | ✗ | ✗ | ✓ 10 áreas/pulso, tyranny 100 | = | = | = | ✓ tyranny reducido a 50 |
| Optimize Global | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | 🔧 stub implementado, on_action pendiente |
| Sistema de menú navegable | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ iram_01–iram_11 | = | ✓ iram_01–iram_45 (refactor IDs) |
| Demografía — Relics | ✗ | ✗ | ✗ | ✓ exodos_decisions_relics.txt | ✓ movido a iram_decisions_demografia.txt | = | = | ✓ ID renombrado iram_22/23 |
| Demografía — Migración Forzada | ✗ | ✗ | ✗ | ✗ | ✓ iram_decisions_demografia.txt | = | = | ✓ ID renombrado iram_24/25 |
| Demografía — Ascenso Forzado | ✗ | ✗ | ✗ | ✗ | ✓ iram_decisions_demografia.txt | = | = | ✓ ID renombrado iram_26/27 |
| Demografía — Descenso Forzado | ✗ | ✗ | ✗ | ✗ | ✓ iram_decisions_demografia.txt | = | = | ✓ ID renombrado iram_28/29 |
| Heredero del Rival | ✗ | ✗ | ✓ v1.6 matrilineal | ✓ sin cambios | = | = | ✓ integrado al menú (has_variable = iram_rival_heir_open) | ✓ IDs renombrados iram_42/43 |
| BOM / IHA / Ego Sum | ✓ | ✓ | ✓ | ✓ sin cambios | = | = | = | ✓ IDs renombrados iram_31–39 |
| The Last Vote | ✓ | ✓ | ✓ | ✓ sin cambios | = | = | = | ✓ ID renombrado iram_44 |
| The Great Leap | ✓ | ✓ | ✓ | ✓ sin cambios | = | = | = | ✓ ID renombrado iram_45 |
| Slave Distributor | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✅ DESCARTADO — Optimize Global cubre la función |

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 2 — ESTADO ACTUAL
# ══════════════════════════════════════════════════════════

## 2.1 Estado de IRAM v4

| Item | Estado |
|---|---|
| Versión activa | v4.3.2 — `mod_pack_IRAM_v4_3_2_2026-05-25_E.zip` |
| Base de código | IRAM v3 (`mod_pack_IRAM_15.zip`) + Gather Global + todo el desarrollo 22–25/05 |
| Diseño global | CERRADO (arquitectura decisions + on_action puro, sin scripted_gui) |
| `exodos_scripted_effects.txt` | ✅ ACTUALIZADO — agrega `iram_cleanup_menu` e `iram_cleanup_demografia` como scripted_effects separados |
| `exodos_units.txt` | ✅ SIN CAMBIOS vs v3 |
| `exodos_decisions_gather_distribute.txt` | ✅ ELIMINADO — separado en `exodos_decisions_gather.txt` y `exodos_decisions_distribute.txt` |
| `exodos_decisions_gather.txt` | ✅ IMPLEMENTADO — IDs `iram_08_activate_gather`, `iram_09_confirm_gather` |
| `exodos_decisions_distribute.txt` | ✅ IMPLEMENTADO — IDs `iram_10_activate_distribute`, `iram_11_confirm_distribute` |
| `exodos_decisions_transfer.txt` | ✅ IMPLEMENTADO — IDs `iram_12_activate_transfer`, `iram_13_confirm_transfer` |
| `exodos_decisions_optimize.txt` | ✅ IMPLEMENTADO — IDs `iram_14_activate_optimize`, `iram_15`–`iram_18` rangos |
| `exodos_decisions_gather_global.txt` | ✅ IMPLEMENTADO — ID `iram_19_confirm_gather_global`, tyranny reducido a 50 |
| `iram_decisions_optimize_global.txt` | 🔧 STUB — `iram_20_activate_optimize_global` (bug: activa variable con nombre incorrecto — ver Sección 0.5) |
| `iram_decisions_menu.txt` | ✅ IMPLEMENTADO — `iram_01`–`iram_07`, `iram_21`, `iram_30`, `iram_40`, `iram_41` |
| `iram_decisions_demografia.txt` | ✅ IMPLEMENTADO — `iram_22`–`iram_29` (Relics, Migración, Ascenso, Descenso) |
| `exodos_decisions_rival_heir.txt` | ✅ IMPLEMENTADO — IDs `iram_42`/`iram_43`, integrado al menú |
| `exodos_decisions_cancel.txt` | ✅ IMPLEMENTADO — ID `iram_02_cancel_all`, cleanup exhaustivo |
| `exodos_decisions_bom.txt` | ✅ IMPLEMENTADO — IDs `iram_31`–`iram_35` |
| `exodos_decisions_ego_sum.txt` | ✅ IMPLEMENTADO — IDs `iram_36`–`iram_39` |
| `exodos_decisions_tgl.txt` | ✅ IMPLEMENTADO — ID `iram_45_tgl_purchase` |
| `exodos_decisions_tlv.txt` | ✅ IMPLEMENTADO — ID `iram_44_tlv_confirm` |
| `exodos_on_action.txt` | ✅ IMPLEMENTADO — Gather Global (10 bloques/pulso) + todas las ops legacy |
| `exodos_events.txt` | ✅ ACTUALIZADO — agrega `exodos.2` (fin Optimize Global); falta `exodos.3` |
| `common/modifiers/iram_relic_modifiers.txt` | ✅ IMPLEMENTADO — 4 modifiers (divine_relic, migracion_forzada, ascenso_forzado, descenso_forzado) |
| Localización ES y EN — todos los archivos | ✅ IMPLEMENTADA — 44 IDs actualizados + keys de `iram_20` y `exodos.2` |

## 2.2 Fixes y pendientes en v4

| Item | Descripción | Estado |
|---|---|---|
| Chequeo ancla destruida en on_action | Bloque único de chequeo de error | ✅ IMPLEMENTADO en v4.0 |
| Guards cruzados en `allow` de confirms | `NOT = exodos_operation_active` en todos los confirms | ✅ IMPLEMENTADO en v4.0 |
| Rival eliminado de Exodos | Sin condición de rival en Gather/Distribute/Optimize/Transfer | ✅ IMPLEMENTADO en v4.0 |
| Relics tokens | `gold` → `treasury`, `add_gold` → `add_treasury`, `picture` eliminado | ✅ CORREGIDO en v4.0 |
| BOM-como-texto | BOM literal `\xef\xbb\xbf` en `exodos_on_action.txt` y `exodos_decisions_optimize.txt` | ✅ CORREGIDO en v4.0 |
| Gather Global capital exclusion | `NOT = { is_capital = yes }` en los 10 bloques de on_action | ✅ IMPLEMENTADO en v4.0 |
| Separación de archivos por función | Un archivo por función (gather, distribute, demografia, menú) | ✅ IMPLEMENTADO en v4.1 |
| Sistema de menú navegable | Variables de estado `iram_menu_*`, 3 niveles + submenú | ✅ IMPLEMENTADO en v4.2 |
| Heredero del Rival — integración al menú | `has_variable = iram_rival_heir_open` en `potential` | ✅ IMPLEMENTADO en v4.3 |
| Condición `has_spouse` en Heredero del Rival | El rival puede no tener esposa — hijo spawna sin familia | ✅ CERRADO — comportamiento aceptado. Sin familia es válido. |
| Refactor 44 IDs a prefijo `iram_` | Todos los IDs de decisiones renombrados con numeración correlativa | ✅ IMPLEMENTADO en v4.3.2 |
| Costo Gather Global reducido | `add_tyranny = 100 → 50`, `add_popularity = -100 → -50` | ✅ IMPLEMENTADO en v4.3.2 |
| `global_migration_speed = 2.5` en Relic | Diseño original descartado — reemplazado por `iram_migracion_forzada` modifier | ✅ CERRADO — Migración Forzada cubre la función con mejor control |
| Reliquia migración (`global_migration_speed`) | Token confirmado en game.zip, reemplazado por diseño de Migración Forzada | ✅ CERRADO — ver arriba |
| `tlv_confirm` — `current_ruler` | `current_ruler` desde country scope en trigger puede no resolver | ⚠ TESTEAR |
| Variable nombre incorrecto en stub `iram_20` | Activa `exodos_optimize_global_gather_active` en vez de `exodos_optimize_global_distribute_active` | ⚠ CORREGIR al implementar on_action |
| Guard `has_variable = exodos_gather_global_completed` en `allow` de `iram_20` | Falta en el stub actual | ⚠ PENDIENTE próxima sesión de código |
| `remove_variable = exodos_gather_global_completed` en `effect` de `iram_20` | Falta en el stub actual | ⚠ PENDIENTE próxima sesión de código |
| on_action Optimize Global | 5 bloques/pulso, rangos automáticos por pops de capital post-gather | ⚠ PENDIENTE — diseño cerrado, ver Sección 19.0 |
| `exodos.3` — evento silencioso de cleanup | Timer 365 días desde fin de Gather Global | ⚠ PENDIENTE próxima sesión de código |
| 3 variables nuevas en `exodos_cleanup_effect` | `exodos_gather_global_completed`, `exodos_optimize_global_distribute_active`, `exodos_optimize_global_done` | ⚠ PENDIENTE próxima sesión de código |
| `set_variable = exodos_gather_global_completed` al fin de Gather Global en on_action | Señal para habilitar Optimize Global | ⚠ PENDIENTE próxima sesión de código |
| Ascenso/Descenso Forzado — comportamiento real | `global_pop_promotion_speed = 100` usa threshold, no barra | ⚠ TESTEAR — ver ERROR 28 |

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
│   │   ├── exodos_decisions_gather.txt                      ← BOM UTF-8 (iram_08, iram_09)
│   │   ├── exodos_decisions_distribute.txt                  ← BOM UTF-8 (iram_10, iram_11)
│   │   ├── exodos_decisions_transfer.txt                    ← BOM UTF-8 (iram_12, iram_13)
│   │   ├── exodos_decisions_optimize.txt                    ← BOM UTF-8 (iram_14–iram_18)
│   │   ├── exodos_decisions_gather_global.txt               ← BOM UTF-8 (iram_19)
│   │   ├── iram_decisions_optimize_global.txt               ← BOM UTF-8 (iram_20 — stub)
│   │   ├── iram_decisions_menu.txt                          ← BOM UTF-8 (iram_01–iram_07, iram_21, iram_30, iram_40, iram_41)
│   │   ├── iram_decisions_demografia.txt                    ← BOM UTF-8 (iram_22–iram_29)
│   │   ├── exodos_decisions_rival_heir.txt                  ← BOM UTF-8 (iram_42, iram_43)
│   │   ├── exodos_decisions_cancel.txt                      ← BOM UTF-8 (iram_02)
│   │   ├── exodos_decisions_bom.txt                         ← BOM UTF-8 (iram_31–iram_35)
│   │   ├── exodos_decisions_ego_sum.txt                     ← BOM UTF-8 (iram_36–iram_39)
│   │   ├── exodos_decisions_tgl.txt                         ← BOM UTF-8 (iram_45)
│   │   └── exodos_decisions_tlv.txt                         ← BOM UTF-8 (iram_44)
│   ├── events/
│   │   ├── exodos_events.txt                                ← BOM UTF-8 (exodos.1, exodos.2 — falta exodos.3)
│   │   └── tlv_events.txt                                   ← BOM UTF-8 (sin cambios)
│   ├── common/
│   │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8
│   │   ├── units/exodos_units.txt                           ← BOM UTF-8 (sin cambios)
│   │   ├── modifiers/iram_relic_modifiers.txt               ← BOM UTF-8 (4 modifiers)
│   │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8 (actualizado con iram_cleanup_menu e iram_cleanup_demografia)
│   └── localization/
│       ├── english/
│       │   ├── exodos_l_english.yml                         ← BOM UTF-8 (actualizado — todos los IDs renombrados + iram_20 + exodos.2)
│       │   ├── iram_menu_l_english.yml                      ← BOM UTF-8 (NUEVO v4.2)
│       │   ├── iram_demografia_l_english.yml                ← BOM UTF-8 (NUEVO v4.1)
│       │   ├── relics_l_english.yml                         ← BOM UTF-8
│       │   ├── bom_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       │   ├── bom_l_english_ego_sum.yml                    ← BOM UTF-8 (sin cambios)
│       │   ├── tlv_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       │   └── tgl_l_english.yml                            ← BOM UTF-8 (sin cambios)
│       └── spanish/
│           ├── exodos_l_spanish.yml                         ← BOM UTF-8 (actualizado — todos los IDs renombrados + iram_20 + exodos.2)
│           ├── iram_menu_l_spanish.yml                      ← BOM UTF-8 (NUEVO v4.2)
│           ├── iram_demografia_l_spanish.yml                ← BOM UTF-8 (NUEVO v4.1)
│           ├── relics_l_spanish.yml                         ← BOM UTF-8
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

**Archivos eliminados en v4.1 (no existen en zip activo):**
- `exodos_decisions_gather_distribute.txt` — separado en gather.txt y distribute.txt
- `exodos_decisions_relics.txt` — contenido absorbido por `iram_decisions_demografia.txt`

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

⚠️ **NOTA v2.3:** Los IDs iram_01–iram_45 del zip activo (`mod_pack_IRAM_v4_3_2_2026-05-25_E.zip`) son el estado viejo. El rediseño de árbol de menú del 2026-05-26 (sesión 19:51, CERRADO) reemplaza esos IDs por iram_01–iram_25. El refactor del zip está pendiente de codear. Esta tabla refleja el **diseño nuevo cerrado** — no el zip activo. Para el código exacto del zip activo ver Sección 8-C.

**IDs iram_01–iram_25 — diseño cerrado 2026-05-26 (pendiente de refactorizar en zip)**

| Función | ID nuevo | Archivo destino | Estado |
|---|---|---|---|
| Menú IRAM — abrir | `iram_01` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Cancelar Todo | `iram_02` | exodos_decisions_cancel.txt | ⏳ pendiente refactor |
| Abrir Gestión POPs/Eco | `iram_03` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Abrir Comportamiento de POPs | `iram_04` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Abrir Político | `iram_05` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Cerrar Menú | `iram_06` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Cerrar Gestión POPs/Eco | `iram_07` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Transfer Activate | `iram_08` | exodos_decisions_transfer.txt | ⏳ pendiente refactor |
| Transfer Confirm | `iram_09` | exodos_decisions_transfer.txt | ⏳ pendiente refactor |
| Gather Global | `iram_10` | exodos_decisions_gather_global.txt | ⏳ pendiente refactor |
| Distribute Global | `iram_11` | iram_decisions_menu.txt (o archivo nuevo) | ⏳ pendiente codear |
| Constructor Automático | `iram_12` | archivo nuevo | ⏳ pendiente codear |
| Optimize Global | `iram_13` | iram_decisions_optimize_global.txt | ⏳ pendiente codear |
| Cerrar Comportamiento de POPs | `iram_14` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Relics Activar | `iram_15` | iram_decisions_demografia.txt | ⏳ pendiente refactor |
| Migración Activar | `iram_16` | iram_decisions_demografia.txt | ⏳ pendiente refactor |
| Ascenso Forzado Activar | `iram_17` | iram_decisions_demografia.txt | ⏳ pendiente refactor |
| Descenso Forzado Activar | `iram_18` | iram_decisions_demografia.txt | ⏳ pendiente refactor |
| Cerrar Político | `iram_19` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Abrir submenú Heredero del Rival | `iram_20` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Cerrar submenú Heredero del Rival | `iram_21` | iram_decisions_menu.txt | ⏳ pendiente refactor |
| Hijo del Rival | `iram_22` | exodos_decisions_rival_heir.txt | ⏳ pendiente refactor |
| Hija del Rival | `iram_23` | exodos_decisions_rival_heir.txt | ⏳ pendiente refactor |
| The Last Vote | `iram_24` | exodos_decisions_tlv.txt | ⏳ pendiente refactor |
| The Great Leap | `iram_25` | exodos_decisions_tgl.txt | ⏳ pendiente refactor |

**Funciones eliminadas del árbol de menú (código preservado en Sección 8)**

| Función eliminada | IDs viejos | Fuente para reconstruir |
|---|---|---|
| Exodos: Concentración (Gather por área) | iram_08/09 | SUPERBACKUP Sección 8 |
| Exodos: Distribución (Distribute por área) | iram_10/11 | SUPERBACKUP Sección 8 |
| Exodos: Optimizar (por área, 4 rangos) | iram_14–iram_18 | SUPERBACKUP Sección 8 |
| Demografía: Desactivar individuales (Relics/Migración/Ascenso/Descenso) | iram_23/25/27/29 | SUPERBACKUP Sección 8 |

Transfer se mantiene (activate + confirm) — sigue con su flujo de dos decisiones.

**Funciones sin ID de menú (siempre visibles o guards propios)**

| Función | Archivo | Notas |
|---|---|---|
| BOM: Eliminar Rivales / Bacanal / Et tu Brute? | exodos_decisions_bom.txt | Sin cambios — fuera del árbol de menú |
| IHA: Confiscar / Fill the Void | exodos_decisions_bom.txt | Sin cambios |
| Ego Sum Mars / Iovis / Mercurii / Minervae | exodos_decisions_ego_sum.txt | Sin cambios |

## 3.4 Tabla de costos y condiciones — ecosistema completo v4

| Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | Condiciones extra |
|---|---|---|---|---|---|---|
| Exodos: Concentración (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Distribución (confirm) | 1000 | 5 | 2500 | +10 | ≤90 | ancla existente, área 100% propia |
| Exodos: Optimizar (confirm → sin costo) | — | — | — | — | — | ancla existente, área 100% propia |
| Exodos: Opt. Rango (decisión final) | 2000 | 10 | 5000 | +10 | ≤90 | exodos_optimize_active seteado |
| Exodos: Transferencia | 2000 | 10 | 5000 | +20 | ≤80 | ancla + destino existentes, owner=ROOT |
| Exodos: Gather Global | — | — | — | +50 | ≤90 | -50 popularidad gobernante, sin op. activa |
| Exodos: Optimize Global | — | — | — | +100 | ≤90 | -100 popularidad gobernante, `has_variable = exodos_gather_global_completed` (⚠ guard pendiente) |
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
| `exodos_optimize_count` | ✓ | ✓ | Count por asentamiento (4/9/14/19, literal) |
| `exodos_anchor_province` | ✓ | ✓ | Province del ancla, guardada en confirm |
| `exodos_destination_province` | ✓ | ✓ | Province destino Transfer |
| `exodos_pulse_counter` | ✓ | ✓ | Contador Transfer (10 pulsos) |
| `exodos_global_active` | ✗ | ✓ | Gather Global en ejecución |
| `iram_menu_open` | ✗ | ✓ | Menú principal abierto |
| `iram_menu_management_open` | ✗ | ✓ | Submenú Gestión POPs/Eco abierto *(era `iram_menu_movimiento_open` — renombrado 2026-05-26)* |
| `iram_menu_behavior_open` | ✗ | ✓ | Submenú Comportamiento de POPs abierto *(era `iram_menu_demografia_open` — renombrado 2026-05-26)* |
| `iram_menu_political_open` | ✗ | ✓ | Submenú Político abierto *(era `iram_menu_politico_open` — renombrado 2026-05-26)* |
| `iram_rival_heir_open` | ✗ | ✓ | Submenú Heredero del Rival abierto |
| `iram_divine_relic_active` | ✗ | ✓ | Reliquia activa (variable de estado, acompana al modifier) |
| `iram_migracion_forzada_active` | ✗ | ✓ | Migración Forzada activa |
| `iram_ascenso_forzado_active` | ✗ | ✓ | Ascenso Forzado activo |
| `iram_descenso_forzado_active` | ✗ | ✓ | Descenso Forzado activo |
| `exodos_gather_global_completed` | ✗ | ⚠ PENDIENTE | Señal: Gather Global terminado, habilita Optimize Global |
| `exodos_optimize_global_distribute_active` | ✗ | ⚠ PENDIENTE | Optimize Global distribute en ejecución |
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
| `exodos_gather_global_done` | Province ya procesada por Gather Global (limpiada en cleanup) |
| `exodos_optimize_global_done` | Province ya procesada por Optimize Global (⚠ PENDIENTE — no existe aún) |

### Variables de unidad (v4 únicamente)

| Variable | Uso |
|---|---|
| `exodos_unit_concentrate` | Unidad ancla legacy |
| `exodos_unit_distribute` | Unidad distribute legacy |
| `exodos_unit_transfer_origin` | Unidad origen Transfer |
| `exodos_unit_transfer_dest` | Unidad destino Transfer |
| `exodos_unit_optimize` | Unidad Optimize |

### Modifiers de país (iram_relic_modifiers.txt)

| Modifier | Efecto | Activado por |
|---|---|---|
| `iram_divine_relic` | `global_pop_conversion_speed = 50`, `global_pop_assimilation_speed = 50` | `iram_22_create_divine_relic` |
| `iram_migracion_forzada` | `global_pop_migration_speed = 100` | `iram_24_activate_migracion` |
| `iram_ascenso_forzado` | `global_pop_promotion_speed = 100` | `iram_26_activate_ascenso` |
| `iram_descenso_forzado` | `global_pop_demotion_speed = 100` | `iram_28_activate_descenso` |

## 3.7 Panel de decisiones — qué aparece cuándo — diseño cerrado 2026-05-26

⚠️ **NOTA v2.3:** Este árbol refleja el **diseño cerrado** de la sesión 2026-05-26 19:51. El zip activo (`mod_pack_IRAM_v4_3_2_2026-05-25_E.zip`) todavía tiene el árbol viejo (iram_01–iram_45). El refactor está pendiente de codear. No usar los IDs de este árbol para buscar código en el zip actual — ir a Sección 8-C para el código real.

El sistema de menú usa variables de estado para controlar visibilidad. El panel del juego muestra decisiones en orden alfabético por ID — el prefijo `iram_` con numeración garantiza el orden correcto.

**Siempre visible (`potential = { is_ai = no; NOT = { has_variable = iram_menu_open } }`):**
- `iram_01` — Abrir Menú IRAM

**Con `iram_menu_open` activo:**
- `iram_02` — Cancelar Todo (siempre visible con menú abierto — botón de pánico)
- `iram_03` — Abrir Gestión POPs/Eco
- `iram_04` — Abrir Comportamiento de POPs
- `iram_05` — Abrir Político
- `iram_06` — Cerrar Menú

**Con `iram_menu_management_open`:**
- `iram_07` — Cerrar Gestión POPs/Eco
- `iram_08` — Transfer Activate
- `iram_09` — Transfer Confirm
- `iram_10` — Gather Global
- `iram_11` — Distribute Global
- `iram_12` — Constructor Automático
- `iram_13` — Optimize Global

**Con `iram_menu_behavior_open`:**
- `iram_14` — Cerrar Comportamiento de POPs
- `iram_15` — Relics Activar (en gris si `has_country_modifier = iram_divine_relic`)
- `iram_16` — Migración Activar (en gris si `has_country_modifier = iram_migracion_forzada`)
- `iram_17` — Ascenso Forzado Activar (en gris si `has_country_modifier = iram_ascenso_forzado`)
- `iram_18` — Descenso Forzado Activar (en gris si `has_country_modifier = iram_descenso_forzado`)

> Nota: los desactivar individuales fueron eliminados. El `iram_02` (Cancelar Todo) los absorbe. Los activar aparecen siempre visibles pero con `allow` bloqueado (`NOT = { has_country_modifier = X }`) cuando la función ya está activa.

**Con `iram_menu_political_open`:**
- `iram_19` — Cerrar Político
- `iram_20` — Abrir submenú Heredero del Rival
- `iram_21` — Cerrar submenú Heredero del Rival

**Con `iram_rival_heir_open`:**
- `iram_22` — Hijo del Rival
- `iram_23` — Hija del Rival

**Con guards propios (sin restricción de submenú):**
- `iram_24` — The Last Vote (guard: is_republic, stability ≥ 50, popularity ≥ 50)
- `iram_25` — The Great Leap (one-shot)

**Variables de submenú renombradas (2026-05-26):**

| Variable antigua | Variable nueva |
|---|---|
| `iram_menu_movimiento_open` | `iram_menu_management_open` |
| `iram_menu_demografia_open` | `iram_menu_behavior_open` |
| `iram_menu_politico_open` | `iram_menu_political_open` |

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

**Pasos post-cierre (después de codear iram_12, iram_11 y Optimize Global on_action):**

| Paso | Tarea | Notas |
|---|---|---|
| A | Verificar sistema nuevo (TECHNICAL_WIKI v3.0 + zip v4.3.7 + PROMPT v3.8) | Antes de borrar nada |
| B | Git — commit inicial con `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` como estado canónico | Mensaje de commit: historial anterior en TECHNICAL_WIKI Secciones 14 y 19 |
| C | No reconstruir historial Git artificialmente — el TECHNICAL_WIKI ya documenta el *por qué* | — |
| D | Borrar archivos viejos solo después de verificar sistema nuevo en Git | `mod_pack_IRAM_15.zip` y TECHNICAL_WIKI ARCHIVE se conservan permanentemente |

**Archivos sin cambios — copiar tal cual desde v3:**
`exodos_decisions_rival_heir.txt`, `exodos_decisions_bom.txt`, `exodos_decisions_bom_ego_sum.txt`,
`exodos_decisions_tgl.txt`, `exodos_decisions_tlv.txt`, `exodos_events.txt`, `tlv_events.txt`,
`bom_l_english.yml`, `bom_l_spanish.yml`, `bom_l_english_ego_sum.yml`, `bom_l_spanish_ego_sum.yml`,
`tlv_l_english.yml`, `tlv_l_spanish.yml`, `tgl_l_english.yml`, `tgl_l_spanish.yml`

---

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
| `current_ruler` desde country scope en trigger (TLV) | ✅ CERRADO — verificado por funcionamiento en juego | — | 2026-05-26 20:49 |
| Heredero del Rival — ¿se porta a v4? | ✅ CERRADO — sin cambios vs v3, integrado al menú en v4.3 | — | 2026-05-25 |
| Condición `has_spouse` en Heredero del Rival | ✅ CERRADO — spawna sin familia si rival no tiene esposa. Comportamiento aceptado. | — | 2026-05-25 |
| Optimize Global — diseño dos pasos + threshold | ✅ CERRADO — ver entrada 2026-05-26 sesiones 17:02→17:52 | — | 2026-05-26 17:52 |
| Optimize Global — implementación on_action | ⚠️ PENDIENTE — después del Constructor | Única función mayor que falta para cerrar v4 | 2026-05-26 20:49 |
| Distribute Global (`iram_11`) — implementación | ⚠️ PENDIENTE | Función nueva, diseño cerrado | 2026-05-26 20:49 |
| Constructor Automático (`iram_12`) — implementación | ⚠️ PENDIENTE — diseño CERRADO 15:12, listo para codear | Sin código el stub no hace nada | 2026-05-27 15:12 |
| Refactor zip — nueva numeración iram_01–iram_25 | ⚠️ PENDIENTE — primera tarea próxima sesión de código | Sin refactor el zip tiene árbol viejo y variables viejas | 2026-05-26 20:49 |
| Bug: variable nombre incorrecto en stub `iram_20` | ✅ CERRADO — corregido en v4.3.7 (sesión 17:14) | — | 2026-05-27 17:14 |
| Bug: BOM doble en `exodos_decisions_gather_global.txt` | ✅ CERRADO — corregido en v4.3.7 (sesión 17:14) | — | 2026-05-27 17:14 |
| Bug: llaves desbalanceadas en `iram_13` y `iram_10` | ✅ CERRADO — corregido en v4.3.7 (sesión 17:14) | — | 2026-05-27 17:14 |
| Bug: `add_popularity` scope incorrecto en `iram_10` | ✅ CERRADO — corregido en v4.3.7 (sesión 17:14) | — | 2026-05-27 17:14 |
| Bug: nombre variable incorrecto en `iram_cleanup_menu` | ✅ CERRADO — corregido en v4.3.7 (sesión 17:14) | — | 2026-05-27 17:14 |
| Ascenso/Descenso Forzado — threshold vs barra | ⚠️ Sin testear | `global_pop_promotion_speed = 100` puede no tener el efecto esperado — ver ERROR 28 | 2026-05-25 |
| Reliquia migración `global_migration_speed = 2.5` | ✅ CERRADO — reemplazado por Migración Forzada (`global_pop_migration_speed = 100`) | — | 2026-05-25 |
| `valor_rp = 0.023223` — nunca verificado contra el engine | ⚠️ Sin verificar | Debilita el argumento del modelo económico (no bloquea código) | 2026-05-19 |
| `exodos.3` — evento silencioso de cleanup 365 días | ⚠️ PENDIENTE | Sin cleanup temporal el estado puede quedar sucio tras 365 días | 2026-05-26 20:49 |
| 3 variables nuevas en `exodos_cleanup_effect` | ⚠️ PENDIENTE | Variables de las funciones nuevas no se limpian con cancel_all | 2026-05-26 20:49 |
| Calibración números Distribute Global (5/10/15) | ⚠️ PENDIENTE — post-testeo | Valores provisorios | 2026-05-26 20:49 |
| Verificar `livestock` vs `cattle` en game files | ✅ CERRADO — es `cattle`. Tabla Constructor corregida en v2.5 | — | 2026-05-27 15:01 |
| `salt` y `honey` — building correcto en Constructor | ✅ CERRADO — van a `latifundia_building` (allow incompatible con `basic_settlement_infratructure_building`) | — | 2026-05-27 15:12 |
| Nombres incorrectos en tabla Constructor (`dyes`, `earthenware`, `gemstones`) | ✅ CERRADO — corregidos a `dye`, `earthware`, `gems` en v2.5 | — | 2026-05-27 15:01 |
| Propagar SESSION LOGs 15:01 y 15:12 al SUPERBACKUP | ✅ CERRADO — propagado en v2.5 | — | 2026-05-27 15:17 |
| Propagar SESSION LOGs 16:53, 17:02, 17:14 al SUPERBACKUP | ✅ CERRADO — propagado en v2.6 | — | 2026-05-27 20:06 |
| Split SUPERBACKUP → TECHNICAL_WIKI ACTIVE v3.0 + ARCHIVE v3.0 | ✅ CERRADO — ejecutado 2026-05-27 20:28 | — | 2026-05-27 20:28 |
| Actualizar PROMPT_MAESTRO + INSTRUCCIONES_HUMANO para TECHNICAL_WIKI | ✅ CERRADO — v3.8 generado 2026-05-27 20:55 | — | 2026-05-27 20:55 |
| Git — commit inicial con v4.3.7 | ⚠️ PENDIENTE POST-CIERRE — ver Sección 13 pasos post-cierre | Sin Git el versionado depende de zips | 2026-05-27 20:06 |
| Skill PDX modding (`/mnt/skills/user/pdxscript/SKILL.md`) | ⚠️ PENDIENTE POST-V4 — extraer reglas genéricas del engine, reutilizable en futuros mods | — | 2026-05-27 20:06 |
| Template de proyecto basado en sistema IRAM | ⚠️ PENDIENTE POST-V4 — reutilizable fuera de PDX | — | 2026-05-27 20:06 |

---

## 2026-05-27 20:55 — Actualización sistema de control

### ✅ Decidido

- PROMPT_MAESTRO v3.7 → v3.8: SUPERBACKUP renombrado a TECHNICAL_WIKI (ACTIVE) en todo el documento. Referencias al ARCHIVE agregadas donde corresponde. Plantilla B actualizada.
- INSTRUCCIONES_HUMANO actualizado: tabla de archivos con ACTIVE + ARCHIVE separados, orden de carga, smoke test, protocolo de reanudación.
- Visión reformulada, perfil del operador y regla de modelo propagados al TECHNICAL_WIKI ACTIVE (Secciones 0.1b, 0.1c, 0.4d).
- Git y pendientes post-v4 propagados a Sección 13 y Sección 19.0.
- Perfil completo del operador y mapa de aprendizaje propagados al TECHNICAL_WIKI ARCHIVE (Sección 14).
- Skill PDX y template de proyecto registrados en Sección 19.0 como pendientes post-v4.

### ❓ Quedó abierto

- iram_12 Constructor Automático — codear completo.
- iram_11 Distribute Global — diseño + codeo.
- Optimize Global on_action — pendiente.
- Git — post-cierre de código.

---

## 2026-05-27 20:06 — Sesión estratégica + SUPERBACKUP v2.6

**Tipo:** estratégica + actualización de documentos. Sin código.

### ✅ Decidido

- **Nombre del documento:** TECHNICAL_WIKI — CERRADO. Más profesional que SUPERBACKUP.
- **Split ACTIVE/ARCHIVE:** ACTIVE = Secciones 0–7, 9–13, 16–17, 19 (entradas v4), 20–22. ARCHIVE = Secciones 8/8-A/8-B/8-C, 14, 18, entradas pre-v4 de Sección 19.
- **Git:** paso final del proceso, no intermedio. Commit inicial con v4.3.7. No reconstruir historial pasado — el TECHNICAL_WIKI documenta el *por qué* mejor que commits reconstruidos.
- **Borrado de archivos viejos:** solo después de verificar sistema nuevo en Git. `mod_pack_IRAM_15.zip` y ARCHIVE se conservan permanentemente.
- **Session logs con Git:** el "qué cambié y por qué" pasa a ser el commit message. La Sección 19 sigue siendo el log de decisiones de diseño. Formato cambia, práctica no desaparece.
- **Modelo:** Sonnet sin pensamiento para docs y codeo conocido. Con pensamiento solo para arquitectura sin solución clara. Haiku: no usar para código.
- **Visión reformulada:** "El mod exitoso es el entregable. El aprendizaje es el objetivo real."
- SUPERBACKUP v2.5 → v2.6: Sección 0.5 actualizada a v4.3.7, bugs conocidos limpiados, 4 entradas nuevas en Sección 19.

### ❓ Quedó abierto

- Split TECHNICAL_WIKI v3.0 — ejecutado en sesión siguiente.
- Actualizar PROMPT_MAESTRO + INSTRUCCIONES_HUMANO — ejecutado en sesión 20:55.

---

## 2026-05-27 17:14 — Auditoría de bugs en código fuente v4.3.6

**Método:** lectura directa de todos los archivos del zip canónico + comparación contra `mod_pack_IRAM_15_GATHER_GLOBAL_v1_3.zip`.

### ✅ Decidido

**5 bugs confirmados en 3 archivos** (ver detalle completo en SESSION_LOG 17:14 auditoría):

- **BUG 1** — `iram_decisions_optimize_global.txt`: `set_variable` ×2 fuera del `effect` por llaves desbalanceadas. Engine los ignoraba silenciosamente.
- **BUG 2** — `exodos_decisions_gather_global.txt`: BOM doble (real + texto literal `\xef\xbb\xbf`). Engine rechazaba el archivo — iram_10 probablemente no existía en el juego.
- **BUG 3** — `exodos_decisions_gather_global.txt`: `set_variable` ×2 fuera del `effect` por llaves desbalanceadas.
- **BUG 4** — `exodos_decisions_gather_global.txt`: `add_popularity` en scope país — engine lo ignoraba.
- **BUG 5** — `exodos_scripted_effects.txt`: `iram_cleanup_menu` usaba `iram_menu_rival_heir_open` (inexistente) en vez de `iram_rival_heir_open`.

### ❓ Quedó abierto

- Aplicar los 5 fixes (resuelto en sesión 17:14 fix — ver entrada anterior).
- iram_12 Constructor Automático — codear completo.

---

## 2026-05-27 17:02 — Fix bug iram_13 documentado

### ✅ Decidido

- Bug estructural en `iram_decisions_optimize_global.txt` confirmado: dos `set_variable` fuera del `effect` por llaves desbalanceadas. Engine los ignoraba silenciosamente.
- Bug distinto al ya documentado en Sección 0.5 (nombre de variable incorrecto) — son dos bugs independientes en el mismo stub.
- Fix indicado al operador para aplicación manual. No se generó zip en esta sesión.

### ❓ Quedó abierto

- Aplicar el fix (incluido en los 5 bugs corregidos en sesión 17:14).
- iram_12 Constructor Automático — codear completo.

---

## 2026-05-27 16:53 — Auditoría pre-codeo Constructor Automático

### ✅ Decidido

- **Bug adicional en stub `iram_13`** — confirmado en código real: dos `set_variable` fuera del `effect` por llaves desbalanceadas. Bug distinto al de nombre de variable ya documentado.
- **Análisis `iram_12`** — sin puntos nuevos abiertos. Guard de `exodos_operation_active`, comportamiento de `port_building` y stub vacío: todos resueltos por documentación existente (patrón `iram_03`, tabla RE6, diseño CERRADO).
- Los 3 falsos positivos del análisis inicial fueron descartados tras releer el SUPERBACKUP correctamente — confirma que la documentación existente cubre los casos.

### ❓ Quedó abierto

- Corregir bug estructural `iram_13` (resuelto en sesión 17:14).
- Codear `iram_12_constructor_auto` completo (decisión + localizaciones ES/EN).

---

## 2026-05-22 — Diseño de Migración Forzada

### ✅ Decidido
- Diseño de Migración Forzada: modifier `iram_migracion_forzada` con `global_pop_migration_speed = 100`. Toggle permanente (duration = -1). Costo 2000 oro.
- Token confirmado: `global_pop_migration_speed` es barra acumulativa — `= 100` satura en 1 mes en condiciones neutras.
- Slaves no migran — hardcoded en el engine. Migración Forzada no afecta esclavos.
- El engine procesa máximo 1 pop emigrando por territorio por tick — cuello de botella real con muchas pops elegibles.
- Zip de trabajo: `mod_pack_IRAM_15_GATHER_GLOBAL_v1_3.zip` — base experimental con migración forzada.

### ❓ Quedó abierto
- Ascenso Forzado y Descenso Forzado — diseño conceptual definido, implementación sesión siguiente.

### ⚠️ Premisas activas
- `valor_rp = 0.023223` — sin verificar, no bloquea código.

---

## 2026-05-23 — Diseño de Demografía completa y Sistema de menú

### ✅ Decidido
- Ascenso Forzado: modifier `iram_ascenso_forzado` con `global_pop_promotion_speed = 100`. Toggle permanente. Costo 2000 oro.
- Descenso Forzado: modifier `iram_descenso_forzado` con `global_pop_demotion_speed = 100`. Toggle permanente. Costo 2000 oro.
- Alerta: `global_pop_promotion_speed` y `global_pop_demotion_speed` usan threshold (`PROMOTE_DEMOTE_THRESHOLD = 0.005`), no barra acumulativa. Verificado en `defines/00_defines.txt`. Comportamiento real con `= 100` sin testear.
- Reorganización: un archivo por función (gather, distribute, transfer, optimize, gather_global, demografia, menu).
- Sistema de menú: diseño conceptual completo — variables de estado `iram_menu_open`, `iram_menu_movimiento_open`, `iram_menu_demografia_open`, `iram_menu_politico_open`. Mecanismo: `potential = { has_variable = X }`.
- Relics se absorbe en `iram_decisions_demografia.txt` — `exodos_decisions_relics.txt` eliminado.

### ❓ Quedó abierto
- Implementación completa — sesión del 25/05.

### ⚠️ Premisas activas
- Ascenso/Descenso Forzado — threshold sin testear.

---

## 2026-05-27 15:12 — Verificación sintaxis engine y cierre de diseño Constructor Automático

### ✅ Decidido

- `salt` y `honey` → `latifundia_building`. DEFINITIVO. Revierte sesión 18:40 donde iban a `basic_settlement_infratructure_building` — ese building tiene `allow = { has_food_trade_good_trigger = yes }` y salt/honey no están en ese trigger → `add_building_level` fallaría silenciosamente.
- `remove_building_level = X` — sin llaves. Confirmado en `common/scripted_effects/00_event_effects.txt` (`destroy_building_effect`). La variante con llaves no existe.
- Demolición: 7 `if` independientes (no `else_if`). `destroy_building_effect` vanilla usa `else_if` porque destruye uno solo. El Constructor demuela todos — patrón distinto.
- Skip de `fortress_building` va en el `limit` del `every_owned_province`, no como `if` interno.
- Fase 2 (construcción): `if/else_if` encadenado con `trade_goods = X` directo — sin triggers del engine (`has_food_trade_good_trigger`, `has_minable_trade_good_trigger` no usados).
- Estructura completa del Constructor CERRADA — ver SESSION_LOG 15:12 para el bloque de código completo.

### ❓ Quedó abierto

- Codear `iram_12_constructor_auto` completo (decisión + localizaciones ES/EN).

---

## 2026-05-27 15:01 — Revisión de diseño Constructor Automático y verificación game.zip

### ✅ Decidido

- Modelo: Sonnet 4.6. Pensamiento extendido: activar puntualmente para diseño complejo, no por defecto.
- `remove_building_level` requiere guards `num_of_X > 0` en cada llamada — confirmado contra engine.
- No usar `has_food_trade_good_trigger` ni `has_minable_trade_good_trigger` en el Constructor. Usar `trade_goods = X` directo. Razón: `stone` es minable pero el diseño lo manda a `local_forum_building` — el trigger del engine lo mandaría a `slave_mine_building` por error.
- Nombres corregidos en tabla: `dyes`→`dye`, `earthenware`→`earthware`, `gemstones`→`gems`, `livestock`→`cattle` (confirmado en game.zip).
- `salt` y `honey` no pueden recibir `basic_settlement_infratructure_building` — allow incompatible. (Decisión de destino cerrada en sesión 15:12.)
- `can_have_port` — hardcoded del engine, no está en `scripted_triggers`. No usarlo.
- `port_building` puede existir en settlements — el Constructor lo demuela con guard pero no lo construye.
- Los 34 trade goods del game están todos cubiertos en la tabla corregida.

### ❓ Quedó abierto

- Destino de `salt` y `honey` (resuelto en sesión 15:12 → `latifundia_building`).

---

## 2026-05-26 20:49 — Cierre de premisas activas y sugerencias de desarrollo

### ✅ Decidido
- `current_ruler` desde country scope en TLV: CERRADO — verificado por funcionamiento en juego. Patrón correcto.
- `valor_rp = 0.023223`: PARCIALMENTE CERRADO — el valor está subestimado porque no incorpora el valor indirecto vía tech militares. No bloquea código (costos fijados por gameplay). Refinamiento pendiente si se quiere recalibrar.
- Orden de testeo de las 3 funciones nuevas: CERRADO — Constructor Automático → Distribute Global → Optimize Global, en ese orden, con savegame dedicado por función. Son interdependientes.

### ❓ Quedó abierto (sin cambios vs sesión 19:51)
- Refactor zip — renumerar iram_01–iram_25, renombrar variables de submenú, eliminar decisiones por área, eliminar desactivar individuales, sacar costos para test.
- Codear Constructor Automático (`iram_12`).
- Codear Distribute Global (`iram_11`).
- Codear Optimize Global (`iram_13`).
- Verificar `livestock` vs `cattle` en game files.
- 3 variables nuevas en `exodos_cleanup_effect`.
- `exodos.3` — evento silencioso de cleanup 365 días.
- Calibración números Distribute — 5/10/15 provisorios.
- SUPERBACKUP Sección 3.7 con el árbol nuevo (resuelto en v2.3) y nota en Sección 3.4 sobre costos eliminados temporalmente.

### ⚠️ Premisas activas
- Ascenso/Descenso Forzado — threshold sin testear.
- `valor_rp = 0.023223` — subestimado, pendiente refinamiento modelo económico.

### Errores de IA documentados en esta sesión (para incorporar en futuras sesiones)
1. R15 violada dos veces — logs 18:40 y 19:51 generados sin preguntar hora al operador.
2. SUPERBACKUP no leído antes de responder — árbol del menú, IDs y premisas activas respondidos sin leer Sección 3.7 y Sección 19 primero. Generó respuestas incorrectas.
3. Terminología territories/areas/provinces confundida reiteradamente — documentado en Sección 3.1. Pasó 4–5 veces en la sesión de investigación de map data.

**Sugerencia para PROMPT_MAESTRO:** agregar regla explícita — antes de responder cualquier pregunta sobre árbol de menú, IDs o premisas activas, leer Sección 3.7 y Sección 19 del SUPERBACKUP. No asumir desde contexto de conversación.

---

## 2026-05-26 19:51 — Rediseño árbol de menú completo y protocolo de test sin costos

### ✅ Decidido

**Árbol de menú — REDISEÑO COMPLETO — CERRADO**

IDs renumerados desde cero para que el orden de aparición en pantalla coincida con el orden lógico de uso. Todas las IDs antiguas (iram_01–iram_45) quedan obsoletas.

Ver árbol completo en Sección 3.7.

**Variables de submenú renombradas:**

| Variable antigua | Variable nueva |
|---|---|
| `iram_menu_movimiento_open` | `iram_menu_management_open` |
| `iram_menu_demografia_open` | `iram_menu_behavior_open` |
| `iram_menu_politico_open` | `iram_menu_political_open` |

**Funciones removidas del zip activo — CERRADO**

Operaciones por área con unidad marcadora (Gather/Distribute/Optimize por área) eliminadas del zip. Código preservado en Sección 8. Transfer se mantiene sin cambios.

**Desactivar individuales de Comportamiento de POPs — CERRADO**

Los desactivar individuales (Relics, Migración, Ascenso, Descenso) se eliminan. El `iram_02` (cancel_all) los absorbe. Los activar individuales quedan visibles siempre pero en gris (`allow` bloqueado) cuando la función ya está activa.

**Funciones nuevas — CERRADO**

| Función | ID nuevo |
|---|---|
| Distribute Global | `iram_11` |
| Constructor Automático | `iram_12` |
| Optimize Global | `iram_13` |

**Gather Global sin confirm — CERRADO**

`iram_10` es una sola decisión, sin activate previo.

**Protocolo de test sin costos — CERRADO**

Para el test amplio se eliminan temporalmente todos los costos. SUPERBACKUP Sección 3.4 es la referencia para restaurarlos.

Costos a eliminar:

| Función | Oro | Manpower | Tyranny | Popularidad |
|---|---|---|---|---|
| Transfer | 2000 | 5000 | +20 | — |
| Gather Global | — | — | +50 | −50 |
| Relics Activar | 5000 | — | — | — |
| Migración Activar | 2000 | — | — | — |
| Ascenso Activar | 2000 | — | — | — |
| Descenso Activar | 2000 | — | — | — |
| BOM, IHA, TLV, TGL | varios | varios | varios | — |

Condiciones funcionales que se mantienen durante el test (guards, no costos):

| Función | Condición |
|---|---|
| Relics/Migración/Ascenso/Descenso | `NOT has_country_modifier` / `has_country_modifier` |
| BOM | rivals ≥ 1, stability, tyranny cap |
| TLV | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL | one-shot |
| Transfer | ancla + destino existentes, owner=ROOT |

Condiciones eliminadas temporalmente junto con costos:

| Función | Condición eliminada |
|---|---|
| Gather Global | tyranny ≤ 90, popularidad ≥ −50 |
| Transfer | tyranny ≤ 80, treasury ≥ 2000, manpower ≥ 5000 |

### ❓ Quedó abierto
- Codear refactor completo del zip con nueva numeración iram_01–iram_25.
- Codear Constructor Automático, Distribute Global, Optimize Global.
- Verificar `livestock` vs `cattle` en game files.
- Calibración números Distribute — 5/10/15 provisorios.
- Pendientes anteriores: 3 variables en `exodos_cleanup_effect`, `exodos.3`.

### ⚠️ Premisas activas sin cambios
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Ascenso/Descenso Forzado — threshold sin testear.
- `current_ruler` desde country scope en TLV — sin testear.

---

## 2026-05-26 18:40 — Investigación map data y cierre tabla Constructor Automático

### ✅ Decidido

**Datos de mapa verificados — CERRADO**

Fuente: `map_data/areas.txt` cruzado con `definition.csv` (IR 2.0.4 instalación local).

| Métrica | Valor |
|---|---|
| Total territories en el mapa | 8.062 |
| territories no jugables (mar, impassable, ríos, lagos, wasteland) | 1.789 |
| territories colonizables | 6.209 |
| Areas con territories colonizables | 551 |
| Promedio territories colonizables por area | 11,27 (~11) |

Distribución: 513 de 551 areas tienen exactamente 10, 11 o 12 territories colonizables. Rango real: 5–15. El número de ~8.000 que aparece en internet incluye todos los tiles del mapa. Los 6.209 son solo colonizables.

Promedio de edificios productivos por area (Constructor Automático): ~10 (11 territories − 1 city capital de area, que el Constructor no toca).

**Tabla Constructor Automático — CERRADA DEFINITIVAMENTE**

⚠ **Correcciones aplicadas en sesión 2026-05-27 15:12** — ver entradas de esa sesión en esta Sección 19.

| Trade good | Edificio | Criterio |
|---|---|---|
| grain, fish, cattle, vegetables | `basic_settlement_infratructure_building` | comida (cubiertos por `has_food_trade_good_trigger`) |
| salt, honey | `latifundia_building` | food-adjacent pero NO en `has_food_trade_good_trigger` — `basic_settlement_infratructure_building` los rechazaría silenciosamente |
| iron, precious_metals, base_metals, marble | `slave_mine_building` | extraídos/minables |
| papyrus, cloth, dye, incense, silk, amber, spices, earthware, gems, glass | `latifundia_building` | nobles/citizens |
| horses, wood, elephants, steppe_horses, camel | `latifundia_building` | estratégicos militares |
| wine, leather, hemp, dates, stone, olive, wild_game, fur, woad | `local_forum_building` | freemen/slaves/tribesmen |

Nombres corregidos respecto a versión anterior: `dyes`→`dye`, `earthenware`→`earthware`, `gemstones`→`gems`, `livestock`→`cattle`.
`stone` → `local_forum_building` por diseño — NO usar `has_minable_trade_good_trigger` (incluye stone pero el diseño lo excluye de mine).
Total: 34 trade goods. Todos cubiertos. Usar `trade_goods = X` directo en el código — sin triggers del engine.

Correcciones incorporadas en esta tabla respecto a sesiones anteriores:
- `marble` → `slave_mine_building` (era `latifundia` — corrección por ser extraído).
- `precious_metals` → `slave_mine_building` (hubo ida y vuelta en 16:54→17:02→aquí — DEFINITIVO).
- `spices` → `latifundia_building` (urban, no minable — era incorrecto en 16:54).
- `horses, wood, elephants, steppe_horses, camel` → `latifundia_building` (estratégicos — no minables).
- `stone` → `local_forum_building` (no tiene edificio productivo en este diseño).
- `honey` → grupo comida en `basic_settlement_infratructure_building` (no va a latifundia).

**Impacto en diseño Optimize Global:** los TG con `local_forum_building` no generan demanda de slaves en el threshold. El diseño de dos pasos del log 17:52 sigue vigente sin modificaciones.

### ❓ Quedó abierto
- Verificar `livestock` vs `cattle` en game files.
- Calibración números Distribute — 5/10/15 provisorios.
- Pendientes anteriores sin cambios.

---

## 2026-05-26 17:52 — Correcciones threshold Optimize Global y cierre de diseño

⚠️ **Este log reemplaza y corrige las decisiones del log 17:02** en todo lo referido al threshold del ancla de Optimize Global. Los valores del log 17:02 eran incorrectos.

### ✅ Decidido

**Threshold base por tipo de territory — CORREGIDO**

| Tipo de territory | Base slaves needed for Local Surplus |
|---|---|
| Settlement | 15 |
| City | 20 |
| Metropolis | 20 |

Modificadores de buildings (reducen el base):

| Building | Modificador |
|---|---|
| Farming Settlement (`basic_settlement_infratructure_building`) | −5 → threshold efectivo = **10** |
| Mine (`slave_mine_building`) | −5 → threshold efectivo = **10** |
| Latifundia (`latifundia_building`) | sin reductor → threshold efectivo = **15** |

Modificadores globales (inventions, misiones, subject types) son impredecibles en runtime — IRAM no puede leerlos. Usar valores base sin reductores globales es conservador en la dirección correcta.

**Threshold del ancla — Optimize Global — CERRADO DEFINITIVO**

El ancla es ciudad (capital de área). Las ciudades producen 2 trade goods de base sin ningún slave — no es necesario reservar slaves para proteger la producción del ancla.

**No hay reserva propia del ancla.** El threshold es únicamente la demanda del área:

```
threshold_ancla_optimize =
    (num_slave_mine_building × 10)
  + (num_basic_settlement_infratructure_building × 10)
  + (num_latifundia_building × 15)
```

**Diseño operacional Optimize Global — DOS PASOS — CERRADO**

Paso 1 — Guard del ancla:
```
num_of_slaves >= 
    (num_slave_mine_building × 10)
  + (num_basic_settlement_infratructure_building × 10)
  + (num_latifundia_building × 15)
```
Si no califica → saltea el área.

Paso 2 — Distribución desde ancla a cada province destino:

| Building en destino | Slaves a mover |
|---|---|
| `slave_mine_building` | `10 − num_of_slaves` (si > 0) |
| `basic_settlement_infratructure_building` | `10 − num_of_slaves` (si > 0) |
| `latifundia_building` | `15 − num_of_slaves` (si > 0) |
| sin building productivo | skip |

Los slaves se mueven desde el ancla únicamente.

### ❓ Quedó abierto
- `salt` y `honey` — ¿extender `has_food_trade_good_trigger` en IRAM o mandar a `latifundia`? (Resuelto en sesión 18:40 → `basic_settlement_infratructure_building`).
- Calibración números Distribute — 5/10/15 provisorios.

---

## 2026-05-26 16:54 — Diseño Distribute Global, Optimize Global y Constructor Automático

⚠️ **Nota:** Los threshold values de esta sesión (base 15 flat, threshold 9) fueron corregidos en la sesión 17:02 y definitivamente en 17:52. Ver esas entradas para los valores correctos.

### ✅ Decidido

**Rename conceptual — CERRADO**
- Lo que estaba en `iram_20` como "Optimize Global" es en realidad un **Distribute Global** — redistribuye pops por volumen desde el ancla en 3 rangos.
- "Optimize Global" pasa a ser una función nueva con lógica distinta (distribuye slaves según demanda real por building).

**Cadena de funciones:**

| Función | Rol |
|---|---|
| Gather Global | Concentra pops en anclas de área |
| Distribute Global (`iram_11`) | Dispersa pops genéricos desde anclas para conversión/esclavización |
| Optimize Global (`iram_13`) | Distribuye slaves específicamente a settlements con demanda real |
| Constructor Automático (`iram_12`) | Prepara terreno: demolish + construye edificio correcto según trade good |

**Distribute Global — diseño:**
- Ancla = capital de área (igual que Gather Global).
- Capital nacional excluida.
- 5 áreas por pulso.
- 3 rangos: 5, 10, 15 pops por province.
- Threshold del ancla: base (ciudad: 40 / metrópolis: 80) + (pops a repartir × provinces del área — script_value dinámico).
- Si ancla no califica → saltea área.

**Constructor Automático — diseño:**
- Barre settlements del área.
- Demolish de todos los edificios de producción.
- NUNCA toca `fortress_building`.
- NUNCA toca ciudades ni metrópolis.
- Construye edificio según trade good (tabla definitiva en sesión 18:40).

**Script value dinámico — confirmado en vanilla:**
- `area = { every_area_province = { limit = { num_of_X_building >= 1 } add = N } }` funciona en script_values.
- Confirmado en `00_mission_seleukid.txt` con `num_of_fortress_building`.

### ❓ Quedó abierto
- Threshold de producción de trade good (resuelto en sesión 17:02 y corregido en 17:52).
- Tabla del Constructor Automático (cerrada definitivamente en sesión 18:40).
- Calibración números Distribute — 5/10/15 provisorios.

---

## 2026-05-26 — Actualización sistema de control (PROMPT_MAESTRO v3.2 + SESSION_LOG + convención de nombres)

### ✅ Decidido
- Convención de nombres formalizada: `AAAA-MM-DD_HH-MM` para todos los archivos del sistema. Sin letras de sufijo. Ver Sección 3.2.1.
- Regla nueva: antes de generar cualquier archivo con fecha/hora, la IA pregunta la hora al operador.
- SESSION_LOG definido como 4to archivo del sistema de control — generado por la IA al cierre de cada sesión, cargado al inicio de la siguiente si existe, propagado al SUPERBACKUP cuando el operador lo decide.
- Regla nueva: cuando la sesión sea larga o se acerque al límite de contexto, la IA sugiere fuertemente generar el SESSION_LOG antes de continuar.
- Referencias a nombres hardcodeados de archivos reemplazadas por "ver Sección 22" en todo el SUPERBACKUP.
- Sección 22 nueva — tabla única de archivos activos, referencia cruzada permanente.
- Sección 3.2.1 nueva — convención de nombres completa con tabla, ejemplos y reglas.
- Sección 20.3 actualizada — checklist ampliado: Sección 22, INSTRUCCIONES_HUMANO, SESSION_LOG.
- Sección 20.4 nueva — cuándo actualizar INSTRUCCIONES_HUMANO.
- Sección 0.2 actualizada — SESSION_LOG en checklist y protocolo de arranque; preguntar hora antes de generar zip.
- Sección 0.4d actualizada — flujo de trabajo con SESSION_LOG y convención de nombres.
- INSTRUCCIONES_HUMANO actualizado a 2026-05-26: nombres de archivos, orden de carga, protocolo de fin de sesión, referencia a Sección 22, Smoke Test con pregunta nueva sobre hora.
- PROMPT_MAESTRO actualizado a v3.2: zip y SUPERBACKUP actualizados, SESSION_LOG en PASO 1 y FORMATO DE ENTREGA, convención de nombres, regla de preguntar hora, regla de sugerir log antes de quedarse sin contexto.

### ❓ Quedó abierto
- Optimize Global on_action (5 bloques/pulso, rangos automáticos por pops de capital).
- `exodos.3` — evento silencioso de cleanup 365 días.
- Corrección variable en stub `iram_20` (`gather_active` → `distribute_active`) + guards pendientes.
- 3 variables nuevas en `exodos_cleanup_effect`.

### ⚠️ Premisas activas sin cambios
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Ascenso/Descenso Forzado — threshold sin testear.
- `current_ruler` desde country scope en TLV — sin testear.

---

## 2026-05-25 — Implementación v4.1 → v4.3.2 + auditoría de archivos

### ✅ Decidido
- v4.1: Separación de archivos por función. `iram_decisions_demografia.txt` con Relics + Migración + Ascenso + Descenso (IDs `iram_22`–`iram_29`). `exodos_scripted_effects.txt` expandido con `iram_cleanup_menu` e `iram_cleanup_demografia`.
- v4.2: `iram_decisions_menu.txt` nuevo con sistema de menú `iram_01`–`iram_11`. Localizaciones ES/EN del menú nuevas.
- v4.3: `exodos_decisions_rival_heir.txt` — Heredero del Rival integrado al menú con `has_variable = iram_rival_heir_open` en `potential`.
- v4.3.2: Refactor masivo — 44 IDs de decisiones renombrados a prefijo `iram_` con numeración `iram_01`–`iram_45`. Costo Gather Global reducido: tyranny 100→50, popularidad -100→-50. Stub `iram_20_activate_optimize_global` nuevo. `exodos.2` nuevo en events. Localizaciones actualizadas.
- Slave Distributor: DESCARTADO — Optimize Global cubre la función.
- Condición `has_spouse` en Heredero del Rival: CERRADA — el hijo spawna sin familia si no existe esposa. Comportamiento aceptado.
- Reliquia migración `global_migration_speed = 2.5`: CERRADA — reemplazada por Migración Forzada.
- Convención de nombres de archivos adoptada: zips `mod_pack_IRAM_vX_X_X_AAAA-MM-DD_HH-MM.zip`, logs `IRAM_SESSION_LOG_AAAA-MM-DD_HH-MM.md`.
- Zip canónico activo: `mod_pack_IRAM_v4_3_2_2026-05-25_E.zip` (nombre original: `mod_pack_IRAM_v4_3_2(1)`, creado 25/5 18:47, 37.545 bytes).
- SUPERBACKUP actualizado a v2.2 (sesión 26/05/2026 01:00).

### ❓ Quedó abierto
- Optimize Global on_action (5 bloques/pulso, rangos automáticos por pops de capital).
- `exodos.3` — evento silencioso de cleanup 365 días.
- Corrección de variable en stub `iram_20` (`gather_active` → `distribute_active`) + guards pendientes.
- 3 variables nuevas en `exodos_cleanup_effect`.
- PROMPT_MAESTRO pendiente de actualizar a v3.2.

### ⚠️ Premisas activas
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Ascenso/Descenso Forzado — threshold sin testear.
- `current_ruler` desde country scope en TLV — sin testear.

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
- [ ] El header refleja "ver Sección 22" (no un nombre hardcodeado)
- [ ] El footer (`*IRAM SUPERBACKUP vX.Y*`) está actualizado
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

## 21.1 Qué cambió en cada versión de v4

| Zip canónico | Nombre original | Fecha/Hora | Tamaño | Cambio principal |
|---|---|---|---|---|
| `mod_pack_IRAM_15_GATHER_GLOBAL_v1_3.zip` | ídem | 22/5 14:54 | 29.801 b | Histórico — base experimental con Migración Forzada |
| `mod_pack_IRAM_v4_1_2026-05-23_A.zip` | `mod_pack_IRAM_v4_1` | 25/5 17:06 | 32.193 b | Separación archivos por función, iram_decisions_demografia, cleanup menu/demografia |
| `mod_pack_IRAM_v4_2_2026-05-25_B.zip` | `mod_pack_IRAM_v4_2` | 25/5 17:21 | 35.430 b | Sistema de menú navegable (iram_01–iram_11), localizaciones menú |
| `mod_pack_IRAM_v4_3_2026-05-25_C.zip` | `mod_pack_IRAM_v4_3` | 25/5 17:40 | 36.036 b | Rival Heir integrado al menú (has_variable = iram_rival_heir_open) |
| `mod_pack_IRAM_v4_3_2_2026-05-25_D.zip` | `mod_pack_IRAM_v4_3_2` | 25/5 18:43 | 36.471 b | Refactor 44 IDs iram_+numeración, costo GG reducido |
| `mod_pack_IRAM_v4_3_2_2026-05-25_E.zip` | `mod_pack_IRAM_v4_3_2(1)` | 25/5 18:47 | 37.545 b | Stub iram_20, exodos.2, localizaciones iram_20+exodos.2 |
| `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` ✅ **CANÓNICO** | ídem | 27/5 17:14 | — | 5 bugs corregidos: BOM doble, llaves desbalanceadas ×2, scope popularity, nombre variable cleanup_menu |

**Duplicados verificados — descartar:**

| Nombre original | Duplicado de | Verificación |
|---|---|---|
| `mod_pack_IRAM_v4_1(1)` | v4_1 | md5sum idéntico — 0 bytes diferentes |
| `mod_pack_IRAM_v4_3(1)` | v4_3 | md5sum idéntico |
| `mod_pack_IRAM_v4_3_1_` | v4_3 | md5sum idéntico |
| `mod_pack_IRAM_v4_3_2(2)` | v4_3_2(1) | md5sum idéntico |

**Zips históricos anteriores a v4.1:**

| Nombre de archivo | Versión | Fecha | Estado | Diferencia clave vs anterior |
|---|---|---|---|---|
| `mod___SUPERBACKUP_.zip` | IRAM v1 (Estable v1.3.5) | 2026-05 | Histórico | Spawn en `capital_scope`, `war=no` obligatorio, sin Optimize, sin Heredero |
| `mod_alt___SUPERBACKUP_.zip` | IRAM v2 (ALT v1.3) | 2026-05 | Histórico | Spawn en posición rival, `war=no` eliminado, BOM absorbe kill_ruler, IHA nuevo |
| `mod_pack_IRAM_13__SUPERBACKUP_.zip` | IRAM v1.3 (histórico) | 2026-05 | Histórico | Versión intermedia entre v2 y v3 |
| `mod_pack_IRAM_15.zip` | IRAM v3 FINAL | 2026-05 | ✅ CERRADO — zip canónico de v3 | Optimize 4 rangos, Heredero del Rival v1.6, herencia matrilineal, todo en `exodos/` |
| `mod_pack_IRAM_v4_3.zip` | IRAM v4 experimental | 2026-05-19 | 🗃 DESCARTADO — rama scripted_gui | scripted_gui, 2 unidades inmóviles, sin activates — ver Sección 18.4 |
| `mod_pack_IRAM_15_GATHER_GLOBAL_v1_2.zip` | IRAM v4.0 (pre-renombrado) | 2026-05-21 | 🗃 RENOMBRADO | Gather Global v1.2 con capital exclusion, Distribute 4 rangos, Relics tokens corregidos |
| `mod_pack_IRAM_v4_0.zip` | IRAM v4.0 | 2026-05-21 | 🗃 HISTÓRICO | Mismo contenido que GATHER_GLOBAL_v1_2, renombrado como versión oficial v4 |

**Regla de uso:**
- Para trabajo activo: cargar `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip`
- Para referencia de v3 estable: cargar `mod_pack_IRAM_15.zip`
- Para análisis histórico: cargar el zip de la versión específica
- Nunca mezclar código de zips distintos sin verificar diferencias en Sección 0.4b

---

---

# ══════════════════════════════════════════════════════════
# SECCIÓN 22 — ARCHIVOS ACTIVOS DEL PROYECTO
# ══════════════════════════════════════════════════════════

**Actualizar esta tabla cada vez que se genera una versión nueva de cualquier archivo.**
Es la única fuente de verdad para nombres de archivos activos. Todos los demás lugares del proyecto referencian esta sección.

| Archivo | Nombre actual | Versión |
|---|---|---|
| TECHNICAL_WIKI (ACTIVE) | `IRAM_TECHNICAL_WIKI_ACTIVE_v3_0_2026-05-27_20-28.md` | v3.0 |
| TECHNICAL_WIKI (ARCHIVE) | `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_0_2026-05-27_20-28.md` | v3.0 |
| PROMPT_MAESTRO | `IRAM_PROMPT_MAESTRO_v3_7_2026-05-27_15-17.md` | v3.7 ⚠️ pendiente actualizar |
| INSTRUCCIONES_HUMANO | `IRAM_INSTRUCCIONES_HUMANO_2026-05-26_21-22.md` | — ⚠️ pendiente actualizar |
| SESSION_LOG (último) | `IRAM_SESSION_LOG_2026-05-27_20-06.md` | — |
| Zip canónico | `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | v4.3.7 |

**Reglas:**
- Esta tabla se actualiza al final de cada sesión que genere un archivo nuevo.
- El SESSION_LOG se carga al inicio de la sesión siguiente si existe. No es bloqueante si no existe.
- Para historial completo de zips: ver Sección 21.

---

*IRAM TECHNICAL WIKI ACTIVE v3.0 — 2026-05-27 20:28*
*IRAM v4 en desarrollo | Engine: Imperator Roma 2.0.4*
*Archivos activos: ver Sección 22*
*Basado en SUPERBACKUP v2.6. Cambios v3.0: split en ACTIVE + ARCHIVE. ACTIVE contiene Secciones 0–7, 9–13, 16–17, 19 (entradas v4 únicamente), 20–22. Sección 0.1 y mapa actualizados para reflejar la separación.*
