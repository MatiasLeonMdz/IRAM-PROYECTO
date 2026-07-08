# DRAGO MOD PACK — IMPERATOR ROME
## Backup Técnico Unificado
### Engine: Imperator Roma 2.0.4 | Ironman compatible ✓ | mod.zip | v1.3.5

---

## INSTRUCCIONES PARA LA IA QUE LEA ESTE DOCUMENTO

Este documento es el backup técnico completo del ecosistema de mods Drago Mod Pack para Imperator: Roma. Reemplaza todos los backups individuales anteriores — es la única fuente de verdad para la distribución estable.

Antes de trabajar en cualquier mod:
1. Leer este documento completo de principio a fin.
2. Leer también el zip `mod.zip` para verificar el estado real de los archivos fuente.
3. No asumir valores del engine de memoria — verificar contra los archivos fuente o las secciones de código de este documento.
4. Las decisiones marcadas como CERRADO no se reabren salvo pedido explícito del usuario.
5. El modelo económico de TGL está CERRADO en su totalidad. No recalcular salvo pedido explícito.

### Flujo de trabajo con la IA

El flujo normal es:
1. El usuario sube los backups (estable y alt) y los zips actuales al inicio de la sesión.
2. La IA lee todo, se pone al día, y trabaja sobre los archivos fuente.
3. La IA entrega los archivos corregidos individualmente y el zip final listo para instalar.
4. El usuario extrae el zip en la carpeta mod, reemplazando todo — instalación limpia.

`build_mods.py` es una herramienta alternativa para el caso en que el usuario edite archivos fuente por su cuenta y necesite regenerar y validar el zip manualmente. Uso: `python build_mods.py` desde la carpeta raíz del mod. Valida BOM en todos los archivos antes de empaquetar y aborta si hay errores. En el flujo normal con IA no se usa.

---

## ESTADO ACTUAL

| Item | Valor |
|---|---|
| Versión | v1.3.5 |
| Fecha último build | 2026-05 |
| Exodos | 1.18 |
| By Other Means | 3.0 |
| The Last Vote | 1.7 |
| The Great Leap | 1.5 |
| Fixes pendientes | Ninguno |

---

## 1. ECOSISTEMA

### 1.1 Tabla de mods

| Mod | Función | Prefijo | Versión .mod | Validado en juego |
|---|---|---|---|---|
| Exodus | Movimiento de población entre territories y áreas | `exodos_` | 1.18 | 2026-04 |
| By Other Means | Elimina/gestiona rivales y gobernante; holdings | `bom_` / `iha_` | 3.0 | — |
| By Other Means — Ego Sum | Maximiza stats del gobernante (módulo de BOM) | `bom_` | — (módulo) | 2026-04 |
| By Other Means — Bacanal | Corrompe rivales del gobernante (módulo de BOM) | `bom_` | — (módulo) | 2026-04 |
| The Last Vote | Disuelve república → dictadura | `tlv_` | 1.7 | — |
| The Great Leap | Compra árbol completo de innovations (one-shot) | `tgl_` | 1.5 | 2026-04 |

Todos los mods se distribuyen en un único zip: `mod.zip`.
El script de generación manual es `build_mods.py` — ver sección de flujo de trabajo.

### 1.2 Reorganización v1.2

En v1.2, `by_other_means/` absorbe las funciones que antes estaban en `the_last_vote/` (tlv_kill_ruler → bom_kill_ruler) y agrega las dos funciones Iron Hand (iha_). `the_last_vote/` queda solo con `tlv_confirm`.

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
1. EXODUS        → Consolidar población en territories clave antes de la campaña política
2. BOM           → Eliminar rivales del gobernante que podrían bloquear la consolidación
3. BOM BACANAL   → Corromper rivales en lugar de eliminarlos (alternativa a BOM)
4. IHA SEIZE     → Confiscar propiedades del rival único restante (antes o en lugar de matarlo)
5. IHA FILL VOID → Otorgar todas las propiedades sin dueño al rival (enriquecerlo antes o en lugar de matarlo)
6. BOM EGO SUM   → Maximizar los stats del gobernante para el rol que va a cumplir
7. BOM KILL      → Eliminar al gobernante actual si obstaculiza el golpe (Et tu, Brute?)
8. TLV CONFIRM   → Disolver la república cuando las condiciones son óptimas
9. TGL           → Comprar el árbol de innovations una vez consolidado el poder
10. VANILLA      → anoint_heir para nominar sucesor con dictadura activa
```

Cada mod es independiente — el flujo es una sugerencia, no una dependencia técnica.

### 1.4 Tabla de costos y condiciones — ecosistema completo

| Mod | Función | Oro | Manpower (script) | Manpower (pantalla) | Tyranny + | Tyranny cap | Condiciones extra |
|---|---|---|---|---|---|---|---|
| Exodus | Gather | 1000 | 5 | 2500 | +10 | ≤90 | war=no, área propia |
| Exodus | Distribute | 1000 | 5 | 2500 | +10 | ≤90 | war=no, área propia |
| Exodus | Transfer | 2000 | 10 | 5000 | +20 | ≤80 | war=no, territories owner=ROOT |
| BOM | Eliminar | 2000 | 1 | 500 | +40 | ≤80 | rivals ≥ 1 |
| BOM | Bacanal | 500 | — | — | +10 | ≤90 | rivals ≥ 1 |
| BOM | Ego Sum | — | — | — | — | — | one-shot por path |
| BOM | Kill Ruler | 2000 | 1 | 500 | +40 | ≤60 | stability ≥ 50 |
| IHA | Confiscar | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, mismo país |
| IHA | Fill the Void | 2000 | — | — | +40 | ≤60 | rivals=1 exacto, mismo país |
| TLV | Confirm | 2000 | — | — | +40 | ≤60 | is_republic, stability ≥ 50, popularity ≥ 50 |
| TGL | Purchase | dinámico | — | — | +100 | ≤0 | one-shot |

### 1.5 Scopes por función

| Mod | Función | Scopes |
|---|---|---|
| Exodus | Gather / Distribute / Transfer | country → unit → province → pop |
| BOM | Eliminar / Bacanal | country → character → character (rival) |
| BOM | Ego Sum | country → character |
| BOM | Kill Ruler | country → character |
| IHA | Confiscar | country → character → character (rival) → province (holding) |
| IHA | Fill the Void | country → character (rival) → province |
| TLV | Confirm | country → character (solo en allow) |
| TGL | Purchase | country → province → country |

### 1.6 Advertencias de flujo

**IHA y la condición rivals=1:** IHA Confiscar e IHA Fill the Void requieren exactamente 1 rival en total, y ese rival debe ser del mismo país que root. Usar BOM Eliminar primero puede dejar al jugador con 1 rival si había 2, habilitando IHA. El orden típico es: BOM Eliminar (hasta quedar con 1 rival) → IHA Confiscar → IHA Fill the Void.

**IHA Confiscar no mata:** el rival sobrevive con loyalty penalizada por `family_property_seized_l` (-40 por 20 años). Puede seguirse con BOM Eliminar o dejarlo vivo arruinado.

**IHA Fill the Void otorga propiedades al rival seleccionado:** en lugar de quitarle propiedades al rival, le otorga todas las propiedades vacías del país. Útil para enriquecer al rival antes de eliminarlo, o como alternativa política a la confiscación.

**BOM Kill Ruler disponible en cualquier tipo de gobierno:** no requiere república. Útil antes de TLV Confirm si el gobernante actual no cumple `popularity >= 50`.

**BOM (Eliminar Rivales) disponible en guerra:** sin restricción `war = no`.

**TLV confirm es irreversible:** disolver la república no tiene marcha atrás.

**Ego Sum y Bacanal son one-shot por partida:** una vez usadas no se pueden repetir aunque el gobernante muera.

**Popup de BOM eliminado en v1.2:** `bom.2` (popup "El Trabajo Está Hecho") fue eliminado. Todos los mods del ecosistema son ahora silenciosos excepto TLV Confirm (que mantiene `tlv.2`) y Exodus (error `exodos.1`).

### 1.7 Compatibilidad con saves existentes

| Mod | Sobre partida existente | Notas |
|---|---|---|
| Exodus | ⚠️ No verificado | Usa unidades marcadoras y variables de estado — riesgo de estado inválido |
| By Other Means | ✓ Compatible | Sin variables persistentes ni unidades |
| BOM — Ego Sum | ✓ Compatible | Variables one-shot se crean al usar la decisión |
| BOM — Bacanal | ✓ Compatible | Sin variables de estado |
| BOM — Kill Ruler | ✓ Compatible | Stateless |
| IHA — Confiscar | ✓ Compatible | Stateless |
| IHA — Fill the Void | ✓ Compatible | Stateless |
| The Last Vote | ⚠️ No verificado | Modifica variables internas del engine al cambiar gobierno |
| The Great Leap | ✓ Compatible | Variable one-shot `tgl_purchased` se crea al usar la decisión |

**Recomendación general:** activar todos los mods antes de iniciar una partida nueva. No agregar ni quitar mods sobre partidas en curso.

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
| Zip unificado | `mod.zip` entregado por la IA | Un solo archivo de distribución, BOM validado |
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

Conocimiento confirmado en juego que aplica a más de un mod. Verificar esta tabla antes de escribir cualquier script nuevo.

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

### 2.2 Variables y flags

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| `set_country_flag` / `has_country_flag` / `clr_country_flag` | `set_variable` / `has_variable` / `remove_variable` | Exodus bug 4 |
| `set_province_flag` / `has_province_flag` / `remove_province_flag` | `set_variable` / `has_variable` / `remove_variable` en scope province | Exodus bug 4 |
| `set_unit_flag` / `has_unit_flag` | `set_variable` / `has_variable` en scope unit | Exodus bug 4 |
| `check_variable = { ... }` como trigger | `var:nombre >= valor` directo | Exodus bug 4 |
| `var:X >= var:Y` (dos variables en trigger) | Contador descendente, comparar contra 0 | Exodus bug 3 |

### 2.3 Localización

| Problema | Solución correcta | Confirmado en |
|---|---|---|
| Corchetes `[ ]` en texto libre de yml | Usar paréntesis `( )` — el engine parsea `[ ]` como variables dinámicas y falla con `Data error in loc key` | TGL v1.3, Exodus bug 24 — 269+269 hits en error.log |
| BOM UTF-8 ausente en .txt o .yml del mod | Agregar BOM `EF BB BF` — usar `build_mods.py` o Python `utf-8-sig`, nunca editar a mano | Todos los mods |
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
| Remover holding en loop | Patrón correcto y validado en engine: `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = x } remove_holding = scope:x }` — `remove_holding` va dentro del `while` pero **fuera** del bloque `random_holdings`. Dentro de `random_holdings` el scope es province y el engine falla. | IHA Seize — confirmado en engine 2026-05 |
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
| `Corrupt Decision Table Entry - '\xEF\xBB\xBFcountry_decisions'` | BOM pegado al token — archivo editado a mano | Regenerar con `build_mods.py` |
| `Creation of dynamic token "\xEF\xBB\xBF..."` | BOM en scripted_effects — archivo editado a mano | Regenerar con `build_mods.py` |
| `Unknown effect/trigger` en decisión | Sintaxis no existe en el engine | Ver sección 2.4 |
| `could not find unit type exodos_marker` | Archivo `exodos_units.txt` sin BOM o no encontrado | Verificar BOM y ruta del archivo |

### 3.2 Cómo verificar que el ecosistema está limpio

Después de cargar una partida con los mods activos, buscar en error.log las siguientes cadenas. Si no aparecen, el ecosistema está funcionando correctamente:

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

Un error.log limpio para el ecosistema no tiene hits en ninguna de estas búsquedas. Cualquier hit indica un problema en el archivo correspondiente.

### 3.3 Errores que NO son del ecosistema

Imperator genera errores de vanilla en el error.log que no son del mod. Ignorar entradas que referencien rutas del juego base (`Imperator/game/`) en lugar del mod (`mod/by_other_means/`, `mod/exodos/`, etc.).

### 3.4 Errores de vanilla documentados — ignorar siempre

| Mensaje | Hits aprox. | Causa | Acción |
|---|---|---|---|
| `has_province_modifier` Wrong scope | ~118 | Game files de vanilla usan `has_province_modifier` en character scope | Ignorar — vanilla puro |
| `Missing Icon for Modifier: exodos_marker_*` | 19 | Unit type sin íconos GFX | **Permanente e ignorable** — los `.dds` se intentaron agregar en v1.3 pero el engine no los cargó; eliminados en v1.3.4. Los warnings no afectan ninguna mecánica |

---

## 4. EXODUS — POPULATION MANAGEMENT

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

**Flujo:**
```
FASE 1 — ACTIVAR:   spawna unidad(es) en capital → set _pending (sin cobro)
FASE 2 — CONFIRMAR: cobra costos → guarda unit_location como var país → set operation_active
FASE 3 — PULSO:     monthly_country_pulse → verifica estado → ejecuta → cleanup condicional
```

**Costos:**

| Operación | Oro | Manpower (script) | Manpower (pantalla) | Tyranny | Tyranny cap | Pulsos |
|---|---|---|---|---|---|---|
| Gather | 1000 | 5 | 2500 | +10 | 90 | ≥1 (hasta fuentes < 2 pops) |
| Distribute | 1000 | 5 | 2500 | +10 | 90 | ≥1 (hasta ancla < 10 pops) |
| Transfer | 2000 | 10 | 5000 | +20 | 80 | 10 fijos |

> El engine multiplica el manpower por ×500 al mostrarlo en pantalla. Valor en script = valor pantalla / 500.

> Transfer requiere `war = no` en confirm (agregado en v1.2). Gather y Distribute ya lo tenían desde v1.1.

**Cleanup condicional — Gather y Distribute:**
El cleanup no es incondicional al terminar el bloque. Gather limpia cuando todas las fuentes del área llegan a `total_population < 2`. Distribute limpia cuando el ancla llega a `total_population < 10`. En áreas muy pobladas la operación puede extenderse más de un pulso. Este comportamiento es intencional — los pisos son la condición de fin natural de la operación.

**Mejora futura pendiente:** evaluar agregar un contador de pulsos como límite de seguridad secundario para Gather y Distribute, similar al `exodos_pulse_counter` de Transfer, para garantizar cleanup en un máximo de N pulsos independientemente del estado de la población.

### 4.3 Operaciones

**GATHER** — concentra pops de toda el área hacia el territory ancla.
- 1 unidad "Exodos - Concentrate" (ES: "Exodos - Concentrar") → jugador la posiciona en el territory destino
- Requiere área 100% propia al confirmar y durante la operación
- Piso fuentes: `total_population >= 2` — deja 1 pop mínimo en cada fuente
- Cleanup cuando todas las fuentes llegan a `< 2 pops`
- Cancel disponible: `exodos_cancel` aparece si `gather_pending` o `gather_active` está activo

**TRANSFER** — mueve pops directamente entre 2 territories durante 10 pulsos.
- 2 unidades: "Exodos - Origin" (ES: "Exodos - Origen") y "Exodos - Destination" (ES: "Exodos - Destino")
- Territories pueden ser de áreas distintas — solo requiere `owner = ROOT`
- 10 pulsos × 10 pops/mes = hasta 100 pops en 10 meses
- Para: contador llega a 0 o ancla llega a `total_population < 2`
- Tiene decisión de cancel (sin reembolso)

**DISTRIBUTE** — dispersa pops desde el territory ancla hacia todas las provinces del área.
- 1 unidad "Exodos - Distribute" (ES: "Exodos - Distribuir") → jugador la posiciona en la province a vaciar
- Requiere área 100% propia al confirmar y durante la operación
- Piso ancla: `total_population >= 10` — garantiza reparto parejo
- Distribute no balancea el área: mueve cantidad fija desde el ancla, no iguala pops existentes
- Cleanup cuando el ancla llega a `< 10 pops`
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

### 4.5 Código completo

#### exodos_decisions.txt
```pdxscript
country_decisions = {

    # ================================================================
    # FASE 1 — ACTIVAR (sin cobro)
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
            custom_tooltip = exodos_tt_no_war
            war = no
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
                name = "Exodos - Concentrate"
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

    exodos_activate_distribute = {
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
                name = "Exodos - Distribute"
                location = capital_scope
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

    # ================================================================
    # FASE 2 — CONFIRMAR (cobra costos)
    # ================================================================

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
            war = no
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
            custom_tooltip = exodos_tt_no_war
            war = no
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
            war = no
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
    # CANCELAR — Transfer, Gather, Distribute
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

#### exodos_on_action.txt
*(sin cambios respecto a v1.3.4 — ver zip)*

#### exodos_scripted_effects.txt
*(sin cambios respecto a v1.3.4 — ver zip)*

#### exodos_units.txt
*(sin cambios respecto a v1.3.4 — ver zip)*

#### exodos_events.txt
*(sin cambios respecto a v1.3.4 — ver zip)*

#### exodos_l_english.yml
```yaml
l_english:
 # Fase 1 — Activate
 exodos_activate_transfer:0 "Exodos: Transfer"
 exodos_activate_transfer_desc:0 "By decree of the state, the people shall be moved. Deploy the Origin and Destination units to mark the source and destination territories, then confirm the operation. Both units must be stationary and positioned in territories under your control. Cost is paid upon confirmation. (Operation will be cancelled if war is declared, a unit is destroyed, or either territory is lost.)"
 exodos_activate_gather:0 "Exodos: Gather"
 exodos_activate_gather_desc:0 "The scattered shall be brought together. Deploy the Concentrate unit to mark the destination territory, then confirm the operation. The entire area must be under your control. Cost is paid upon confirmation. (Operation will be cancelled if war is declared, the unit is destroyed, or any territory in the area is lost.)"
 exodos_activate_distribute:0 "Exodos: Distribute"
 exodos_activate_distribute_desc:0 "The crowded shall be dispersed across the land. Deploy the Distribute unit to mark the source territory, then confirm the operation. The entire area must be under your control. Cost is paid upon confirmation. (Operation will be cancelled if war is declared, the unit is destroyed, or any territory in the area is lost.)"

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
 exodos_tt_no_war:0 "The state cannot move its people while war rages on. (At war)"
 exodos_tt_unit_stopped:0 "The units must reach their destination before the operation can begin. (Unit still moving)"
 exodos_tt_owner:0 "Both territories must be under the authority of the state. (Territory not owned)"
 exodos_tt_area_owner:0 "The entire area must be under the authority of the state. (Area not fully controlled)"
```

#### exodos_l_spanish.yml
```yaml
l_spanish:
 # Fase 1 — Activate
 exodos_activate_transfer:0 "Exodos: Transferencia"
 exodos_activate_transfer_desc:0 "Por decreto del estado, el pueblo sera trasladado. Despliega las unidades Origen y Destino para marcar los territorios de origen y destino, luego confirma la operacion. Ambas unidades deben estar estacionarias y posicionadas en territorios bajo tu control. El costo se cobra al confirmar. (La operacion sera cancelada si se declara la guerra, una unidad es destruida, o alguno de los territorios es perdido.)"
 exodos_activate_gather:0 "Exodos: Concentracion"
 exodos_activate_gather_desc:0 "Los dispersos seran reunidos. Despliega la unidad Concentrar para marcar el territorio de destino, luego confirma la operacion. El area completa debe estar bajo tu control. El costo se cobra al confirmar. (La operacion sera cancelada si se declara la guerra, la unidad es destruida, o cualquier territorio del area es perdido.)"
 exodos_activate_distribute:0 "Exodos: Distribucion"
 exodos_activate_distribute_desc:0 "Los hacinados seran dispersados por la tierra. Despliega la unidad Distribuir para marcar el territorio de origen, luego confirma la operacion. El area completa debe estar bajo tu control. El costo se cobra al confirmar. (La operacion sera cancelada si se declara la guerra, la unidad es destruida, o cualquier territorio del area es perdido.)"

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
 exodos_tt_no_war:0 "El estado no puede mover a su pueblo mientras la guerra arrasa. (En guerra)"
 exodos_tt_unit_stopped:0 "Las unidades deben llegar a su destino antes de que la operacion pueda comenzar. (Unidad en movimiento)"
 exodos_tt_owner:0 "Ambos territorios deben estar bajo la autoridad del estado. (Territorio no controlado)"
 exodos_tt_area_owner:0 "El area completa debe estar bajo la autoridad del estado. (Area no controlada en su totalidad)"
```

### 4.6 Estructura de archivos
```
mod/
├── exodos.mod                                               ← sin BOM
└── exodos/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/exodos_decisions.txt                       ← BOM UTF-8
    ├── events/exodos_events.txt                             ← BOM UTF-8
    ├── common/
    │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8, raíz directa
    │   ├── units/exodos_units.txt                           ← BOM UTF-8
    │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8, raíz directa
    └── localization/
        ├── english/exodos_l_english.yml                     ← BOM UTF-8
        └── spanish/exodos_l_spanish.yml                     ← BOM UTF-8
```

---

## 5. BY OTHER MEANS (v3.0)

### 5.1 Descripción

`by_other_means/` es el mod de control de personajes. En v3.0 absorbe:
- Las funciones originales de BOM: Eliminar Rivales, Bacanal, Ego Sum
- `tlv_kill_ruler` renombrado a `bom_kill_ruler` (movido desde TLV)
- Las dos funciones nuevas de Iron Hand: `iha_seize_holdings` y `iha_fill_the_void`

### 5.2 Terminología engine

| Diseño | Engine |
|---|---|
| "rivales del gobernante" | `every_character = { limit = { is_ruler = yes } every_rival = { } }` desde country scope |
| "gobernante tiene rivales" | `any_character = { is_ruler = yes num_of_rivals >= 1 }` desde country scope |
| "gobernante" | `every_character = { limit = { is_ruler = yes } }` desde country scope |
| "rival del mismo país" | `any_rival = { employer = ROOT }` desde character scope del gobernante |
| "propiedades del rival" | `every_holdings = { }` desde character scope del rival |

### 5.3 Arquitectura — bom_confirm

- 1 decisión, ejecución directa, sin fases, sin popup
- Mata a todos los rivales del gobernante (hasta 4 — límite del engine)
- Stateless — sin variables de estado

**Costos:** 2000 oro | manpower -1 (500 pantalla) | +40 tyranny | cap ≤80 | rivals ≥ 1

### 5.4 Arquitectura — bom_bacanal

- 1 decisión, ejecución directa, sin popup
- Aplica trait `lustful` a todos los rivales del gobernante
- `remove_trait = chaste` antes de `add_trait = lustful`

**Costos:** 500 oro | +10 tyranny | cap ≤90 | rivals ≥ 1

### 5.5 Arquitectura — bom_kill_ruler

- Movido desde `the_last_vote/` en v1.2
- 1 decisión, ejecución directa, sin popup
- Mata al gobernante actual — el sucesor es asignado por el engine vanilla
- Sin restricción de tipo de gobierno

**Costos:** 2000 oro | manpower -1 (500 pantalla) | +40 tyranny | cap ≤60 | stability ≥ 50

### 5.6 Arquitectura — iha_seize_holdings

- Confisca todas las propiedades del único rival del gobernante
- Condición: exactamente 1 rival en total, de la misma nación que root
- Patrón validado en engine: `while { limit = { num_holdings_owned > 0 } random_holdings { save_scope_as = iha_holding } remove_holding = scope:iha_holding }` — `remove_holding` va dentro del `while` pero fuera del bloque `random_holdings`
- Aplica `family_property_seized_l` al rival (-40 loyalty por 20 años)
- El rival sobrevive

**Costos:** 2000 oro | +40 tyranny | cap ≤60 | rivals=1 exacto, employer=ROOT

### 5.7 Arquitectura — iha_fill_the_void

- Transfiere todas las propiedades sin dueño del país al rival seleccionado
- Condición: exactamente 1 rival en total, de la misma nación que root
- La capital está automáticamente excluida (el engine no le asigna holding slot)
- Usa `save_scope_as = iha_rival_scope` para capturar al rival, luego `scope:iha_rival_scope = { add_holding = PREV }` desde province scope

**Costos:** 2000 oro | +40 tyranny | cap ≤60 | rivals=1 exacto, employer=ROOT

### 5.8 Código completo

#### bom_decisions.txt
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
            add_treasury = -2000
            add_manpower = -1
            add_tyranny = 40
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    add_health = -100
                }
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
            add_treasury = -500
            add_tyranny = 10
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    remove_trait = chaste
                    add_trait = lustful
                }
            }
        }
        ai_will_do = { factor = 0 }
    }

    bom_kill_ruler = {
        potential = {
            is_ai = no
        }
        highlight = { scope:province = { always = yes } }
        allow = {
            is_ai = no
            tyranny <= 60
            stability >= 50
            treasury >= 2000
            manpower >= 1
        }
        effect = {
            add_tyranny = 40
            add_stability = -50
            add_treasury = -2000
            add_manpower = -1
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
            add_treasury = -2000
            add_tyranny = 40
            every_character = {
                limit = { is_ruler = yes }
                every_rival = {
                    limit = { employer = ROOT }
                    while = {
                        limit = { num_holdings_owned > 0 }
                        random_holdings = {
                            save_scope_as = iha_holding
                        }
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
            add_treasury = -2000
            add_tyranny = 40
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

#### bom_events.txt
```pdxscript
namespace = bom
```

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

#### descriptor.mod
```
name = "By Other Means"
version = "3.0"
supported_version = "2.0.*"
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

#### bom_decisions_ego_sum.txt
*(sin cambios — ver zip)*

#### bom_l_english_ego_sum.yml
*(sin cambios — ver zip)*

#### bom_l_spanish_ego_sum.yml
*(sin cambios — ver zip)*

---

## 7. THE LAST VOTE (v1.7)

### 7.1 Descripción

En v1.2, `the_last_vote/` queda reducido a una sola decisión: `tlv_confirm`. `tlv_kill_ruler` fue movido a `by_other_means/` como `bom_kill_ruler`.

### 7.2 Arquitectura — tlv_confirm

| Condición | Valor | Lógica |
|---|---|---|
| `is_republic` | yes | Solo en república |
| `tyranny` | <= 60 | La decisión agrega +40 — salís con hasta 100 |
| `stability` | >= 50 | La decisión resta -50 — salís con mínimo 0 |
| `treasury` | >= 2000 | La decisión resta -2000 |
| `popularity` del gobernante | >= 50 | Apoyo popular suficiente |

Costos: +40 tyranny, -50 stability, -2000 oro.
Orden obligatorio: `clearup` → `law_variable` → `change_government` → `law_change`.

### 7.3 Código completo

#### tlv_decisions.txt
*(sin cambios — ver zip)*

#### tlv_events.txt
*(sin cambios — ver zip)*

#### tlv_l_english.yml
*(sin cambios — ver zip)*

#### tlv_l_spanish.yml
*(sin cambios — ver zip)*

#### the_last_vote.mod
```
name = "The Last Vote"
version = "1.7"
supported_version = "2.0.*"
path = "mod/the_last_vote"
```

#### descriptor.mod
```
name = "The Last Vote"
version = "1.7"
supported_version = "2.0.*"
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

#### tgl_decisions.txt
*(sin cambios — ver zip)*

#### tgl_l_english.yml
*(sin cambios — ver zip)*

#### tgl_l_spanish.yml
*(sin cambios — ver zip)*

#### the_great_leap.mod
```
name = "The Great Leap"
version = "1.5"
supported_version = "2.0.*"
path = "mod/the_great_leap"
```

#### descriptor.mod
```
name = "The Great Leap"
version = "1.5"
supported_version = "2.0.*"
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
├── build_mods.py                                            ← script de generación manual (opcional)
├── exodos.mod                                               ← sin BOM
├── by_other_means.mod                                       ← sin BOM
├── the_last_vote.mod                                        ← sin BOM
├── the_great_leap.mod                                       ← sin BOM
│
├── exodos/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/exodos_decisions.txt                       ← BOM UTF-8
│   ├── events/exodos_events.txt                             ← BOM UTF-8
│   ├── common/
│   │   ├── on_action/exodos_on_action.txt                   ← BOM UTF-8
│   │   ├── units/exodos_units.txt                           ← BOM UTF-8
│   │   └── scripted_effects/exodos_scripted_effects.txt     ← BOM UTF-8
│   └── localization/
│       ├── english/exodos_l_english.yml                     ← BOM UTF-8
│       └── spanish/exodos_l_spanish.yml                     ← BOM UTF-8
│
├── by_other_means/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/
│   │   ├── bom_decisions.txt                                ← BOM UTF-8
│   │   └── bom_decisions_ego_sum.txt                        ← BOM UTF-8
│   ├── events/bom_events.txt                                ← BOM UTF-8
│   └── localization/
│       ├── english/
│       │   ├── bom_l_english.yml                            ← BOM UTF-8
│       │   └── bom_l_english_ego_sum.yml                    ← BOM UTF-8
│       └── spanish/
│           ├── bom_l_spanish.yml                            ← BOM UTF-8
│           └── bom_l_spanish_ego_sum.yml                    ← BOM UTF-8
│
├── the_last_vote/
│   ├── descriptor.mod                                       ← sin BOM
│   ├── decisions/tlv_decisions.txt                          ← BOM UTF-8
│   ├── events/tlv_events.txt                                ← BOM UTF-8
│   └── localization/
│       ├── english/tlv_l_english.yml                        ← BOM UTF-8
│       └── spanish/tlv_l_spanish.yml                        ← BOM UTF-8
│
└── the_great_leap/
    ├── descriptor.mod                                       ← sin BOM
    ├── decisions/tgl_decisions.txt                          ← BOM UTF-8
    └── localization/
        ├── english/tgl_l_english.yml                        ← BOM UTF-8
        └── spanish/tgl_l_spanish.yml                        ← BOM UTF-8
```

Total archivos en mod.zip: 29 (sin build_mods.py).

---

## 10. INSTALACIÓN

Extraer el contenido de `mod.zip` en:
```
C:\Users\{usuario}\Documents\Paradox Interactive\Imperator\mod\
```

Extracción limpia — reemplaza todo lo que hubiera. El archivo `dlc_load.json` en esa misma carpeta debe incluir:
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

Ego Sum, Bacanal, Kill Ruler, IHA Seize e IHA Fill the Void no tienen entrada propia — viven dentro de `by_other_means/` y se activan con ese mod.

---

## 11. PENDIENTES

| Tarea | Mod | Prioridad |
|---|---|---|
| Evaluar contador de pulsos como límite secundario para Gather y Distribute | Exodus | MEDIA |
| Publicar en Steam Workshop | Todos | BAJA |

---

## 12. HISTORIAL

### v1.3.5 — 2026-05
- **EXODUS** — `exodos_activate_transfer`: `tyranny <= 90` corregido a `tyranny <= 80` en `allow` (FIX-10)
- **EXODUS** — `is_ai = no` agregado en `allow` de los tres `exodos_activate_*` (FIX-09)
- **EXODUS** — Nombres de unidades corregidos a español: "Exodos - Concentrate" → "Exodos - Concentrar", "Exodos - Distribute" → "Exodos - Distribuir", "Exodos - Origin" → "Exodos - Origen", "Exodos - Destination" → "Exodos - Destino" (FIX-02 expandido)
- **EXODUS** — Comentario `# CANCELAR — solo Transfer` corregido a `# CANCELAR — Transfer, Gather, Distribute` en decisions.txt y ambos yml (FIX-11)
- **BOM** — `iha_fill_the_void_desc` EN: agregado "to the selected rival" (FIX-03)
- **BOM** — `iha_fill_the_void_desc` ES: "holdings" → "propiedades", agregado "seleccionado" (FIX-03)
- **BOM** — `iha_seize_holdings_desc` ES: "tomarla." → "Tomala." (FIX-04)
- **TGL** — `supported_version = "1.5"` → `"2.0.*"` en `the_great_leap.mod` y `the_great_leap/descriptor.mod` (FIX-05)
- **Doc** — Sección 1.9: convención de idioma de UI agregada como norma del ecosistema
- **Doc** — Sección 1.10: tabla de nombres de unidades Exodus agregada
- **Doc** — Sección 2.6: patrón `remove_holding` corregido — va dentro del `while` pero fuera de `random_holdings`; documentación anterior era incorrecta
- **Doc** — Sección 4.2: cleanup de Gather y Distribute documentado como condicional (intencional); tabla de pulsos corregida; mejora futura documentada
- **Doc** — Sección 4.3: nombres de unidades actualizados con equivalentes en español
- **Doc** — Sección 5.6: patrón `remove_holding` corregido para reflejar código real validado
- **Doc** — Flujo de trabajo con IA documentado; rol de `build_mods.py` aclarado
- **Doc** — Sección "Estado actual" agregada al inicio
- **Doc** — Fixes pendientes incorporados en sección PENDIENTES; `fixes.md` separado eliminado
- **Versión** — Exodos 1.17 → 1.18

### v1.3.4 — 2026-05
- **EXODUS** — 21 íconos `.dds` eliminados del zip — el engine no los cargaba (warnings `Missing Icon for Modifier: exodos_marker_*` persistían igual); los warnings son permanentes e ignorables, no afectan ninguna mecánica
- **Doc** — Sección 3.4 actualizada: warnings de `exodos_marker_*` documentados como permanentes
- **Doc** — Sección 9 actualizada: carpeta `gfx/` eliminada, conteo 50 → 29 archivos
- **build_mods.py** — `BINARY_EXTENSIONS` y lógica de skipped eliminados — el proyecto no tiene `.dds`; output simplificado
- **VALIDACIÓN COMPLETA** — todas las funciones testeadas en engine y funcionando

### v1.3.3 — 2026-05
- **BOM** — `iha_seize_holdings` corregido — `remove_holding` dentro del `while` pero fuera de `random_holdings`

### v1.3.2 — 2026-05
- **BOM** — `iha_seize_holdings` corregido (primera iteración — incompleta)
- **EXODUS** — íconos base agregados (luego eliminados en v1.3.4)

### v1.3.1 — 2026-05
- **BOM** — `iha_fill_the_void` corregido — `current_ruler` no resuelve desde province scope

### v1.3 — 2026-05
- **EXODUS** — `exodos_cancel` ampliado a las 3 operaciones en todas las fases
- **EXODUS** — 19 íconos `.dds` agregados (luego eliminados en v1.3.4)

### v1.2 — 2026-05
- **BOM** — `bom_kill_ruler` agregado; `bom.2` eliminado; `iha_seize_holdings` e `iha_fill_the_void` agregados
- **TLV** — `tlv_kill_ruler` eliminado (movido a BOM); costos actualizados
- **EXODUS** — tyranny cap Gather/Distribute ≤80 → ≤90; Transfer confirm: `war = no` agregado

### v1.1 — 2026-05
- **TGL** — `tyranny <= 0` corregido; tooltip corregido
- **EXODUS** — `exodos_cancel` ampliado; `war = no` en confirm Gather y Distribute
- **EGO SUM** — `remove_trait` antes de `add_trait` corregido
- **BOM** — `war = no` eliminado de `bom_confirm`

### v1.0 — 2026-04
- Documento unificado creado

---

*Drago Mod Pack — Backup Técnico Unificado v1.3.5 — mod en mod.zip*
