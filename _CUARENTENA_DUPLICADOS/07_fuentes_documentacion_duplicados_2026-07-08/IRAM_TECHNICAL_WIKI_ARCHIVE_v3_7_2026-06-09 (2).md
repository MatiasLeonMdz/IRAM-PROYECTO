# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK
## TECHNICAL WIKI ARCHIVE — v3.7
### Engine: Imperator Roma 2.0.4 | Historial y código fuente v1/v2/v3

**Este documento es el ARCHIVE del TECHNICAL WIKI.** Contiene el historial narrativo,
código fuente completo de v1/v2/v3, decisiones descartadas, y entradas pre-v4 del log de sesiones.
Para trabajo activo usar el **TECHNICAL_WIKI_ACTIVE_v3_0**.

---

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

## TECHNICAL_WIKI ACTIVE v3.1 + ARCHIVE v3.1 — 2026-05-29 16:17

- Sección 19 del ACTIVE actualizada con entradas de sesiones 2026-05-29.
- Fix ciudades secundarias Gather Global codeado en v4.3.11.
- Zip canónico activo: `mod_pack_IRAM_v4_3_11_2026-05-29_05-49.zip`.

## TECHNICAL_WIKI v3.0 (split ACTIVE + ARCHIVE) — 2026-05-27 20:28

- SUPERBACKUP v2.6 dividido en TECHNICAL_WIKI ACTIVE v3.0 + ARCHIVE v3.0.
- ACTIVE: Secciones 0–7, 9–13, 16–17, 19 (entradas v4), 20–22.
- ARCHIVE: Secciones 8/8-A/8-B/8-C, 14, 18, entradas pre-v4 de Sección 19.
- PROMPT_MAESTRO actualizado a v3.8: referencias SUPERBACKUP → TECHNICAL_WIKI ACTIVE/ARCHIVE.
- INSTRUCCIONES_HUMANO actualizado: orden de carga, protocolo de reanudación, smoke test.

## SUPERBACKUP v2.6 — 2026-05-27 20:06 (sesión estratégica)

- Nombre del documento: TECHNICAL_WIKI — CERRADO. Más profesional que SUPERBACKUP.
- Decisión Git: commit inicial con v4.3.7 como estado canónico. No reconstruir historial pasado.
- Modelo: Sonnet sin pensamiento para docs y codeo conocido. Con pensamiento solo para arquitectura sin solución clara.
- Visión reformulada: "El mod exitoso es el entregable. El aprendizaje es el objetivo real."

## SUPERBACKUP v2.5 — 2026-05-27 (sesiones 15:01, 15:12, 15:17)

- Verificación de sintaxis engine contra game.zip: `remove_building_level` sin llaves (RE8),
  demolición con `if` independientes no `else_if` (RE9), `trade_goods = X` directo sin triggers del engine (RE10).
- Tabla Constructor Automático cerrada definitivamente: 34 trade goods cubiertos.
  Correcciones: `dyes`→`dye`, `earthenware`→`earthware`, `gemstones`→`gems`, `livestock`→`cattle`.
  `salt` y `honey` → `latifundia_building` (not `basic_settlement_infratructure_building` — allow incompatible).
- Diseño Constructor Automático CERRADO: 7 `if` independientes para demoler, `if/else_if` para construir,
  skip `fortress_building` en limit del `every_owned_province`, instantáneo.

## SUPERBACKUP v2.4 — 2026-05-27 17:14 (auditoría bugs v4.3.6)

- **5 bugs corregidos en zip v4.3.7:**
  - BUG 1: `iram_decisions_optimize_global.txt` — `set_variable` ×2 fuera del `effect` por llaves desbalanceadas.
  - BUG 2: `exodos_decisions_gather_global.txt` — BOM doble (real + texto literal).
  - BUG 3: `exodos_decisions_gather_global.txt` — `set_variable` ×2 fuera del `effect` por llaves desbalanceadas.
  - BUG 4: `exodos_decisions_gather_global.txt` — `add_popularity` en scope país (ignorado por engine).
  - BUG 5: `exodos_scripted_effects.txt` — `iram_cleanup_menu` usaba `iram_menu_rival_heir_open` (inexistente).
- Zip canónico: `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip`.

## SUPERBACKUP v2.3 — 2026-05-26 (sesiones 16:54 → 20:49)

- **Rediseño árbol de menú CERRADO** — IDs iram_01–iram_25, orden de aparición = orden lógico de uso.
  Variables de submenú renombradas: `iram_menu_movimiento_open`→`iram_menu_management_open`,
  `iram_menu_demografia_open`→`iram_menu_behavior_open`, `iram_menu_politico_open`→`iram_menu_political_open`.
- **Funciones eliminadas del zip activo:** Gather/Distribute/Optimize por área con unidad marcadora.
  Código preservado en Sección 8. Transfer se mantiene.
- **Desactivar individuales de Comportamiento de POPs eliminados** — `iram_02` (cancel_all) los absorbe.
- **Funciones nuevas:** Distribute Global (`iram_11`), Constructor Automático (`iram_12`), Optimize Global (`iram_13`).
- **Gather Global sin confirm previo** — `iram_10` es decisión única.
- **Protocolo de test sin costos** — costos de Transfer, GG, Demografía, BOM/IHA/TLV/TGL eliminados
  temporalmente. Tabla de referencia para restaurar en Sección 3.4 del ACTIVE.
- **Diseño Distribute Global:** 5 áreas/pulso, 3 rangos (5/10/15 pops por province), threshold dinámico.
- **Diseño Optimize Global CERRADO:** dos pasos — guard del ancla por demanda real de slaves
  (mine×10 + básico×10 + latifundia×15), distribución directa desde ancla a cada province destino.
- **Diseño Constructor Automático:** barre settlements, demuela todo, construye según trade good.
  Nunca toca `fortress_building` ni ciudades/metrópolis. Instantáneo.
- **Convención de nombres de archivos** formalizada — `AAAA-MM-DD_HH-MM` sin letras de sufijo.
- **SESSION_LOG** definido como 4to archivo del sistema de control.
- **R17 agregada** al PROMPT: leer Sección 3.7 y 19 antes de responder sobre árbol de menú o IDs.

## v4.3.15 — 2026-05-29 23:02

- Costos eliminados temporalmente para test amplio de funciones nuevas.
- Zip: `mod_pack_IRAM_v4_3_15_2026-05-29_23-02.zip`.

## TECHNICAL_WIKI ACTIVE v3.4 + ARCHIVE v3.4 — 2026-06-03 01:09

- Limpieza de secciones stale en ACTIVE v3.3.
- **Sec 3.3 IDs tabla:** nota de advertencia y 22 filas "⏳ pendiente refactor/codear" → ✅ IMPLEMENTADO.
  Refactor IDs iram_01–iram_25 completo en zip v4.3.16 — tabla refleja estado real.
- **Sec 4:** OG entry "⚠ PENDIENTE diseño" → "✅ IMPLEMENTADO v4.3.16".
- **Sec 5 matriz:** OG columna v4 "stub, on_action pendiente" → "✅ IMPLEMENTADO v4.3.16".
- **Tabla de costos:** OG row — guard `has_variable = exodos_gather_global_completed` removido
  (guard descartado en sesión 00:38, faltaba en esta tabla).
- Zip canónico: `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` (sin cambios).

## TECHNICAL_WIKI ACTIVE v3.3 + ARCHIVE v3.3 — 2026-06-03 00:38

- Auditoría completa zip v4.3.16 vs wiki ACTIVE v3.2.
- **Discrepancia resuelta:** DG (Distribute Global on_action), OG (Optimize Global on_action)
  y Constructor Automático (`iram_12`) ya implementados en zip — wiki los tenía como PENDIENTE.
  Wiki actualizada a v3.3.
- **Operaciones por área:** `exodos_decisions_gather/distribute/optimize.txt` no existen en v4.3.16.
  Estaban en v4.3.7. Sin documentación de remoción deliberada — queda abierto.
- **Señal GG→OG descartada:** `exodos_gather_global_completed` no se implementa. OG y DG
  son de activación libre por diseño ("el ecosistema habilita, no castiga").
- **Cerrados:** Fix Gather legacy, 3 variables en cleanup, guards OG, refactor zip, Git.
- Zip canónico: `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip` (sin cambios).

## v4.3.16 — 2026-05-30 03:14

- **BUG A corregido:** `exodos.2` decía "Optimize Global" pero era disparado tanto por DG como por OG.
  Fix: locs de exodos.2 renombradas a "Distribute Global". exodos.3 creado para OG. exodos.4 creado para GG.
- **BUG B corregido:** GG terminaba sin notificar al jugador.
  Fix: `trigger_event = { id = exodos.4 }` agregado al cleanup de GG.
- **BUG C corregido (crítico):** GG no llamaba a `exodos_cleanup_effect` al terminar.
  `exodos_gather_global_done` persistía en todas las provincias — segunda ejecución de GG
  terminaba en el primer pulso sin mover ningún pop.
  Fix: `remove_variable` ×2 del cleanup de GG reemplazados por `trigger_event = { id = exodos.4 }` +
  `exodos_cleanup_effect = yes`.
- **Tabla de eventos definitiva:** exodos.1→error Transfer | exodos.2→fin DG | exodos.3→fin OG | exodos.4→fin GG.
- **R19 agregada** a Sección 0.4c del ACTIVE y PROMPT_MAESTRO v3.9: confirmar antes de modificar archivos.
- **Documentación:** ACTIVE limpiado (Sección 19 solo entradas abiertas), historial propagado a ARCHIVE Sección 14.
- **Bug cosmético — desc keys desacopladas de IDs (silent bug):** la mayoría de las decisiones
  mostraban descripción vacía en el panel. El engine busca `<decision_id>_desc` exacto — las claves
  usaban el patrón viejo (`exodos_X_desc`, `bom_X_desc`, etc.) desacoplado del ID numerado.
  Decisiones con desc correcta en v4.3.16: `iram_11_distribute_global_desc`,
  `iram_12_constructor_auto_desc`, `iram_13_activate_optimize_global_desc`, y navegación de menú.
  Todas las demás: desc vacía en juego. Corregido en v5.0 TAREA 3d.
- Zip: `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip`.

# ══════════════════════════════════════════════════════════

---

# SECCIÓN 18 — DECISIONES DE DISEÑO DESCARTADAS
# ══════════════════════════════════════════════════════════

**Propósito:** evitar que una IA futura re-proponga alternativas ya evaluadas y descartadas.
Las decisiones marcadas CERRADO no se reabren salvo pedido explícito del usuario.

## 18.1 Exodos — descartadas

- **Slave Distributor** (descartado 2026-05-25): Optimize Global cubre la función. El engine convierte pops libres excedentes a slaves según thresholds de producción sin intervención del jugador. Implementar un Slave Distributor separado era redundante.

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

## 18.5 Arquitectura monolítica v4.3.16 — snapshot pre-split modular

**Propósito:** documentar el estado arquitectónico de v4.3.16 antes de la migración a 4 mods independientes (v5.0). Referencia para entender decisiones del split.

### H3-a — `exodos_cleanup_effect` acoplado a `iram_cleanup_demografia`

En v4.3.16, el scripted effect `exodos_cleanup_effect` (en `exodos/common/scripted_effects/exodos_scripted_effects.txt`) llamaba internamente a `iram_cleanup_demografia = yes`. Esto acoplaba el cancel de EXODOS con el reset completo de demografía — cancelar una operación Gather Global también reseteaba los modifiers de Migración/Ascenso/Descenso Forzado.

En v5.0 el acoplamiento se rompe: `iram_cleanup_exodos` (EXODOS) e `iram_cleanup_bom` (BOM) son scripted effects independientes en mods independientes. El cancel de uno no afecta al otro.

### H3-b — Decisiones BOM/IHA sin guard de menú

En v4.3.16, las decisiones `iram_31_bom_confirm` hasta `iram_35_iha_fill_the_void` eran visibles directamente en el panel de decisiones de IR2 (sin submenú político). La única condición de visibilidad era el cumplimiento de condiciones de rival en `potential`.

En v5.0 pasan a estar gateadas por `iram_bom_menu_bom` — solo aparecen cuando el jugador abre el submenú "Acciones Políticas" dentro del menú BOM.

### H3-c — `iram_cleanup_menu` monolítico (5 variables)

En v4.3.16, un único scripted effect limpiaba 5 variables de menú:
```pdxscript
iram_cleanup_menu = {
    remove_variable = iram_menu_open
    remove_variable = iram_menu_management_open
    remove_variable = iram_menu_behavior_open
    remove_variable = iram_menu_political_open
    remove_variable = iram_rival_heir_open
}
```

En v5.0 se descompone en dos effects independientes:
- `iram_cleanup_exodos_menu` — limpia `iram_exodos_menu` (1 variable, mod exodos)
- `iram_cleanup_bom_menu` — limpia 5 variables BOM (mod by_other_means)

### Referencia

Archivo fuente de referencia: `exodos/common/scripted_effects/exodos_scripted_effects.txt` en `mod_pack_IRAM_v4_3_16_2026-05-30_03-14.zip`.
Documentado: 2026-06-05 19:33 (sesión correcciones 4 y 5) + 2026-06-05 19:54 (auditoría).

---

# ══════════════════════════════════════════════════════════

---

# ══════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════
# SECCIÓN 19b (ARCHIVE) — LOG DE SESIONES v4.3.16 → v5.0
# Movido desde ACTIVE v3.10 — 2026-06-09 03:47
# Cubre el ciclo de decisiones que llevó de v4.3.16 a v5.0
# ══════════════════════════════════════════════════════════

## 2026-06-05 19:54 — Auditoría del zip + unificación del plan v5.0

### ✅ Cerrado

- **ERROR A — Desc keys desacopladas:** bug preexistente en v4.3.16 confirmado contra el zip.
  Todas las decisiones excepto DG, Constructor, OG y navegación de menú mostraban
  descripción vacía en juego. Corregido en TAREA 3d del plan unificado.

- **ERROR B — Bug BOM doble en TAREA 3c:** script Python del SESSION_LOG ESPECIAL generaba
  BOM doble. Corregido: usar `encoding="utf-8-sig"` en la escritura, no manipular BOM a mano.

- **ERROR C — Detección parcial en TAREA 3c:** usar `k + ':'` en startswith, no `k` solo.

- **ERROR D — Orden del sed en TAREA 3b:** documentado como obligatorio. Comentario añadido.

- **TAREA 3d agregada:** fix desc keys en yml. Ver tabla completa en SESSION_LOG 2026-06-05 19:54.

- **TAREA 3e (renumeración de ex-TAREA 3c):** claves huérfanas usan nombres post-TAREA 3c.
  orphaned_keys en el script deben tener prefijo `iram_` (no `exodos_`).

- **Cancel verificado en zip:** ya era siempre visible en v4.3.16. Sin cambio de comportamiento.

- **Plan unificado:** plan de ejecución canónico consolidado en PARTE 3 del log 2026-06-05 19:54.
  Reemplaza los planes de SESSION_LOG 03:33 y SESSION_LOG ESPECIAL 19:33.

### ❓ Quedó abierto

- Ejecución completa de v5.0.
- Fix desc keys de demografía: verificación manual del yml fuente requerida (TAREA 10).

### ⚠️ Premisas activas

- Caveat `\n\n` en localizaciones — verificar en testeo.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Compatibilidad savegame: clean break — jugador ejecuta cancel_all antes de actualizar.

---

## 2026-06-05 19:33 — Auditoría crítica plan v5.0 (correcciones 4 y 5)

### ✅ Cerrado

- **P1 — TAREA 3b agregada:** sed global para variables de menú con prefijo iram_
  no capturadas por TAREA 3. iram_menu_management_open → iram_exodos_menu, etc.

- **P2 — Límites on_action corregidos:** Bloque 2: 687–1117 (no 686–1119).

- **P3 — Cancel siempre visible:** ambos cancel usan potential = { is_ai = no } sin guard.
  iram_bom_active mantiene rol de variable trazable sin gatear ninguna decisión.
  Única excepción RD1 vigente: iram_exodos_confirm_transfer (iram_transfer_pending).

- **P4 — Strings menú BOM definidas:** inglés y español, completas.
  Ver SESSION_LOG_ESPECIAL correcciones_4_5 2026-06-05 19:33.

- **P5 — Ego sum reset en cancel: intencional.** No agregar excepción en cleanup.

- **P6 — R3 verificada contra zip.** Confirmado: activate_transfer sí setea transfer_pending.
  Wiki estaba equivocado. SESSION_LOG 03:33 §1.5 es la versión correcta.

- **H1 — TAREA 3c agregada:** eliminar 9 pares de strings huérfanos de operaciones por área
  (gather/distribute/optimize legacy v2/v3) de los yml.

- **H2 — Bug desc keys v4.3.16 documentado:** cosmético, no requiere corrección,
  decisiones eliminadas en TAREA 9.3. Documentar en ARCHIVE.

- **H3 — Deuda arquitectónica documentada:** snapshot pre-split para ARCHIVE.

### ❓ Quedó abierto

- Ejecución completa de v5.0.

### ⚠️ Premisas activas

- Caveat \n\n en localizaciones — verificar en testeo.
- valor_rp = 0.023223 — sin verificar, no bloquea código.

---

## 2026-06-04 03:33 — Diseño completo v5.0: arquitectura modular, IDs, RD1, ego sum

### ✅ Cerrado

- **Arquitectura modular v5.0:** 4 mods independientes. exodos, by_other_means, the_great_leap,
  the_last_vote. Cada uno con menú, decisiones, localizaciones y cancel propios.
  Carpetas raíz y .mod intocables.

- **Versión v5.0:** quiebre arquitectónico completo — split de mods + tercer rename de IDs +
  rewrite de menús + RD1 universal + ego sum + iram_bom_active.

- **RD1:** potential solo contiene is_ai + variable de menú. Allow contiene todas las condiciones
  de juego con custom_tooltip. Excepciones documentadas: cancel_all y confirm_transfer (estado operacional).

- **Armonización de IDs:** prefijos por mod — iram_exodos_, iram_bom_, iram_tgl_, iram_tlv_.
  Tabla completa en SESSION_LOG 2026-06-04 03:33.

- **R3 corregida:** Transfer SÍ usa iram_transfer_pending. R3 era incorrecto. Wiki Sección 3.6
  tenía error (decía "eliminada" para exodos_transfer_pending).

- **iram_bom_active:** variable agregadora para trazabilidad de estado BOM.
  Seteada por: 4 decisiones demo + 4 ego sum. Limpiada por iram_cleanup_bom.

- **Ego sum mecánica:** una por gobernante (iram_bom_ego_gobernante_used en scope ruler) +
  una por dios por partida (iram_bom_ego_X_used de país). Cancel BOM resetea todo.

- **Split on_action → 4 archivos:** RE11 documentada. Plan técnico en SESSION_LOG 2026-06-03 02:01.

- **Stubs de costos:** mantener costos comentados hasta post-testeo.

### ❓ Quedó abierto

- Ejecución de v5.0 (código + wiki + PROMPT_MAESTRO).
- Testeo exhaustivo post-ejecución.

### ⚠️ Premisas activas

- Caveat `\n\n` en localizaciones — verificar en testeo.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Compatibilidad savegame: clean break — jugador ejecuta cancel_all antes de actualizar.

---

## 2026-06-03 01:40 — Calibración DG, cierre operaciones por área, protocolo Ascenso/Descenso

### ✅ Cerrado

- **Calibración DG — counts 4/9/14 definitivos:** R1 = 4, R2 = 9, R3 = 14 pops/pulso/territorio.

- **Operaciones por área — removidas intencionalmente:** deliberadamente reemplazadas por GG/DG/OG.

### ❓ Quedó abierto

- Protocolo de testeo Ascenso/Descenso Forzado. Modifier actúa como multiplicador del umbral.
  Criterio: cambio de tipo de pop visible ≤12 meses → ✅ / no visible → rediseñar.

### ⚠️ Premisas activas

- Caveat `\n\n` — verificar en testeo.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.

---

## 2026-06-03 01:09 — Limpieza de secciones stale (Sec 3.3, 4, 5, costos)

### ✅ Cerrado

- **Sec 3.3 — IDs tabla:** nota de advertencia "pendiente de codear" y 22 filas "⏳" actualizadas
  a ✅ IMPLEMENTADO. El refactor de IDs iram_01–iram_25 está completo en zip v4.3.16.
- **Sec 4 — comparativa v3 vs v4:** entrada Optimize Global actualizada de "⚠ PENDIENTE diseño"
  a "✅ IMPLEMENTADO v4.3.16".
- **Sec 5 — matriz v1→v4:** fila Optimize Global columna v4 actualizada de "stub, on_action pendiente"
  a "✅ IMPLEMENTADO v4.3.16".
- **Tabla de costos:** fila Optimize Global — removida referencia a `has_variable = exodos_gather_global_completed`
  (guard descartado en sesión 00:38, faltaba limpiar de esta tabla).

### ⚠️ Premisas activas sin cambios

Sin novedades. Ver Sección 19.0.

---

## 2026-06-03 00:38 — Auditoría zip v4.3.16 vs wiki + cierre de pendientes pre-testeo

### ✅ Decidido

- **Auditoría zip v4.3.16:** el zip está más avanzado que la wiki en tres funciones.
  DG (Distribute Global on_action), OG (Optimize Global on_action) y Constructor Automático (`iram_12`)
  estaban completamente implementados en zip v4.3.16. La wiki los tenía como PENDIENTE.
  Discrepancia resuelta — wiki actualizada a v3.3.

- **Operaciones por área eliminadas del zip:** `exodos_decisions_gather.txt`, `exodos_decisions_distribute.txt`
  y `exodos_decisions_optimize.txt` no existen en v4.3.16. Las operaciones Gather/Distribute/Optimize
  por área no están en el zip canónico activo. Estaban en v4.3.7. No hay documentación de su remoción
  deliberada — queda abierto como verificación pendiente.

- **Señal GG→OG descartada:** `exodos_gather_global_completed` no se implementa.
  OG y DG son de activación libre — el jugador puede correrlos sin haber hecho GG primero.
  Ambos manejan el caso "no hay pops suficientes" gracefully (skipean el área).
  Consistente con "el ecosistema habilita, no castiga."

- **Variables descartadas:** `exodos_gather_global_completed` y `exodos_optimize_global_distribute_active`
  no se implementan. `exodos_optimize_global_done` ya estaba en cleanup. Las "3 variables pendientes"
  quedan cerradas.

- **Fix Gather legacy cerrado:** la operación Gather por área no existe en zip v4.3.16.
  No hay código que fixear.

- **Git:** commit inicial confirmado como hecho antes de esta sesión.

### ⚠️ Premisas activas sin cambios

- Ascenso/Descenso Forzado — threshold sin testear.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.
- Caveat `\n\n` en localizaciones — verificar en testeo en juego.
- Calibración números Distribute Global (5/10/15) — post-testeo.
- Operaciones por área — verificar si remoción fue intencional.

---

## 2026-05-30 03:14 — Auditoría de código + fixes GG/DG/OG + documentación v4.3.16

### ✅ Decidido

- **v4.3.16 implementado:** fixes de tres bugs en eventos de completado GG/DG/OG.

  **BUG A — exodos.2 nombre incorrecto para DG:**
  exodos.2 decía "Optimize Global" pero era disparado tanto por DG como por OG.
  Fix: exodos.2 → DG (locs renombradas), exodos.3 → OG (nuevo), exodos.4 → GG (nuevo).

  **BUG B — GG sin notificación de completado:**
  GG terminaba silenciosamente. Fix: `trigger_event = { id = exodos.4 }` en cleanup de GG.

  **BUG C — GG segunda ejecución rota (crítico):**
  GG no llamaba a `exodos_cleanup_effect` al terminar. `exodos_gather_global_done` persistía
  en todas las provincias. Segunda ejecución terminaba en el primer pulso sin mover ningún pop.
  Fix: reemplazar los dos `remove_variable` del cleanup de GG por `trigger_event = { id = exodos.4 }`
  + `exodos_cleanup_effect = yes`.

- **Tabla de eventos de completado definitiva:**
  exodos.1 → error Transfer | exodos.2 → fin DG | exodos.3 → fin OG | exodos.4 → fin GG

- **R19 agregada** a Sección 0.4c y PROMPT_MAESTRO: antes de modificar cualquier archivo,
  describir el cambio en una oración y esperar confirmación del operador. Sin excepción.
  Diagnóstico: la regla existía en Plantilla A del PROMPT pero sin número ni color — la IA
  la trataba como contexto, no como regla operativa.

- **Documentación propagada al ARCHIVE:** historial v4.3.2 → v4.3.16 agregado a Sección 14.
  Sección 19 del ACTIVE limpiada — solo entradas abiertas.

### ⚠️ Premisas activas sin cambios

- Ascenso/Descenso Forzado — threshold sin testear.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.

---

## 2026-05-29 05:49 — Fix ciudades secundarias Gather Global + textos \n\n

### ✅ Decidido

- Bug ciudades secundarias en Gather Global: CERRADO — fix codeado en v4.3.11.
- Textos iram_10/11/12/13 (ES + EN): CERRADO — estructura \n\n + línea de ciudades secundarias.
- Caveat if/else en script_value: CERRADO — confirmado en _script_values.info del game.zip.

### ⚠️ Premisas activas sin cambios

- Ascenso/Descenso Forzado — threshold sin testear.
- `valor_rp = 0.023223` — sin verificar, no bloquea código.

---

# ══════════════════════════════════════════════════════════

# SECCIÓN 19 (ARCHIVE) — LOG DE SESIONES PRE-v4
# ══════════════════════════════════════════════════════════

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

## STRATEGIC LOG — 2026-05-27 (Charla 11) — Perfil del operador y visión

*Registrado desde IRAM_STRATEGIC_LOG_2026-05-27_11.md — sesión de revisión estratégica del proyecto.*

### Perfil del operador

- Experiencia previa en EU4 modding con events llamados por consola — domina scopes, effects, triggers básicos.
- Las soluciones arquitectónicas más difíciles de IRAM (spawn de unidades v1, scope global v3, workaround de rivales v2) fueron diseñadas por el operador, no por la IA. La IA no pudo resolver esos problemas.
- IRAM confirma transferencia de habilidades a un nuevo engine (IR 2.0.4), no aprendizaje desde cero.
- Objetivo real: ciencia de datos — el modding es el camino ameno hacia coding y data science.
- Recién arrancando curso formal de datos al momento de esta sesión.
- Usa IA deliberadamente para saltear boilerplate y mecánica fina — no para evitar el trabajo difícil.
- El modelo económico (Sección 17) y los simuladores de Optimize fueron trabajo cuantitativo real — modelado y simulación aplicados.

### Mapa de aprendizaje — skills de IT desarrolladas en IRAM

**Ya desarrolladas (confirmadas en esta charla):**

| Skill | Evidencia |
|---|---|
| Pensamiento computacional | Soluciones arquitectónicas propias que la IA no pudo resolver |
| Diseño de sistemas | Arquitectura del menú navegable, flujo de operaciones, estados |
| Modelado cuantitativo | Modelo económico v4, simuladores de Optimize |
| Documentación técnica profesional | TECHNICAL_WIKI = living spec con ADRs, historial, estado |
| AI collaboration | PROMPT_MAESTRO, gestión de contexto, saber qué delegar y qué no |
| Gestión de proyecto | Versionado, sesiones, decisiones documentadas, pendientes |
| Debugging y especificación de bugs | 5 bugs documentados con contexto, causa y verificación |
| Arquitectura de decisiones | Por qué decisions > events para este caso de uso |

**En desarrollo activo:**

| Skill | Vía |
|---|---|
| Python | Curso de datos |
| Análisis de datos / data science | Curso de datos |
| Lectura y escritura de código fino | IRAM + práctica deliberada |

**Próximas:**

| Skill | Cuándo |
|---|---|
| Git + GitHub | Antes o durante cierre de IRAM |
| Terminal básica | Con Git |
| VS Code | Con Git |
| SQL | Durante curso de datos |
| Visualización de datos | Durante curso de datos |

**Conexión directa con data science:**
- Modelado económico IRAM → modelado estadístico
- Simuladores de Optimize → simulación y análisis de sensibilidad
- Gestión de contexto con IA → AI-assisted data analysis (patrón estándar en DS moderno)
- Documentación reproducible → reproducibilidad en notebooks y pipelines

---


# ══════════════════════════════════════════════════════════
# SECCIÓN LEGACY v4 — CONTENIDO MOVIDO DESDE ACTIVE v3.6
# Movido: 2026-06-08 19:27 | Razón: superado por v5.0/v5.1
# ══════════════════════════════════════════════════════════

Este bloque contiene el diseño y código de referencia de IRAM v4 que fue reemplazado
en v5.0. Se preserva para consulta histórica y como fuente de reconstrucción si fuera necesario.

---

## LEGACY 4.1 — Concentrate (Gather por área) — v4

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


---

## LEGACY 4.2 — Distribute por área — v4

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


---

## LEGACY 4.4 — Optimize por área (4 rangos) — v4

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

---

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

---

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

---

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

**Pasos post-cierre — estado 2026-06-03:**

| Paso | Tarea | Estado |
|---|---|---|
| A | Verificar sistema nuevo (TECHNICAL_WIKI v3.3 + zip v4.3.16 + PROMPT v3.9) | ⚠ PENDIENTE — testeo exhaustivo en partida |
| B | Git — commit inicial | ✅ CERRADO — commit hecho antes de 2026-06-03 |
| C | No reconstruir historial Git artificialmente — el TECHNICAL_WIKI ya documenta el *por qué* | ✅ CERRADO |
| D | Borrar archivos viejos solo después de verificar sistema nuevo en Git | ⚠ Post-testeo |

**Archivos sin cambios — copiar tal cual desde v3:**
`exodos_decisions_rival_heir.txt`, `exodos_decisions_bom.txt`, `exodos_decisions_bom_ego_sum.txt`,
`exodos_decisions_tgl.txt`, `exodos_decisions_tlv.txt`, `exodos_events.txt`, `tlv_events.txt`,
`bom_l_english.yml`, `bom_l_spanish.yml`, `bom_l_english_ego_sum.yml`, `bom_l_spanish_ego_sum.yml`,
`tlv_l_english.yml`, `tlv_l_spanish.yml`, `tgl_l_english.yml`, `tgl_l_spanish.yml`

---


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

---

*Fin del bloque LEGACY v4 — movido desde ACTIVE v3.6 el 2026-06-08*


*IRAM TECHNICAL WIKI ARCHIVE v3.7 — 2026-06-05 20:29*
*Cambios v3.5: U-nuevo-A (bug desc keys v4.3.16 en Sección 14). Sección 18.5 agregada (arquitectura monolítica pre-split: H3-a cleanup acoplado, H3-b BOM sin guard de menú, H3-c cleanup_menu monolítico).*
