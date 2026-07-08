# EXODOS: REPARTIR ESCLAVOS — SLAVE DISTRIBUTOR
## Backup Técnico de Sesión
### Engine: Imperator Roma 2.0.4 | Módulo: Slave Distributor | v0.2 (diseño cerrado, implementación pendiente)

---

## INSTRUCCIONES PARA LA IA QUE LEA ESTE DOCUMENTO

Este documento es el backup técnico completo del diseño de la función **Exodos: Repartir Esclavos** para el mod IRAM. Es autónomo — no requiere ningún otro documento para entender el diseño. Para implementar (escribir código), sí se necesitan los archivos fuente listados en la sección de archivos.

**Antes de trabajar en esta función, leer este documento completo de principio a fin. Sin excepciones.**

### Reglas de trabajo

1. Los thresholds de la sección 3 fueron verificados **ingame por el usuario con capturas**. Son verdad absoluta — no recalcular, no reemplazar con valores de memoria ni de la wiki.
2. Los modificadores globales de la sección 4 fueron extraídos directamente de `game.zip`. Son verdad absoluta.
3. La wiki (`wiki_imperator.txt`) tiene errores de interpretación sobre esta mecánica — NO usarla como fuente para los thresholds. Solo para contexto general.
4. Las decisiones marcadas como **CERRADO** no se reabren salvo pedido explícito del usuario.
5. El mod opera sobre IR 2.0.4. No asumir compatibilidad con otras versiones.
6. Ciudades y metrópolis son siempre el ancla — **nunca son destino** del Slave Distributor.
7. Misiones, eventos y exclusivas de nación (ej: ANU) **no se consideran** para el diseño de los tiers. Solo modificadores genéricos disponibles para cualquier jugador.
8. El diseño de los tiers está **CERRADO**. No recalcular salvo pedido explícito del usuario con nuevas capturas.
9. La localización está **CERRADA**. Ver sección 6.
10. Seguir las convenciones del ecosistema IRAM en todo momento — ver sección 7.

### Archivos necesarios para continuar el desarrollo

Pedir al usuario que suba **todos** estos archivos al inicio de la sesión antes de escribir código:

| Archivo | Por qué es necesario |
|---|---|
| `backup_slave_distributor_v2.md` | **Este documento** — fuente de verdad del módulo |
| `backup_mod_pack_IRAM_1_1.md` | Backup técnico del mod IRAM — convenciones, reglas, estructura de archivos |
| `mod_pack_IRAM_4.zip` | Código fuente actual del mod — base a modificar |
| `game.zip` | Engine IR 2.0.4 — verificar triggers y sintaxis si hay dudas |

Los siguientes archivos son opcionales (solo si surge una duda específica):

| Archivo | Cuándo pedirlo |
|---|---|
| `optimizador_provincial_backup_v4.md` | Si hay dudas sobre el flujo general del ecosistema |
| `wiki_imperator.txt` | Solo para contexto general — NO para thresholds de slaves |

---

## ESTADO ACTUAL

| Item | Valor |
|---|---|
| Versión del módulo | v0.2 |
| Fecha | 2026-05 |
| Función en el juego | "Exodos: Repartir Esclavos" (ES) / "Exodos: Distribute Slaves" (EN) |
| Estado del diseño de thresholds | **CERRADO** — verificados ingame con capturas (sección 3) |
| Estado de los modificadores globales | **CERRADO** — extraídos de `game.zip` (sección 4) |
| Estado de los tiers | **CERRADO** — 5 decisiones de tier definidas (sección 5) |
| Estado de la localización | **CERRADA** — textos definidos (sección 6) |
| Estado de la implementación | **PENDIENTE** — no se escribió código |
| Temas críticos antes de codear | **4 temas abiertos** — ver sección 8 (URGENTE) |

---

## 1. POSICIÓN EN EL ECOSISTEMA

### 1.1 Flujo completo

La función Slave Distributor es el **cuarto paso** del ecosistema, posterior a conversión y asimilación:

```
1. GATHER (legacy o dentro de Optimize)
   └── Reúne todos los pops del área en la ciudad ancla

2. DISTRIBUTE / OPTIMIZE
   └── Distribuye pops desde el ancla para maximizar velocidad de conversión y asimilación

3. [tiempo — conversión y asimilación ocurren]

4. EXODOS: REPARTIR ESCLAVOS  ←  este módulo
   └── FASE GATHER: reúne todos los slaves de los asentamientos en el ancla
   └── FASE DISTRIBUTE: reparte slaves desde el ancla a cada asentamiento
       según su tipo de building, para maximizar producción de trade goods
```

### 1.2 Premisa de partida

**Todos los territorios del área ya producen 1 trade good.** El objetivo de esta función es llevarlos a **2 trade goods** (surplus), que es lo que habilita rutas de comercio de exportación. No se diseña para llegar a 3 o más.

### 1.3 Qué es el ancla

La ciudad o metrópolis del área. Es siempre el territorio desde donde se reparten los slaves. **Nunca es destino** — el Slave Distributor no toca los pops del ancla, solo los usa como reservorio.

---

## 2. MECÁNICA DEL ENGINE — BASE TEÓRICA

> ⚠️ Esta sección es base teórica extraída de `game.zip`. Los valores prácticos verificados ingame están en la sección 3 y son los que mandan. No usar esta sección para calcular counts.

### 2.1 Fuente

`game.zip` → `common/defines/00_defines.txt` y archivos de buildings, laws, inventions.

### 2.2 Defines del engine

```
NTrade = {
    SLAVE_POPS_TO_PRODUCE_EXTRA = 20   # slaves adicionales para pasar de 1 a 2 goods
    MINIMUM_SLAVES_PER_GOOD = 3        # base mínima antes de modificadores
}
```

### 2.3 Buildings con local_goods_from_slaves (solo asentamientos)

Extraído de `game.zip` → `common/buildings/00_default.txt`:

| Building | local_goods_from_slaves | Notas |
|---|---|---|
| `slave_mine_building` (Mina) | −5 | Solo asentamientos con trade good mineable |
| `basic_settlement_infratructure_building` (Asentamiento Agrícola) | −5 | Solo asentamientos con trade good de comida |
| `foundry_building` (Fundición) | −4 | Solo ciudades (`has_city_status = yes`) — **irrelevante, el ancla no es destino** |
| `latifundia_building` (Finca de Esclavos) | **0** | No afecta goods_from_slaves — solo slave output y comida |

### 2.4 Modificadores de established_city

`established_city` da `local_goods_from_slaves = +5` (positivo = sube el threshold). Irrelevante para el diseño porque las ciudades son el ancla, no el destino.

---

## 3. THRESHOLDS VERIFICADOS INGAME — VERDAD ABSOLUTA

> ⚠️ Estos valores fueron confirmados por el usuario con capturas ingame. Son la verdad absoluta para el diseño de los tiers. No recalcular.

### 3.1 Configuración de partida del usuario (referencia)

- Roma, dictadura (tipo monarquía)
- Todas las techs genéricas activas (incluyendo inv cívica `global_goods_from_slaves_inv` −1)
- Ley Roma activa (−2 global)
- Total modificadores globales activos: **−3**

### 3.2 Slaves necesarios para pasar de 1 a 2 trade goods

Con la configuración del usuario (−3 modificadores globales):

| Tipo de asentamiento | Slaves necesarios para 2do good |
|---|---|
| Con Mina o Asentamiento Agrícola | **9** |
| Otros (sin building o con Finca de Esclavos) | **14** |

Estos son los valores del **tier 2** en la tabla de la sección 5.

---

## 4. MODIFICADORES GLOBALES GENÉRICOS — FUENTE: game.zip

> Solo se consideran modificadores genéricos disponibles para cualquier jugador. Misiones, exclusivas de nación y eventos están excluidos del diseño.

### 4.1 Todos los global_goods_from_slaves negativos genéricos

Extraído de `game.zip` → laws, inventions, great_work_effects:

| Fuente | Archivo fuente | Valor | Tipo de gobierno |
|---|---|---|---|
| Inv cívica `global_goods_from_slaves_inv` | `common/inventions/00_civic_inventions.txt` | −1 | Todos |
| Ley Roma (la de civic_tech ≥ 12) | `common/laws/00_rome.txt` | −2 | Roma/Monarquía |
| Ley República (equivalente) | `common/laws/00_republic.txt` | −2 | República |
| Ley tribal `formalized_industry_law_tribal` | `common/laws/00_tribal.txt` | −1 | Tribal |
| Gran obra tier 4 `gw_effect_slave_work_tier_4` | `common/great_work_effects/00_default.txt` | −1 | Todos |

**Nota:** Los tiers 1, 2 y 3 de la gran obra tienen `global_goods_from_slaves` comentado (`#`) en el código — están desactivados en el engine. Solo el tier 4 aplica.

### 4.2 Modificadores excluidos del diseño

| Fuente | Razón de exclusión |
|---|---|
| `channeled_irrigation_invention` (Oratory) | Exclusiva de ANU |
| `country_improvement_rhodesian_designs` | Misión específica |
| `global_goods_from_slaves = -4` (subject type) | Solo para subjects — irrelevante para el jugador |
| Modifiers de eventos y misiones (`from_events_province`, `from_missions`) | Variables, no genéricos |

### 4.3 Máximo acumulable por tipo de gobierno

| Gobierno | Modificadores acumulables | Total máximo |
|---|---|---|
| Roma / Monarquía / República | Inv cívica (−1) + Ley (−2) + Gran obra t4 (−1) | **−4** |
| Tribal | Inv cívica (−1) + Ley tribal (−1) + Gran obra t4 (−1) | **−3** |

Ley Roma/República y tribal son **mutuamente excluyentes** (un jugador tiene un solo tipo de gobierno).

---

## 5. TIERS DE DISTRIBUCIÓN — CERRADO

### 5.1 Lógica de los tiers

Cada tier define cuántos slaves se mandan por tipo de asentamiento. El jugador elige el tier que corresponde a sus modificadores globales activos. A más modificadores activos, menor threshold, menor tier a elegir.

### 5.2 Tabla de tiers

| Decisión | Mina / Asentamiento Agrícola | Otros | Modificadores globales activos |
|---|---|---|---|
| `exodos_slave_dist_t1` | **8** | **13** | −4 (inv + ley mon/rep + gran obra t4) |
| `exodos_slave_dist_t2` | **9** | **14** | −3 (inv + ley mon/rep) ← config usuario |
| `exodos_slave_dist_t3` | **10** | **15** | −2 (solo ley) |
| `exodos_slave_dist_t4` | **11** | **16** | −1 (solo inv) |
| `exodos_slave_dist_t5` | **12** | **17** | 0 (ningún modificador) |

### 5.3 Regla de branching por building

Para cada asentamiento destino, el pulso detecta el building y asigna el count correspondiente:

```
si has_building = slave_mine_building
    → count = COUNT_MINA_AGRICOLA del tier elegido
si has_building = basic_settlement_infratructure_building
    → count = COUNT_MINA_AGRICOLA del tier elegido
sino (cualquier otro asentamiento, incluyendo los que tienen latifundia)
    → count = COUNT_OTROS del tier elegido
```

La `latifundia_building` (Finca de Esclavos) cae en "Otros" — no tiene `local_goods_from_slaves` y no modifica el threshold.

---

## 6. LOCALIZACIÓN — CERRADA

### 6.1 Decisión de activación

| Clave | Español | Inglés |
|---|---|---|
| `exodos_activate_slave_dist` | `"Exodos: Repartir Esclavos"` | `"Exodos: Distribute Slaves"` |
| `exodos_activate_slave_dist_desc` | Ver 6.2 | Ver 6.2 |

### 6.2 Texto de la decisión de activación

**Español:**
```
"Se reuniran todos los esclavos de los asentamientos de la provincia en la ciudad ancla
y luego se distribuiran segun el tier elegido para maximizar la produccion de trade goods.
Recluta o mueve un ejercito o leva bajo el mando del rival del gobernante en cualquier
territorio de la provincia — la unidad marcadora sera generada ahi automaticamente,
usala para marcar tu ciudad principal en la provincia. Podes moverla antes de elegir
la cantidad, el costo de la operacion se cobra en la siguiente decision."
```

**Inglés:**
```
"All slaves from the province's settlements will be gathered into the anchor city,
then distributed according to the chosen amount to maximize trade good production.
Raise or move an army or levy under the ruler's rival in any territory of the province
— the marker unit will be generated there automatically, use it to mark your main city
in the province. You may move it before choosing the amount, the operation cost is
charged in the next decision."
```

### 6.3 Decisiones de tier

| Clave | Español | Inglés |
|---|---|---|
| `exodos_slave_dist_t1` | `"Mina/Asentamiento Agricola: 8 esclavos — Otros: 13 esclavos"` | `"Mine/Farming Settlement: 8 slaves — Other: 13 slaves"` |
| `exodos_slave_dist_t2` | `"Mina/Asentamiento Agricola: 9 esclavos — Otros: 14 esclavos"` | `"Mine/Farming Settlement: 9 slaves — Other: 14 slaves"` |
| `exodos_slave_dist_t3` | `"Mina/Asentamiento Agricola: 10 esclavos — Otros: 15 esclavos"` | `"Mine/Farming Settlement: 10 slaves — Other: 15 slaves"` |
| `exodos_slave_dist_t4` | `"Mina/Asentamiento Agricola: 11 esclavos — Otros: 16 esclavos"` | `"Mine/Farming Settlement: 11 slaves — Other: 16 slaves"` |
| `exodos_slave_dist_t5` | `"Mina/Asentamiento Agricola: 12 esclavos — Otros: 17 esclavos"` | `"Mine/Farming Settlement: 12 slaves — Other: 17 slaves"` |

Los `_desc` de las decisiones de tier replican el mismo texto que Optimize — advertencia de guardado, explicación del marcador, MAYÚSCULAS para acciones irreversibles. Ver `exodos_opt_range_03_desc` en `exodos_l_spanish.yml` / `exodos_l_english.yml` como plantilla exacta.

---

## 7. CONVENCIONES DEL ECOSISTEMA IRAM — OBLIGATORIO RESPETAR

Extraído de `backup_mod_pack_IRAM_1_1.md`. Estas reglas aplican a todo código nuevo:

1. `is_ai = no` va siempre en `potential` **Y** en `allow`. Sin excepción.
2. No existe `exodos_cancel` particular — solo `exodos_cancel_all`. No agregar cancels particulares.
3. Los costos de la operación **no se escriben en los textos de localización** — el engine los muestra automáticamente desde el `effect`.
4. BOM UTF-8 en todos los `.txt` y `.yml`. Sin BOM en los `.mod`.
5. Todo el código nuevo va en el mod `exodos/` — los otros tres mods son TEST SHELL vacíos.
6. El archivo de decisiones del módulo va en `exodos/decisions/exodos_decisions_slave_dist.txt` (archivo nuevo).
7. El pulso mensual va en `exodos/common/on_action/exodos_on_action.txt` (agregar bloques al existente).
8. La localización va en `exodos/localization/spanish/exodos_l_spanish.yml` y `exodos/localization/english/exodos_l_english.yml` (agregar al existente).
9. El cleanup de variables nuevas va en `exodos/common/scripted_effects/exodos_scripted_effects.txt` (modificar el existente).

### 7.1 Patrón de scope del pulso mensual (referencia de Optimize)

El patrón verificado y funcional para iterar territorios del área desde el ancla es:

```
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

```
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

**Para el Slave Distributor**, el Gather filtra por `pop_type = slaves` y el corte es cuando los asentamientos no-ancla tienen menos de 2 slaves (mismo criterio que Optimize con `total_population`).

---

## 8. TEMAS CRÍTICOS ANTES DE CODEAR — URGENTE

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

**Acción requerida:** Confirmar que el patrón de cleanup es idéntico al de Optimize antes de implementar. Verificar en `mod_pack_IRAM_4.zip` → `exodos_scripted_effects.txt`.

### TEMA 4 — Unidad marcadora ⚠️

**Problema:** La función necesita su propia unidad marcadora (`exodos_unit_slave_dist`), igual que Optimize tiene `exodos_unit_optimize`. Hay que agregarla al chequeo de "unidad destruida = error" en el `monthly_country_pulse` de `exodos_on_action.txt`.

**Acción requerida:** Confirmar que el patrón de activación/destrucción de la unidad es idéntico al de Optimize. El bloque a agregar en `on_action` sería:

```
# Unidad Slave Dist destruida
if = {
    limit = {
        has_variable = exodos_slave_dist_active
        NOT = { any_unit = { has_variable = exodos_unit_slave_dist } }
    }
    trigger_event = { id = exodos.1 }
}
```

---

## 9. ESQUEMA DEL PULSO MENSUAL (DISEÑO — NO IMPLEMENTADO)

Este es el pseudocódigo del comportamiento esperado. No es código real del mod — es el diseño a implementar una vez resueltos los temas de la sección 8.

```
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

---

## 10. REFERENCIAS TÉCNICAS RÁPIDAS

### 10.1 Counts por tier (para copiar al escribir código)

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

### 10.2 Triggers clave (para copiar al escribir código)

```
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

### 10.3 Nombres de decisiones y variables

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

---

*Backup v2 generado al cierre de sesión. Próximo paso: resolver los 4 temas de la sección 8 en orden antes de codear.*
