# DRAGO MOD PACK — DISTRIBUCIÓN ALTERNATIVA
## Backup Técnico Unificado
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | mod_alt.zip | v1.3-alt

---

## INSTRUCCIONES PARA LA IA QUE LEA ESTE DOCUMENTO

Este documento es el backup técnico completo de la **distribución alternativa** del Drago Mod Pack.
Es completamente autónomo — no requiere leer ningún otro documento para trabajar con esta distribución.

Antes de trabajar en cualquier mod:
1. Leer este documento completo de principio a fin.
2. Leer también el zip `mod_alt.zip` para verificar el estado real de los archivos fuente.
3. No asumir valores del engine de memoria — verificar contra los archivos fuente o las secciones de código de este documento.
4. Las decisiones marcadas como CERRADO no se reabren salvo pedido explícito del usuario.
5. El modelo económico de TGL está CERRADO en su totalidad. No recalcular salvo pedido explícito.

### Diferencia central respecto a la distribución estable

En la distribución estable, `exodos_activate_gather` y `exodos_activate_distribute` spawnean
la unidad marcadora en `capital_scope`. El jugador la mueve manualmente al territory destino.
Además, todas las operaciones requieren `war = no`.

En esta distribución alternativa, el marcador **spawna directamente en la province donde está
el ejército del rival calificado**. El jugador recluta una leva del rival en la province que
elige, ejecuta activate, y el marcador aparece ahí. Además, `war = no` fue eliminado de todas
las operaciones — Exodus alt es operable en guerra.

BOM, TLV y TGL son idénticos en ambas distribuciones.

### Flujo de trabajo con la IA

El flujo normal es:
1. El usuario sube los backups (estable y alt) y los zips actuales al inicio de la sesión.
2. La IA lee todo, se pone al día, y trabaja sobre los archivos fuente.
3. La IA entrega los archivos corregidos individualmente y el zip final listo para instalar.
4. El usuario extrae el zip en la carpeta mod, reemplazando todo — instalación limpia.

`build_mods_alt.py` es una herramienta alternativa para el caso en que el usuario edite archivos fuente por su cuenta y necesite regenerar y validar el zip manualmente. Uso: `python build_mods_alt.py` desde la carpeta raíz del mod. Valida BOM en todos los archivos antes de empaquetar y aborta si hay errores. En el flujo normal con IA no se usa.

---

## ESTADO ACTUAL

| Item | Valor |
|---|---|
| Versión | v1.3-alt |
| Fecha último build | 2026-05 |
| Exodos ALT | 1.21 ALT |
| By Other Means | 3.0 |
| The Last Vote | 1.7 |
| The Great Leap | 1.5 |
| Fixes pendientes | Ninguno |

---

## 1. ECOSISTEMA

### 1.1 Tabla de mods

| Mod | Función | Prefijo | Versión .mod | Validado en juego |
|---|---|---|---|---|
| Exodus ALT | Movimiento de población — spawn en posición del rival | `exodos_` | 1.21 ALT | 2026-05 |
| By Other Means | Elimina/gestiona rivales y gobernante; holdings | `bom_` / `iha_` | 3.0 | — |
| By Other Means — Ego Sum | Maximiza stats del gobernante (módulo de BOM) | `bom_` | — (módulo) | 2026-04 |
| By Other Means — Bacanal | Corrompe rivales del gobernante (módulo de BOM) | `bom_` | — (módulo) | 2026-04 |
| The Last Vote | Disuelve república → dictadura | `tlv_` | 1.7 | — |
| The Great Leap | Compra árbol completo de innovations (one-shot) | `tgl_` | 1.5 | 2026-04 |

Todos los mods se distribuyen en un único zip: `mod_alt.zip`.
El script de generación manual es `build_mods_alt.py` — ver sección de flujo de trabajo.

### 1.2 Reorganización v1.2 (estable)

En v1.2 del ecosistema estable, `by_other_means/` absorbió las funciones que antes estaban en `the_last_vote/` y agregó las dos funciones Iron Hand. Esta reorganización aplica igual a la distribución alt.

| Función | Mod anterior | Mod actual |
|---|---|---|
| Eliminar rivales | BOM | BOM (sin cambio) |
| Bacanal | BOM | BOM (sin cambio) |
| Ego Sum | BOM | BOM (sin cambio) |
| Et tu, Brute? (kill ruler) | TLV | BOM (renombrado a `bom_kill_ruler`) |
| Confiscar Propiedades | nuevo | BOM (`iha_seize_holdings`) |
| Fill the Void | nuevo | BOM (`iha_fill_the_void`) — otorga propiedades vacías al rival seleccionado |
| Disolver república | TLV | TLV (sin cambio) |

### 1.3 Flujo combinado sugerido

```
1. BOM           → Reducir rivales a exactamente 1 (condición necesaria para Exodus Gather/Distribute)
2. EXODUS ALT    → Reclutar leva del rival en territory destino → Gather o Distribute
3. BOM BACANAL   → Corromper al rival único restante (alternativa a eliminarlo)
4. IHA SEIZE     → Confiscar propiedades del rival único restante
5. IHA FILL VOID → Otorgar todas las propiedades sin dueño al rival seleccionado
6. BOM EGO SUM   → Maximizar los stats del gobernante
7. BOM KILL      → Eliminar al gobernante actual si obstaculiza el golpe
8. TLV CONFIRM   → Disolver la república cuando las condiciones son óptimas
9. TGL           → Comprar el árbol de innovations una vez consolidado el poder
10. VANILLA      → anoint_heir para nominar sucesor con dictadura activa
```

**Nota importante:** Exodus alt (Gather/Distribute) requiere exactamente 1 rival en `in_command`.
Usar BOM Eliminar antes de Exodus para llegar a 1 rival es el flujo típico. Transfer no tiene
condición de rival y puede usarse en cualquier momento.

Cada mod es independiente — el flujo es una sugerencia, no una dependencia técnica.

### 1.4 Tabla de costos y condiciones — ecosistema completo

| Mod | Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | War | Condiciones extra |
|---|---|---|---|---|---|---|---|---|
| Exodus ALT | Gather activate | — | — | — | — | — | permitida | 1 rival exacto, employer=ROOT, in_command=yes |
| Exodus ALT | Gather confirm | 1000 | 5 | 2500 | +10 | ≤90 | permitida | unidad detenida, área 100% propia |
| Exodus ALT | Distribute activate | — | — | — | — | — | permitida | 1 rival exacto, employer=ROOT, in_command=yes |
| Exodus ALT | Distribute confirm | 1000 | 5 | 2500 | +10 | ≤90 | permitida | unidad detenida, área 100% propia |
| Exodus ALT | Transfer activate | — | — | — | — | — | permitida | — |
| Exodus ALT | Transfer confirm | 2000 | 10 | 5000 | +20 | ≤80 | permitida | unidades detenidas, territories owner=ROOT |
| BOM | Eliminar | 2000 | 1 | 500 | +40 | ≤80 | — | rivals ≥ 1 |
| BOM | Bacanal | 500 | — | — | +10 | ≤90 | — | rivals ≥ 1 |
| BOM | Ego Sum | — | — | — | — | — | — | one-shot por path |
| BOM | Kill Ruler | 2000 | 1 | 500 | +40 | ≤60 | — | stability ≥ 50 |
| IHA | Confiscar | 2000 | — | — | +40 | ≤60 | — | rivals=1 exacto, mismo país |
| IHA | Fill the Void | 2000 | — | — | +40 | ≤60 | — | rivals=1 exacto, mismo país |
| TLV | Confirm | 2000 | — | — | +40 | ≤60 | — | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL | Purchase | dinámico | — | — | +100 | ≤0 | — | one-shot |

### 1.5 Scopes por función

| Mod | Función | Scopes |
|---|---|---|
| Exodus ALT | Gather / Distribute | country → character → unit → province → pop |
| Exodus ALT | Transfer | country → unit → province → pop |
| BOM | Eliminar / Bacanal | country → character → character (rival) |
| BOM | Ego Sum | country → character |
| BOM | Kill Ruler | country → character |
| IHA | Confiscar | country → character → character (rival) → province (holding) |
| IHA | Fill the Void | country → character (rival) → province |
| TLV | Confirm | country → character (solo en allow) |
| TGL | Purchase | country → province → country |

Gather y Distribute agregan el paso `country → character` para navegar al rival y capturar
la posición de su ejército antes de spawnear el marcador.

### 1.6 Advertencias de flujo

**Exodus ALT — Gather/Distribute requieren rival en comando:** si el rival no está en `in_command`,
las decisiones no aparecen en el panel. Reclutar una leva del rival en el territory destino
antes de ejecutar activate — esa leva activa `in_command = yes`.

**Exodus ALT — el rival es solo un selector de province:** el rival y su ejército cumplen una única función — indicar la province donde spawnear la unidad marcadora en activate. Una vez que el marcador existe en el mapa, el rival ya cumplió su rol. Si después disuelve su ejército, no hay estado inválido: el marcador sigue en el mapa y el jugador lo mueve o confirma normalmente desde ahí.

**Exodus ALT — guerra permitida:** `war = no` fue eliminado de todas las operaciones. El pulso
mensual sigue siendo el guard de runtime — si el área deja de ser 100% propia o el ancla cambia
de dueño, `exodos.1` cancela la operación automáticamente.

**Exodus ALT — Transfer sin condición de rival:** Transfer no requiere rival en comando. Se puede
usar en cualquier momento, también en guerra.

**IHA y la condición rivals=1:** IHA Confiscar e IHA Fill the Void requieren exactamente 1 rival en total, del mismo país que root. Usar BOM Eliminar primero puede dejar al jugador con 1 rival si había 2, habilitando IHA.

**IHA Confiscar no mata:** el rival sobrevive con loyalty penalizada por `family_property_seized_l` (-40 por 20 años).

**IHA Fill the Void otorga propiedades al rival seleccionado:** le otorga todas las propiedades vacías del país.

**BOM Kill Ruler disponible en cualquier tipo de gobierno:** no requiere república.

**BOM (Eliminar Rivales) disponible en guerra:** sin restricción `war = no`.

**TLV confirm es irreversible:** disolver la república no tiene marcha atrás.

**Ego Sum y Bacanal son one-shot por partida:** una vez usadas no se pueden repetir aunque el gobernante muera.

**Popup de BOM eliminado en v1.2:** todos los mods son silenciosos excepto TLV Confirm (`tlv.2`) y Exodus (`exodos.1`).

### 1.7 Compatibilidad con saves existentes

| Mod | Sobre partida existente | Notas |
|---|---|---|
| Exodus ALT | ⚠️ No verificado | Usa unidades marcadoras y variables de estado — riesgo de estado inválido |
| By Other Means | ✓ Compatible | Sin variables persistentes ni unidades |
| BOM — Ego Sum | ✓ Compatible | Variables one-shot se crean al usar la decisión |
| BOM — Bacanal | ✓ Compatible | Sin variables de estado |
| BOM — Kill Ruler | ✓ Compatible | Stateless |
| IHA — Confiscar | ✓ Compatible | Stateless |
| IHA — Fill the Void | ✓ Compatible | Stateless |
| The Last Vote | ⚠️ No verificado | Modifica variables internas del engine al cambiar gobierno |
| The Great Leap | ✓ Compatible | Variable one-shot `tgl_purchased` se crea al usar la decisión |

**Recomendación general:** activar todos los mods antes de iniciar una partida nueva.

### 1.8 Límites conocidos del engine

| Límite | Valor | Confirmado en |
|---|---|---|
| Máximo de rivales por personaje | 4 | BOM — límite del engine, no del mod |
| Máximo de `add_trait` en una decisión | Sin límite confirmado | Ego Sum usa hasta 10 — validado |
| `every_rival` desde country scope | No funciona directo — requiere entrar a character scope primero | BOM v2.5 |
| `add_health = -100` | Determinista — no hay fallo real | BOM |
| `country_event` siempre dispara en `root` | No dispara en el país del objetivo — solo en el propio | BOM v2.1 |
| Slots de edificios | `floor(pops/10) + local_building_slot` del rank | Defines: `POPS_PER_BUILDING = 10` |
| `every_holdings` / `remove_holding` | Funciona desde cualquier character scope — no requiere head of family | confirmado en game files |
| `add_holding` / `remove_holding` | Effects reales scriptables desde character scope | confirmado en game files |
| `num_holdings_owned` | Trigger válido en character scope | confirmado en game files |
| `family_property_seized_l` | loyalty key vanilla: -40 por 20 años | confirmado en game files |
| `unit_commander` como trigger | No existe — cero hits en game.zip (1012 archivos) | Exodus alt — investigación exhaustiva |
| `location = { }` desde character scope | Resuelve capital de gobernación, no posición del ejército | Exodus alt |
| `commander = scope:X` en `random_unit` / `any_unit` | Trigger válido desde country scope | `roman_flavor.txt`, `power_base_character_events.txt` — vanilla |
| Un character puede comandar N ejércitos | Falso — máximo 1 ejército por character, limitación hard del engine | Exodus alt |

### 1.9 Convenciones del ecosistema (CERRADO)

| Convención | Valor | Razón |
|---|---|---|
| `is_ai = no` en `potential` y `allow` | Siempre en ambos | `potential` filtra visualmente, `allow` es segunda línea de defensa |
| Cobro en `confirm`, no en `activate` | Siempre (Exodus); en decisiones one-shot, cobro directo en `effect` | El jugador paga solo cuando está seguro de ejecutar |
| Sin cooldown | Siempre | Variables de tiempo generan fallos; `is_ai = no` es la única restricción de abuso |
| UTF-8 BOM en todos los .txt y .yml | Obligatorio | Sin BOM el engine no parsea los archivos del mod |
| Sin BOM en .mod y descriptor.mod | Obligatorio | Con BOM el engine corrompe la entrada |
| `ai_will_do = { factor = 0 }` | Siempre | Excluye a la IA de todas las decisiones del ecosistema |
| Ironman compatible | Obligatorio | Ningún mod usa mecanismos que rompan Ironman |
| Zip unificado | `mod_alt.zip` entregado por la IA | Un solo archivo de distribución, BOM validado |
| Sin popups de éxito | A partir de v1.2 | Solo quedan popups de error (exodos.1) y estado (tlv.2) |
| Todo lo visible al usuario va en el idioma del usuario | Obligatorio | Incluye nombres de decisiones, descripciones, tooltips, eventos, y nombres de unidades. La versión EN usa inglés, la versión ES usa español. El código interno (variables, keys, prefijos) siempre en inglés. |

### 1.10 Nombres de unidades Exodus

Los nombres de unidades son UI — van en el idioma del usuario.

| Código (`decisions.txt`) | Interfaz EN | Interfaz ES |
|---|---|---|
| `"Exodos - Origin"` | Exodos - Origin | Exodos - Origen |
| `"Exodos - Destination"` | Exodos - Destination | Exodos - Destino |
| `"Exodos - Concentrate"` | Exodos - Concentrate | Exodos - Concentrar |
| `"Exodos - Distribute"` | Exodos - Distribute | Exodos - Distribuir |

El `decisions.txt` contiene el nombre que aparece en el mapa. Para la versión en español, estos nombres deben estar en español en el archivo de código.

---

## 2. GOTCHAS DEL ENGINE

Conocimiento confirmado en juego. Verificar esta tabla antes de escribir cualquier script nuevo.

### 2.1 Scopes

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| `ruler = { }` desde country scope en effect | `every_character = { limit = { is_ruler = yes } ... }` | BOM v2.5, TLV v1.3 — 1454 hits en error.log |
| `ruler = { }` desde country scope en trigger | `any_character = { is_ruler = yes ... }` | BOM v2.5 |
| `every_rival = { }` directo desde country scope | `every_character = { limit = { is_ruler = yes } every_rival = { } }` | BOM v2.5 |
| `move_pop = prev` desde scope pop | `save_scope_as` antes del bucle + `move_pop = scope:nombre` | Exodus bug 1 |
| `move_pop = prev.prev` desde scope anidado | `save_scope_as = nombre` antes del `while` + `move_pop = scope:nombre` | Exodus bug 15 |
| `every_owned_province { limit = { has_variable = X } }` para filtrar área | `var:province = { area = { every_area_province = {} } }` | Exodus bug 2 |
| Iterar holdings y remover en el mismo loop | `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = x } remove_holding = scope:x }` — `remove_holding` va dentro del `while` pero fuera del bloque `random_holdings` | IHA Seize — confirmado en engine 2026-05 |
| `current_ruler` desde province scope | No resuelve — guardar con `every_character = { limit = { is_ruler = yes } save_scope_as = X }` antes del loop y usar `scope:X` dentro | IHA Fill the Void bug |
| `unit_commander` como trigger en unit scope | No existe — usar `commander = scope:X` como filtro en `any_unit`/`random_unit` desde country scope | game.zip exhaustivo — Exodus alt |
| `location = { }` en character scope para posición del ejército | Resuelve capital de gobernación, no posición del ejército — navegar vía `random_unit { limit = { commander = scope:rival } } unit_location = { save_scope_as = X }` | Exodus alt |
| `commander = scope:X` en `limit` de `random_unit` / `any_unit` | Trigger válido en unit scope desde country scope — filtra unidades por commander | `roman_flavor.txt`, `power_base_character_events.txt` — vanilla |
| Un character puede comandar N ejércitos simultáneamente | Falso — limitación hard del engine, máximo 1 ejército por character | Exodus alt |

### 2.2 Variables y flags

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| `set_country_flag` / `has_country_flag` / `clr_country_flag` | `set_variable` / `has_variable` / `remove_variable` | Exodus bug 4 |
| `set_province_flag` / `has_province_flag` / `remove_province_flag` | `set_variable` / `has_variable` / `remove_variable` en scope province | Exodus bug 4 |
| `set_unit_flag` / `has_unit_flag` | `set_variable` / `has_variable` en scope unit | Exodus bug 4 |
| `check_variable = { ... }` como trigger | `var:nombre >= valor` directo | Exodus bug 4 |
| `var:X >= var:Y` (dos variables en trigger) | Contador descendente, comparar contra 0 | Exodus bug 3 |
| Scopes `save_scope_as` | No persisten entre ticks — no necesitan cleanup en `exodos_cleanup_effect` | Exodus alt |

### 2.3 Localización

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| Corchetes `[ ]` en texto libre de yml | Usar paréntesis `( )` — el engine parsea `[ ]` como variables dinámicas y falla con `Data error in loc key` | TGL v1.3, Exodus bug 24 |
| BOM UTF-8 ausente en .txt o .yml del mod | Agregar BOM `EF BB BF` — usar `build_mods_alt.py` o Python `utf-8-sig`, nunca editar a mano | Todos los mods |
| BOM presente en descriptor.mod o .mod raíz | Eliminar — esos archivos van sin BOM | Todos los mods |
| BOM escrito como texto literal `\xEF\xBB\xBF` | BOM real vía Python `b'\xef\xbb\xbf'` o `utf-8-sig` | TGL v1.1, Exodus bug 12 |

### 2.4 Sintaxis que no existe

| Sintaxis errónea | Reemplazo correcto | Confirmado en |
|---|---|---|
| `every_owned_territory` | `every_owned_province` | TGL v1.1 |
| `province_rank = city_metropolis` | `has_province_rank = city_metropolis` | TGL v1.1 |
| `num_of_pops` como script value o trigger | `total_population >= N` en scope province | Exodus bug 9 |
| `disband_unit = yes` | `destroy_unit = yes` | Exodus bug 4 |
| `is_triggered_only = yes` en eventos de mod | Eliminar | Exodus bug 8 |
| `ai_will_do = { value = 0 }` | `ai_will_do = { factor = 0 }` | Exodus bug 4 |
| `on_action = { monthly_country_pulse = {} }` con wrapper | Raíz directa: `monthly_country_pulse = {}` | Exodus bug 5 |
| `scripted_effects = { ... }` con wrapper | Raíz directa: `nombre_effect = {}` | Exodus bug 6 |
| `death = { death_reason = ... }` desde ruler scope | No funciona, silencioso — sin reemplazo confirmado | BOM, TLV |
| `has_holding` como trigger directo | `num_holdings_owned > 0` en character scope | IHA design |

### 2.5 Cambio de gobierno

| Regla | Detalle | Confirmado en |
|---|---|---|
| Orden obligatorio para cambio a dictadura | `clearup` → `law_variable` → `change_government` → `law_change` | TLV v1.0 |
| `change_government = dictatorship` sin clearup | Variables de dictadura/senate quedan huérfanas | TLV |
| `dictatorship` es `type = monarchy` | `nominated_heir` funciona sin restricciones | TLV |
| `nominated_heir_modifier` en república | Se cancela automáticamente (`is_monarchy = no`) | TLV |
| `minimum_electable_age` override | No existe — propiedad fija del tipo de gobierno | TLV |

### 2.6 Holdings

| Regla | Detalle | Confirmado en |
|---|---|---|
| Iterar holdings desde character scope | `every_holdings = { }` — funciona desde cualquier character | game files |
| Remover holding en loop | Patrón correcto y validado en engine: `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = x } remove_holding = scope:x }` — `remove_holding` va dentro del `while` pero **fuera** del bloque `random_holdings` | IHA Seize — confirmado en engine 2026-05 |
| Agregar holding al rival desde country | `every_owned_province { limit = { NOT = { exists = holding_owner } } scope:iha_rival_scope = { add_holding = PREV } }` | IHA design |
| Capital excluida automáticamente | El engine no asigna holding slot a la capital — `NOT = { exists = holding_owner }` no matchea la capital | confirmado en game files |
| `add_loyalty` con named key | Solo acepta loyalty keys definidas en `common/loyalty/` — no literales numéricos | IHA design |
| `family_property_seized_l` | Loyalty key vanilla existente: -40 por 20 años, disponible sin definir archivo propio | confirmado en game files |

### 2.7 Miscelánea

| Regla | Detalle | Confirmado en |
|---|---|---|
| Multiplicador manpower x500 | Valor en script = valor pantalla / 500 | Exodus |
| `country_event` siempre dispara en `root` | No dispara en el país del objetivo — solo en el propio | BOM v2.1 |
| Cooldown con variables de tiempo | Genera fallos en el delay — no usar | BOM v2.3 |
| IDs de eventos | Deben ser numéricos: `exodos.1`, no `exodos.fail` | Exodus bug 10 |
| Slots de edificios | `floor(pops/10) + local_building_slot` del rank | Defines: `POPS_PER_BUILDING = 10` |

---

## 3. GUÍA DE DIAGNÓSTICO — error.log

El archivo se encuentra en:
```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\logs\error.log
```

Se sobreescribe en cada sesión de juego. Abrirlo mientras el juego está corriendo puede dar lecturas incompletas — cerrarlo primero.

### 3.1 Errores críticos del ecosistema

| Mensaje en error.log | Causa | Solución |
|---|---|---|
| `Wrong scope for effect: country, expected character` | Uso de `ruler = { }` desde country scope en effect | Reemplazar por `every_character = { limit = { is_ruler = yes } ... }` |
| `Wrong scope for trigger: country, expected character` | Uso de `ruler = { }` desde country scope en trigger | Reemplazar por `any_character = { is_ruler = yes ... }` |
| `Data error in loc key` | Corchetes `[ ]` en texto libre de yml | Reemplazar por paréntesis `( )` |
| `Corrupt Decision Table Entry - '\xEF\xBB\xBFcountry_decisions'` | BOM pegado al token — archivo editado a mano | Regenerar con `build_mods_alt.py` |
| `Creation of dynamic token "\xEF\xBB\xBF..."` | BOM en scripted_effects — archivo editado a mano | Regenerar con `build_mods_alt.py` |
| `Unknown effect/trigger` en decisión | Sintaxis no existe en el engine | Ver sección 2.4 |
| `could not find unit type exodos_marker` | Archivo `exodos_units.txt` sin BOM o no encontrado | Verificar BOM y ruta del archivo |

### 3.2 Cómo verificar que el ecosistema está limpio

Después de cargar una partida con los mods activos, buscar en error.log:

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

### 3.3 Errores que NO son del ecosistema

Ignorar entradas que referencien rutas del juego base (`Imperator/game/`).

### 3.4 Errores de vanilla documentados — ignorar siempre

| Mensaje | Hits aprox. | Causa | Acción |
|---|---|---|---|
| `has_province_modifier` Wrong scope | ~118 | Game files de vanilla | Ignorar — vanilla puro |
| `Missing Icon for Modifier: exodos_marker_*` | 19 | Unit type sin íconos GFX | Permanente e ignorable — no afectan ninguna mecánica |

---

## 4. EXODUS ALT — POPULATION MANAGEMENT

### 4.1 Terminología engine

| Diseño | Engine |
|---|---|
| "territory" / "location" | `province` (scope) |
| "provincia" geográfica | `area` (scope) |
| "región" | `region` (scope) |

### 4.2 Arquitectura

- 3 operaciones independientes: Gather, Transfer, Distribute
- 1 sola operación activa a la vez
- IA excluida: `is_ai = no` en `potential` y `allow` de todas las decisiones
- Sin cooldown — las decisiones se rehabilitan inmediatamente tras éxito o cancelación
- Cobro de oro, manpower y tyranny en confirm, no en activate
- Unidades Exodos permanecen en el mapa durante la operación — son el sensor de estado
- Si una unidad es destruida o el territorio cambia de dueño → el pulso detecta y cancela
- Gather y Distribute requieren área 100% propia al confirmar y durante la operación
- **ALT:** `war = no` eliminado de todas las operaciones — Exodus es operable en guerra
- **ALT:** Gather y Distribute requieren exactamente 1 rival en `in_command` para activate

**Flujo:**
```
FASE 1 — ACTIVAR:   captura posición del ejército del rival → spawna unidad(es) ahí → set _pending (sin cobro)
FASE 2 — CONFIRMAR: cobra costos → guarda unit_location como var país → set operation_active
FASE 3 — PULSO:     monthly_country_pulse → verifica estado → ejecuta → cleanup condicional
```

**Costos:**

| Operación | Oro | Manpower (script) | Manpower (pantalla) | Tyranny | Tyranny cap | Pulsos |
|---|---|---|---|---|---|---|
| Gather | 1000 | 5 | 2500 | +10 | 90 | ≥1 (hasta fuentes < 2 pops) |
| Distribute | 1000 | 5 | 2500 | +10 | 90 | ≥1 (hasta ancla < 30 pops) |
| Transfer | 2000 | 10 | 5000 | +20 | 80 | 10 fijos |

> El engine multiplica el manpower por ×500 al mostrarlo en pantalla. Valor en script = valor pantalla / 500.

**Cleanup condicional — Gather y Distribute:**
El cleanup no es incondicional al terminar el bloque. Gather limpia cuando todas las fuentes del área llegan a `total_population < 2`. Distribute limpia cuando el ancla llega a `total_population < 30`. En áreas muy pobladas la operación puede extenderse más de un pulso. Este comportamiento es intencional — los pisos son la condición de fin natural de la operación.

**Mejora futura pendiente:** evaluar agregar un contador de pulsos como límite de seguridad secundario para Gather y Distribute, similar al `exodos_pulse_counter` de Transfer.

### 4.3 Operaciones

**GATHER** — concentra pops de toda el área hacia el territory ancla.
- Requiere exactamente 1 rival del gobernante, del mismo estado, en `in_command = yes`
- El jugador recluta una leva del rival en el territory destino (mecánica vanilla)
- 1 unidad "Exodos - Concentrate" (ES: "Exodos - Concentrar") → spawna automáticamente en la province del rival
- El jugador puede moverla antes de confirmar si quiere ajustar el destino
- Requiere área 100% propia al confirmar y durante la operación
- Piso fuentes: `total_population >= 2` — deja 1 pop mínimo en cada fuente; `count = 20` por fuente por pulso
- Cleanup cuando todas las fuentes llegan a `< 2 pops`
- Cancel disponible: `exodos_cancel` aparece si `gather_pending` o `gather_active` está activo

**TRANSFER** — mueve pops directamente entre 2 territories durante 10 pulsos.
- Sin condición de rival — operable en cualquier momento
- 2 unidades: "Exodos - Origin" (ES: "Exodos - Origen") y "Exodos - Destination" (ES: "Exodos - Destino") → spawnean en capital
- Territories pueden ser de áreas distintas — solo requiere `owner = ROOT`
- 10 pulsos × 10 pops/mes = hasta 100 pops en 10 meses
- Para: contador llega a 0 o ancla llega a `total_population < 2`
- Tiene decisión de cancel (sin reembolso)

**DISTRIBUTE** — dispersa pops desde el territory ancla hacia todas las provinces del área.
- Requiere exactamente 1 rival del gobernante, del mismo estado, en `in_command = yes`
- El jugador recluta una leva del rival en el territory a vaciar (mecánica vanilla)
- 1 unidad "Exodos - Distribute" (ES: "Exodos - Distribuir") → spawna automáticamente en la province del rival
- El jugador puede moverla antes de confirmar si quiere ajustar el origen
- Requiere área 100% propia al confirmar y durante la operación
- Piso ancla: `total_population >= 30` — garantiza reparto parejo; `count = 10` por destino por pulso
- Distribute no balancea el área: mueve cantidad fija desde el ancla, no iguala pops existentes
- Cleanup cuando el ancla llega a `< 30 pops`
- Cancel disponible: `exodos_cancel` aparece si `distribute_pending` o `distribute_active` está activo

### 4.4 Variables de estado

**País:**
| Variable | Uso |
|---|---|
| `exodos_transfer_pending` | Transfer activado, esperando confirmar |
| `exodos_gather_pending` | Gather activado, esperando confirmar |
| `exodos_distribute_pending` | Distribute activado, esperando confirmar |
| `exodos_operation_active` | Operación en ejecución |
| `exodos_gather_active` | Qué operación corre en el pulso |
| `exodos_transfer_active` | Ídem |
| `exodos_distribute_active` | Ídem |
| `exodos_anchor_province` | Province origen/ancla |
| `exodos_destination_province` | Province destino Transfer |
| `exodos_pulse_counter` | Contador descendente — solo Transfer (10 pulsos) |

**Province:**
| Variable | Uso |
|---|---|
| `exodos_is_anchor` | Ancla/origen — excluida de iteración |
| `exodos_is_destination` | Destino en Transfer |

**Unidad:**
| Variable | Uso |
|---|---|
| `exodos_unit_concentrate` | Unidad Gather |
| `exodos_unit_transfer_origin` | Unidad origen Transfer |
| `exodos_unit_transfer_dest` | Unidad destino Transfer |
| `exodos_unit_distribute` | Unidad Distribute |

### 4.5 Mecanismo de spawn alt — Gather y Distribute

El mecanismo de spawn de Gather y Distribute difiere del estable. En lugar de `location = capital_scope`,
el effect de activate navega al ejército del rival para capturar su province:

```pdxscript
# 1. Guardar el rival como scope desde character scope
every_character = {
    limit = { is_ruler = yes }
    every_rival = {
        limit = {
            employer = ROOT
            in_command = yes
        }
        save_scope_as = exodos_rival
    }
}
# 2. Navegar a su ejército y capturar la province
random_unit = {
    limit = { commander = scope:exodos_rival }
    unit_location = { save_scope_as = exodos_rival_loc }
}
# 3. Spawnear el marcador ahí
create_unit = {
    location = scope:exodos_rival_loc
    ...
}
```

**Por qué este camino:** `unit_commander` no existe en el engine (0 hits en game.zip).
`location = { }` desde character scope resuelve la capital de su gobernación, no la posición
del ejército. El único camino válido es country → `random_unit { limit = { commander = scope:X } }`
→ `unit_location`. Confirmado en vanilla: `roman_flavor.txt` y `power_base_character_events.txt`.

**Scopes `save_scope_as` no persisten entre ticks** — `exodos_rival` y `exodos_rival_loc` no
necesitan limpieza en `exodos_cleanup_effect`.

### 4.6 Código completo — exodos_decisions.txt

```pdxscript
country_decisions = {

    # ================================================================
    # TRANSFER — 2 fases, unidades selectoras
    # ================================================================

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
                name = "Exodos - Origin"
                location = capital_scope
                sub_unit = exodos_marker
                save_scope_as = exodos_origin_scope
            }
            scope:exodos_origin_scope = {
                set_variable = { name = exodos_unit_transfer_origin value = 1 }
            }
            create_unit = {
                name = "Exodos - Destination"
                location = capital_scope
                sub_unit = exodos_marker
                save_scope_as = exodos_dest_scope
            }
            scope:exodos_dest_scope = {
                set_variable = { name = exodos_unit_transfer_dest value = 1 }
            }
            set_variable = { name = exodos_transfer_pending value = 1 }
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
            custom_tooltip = exodos_tt_unit_stopped
            NOT = {
                any_unit = {
                    has_variable = exodos_unit_transfer_origin
                    is_moving = yes
                }
            }
            NOT = {
                any_unit = {
                    has_variable = exodos_unit_transfer_dest
                    is_moving = yes
                }
            }
            custom_tooltip = exodos_tt_owner
            any_unit = {
                has_variable = exodos_unit_transfer_origin
                unit_location = { owner = ROOT }
            }
            any_unit = {
                has_variable = exodos_unit_transfer_dest
                unit_location = { owner = ROOT }
            }
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
                    ROOT = {
                        set_variable = {
                            name = exodos_anchor_province
                            value = prev
                        }
                    }
                    set_variable = { name = exodos_is_anchor value = 1 }
                }
            }
            every_unit = {
                limit = { has_variable = exodos_unit_transfer_dest }
                unit_location = {
                    ROOT = {
                        set_variable = {
                            name = exodos_destination_province
                            value = prev
                        }
                    }
                    set_variable = { name = exodos_is_destination value = 1 }
                }
            }
            set_variable = { name = exodos_pulse_counter value = 10 }
            remove_variable = exodos_transfer_pending
            set_variable = { name = exodos_operation_active value = 1 }
            set_variable = { name = exodos_transfer_active value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    # ================================================================
    # GATHER — 2 fases, unidad spawneada en posicion del ejercito del rival
    # ================================================================

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
                any_rival = {
                    employer = ROOT
                    in_command = yes
                }
            }
            tyranny <= 90
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = {
                        employer = ROOT
                        in_command = yes
                    }
                    save_scope_as = exodos_rival
                }
            }
            random_unit = {
                limit = {
                    commander = scope:exodos_rival
                }
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

    exodos_confirm_gather = {
        potential = {
            is_ai = no
            has_variable = exodos_gather_pending
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            custom_tooltip = exodos_tt_unit_stopped
            NOT = {
                any_unit = {
                    has_variable = exodos_unit_concentrate
                    is_moving = yes
                }
            }
            any_unit = {
                has_variable = exodos_unit_concentrate
                unit_location = { owner = ROOT }
            }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_concentrate
                unit_location = {
                    area = {
                        NOT = {
                            any_area_province = {
                                NOT = { owner = ROOT }
                            }
                        }
                    }
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
                    ROOT = {
                        set_variable = {
                            name = exodos_anchor_province
                            value = prev
                        }
                    }
                    set_variable = { name = exodos_is_anchor value = 1 }
                }
            }
            remove_variable = exodos_gather_pending
            set_variable = { name = exodos_operation_active value = 1 }
            set_variable = { name = exodos_gather_active value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    # ================================================================
    # DISTRIBUTE — 2 fases, unidad spawneada en posicion del ejercito del rival
    # ================================================================

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
                any_rival = {
                    employer = ROOT
                    in_command = yes
                }
            }
            tyranny <= 90
        }
        effect = {
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = {
                        employer = ROOT
                        in_command = yes
                    }
                    save_scope_as = exodos_rival
                }
            }
            random_unit = {
                limit = {
                    commander = scope:exodos_rival
                }
                unit_location = { save_scope_as = exodos_rival_loc }
            }
            create_unit = {
                name = "Exodos - Distribute"
                location = scope:exodos_rival_loc
                sub_unit = exodos_marker
                save_scope_as = exodos_dist_scope
            }
            scope:exodos_dist_scope = {
                set_variable = { name = exodos_unit_distribute value = 1 }
            }
            set_variable = { name = exodos_distribute_pending value = 1 }
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
            custom_tooltip = exodos_tt_unit_stopped
            NOT = {
                any_unit = {
                    has_variable = exodos_unit_distribute
                    is_moving = yes
                }
            }
            any_unit = {
                has_variable = exodos_unit_distribute
                unit_location = { owner = ROOT }
            }
            custom_tooltip = exodos_tt_area_owner
            any_unit = {
                has_variable = exodos_unit_distribute
                unit_location = {
                    area = {
                        NOT = {
                            any_area_province = {
                                NOT = { owner = ROOT }
                            }
                        }
                    }
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
                    ROOT = {
                        set_variable = {
                            name = exodos_anchor_province
                            value = prev
                        }
                    }
                    set_variable = { name = exodos_is_anchor value = 1 }
                }
            }
            remove_variable = exodos_distribute_pending
            set_variable = { name = exodos_operation_active value = 1 }
            set_variable = { name = exodos_distribute_active value = 1 }
        }
        ai_will_do = { factor = 0 }
    }

    # ================================================================
    # CANCELAR — Transfer, Gather, Distribute (pending y active)
    # ================================================================

    exodos_cancel = {
        potential = {
            is_ai = no
            OR = {
                has_variable = exodos_transfer_pending
                has_variable = exodos_transfer_active
                has_variable = exodos_gather_pending
                has_variable = exodos_gather_active
                has_variable = exodos_distribute_pending
                has_variable = exodos_distribute_active
            }
        }
        highlight = { scope:province = { always = yes } }
        allow = { always = yes }
        effect = {
            exodos_cleanup_effect = yes
        }
        ai_will_do = { factor = 0 }
    }
}
```

### 4.7 Código completo — exodos_on_action.txt

```pdxscript
monthly_country_pulse = {
    effect = {
        if = {
            limit = {
                is_ai = no
                has_variable = exodos_operation_active
            }

            # ── 1. CHEQUEOS DE ERROR ──────────────────────────────────

            # Unidad destruida o desaparecida
            if = {
                limit = {
                    NOT = {
                        any_unit = {
                            OR = {
                                has_variable = exodos_unit_transfer_origin
                                has_variable = exodos_unit_transfer_dest
                                has_variable = exodos_unit_concentrate
                                has_variable = exodos_unit_distribute
                            }
                        }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            # Ancla perdida
            else_if = {
                limit = {
                    var:exodos_anchor_province = {
                        NOT = { owner = ROOT }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            # Destino perdido (solo Transfer)
            else_if = {
                limit = {
                    has_variable = exodos_transfer_active
                    var:exodos_destination_province = {
                        NOT = { owner = ROOT }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            # Area ya no es 100% propia (solo Gather)
            else_if = {
                limit = {
                    has_variable = exodos_gather_active
                    var:exodos_anchor_province = {
                        area = {
                            any_area_province = {
                                NOT = { owner = ROOT }
                            }
                        }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            # Area ya no es 100% propia (solo Distribute)
            else_if = {
                limit = {
                    has_variable = exodos_distribute_active
                    var:exodos_anchor_province = {
                        area = {
                            any_area_province = {
                                NOT = { owner = ROOT }
                            }
                        }
                    }
                }
                trigger_event = { id = exodos.1 }
            }

            else = {

                # ── 2. GATHER ─────────────────────────────────────────
                if = {
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
                                    random_pops_in_province = {
                                        move_pop = scope:exodos_dest
                                    }
                                }
                            }
                        }
                    }

                    # Cleanup cuando todas las fuentes llegaron a < 2 pops
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

                # ── 3. TRANSFER ───────────────────────────────────────
                else_if = {
                    limit = { has_variable = exodos_transfer_active }

                    var:exodos_destination_province = {
                        save_scope_as = exodos_dest
                    }
                    var:exodos_anchor_province = {
                        while = {
                            count = 10
                            limit = { total_population >= 2 }
                            random_pops_in_province = {
                                move_pop = scope:exodos_dest
                            }
                        }
                    }

                    # Contador — 10 pulsos
                    change_variable = { name = exodos_pulse_counter add = -1 }
                    if = {
                        limit = {
                            OR = {
                                var:exodos_pulse_counter <= 0
                                var:exodos_anchor_province = {
                                    total_population < 2
                                }
                            }
                        }
                        exodos_cleanup_effect = yes
                    }
                }

                # ── 4. DISTRIBUTE ─────────────────────────────────────
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
                                    limit = {
                                        scope:exodos_origin = {
                                            total_population >= 30
                                        }
                                    }
                                    scope:exodos_origin = {
                                        random_pops_in_province = {
                                            move_pop = scope:exodos_dist_target
                                        }
                                    }
                                }
                            }
                        }
                    }

                    # Cleanup cuando el ancla llega a < 30 pops
                    if = {
                        limit = {
                            var:exodos_anchor_province = {
                                total_population < 30
                            }
                        }
                        exodos_cleanup_effect = yes
                    }
                }
            }
        }
    }
}
```

### 4.8 Localización completa

#### exodos_l_spanish.yml
```yaml
l_spanish:
 # Fase 1 — Activate
 exodos_activate_transfer:0 "Exodos: Transferencia"
 exodos_activate_transfer_desc:0 "Por decreto del estado, el pueblo sera trasladado. Despliega las unidades Origen y Destino para marcar los territorios de origen y destino, luego confirma la operacion. Ambas unidades deben estar estacionarias y posicionadas en territorios bajo tu control. El costo se cobra al confirmar. (La operacion sera cancelada si una unidad es destruida o alguno de los territorios es perdido.)"
 exodos_activate_gather:0 "Exodos: Concentracion"
 exodos_activate_gather_desc:0 "Los dispersos seran reunidos. Recluta un ejercito o leva bajo el mando del rival del gobernante en el territorio donde quieras concentrar la poblacion — la unidad marcadora sera posicionada ahi automaticamente. Podes moverla antes de confirmar. El costo se cobra al confirmar. (La operacion sera cancelada si la unidad es destruida o cualquier territorio del area es perdido.)"
 exodos_activate_distribute:0 "Exodos: Distribucion"
 exodos_activate_distribute_desc:0 "Los hacinados seran dispersados por la tierra. Recluta un ejercito o leva bajo el mando del rival del gobernante en el territorio que quieras vaciar — la unidad marcadora sera posicionada ahi automaticamente. Podes moverla antes de confirmar. El costo se cobra al confirmar. (La operacion sera cancelada si la unidad es destruida o cualquier territorio del area es perdido.)"

 # Confirmar
 exodos_confirm_transfer:0 "Exodos: Confirmar Transferencia"
 exodos_confirm_transfer_desc:0 "La orden esta dada. El pueblo marchara durante diez meses. Costo: 2000 oro, 5000 soldados, 20 tirania. Ambas unidades deben estar estacionarias antes de que la operacion pueda comenzar."
 exodos_confirm_gather:0 "Exodos: Confirmar Concentracion"
 exodos_confirm_gather_desc:0 "Suena el llamado. Los dispersos convergaran. Costo: 1000 oro, 2500 soldados, 10 tirania. La unidad debe estar estacionaria y el area completa bajo tu control."
 exodos_confirm_distribute:0 "Exodos: Confirmar Distribucion"
 exodos_confirm_distribute_desc:0 "Se abren las puertas. El pueblo se extendera por la tierra. Costo: 1000 oro, 2500 soldados, 10 tirania. La unidad debe estar estacionaria y el area completa bajo tu control."

 # Cancelar — Transfer, Gather, Distribute
 exodos_cancel:0 "Cancelar el Exodo"
 exodos_cancel_desc:0 "El decreto es rescindido. La operacion termina aqui. Los costos ya pagados no seran reembolsados."

 # Evento de fallo
 exodos.1.t:0 "El Exodo Ha Fracasado"
 exodos.1.d:0 "El movimiento del pueblo ha llegado a un abrupto fin. Los esfuerzos del estado han sido en vano."
 exodos.1.ok:0 "Que asi sea."

 # Custom tooltips
 exodos_tt_unit_stopped:0 "Las unidades deben llegar a su destino antes de que la operacion pueda comenzar. (Unidad en movimiento)"
 exodos_tt_owner:0 "Ambos territorios deben estar bajo la autoridad del estado. (Territorio no controlado)"
 exodos_tt_area_owner:0 "El area completa debe estar bajo la autoridad del estado. (Area no controlada en su totalidad)"
 exodos_tt_rival_commander:0 "Se requiere exactamente un rival del gobernante del mismo estado, al mando de un ejercito o leva activa. Recluta primero una leva del rival en el territorio destino. (Condicion de rival no cumplida)"
```

#### exodos_l_english.yml
```yaml
l_english:
 # Fase 1 — Activate
 exodos_activate_transfer:0 "Exodos: Transfer"
 exodos_activate_transfer_desc:0 "By decree of the state, the people shall be moved. Deploy the Origin and Destination units to mark the source and destination territories, then confirm the operation. Both units must be stationary and positioned in territories under your control. Cost is paid upon confirmation. (Operation will be cancelled if a unit is destroyed or either territory is lost.)"
 exodos_activate_gather:0 "Exodos: Gather"
 exodos_activate_gather_desc:0 "The scattered shall be brought together. Raise an army or levy under the ruler's rival in the territory where you want to concentrate population — the marker unit will be placed there automatically. You may move it before confirming. Cost is paid upon confirmation. (Operation will be cancelled if the unit is destroyed or any territory in the area is lost.)"
 exodos_activate_distribute:0 "Exodos: Distribute"
 exodos_activate_distribute_desc:0 "The crowded shall be dispersed across the land. Raise an army or levy under the ruler's rival in the territory you want to empty — the marker unit will be placed there automatically. You may move it before confirming. Cost is paid upon confirmation. (Operation will be cancelled if the unit is destroyed or any territory in the area is lost.)"

 # Confirmar
 exodos_confirm_transfer:0 "Exodos: Confirm Transfer"
 exodos_confirm_transfer_desc:0 "The order is given. The people will march for ten months. Costs: 2000 gold, 5000 manpower, 20 tyranny. Both units must be stationary before the operation can begin."
 exodos_confirm_gather:0 "Exodos: Confirm Gather"
 exodos_confirm_gather_desc:0 "Sound the call. The scattered shall converge. Costs: 1000 gold, 2500 manpower, 10 tyranny. The unit must be stationary and the entire area must be under your control."
 exodos_confirm_distribute:0 "Exodos: Confirm Distribute"
 exodos_confirm_distribute_desc:0 "Open the gates. The people shall spread across the land. Costs: 1000 gold, 2500 manpower, 10 tyranny. The unit must be stationary and the entire area must be under your control."

 # Cancelar — Transfer, Gather, Distribute
 exodos_cancel:0 "Cancel the Exodos"
 exodos_cancel_desc:0 "The decree is rescinded. The operation ends here. Costs already paid will not be refunded."

 # Evento de fallo
 exodos.1.t:0 "The Exodos Has Failed"
 exodos.1.d:0 "The movement of the people has been brought to an abrupt end. The state's efforts have come to nothing."
 exodos.1.ok:0 "So be it."

 # Custom tooltips
 exodos_tt_unit_stopped:0 "The units must reach their destination before the operation can begin. (Unit still moving)"
 exodos_tt_owner:0 "Both territories must be under the authority of the state. (Territory not owned)"
 exodos_tt_area_owner:0 "The entire area must be under the authority of the state. (Area not fully controlled)"
 exodos_tt_rival_commander:0 "Exactly one rival of the ruler is required — of the same state, commanding an active army or levy. Raise a levy under the rival in the target territory first. (Rival condition not met)"
```

### 4.9 Archivos idénticos al estable

Los siguientes archivos son byte-a-byte idénticos a la distribución estable v1.3.5:

- `exodos/common/scripted_effects/exodos_scripted_effects.txt`
- `exodos/events/exodos_events.txt`
- `exodos/common/units/exodos_units.txt`

El `exodos/common/on_action/exodos_on_action.txt` difiere del estable únicamente en:
- Ausencia del chequeo `war = yes` en los guards de error
- `count = 20` en Gather (estable tiene `count = 10`)
- `total_population >= 30` / `< 30` en Distribute (estable tiene `>= 10` / `< 10`)

### 4.10 Estructura de archivos
```
mod/
├── exodos.mod                                               ← sin BOM
└── exodos/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/exodos_decisions.txt                       ← BOM UTF-8 (ALT)
    ├── events/exodos_events.txt                             ← BOM UTF-8
    ├── common/
    │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8 (ALT)
    │   ├── units/exodos_units.txt                           ← BOM UTF-8
    │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8
    └── localization/
        ├── english/exodos_l_english.yml                     ← BOM UTF-8 (ALT)
        └── spanish/exodos_l_spanish.yml                     ← BOM UTF-8 (ALT)
```

---

## 5. BY OTHER MEANS (v3.0)

### 5.1 Descripción

`by_other_means/` es el mod de control de personajes. Incluye:
- Eliminar Rivales, Bacanal, Ego Sum
- `bom_kill_ruler` (movido desde TLV en v1.2)
- Iron Hand: `iha_seize_holdings` e `iha_fill_the_void`

### 5.2 Terminología engine

| Diseño | Engine |
|---|---|
| "rivales del gobernante" | `every_character = { limit = { is_ruler = yes } every_rival = { } }` desde country scope |
| "gobernante tiene rivales" | `any_character = { is_ruler = yes num_of_rivals >= 1 }` desde country scope |
| "gobernante" | `every_character = { limit = { is_ruler = yes } }` desde country scope |
| "rival del mismo país" | `any_rival = { employer = ROOT }` desde character scope del gobernante |
| "propiedades del rival" | `every_holdings = { }` desde character scope del rival |

### 5.3 Arquitectura — bom_confirm

**Costos:** 2000 oro | manpower -1 (500 pantalla) | +40 tyranny | cap ≤80 | rivals ≥ 1

### 5.4 Arquitectura — bom_bacanal

**Costos:** 500 oro | +10 tyranny | cap ≤90 | rivals ≥ 1

### 5.5 Arquitectura — bom_kill_ruler

**Costos:** 2000 oro | manpower -1 (500 pantalla) | +40 tyranny | cap ≤60 | stability ≥ 50

### 5.6 Arquitectura — iha_seize_holdings

- Patrón validado: `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = iha_holding } remove_holding = scope:iha_holding }` — `remove_holding` va dentro del `while` pero fuera del bloque `random_holdings`
- Aplica `family_property_seized_l` al rival (-40 loyalty por 20 años)

**Costos:** 2000 oro | +40 tyranny | cap ≤60 | rivals=1 exacto, employer=ROOT

### 5.7 Arquitectura — iha_fill_the_void

- Transfiere todas las propiedades sin dueño al rival seleccionado
- Usa `save_scope_as = iha_rival_scope` para capturar al rival, luego `scope:iha_rival_scope = { add_holding = PREV }` desde province scope

**Costos:** 2000 oro | +40 tyranny | cap ≤60 | rivals=1 exacto, employer=ROOT

### 5.8 Código completo

#### bom_decisions.txt
*(idéntico al estable — ver zip)*

#### bom_l_english.yml
```yaml
l_english:
 bom_confirm:0 "By Other Means: Eliminate Rivals"
 bom_confirm_desc:0 "The state has enemies that cannot be defeated in open battle. Authorize the elimination of all rivals of the ruler. Cost: 2000 gold, 500 manpower, 40 tyranny. This cannot be undone."
 bom_bacanal:0 "Bacchanalia"
 bom_bacanal_desc:0 "The power extends an invitation — wine, excess, ruin. Those who stand against us will not fall in battle. They will fall in their own chambers, by their own appetites. Cost: 500 gold, 10 tyranny."
 bom_kill_ruler:0 "Et tu, Brute?"
 bom_kill_ruler_desc:0 "The ruler must fall. Authorize their elimination and clear the path. Cost: 2000 gold, 500 manpower, 40 tyranny."
 iha_seize_holdings:0 "Iron Hand: Seize Properties"
 iha_seize_holdings_desc:0 "The sword is not always necessary. Strip the rival of the ruler of everything they hold. Land is power — take it. Cost: 2000 gold, 40 tyranny."
 iha_fill_the_void:0 "Iron Hand: Fill the Void"
 iha_fill_the_void_desc:0 "While a rival threatens, the land cannot sit unclaimed. Grant every holding without an owner to the selected rival, enriching them beyond their ambitions. Cost: 2000 gold, 40 tyranny."
```

#### bom_l_spanish.yml
```yaml
l_spanish:
 bom_confirm:0 "By Other Means: Eliminar Rivales"
 bom_confirm_desc:0 "El estado tiene enemigos que no pueden ser derrotados en batalla abierta. Autoriza la eliminacion de todos los rivales del gobernante. Costo: 2000 oro, 500 soldados, 40 tirania. Esto no puede deshacerse."
 bom_bacanal:0 "Bacanal"
 bom_bacanal_desc:0 "El poder extiende una invitacion — vino, exceso, ruina. Quienes se nos oponen no caeran en batalla. Caeran en sus propias camaras, por sus propios apetitos. Costo: 500 oro, 10 tirania."
 bom_kill_ruler:0 "Et tu, Brute?"
 bom_kill_ruler_desc:0 "El gobernante debe caer. Autoriza su eliminacion y despeja el camino. Costo: 2000 oro, 500 soldados, 40 tirania."
 iha_seize_holdings:0 "Iron Hand: Confiscar Propiedades"
 iha_seize_holdings_desc:0 "La espada no siempre es necesaria. Despoja al rival del gobernante de todo lo que posee. La tierra es poder — Tomala. Costo: 2000 oro, 40 tirania."
 iha_fill_the_void:0 "Iron Hand: Llenar el Vacio"
 iha_fill_the_void_desc:0 "Mientras un rival amenaza, la tierra no puede quedarse sin dueno. Otorga todas las propiedades sin dueno al rival seleccionado, enriqueciendolo mas alla de sus ambiciones. Costo: 2000 oro, 40 tirania."
```

*(bom_decisions_ego_sum.txt, bom_l_english_ego_sum.yml, bom_l_spanish_ego_sum.yml — sin cambios)*

#### by_other_means.mod
```
name = "By Other Means"
version = "3.0"
supported_version = "2.0.*"
path = "mod/by_other_means"
```

### 5.9 Estructura de archivos
```
mod/
├── by_other_means.mod                                       ← sin BOM
└── by_other_means/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/
    │   ├── bom_decisions.txt                                ← BOM UTF-8
    │   └── bom_decisions_ego_sum.txt                        ← BOM UTF-8
    ├── events/bom_events.txt                                ← BOM UTF-8
    └── localization/
        ├── english/
        │   ├── bom_l_english.yml                            ← BOM UTF-8
        │   └── bom_l_english_ego_sum.yml                    ← BOM UTF-8
        └── spanish/
            ├── bom_l_spanish.yml                            ← BOM UTF-8
            └── bom_l_spanish_ego_sum.yml                    ← BOM UTF-8
```

---

## 6. BY OTHER MEANS — EGO SUM

### 6.1 Decisiones

| ID | Nombre | Stat | +Total | Variable one-shot |
|---|---|---|---|---|
| bom_ego_sum_mars | Filius Martis — Path of War | martial | +10 | bom_ego_sum_mars_used |
| bom_ego_sum_iovis | Filius Iovis — Path of Piety | zeal | +10 | bom_ego_sum_iovis_used |
| bom_ego_sum_mercurii | Filius Mercurii — Path of Oratory | charisma | +10 | bom_ego_sum_mercurii_used |
| bom_ego_sum_minervae | Filius Minervae — Path of Wisdom | finesse | +10 | bom_ego_sum_minervae_used |

### 6.2 Código completo

*(idéntico al estable — ver zip)*

---

## 7. THE LAST VOTE (v1.7)

### 7.1 Descripción

Una sola decisión: `tlv_confirm`. Disuelve la república en dictadura.

### 7.2 Arquitectura — tlv_confirm

| Condición | Valor |
|---|---|
| `is_republic` | yes |
| `tyranny` | <= 60 |
| `stability` | >= 50 |
| `treasury` | >= 2000 |
| `popularity` del gobernante | >= 50 |

Costos: +40 tyranny, -50 stability, -2000 oro.
Orden obligatorio: `clearup` → `law_variable` → `change_government` → `law_change`.

### 7.3 Código completo

*(idéntico al estable — ver zip)*

#### the_last_vote.mod
```
name = "The Last Vote"
version = "1.7"
supported_version = "2.0.*"
path = "mod/the_last_vote"
```

### 7.4 Estructura de archivos
```
mod/
├── the_last_vote.mod                                        ← sin BOM
└── the_last_vote/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/tlv_decisions.txt                          ← BOM UTF-8
    ├── events/tlv_events.txt                                ← BOM UTF-8
    └── localization/
        ├── english/tlv_l_english.yml                        ← BOM UTF-8
        └── spanish/tlv_l_spanish.yml                        ← BOM UTF-8
```

---

## 8. THE GREAT LEAP (v1.5)

### 8.1 Parámetros

| Parámetro | Valor |
|---|---|
| Innovations otorgadas | 320 (árbol completo) |
| Costo oro | 516 oro/metrópolis + 258 oro/ciudad |
| Costo tyranny | 100 fijo |
| Tyranny cap | `tyranny <= 0` |
| Piso treasury | `>= 258` |
| One-shot | `tgl_purchased` bloquea reuso |

### 8.2 Código completo

*(idéntico al estable — ver zip)*

#### the_great_leap.mod
```
name = "The Great Leap"
version = "1.5"
supported_version = "2.0.*"
path = "mod/the_great_leap"
```

### 8.3 Estructura de archivos
```
mod/
├── the_great_leap.mod                                       ← sin BOM
└── the_great_leap/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/tgl_decisions.txt                          ← BOM UTF-8
    └── localization/
        ├── english/tgl_l_english.yml                        ← BOM UTF-8
        └── spanish/tgl_l_spanish.yml                        ← BOM UTF-8
```

---

## 9. ESTRUCTURA COMPLETA DEL ECOSISTEMA

```
mod/
├── build_mods_alt.py                                        ← script de generación manual (opcional)
├── exodos.mod                                               ← sin BOM
├── by_other_means.mod                                       ← sin BOM
├── the_last_vote.mod                                        ← sin BOM
├── the_great_leap.mod                                       ← sin BOM
│
├── exodos/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/exodos_decisions.txt                       ← BOM UTF-8 (ALT)
│   ├── events/exodos_events.txt                             ← BOM UTF-8
│   ├── common/
│   │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8 (ALT)
│   │   ├── units/exodos_units.txt                           ← BOM UTF-8
│   │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8
│   └── localization/
│       ├── english/exodos_l_english.yml                     ← BOM UTF-8 (ALT)
│       └── spanish/exodos_l_spanish.yml                     ← BOM UTF-8 (ALT)
│
├── by_other_means/   (idéntico al estable)
├── the_last_vote/    (idéntico al estable)
└── the_great_leap/   (idéntico al estable)
```

Total archivos en mod_alt.zip: 29 (sin build_mods_alt.py).

---

## 10. INSTALACIÓN

Extraer el contenido de `mod_alt.zip` en:
```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\
```

Extracción limpia — reemplaza todo lo que hubiera. El archivo `dlc_load.json`:
```json
{
    "enabled_mods": [
        "mod/exodos.mod",
        "mod/by_other_means.mod",
        "mod/the_last_vote.mod",
        "mod/the_great_leap.mod"
    ],
    "disabled_dlcs": []
}
```

---

## 11. PENDIENTES

| Tarea | Mod | Prioridad |
|---|---|---|
| Evaluar contador de pulsos como límite secundario para Gather y Distribute | Exodus ALT | MEDIA |
| Publicar en Steam Workshop | Todos | BAJA |

---

## 12. HISTORIAL

### v1.3-alt — 2026-05
- **EXODUS ALT** — `is_ai = no` agregado en `allow` de `exodos_activate_transfer` (FIX-08)
- **EXODUS ALT** — Gather `count = 10` → `count = 20` en `exodos_on_action.txt` (FIX-06; archivo target corregido: es `on_action`, no `scripted_effects`)
- **EXODUS ALT** — Distribute `total_population >= 10` / `< 10` → `>= 30` / `< 30` en `exodos_on_action.txt` (FIX-07; mismo archivo target corregido)
- **EXODUS ALT** — Nombres de unidades corregidos a español en `exodos_decisions.txt` (FIX-02 expandido)
- **BOM** — `iha_fill_the_void_desc` EN: agregado "to the selected rival" (FIX-03)
- **BOM** — `iha_fill_the_void_desc` ES: "holdings" → "propiedades", agregado "seleccionado" (FIX-03)
- **BOM** — `iha_seize_holdings_desc` ES: "tomarla." → "Tomala." (FIX-04)
- **TGL** — `supported_version = "1.5"` → `"2.0.*"` (FIX-05)
- **Doc** — Documento reescrito como autónomo completo — elimina todas las referencias "ver backup estable sección X"
- **Doc** — Sección 1.9: convención de idioma de UI agregada
- **Doc** — Sección 1.10: tabla de nombres de unidades agregada
- **Doc** — Sección 2.6: patrón `remove_holding` corregido — va dentro del `while` pero fuera de `random_holdings`
- **Doc** — Sección 4.2: cleanup condicional documentado; piso Distribute actualizado a 30; mejora futura documentada
- **Doc** — Sección 4.9: diferencias con estable documentadas explícitamente
- **Doc** — Flujo de trabajo con IA documentado; rol de `build_mods_alt.py` aclarado
- **Doc** — Sección "Estado actual" agregada
- **Doc** — Fixes pendientes incorporados en sección PENDIENTES
- **Versión** — Exodos 1.20 ALT → 1.21 ALT

### v1.2-alt — 2026-05
- **EXODUS ALT** — `exodos_tt_no_war` eliminado de localización ES y EN
- **Versión** — Exodos 1.19 ALT → 1.20 ALT

### v1.1-alt — 2026-05
- **EXODUS ALT** — `war = yes` eliminado del guard en `monthly_country_pulse`
- **Versión** — Exodos 1.18 ALT → 1.19 ALT

### v1.0-alt — 2026-05
- **EXODUS ALT** — distribución alt creada: spawn por posición del rival, `war = no` eliminado

---

*Drago Mod Pack — Backup Técnico Distribución Alternativa v1.3-alt — mod en mod_alt.zip*
