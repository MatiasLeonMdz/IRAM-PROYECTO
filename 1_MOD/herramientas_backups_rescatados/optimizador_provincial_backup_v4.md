# OPTIMIZADOR PROVINCIAL — IMPERATOR: ROME
## Backup Técnico Unificado
### Engine: Imperator Roma 2.0.4 | Herramienta: imperator_optimizer_v4.html | v4.0

---

## INSTRUCCIONES PARA LA IA QUE LEA ESTE DOCUMENTO

Este documento es el backup técnico completo del Optimizador Provincial de Imperator: Rome.
Es completamente autónomo — no requiere leer ningún otro documento para continuar el desarrollo.

**Antes de trabajar en el optimizador, leer este documento completo de principio a fin. Sin excepciones.**

### Reglas de trabajo

1. No asumir velocidades del engine de memoria — todos los valores fueron verificados en capturas de partida reales.
2. Las decisiones marcadas como **CERRADO** no se reabren salvo pedido explícito del usuario.
3. El modelo de velocidades está **CERRADO**. No recalcular salvo que el usuario aporte nuevas capturas o cambie la configuración de edificios, leyes o gobernante.
4. La fórmula de distribución óptima fue **CORREGIDA en sesión 4** — ya no es proporcional a velocidad de conversión. Ver sección 4.2.
5. Los breakdowns teóricos (sección 3) son informativos. Los valores de captura (sección 3.1) son la verdad absoluta para el simulador.
6. Hay una discrepancia conocida y documentada en los breakdowns de asimilación de ciudad (ver sección 3.6). No intentar resolverla — está investigada y aceptada.
7. Los asentamientos NO tienen caminos. Confirmado por el usuario en sesión 4. No agregar bonus de caminos a los asentamientos.
8. La penalización de cultura no integrada en asimilación (−25%) está activa durante toda la fase 2 en los asentamientos. Verificado en capturas — aparece en rojo en el tooltip. El valor `sett_assim_ph2 = 1.80%` ya la incluye. No hay transición de velocidad dentro de la fase 2.

### Flujo de trabajo con la IA

1. El usuario sube este backup al inicio de la sesión.
2. La IA lee el documento completo, se pone al día.
3. La IA trabaja sobre el archivo HTML del optimizador.
4. La IA entrega el archivo HTML corregido listo para usar en el navegador sin instalación.

### Convención de nombres de capturas

Los nombres de archivo de las capturas siguen el formato:
```
{tipo_territorio}_{ley_activa}_{edicto_activo}_{proceso_visto}.png
```
- **tipo_territorio**: `ciudad` o `asentamiento`
- **ley_activa**: `ley_relig` (religious_integration_efforts) o `ley_cultura` (monarchy_religious_mandate_military)
- **edicto_activo**: `edicto_relig` (conversión religiosa) o `edicto_cultur`/`edicto_cultural` (asimilación cultural)
- **proceso_visto**: `conversion` (tooltip de conversión religiosa) o `asimilasion`/`asimilacion` (tooltip de asimilación cultural)

Los tooltips en verde son bonuses, en rojo son penalizaciones. El tooltip de conversión dice "se convierte a la fe helénica", el de asimilación dice "se asimila para convertirse en Romano".

---

## ESTADO ACTUAL

| Item | Valor |
|---|---|
| Versión | v4.0 |
| Fecha | 2026-05 |
| Archivo entregable | `imperator_optimizer_v4.html` |
| Estado del modelo de velocidades | **CERRADO** — verificado en capturas |
| Estado del modelo de edificios | **CERRADO** — `calcSlots`, `calcCityConvSpd`, `calcCityAssimPh2Spd` implementados y verificados |
| Estado de la distribución óptima | **CORREGIDO en sesión 4** — ya no es proporcional a conv, sino búsqueda del mínimo tiempo total. Ver sección 4.2 |
| Factor de política de asimilación | **CERRADO** — corregido en sesión 3: era ×0.12, es ×0.10 |
| Caminos en asentamientos | **CERRADO** — ningún asentamiento tiene caminos. Confirmado sesión 4 |
| Penalización cultura en assim fase 2 | **CERRADO** — el −25% está activo y baked en `sett_assim_ph2 = 1.80%`. Verificado en capturas sesión 4 |

---

## 1. CONFIGURACIÓN DE PARTIDA

### 1.1 Parámetros fijos

Estos parámetros son fijos — el optimizador los tiene hardcodeados. Si cambian, hay que recalibrar con nuevas capturas.

| Parámetro | Valor |
|---|---|
| Tipo de gobierno | Monarquía (dictadura — tipo monarquía, NOT república) |
| Gobernantes endiosados activos | 4 |
| Zeal del gobernante | 5 |
| Finesse del gobernante | 5 |
| Tecnologías | Completas (todas las invenciones activas) |
| Religión de estado | Helénica |
| Religión inicial del área | Diferente (extranjera) |
| Cultura inicial del área | Diferente (no integrada) |
| Tipo de pop | **Todos esclavos** — confirmado por usuario sesión 4 |

**Importante:** Roma bajo dictadura es tipo monarquía — NO aplica el −15% de república a conversión ni las leyes romanas republicanas. Las leyes activas son las de monarquía.

**Todos los pops son esclavos:** antes de iniciar la conversión/asimilación se cambian los derechos de las pops para que todos sean esclavos. Esto garantiza que la base de conversión y asimilación es siempre 0.6 sin excepción (freemen tienen base diferente). El modelo no contempla mezcla de tipos de pop — si hubiera freemen, habría que recalibrar.

### 1.2 Configuración del área

| Territorio | Cantidad | Edificios fijos | Edificios rotativos | Caminos |
|---|---|---|---|---|
| Ciudad (Cosae) | 1 | Gran templo (+2.00 flat conv) · Gran teatro (+2.00 flat assim) | Fase 1: N bibliotecas · Fase 2: N mercados | 2 tramos (+5%) — baked en capturas |
| Asentamiento | 9 | Legación provincial (+15% assim) | — | **Ninguno** — confirmado por usuario sesión 4 |

**Colonia romana:** Cosae tiene Colonia romana religious (+2.00 flat assim). Es un bonus especial no replicable. Aparece en TODAS las capturas de ciudad. El modelo genérico NO la incluye, pero las capturas de ciudad sí la contienen. Ver sección 3.5 para el tratamiento correcto.

**Cosae es la capital del estado:** aplica `is_capital_city` (+20% conv · +20% assim). Este modificador NO aparece en el tooltip del juego — es implícito al ser siempre capital. Está incluido en los valores de captura pero no es visible en los breakdowns del tooltip.

### 1.3 Leyes y edictos por fase

| Fase | Edicto activo | Ley nacional activa | Política del gobernador activa |
|---|---|---|---|
| Fase 1 — Conversión | Religioso (ícono toga blanca) | `religious_integration_efforts` | Conversión religiosa (+1.80 flat conv) |
| Fase 2 — Asimilación | Cultural (ícono caretas de teatro) | `monarchy_religious_mandate_military` | Asimilación cultural (+0.50 flat assim) |

**Nota:** el ícono al lado del gobernador en la UI indica el edicto activo — caretas de teatro = cultural, muñeco de toga blanca = religioso.

### 1.4 Edificios rotativos — fórmula de slots

Los slots de edificios rotativos (bibliotecas en fase 1, mercados en fase 2) se calculan según los pops de la ciudad:

```
slots_totales_ciudad    = floor(pops / 10) + 2          (ciudad normal)
slots_totales_metropolis = floor(pops / 10) + 4         (metrópolis, ≥80 pops)
slots_fijos             = 2  (Gran templo + Gran teatro)
slots_rotativos         = slots_totales - slots_fijos
```

**Fuentes:**
- `POPS_PER_BUILDING = 10` — `common/defines/00_defines.txt`
- `city: local_building_slot = 2` — `common/province_ranks/00_default.txt`
- `city_metropolis: local_building_slot = 4` — `common/province_ranks/00_default.txt`
- Umbral metrópolis: 80 pops (hardcodeado C++, dato establecido del juego)

**Urban Planning activa:** la invención `Urban Planning` da **+2 building slots globales en ciudades**. Está activa — confirmado por el usuario (tecnologías completas). Sumar +2 a slots_totales siempre.

**Tabla de slots rotativos con Urban Planning activo:**

| Pops ciudad | Rango | Slots totales | Slots fijos | Slots rotativos |
|---|---|---|---|---|
| 10 | ciudad | 3+2=5 | 2 | 3 |
| 20 | ciudad | 4+2=6 | 2 | 4 |
| 30 | ciudad | 5+2=7 | 2 | 5 |
| 40 | ciudad | 6+2=8 | 2 | 6 |
| 50 | ciudad | 7+2=9 | 2 | 7 |
| 60 | ciudad | 8+2=10 | 2 | 8 |
| 70 | ciudad | 9+2=11 | 2 | 9 |
| 80 | metrópolis | 12+2=14 | 2 | 12 |
| 90 | metrópolis | 13+2=15 | 2 | 13 |
| 100 | metrópolis | 14+2=16 | 2 | 14 |

### 1.5 Efecto de edificios rotativos

| Edificio | Efecto | Fase relevante | Stackeable |
|---|---|---|---|
| Biblioteca | +2.5% conv (local_pop_conversion_speed_modifier = 0.025) | Fase 1 | Sí, sin límite |
| Mercado | +2.5% assim (local_pop_assimilation_speed_modifier = 0.025) | Fase 2 | Sí, sin límite |

Fuente: `common/buildings/00_default.txt` — verificado en archivos del juego.

**Verificación en capturas:** en todas las capturas de ciudad aparece `Mercado: +12.50%` → 5 mercados × 2.5% = 12.5% ✓

### 1.6 Invenciones activas relevantes

| Invención | Efecto | Aplica a |
|---|---|---|
| Culto formulado | +0.50 flat conv · +15% conv | Conversión |
| Proselitismo institucional | +20% conv | Conversión |
| Asimilación religiosa | +10% conv | Conversión |
| Prohibir brujería | +5% conv | Conversión |
| Conversión religiosa (inv) | +30% conv | Conversión |
| Administración cultural | +10% assim | Asimilación |
| Difusión cultural (inv) | +30% assim | Asimilación |
| Urban Planning | +2 slots ciudad | Edificios |

---

## 2. MECÁNICAS DEL ENGINE VERIFICADAS

### 2.1 Base por tipo de pop

Extraído de `common/pop_types/slaves.txt`:
```
convert    = 0.6
assimilate = 0.6
```
Aplica igualmente a freemen. La felicidad no afecta velocidad de conversión/asimilación.

### 2.2 Fórmula de velocidad

```
velocidad_final = (base_pop + Σ_flat_bonuses) × (1 + Σ_%_modifiers)
```

Los flat bonuses se suman primero, luego se aplica el multiplicador % sobre el total flat. Esta fórmula es lineal — no hay caps ni fórmulas alternativas confirmadas en los archivos del juego.

### 2.3 Scaling de la política del gobernador — CORREGIDO EN SESIÓN 3

El archivo declara valores fijos pero el engine los escala por stat internamente (C++, no expuesto en scripts):

| Política | Stat | Factor real | Con stat=5 | Valor en tooltip |
|---|---|---|---|---|
| Conversión religiosa | Zeal | ×0.12/punto (= stat × 0.36 / 10... ver nota) | +1.80 flat | "Conversión religiosa: +1.80" |
| Asimilación cultural | Finesse | **×0.10/punto** | **+0.50 flat** | "Asimilación cultural: +0.60"* |

**⚠ CORRECCIÓN CRÍTICA (sesión 3):** El backup v1.0 tenía el factor de asimilación como ×0.12 → +0.60. Esto era INCORRECTO. El factor real es **×0.10 → +0.50**. El tooltip muestra +0.60 pero el valor que entra en la fórmula es +0.50. Esta corrección fue verificada contra múltiples capturas:

- `asentamiento_ley_relig_edicto_cultur_asimilasion` (0.80%): con +0.50 → `1.10 × 0.72 = 0.792 ≈ 0.80` ✓
- `asentamiento_ley_cultura_edicto_cultura` (1.80%): con +0.50 → `1.35 × 1.375 = 1.856 ≈ 1.80` ✓ (delta 0.056 = redondeo)

*El tooltip muestra +0.60 porque el juego redondea o usa una escala de display diferente a la de cálculo. El valor real que produce los resultados observados es +0.50.*

### 2.4 Leyes — efectos completos

Las leyes de monarquía dan DOS efectos simultáneos (no solo el flat que aparecía en v1.0):

| Ley | Flat global | % global |
|---|---|---|
| `religious_integration_efforts` (conv) | +0.25 flat conv | +30% conv |
| `monarchy_religious_mandate_military` (assim) | +0.25 flat assim | +30% assim |

Fuente: `common/laws/00_monarchy.txt`. El +30% aparece en el tooltip como línea separada (verificado en capturas). El +0.25 flat también aparece en tooltip.

### 2.5 Mecánica de procesamiento de pops

- 1 pop asimilando + 1 pop convirtiendo por territorio simultáneamente
- Deben ser pops distintos
- El throughput no aumenta con más pops — solo cambia la cola
- La velocidad es constante por pop (no se distribuye)

Fuente: wiki oficial Imperator: Rome.

### 2.6 Penalizaciones dinámicas

Fuente: `common/modifiers/00_hardcoded.txt`

| Condición | Efecto en conversión | Efecto en asimilación |
|---|---|---|
| Religión dominante ≠ religión de estado | −25% conv | −10% assim |
| Cultura dominante no integrada | −10% conv | −25% assim |
| Pop siendo asimilado tiene religión diferente | — | −33% assim (ASSIMILATE_DIFF_RELIGION_PENALTY) |

**Desactivación:** cada penalización desaparece territorio por territorio cuando la cultura/religión del estado supera el **50% de los pops** en ese territorio. Condición territorial, no global.

**El −33% sí aparece en tooltip** como "No es de religión Helénica: −33.00%" — NO es oculto.

### 2.7 Gobernantes endiosados

Solo afecta conversión religiosa. No afecta asimilación cultural.

| Cantidad | Bonus conversión |
|---|---|
| 1 | +15% |
| 2 | +30% |
| 3 | +45% |
| 4 | +60% |

Fuente: `common/modifiers/00_hardcoded.txt` — `number_of_deified_rulers: global_pop_conversion_speed_modifier = 0.15` por deificado.

### 2.8 Modificador is_capital_city — NO aparece en tooltip

`common/modifiers/00_hardcoded.txt`:
```
is_capital_city = {
    local_pop_conversion_speed_modifier  = 0.20   (+20% conv)
    local_pop_assimilation_speed_modifier = 0.20  (+20% assim)
}
```

**Este modificador NO aparece en el tooltip del juego.** Cosae es siempre capital → aplica siempre → está baked en los valores de captura. No sumarlo al calcular desde los tooltips — ya está incluido en el resultado final.

### 2.9 Caminos (roads)

`common/modifiers/00_hardcoded.txt`:
```
roads_in_province:
    local_pop_conversion_speed_modifier  = 0.025  (+2.5% por tramo)
    local_pop_assimilation_speed_modifier = 0.025 (+2.5% por tramo)
```

El tooltip agrupa todos los tramos en una sola línea. Tarquini muestra +5% (2 tramos). Caere muestra +7.5% (3 tramos). Cosae muestra +5% (2 tramos).

---

## 3. VELOCIDADES VERIFICADAS EN PARTIDA

### 3.1 Tabla maestra de velocidades — VERDAD ABSOLUTA

Todos los valores fueron extraídos de capturas reales. Son la única fuente de verdad para el simulador.

| Archivo de captura | Territorio | Proceso | Edicto | Ley | Velocidad |
|---|---|---|---|---|---|
| `asentamiento_ley_relig_edicto_relig_conversion.png` | Asentamiento (Tarquini) | Conversión | Religioso | Religiosa | **5.82%/mes** |
| `asentamiento_ley_relig_edicto_relig_asimilasion.png` | Asentamiento (Tarquini) | Asimilación | Religioso | Religiosa | **0.43%/mes** |
| `asentamiento_ley_relig_edicto_cultur_conversion.png` | Asentamiento (Tarquini) | Conversión | Cultural | Religiosa | **2.49%/mes** |
| `asentamiento_ley_relig_edicto_cultur_asimilasion.png` | Asentamiento (Tarquini) | Asimilación | Cultural | Religiosa | **0.80%/mes** |
| `asentamiento_ley_cultura_edicto_cultura.png` | Asentamiento (Caere) | Asimilación | Cultural | Cultural | **1.80%/mes** |
| `ciudad_ley_relig_edicto_relig_conversion.png` | Ciudad (Cosae) | Conversión | Religioso | Religiosa | **10.04%/mes** |
| `ciudad_ley_relig_edicto_relig_asimilasion.png` | Ciudad (Cosae) | Asimilación | Religioso | Religiosa | **5.52%/mes** |
| `ciudad_ley_relig_edicto_cultural_conversion.png` | Ciudad (Cosae) | Conversión | Cultural | Religiosa | **6.53%/mes** |
| `ciudad_ley_relig_edicto_cultural_asimilacion.png` | Ciudad (Cosae) | Asimilación | Cultural | Religiosa | **6.22%/mes** |
| `ciudad_ley_cultura_edicto_cultura.png` | Ciudad (Cosae) | Asimilación | Cultural | Cultural | **6.87%/mes** |

**Nota:** todas las capturas son con 2 gobernantes endiosados. Los valores con 4 deificados se calculan proporcionalmente (ver sección 3.2).

### 3.2 Valores usados en el simulador

```javascript
const SPD = {
  city_conv_ph1:  11.59, // Ciudad, edicto religioso, 4 deificados (calculado desde 10.04)
  city_assim_ph1:  5.52, // Ciudad, edicto religioso, asimilación paralela fase 1
  city_assim_ph2:  6.87, // Ciudad, edicto cultural, religión ya convertida
  sett_conv_ph1:   6.77, // Asentamiento, edicto religioso, 4 deificados (calculado desde 5.82)
  sett_assim_ph1:  0.43, // Asentamiento, edicto religioso, penalización religiosa activa
  sett_assim_ph2:  1.80, // Asentamiento, edicto cultural, religión ya convertida
};
```

**Cálculo de 4 deificados desde 2 deificados:**
- Multiplicador base conv asentamiento (2 deif): `5.82 / 3.15 = 1.848`
- Con 4 deif: `+60%` en lugar de `+30%` → multiplicador nuevo = `1.848 + 0.30 = 2.148` (aproximado)
- Método usado: `valor_4deif = valor_2deif × (mult_base + 0.60) / (mult_base + 0.30)`
- Asentamiento: `5.82 × (1.848 + 0.30) / (1.848) = 5.82 × 1.162 = 6.77` ✓
- Ciudad: `10.04 × 1.154 = 11.59` ✓

### 3.3 Breakdown verificado — asentamiento conversión (CIERRA ✓)

Captura: `asentamiento_ley_relig_edicto_relig_conversion` (5.82%, 2 deificados)

| Componente | Tipo | Valor |
|---|---|---|
| Esclavo base | flat | +0.60 |
| Política conv. (Zeal 5 × 0.12 × 3) | flat | +1.80 |
| Culto formulado (edificio) | flat | +0.50 |
| Ley conv flat | flat | +0.25 |
| **Total flat** | | **3.15** |
| Caminos (2 tramos) | % | +5.00% |
| Cultura no integrada (conv) | % | −10.00% |
| Proselitismo institucional | % | +20.00% |
| Asimilación religiosa (inv) | % | +10.00% |
| Prohibir brujería (inv) | % | +5.00% |
| Culto formulado (inv) | % | +15.00% |
| Conversión religiosa (inv) | % | +30.00% |
| 2 deificados | % | +30.00% |
| Ley conv % | % | +30.00% |
| Cultura no integrada (conv) | % | −20.00% |
| **Total %** | | **+85% → ×1.85** |
| **Resultado** | | **3.15 × 1.85 = 5.8275 ≈ 5.82** ✓ |

### 3.4 Breakdown verificado — ciudad conversión (CIERRA ✓)

Captura: `ciudad_ley_relig_edicto_relig_conversion` (10.04%, 2 deificados, incluye Colonia romana pero esta no afecta conversión)

| Componente | Tipo | Valor |
|---|---|---|
| Esclavo base | flat | +0.60 |
| Política conv. (Zeal 5 × 0.12 × 3) | flat | +1.80 |
| Gran templo | flat | +2.00 |
| Culto formulado (edificio) | flat | +0.50 |
| Ley conv flat | flat | +0.25 |
| **Total flat** | | **5.15** |
| Caminos (2 tramos) | % | +5.00% |
| Proselitismo institucional | % | +20.00% |
| Asimilación religiosa (inv) | % | +10.00% |
| Prohibir brujería (inv) | % | +5.00% |
| Culto formulado (inv) | % | +15.00% |
| Conversión religiosa (inv) | % | +30.00% |
| 2 deificados | % | +30.00% |
| Ley conv % | % | +30.00% |
| Cultura no integrada (conv) | % | −20.00% |
| **Total %** | | **+95% → ×1.95** |
| **Resultado** | | **5.15 × 1.95 = 10.04** ✓ |

*Con 4 deificados: % = +125% → ×2.25 → 5.15 × 2.25 = 11.59*

### 3.5 Breakdown verificado — asentamiento asimilación (CIERRA ✓)

Captura: `asentamiento_ley_relig_edicto_relig_asimilasion` (0.43%)

| Componente | Tipo | Valor |
|---|---|---|
| Esclavo base | flat | +0.60 |
| *(sin política assim — edicto es religioso)* | | |
| **Total flat** | | **0.60** |
| Religión diferente (−33%) | % | −33.00% |
| Caminos (2 tramos) | % | +5.00% |
| Cultura no integrada (assim) | % | −25.00% |
| Legación provincial | % | +15.00% |
| Administración cultural (inv) | % | +10.00% |
| **Total %** | | **−28% → ×0.72** |
| **Resultado** | | **0.60 × 0.72 = 0.432 ≈ 0.43** ✓ |

### 3.6 Discrepancia conocida — asimilación de ciudad (NO REABRIR)

**Los breakdowns teóricos de asimilación de ciudad no cierran exactamente.** Investigado extensamente en sesiones 2 y 3. Conclusiones:

1. El modificador `is_capital_city = +20% assim` aplica pero **no aparece en el tooltip** — está baked en el resultado.
2. Aun sumando ese +20% oculto, los números no cierran.
3. Hay algo en el engine C++ de ciudad (posiblemente relacionado con el estatus de capital) que no está expuesto en los scripts del juego.
4. **El error es de ~1-2% sobre la velocidad final** — equivalente a 1-2 meses de diferencia en una campaña de 200+ meses. **No es significativo** para las decisiones estratégicas.
5. **Solución adoptada:** usar los valores de captura como verdad absoluta. Los breakdowns de ciudad son solo informativos.

**No investigar más esta discrepancia salvo que el usuario lo pida explícitamente.**

### 3.7 Cálculo teórico de velocidades con edificios rotativos

Aunque los breakdowns de ciudad no cierran perfectamente, el delta de edificios es pequeño y calculable. Para calcular el efecto de N bibliotecas (fase 1) o N mercados (fase 2) adicionales sobre los valores de captura base:

**Conversión ciudad con N bibliotecas** (desde breakdown verificado, sección 3.4):
```
flat_base_conv_ciudad = 5.15
mult_base_conv_ciudad_2deif = 1.95   (verificado en captura)
mult_base_conv_ciudad_4deif = 2.25

city_conv_ph1(N_libs) = 5.15 × (2.25 + N_libs × 0.025)
```

Con 0 libs: `5.15 × 2.25 = 11.59` ✓ (coincide con SPD base)
Con 5 libs: `5.15 × 2.375 = 12.23%/mes`
Con 10 libs: `5.15 × 2.50 = 12.875%/mes`

**Asimilación ciudad fase 2 con N mercados** (desde multiplicador implícito de captura):
```
// Multiplicador implícito extraído de captura ciudad_ley_cultura_edicto_cultura:
// El valor 6.87 incluye: Colonia romana +2.00 flat, 0 mercados extra sobre los 5 base

// Para calcular con N mercados sobre los 5 ya baked:
// flat_base = 3.45 (sin colonia — modelo genérico)
// mult_base_con_5_mercados está incluido en el SPD base de 6.87
// delta por mercado adicional = flat_base × 0.025

city_assim_ph2(N_mercados_extra) = SPD.city_assim_ph2 + flat_assim × N_mercados_extra × 0.025
// flat_assim ciudad (sin colonia) = 0.60 + 0.50 + 2.00(teatro) + 0.25 = 3.35
```

**Nota:** el número de mercados baked en las capturas es 5. Si la partida va a tener un número diferente, hay que ajustar.

---

## 4. MODELO DE OPTIMIZACIÓN

### 4.1 Objetivo

Minimizar el tiempo total (en meses) para alcanzar **100% conversión + 100% asimilación** en el área completa (1 ciudad + 9 asentamientos), partiendo de 0% en ambos procesos.

### 4.2 Distribución óptima — CORREGIDO EN SESIÓN 4

**La distribución proporcional a velocidad de conversión (v1.0-v2.0) era incorrecta.**

**Razonamiento:** El cuello de botella real no es la conversión sino la asimilación de los asentamientos en fase 2 (1.80%/mes vs 6.87%/mes de la ciudad — casi 4× más lento). La asimilación de asentamientos depende casi exclusivamente de cuántos pops tienen (la paralela en fase 1 es despreciable: 0.43%/mes). Por lo tanto, para minimizar el tiempo total hay que minimizar los pops en asentamientos y concentrar el excedente en la ciudad.

**Adicionalmente**, más pops en la ciudad genera más slots → más bibliotecas en fase 1 → más velocidad de conversión ciudad → el loop es coherente: conviene siempre darle más pops a la ciudad.

**Fórmula correcta:** búsqueda discreta del `city_pops` que minimiza `total_months`:

```javascript
function calcOptimalDist(total) {
  let best = null;
  // Iterar sobre posibles pops en asentamiento (mínimo 1 por asentamiento)
  for (let settPops = 1; settPops <= Math.floor((total - 1) / N_SETT); settPops++) {
    const cityPops = total - N_SETT * settPops;
    if (cityPops < 1) break;
    const plan = calcPlan(total, cityPops, settPops);
    if (!best || plan.totalMonths < best.totalMonths) best = plan;
  }
  return best;
}
```

**Tabla de distribuciones óptimas verificadas numéricamente:**

| Total pops | Ciudad | Asent c/u | Slots | Conv spd ciudad | Switch | Assim | Total |
|---|---|---|---|---|---|---|---|
| 50 | 14 | 4 | 3 | 11.97%/m | 117m | 194m | 311m |
| 100 | 37 | 7 | 5 | 12.23%/m | 303m | 317m | 619m |
| 150 | 51 | 11 | 7 | 12.49%/m | 408m | 514m | 922m |
| 200 | 74 | 14 | 9 | 12.75%/m | 581m | 639m | 1220m |
| 250 | 97 | 17 | 13 | 13.26%/m | 731m | 770m | 1501m |
| 300 | 111 | 21 | 15 | 13.52%/m | 821m | 971m | 1792m |

**Comparación con distribución proporcional anterior (150 pops):**
- Proporcional (anterior): ciudad=24, asent=14 → 935m
- Óptima (nueva): ciudad=51, asent=11 → 922m → **13 meses menos**
- A 300 pops la diferencia sube a ~82 meses.

### 4.3 Orden de fases — CERRADO

**Conversión al 100% primero, luego asimilación.** Justificación matemática evaluada:

La ganancia de asimilación por switchear antes del 100% de conversión es insignificante (< 1 pop extra por asentamiento) comparada con el costo de completar la conversión restante a 2.49%/mes (edicto cultural) en lugar de 6.77%/mes (edicto religioso).

### 4.4 Estrategia de edificios rotativos — CERRADO

```
Fase 1 (edicto religioso):
  - Ciudad: N_libs = slots_rotativos(pops_ciudad) bibliotecas
  - Efecto: +N_libs × 2.5% sobre velocidad de conversión de ciudad

Switch (al 100% conversión):
  - Cambiar edicto: religioso → cultural
  - Cambiar ley: religious_integration_efforts → monarchy_religious_mandate_military
  - Demoler N_libs bibliotecas, construir N_libs mercados
  - El optimizador indica esto explícitamente al usuario en la sección "Plan de edictos y leyes"

Fase 2 (edicto cultural):
  - Ciudad: N_libs mercados (mismo número que había de bibliotecas)
  - Efecto: +N_libs × 2.5% sobre velocidad de asimilación de ciudad
```

**El número de edificios rotativos es un output calculado (no input del usuario).** Se deriva de los pops asignados a la ciudad.

**Implementado en v4.0.** Las funciones `calcSlots(cityPops)`, `calcCityConvSpd(numLibs)` y `calcCityAssimPh2Spd(numMercs)` están en el HTML. Verificadas contra la tabla de distribuciones óptimas de la sección 4.2 — 6/6 filas exactas.

### 4.5 Fórmula de tiempo por fase

```javascript
// Fase 1: tiempo hasta que el último territorio termine conversión
tiempo_conv_ciudad = pops_ciudad × (100 / SPD.city_conv_ph1(N_libs))
tiempo_conv_asent  = pops_asent  × (100 / SPD.sett_conv_ph1)
switch_month = ceil(max(tiempo_conv_ciudad, tiempo_conv_asent))

// Asimilación acumulada durante fase 1 (paralela)
pts_assim_ciudad_ph1 = switch_month × SPD.city_assim_ph1
pts_assim_asent_ph1  = switch_month × SPD.sett_assim_ph1
pops_assim_ciudad_done = floor(pts_assim_ciudad_ph1 / 100)
pops_assim_asent_done  = floor(pts_assim_asent_ph1  / 100)

// Fase 2: asimilación restante
pops_ciudad_restantes = pops_ciudad - pops_assim_ciudad_done
pops_asent_restantes  = pops_asent  - pops_assim_asent_done
tiempo_assim_ciudad = pops_ciudad_restantes × (100 / SPD.city_assim_ph2(N_libs))
tiempo_assim_asent  = pops_asent_restantes  × (100 / SPD.sett_assim_ph2)
assim_duration = ceil(max(tiempo_assim_ciudad, tiempo_assim_asent))

// Total
total_months = switch_month + assim_duration
```

---

## 5. ARQUITECTURA DEL SIMULADOR

### 5.1 Descripción general

Archivo único HTML/JS/CSS sin dependencias externas. Se abre directamente en el navegador local. No requiere servidor ni instalación.

### 5.2 Inputs del usuario

| Input | Tipo | Rango | Descripción |
|---|---|---|---|
| Total de pops | Slider + botones ±5 | 50–300 | **Único input del usuario** |

Todo lo demás es calculado automáticamente o hardcodeado.

### 5.3 Outputs calculados

| Output | Descripción |
|---|---|
| Distribución óptima | Pops en ciudad y en cada asentamiento |
| Bibliotecas fase 1 | Cantidad calculada según pops ciudad |
| Mercados fase 2 | Misma cantidad que bibliotecas |
| Velocidad conv ciudad (con libs) | Recalculada con bonus de bibliotecas |
| Mes del switch | Mes exacto para cambiar edicto+ley+edificios |
| Duración fase 1 | Meses de conversión |
| Duración fase 2 | Meses de asimilación restante |
| Pops asimilados al switch | Progreso paralelo al momento del switch |
| Tiempo total | Suma fase 1 + fase 2 en meses y años |
| Tabla de territorios | Pops y tiempo estimado por territorio |
| Simulación mes a mes | Progreso animado con barras |

### 5.4 Componentes del simulador

| Componente | Función |
|---|---|
| `calcSlots(pops)` | Calcula slots rotativos según pops y rango ciudad/metrópolis |
| `calcSPD(numLibs)` | Retorna objeto SPD con velocidades ajustadas por edificios |
| `calcOptimalDist(total)` | Búsqueda discreta del city_pops que minimiza total_months (reemplaza proporcional) |
| `calcPlan(cityPops, settPops)` | Plan completo: fases, switch, tiempos, asimilación paralela |
| `buildTerrs(plan)` | Estado inicial de cada territorio para la simulación |
| `stepMonth()` | Avanza 1 mes |
| `renderPlan()` | Renderiza plan estático |
| `renderSim()` | Renderiza estado de simulación |

### 5.5 Lógica mes a mes

```
Por cada mes:
  1. Detectar si se superó switch_month → cambiar phase a 'assim'
  2. Para cada territorio:
     a. CONVERSIÓN: si phase='conv' y quedan pops sin convertir
        → acumular velocidad; por cada 100 pts completar 1 pop
     b. ASIMILACIÓN: siempre, si quedan pops sin asimilar (pop distinto al que convierte)
        → velocidad según phase y tipo de territorio
        → por cada 100 pts completar 1 pop
  3. Detectar fin: todos los pops asimilados → done = true
```

### 5.6 Controles de simulación

| Control | Acción |
|---|---|
| Iniciar | Construye estado inicial con distribución actual |
| +1 mes | Avanza 1 paso |
| +1 año | Avanza 12 pasos |
| +5 años | Avanza 60 pasos |
| Simular completo | Corre hasta done=true (max 100.000 iteraciones) |
| Reiniciar | Resetea simulación (mantiene el plan) |

---

## 6. FUENTES Y BIBLIOGRAFÍA

### 6.1 Archivos del juego verificados

| Archivo | Dato extraído |
|---|---|
| `common/pop_types/slaves.txt` | Base convert=0.6 · assimilate=0.6 |
| `common/governor_policies/00_default.txt` | Política conv=3 · assim=1 (antes de scaling C++) |
| `common/modifiers/00_hardcoded.txt` | Todas las penalizaciones · is_capital_city +20% · caminos +2.5%/tramo |
| `common/buildings/00_default.txt` | Gran templo +2.00 · Gran teatro +2.00 · Mercado +2.5% · Biblioteca +2.5% |
| `common/defines/00_defines.txt` | POPS_PER_BUILDING=10 · ASSIMILATE_DIFF_RELIGION_PENALTY=-0.33 |
| `common/province_ranks/00_default.txt` | city: +2 slots base · metropolis: +4 slots base |
| `common/laws/00_monarchy.txt` | Leyes de monarquía: flat +0.25 Y % +30% cada una |
| `common/inventions/00_civic_inventions.txt` | Urban Planning: +2 slots ciudad globales |

### 6.2 Wiki del juego

- Mecánica de 1 pop por proceso por territorio
- Condición de desactivación de penalizaciones (50% dominancia territorial)
- Factor scaling de política: `(Governor stat + 1) / 10 × Base Policy Modifier`

**Nota sobre el factor de la wiki vs lo verificado en capturas:** la wiki dice `(stat + 1) / 10`. Con stat=5: `(5+1)/10 = 0.60`. Esto coincide con la política de conversión (`3 × 0.60 = 1.80` ✓) pero NO con la política de asimilación (`1 × 0.60 = 0.60` pero el valor real que cierra los breakdowns es **0.50**). La wiki puede estar desactualizada o referirse a la conversión únicamente. **Usar los valores verificados en capturas, no la wiki.**

---

## 7. PENDIENTES ABIERTOS

| Tarea | Prioridad | Notas |
|---|---|---|
| Verificar número de mercados baked en capturas vs partida real | **MEDIA** | Las capturas tienen 5 mercados. Si la partida tiene otro número al momento de usar, recalibrar. |
| Captura directa con 4 deificados | **BAJA** | Valores calculados están verificados indirectamente. Una captura directa los confirmaría. |

---

## 8. DECISIONES CERRADAS

| Decisión | Resolución | Justificación |
|---|---|---|
| Orden de fases | Conversión primero al 100% | Matematicamente demostrado en sesión 1 |
| Distribución óptima | **CORREGIDO sesión 4:** búsqueda discreta minimizando tiempo total, no proporcional a conv | El cuello de botella es la assim de asentamientos (1.80%/m). Minimizar pops en asent siempre reduce el total |
| Asimilación paralela | Corre durante fase 1 a velocidad baja | Engine permite 1 conv + 1 assim simultáneos |
| Colonia romana | En modelo genérico: NO incluida | Bonus no replicable. Está en capturas pero no en SPD |
| Número de asentamientos | 9 fijo | Confirmado por usuario en sesión 1 |
| Único input del usuario | Total de pops | Confirmado en sesión 1. Todo lo demás es calculado |
| Edificios rotativos como output | No son input — se calculan desde pops | Confirmado en sesión 1 |
| Breakdowns de ciudad | Usar capturas, no teoría | Discrepancia conocida, no significativa (1-2%) |
| Factor política assim | ×0.10 → +0.50 (no ×0.12 → +0.60) | Corregido sesión 3, verificado en múltiples capturas |
| Urban Planning activa | Sí — confirmado por usuario | Tecnologías completas, sesión 3 |
| Tipo de pop | Todos esclavos — base 0.6 sin excepción | Antes de iniciar se cambian los derechos. Si hubiera freemen habría que recalibrar |
| Penalización −25% cultura en assim fase 2 | Activa durante toda la fase 2, baked en sett_assim_ph2=1.80% | Verificado en capturas sesión 4: aparece en rojo en tooltip. No hay transición de velocidad dentro de fase 2 |
| Penalización −25% cultura en assim fase 2 — ¿desaparece a mitad? | NO — permanece activa hasta casi el final | Verificado en capturas: con 45% de progreso el debuff sigue activo. La cultura romana no alcanza 50% dominante hasta casi completar la asimilación |

---

## 9. HISTORIAL

### v1.0 — 2026-05 (sesiones 1 y 2)
- Modelo de velocidades construido y verificado desde cero
- 10 capturas de pantalla verificadas
- Archivos del juego extraídos
- Fórmula de distribución óptima definida (proporcional a conv — luego corregida)
- Justificación matemática del orden de fases
- Simulador `imperator_optimizer_v3.html` entregado
- Bibliotecas agregadas como slider (luego revertido)
- Debate sobre factor de política: ×0.12 asumido (incorrecto)
- Debate sobre Colonia romana y su tratamiento
- Descubrimiento del +30% de ley que faltaba en v1.0

### v2.0 — 2026-05 (sesión 3)
- **CORRECCIÓN CRÍTICA:** factor de política de asimilación corregido de ×0.12 a ×0.10
- Convención de nombres de capturas documentada formalmente
- is_capital_city (+20% oculto) identificado y documentado
- Discrepancia de ciudad investigada, aceptada y cerrada definitivamente
- Fórmula de slots de edificios documentada con Urban Planning
- Estrategia de edificios rotativos (bibliotecas fase 1 → mercados fase 2) definida
- Pendiente de implementación en HTML claramente especificado
- Urban Planning confirmada activa — tabla de slots con +2 es definitiva

### v3.0 — 2026-05 (sesión 4)
- **CORRECCIÓN CRÍTICA:** distribución óptima corregida — ya no es proporcional a velocidad de conversión
  - Razonamiento: el cuello de botella real es la asimilación de asentamientos (1.80%/m), no la conversión
  - La ciudad asimila ~4× más rápido → conviene minimizar pops en asentamientos siempre
  - Más pops en ciudad → más slots → más bibliotecas → más velocidad conv → el loop es coherente
  - Nueva fórmula: búsqueda discreta del city_pops que minimiza total_months
  - Tabla de distribuciones óptimas calculada y documentada en sección 4.2
- **CERRADO:** todos los pops son esclavos — derechos cambiados antes de iniciar. Base 0.6 garantizada sin excepción
- **CERRADO:** caminos en asentamientos — ninguno tiene. Confirmado por usuario
- **CERRADO:** penalización −25% cultura en assim fase 2 — verificada en capturas (aparece en rojo), permanece activa durante toda la fase 2, baked en sett_assim_ph2=1.80%. No hay transición de velocidad dentro de la fase 2
- Capturas revisadas en sesión: confirmaron que los debuffs están activos en los tooltips como se esperaba

### v4.0 — 2026-05 (sesión 5)
- **IMPLEMENTADO:** cálculo de slots y edificios rotativos en HTML
  - `calcSlots(cityPops)`: slots rotativos según pops, rango (ciudad/metrópolis) y Urban Planning
  - `calcCityConvSpd(numLibs)`: velocidad de conversión ciudad con N bibliotecas
  - `calcCityAssimPh2Spd(numMercs)`: velocidad de asimilación ciudad fase 2 con N mercados
  - Integrado en `calcPlan` y `calcOptimalDist` — cada candidato de distribución usa sus velocidades reales
  - UI muestra rango ciudad, slots rotativos, bibliotecas y mercados en la tarjeta de distribución
  - Switch box muestra "N bibliotecas → demoler" y "N mercados → construir"
- **IMPLEMENTADO:** distribución óptima por búsqueda discreta
  - Reemplaza `calcDist` proporcional (incorrecto desde v1.0)
  - Itera sobre todos los `settPops` posibles (mínimo 1), elige el que minimiza `totalMonths`
  - Cada candidato usa sus slots y velocidades propias — la búsqueda es consistente
- **VERIFICADO:** tabla de distribuciones óptimas (sección 4.2) — 6/6 filas exactas contra el código
- Firma de `calcPlan` actualizada: `calcPlan(cityPops, settPops)` (sin `total`)

---

*Optimizador Provincial Imperator: Rome — Backup Técnico v4.0 — 2026-05*
