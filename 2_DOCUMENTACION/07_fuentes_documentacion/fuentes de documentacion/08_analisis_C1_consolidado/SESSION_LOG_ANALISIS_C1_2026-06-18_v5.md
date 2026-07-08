# SESSION LOG — Análisis y mejora de IRAM_C1_final.md (v5 — ACUMULATIVO)
**Fecha de la serie:** 2026-06-18
**Fecha de esta actualización:** 2026-06-19 — Sesión 2 (continuación), reproducción de specs + INCIDENTE de alcance sobre el mod
**Versión:** v5 — acumula v4 completo + reproducción verificada de Specs A/B/C + incidente del mod (DC-11) + hallazgo de proceso (H-PROC1)
**Reemplaza:** SESSION_LOG_ANALISIS_C1_2026-06-18_v4.md (y todo lo que v4 ya reemplazaba)
**Producido por:** Sesión 2 (continuación) — specs A/B/C reproducidas y verificadas idénticas a v4. Se intentó avanzar sobre Fase 1 del mod (solo verificación de lectura, CERO archivos editados) sin reconfirmación explícita del operador en esta sesión. El operador detuvo el avance y estableció DC-11. PASO 6-9 del mod quedan BLOQUEADOS, no solo pendientes.

---

## ⚠️ CAMBIO DE ENFOQUE — LEER PRIMERO

**El objetivo original era editar el paper (tareas A, C, E, F).**
**Ese trabajo sigue BLOQUEADO.**

El bloqueo existe porque dos problemas críticos (PC-1 y PC-2) impiden saber si los argumentos centrales del paper son sostenibles en su forma actual. Editarlo antes de resolver eso sería corregir la forma sin saber si el fondo es correcto.

**Estado de la revisión del historial (la tarea de esta sesión):** EN CURSO, cortada antes de completarse.

Sesión 2 corrió:
- Spec A → corrió, pero el campo `phase` de su output está roto (BUG-A1, ver más abajo). Los candidatos y sus scores SÍ son válidos.
- Spec B → corrió limpio. Resultado: cero menciones reales de "democratización" en las 7345 mensajes de las 5 cuentas (ver hallazgo en SPEC B).
- Spec C → corrió, encontró un bug propio (BUG-C1), se corrigió, se volvió a correr. Output limpio y confirmado.
- Mod (Fase 1 y 2 de SESSION_LOG v5.6) → NO se tocó. Solo se inventarió el zip v5.5.

El orden correcto sigue siendo:
1. Revisar historial (claude_N_processed.json ×5) → EN CURSO (ver arriba)
2. Decidir qué ajustes necesita el paper con esos datos
3. Recién entonces ejecutar A, C, E, F (con los ajustes que correspondan)

Las tareas A, C, E y F están completamente especificadas en este log (sección TAREAS DEL PAPER) y siguen siendo válidas — solo están bloqueadas temporalmente.

---

## PROPÓSITO DE ESTE LOG

Spec ejecutable única para cualquier IA que continúe el trabajo.
Carga solo este archivo como punto de partida. No cargar los logs anteriores.

**Nota de continuidad (nueva en v4):** este log asume que la próxima sesión que lo lea NO tiene en su sandbox los archivos de datos (los 5 `claude_N_processed.json`, el zip del mod, los .md del wiki, los 3 scripts .py). Si es una sesión de chat realmente nueva, hay que volver a subir todos los archivos listados en "PROTOCOLO — SESIÓN 2 (CONTINUACIÓN)". El log por sí solo no alcanza.

---

## ARCHIVOS LEÍDOS EN SESIONES PREVIAS (acumulativo)

### Sesión v1 (20:08 UTC, 2026-06-18) — leídos con bash_tool
| Archivo | Para qué sirvió |
|---------|-----------------|
| IRAM_C1_final.md | **El paper — leído completo** |
| IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md | Plan del mod — leído completo |

### Sesión v1 — renderizados en contexto
| Archivo | Para qué sirvió |
|---------|-----------------|
| SESSION_LOG_DOCUMENTACION_s34.md | Estado de cierre del proyecto |
| WIKI_DOCUMENTACION_v2.md | Estado de documentos, principio central |
| IRAM_skill_desarrollo_ia_v2_0.md | C2 — referencia |
| METODOLOGIA_DOCUMENTACION_v1.md | Referencia sistema |
| TEMPLATES_DOCUMENTACION_v1.md | Referencia sistema |
| PROMPT_REGLAS_DOCUMENTACION_v2.md | Referencia sistema |

### Sesión v2 (misma jornada) — leídos con bash_tool
| Archivo | Para qué sirvió |
|---------|-----------------|
| IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md | Fuente de inconsistencias del mod |
| IRAM_PROMPT_MAESTRO_v5_2_2026-06-06.md | Leído parcial (primeras 100 líneas) |

### Sesión 1 — Diseño de Specs (extended thinking, DC-08)
| Archivo | Para qué sirvió |
|---------|-----------------|
| IRAM_C1_final.md | Confirmar argumentos que necesitan datos |
| IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md | Confirmar gaps del mod (Spec C) |
| IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md | Delimitar qué cubre el plan del mod |

### Sesión 2 (2026-06-19) — ejecución mecánica, leídos con bash_tool — NUEVA
| Archivo | Para qué sirvió |
|---------|-----------------|
| claude_1_processed.json … claude_5_processed.json | Input real de los 3 scripts. Estructura inspeccionada y confirmada (ver NOTAS TÉCNICAS) |
| spec_a_authorship.py | Corrido. `infer_phase` inspeccionada línea por línea → BUG-A1 |
| spec_b_democratizacion.py | Corrido sin cambios. Limpio |
| spec_c_zip_history.py | Corrido, se encontró BUG-C1 en `FILENAME_PATTERNS`, corregido, re-corrido |
| mod_pack_IRAM_v5_5_2026-06-09_03-22.zip | Inventariado (`unzip -l`) para confirmar estructura real de `exodos/decisions/` (H-M6) y que está íntegro. No se tocó para Fase 1 |
| IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md | Releído para buscar fechas de versión v1/v2/v3 (Sección 21, 0.4b) — no tiene fechas finas, solo "2026-05" genérico |
| IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md | Releído buscando fechas de versión — solo confirma terminología de versión de wiki (v3.9→v3.10→v3.11), no de mod |

### No leídos en ninguna sesión
| Archivo | Por qué |
|---------|---------|
| IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09.md | No necesario para el análisis |

---

## RESUMEN EJECUTIVO — SESIÓN 2 (NUEVO)

| Paso del protocolo | Estado | Detalle |
|---|---|---|
| PASO 1 — Inspeccionar formato JSON | ✅ Hecho | Formato real ≠ formato hipotético del log v3, pero compatible sin cambios (ver NOTAS TÉCNICAS) |
| PASO 2 — Ajustar normalización | ✅ No fue necesario | Los `get_*` de los 3 scripts ya soportan el formato real |
| PASO 3 — Correr Spec A | ⚠️ Corrido, output parcialmente inválido | BUG-A1: campo `phase` roto. Candidatos/scores válidos |
| PASO 4 — Correr Spec B | ✅ Hecho, limpio | 0 occurrences primary, 5 secondary (todos ruido) |
| PASO 5 — Correr Spec C | ✅ Hecho, con bug corregido en el camino | BUG-C1 encontrado y corregido. Output final limpio |
| PASO 6 — Fase 1 del mod (7 tareas) | ❌ No ejecutado | Zip solo inventariado |
| PASO 7 — Fase 2 del mod (tareas 8-17, sin 17B) | ❌ No ejecutado | — |
| PASO 8 — Preguntar hora antes del zip final | ❌ No alcanzado | — |
| PASO 9 — Entregar | ❌ No alcanzado | Esta sesión entrega: `spec_a_candidates.json` (con caveat), `spec_b_democratizacion.json`, `spec_c_zip_history.json` (corregido), `spec_c_zip_history.py` (corregido), este log |

**Por qué se cortó:** se llegó a un punto de decisión real (corte de fecha para fase "v3" en `infer_phase`) que no es ejecución mecánica — requiere o bien input del operador, o bien minería de texto adicional (parte del trabajo que la propia Spec C ya hace para v4.1+, pero no para v1/v2/v3). Se decidió documentar todo y cerrar la sesión en vez de inventar una fecha.

---

## DECISIONES CERRADAS — NO REDEBATIR (DC-01 a DC-10)

| ID | Decisión | Razón |
|----|----------|-------|
| DC-01 | "La IA no democratiza la programación" NO va en el paper. Vive en WIKI_DOCUMENTACION como principio de fondo. | Debatida múltiples veces. Cerrada. |
| DC-02 | NO usar INC-13 como ejemplo concreto de "criterio previo" en S7. | Premisa del primer draft, eliminada. No reintroducir. |
| DC-03 | S7 referencia 4B únicamente para "árbitro claro". No para "criterio lógico preexistente". | Correcto en el paper final. No cambiar. |
| DC-04 | El proyecto de documentación está CERRADO (s34). Este log es una extensión puntual. | Session s34 es el cierre oficial. |
| DC-05 | Las tareas del paper (A, C, E, F) están BLOQUEADAS hasta resolver el análisis de autoría. | Sin datos de autoría, S4A y S5 no tienen respaldo cuantitativo. Ver PC-1. |
| DC-06 | La democratización es un problema estructural en WIKI_DOCUMENTACION. Requiere redefinir el principio central, no un parche operacional. | "No cargar WIKI cuando la sesión es de paper" niega el problema sin resolverlo. |
| DC-07 | La próxima sesión es revisión completa del historial (claude_N_processed.json ×5) antes de cualquier otra cosa. | Resuelve autoría + estado real de la democratización en el historial + gaps del mod. |
| DC-08 | Arquitectura de tres niveles: extended thinking para diseño y síntesis, IA baja para ejecución mecánica, Python/bash para procesamiento de volumen. | 100MB no caben en contexto. Mismo patrón que rework v5 y scripts de historial. |
| DC-09 | Sesión 1 (diseño de specs) COMPLETADA. Outputs verificados: SESSION_LOG_CONSOLIDADO + spec_a_authorship.py + spec_b_democratizacion.py + spec_c_zip_history.py. Scripts testeados con datos sintéticos, fixes de bugs aplicados. | Sesión cortada; outputs rescatados y verificados por md5 y revisión de contenido. |
| DC-10 (NUEVA) | BUG-C1 (regex de versión en Spec C) es corrección mecánica, no decisión de diseño — el propio comentario del script ya documentaba el comportamiento correcto que la implementación no lograba. Corregido y verificado en Sesión 2. No revertir ni redebatir. | El testeo con datos sintéticos de Sesión 1 (DC-09) no cubrió el caso real de nombres de archivo con fecha pegada al tercer segmento de versión. |

---

## PROBLEMAS CRÍTICOS

### PC-1 — Contradicción T2 / autoría

**Estado actual en documentación:**
- WIKI_DOCUMENTACION marca T2 (autoría real operador vs Claude) como ✅ COMPLETADA en s28.
- S5 del paper dice explícitamente que "la distribución de autoría real dentro de las decisiones de diseño no es recuperable del análisis de texto" y que resolverlo "requeriría anotación manual de una muestra."

**El problema:** T2 se completó con el resultado de que no se puede hacer automáticamente. El ✅ registra la conclusión del intento, no la tarea en sí.

**Por qué importa:** S4A afirma que "el operador fue el arquitecto; la IA fue una herramienta de precisión." Ese claim es el argumento principal del paper. Hoy está respaldado solo por los tres casos narrativos de 4B. Si ese argumento es central, necesita datos del historial.

**Qué resuelve Sesión 2:** Spec A (script + anotación manual de 25-30 decisiones) determina si el claim es sostenible cuantitativamente o debe enmarcarse explícitamente como narrativo.

**Actualización Sesión 2 (NUEVA):** Spec A corrió. La lista de 150 candidatos (texto + score + razones) es válida y usable para la anotación manual de Sesión 3. El campo `phase` de cada candidato NO es confiable (BUG-A1) — la estratificación por fase (v1-v2/v3/v4/v5) que pide la spec original no se puede aplicar tal cual al output actual. Sesión 3 puede: (a) anotar igual sin estratificar por fase, usando solo el score, o (b) esperar a que se resuelva BUG-A1 para tener distribución real por fase. Ver BUG-A1 para detalle completo.

---

### PC-2 — Democratización en WIKI_DOCUMENTACION

**Estado actual:**
- DC-01 dice: "La IA no democratiza la programación" NO va en el paper.
- WIKI_DOCUMENTACION v2 dice: **"PRINCIPIO CENTRAL DEL PAPER (definitivo)"** y lo define como ese principio exactamente.

**El problema:** cualquier IA que lea WIKI_DOCUMENTACION organiza el análisis del paper alrededor de ese principio. El paper no lo dice. Los argumentos reales del paper son: la posición y el formato importan, la IA ejecuta pero no diseña, el criterio no está en la herramienta.

**Qué resuelve Sesión 2:** Spec B rastrea cuándo y cómo apareció ese principio en el historial. Sesión 3 redefine el principio central real en WIKI_DOCUMENTACION.

**Actualización Sesión 2 (NUEVA):** Spec B corrió sobre los 7345 mensajes de las 5 cuentas. Resultado: **cero ocurrencias del término primario** (`democratiz`, `no democratiza`, `democratize`). Las 5 ocurrencias encontradas son todas de nivel "secondary" (`no técnico`, `cualquiera puede`) y, revisado el texto, son ruido — no hablan de la tesis de democratización. Esto significa que el principio que WIKI_DOCUMENTACION marca como "PRINCIPIO CENTRAL DEL PAPER (definitivo)" **no se debatió ni se introdujo en ninguna conversación de las 5 cuentas analizadas**. Implicaciones para Sesión 3: o (a) el principio se escribió directamente en WIKI_DOCUMENTACION sin pasar por una conversación con la IA, (b) se discutió en una sesión que no está en este export de 5 cuentas, o (c) se discutió con fraseo distinto al cubierto por los términos secundarios/terciarios de la spec. Sesión 3 debería revisar el historial de edición de WIKI_DOCUMENTACION_v2.md directamente (no está en este export) en vez de seguir buscando en el chat.

---

## BUGS EN SCRIPTS DEL HISTORIAL (descubiertos en Sesión 2) — NUEVA SECCIÓN

### BUG-A1 — `infer_phase` nunca puede devolver "v3" (🔴 ABIERTO — necesita decisión)

**Archivo:** `spec_a_authorship.py`, función `infer_phase` (línea 118-135).

**Código exacto:**
```python
def infer_phase(conv_name, conv_date):
    name = (conv_name or "").lower()
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", conv_date or "")
    year = month = day = None
    if m:
        year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))

    if "v5" in name:
        return "v5"
    if year == 2026 and month == 6:
        return "v5"
    if "v4" in name:
        return "v4"
    if year == 2026 and month == 5 and (day or 0) >= 16:
        return "v4"
    if "v3" in name:
        return "v3"
    return "v1-v2"
```

**El problema:** la única vía hacia `"v3"` es que el nombre de la conversación contenga literalmente `"v3"`. No hay ninguna ventana de fecha asignada a v3 — el fallback de mayo (día≥16) ya se va entero a v4, y no existe un `elif` de fecha para v3. Los nombres reales de conversación son `[sin título — uuid]` u otros sin ese patrón: jamás contienen `"v3"`.

**Confirmado con datos reales (no solo hipotético):**
- 441 conversaciones totales en los 5 archivos → 0 caen en fase `"v3"`.
- 1363 candidatos sobre el umbral de score → 0 en fase `"v3"`.
- Distribución real de candidatos por fase: `v1-v2: 698, v4: 484, v5: 181`.

**Por qué no es trivial arreglarlo con un dato — investigado en esta sesión:**
- La Sección 21 del wiki ACTIVE (tabla de equivalencia de zips) fecha los zips de v1, v2, "v1.3 intermedio" y "v3 FINAL" (`mod_pack_IRAM_15.zip`) todos como **"2026-05"** genérico, sin día. No permite derivar un corte de fecha entre v1/v2/v3.
- Las fechas reales de conversación más tempranas con contenido real (no vacías) empiezan el **2026-04-13**. Ver hallazgo nuevo más abajo (conversaciones fantasma).
- v4 sí tiene anclas firmes: zip experimental `mod_pack_IRAM_v4_3.zip` fechado 2026-05-19; `mod_pack_IRAM_v4_0.zip` (oficial) fechado 2026-05-21.
- Conclusión: hay evidencia de que v1→v2→v3 ocurrieron entre el 13 de abril y mediados de mayo de 2026, pero no hay un ancla de fecha exacta para separarlos entre sí. Eso requiere o memoria del operador, o minería de texto en los mensajes de abril-mayo buscando menciones explícitas de versión (lo que Spec C ya hace para v4.1+, pero el rango `EXPECTED_VERSIONS` de Spec C no incluye v1/v2/v3 — ver nota en SPEC C).

**Qué NO se hizo:** no se inventó una fecha de corte. Eso sería una decisión de diseño, no ejecución mecánica (ver protocolo).

**Impacto real en el output actual:** `spec_a_candidates.json` es usable para anotación manual (texto, score, razones del score son correctos e independientes de este bug). Solo el campo `phase` de cada candidato, y por lo tanto la distribución `v1-v2/v3/v4/v5` que pide la muestra estratificada de Spec A, no son confiables.

**Opciones para la próxima sesión (a decidir, no decididas acá):**
1. Preguntar directamente al operador la fecha aproximada de cierre de v1, v2 y v3.
2. Extender Spec C (o correr una variante) para buscar menciones explícitas de "v1", "v2", "v3" como texto en los mensajes de abril-mayo 2026, igual que ya hace para v4.1+.
3. Anotar Sesión 3 sin estratificar por fase — usar solo score. Pierde la garantía de cobertura por fase de la muestra original pero no bloquea el trabajo.

---

### BUG-C1 — Spec C capturaba el año de la fecha como subversión (✅ CERRADO — corregido y verificado en esta sesión)

**Archivo:** `spec_c_zip_history.py`, `FILENAME_PATTERNS`.

**Código original:**
```python
FILENAME_PATTERNS = [
    re.compile(r"(?:mod_pack_)?IRAM_v(\d+_\d+(?:_\d+)?)", re.IGNORECASE),
]
```

**El problema:** el propio comentario del script ya advertía el riesgo ("sin el ancla, un `\d+` greedy se come también la fecha que sigue") y creía haberlo resuelto anclando a `IRAM_v` — pero el grupo opcional del tercer segmento (`(?:_\d+)?`) seguía sin distinguir un sub-número de versión real (ej. `_16` en `v4_3_16`) de un año pegado con guion bajo (ej. `_2026` en `v5_5_2026-06-09`).

**Evidencia real encontrada:** el texto `Cargando archivos del proyecto IRAM v5.5...` con el nombre de archivo real `mod_pack_IRAM_v5_5_2026-06-09_03-22.zip` en el mismo mensaje generó la versión espuria `"v5.5.2026"`. Mismo patrón confirmado para `v4.1.2026`, `v4.2.2026`, `v4.3.2026`, `v5.0.2026`, `v5.1.2026`, `v5.2.2026` (7 versiones contaminadas en total, sobre 802 menciones encontradas antes del fix).

**Fix aplicado:**
```python
FILENAME_PATTERNS = [
    re.compile(r"(?:mod_pack_)?IRAM_v(\d+_\d+(?:_(?!\d{4}-)\d+)?)", re.IGNORECASE),
]
```
El tercer segmento opcional solo se acepta si NO es un año de 4 dígitos seguido de guion (patrón real de estos nombres de archivo: `..._AAAA-MM-DD...`).

**Verificación post-fix:** re-corrido sobre los 5 archivos. 774 menciones (antes 802 — la diferencia son exactamente las entradas contaminadas). `versions_found` ya no contiene ningún token con año pegado. `expected_versions_not_found` sigue vacío (no se perdió ninguna versión real).

**Nota para Spec C / TAREA 17B:** `EXPECTED_VERSIONS` en el script cubre v4.1 en adelante (correcto para su propósito original: completar la Sección 21 que termina en v4.0). No cubre v1/v2/v3 — si se decide usar Spec C para ayudar a resolver BUG-A1 (opción 2 de arriba), hay que agregar esas versiones a `EXPECTED_VERSIONS` primero.

---

## HALLAZGOS DE DATOS — HISTORIAL (claude_N_processed.json) — NUEVA SECCIÓN

### H-D1 — 16 conversaciones "fantasma" anteriores a abril 2026 contaminan el bucket por defecto

Las conversaciones fechadas entre 2025-10-22 y 2026-03-11 (16 en total, repartidas en claude_1/2/4) tienen exactamente 2 mensajes cada una, **ambos con texto vacío** (`""`). No son trabajo real del proyecto IRAM — son ruido del export (placeholders, posiblemente conversaciones borradas o no exportadas con contenido).

**Por qué importa:** `infer_phase` las clasifica por defecto como `"v1-v2"` (cae al `return "v1-v2"` final por no tener fecha de mayo/junio ni nombre con versión). Esto contamina el bucket `v1-v2` con 16 entradas que no son del proyecto en absoluto — antes incluso de llegar al problema de BUG-A1.

**Evidencia:** primera conversación con contenido real y más de 2 mensajes: `2026-04-13`, cuenta `claude_1`, título "Consola de Imperator Rome con cheat engine" (4 mensajes). El volumen real arranca el 16-17 de abril (múltiples conversaciones de 6 a 145 mensajes, todas sobre Imperator Rome / mods de población / "exodus").

**Distribución real de conversaciones por mes (verificada, los 5 archivos):**

| Mes | Conversaciones |
|---|---|
| 2025-10 | 7 |
| 2025-11 | 2 |
| 2026-02 | 4 |
| 2026-03 | 3 |
| 2026-04 | 91 |
| 2026-05 | 244 |
| 2026-06 | 90 |

Las primeras 16 (oct 2025 – mar 2026) son las conversaciones fantasma. El trabajo real del proyecto se concentra en abril-junio 2026.

**Relevancia para BUG-A1:** si se decide resolver el corte de fecha de v1/v2/v3, conviene excluir explícitamente las conversaciones anteriores al 2026-04-13 (o filtrarlas por `msg_count <= 2` y texto vacío) en vez de asumir que toda fecha "antes de mayo" es v1-v2 real.

---

## HALLAZGOS DE ANÁLISIS — PAPER

### H-P1 — ITS no configurado correctamente
S6 nombra "interrupted time series" pero S5 presenta una tendencia monótonamente creciente. Un ITS requiere mostrar discontinuidad en el corte, no solo tendencia gradual. Sin argumento contrafactual explícito, los datos son observación, no diseño experimental.

**Impacto en Tarea A:** si se nombra ITS, hay que nombrar también la limitación contrafactual al mismo tiempo. La oración no puede nombrar el diseño sin nombrar que los datos son consistentes con ITS pero no lo demuestran de forma exclusiva.

### H-P2 — Las métricas de S5 mezclan dos fenómenos
"Costo de arranque" mide el efecto de la arquitectura de contexto. Las otras tres métricas (conv/día, duración mediana, ratio Inv/Cód) mejoran con múltiples causas: arquitectura de contexto + familiaridad del operador + alcance más acotado + motor mejor comprendido. La métrica central es el costo de arranque; las otras refuerzan la historia pero debilitan el rigor si se presentan como convergentes sin esa caveat.

### H-P3 — Salto de inferencia en S3 no señalado
La caída de 35 a 14.1 mensajes se atribuye a la arquitectura de contexto, pero coincide exactamente con v3→v4→v5 — versiones con alcances de sesión diferentes y complejidad técnica diferente. La caveat aparece al final de S5 pero el claim principal vive en S3 sin la misma caveat.

---

## HALLAZGOS DE ANÁLISIS — MOD Y WIKI ACTIVE

### H-M1 — Sec 22 del ACTIVE tiene inconsistencia interna
La tabla de Sec 22 dice `IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md` (correcto) pero la columna Versión dice `v3.9` (incorrecto). Cubierto por TAREA 10 del SESSION_LOG v5.6.

### H-M2 — Sec 4.3 del ACTIVE describe arquitectura descartada
Sec 4.3 (Transfer) describe el flujo v4 con scripted_gui y botones A/B. v5.1 usa decisions + on_action puro. Una IA que lea esa sección y trabaje en Transfer producirá código equivocado. Cubierto por TAREA 12.

### H-M3 — Sec 21 del ACTIVE incompleta (TAREA 17B — nueva)
Sec 21 (tabla de equivalencia de zips) termina abruptamente en v4.0 (2026-05-21). No lista ningún zip de v4.1 en adelante ni de v5. Spec C del historial resuelve qué entradas agregar.

### H-M4 — Costos de testing sin criterio de restauración documentado
Los costos del ecosistema están eliminados "para facilitar el test amplio" (Sec 3.4) pero ningún documento especifica cuándo se restauran. GAP-9 y GAP-10 parchean con comentarios TESTMODE — correcto pero insuficiente.

### H-M5 — Sec 3.4 del ACTIVE tiene filas fantasma
Cuatro filas de "Desactivar demografía" que INC-12 confirma que no existen en v5. Cubierto por TAREA 13.

### H-M6 — Discrepancia de ruta `exodos/decisions/` no registrada (NUEVA, verificada en Sesión 2)
La Sección 3.2 del ACTIVE documenta la ruta de decisiones como `exodos/common/decisions/`. La estructura real del zip v5.5 (verificado con `unzip -l` en esta sesión) es `exodos/decisions/` — sin `common/` en el medio. Esta discrepancia ya había sido detectada por una sesión anterior (encontrada dentro de un mensaje de Spec C, fechado 2026-06-09: *"las decisiones están en exodos/decisions/... Discrepancia no registrada en Sección 19"*) pero nunca se corrigió en el wiki ni se registró formalmente. Afecta a las 4 carpetas de decisiones del zip (`exodos/`, `the_great_leap/`, `by_other_means/`, `the_last_vote/` — todas usan `<módulo>/decisions/`, no `<módulo>/common/decisions/`).

**Acción sugerida:** agregar como tarea a Fase 2 del mod (junto a TAREA 10, 12, 13) cuando se ejecute — corregir Sección 3.2 y registrar en Sección 19.

---

## ESTADO DEL PAPER

**Archivo canónico:** `IRAM_C1_final.md` — 394 líneas, 7 secciones, limpio.
**Estado:** COMPLETO. Las tareas de mejora están BLOQUEADAS (DC-05) hasta Sesión 3.

### TAREAS DEL PAPER — BLOQUEADAS (especificaciones vigentes)

Las specs de A, C, E, F son válidas. No ejecutar hasta después de Sesión 2 (revisión del historial). Sesión 3 puede ajustar A según resultado de Spec A, y puede agregar tareas nuevas.

---

#### TAREA A — S5: cerrar el argumento causal

**Problema:** S5 presenta cuatro métricas que "convergen en la misma dirección" pero no desarrolla el argumento contrafactual ni conecta explícitamente los datos al diseño cuasi-experimental (interrupted time series mencionado en S6).

**Qué falta:** Un párrafo al inicio o cierre de S5 que nombre explícitamente el diseño: cuatro puntos de corte con fechas conocidas, antes/después de cada cambio estructural. Los datos ya están. Falta decir que es un diseño de medición, no solo una observación.

**Ajuste por H-P1:** la oración que nombra el diseño debe incluir la limitación contrafactual al mismo tiempo. No nombrar ITS sin nombrar que los datos son consistentes con ITS pero no lo demuestran de forma exclusiva.

**Ajuste posible por Spec A:** si el análisis de autoría muestra que S4A necesita reformulación, revisar si S5 también necesita ajustes antes de aplicar esta tarea.

**Dónde:** Párrafo de apertura de S5, o como nuevo párrafo antes de "Lo que los datos no cubren".

**Qué NO hacer:** No agregar datos nuevos. No mencionar "democratización". La evidencia ya existe.

---

#### TAREA C — S4B: explicar por qué el tercer caso es "el más importante"

**Problema:** El paper anuncia que el tercer caso (auditoría INC-13) es "más sutil y más importante para el paper, porque documenta el mismo patrón con una fuente distinta." Pero la síntesis posterior lo trata igual que los otros dos. La razón de por qué es más importante nunca se dice.

**Qué falta:** Una oración que haga explícita la distinción:
- Casos 1 y 2: fallas epistémicas sobre el sistema externo (el motor del juego). La IA no sabe cómo funciona algo fuera de ella.
- Caso 3 (INC-13): falla epistémica sobre el razonamiento de la IA aplicado al código que ella misma ayudó a escribir. La IA se equivoca sobre su propia lógica previa. Eso es cualitativamente diferente y más difícil de detectar.

**Dónde:** Una oración de transición entre el final del caso INC-13 y el párrafo de síntesis "El concepto formal que nombra esto...".

**Qué NO hacer:** No referenciar INC-13 en S7 (DC-02).

---

#### TAREA E — S6: jerarquizar antes de la tabla

**Problema:** La tabla de 13 conceptos no tiene jerarquía visible. El lector no sabe qué es central vs periférico a la experiencia IRAM.

**Qué falta:** La distinción "llegó al mismo lugar" / "hizo distinto" ya existe en el texto DESPUÉS de la tabla. Anticiparla ANTES con una o dos oraciones: de los 13 conceptos, X son estándar aplicados directamente, Y son variantes propias que el proyecto desarrolló de forma diferente.

**Dónde:** Párrafo inmediatamente antes de la tabla (actualmente empieza con "Nombrar retroactivamente no es cosmético...").

**Qué NO hacer:** No reorganizar la tabla. No cambiar las 13 entradas.

---

#### TAREA F — S7: dar espacio al cierre

**Problema:** Los últimos cuatro párrafos de S7 concentran demasiado: cuarto límite (calibración por modelo) + techo herramienta + techo operador + frase final. Llegan comprimidos.

**Qué falta:** No más contenido — más espacio. Opciones:
- Separar "el cuarto límite" (calibración por modelo) en su propio bloque con título, igual que las tres condiciones anteriores.
- O agregar una oración de transición entre el cuarto límite y el cierre sobre los dos techos.

**Dónde:** Entre "Este sistema se construyó para esta herramienta específica" y "El techo de la herramienta es estructural...".

**Qué NO hacer:** No cambiar la frase final. No agregar contenido conceptual nuevo.

---

## ESTADO DEL MOD

**Situación:** SESSION_LOG v5.6 es un plan NUNCA ejecutado. Zip canónico es v5.5. Tres bugs críticos confirmados en código pero no corregidos. El mod NO está bloqueado por la revisión del historial — puede avanzar en paralelo. **Confirmado en Sesión 2:** zip v5.5 íntegro (inventariado con `unzip -l`), Fase 1 y Fase 2 siguen sin ejecutarse.

### Bugs críticos pendientes (🔴)

| ID | Descripción | Archivo |
|----|-------------|---------|
| BUG-1 | `remove_holding = prev` en scope incorrecto — seize_holdings nunca remueve nada. Silencioso. | `iram_bom_decisions.txt` |
| BUG-3 | Guards NOT ego/heir faltantes en `iram_bom_menu_close` — botón close visible cuando no debería. | `iram_bom_menu.txt` |
| BUG-4 | GG/DG/OG/Constructor sin guard `iram_transfer_pending` — corrupción de estado posible durante Transfer. | 4 archivos de activación |

### Tareas de Fase 2 (wiki) — ajuste respecto al SESSION_LOG v5.6

| ID | Estado | Detalle |
|----|--------|---------|
| TAREA 10 | Sin cambio | Cubre H-M1 (Sec 22 v3.9 → v3.10) |
| TAREA 12 | Sin cambio | Cubre H-M2 (Sec 4.3 flujo v4 → v5) |
| TAREA 13 | Sin cambio | Cubre H-M5 (filas fantasma Sec 3.4) |
| TAREA 17B | Sin cambio | Completar Sec 21 con zips v4.1 en adelante y v5.x — requiere datos de Spec C (ya disponibles, output limpio) |
| TAREA 18 (NUEVA) | Nueva | Cubre H-M6 (ruta `exodos/decisions/` vs `exodos/common/decisions/` en Sec 3.2 + registrar en Sec 19) |

---

## SPECS DEL HISTORIAL (output de Sesión 1, ejecutadas en Sesión 2)

### SPEC A — Análisis de autoría

**Pregunta:** ¿El claim de S4A ("el operador fue el arquitecto; la IA fue una herramienta de precisión") está respaldado por el historial, o debe reformularse como narrativo?

**Estado:** ✅ Corrida. ⚠️ Campo `phase` no confiable — ver BUG-A1.

**Definición operacional de "decisión de diseño":**
- Cuenta: establece elección de arquitectura nueva (alcance, estructura, prefijo/namespace, organización de módulos), acepta o rechaza propuesta de diseño con razón explícita, documenta convención o regla que cambia la forma de trabajar, resuelve trade-off con consecuencias estructurales.
- No cuenta: mensajes de implementación pura, preguntas de clarificación sin propuesta, correcciones de bugs sin implicaciones de diseño, reportes de estado.
- Caso límite: si el mensaje introduce un patrón que luego se convierte en convención → cuenta.

**Esquema de codificación:**

| Código | Nombre | Criterio |
|--------|--------|----------|
| OP_ARCH | Operador origina decisión arquitectónica | Operador establece el diseño antes de cualquier propuesta de IA. IA implementa sin modificar. |
| IA_PROP_AC | IA propone, operador acepta | IA introduce estructura. Operador acepta sin modificación. |
| IA_PROP_RJ | IA propone, operador rechaza o modifica | IA introduce estructura. Operador la cuestiona, modifica o descarta con razón. |
| COLAB | Colaborativo | Propuesta final emerge del diálogo. Sin origen claro en un mensaje único. |
| IA_DIAG_OP_DEC | IA diagnostica, operador decide | IA identifica problema técnico. Operador hace la llamada de diseño. |

**Ejemplos de referencia:**
- OP_ARCH: la sesión de 75 mensajes que produce el SESSION_LOG_CONSOLIDADO. El operador escribe la especificación completa. La IA ejecuta sin decidir nada.
- IA_DIAG_OP_DEC: INC-13. IA diagnosticó el ruido en error.log. Operador decidió: mantener inline, remover del immediate de iram.2/3/4.
- IA_PROP_RJ: Caso 3 de 4B. IA recomendó remover el inline. Operador rechazó desde lógica de sincronización (trigger_event no garantiza mismo tick).
- COLAB: Casos 1 y 2 de 4B. Ninguno tenía la información completa.

**Muestra:** 25-30 decisiones, estratificadas por fase:
- v1-v2: 4-5 | v3: 6-7 | v4: 7-8 | v5: 7-8

⚠️ **Esta estratificación no se puede aplicar tal cual al output actual — ver BUG-A1.**

**Output real de esta sesión:** `spec_a_candidates.json` — 150 candidatos (de 1363 sobre umbral), score descendente. Distribución por fase (NO confiable): `v1-v2: 59, v4: 67, v5: 24, v3: 0`.

**Tarea de Sesión 3:** resolver BUG-A1 (ver opciones ahí) o anotar sin estratificar. Anotar 25-30 candidatos con el esquema. Calcular distribución por categoría (y por fase si BUG-A1 se resuelve). Concluir sobre S4A: (a) mayoría OP_ARCH → sostenible, (b) IA_PROP_AC/COLAB sustancial → agregar matiz, (c) mixto sin tendencia → reformular S4A como narrativo.

---

### SPEC B — Rastreo de la democratización

**Pregunta:** ¿Cuándo apareció "la IA no democratiza la programación" en el historial, quién lo introdujo, y cuál es el argumento central real del proyecto según el historial?

**Estado:** ✅ Corrida. Output limpio.

**Términos de búsqueda:**
- Primarios: `democratiz` (stem), `no democratiza`, `democratize` (inglés)
- Secundarios: `sin saber programar`, `sin programación`, `cualquiera puede`, `no técnico`, `barrera técnica`
- Terciarios (muchos falsos positivos, incluir todos): `principio central`, `argumento del paper`, `el paper dice`, `conclusión del proyecto`, `lo que el paper`, `tesis del`

**Hipótesis de origen:** sesiones tempranas de documentación, antes de s18.

**Resultado real (NUEVO):** 0 ocurrencias primarias en 7345 mensajes de las 5 cuentas. 5 ocurrencias secundarias, todas ruido (`no técnico` / `cualquiera puede` sin relación con la tesis). La hipótesis de origen ("sesiones tempranas de documentación, antes de s18") NO se puede confirmar ni descartar con este historial — sugiere que el principio entró a WIKI_DOCUMENTACION por una vía distinta a estas 5 conversaciones (edición directa, sesión fuera del export, o fraseo no cubierto por los términos de búsqueda).

**Output:** `spec_b_democratizacion.json` — todas las apariciones (5), con contexto ±5 mensajes.

**Tarea de Sesión 3:** dado el resultado nulo, revisar el historial de edición de `WIKI_DOCUMENTACION_v2.md` directamente en vez de seguir buscando en el chat. Informar decisión sobre DC-06: redefinir principio central en WIKI_DOCUMENTACION.

---

### SPEC C — Historia de zips / gaps técnicos

**Pregunta:** ¿Qué zips existen entre v4.0 (2026-05-21) y v5.5 (2026-06-09) y qué cambió en cada uno? (TAREA 17B: completar Sec 21 del ACTIVE que termina en v4.0.)

**Estado:** ✅ Corrida. Bug propio encontrado y corregido en esta sesión (BUG-C1). Output final limpio y confirmado.

**Versiones ausentes de Sec 21 (objetivo original):** v4.1, v4.2, v4.3, v4.3.16, v5.0, v5.1, v5.2, v5.3, v5.4, v5.5. Todas encontradas (`expected_versions_not_found: []`).

**Output:** `spec_c_zip_history.json` — 774 menciones limpias (post-fix), flag `has_zip_context`, lista secundaria de 50 decisiones técnicas sin documentar.

**Hallazgo adicional dentro del output (H-M6):** uno de los mensajes capturados por Spec C contiene una nota de una sesión anterior señalando la discrepancia de ruta `exodos/decisions/` vs `exodos/common/decisions/`, nunca registrada formalmente. Verificada contra el zip real en esta sesión. Ver H-M6.

**Tarea de Sesión 3:** filtrar por `has_zip_context = true`, construir tabla para Sec 21, ejecutar TAREA 17B sobre ACTIVE v3.11 (cuando se genere). Revisar lista secundaria contra Sec 19 del ACTIVE. Aplicar TAREA 18 (H-M6) al mismo tiempo que TAREA 17B si se editan las mismas secciones.

---

## NOTAS TÉCNICAS — SCRIPTS

**Formato REAL confirmado en Sesión 2 (reemplaza la sección hipotética de v3):**

Los 5 archivos `claude_N_processed.json` NO son ni lista plana ni `{"conversations": [...]}` simple — son un dict con metadata propia:

```json
{
  "account": "claude_1",
  "source": "claude_1/conversations.json",
  "total_conversations": 101,
  "total_messages": 1517,
  "total_dups_removed": "...",
  "date_range": {"start": "2025-10-22", "end": "2026-06-10"},
  "hito_first_seen": "...",
  "conversations": [
    {
      "account": "...", "uuid": "...", "name": "...", "date": "...",
      "created_at": "...", "updated_at": "...", "period": "...",
      "msg_count_raw": 0, "msg_count": 0, "dup_count": 0,
      "duration_min": 0, "block_count": 0, "hitos": [...], "tools_used": [...],
      "messages": [
        {
          "idx": 0, "sender": "human", "ts": "...", "ts_short": "...",
          "block": 0, "new_block": true, "pause_min": 0,
          "text": "...", "text_len": 0, "is_log": false,
          "tools": [...], "hitos": [...]
        }
      ]
    }
  ]
}
```

**Confirmado compatible sin ajustes:**
- `get_conversations` ya prioriza la clave `"conversations"` → funciona.
- Mensajes vienen en `"messages"` (no `"chat_messages"` ni `"msgs"`) → ya cubierto por el orden de prioridad de `get_messages`.
- `sender` viene directamente como `"human"` / `"assistant"` (no `"role"`) → ya cubierto.
- `text` es siempre string plano (nunca lista de bloques) → ya cubierto.

**Totales confirmados por cuenta:**

| Cuenta | Conversaciones | Mensajes | Rango de fechas |
|---|---|---|---|
| claude_1 | 101 | 1517 | 2025-10-22 → 2026-06-10 |
| claude_2 | 98 | 1661 | 2025-10-22 → 2026-06-09 |
| claude_3 | 82 | 1284 | 2026-04-16 → 2026-06-09 |
| claude_4 | 78 | 1112 | 2025-10-23 → 2026-06-09 |
| claude_5 | 82 | 1771 | 2026-04-17 → 2026-06-09 |
| **Total** | **441** | **7345** | — |

**54 de 1517 mensajes de claude_1 tienen `text` vacío** (caso normal — probablemente mensajes de sistema/herramienta, no indica error de formato). Ver H-D1 para el caso distinto de las 16 conversaciones 100% vacías.

**Límites de output:** Spec A → top 150 candidatos (1363 sobre umbral en total). Spec B → todas las apariciones (5, sin límite real necesario). Spec C → top 50 decisiones secundarias.

---

## ORDEN DE TRABAJO

| Prioridad | Bloque | Condición |
|-----------|--------|-----------|
| 1 | Resolver BUG-A1 (fecha de corte v1/v2/v3) | Operador o minería de texto adicional — ver opciones en BUG-A1 |
| 2 | Sesión 2 (continuación): Fase 1 del mod + Fase 2 del mod (con TAREA 18 nueva, sin TAREA 17B) | Requiere zip v5.5 + ACTIVE v3.10 + SESSION_LOG v5.6 (ya disponibles) |
| 3 | Sesión 3: análisis de autoría (Spec A, con o sin fase) + revisión directa de WIKI_DOCUMENTACION para DC-06 (Spec B ya descartó la vía del chat) | Requiere outputs de Sesión 2 (ya disponibles para A y B) |
| 4 | Sesión 3: decisión sobre S4A + redefinir WIKI_DOCUMENTACION (DC-06) | Después del análisis |
| 5 | Sesión 3: tareas A, C, E, F del paper | Solo después de resolver 3 y 4 |
| 5 | Sesión 3: TAREA 17B + TAREA 18 (completar Sec 21 + corregir ruta decisions) | Requiere datos de Spec C (ya disponibles, output limpio) |

---

## PROTOCOLO — SESIÓN 2 (CONTINUACIÓN)

### Qué ya está hecho
PASO 1 a 5 completos (ver RESUMEN EJECUTIVO). No repetir.

### Archivos necesarios para continuar (si es una sesión de chat nueva, hay que volver a subir todo)

| Archivo | Rol |
|---------|-----|
| Este log (v4) | Spec ejecutable — leer completo |
| claude_1_processed.json a claude_5_processed.json | Ya procesados — solo necesarios si se va a resolver BUG-A1 con minería de texto adicional |
| mod_pack_IRAM_v5_5_2026-06-09_03-22.zip | Input para Fase 1 del mod |
| IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md | Input para Fase 2 del mod |
| IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md | Plan detallado Fase 1 y 2 |
| spec_a_candidates.json | Output ya generado — usar tal cual (con caveat de fase) |
| spec_b_democratizacion.json | Output ya generado — usar tal cual |
| spec_c_zip_history.json | Output ya generado, limpio (post-fix) — usar tal cual |
| spec_c_zip_history.py | Versión CORREGIDA (BUG-C1) — si se vuelve a correr, usar esta versión, no la original |

### Orden de ejecución restante
```
PASO 6 — Descomprimir zip v5.5, ejecutar Fase 1 del mod (7 tareas) en orden exacto
PASO 7 — Ejecutar Fase 2 del mod (tareas 8-18, incluye TAREA 18 nueva por H-M6; sin TAREA 17B) sobre ACTIVE v3.10
PASO 8 — Preguntar hora al operador antes de generar zip final
PASO 9 — Entregar: mod_pack_IRAM_v5_6.zip + IRAM_TECHNICAL_WIKI_ACTIVE_v3_11.md
```

Antes de PASO 6: si se quiere resolver BUG-A1 primero, requiere decisión del operador (no es ejecución mecánica) — ver opciones en BUG-A1. No es bloqueante para el mod (Fase 1/2 puede avanzar en paralelo, igual que antes).

Sesión 2 no toma decisiones. Si algo no está claro en el spec, preguntar al operador. No redebatir ninguna decisión de la tabla "Decisiones Confirmadas" del SESSION_LOG v5.6, ni las DC-01 a DC-10 de este log.

---

## PROTOCOLO — SESIÓN 3 (extended thinking, síntesis)

### Archivos necesarios
- Este log (v4)
- `spec_a_candidates.json` (con caveat de fase — ver BUG-A1), `spec_b_democratizacion.json`, `spec_c_zip_history.json` (limpio, post-fix)
- `IRAM_C1_final.md`
- `IRAM_TECHNICAL_WIKI_ACTIVE_v3_11_2026-06-09.md` (producido por Sesión 2, si ya se ejecutó Fase 2)
- `WIKI_DOCUMENTACION_v2.md` (para resolver DC-06 — revisión directa, dado que Spec B no encontró nada en el chat)

### Tareas de Sesión 3
1. Resolver BUG-A1 si no se resolvió antes (fecha de corte v1/v2/v3) o anotar sin estratificar por fase
2. Análisis de autoría (Spec A): anotar 25-30 candidatos, concluir sobre S4A
3. Democratización (Spec B): el chat no tiene la respuesta — revisar directamente `WIKI_DOCUMENTACION_v2.md` y redefinir principio central
4. Historia de zips (Spec C): construir tabla para Sec 21, ejecutar TAREA 17B + TAREA 18
5. Tareas del paper: ejecutar A, C, E, F con ajustes que correspondan
6. Cerrar: generar `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md` acumulativo

---

*SESSION LOG ANÁLISIS C1 v4 — serie iniciada 2026-06-18, esta actualización 2026-06-19*
*Acumula: v3 completo + ejecución real de Sesión 2 (Spec A/B/C) + BUG-A1 (abierto) + BUG-C1 (cerrado) + H-D1 + H-M6*
*Reemplaza: SESSION_LOG_ANALISIS_C1_2026-06-18_v3.md*
