# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-04 23:44 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-04_23-17.md (queda como archivo histórico, no como insumo a recargar completo)
**Tipo de sesión:** auditoría de continuidad — no se ejecutó ninguna tarea operativa del proyecto (mod, corpus, paper, carpetas). Esta sesión ocurrió en una cuenta distinta a la que venía trabajando, a partir de dos archivos subidos: el ZIP completo del proyecto (`IRAM_PROYECTO3.zip`) y el log `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md`. Se generó este log para transferir el trabajo a una tercera cuenta, arrancando solo con este documento + el mismo ZIP.
**Motivo de esta versión:** auditoría completa de fugas de continuidad entre logs (DR-35, DR-36, DR-37) + regla de consolidación adoptada para prevenir que se repita (DR-38).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

**Nota sobre esta sesión en particular:** no avanzó esa prioridad única — fue una sesión de auditoría hacia atrás (¿qué se perdió en transiciones de log anteriores?), no hacia adelante. Las tareas operativas siguen exactamente donde estaban en `23-17`. Ver sección PRÓXIMAS TAREAS, sin cambios de fondo respecto al log anterior.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-34 de los logs anteriores siguen vigentes sin modificación. No se repiten acá — se citan por ID. Si hace falta el detalle, ir a `SESSION_LOG_REPLANTEO_2026-06-19_2.md` (DR-01 a DR-09), `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (DR-10 a DR-26), `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` (DR-27 a DR-33) y `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` (DR-34).

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión no tocó WIKI_DOCUMENTACION_v2.md ni ningún archivo del proyecto — fue auditoría de lectura sobre los logs mismos, dentro del ZIP.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-35 | **Confirmado: dos tareas de `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` se perdieron en la reescritura de `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md`, sin marcarse resueltas ni descartadas.** Método: comparación ítem por ítem de la sección "PRÓXIMAS TAREAS" de `02-43` contra `17-58` y `23-17`. Resultado: de las 4 tareas de `02-43` (tarea 0 con dos sub-puntos, tarea 1, tarea 2, tarea 4 — la "tarea 3" sobre umbrales ya estaba absorbida en la 0), sobrevivieron la 0 (parcial) y la 1. **Se perdieron:** <br>(a) **Inventario terminológico completo** — sesión dedicada para asignar nombre formal o `[TEMP]` a cada mecanismo/herramienta/proceso/análisis del proyecto. Plan ya definido: búsqueda en ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, publicaciones de Anthropic/OpenAI/DeepMind, grey literature. Mínimo 5 queries por ítem, 3 idiomas, umbral de 5 búsquedas + 2 fuentes grises. <br>(b) **Verificación de cifras de hitos** — cita de línea exacta en `hitos_v7` (archivo `IRAM_hitos_metodologicos_2026-06-12_v7.md`, en Corpus A/gaps) para los números de autoría "Operador-iniciativa" y colaborativos. Nota: la regla derivada de esta tarea (*"no usar cifras de hitos sin verificación de línea"*) sí sobrevivió en el `QUÉ NO HACER` de ambos logs posteriores — es la acción que la cumple la que se perdió, no la regla. <br>**Ninguna de las dos se ejecutó todavía en ninguna sesión posterior.** Quedan reincorporadas como tareas 6 y 7 de la lista de PRÓXIMAS TAREAS de este log — el operador no pidió ejecutarlas todavía, solo que quedaran registradas. |
| DR-36 | **Detalle perdido en el mismo salto (`02-43`→`17-58`): qué bugs del mod se corrigieron y en qué versión.** `SESSION_LOG_REPLANTEO_2026-06-20_5.md` y `02-43` tenían la línea completa: *"Mod IRAM: Sustancialmente cerrado. BUG-1, BUG-3, BUG-4 corregidos en v5.6. Quedan bugs menores — no se tocan en esta fase."* Desde `17-58` en adelante (incluyendo `23-17`, el log inmediatamente anterior a este) la línea se comprimió a *"Sustancialmente cerrado. Sin cambios."* — la sustancia (mod cerrado) sigue siendo correcta y no cambia ninguna decisión operativa, pero el detalle verificable (qué bugs, corregidos dónde) dejó de estar en la cadena activa sin nota de "ver detalle en X". No es bloqueante para nada — se restaura acá por trazabilidad, en la tabla de ESTADO REAL de este mismo log. |
| DR-37 | **El mismo tipo de fuga ya había ocurrido antes en una serie de logs distinta del proyecto (`SESSION_LOG_DOCUMENTACION`, la que llevó al cierre del paper C1 en s34) — y ya había sido diagnosticado, corregido, y se había escrito una regla para prevenirlo, que nunca llegó a la serie REPLANTEO.** Caso concreto: en `s19` el "Marco Conceptual (12 clusters)" quedó documentado en el cuerpo del log pero no se trasladó a la sección de pendientes de `s20`, que solo copió la nota "sin cambios desde s19" sin el contenido real. El propio proyecto lo detectó en `s22` (ahí aparece una "TAREA 0 — URGENTE: Auditoría de fuentes de documentación", con búsqueda dirigida: *"secciones presentes en s19 que no aparezcan en s20 ni en s21"*), lo recuperó en `s23` (pasó a vivir en `WIKI_DOCUMENTACION_v1.md`, no en el SESSION_LOG), y en `s21` había quedado escrita la regla de prevención (ver DR-38). Esto confirma que el mecanismo de fuga (log largo con mucho contenido nuevo → la sección de estado/pendientes se reescribe de memoria en vez de compararse línea por línea contra la anterior) no es exclusivo de la serie REPLANTEO — es un riesgo estructural de cómo funciona este sistema de logs en general, y ya se manifestó dos veces en dos series distintas del mismo proyecto. Auditoría completa de todas las demás transiciones de log del proyecto (serie ANALISIS_C1 v1-v5 completa, serie DOCUMENTACION s7-s18 y s24-s34): sin fugas adicionales — los ítems se degradan explícitamente de bloqueante a deuda residual, se marcan `[x]`/`[ ]`, o se cierran citando en qué sesión se resolvieron (formato DEC-XX). Única omisión menor sin cerrar del todo, no relacionada con este mecanismo: `fallo_sesiones_16-06-2026.md` queda pendiente desde `s23` (ligado a tarea de autoría real, T2) y el proyecto de documentación se declara "sin deuda residual" en `s33`/`s34` sin volver a mencionarlo explícitamente — no bloqueó el cierre del paper, no requiere acción a menos que se retome esa línea de autoría. |
| DR-38 | **Regla de consolidación adoptada para la serie REPLANTEO, portada desde `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s21.md` (donde ya existía sin haberse aplicado nunca acá).** Antes de reescribir las secciones "PRÓXIMAS TAREAS" o "ESTADO REAL" al generar un nuevo SESSION_LOG_REPLANTEO, comparar la versión nueva contra la del log inmediatamente anterior, ítem por ítem: todo lo que estaba debe aparecer en la nueva versión, o estar marcado explícitamente "resuelto (DR-XX)" / "descartado porque Y" / "absorbido en Z". No alcanza con una nota genérica tipo "sin cambios" cuando en realidad había contenido específico (fechas, nombres de archivo, números de bug, IDs) que se está comprimiendo o perdiendo. Esta regla aplica en particular cuando la sesión trae mucho contenido nuevo y urgente (fue exactamente lo que pasó en el salto `02-43→17-58`, con estructura de carpetas + prueba de memoria + nomenclatura todo junto) — ese es el escenario de mayor riesgo de reescribir de memoria en vez de cotejar. |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-04 23:44

*(Sin cambios operativos respecto a `23-17`. Se restaura el detalle de Mod IRAM perdido en el salto anterior — ver DR-36.)*

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. BUG-1, BUG-3, BUG-4 corregidos en v5.6 (detalle restaurado, DR-36). Quedan bugs menores sin identificar en el log actual — no se tocan en esta fase. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34. Sin cambios. |
| WIKI_DOCUMENTACION_v2.md | Sin tocar (DR-12 sigue vigente). |
| Corpus A / Corpus B | Sin cambios de estado — sigue sin procesar. |
| Estructura física de carpetas | Diseñada y acordada (DR-27). **No aplicada todavía.** |
| Nomenclatura — Mod | ✅ Resuelta. |
| Nomenclatura — Documentación del mod | ❌ No resuelta (DR-31). Plan de 3 capas acordado (DR-32), no ejecutado. |
| Nomenclatura — UTN/Portafolio | ✅ Resuelta — vive en este chat de replanteo (DR-28). |
| Prueba de fuga de memoria — Claude (claude.ai) | Ejecutada. Sin fugas (DR-29). Cobertura de zips anidados verificada (DR-33). |
| Prueba de fuga de memoria — 5 cuentas del corpus | **Cerrada (DR-34).** `claude_1`–`claude_4`: negativo. `claude_5`: memoria activada/desactivada sin borrar → propagación de info desactualizada a otro chat de esa cuenta (fenómeno distinto al buscado). |
| **Auditoría de continuidad entre logs (esta sesión)** | **Cerrada (DR-35/DR-36/DR-37).** Encontradas y documentadas: 2 tareas perdidas (DR-35), 1 detalle comprimido sin trazabilidad (DR-36), 1 precedente del mismo mecanismo en otra serie con regla de prevención ya escrita pero nunca portada (DR-37). Regla de consolidación adoptada hacia adelante (DR-38). |
| Diplomatura UTN | Entrega Parte 1: 15/07/2026 (sin cambios). |
| Tarea 0 (criterios de forma/fondo) | Sin cambios esta sesión — sigue con el mismo sub-punto abierto (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline). |

---

## PRÓXIMAS TAREAS — en orden de prioridad

*(Idéntica a la lista de `23-17`, con las dos tareas recuperadas de DR-35 agregadas al final como 6 y 7 — no se reordenó nada más. El operador no pidió ejecutar ninguna de las dos todavía, solo dejarlas registradas.)*

1. **Aplicar físicamente la estructura de carpetas DR-27** (mover archivos, no renombrar todavía).
2. **Ejecutar el plan de 3 capas de DR-32** sobre `fuentes de documentacion` (mapa de vigencia → mapa de citas cruzadas → recién ahí, renombrado).
3. Retomar la tarea 0 pendiente de logs anteriores (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline).
4. Inventario completo del material de archivo (tarea 1 de logs anteriores) — sigue pendiente.
5. *(Opcional, no bloqueante)* Si se quiere cerrar el tema memoria por completo: confirmar en `claude_5` que la memoria persistente quedó efectivamente desactivada y, si la interfaz lo permite, borrar el contenido residual para que no vuelva a propagarse a un tercer chat.
6. *(Recuperada de `02-43`, DR-35a — no bloqueante, sin fecha asignada)* **Inventario terminológico completo.** Sesión dedicada. Nombre formal o `[TEMP]` para cada mecanismo/herramienta/proceso/análisis del proyecto. Plan: ACM, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar, Hugging Face papers, publicaciones Anthropic/OpenAI/DeepMind, grey literature. Mínimo 5 queries por ítem, 3 idiomas, umbral de 5 búsquedas + 2 fuentes grises.
7. *(Recuperada de `02-43`, DR-35b — no bloqueante, sin fecha asignada)* **Verificación de cifras de hitos.** Cita de línea exacta en `IRAM_hitos_metodologicos_2026-06-12_v7.md` para los números de autoría "Operador-iniciativa" y colaborativos.

---

## QUÉ NO HACER — VIGENTE + AGREGADO DE ESTA SESIÓN

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes.
- No tocar el mod.
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual.
- No bajar el estatus de ningún documento sin el inventario de DR-07.
- No asumir que algo "puede avanzar en paralelo" sin confirmación del operador.
- No narrar logros, "calibre", ni dramatizar decisiones propias.
- No llamar a actualizar el log sin instrucción explícita del operador.
- No proponer métricas sin anclarlas a una pregunta concreta.
- No afirmar novedad del proyecto sin búsqueda más profunda.
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).
- No presentar el timeline como fechas confirmadas — siempre con "(condicionado — ver DR-18)".
- No usar cifras de hitos de autoría sin verificación de línea en hitos_v7.
- No renombrar archivos de `fuentes de documentacion` sin haber hecho antes el mapa de vigencia y citas cruzadas (DR-32).
- No confundir el hallazgo de `claude_5` (DR-34, contaminación por memoria mal desactivada) con una fuga tipo DR-30 (detalle operativo no documentado) — son mecanismos distintos y no deben mezclarse si se reporta este resultado más adelante.
- **Nueva (DR-38): al generar el próximo SESSION_LOG_REPLANTEO, no reescribir "PRÓXIMAS TAREAS" ni "ESTADO REAL" de memoria — cotejar ítem por ítem contra este log. Todo lo que está acá debe aparecer en la siguiente versión, o quedar marcado explícitamente resuelto/descartado/absorbido, citando el ID que lo resuelve.**

---

## APÉNDICE — MATERIAL DE REFERENCIA PARA LA PRÓXIMA CUENTA (no redebatir, solo consultar si hace falta detalle)

Esta sesión ocurrió en una cuenta sin memoria previa del proyecto, solo con el ZIP y el log `23-17`. Lo que sigue es un mapa de dónde vive cada cosa dentro del ZIP, para que la próxima cuenta no tenga que re-explorarlo de cero.

**Estructura real del ZIP (`IRAM_PROYECTO3.zip`, carpeta raíz `IRAM PROYECTO/`):**
- Serie `SESSION_LOG_REPLANTEO_*.md` en la raíz — la que este log continúa. Hay bastante ruido: varios archivos duplicados con sufijos `2`, `3`, etc. de subidas repetidas (confirmado con diff en varios pares, ej. `2026-06-20 3.md` y `2026-06-20 4.md` son idénticos). La cadena canónica real, por contenido (no por nombre de archivo), es: `2026-06-19_2` → `2026-06-20_5` → `2026-07-03_02-43` (el archivo con más líneas de cada tanda de duplicados es siempre el vigente) → `2026-07-03_17-58` → `2026-07-04_23-17` → este archivo.
- `DOCUMENTACION/` en la raíz — contiene el paper cerrado (`IRAM_C1_final.md`), la wiki sin tocar (`WIKI_DOCUMENTACION_v2.md`), specs de análisis (`spec_a_authorship.py`, `spec_b_democratizacion.py`, `spec_c_zip_history.py` — también con duplicados por sufijo), y la serie completa `SESSION_LOG_DOCUMENTACION_s7` a `s34` que documenta cómo se cerró el paper C1 (serie prolija, sin fugas salvo el caso s19→s20 ya citado en DR-37).
- `documentacion iram 10-06-2026 00.30/` — contiene, anidada dos veces (carpeta `fuentes de documentacion/` duplicada dentro de sí misma, confirmado backup exacto por DR-33), la serie completa `SESSION_LOG_DOCUMENTACION` más `historial viejo/` (conversaciones crudas de abril-mayo) y `IRAM_legacy v1 v2 v3 v4/` (versiones descartadas del mod). Esta es la carpeta con el problema de nomenclatura sin resolver (DR-31).
- `documentacion claude 1.zip` a `documentacion claude 5.zip` en la raíz — Corpus B crudo, período 10-20/06, todavía sin procesar. Corresponde a las mismas 5 cuentas de DR-30/DR-34.
- `Consigna.md/pdf`, `Consigna_1.*`, `Consigna_2.*` — material de la diplomatura UTN.
- `achievements_imperator.xlsx` — sin relación directa con las tareas activas, no auditado en esta sesión.

**Para retomar la Tarea 1 (inventario completo, punto 4 de la lista):** este apéndice no lo reemplaza — sigue haciendo falta el inventario ítem por ítem con estado vigente/histórico/pendiente que pide esa tarea. Esto es solo un mapa de navegación rápida.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
