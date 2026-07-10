# IMPERATOR: ROME — ALTERNATIVE MECHANICS MOD PACK
## TECHNICAL WIKI ARCHIVE — v3.0
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

# ══════════════════════════════════════════════════════════

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

*IRAM TECHNICAL WIKI ARCHIVE v3.0 — 2026-05-27 20:28*
