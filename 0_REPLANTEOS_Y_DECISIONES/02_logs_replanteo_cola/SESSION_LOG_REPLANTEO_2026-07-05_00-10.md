# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-05 00:10 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-04_23-44.md (queda como archivo histórico, no como insumo a recargar completo)
**Tipo de sesión:** auditoría de continuidad, parte 2 — no se ejecutó ninguna tarea operativa del proyecto (mod, corpus, paper, carpetas). Continuación directa de la auditoría de `23-44`, esta vez sobre la serie `SESSION_LOG_REPLANTEO_*` completa (no solo la cadena canónica citada en su apéndice) más los archivos sueltos de la raíz asociados a la prueba de fuga de memoria (`resultado_prueba_fuga_memoria.md`, `instruccion_prueba_fuga_memoria.md`, `sigue log.md`).
**Motivo de esta versión:** cita rota hacia el detalle de DR-27–DR-33 (DR-39), borrador descartado sin marcar (DR-40), dos fugas reales documentadas en `resultado_prueba_fuga_memoria.md` que nunca recibieron ID ni entraron a QUÉ NO HACER (DR-41), cita de origen de DR-38 con nombre de archivo incorrecto y regla reformulada más débil que la original (DR-42), diagnóstico de causa raíz de DR-41 por relato directo del operador — contaminación de memoria de `claude_5` con efecto en nombres de archivo de otro proyecto (DR-43), encuadre de ese caso como evidencia citable para C1 sin reclamo de novedad (DR-44).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

**Nota sobre esta sesión en particular:** tampoco avanzó esa prioridad única — fue, otra vez, una sesión de auditoría hacia atrás, no hacia adelante. A diferencia de `23-44` (que auditó saltos entre logs consecutivos), esta sesión auditó la serie completa contra su propio apéndice de navegación y contra los archivos de evidencia sueltos que ese apéndice no listaba. Las tareas operativas siguen exactamente donde estaban en `23-44`. Ver PRÓXIMAS TAREAS, sin cambios de fondo.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-38 de los logs anteriores siguen vigentes, con dos correcciones puntuales de esta sesión (ver DR-39 y DR-42 abajo — no anulan las decisiones, corrigen su cita o su redacción). Se citan por ID. Si hace falta el detalle:
- `SESSION_LOG_REPLANTEO_2026-06-19_2.md` — DR-01 a DR-09 (incluye la investigación de novedad citada en DR-44).
- `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` — DR-10 a DR-26.
- `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md` (**con el "2" — corregido por DR-39, no usar la versión sin sufijo**) — DR-27 a DR-33.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-17.md` — DR-34.
- `SESSION_LOG_REPLANTEO_2026-07-04_23-44.md` — DR-35 a DR-38.

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión tampoco tocó `WIKI_DOCUMENTACION_v2.md` ni ningún archivo del proyecto — fue auditoría de lectura sobre los logs y archivos de evidencia dentro del ZIP.

**Nota especial sobre DR-38:** su cita de origen y su redacción quedan corregidas por DR-42 (ver tabla). La decisión en sí (adoptar una regla de consolidación) sigue vigente — lo que cambia es cuál es el texto exacto de la regla que rige de acá en adelante.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-39 | **Cita rota hacia el detalle de DR-27–DR-33.** `23-17` y `23-44` citan `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` (sin sufijo) como fuente de ese rango. Existen dos archivos con ese timestamp y no son idénticos: `..._17-58 2.md` (18:01) es la versión más nueva — confirmado por el propio `resultado_prueba_fuga_memoria.md`, que la llama explícitamente "el más reciente" — y contiene un dato que la otra no tiene (verificación de `DOCUMENTACION.zip`, 18/18 archivos idénticos, dentro de DR-33). **Corrección: la cita correcta de DR-27 a DR-33, de acá en adelante, es `SESSION_LOG_REPLANTEO_2026-07-03_17-58 2.md`.** |
| DR-40 | **Borrador descartado sin marcar.** `SESSION_LOG_REPLANTEO_2026-07-03_17-47.md` es un intento intermedio de la sesión de las 17:58 (11 minutos antes), con DR-28/29/30 numerados en un orden distinto al de la versión final. A diferencia de otros pares duplicados de la serie (`2026-06-20 3/4`, los `07-03` de madrugada), no estaba marcado como descartado en ningún apéndice. Queda formalmente descartado acá: no es insumo, no se cita, no se abre salvo arqueología puntual. |
| DR-41 | **Dos fugas reales de `resultado_prueba_fuga_memoria.md` (04/07) sin ID ni registro en QUÉ NO HACER.** (a) La afirmación "Módulos 1-4 (16 unidades) de la diplomatura verificados y reorganizados" no tiene respaldo en ningún archivo del proyecto. (b) La convención de nombres `ModuloN_UnidadM_Tema_Corto.md` tampoco existe documentada en ningún lado. Ambas quedan marcadas como fuga confirmada — no asumir ninguna de las dos como cierta en trabajo futuro sobre la pieza UTN/Portafolio. (Causa raíz identificada en DR-43 — no es narrativa inventada de la nada, ver esa entrada.) |
| DR-42 | **Cita de origen de DR-38 con nombre de archivo incorrecto, y regla reformulada más débil que la original.** DR-38 cita `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s21.md`; el archivo real es `SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md` (contenido correcto, nombre mal citado). Además, la regla original en `s21` es más estricta que su reformulación en DR-38: dice explícitamente *"nunca reescribir celdas existentes de tabla, solo agregar al final"* (append-only) — DR-38 la había suavizado a "comparar ítem por ítem y marcar resuelto/descartado". **La versión vigente de la regla de consolidación, de acá en adelante, es la append-only original de `s21`, no la reformulación de DR-38.** Este mismo log se generó seleccionando esa versión. |
| DR-43 | **Causa raíz de DR-41: contaminación de memoria en `claude_5` (mismo mecanismo de DR-34) con efecto en nombres de archivo, no solo en narrativa.** Según relato directo del operador: en una charla de `claude_5` sin relación con IRAM (debate de enfoque diplomatura/portfolio), la memoria persistente contaminada de una sesión IRAM anterior hizo que Claude nombrara archivos de la diplomatura como si fueran del proyecto IRAM — origen de la convención `ModuloN_UnidadM_Tema_Corto.md` de DR-41: no fue inventada de la nada, se usó en esa charla puntual para archivos de diplomatura mal etiquetados. **No verificable con el material disponible:** los dos zips de `claude_5` (`documentacion claude 5.zip`, mod + documentación post-10/06) no llegan a la fecha de esa charla — el crudo no está en el proyecto. Queda como hallazgo diagnosticado por relato del operador, no por evidencia documental cruzada — a diferencia del resto de DR-34/41, que sí tenían archivo de respaldo. No genera tarea de verificación: no hay con qué ejecutarla. |
| DR-44 | **DR-43 queda marcado como caso de evidencia para C1, no como hallazgo de novedad.** El fenómeno de fondo (memoria/documentación que se desactualiza en silencio mientras el objeto real cambia) ya está catalogado como no-novedoso en la investigación de `2026-06-19_2` ("stale specs"/"factual drift"). Lo que aporta DR-43 es un caso propio, con fecha y mecanismo trazado, de esa misma familia de fallas aplicada a memoria de producto en vez de a documentación escrita. Uso sugerido: guardarlo como ejemplo citable para cuando se retome C1 — no requiere acción ahora, no cambia prioridades. |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-05 00:10

*(Sin cambios operativos respecto a `23-44`. Se agrega el cierre de esta auditoría, parte 2.)*

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. BUG-1, BUG-3, BUG-4 corregidos en v5.6. Quedan bugs menores sin identificar — no se tocan en esta fase. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34. Sin cambios. |
| WIKI_DOCUMENTACION_v2.md | Sin tocar (DR-12 sigue vigente). |
| Corpus A / Corpus B | Sin cambios de estado — sigue sin procesar. |
| Estructura física de carpetas | Diseñada y acordada (DR-27). **No aplicada todavía.** |
| Nomenclatura — Mod | ✅ Resuelta. |
| Nomenclatura — Documentación del mod | ❌ No resuelta (DR-31). Plan de 3 capas acordado (DR-32), no ejecutado. |
| Nomenclatura — UTN/Portafolio | ✅ Resuelta — vive en este chat de replanteo (DR-28). **Ojo:** no confundir con la convención fabricada de DR-41/43 (`ModuloN_UnidadM_Tema_Corto.md`), que no es la resolución real. |
| Prueba de fuga de memoria — Claude (claude.ai) | Ejecutada. Sin fugas (DR-29). Cobertura de zips anidados verificada (DR-33, ver DR-39 para la cita correcta). |
| Prueba de fuga de memoria — 5 cuentas del corpus | Cerrada (DR-34). `claude_1`–`claude_4`: negativo. `claude_5`: memoria activada/desactivada sin borrar → propagación de info desactualizada, con efecto adicional en nombres de archivo de otro proyecto (DR-43, no verificable con el material disponible). |
| Auditoría de continuidad, sesión `23-44` | Cerrada (DR-35/36/37/38). |
| **Auditoría de continuidad, esta sesión (parte 2)** | **Cerrada (DR-39 a DR-44).** Encontrados y corregidos: 1 cita rota (DR-39), 1 borrador sin marcar (DR-40), 2 fugas sin ID (DR-41), 1 cita de origen incorrecta + regla debilitada (DR-42), 1 causa raíz diagnosticada sin evidencia documental disponible (DR-43), 1 caso encuadrado como evidencia para C1 (DR-44). |
| Tarea 0 (criterios de forma/fondo) | Sin cambios esta sesión — sigue con el mismo sub-punto abierto (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline). |

---

## PRÓXIMAS TAREAS — en orden de prioridad

*(Idéntica a la lista de `23-44` — sin cambios. Ninguna tarea nueva de esta sesión: se había considerado agregar "revisar `documentacion claude 5.zip`" para DR-43, pero se descartó porque el material no llega a la fecha necesaria — ver DR-43.)*

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
- Al generar el próximo SESSION_LOG_REPLANTEO, no reescribir "PRÓXIMAS TAREAS" ni "ESTADO REAL" de memoria — cotejar ítem por ítem contra este log. Todo lo que está acá debe aparecer en la siguiente versión, o quedar marcado explícitamente resuelto/descartado/absorbido, citando el ID que lo resuelve.
- **(DR-42) Al agregar una sección nueva a un log, no reescribir celdas de tabla existentes — solo agregar al final. Esta es la regla vigente, más estricta que la reformulación de DR-38.**
- **(DR-39) Al citar un log por nombre de archivo, verificar primero que no exista un duplicado con sufijo numérico antes de asumir cuál es el vigente — no alcanza con el nombre "sin sufijo" por default.**
- **(DR-41/DR-43) No asumir completitud de los Módulos UTN 1-4 ni dar por real la convención `ModuloN_UnidadM_Tema_Corto.md` — confirmado como material de otro proyecto (diplomatura) mal etiquetado como IRAM por contaminación de memoria, no una resolución de nomenclatura real.**

---

## APÉNDICE — MATERIAL DE REFERENCIA PARA LA PRÓXIMA CUENTA (no redebatir, solo consultar si hace falta detalle)

*(Se mantiene el mapa de `23-44`, con una corrección — DR-39 — y el agregado de archivos que ese mapa no listaba y que esta sesión sí usó como evidencia.)*

**Estructura real del ZIP (`IRAM_PROYECTO3.zip`, carpeta raíz `IRAM PROYECTO/`):**
- Serie `SESSION_LOG_REPLANTEO_*.md` en la raíz. Cadena canónica real, por contenido: `2026-06-19_2` → `2026-06-20_5` → `2026-07-03_02-43` → `2026-07-03_17-58 2` (**con el "2" — corregido por DR-39**, no `17-58.md` sin sufijo) → `2026-07-04_23-17` → `2026-07-04_23-44` → este archivo. `2026-07-03_17-47.md` queda formalmente descartado (DR-40).
- `DOCUMENTACION/` en la raíz — paper cerrado (`IRAM_C1_final.md`), wiki sin tocar (`WIKI_DOCUMENTACION_v2.md`), specs de análisis, serie `SESSION_LOG_DOCUMENTACION_s7` a `s34`.
- `documentacion iram 10-06-2026 00.30/` — serie `SESSION_LOG_DOCUMENTACION` anidada, `historial viejo/`, `IRAM_legacy v1-v4/`. Nota: el archivo con la regla de origen de DR-42 se llama `SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md` (no "CONSOLIDADO_s21" como decía la cita anterior).
- `documentacion claude 1.zip` a `documentacion claude 5.zip` — Corpus B crudo, período 10-20/06, sin procesar. `claude_5` no llega a la fecha de la charla de DR-43 (ver esa entrada).
- `Consigna.md/pdf`, `Consigna_1.*`, `Consigna_2.*` — material de la diplomatura UTN.
- **Agregado por esta sesión (no listados en el mapa de `23-44`, usados como evidencia de DR-39/41):** `resultado_prueba_fuga_memoria.md` (evidencia detrás de DR-29/34/41), `instruccion_prueba_fuga_memoria.md` (plantilla de esa prueba), `sigue log.md` (transcripción cruda de la sesión que generó DR-26), `memoria_claude_volcado.md` / `volcado_memoria.md` (volcados de memoria usados en la prueba de fuga), `CHARLA REPLANTEO 1.md` / `2.md` y `RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20*.md` (transcripciones crudas de las charlas fundacionales), `SESION TRUNCADA.md` (transcripción cruda de una sesión cortada, 229KB — no confundir con el fenómeno de "sesión cortada" que este sistema de logs está diseñado para mitigar; es solo el nombre del archivo).
- `achievements_imperator.xlsx`, `wiki_imperator.txt` — sin relación directa con las tareas activas, no auditados en esta sesión.

**Para retomar la Tarea 1 (inventario completo, punto 4 de la lista):** este apéndice no lo reemplaza — sigue haciendo falta el inventario ítem por ítem con estado vigente/histórico/pendiente. Esto es solo un mapa de navegación rápida.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
