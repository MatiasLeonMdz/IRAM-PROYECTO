# IRAM — Hitos Metodológicos
**Generado:** 2026-06-10 15:42 | **Actualizado:** 2026-06-11 13:12 (sesión v6 — cierre gap v4.1→v4.3.16)
**Fuente:** Historial unificado 7448 msgs (5 Claudes) + TECHNICAL_WIKI_ACTIVE v3.10 + TECHNICAL_WIKI_ARCHIVE v3.7 + zip v5.5 + conversations.json CLAUDE_1–5
**Sesión v3:** Nuevo hallazgo sesion_estrategica_2026-05-27; primera_auditoria dividida; mecanismo generador de reglas
**Sesión v4:** Reconstrucción completa v5 desde conversations.json — narrativa causal, mapa versiones, 4 hitos nuevos confirmados
**Sesión v5:** Fusión v3.1 + v4 — documento definitivo. Se incorporan: marco 5D completo, sección fuentes, tabla transiciones, hallazgos nuevos de v3.1, evidencia extendida; se incorporan: hitos período v5, mapa versiones v1→v5.5, de v4.
**Sesión v6 (esta):** Cierre gap v4.1→v4.3.16 desde conversations.json (5 cuentas). Se resuelven: `primera_wiki`, `primera_auditoria_formal`, `sesion_estrategica_2026-05-27` (cuenta exacta). Se agregan: `technical_wiki_split`, `git_init`, `R19_confirm_before_modify`, `RE6_building_names`. Se marca ⚠️ hallazgo cuentas paralelas (modelo de transiciones a revisar). Mapa v4.3 completado.

---

## LEYENDA — ESTADOS

| Símbolo | Significado |
|---------|-------------|
| ✅ | Confirmado con evidencia directa del historial |
| ❌ | Falso positivo — fecha del script incorrecta, real documentada abajo |
| ⚠️ | No verificado en esta sesión (falta buscar en historial) |
| 🔍 | Hallazgo nuevo, no estaba en el checklist original |

---

## MARCO DE ANÁLISIS — 5 DIMENSIONES

Cada hito se documenta con las siguientes dimensiones. Los campos marcados ⚠️ requieren verificación en el `conversations.json`.

### Dimensión 1 — Autoría
Quién tuvo la iniciativa o resolvió el problema central.
- **Operador** — el usuario diseñó o descubrió la solución; Claude implementó
- **Claude** — la IA propuso la solución; el usuario la adoptó o rechazó
- **Colaborativo** — el resultado emergió de la interacción; no atribuible a uno solo

### Dimensión 2 — Causalidad
Qué problema concreto existía antes de que apareciera este hito. Responde: "¿por qué fue necesario?"
Formato: *antes hacíamos X → generaba el problema Y → por eso nació Z.*

### Dimensión 3 — Timeline
A cuál de las dos historias paralelas del proyecto pertenece este hito.
- **Mod técnico** — historia de Exodos, BOM, las funciones. Versiones v1→v5.
- **Sistema documentación** — historia de cómo el equipo aprendió a trabajar. Backups, prompts, logs.
- **Ambos** — el hito afecta las dos historias simultáneamente.

### Dimensión 4 — Ciclo de vida
Qué ocurrió con esta práctica en el tiempo.
- **Permanente** — parte del sistema de trabajo independientemente del contexto
- **Temporal/situacional** — se desplegó para un contexto específico; se puede retirar sin romper el sistema
- **Descartado** — se probó y se abandonó; documentar razón

### Dimensión 5 — Transición de cuenta
Si el hito ocurrió en el contexto de una transición entre cuentas (Claude 1→2, etc.) o fue detonado por el límite de contexto de una cuenta. Aplica especialmente al sistema de documentación.

---

## CHECKLIST DE HITOS

---

### [ ] primeros_scripts
**Script detectó:** 2026-04-16 (CLAUDE_1)
**Estado:** ✅ CONFIRMADO

**Autoría:** Colaborativo — el operador construyó el modelo lógico (área→tablero, territorio→casilla, pop→ficha) y encontró la forma de acceder a los archivos `.gui` del juego (el problema técnico que lo desbloqueaba); Claude construyó el primer código real una vez que el modelo estaba pensado.
**Causalidad:** La pregunta fundacional (2026-04-09) no podía ejecutarse sin acceso a los archivos `.gui` del juego. Una vez resuelto el acceso, la primera sesión con código real fue inmediata.
**Timeline:** Mod técnico
**Ciclo de vida:** Permanente — el mod sigue requiriendo scripts.

**Evidencia:**
- Conv "Finding a mod without owning the game" (CLAUDE_1, 18:38–19:01)
- Claude leyó archivos `.gui` del juego real y construyó el primer mod funcional: movimiento de pops con estructura de archivos, GUI, decisiones, eventos.
**Nota:** La conv 6 (2026-04-09) "Redistribución automática de pops" tiene solo 2 mensajes del usuario preguntando si es posible, sin código — no cuenta como primeros_scripts.

---

### [ ] primer_session_log
**Script detectó:** 2026-05-25 (CLAUDE_1)
**Estado:** ✅ CONFIRMADO (con matiz)

**Autoría:** Colaborativo — Claude propuso el formato y el nombre (`IRAM_SESSION_LOG.md`); el operador decidió adoptarlo.
**Causalidad:** El SUPERBACKUP transmitía el estado técnico del mod pero no el estado operativo de la sesión: qué se hizo en la última, qué falta, qué quedó abierto. La IA arrancaba cada sesión con contexto técnico completo pero sin saber "qué pasó ayer". El SESSION_LOG cubrió ese gap.
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente.
**Transición de cuenta:** No fue detonado por una transición, sino por la acumulación de sesiones dentro de CLAUDE_3 — el problema se volvió visible cuando la brecha entre sesiones era larga.

**Evidencia (tres fechas distintas):**
- **Concepto diseñado:** 2026-05-23, CLAUDE_3 — Claude propuso el SESSION_LOG como "backup accesorio del SUPERBACKUP"
- **Primer archivo generado:** 2026-05-25 (CLAUDE_1), `IRAM_SESSION_LOG_2026-05-25_19-07.md`
- **Formalizado en SUPERBACKUP:** 2026-05-26, SUPERBACKUP v2.3 — "SESSION_LOG definido como 4to archivo del sistema de control" (confirmado en TECHNICAL_WIKI_ARCHIVE v3.7, línea 1784)

**Distinción:** 2026-05-23 = diseño del concepto; 2026-05-25 = primera instancia real; 2026-05-26 = formalizado en el sistema.

---

### [ ] primera_wiki
**Script detectó:** 2026-05-28 (CLAUDE_1) — ❌ FALSO POSITIVO PARCIAL
**Estado:** ✅ RESUELTO — definición adoptada: primer documento de referencia técnica del proyecto

**Autoría:** Operador-iniciativa — la necesidad de documentar fue del operador; Claude generó el formato y el contenido.
**Causalidad:** El código y las decisiones de diseño estaban dispersos en el historial de conversaciones. Sin una fuente de verdad centralizada, cada sesión perdía tiempo reconstruyendo contexto. La wiki fue la respuesta a esa fricción.
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente — evolucionó (backup → SUPERBACKUP → TECHNICAL_WIKI) pero nunca se abandonó.

**Evidencia por capa:**

| Capa | Fecha | Evento |
|------|-------|--------|
| Primer documento de referencia técnica | 2026-04-17 (CLAUDE_2) | `exodus_backup_tecnico_v5.md` — primer backup técnico del mod |
| Primer SUPERBACKUP con ese nombre | 2026-05-14 (CLAUDE_4) | `IRAM_SUPERBACKUP_v1_0.md` creado en "Desarrollo y retroalimentación del proyecto" |
| Nombre "TECHNICAL_WIKI" adoptado | 2026-05-27 (CLAUDE_3) | Usuario preguntó "TECHNICAL_WIKI supongo que nombre es el mas comun para este tipo de documento" — confirmado con conversations.json |
| Split ACTIVE/ARCHIVE ejecutado | 2026-05-27 20:28 | SUPERBACKUP v2.6 → TECHNICAL_WIKI ACTIVE v3.0 + ARCHIVE v3.0 (confirmado en ARCHIVE v3.7, línea 1731) |

**Falso positivo detectado:** El script marcó `primera_wiki` en 2026-05-15 CLAUDE_3 porque Claude buscó en `wiki_imperator.txt` (la wiki oficial del juego), no del proyecto.

**Resolución (2026-06-11):** `primera_wiki` = **2026-04-17 (CLAUDE_2), `exodus_backup_tecnico_v5.md`**. El evento de adopción del nombre TECHNICAL_WIKI y el split ACTIVE/ARCHIVE se documentan como hito separado `technical_wiki_split` (ver abajo).

---

### [ ] separacion_active_archive
**Script detectó:** 2026-04-16 (CLAUDE_1) — ❌ FALSO POSITIVO CONFIRMADO
**Estado:** ✅ CONFIRMADO (fecha real)

**Autoría:** Colaborativo — el operador pidió "pensemos en la reestructuración"; Claude propuso el split específico ACTIVE/ARCHIVE; el operador propuso el nombre TECHNICAL_WIKI.
**Causalidad:** El SUPERBACKUP creció hasta 220KB mezclando instrucciones y contexto. Claude no podía priorizar — ignoraba reglas sepultadas en el contexto → repetía bugs documentados. El historial de versiones anteriores (v1/v2/v3) ocupaba espacio de contexto que competía con el trabajo activo. El split separó lo histórico (ARCHIVE) de lo operativo (ACTIVE).
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente.
**Transición de cuenta:** No fue detonado por una transición de cuenta, sino por el crecimiento orgánico del documento.

**Evidencia del falso positivo:**
- La conv "Finding a mod without owning the game" (2026-04-16) no tiene nada que ver con la wiki
- El keyword "archive" se disparó porque Claude mencionó archivos `.bin` del juego

**Fecha real:** 2026-05-27 (CLAUDE_3) — "Prioridades del proyecto: constructor automático o reestructuración"
- Misma sesión donde se adoptó el nombre TECHNICAL_WIKI
- Misma sesión donde se decidió que ARCHIVE contiene v1/v2/v3 + historia; ACTIVE contiene diseño v4 + sesiones activas
- **Confirmado por el ARCHIVE v3.7:** línea 1731 — "TECHNICAL_WIKI v3.0 (split ACTIVE + ARCHIVE) — 2026-05-27 20:28"

---

### [ ] primer_prompt_maestro
**Script detectó:** 2026-04-17 (CLAUDE_3) — ❌ FALSO POSITIVO CONFIRMADO
**Estado:** ✅ CONFIRMADO (fecha real)

**Autoría:** Operador-iniciativa — el operador tuvo la idea de crear un prompt para que otra IA retomara el trabajo; Claude lo generó.
**Causalidad:** CLAUDE_1 llegó a su límite de contexto con ~40 conversaciones sin estructura transferible. El trabajo necesitaba continuar en una cuenta nueva, pero no había ninguna especificación de cómo hacerlo. El backup mezclaba instrucciones y contexto — Claude no podía priorizar reglas sepultadas. El PROMPT_MAESTRO fue el mecanismo para transferir "cómo trabajar" sin depender de que la nueva IA infiriera el proceso.
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente — evolucionó (sin versión → v2.1 → v3.x) pero nunca se abandonó.
**Transición de cuenta:** Detonado directamente por la transición CLAUDE_1 → nueva cuenta. Es el hito de documentación más claramente vinculado a una transición de cuenta.

**Evidencia del falso positivo:**
- La conv de 2026-04-17 CLAUDE_3 marcada tiene **0 mensajes** (vacía, "Greeting" nunca usado)

**Fecha real:** 2026-05-16 (CLAUDE_4 o CLAUDE_1 según cuenta exacta) — "Documentación de proyecto con análisis de versiones" (= conv_45)
- Usuario subió el historial de conversaciones y pidió "dame el prompt adecuado para que otra IA haga esta tarea lo mejor posible"
- Claude creó `IRAM_PROMPT_MAESTRO.md` (primera versión, sin número)
- Evidencia directa: `📄 create_file: /mnt/user-data/outputs/IRAM_PROMPT_MAESTRO.md` en esa sesión
- **Nota:** conv_45 y primer_prompt_maestro son la misma sesión — se habían tratado como dos ítems separados

**Evolución posterior del PROMPT_MAESTRO:**
- v2.1 → 2026-05-20 (CLAUDE_5)
- v3.0 → 2026-05-19 (meta-análisis del sistema de control, confirmado en ARCHIVE v3.7, línea 2243)
- v3.x → 2026-05-23 en adelante
- v5.2 → 2026-06-08 (ajustes post-rework v5)

---

### [ ] primera_auditoria_codigo
**Script detectó:** ~2026-04-18 — ⚠️ FECHA PENDIENTE DE VERIFICAR en conversations.json
**Estado:** ⚠️ FECHA EXACTA PENDIENTE — práctica confirmada. Auditoría formal de v4 confirmada: v4.3.13/14, CLAUDE_1, 2026-05-30.

**Autoría:** Colaborativo — el operador identificó la necesidad de limpiar código antes de versiones canónicas; Claude ejecutó la revisión sistemática.
**Causalidad:** El código se acumulaba entre sesiones sin revisión integral. Los mismos bugs aparecían versión tras versión. El debugging sistemático con Claude permitió identificar patrones recurrentes → esos patrones se convirtieron en reglas del proceso → las reglas se incorporaron al PROMPT_MAESTRO. Este es el **mecanismo generador de reglas** del proyecto.
**Timeline:** Ambos — práctica técnica del mod que alimentó el sistema de documentación.
**Ciclo de vida:** Permanente — se usó en v2, v3, v4, v5. Culmina en la auditoría consolidada v5.5 (35 hallazgos).
**Transición de cuenta:** ⚠️ Verificar si la práctica se intensificó en transiciones de cuenta (momento de mayor riesgo de introducir regresiones).

**Cadena causal completa (confirmada por el operador 2026-06-10):**
```
bug recurrente
      ↓
debugging sistemático con Claude
      ↓
patrón identificado (mismo bug, distintas versiones)
      ↓
regla incorporada al PROMPT_MAESTRO
      ↓
bug deja de aparecer en versiones siguientes
```

**Relevancia para el SKILL.md:** el PROMPT_MAESTRO no fue diseñado top-down — es un documento emergente que creció desde los errores reales. Cada regla tiene un bug detrás. La sección de "patrones de error comunes" del SKILL.md no es un apéndice — es la historia de cómo nació el sistema. Valida R10: "cada regla del PROMPT_MAESTRO es un problema resuelto."

**Mecanismo generador de reglas visible en los SUPERBACKUPs:** las reglas empezaron embebidas en el contexto (backup) y luego migraron al PROMPT_MAESTRO cuando el backup se volvió demasiado grande para que Claude las priorizara. En el backup IRAM v1.5.1 ya existían:
- *"`is_ai = no` va siempre en `potential` Y en `allow`. Sin excepción."*
- *"El cancel particular no existe en IRAM. Solo existe `exodos_cancel_all`."*
- *"Las decisiones marcadas como CERRADO no se reabren."*
Cada una tiene un bug detrás.

**Auditoría formal v4 — confirmada (2026-06-11):**
- **Fecha:** 2026-05-30, CLAUDE_1
- **Sesión:** 'Tarea de sesión con archivos' (82 msgs) → v4.3.13
- **Qué se hizo:** Code review y cleanup de código, análisis de bloat en on_action, fixes de `trigger_event` en DG y OG
- **Resultado del cleanup:** Optimize 34KB → 10KB (visible en delta de versiones)
- **Nota:** Esta es la primera auditoría *formal y sistemática* de v4; la práctica de auditoría existe desde antes

**Evidencia a buscar en conversations.json (deuda residual):**
- Primera sesión donde Claude revisó código sistemáticamente buscando bugs (no arreglando un bug específico)
- Primera vez que un patrón de bug se convirtió en regla explícita

---

### [ ] primera_auditoria_metodologica
**Script detectó:** 2026-04-22 (CLAUDE_5)
**Estado:** ✅ CONFIRMADO

**Autoría:** Operador-iniciativa — el operador pidió explícitamente "busca errores metodologicos"; Claude ejecutó la revisión y encontró los errores.
**Causalidad:** El modelo económico se había construido a lo largo de múltiples sesiones sin revisión integral. La sospecha de inconsistencias llevó al primer uso deliberado de la IA como auditor externo del propio razonamiento — distinto del debugging de código.
**Timeline:** Ambos — auditoría del modelo económico del mod (Sección 17 del ARCHIVE) con metodología de revisión sistemática.
**Ciclo de vida:** Permanente — las auditorías de diseño se convirtieron en práctica regular. El STRATEGIC LOG 2026-05-27 la valida retroactivamente como trabajo cuantitativo real.

**Evidencia:**
- Conv "Análisis de pricing y cálculo de innovaciones" (CLAUDE_5, 05:23–05:25)
- Usuario: "los precios no estan cerrados, revisa la wiki para ver como surge cada valor y **busca errores metodologicos**"
- Claude encontró 2 errores críticos que cambiaban los números del modelo de pricing
- STRATEGIC LOG (ARCHIVE línea 2274): "El modelo económico y los simuladores de Optimize fueron trabajo cuantitativo real — modelado y simulación aplicados."

**Distinción con primera_auditoria_codigo:** la auditoría de código busca bugs en scripts. La auditoría metodológica busca errores en el razonamiento de diseño. Son prácticas distintas con causalidades distintas — la primera alimenta el PROMPT_MAESTRO técnico; la segunda alimenta la práctica de validar decisiones de diseño con la IA.

---

### [ ] sistema_versiones
**Script detectó:** 2026-04-13 (CLAUDE_1) — ❌ FALSO POSITIVO CONFIRMADO
**Estado:** ✅ CONFIRMADO (evolución real documentada; fecha de convención estable precisada por ARCHIVE)

**Autoría:** Colaborativo — la convención evolucionó gradualmente; la formalización de `AAAA-MM-DD_HH-MM` fue documentada por Claude en el SUPERBACKUP pero responde a una necesidad operativa del operador (identificar unívocamente cada zip).
**Causalidad:** Múltiples zips sin naming consistente generaban confusión para identificar qué estado del mod correspondía a qué momento. La convención resolvió el problema de trazabilidad.
**Timeline:** Ambos — aplica tanto al mod (zips canónicos) como al sistema de docs (SESSION_LOG, wiki).
**Ciclo de vida:** Permanente.

**Evidencia del falso positivo:**
- Conv "Consola de Imperator Rome con cheat engine" (2026-04-13) — "La versión actual y final del juego es la 2.0.4 'Augustus'" (versión del juego, no del mod)

**Evolución real — precisada con ARCHIVE v3.7:**

| Fecha | Evento | Fuente |
|-------|--------|--------|
| 2026-04-17 | Primeros nombres versionados: `exodus_v2.zip`, `exodus_v3` | Historial |
| 2026-05-05 | Primer `mod_pack_IRAM_XX.zip` (número incremental, sin vX.X.X) | Historial |
| 2026-05-11 | Aparece "IRAM v1.0" como nombre de versión del mod | Historial |
| ~2026-05-21 | Primer `mod_pack_IRAM_v4_0.zip` (convención vMAYOR_MENOR) | Historial |
| **2026-05-26** | **Convención `AAAA-MM-DD_HH-MM` formalizada** en SUPERBACKUP v2.3 | **ARCHIVE v3.7, línea 1783** |
| **2026-05-27** | **Primer zip con convención completa:** `mod_pack_IRAM_v4_3_7_2026-05-27_17-14.zip` | **ARCHIVE v3.7, línea 1764** |

**Resolución de la ambigüedad:** la convención fue formalizada el **2026-05-26** y aplicada por primera vez el **2026-05-27**. Esas son las fechas canónicas.

---

### 🔍 tres_capas_lenguaje (hito técnico)
**Fecha:** inicio del proyecto (~2026-04-09); identificado como hito en sesión 2026-06-10
**Estado:** ✅ CONFIRMADO — evidencia en SESSION_LOG 2026-06-10 18:58

**Autoría:** Operador — identificó el problema y desarrolló las soluciones tácticas y estructurales.
**Causalidad:**
*El problema:* tres vocabularios incompatibles operando simultáneamente:
- Wiki del juego: terminología propia (diferente al código)
- Código del juego: terminología técnica del engine
- Modelo del proyecto: area, territorio, ficha (diferente a ambas)
Claude no podía sostener la analogía del modelo con consistencia.
*Solución táctica:* "olvidate de que es IR, resolvemos el problema lógico en el contexto del código."
*Solución estructural:* vocabulario técnico específico del proyecto que emergió de cada reencuadre exitoso y se estabilizó como terminología compartida.
*Consecuencia documental:* la wiki propia no era redundante con la wiki del juego — eran documentos de naturaleza diferente. La wiki del juego habla IR. La wiki del proyecto habla el modelo lógico mapeado al código. Explica por qué la wiki propia fue necesaria.
**Timeline:** Ambos — afecta el mod técnico (cómo se diseñó) y el sistema de documentación (por qué fue necesaria la wiki propia).
**Ciclo de vida:** Permanente — el vocabulario técnico del proyecto es parte de todos los documentos.
**Transición de cuenta:** No detonado por transición; presente desde el inicio. La solución táctica emergió de la fricción acumulada en múltiples sesiones.

---

### 🔍 sesion_estrategica_2026-05-27
**Fecha:** 2026-05-27 (CLAUDE_3 — ✅ confirmado con conversations.json 2026-06-11)
**Estado:** ✅ CONFIRMADO — evidencia directa en ARCHIVE v3.7, Sección 19 + conversations.json

**Autoría:** Colaborativo — el operador inició la revisión estratégica; Claude documentó el perfil y la visión reformulada.
**Causalidad:** El proyecto tenía dos narrativas que corrían sin estar explícitamente articuladas: el mod técnico y el aprendizaje del operador. Sin esa articulación, el SKILL.md y la documentación del proceso carecían de norte claro. Esta sesión lo definió.
**Timeline:** Ambos — sesión de revisión técnica (cierre v4, decisiones de arquitectura) y a la vez el momento donde se formaliza el marco de aprendizaje del proyecto.
**Ciclo de vida:** Permanente — la visión reformulada ("El mod exitoso es el entregable. El aprendizaje es el objetivo real.") es el marco de referencia de todo el trabajo posterior, incluyendo el SKILL.md.
**Transición de cuenta:** No fue detonado por transición de cuenta sino por madurez del proyecto — suficiente historia acumulada para hacer un balance estratégico.

**Evidencia directa (ARCHIVE v3.7):**
- Línea 1744: *"Visión reformulada: 'El mod exitoso es el entregable. El aprendizaje es el objetivo real.'"*
- Líneas 2262–2314: STRATEGIC LOG completo — perfil del operador, mapa de skills desarrolladas, conexiones IRAM → DS
- Línea 2271: *"Objetivo real: ciencia de datos — el modding es el camino ameno hacia coding y data science."*
- Línea 2273: *"Usa IA deliberadamente para saltear boilerplate y mecánica fina — no para evitar el trabajo difícil."*

**Contenido documentado en el STRATEGIC LOG:**
- Perfil del operador: experiencia previa EU4, habilidades arquitectónicas propias, inicio de curso de datos
- Mapa de skills desarrolladas: pensamiento computacional, diseño de sistemas, modelado cuantitativo, documentación técnica, AI collaboration, gestión de proyecto, debugging, arquitectura de decisiones
- Skills en desarrollo: Python, análisis de datos, lectura y escritura de código fino
- Conexiones directas IRAM → DS: modelado económico → modelado estadístico; simuladores Optimize → simulación y análisis de sensibilidad; gestión de contexto → AI-assisted data analysis; documentación reproducible → notebooks y pipelines

**Relevancia para el SKILL.md:** esta sesión es la fuente primaria del marco de dos objetivos. El SKILL.md sin referencia a esta sesión pierde su fundamento estratégico.

---

### 🔍 minilogs_por_tarea (R20)
**Fecha:** 2026-06-06 (CLAUDE_3, durante ejecución TAREA 3 de v5.0)
**Estado:** ✅ CONFIRMADO — evidencia directa en conv "Proyecto IRAM" (CLAUDE_3, 2026-06-06)

**Autoría:** Colaborativo — el operador pidió el minilog en .md; Claude propuso el formato estándar `IRAM_MINILOG_TAREA_X_[FECHA]_[HORA].md`; el operador lo adoptó como R20 en el PROMPT_MAESTRO.
**Causalidad:**
*Antes hacíamos X:* el operador recibía el trabajo al final de la sesión como zip único sin registro intermedio.
*Generaba el problema Y:* cuando una sesión se cortaba mid-task, no había forma de saber exactamente qué había cambiado ni qué falta.
*Por eso nació Z:* un minilog por tarea documenta qué se cambió, qué archivos se tocaron, qué quedó pendiente — base del SESSION_LOG final.
**Timeline:** Sistema documentación
**Ciclo de vida:** Temporal/situacional — activado para reworks largos de múltiples TAREAs. No aplica a desarrollo cotidiano.
**Transición de cuenta:** No detonado por transición; detonado por interrupción de sesión durante rework v5.

**Evidencia:** conv "Proyecto IRAM" (CLAUDE_3, 2026-06-06): *"dame el minilog en un .md o como dice el prompt maestro?"* → R20 agregada al PROMPT_MAESTRO v5.2 en la misma sesión.

---

### 🔍 zips_wip_por_tarea (R19)
**Fecha:** 2026-06-06 (CLAUDE_3, misma sesión que minilogs)
**Estado:** ✅ CONFIRMADO

**Autoría:** Operador-iniciativa — el operador preguntó "¿y los archivos por si se corta la sesión?" y luego "¿las tareas 1 y 2 se perdieron entonces?"; Claude propuso y ejecutó el zip WIP post-tarea.
**Causalidad:**
*Antes hacíamos X:* el zip de trabajo vivía solo en memoria del contenedor.
*Generaba el problema Y:* si la sesión se cortaba, todo el trabajo de las TAREAs completadas en esa sesión se perdía.
*Por eso nació Z:* zip WIP descargable después de cada tarea — si la sesión se corta, se retoma desde el último WIP sin pérdida.
**Timeline:** Sistema documentación
**Ciclo de vida:** Temporal/situacional — activado para reworks largos con múltiples TAREAs. No aplica a sesiones de desarrollo normal.
**Transición de cuenta:** No detonado por transición; detonado por corte de sesión durante rework v5.

**Nota sobre FP en v3.1:** el script había detectado "zips_wip" en 2026-05-05 (CLAUDE_1) — conv "Seize no funciona". Pendiente verificar en conversations.json si el concepto existía antes de 2026-06-06 o si es un falso positivo.

**Evidencia:** conv "Proyecto IRAM" (CLAUDE_3, 2026-06-06): *"y los archivos por si se corta la sesion? que paso con los de las sesiones anteriores? no estas siguiendo las instrucciones si se corta la sesion como seguimos?"*

---

### 🔍 session_log_consolidado
**Fecha:** 2026-06-04 02:45 (CLAUDE_4, generado al cierre de la sesión de diseño)
**Estado:** ✅ CONFIRMADO

**Autoría:** Colaborativo — el operador propuso dividir en sesión de diseño + sesión de ejecución; Claude generó el formato del consolidado.
**Causalidad:**
*Antes hacíamos X:* SESSION_LOG con estado + próximos pasos simples.
*Generaba el problema Y:* para reworks complejos (13+ TAREAs con decisiones de diseño interdependientes), el SESSION_LOG simple no era suficiente instrucción para que otra IA ejecutara sin tomar decisiones.
*Por eso nació Z:* SESSION_LOG_CONSOLIDADO de 4 partes: (1) estado de ejecución, (2) decisiones de diseño cerradas, (3) plan canónico con comandos exactos, (4) material de referencia.
**Timeline:** Sistema documentación
**Ciclo de vida:** Temporal/situacional — activado para reworks de gran escala donde la sesión de diseño y la sesión de ejecución están separadas.
**Transición de cuenta:** No detonado por transición; detonado por complejidad del rework v5.

**Evidencia:** conv "Confirmación de cambios" (CLAUDE_4, 2026-06-04): *"¿Te parece [dividir en dos sesiones] o preferís arrancar a codear ahora?" → "Si me parece correcto."*

---

### 🔍 RD1_potential_minimo
**Fecha:** 2026-06-04 (CLAUDE_4, sesión de diseño v5)
**Estado:** ✅ CONFIRMADO

**Autoría:** Operador — decisión de diseño: *"el jugador tiene que tener acceso a la información siempre. para eso están las tooltips."*
**Causalidad:**
*Antes hacíamos X:* `potential` ocultaba decisiones cuando las condiciones no se cumplían.
*Generaba el problema Y:* el jugador no sabía que existían esas funciones ni cuándo podría usarlas.
*Por eso nació Z:* `potential` solo para `is_ai = no` + estado del menú. `allow` con `custom_tooltip` para todas las condiciones. Decisiones siempre visibles.
**Timeline:** Mod técnico
**Ciclo de vida:** Permanente — regla de diseño del mod. Retroactiva: se aplicó al código existente de demografía, ego_sum y otros.
**Transición de cuenta:** No detonado por transición.

---

### 🔍 technical_wiki_split
**Fecha:** 2026-05-27 (CLAUDE_3) — ✅ CONFIRMADO con conversations.json
**Estado:** ✅ CONFIRMADO

**Autoría:** Colaborativo — Claude analizó el SUPERBACKUP v2.5 (4957 líneas) y propuso la reestructuración; Operador eligió el nombre "TECHNICAL_WIKI" y aprobó el split.
**Causalidad:** *Antes hacíamos X:* el SUPERBACKUP crecía sin estructura, mezclando historial v1/v2/v3 con trabajo activo v4. *Generaba el problema Y:* Claude no podía priorizar — el material histórico compitía con el operativo en el contexto. *Por eso nació Z:* split ACTIVE (sesiones v4 + diseño operativo) / ARCHIVE (v1/v2/v3 + historia) + nombre profesional TECHNICAL_WIKI.
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente
**Transición de cuenta:** No detonado por transición — fue una decisión estratégica durante sesión activa de CLAUDE_3.

**Evidencia:**
- Conv 'Prioridades del proyecto: constructor automático o reestructuración' (CLAUDE_3, 2026-05-27, 30 msgs)
- Usuario: "TECHNICAL_WIKI supongo que nombre es el mas comun para este tipo de documento"
- SUPERBACKUP v2.5 → v2.6 en esta sesión → TECHNICAL_WIKI ACTIVE v3.0 + ARCHIVE v3.0
- ARCHIVE v3.7, línea 1731: "TECHNICAL_WIKI v3.0 (split ACTIVE + ARCHIVE) — 2026-05-27 20:28"

**Nota:** este hito es la separación del evento `primera_wiki` (2026-04-17, primer backup) del evento de maduración del sistema (2026-05-27, nombre + split). Son dos hitos distintos en la misma historia.

---

### 🔍 git_init
**Fecha:** 2026-05-28 (CLAUDE_1) — ✅ CONFIRMADO con conversations.json
**Estado:** ✅ CONFIRMADO

**Autoría:** Operador-iniciativa — decisión de versionar con git como backup robusto.
**Causalidad:** *Antes hacíamos X:* los zips canónicos eran el único backup del código. *Generaba el problema Y:* sin control de versiones real no había forma de revertir cambios sin reconstruir desde un zip anterior. *Por eso nació Z:* git init con v4.3.7 como primer commit.
**Timeline:** Mod técnico
**Ciclo de vida:** Permanente
**Transición de cuenta:** No detonado por transición.

**Evidencia:**
- Conv 'Falta bloque PASO 1 del prompt maestro' (CLAUDE_1, 2026-05-28, 46 msgs) → v4.3.8
- `git init` ejecutado con IRAM v4.3.7 como commit inicial
- Mensaje del commit: "Historial completo en TECHNICAL_WIKI Secciones 14 y 19"
- Herramienta: Git Bash → simplificado a GitHub Desktop en sesiones posteriores

---

### 🔍 R19_confirm_before_modify
**Fecha:** 2026-05-30 (CLAUDE_1, sesión 03:14) — ✅ CONFIRMADO con conversations.json
**Estado:** ✅ CONFIRMADO

**Autoría:** Colaborativo — Claude diagnosticó el problema y propuso el texto; Operador lo numeró como R19 y lo incorporó al PROMPT_MAESTRO.
**Causalidad:** *Antes hacíamos X:* Claude ejecutaba múltiples fixes en una sesión sin confirmación intermedia. *Generaba el problema Y:* el operador detectaba cambios no autorizados al revisar el resultado — Claude había modificado 4 archivos sin confirmar cada uno. *Por eso nació Z:* regla explícita numerada: describir el cambio en una oración y esperar confirmación antes de ejecutar. Sin excepción.
**Timeline:** Sistema documentación
**Ciclo de vida:** Permanente
**Transición de cuenta:** No detonado por transición.

**Evidencia:**
- Conv 'ESTADO ACTUAL 30/05' (CLAUDE_1, 2026-05-30, 50 msgs) — sesión de cierre de v4
- Operador preguntó "¿en qué fallan las instrucciones?" tras detectar 4 fixes ejecutados sin confirmación
- Claude diagnosticó que el protocolo estaba en Plantilla A pero no en las reglas numeradas
- Texto exacto: *"Antes de modificar cualquier archivo: describir el cambio en una oración y esperar confirmación explícita del operador. Sin excepción."*

**Relevancia para el SKILL.md:** ejemplo paradigmático del mecanismo generador de reglas (bug → diagnóstico → regla). El bug fue un exceso de iniciativa de Claude, no un error técnico.

---

### 🔍 RE6_building_names_from_source
**Fecha:** 2026-05-27 (CLAUDE_2) — ✅ CONFIRMADO con conversations.json
**Estado:** ✅ CONFIRMADO

**Autoría:** Colaborativo — Operador señaló el error de nomenclatura; Claude propuso la regla.
**Causalidad:** *Antes hacíamos X:* Claude usaba nombres de buildings por inferencia o contexto. *Generaba el problema Y:* `hill_fort` fue usado durante toda una sesión de diseño del constructor automático; el fuerte real en el juego es `fortress_building` — tokens desperdiciados en diseño incorrecto. *Por eso nació Z:* verificar nombre exacto en `common/buildings/00_default.txt` antes de codear o diseñar.
**Timeline:** Mod técnico (pero genera regla de proceso)
**Ciclo de vida:** Permanente
**Transición de cuenta:** No detonado por transición.

**Evidencia:**
- Conv 'Ejecución de tareas pendientes IRAM' (CLAUDE_2, 2026-05-27, 58 msgs) → v4.3.6
- Error: Claude usó `hill_fort` como nombre del fuerte durante todo el diseño de iram_12
- Corrección: el fuerte real es `fortress_building` (en `00_default.txt`)

---

### ⚠️ cuentas_paralelas — HALLAZGO PENDIENTE DE FORMALIZAR
**Fecha del hallazgo:** 2026-06-11 (análisis conversations.json)
**Estado:** ⚠️ REQUIERE REVISIÓN DEL MODELO DE TRANSICIONES

**Descripción:** El análisis de densidad mensual de sesiones IRAM por cuenta muestra que las 5 cuentas trabajaban **simultáneamente**, no de forma secuencial:

```
Mes       C1  C2  C3  C4  C5  TOT
2026-05   11  13   7   8  10   49
2026-06    4   6   6   6   2   24
```

En mayo de 2026, todos los Claudes tenían sesiones IRAM activas. Esto contradice el modelo mental documentado en el PROMPT ("cada cuenta continuaba cuando la anterior llegaba al límite") — la realidad es un sistema distribuido con múltiples contextos parciales en paralelo.

**Implicancias:**
- La sección TRANSICIONES DE CUENTA de este documento asume linealidad — requiere revisión
- El costo de las transiciones (Plantilla D Bloque 2) es más complejo: no son transiciones limpias sino gestión de contextos parciales paralelos
- El SKILL.md debe documentar esto: el riesgo no era solo "perder contexto al cambiar cuenta" sino "fragmentar el contexto entre cuentas activas simultáneamente"

**Qué falta para formalizar:**
- Entender por qué se usaban múltiples cuentas en paralelo (¿límite de tokens por sesión? ¿estrategia deliberada? ¿ambas?)
- Mapear qué tipo de trabajo iba a cada cuenta (¿había especialización?)
- Revisar si el modelo de "transición" aplica o si el modelo correcto es "rotación"

---

Las transiciones entre cuentas fueron los eventos de mayor riesgo del proyecto — potencial pérdida total de contexto. El sistema de documentación existe en gran medida como respuesta a este problema. Cada transición es una prueba de estrés de ese sistema.

| Transición | Fecha aprox. | Estado del sistema en ese momento | Hito metodológico asociado |
|------------|-------------|-----------------------------------|---------------------------|
| Pre-IRAM → CLAUDE_1 | ~2026-04-09 | Sin sistema — solo historial | — |
| CLAUDE_1 agotado | 2026-05-16 | Solo historial de 40 convs exportado | Detonó `primer_prompt_maestro` y `conv_45` |
| → CLAUDE_2 | ⚠️ Fecha exacta pendiente | ⚠️ Estado del sistema pendiente | ⚠️ Pendiente |
| → CLAUDE_3 | ⚠️ Fecha exacta pendiente | ⚠️ Pendiente | ⚠️ Pendiente |
| → CLAUDE_4 | ⚠️ Fecha exacta pendiente | ⚠️ Pendiente | ⚠️ Pendiente |
| → CLAUDE_5 | ⚠️ Fecha exacta pendiente | SUPERBACKUP + PROMPT_MAESTRO v2.1+ | ⚠️ Pendiente |

**Observación clave del ARCHIVE v3.7:** la primera transición bien documentada es la que llevó a conv_45 (2026-05-16). Antes de esa sesión no había PROMPT_MAESTRO — la IA nueva tenía que reconstruir el contexto desde el historial bruto. Esa experiencia generó todo el sistema de control posterior. Es el hito de causalidad más claro del proyecto.

**Qué buscar en conversations.json para completar esta tabla:**
- Primera mención de "nueva cuenta" o "límite de conversaciones" en cada cuenta
- Calidad del contexto disponible al inicio de cada cuenta (¿arrancó con SUPERBACKUP? ¿con qué versión?)
- Cuántas sesiones tomó "ponerse al día" en cada transición

---

## FUENTES DISPONIBLES Y SU VALOR PARA LA DOCUMENTACIÓN

### TECHNICAL_WIKI_ARCHIVE v3.7 (163KB, 3476 líneas)

**Qué tiene:**
- Código fuente completo de v1/v2/v3/v4 (Secciones 8, 8-A, 8-B, 8-C)
- Historial de versiones con cambios por versión (Sección 14)
- Log de sesiones técnicas **desde 2026-05-19** (Secciones 19b y 19) — con fechas exactas y decisiones
- Decisiones descartadas del mod (Sección 18)
- STRATEGIC LOG 2026-05-27 — **la única fuente existente que documenta explícitamente quién hizo qué** (autoría del mod técnico)
- Confirmación de fechas: `separacion_active_archive` (2026-05-27 20:28), `sistema_versiones` (convención formalizada 2026-05-26, primer zip 2026-05-27), `primer_session_log` (SESSION_LOG como 4to archivo del sistema, 2026-05-26)

**Para qué sirve en la documentación:**
- Corroborar y precisar hitos que ya teníamos — no reemplaza el historial de conversaciones
- Fuente primaria sobre autoría técnica (mod) gracias al STRATEGIC LOG
- Resolver ambigüedades de fecha en el periodo 2026-05-19 en adelante
- No sirve para hitos metodológicos anteriores a mayo 2026 ni para WIPs/minilogs

**Qué NO tiene:**
- Ninguna mención de WIPs, minilogs, zips_wip como conceptos
- El periodo 2026-04-09 a 2026-05-14 está muy comprimido (sin fechas exactas)
- Autoría del sistema de documentación (solo del mod técnico)

---

## HALLAZGOS NUEVOS (no estaban en el checklist original)

### 🔍 nombre_IRAM_adoptado
**Fecha de primera mención:** 2026-05-11 (CLAUDE_3 y CLAUDE_5)
- Conv "Diseño de puente actualizado" (CLAUDE_3, 17:40): "Proyecto activo: IRAM v1.0"
- Conv "Ponerse al día" (CLAUDE_5, 18:43): Lista de pendientes incluye "8. nombre IRAM, versión 1.0"

**Confirmación por el usuario:** 2026-05-23 (CLAUDE_3)
- Usuario: "Imperator Rome: Alternative Mechanics"
- Claude: "**Nombre confirmado:** [...] 'IRAM' para abreviar en pantalla"

**Autoría:** Operador — propuesta de Claude en 2026-05-11; decisión explícita del operador el 2026-05-23.

**Nota:** el rename Drago → IRAM no fue cosmético — el operador reconoció que el objeto cambió de categoría: ya no era utilidad personal, ya no era mod de movimiento de pops — era un sistema que cambia cómo funciona el juego. "Exodos" quedó fossilizado en el código — los nombres internos tienen inercia.

---

### 🔍 conv_6_primer_mensaje_IRAM
**Fecha:** 2026-04-09 (CLAUDE_1)
**Autoría:** Operador — pregunta fundacional, sin respuesta registrada de Claude.
**Causalidad:** Origen de todo el proyecto. Sin esta pregunta no existe IRAM.
**Contenido:** 2 mensajes del usuario preguntando si es posible redistribuir pops automáticamente en Imperator Rome. No hay respuesta del asistente en el registro.

---

### 🔍 conv_45_primera_documentacion_sistematica
**Fecha:** 2026-05-16 (CLAUDE_1, 03:23)
**Autoría:** Operador-iniciativa — el operador tomó la decisión de documentar sistemáticamente; Claude ejecutó.
**Causalidad:** CLAUDE_1 llegaba a su límite. El operador tenía 40 conversaciones de historia pero sin estructura para transferirla. Esta sesión fue la respuesta.
**Importancia:** Origen directo del sistema de documentación completo. El SESSION_LOG, la estructura de tres capas, y el PROMPT_MAESTRO formal surgieron de esta sesión. conv_45 y primer_prompt_maestro son el mismo evento.

---

## TABLA RESUMEN — FALSOS POSITIVOS

| Hito | Fecha script | Tipo FP | Fecha real |
|------|-------------|---------|-----------|
| separacion_active_archive | 2026-04-16 | Keyword "archive" en archivos del juego (.bin, .dat) | 2026-05-27 (CLAUDE_3) |
| primer_prompt_maestro | 2026-04-17 | Conversación vacía (0 msgs) | 2026-05-16 |
| sistema_versiones | 2026-04-13 | "versión 2.0.4" = versión del juego, no del mod | 2026-05-26 (formalización) / 2026-05-27 (primera aplicación) |
| primera_wiki | 2026-05-15 | Claude leyó `wiki_imperator.txt` (wiki del juego) | 2026-04-17 (primer backup) / 2026-05-27 (nombre TECHNICAL_WIKI) |
| zips_wip (posible) | 2026-05-05 | "Seize no funciona" — pendiente verificar | 2026-06-06 (confirmado) |

---

## MAPA DE VERSIONES — COMPLETO (v1 a v5.5)

| Versión | Nombre | Cambio definitorio | Fecha | Evidencia |
|---|---|---|---|---|
| v1 | Drago stable | Scope: spawn en capital, war=no | ~2026-04-16 | zip + backup 1.3.5 |
| v2 | Drago alt | Spawn en rival + war=no eliminado | ~2026-05-06 | zip + backup alt 1.3 |
| v3 | IRAM | Optimize + rename + unificación mods | ~2026-05-13 | zip + backup IRAM 1.5.1 |
| v4 | IRAM expansión | Modelo económico, demografía, reliquias | ~2026-05-22 | zip v4.1 + SUPERBACKUP v2.1 |
| v4.3.16 | IRAM expansión | Última v4 — punto de partida de v5 | 2026-05-30 | zip v4.3.16 |
| v5.0 | IRAM final | Modularidad: 4 mods independientes | 2026-06-06 | conversations.json + SESSION_LOGs |
| v5.1 | — | Bugfixes post-testing | 2026-06-08 | conv "IRAM v5.1 testing" |
| v5.2 | — | Más bugfixes + PROMPT_MAESTRO | 2026-06-08 | conv "IRAM v5.2 prompt maestro" |
| v5.3 | — | Bugfix session | 2026-06-09 | MINILOG_BUGFIX |
| v5.4 | — | Fixes adicionales | 2026-06-09 | SESSION_LOG v5.4 |
| v5.5 | IRAM final | Fix .mod versions + wiki cleanup | 2026-06-09 03:22 | SESSION_LOG_v5_5 |

**Salto arquitectónico más grande del proyecto:** v2→v3 en on_action (199 → 896 líneas, 4.5x). Habilitado por el spawn en posición del rival → Optimize fue posible.

---

## QUÉ FALTA

### Hitos pendientes de verificación en conversations.json
- [ ] **Transiciones de cuenta** (CLAUDE_1→2, 2→3, 3→4, 4→5): fechas exactas, estado del sistema en cada transición, mensajes hasta recuperar contexto operativo. Solo CLAUDE_1→conv_45 está documentada.
- [ ] **primera_auditoria_codigo**: fecha exacta (~2026-04-18), primera sesión de debugging sistemático, primera vez que un patrón de bug se convirtió en regla explícita (R10).
- [ ] **primera_wiki**: decidir qué capa define el hito (2026-04-17 vs 2026-05-27).
- [ ] **zips_wip** (posible FP): verificar si el script de 2026-05-05 es FP o si el concepto existía antes de 2026-06-06.
- [ ] **cuenta exacta de sesion_estrategica_2026-05-27** (CLAUDE_3 o CLAUDE_4).
- [ ] Para cada regla del PROMPT_MAESTRO: identificar el bug o problema que la originó (R10).

### Dimensiones pendientes
- [ ] **Autoría del sistema de documentación** — el STRATEGIC LOG cubre autoría del mod técnico, no del sistema de docs. Requiere conversations.json.
- [ ] **Trazabilidad de reglas** — qué bug generó cada regla. Evidencia parcial en ARCHIVE v3.7.

### Plantillas pendientes
- [ ] **Plantilla D**: análisis cuantitativo del proceso — requiere conversations.json. Bloque 0 prioritario: evolución del contexto 5MB→350KB como *interrupted time series* con 4 puntos de corte identificados.
- [ ] **Plantilla B**: análisis de gaps (conocimiento en chats pero no en wiki)
- [ ] **Plantilla C**: construcción del SKILL.md (requiere Plantilla D primero)

---

*IRAM Hitos Metodológicos — actualizado 2026-06-10*
*v1–v3: revisión manual, 4 FPs confirmados, hitos fundacionales*
*v4: reconstrucción v5 completa — narrativa causal, mapa v5.0→v5.5, 4 hitos nuevos confirmados (minilogs, zips_wip, session_log_consolidado, RD1)*
*v5 (esta versión): fusión definitiva v3.1 + v4 — marco 5D completo, sección fuentes, tabla transiciones, hallazgos nuevos, evidencia extendida incorporados*
