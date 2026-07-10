# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-03 17:58 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-03_02-43.md (queda como archivo histórico, no como insumo a recargar completo)
**Motivo de esta versión:** confirmación de estructura física de carpetas para las 3 piezas (DR-27) + aclaración de que el material de replanteo no es una 4ta pieza permanente sino transitorio (DR-28) + prueba de fuga de memoria ejecutada contra Claude de claude.ai, no una de las 5 cuentas del corpus, con resultado negativo (DR-29) + extensión de esa prueba a las 5 cuentas de Claude que trabajaron directamente en el proyecto, todavía no ejecutada (DR-30) + identificación de que la carpeta `fuentes de documentacion` tiene el problema de nomenclatura no resuelto que las otras dos piezas ya resolvieron (DR-31) + plan de mapa de vigencia + citas cruzadas, todavía no ejecutado (DR-32) + verificación exhaustiva de los 21 zips anidados del proyecto, cierra un hueco de cobertura de la prueba de memoria (DR-33).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-26 de los logs anteriores siguen vigentes sin modificación. No se repiten acá — se citan por ID. Si hace falta el detalle, ir a `SESSION_LOG_REPLANTEO_2026-06-19_2.md` (DR-01 a DR-09) y `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (DR-10 a DR-26).

**Nota especial sobre DR-12:** sigue vigente sin cambios. La sesión de hoy no tocó WIKI_DOCUMENTACION_v2.md ni la corrigió — solo se discutió estructura de carpetas y se ejecutó una prueba de memoria en un chat separado (Claude de claude.ai, ver DR-28), que no es insumo del corpus.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-27 | **Estructura física de carpetas confirmada para las 3 piezas (DR-25).** No se ejecutó todavía — queda como diseño acordado, pendiente de aplicación física. Estructura: <br>`01_MOD/` (activo: contenido actual de `IRAM mod v5/` tal cual) + `01_MOD/archive/` (legacy v1-v4, `game.zip`, `wiki_imperator.txt`, `achievements_imperator.xlsx`). <br>`02_DOCUMENTACION/` (activo: PROMPT_MAESTRO, WIKI, SESSION_LOG vigentes, paper C1, specs — más el SESSION_LOG_REPLANTEO vigente, mientras el replanteo siga en curso) + `02_DOCUMENTACION/archive/` (historial viejo, replanteo ya cerrado, corpus_b_crudo sin procesar). <br>`03_UTN_PORTAFOLIO/` (con dos subcarpetas: `consignas/` para `Consigna.md/pdf`, `Consigna_1`, `Consigna_2`; y `entregable/`, reservada para cuando el trabajo de las 3 etapas se materialice como archivo — hoy no existe ningún archivo ahí). |
| DR-28 | **El material del replanteo (CHARLA REPLANTEO, SESSION_LOG_REPLANTEO, SESION TRUNCADA) no es una 4ta pieza permanente.** Es meta-análisis transitorio: el proceso de decidir cómo se estructuran y cuentan las 3 piezas reales (mod, documentación, entregable UTN/portafolio). Una vez cerrado, lo que sobrevive de él no queda como carpeta propia — se reparte así: las decisiones DR-xx se incorporan al contenido oficial de `02_DOCUMENTACION` (terminan reflejadas en WIKI/SESSION_LOG); el session log del replanteo cerrado pasa a `02_DOCUMENTACION/archive/`; el producto final del replanteo es, por DR-25, la misma cosa que el entregable de `03_UTN_PORTAFOLIO/entregable/`. |
| DR-29 | **Prueba de fuga de memoria ejecutada — pero contra la cuenta equivocada para el objetivo real.** Se corrió una comprobación cruzando el volcado de memoria de Claude (claude.ai, la cuenta de esta conversación — nunca trabajó directamente en el proyecto) contra el material real del ZIP. Resultado: **sin fugas**. Las 5 afirmaciones "sospechosas" de esa memoria (esqueleto s17, nueve correcciones de criterio, tiering, PROMPT_MAESTRO como artefacto central, "tres patrones nunca documentados") tienen equivalente verificable en los documentos — el único matiz es que la memoria tenía una versión desactualizada del punto del tiering, que ya se había consolidado en el paper (`IRAM_C1_final.md`, sección 4D) para cuando se hizo la prueba. Esto valida el diseño del sistema de logs/wiki para esta cuenta, pero **no es la prueba que más importa**: esta cuenta no ejecutó ningún trabajo real del proyecto, así que su memoria tenía poco margen para contener algo genuinamente nuevo. |
| DR-30 | **Extender la misma prueba a las 5 cuentas de Claude que sí trabajaron directamente en el proyecto (`claude_1` a `claude_5`, las del corpus).** Esas cuentas sí ejecutaron sesiones reales — su memoria puede tener detalles operativos finos (decisiones de una sesión puntual, nombres exactos, matices que en el momento parecían menores y nunca llegaron a un log) que la cuenta de esta conversación no puede tener por no haber participado. Esta es la comprobación que realmente prueba si el sistema de logs/wiki cumple su función, no la de DR-29. **No ejecutada todavía** — es la próxima tarea operativa, a correr directamente en el chat de cada una de esas 5 cuentas. |
| DR-31 | **Nomenclatura por pieza — resultado del chequeo de esta sesión.** Pieza 1 (Mod): resuelta, esquema `IRAM_[TIPO]_v[N]_AAAA-MM-DD_HH-MM.md` consistente en los 10 archivos de `IRAM mod v5/`. Pieza 3 (UTN/Portafolio): resuelta — el entregable vive en este chat de replanteo, con reglas ya definidas (DR-13/DR-14/DR-25) para cuando se materialice como archivo; no hay vacío real, solo ausencia de artefacto porque todavía no salió del proceso de decisión. Pieza 2 (Documentación del mod, carpeta `fuentes de documentacion`): **no resuelta**. Problemas concretos identificados: (a) esquema `s[N]` sin fecha en varios archivos (`IRAM_C1_esqueleto_s17.md`, `IRAM_C1_s3_draft_s20.md`) que no permite ubicar temporalmente el archivo y en algunos casos mezcla dos números de sesión distintos en el mismo nombre; (b) sufijos `(2)`, `(3)`, `(1)` que son duplicados de subida, no versiones reales (confirmado con `diff` en al menos un par); (c) archivos sin ningún esquema de nombre, incluyendo el más citado del proyecto (`IRAM_C1_final.md`, sin fecha ni número de sesión). DR-24 (convención `AAAA-MM-DD_HH-MM`) se aplicó hacia adelante al replanteo, pero nunca se aplicó retroactivamente a esta carpeta. |
| DR-32 | **Plan acordado para resolver DR-31 — no ejecutado todavía.** Enfoque en 3 capas, cada una con checkpoint antes de la siguiente: (1) Mapa de vigencia — recorrer los archivos tipo log/wiki/prompt/paper (no las transcripciones crudas de charla) usando sus propios encabezados de "Reemplaza a...", "Fecha", "Estado" para armar tabla archivo→pieza→vigente/histórico→reemplazado-por; bajo costo, alto valor, útil incluso sin renombrar nada. (2) Mapa de citas cruzadas, acotado a los archivos que el paso 1 marque como vigentes — no escanear los 208 archivos completos, porque las transcripciones muertas citándose entre sí no necesitan quedar mapeadas. Distinguir tres tipos de relación: "reemplaza a" (rompe algo si se toca mal), "depende de" (ej. C2 depende de la base de hechos, no del paper — DR-02; rompe algo si se toca mal), "cita como evidencia puntual" (ej. DR-22 citando `failed_3.md`; no rompe nada si el archivo queda donde está). (3) Renombrado + guía maestra, aplicado solo después de tener 1 y 2 verificados. El renombrado en sí quedó explícitamente pospuesto esta sesión — el foco pasó a reorganización de carpetas (DR-27) y a la prueba de memoria (DR-29/DR-30) antes de volver a esto. |
| DR-33 | **Verificación exhaustiva de los 21 zips anidados dentro del ZIP del proyecto — cierra un hueco de cobertura de DR-29.** DR-29 se corrió solo contra archivos .md ya descomprimidos; quedaba sin confirmar si algún zip anidado contenía material narrativo no reflejado en esos .md. Resultado, uno por uno: (a) `documentacion iram 10-06-2026 00.30.zip` y `fuentes de documentacion.zip` — backups exactos de sus carpetas hermanas, confirmado con `diff -r`, cero diferencias; redundantes, sin contenido nuevo. (b) Los 10 `mod_pack_IRAM_*.zip` + `game.zip` — código/assets del mod (`.txt`/`.yml`/`.mod`), cero archivos `.md`; fuera del alcance de una prueba de fuga de memoria narrativa. (c) Los 5 `data-*-batch-0000.zip` de `historial viejo` (conversaciones crudas, abril-mayo 2026, no mencionados en ningún log previo) — verificados por muestra: el caso técnico "botones invisibles / `POPSButtonStyle` no definido" extraído del `conversations.json` crudo aparece confirmado en 5 archivos `.md` ya procesados (incluyendo `IRAM_historial_desarrollo_2.md`). El crudo llegó al documento — no es una fuga. (d) Los 5 `documentacion claude N.zip` de la raíz (Corpus B, período 10-20/06) — **quedan sin verificar**, pero no por omisión: es el mismo Corpus B que el log ya tenía marcado como "no procesado todavía"; no corresponde compararlo contra un .md procesado porque ese .md no existe aún. **Conclusión: DR-29 queda confirmado y reforzado — el universo de .md que se usó para esa prueba no tenía material narrativo oculto en zips sin abrir.** La única cobertura pendiente real sigue siendo DR-30 (las 5 cuentas del corpus) y, dentro de DR-30, el crudo de `documentacion claude 1-5.zip` una vez procesado. |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-03 17:58

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. Sin cambios desde el log anterior. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34. Sin cambios desde el log anterior. Confirmado en esta sesión que sí contiene la sección 4D (tiering), consolidada — no es un hallazgo huérfano. |
| WIKI_DOCUMENTACION_v2.md | Sin tocar (DR-12 sigue vigente). |
| Corpus A / Corpus B | Sin cambios de estado desde el log anterior — sigue sin procesar. |
| Estructura física de carpetas | Diseñada y acordada (DR-27). **No aplicada todavía.** |
| Nomenclatura — Mod | ✅ Resuelta (confirmado esta sesión). |
| Nomenclatura — Documentación del mod | ❌ No resuelta (DR-31). Plan de 3 capas acordado (DR-32), no ejecutado. |
| Nomenclatura — UTN/Portafolio | ✅ Resuelta — vive en este chat (DR-28). |
| Prueba de fuga de memoria — Claude (claude.ai) | Ejecutada. Sin fugas encontradas (DR-29). Cobertura verificada contra los 21 zips anidados del proyecto — sin material narrativo oculto sin abrir (DR-33). |
| Prueba de fuga de memoria — 5 cuentas del corpus | No ejecutada (DR-30). Próxima tarea operativa. |
| Diplomatura UTN | Entrega Parte 1: 15/07/2026 (sin cambios). |
| Tarea 0 (criterios de forma/fondo, ver log anterior) | Sin cambios esta sesión — sigue con el mismo sub-punto abierto (umbrales concretos de B) y la misma nota de vínculo diplomatura↔pipeline sin confirmar explícitamente. No se retomó en esta sesión; el foco fue estructura de carpetas y prueba de memoria. |

---

## PRÓXIMAS TAREAS — en orden de prioridad

1. **[Prioridad alta, acordada esta sesión] Ejecutar DR-30**: correr la prueba de fuga de memoria directamente en el chat de cada una de las 5 cuentas de Claude del corpus (`claude_1` a `claude_5`). Método sugerido: pedirle a cada cuenta que vuelque su memoria sobre IRAM en un .md propio, sin inventar, marcando qué es certeza vs. reconstrucción — mismo formato que el volcado de esta cuenta, para poder cruzar los 5 resultados de forma consistente. Cada cuenta analiza su propia memoria contra el material real (o contra lo que tenga disponible) y reporta si encuentra algo que no esté en los logs/wiki.
2. Aplicar físicamente la estructura de carpetas DR-27 (mover archivos, no renombrar todavía).
3. Ejecutar el plan de 3 capas de DR-32 sobre `fuentes de documentacion` (mapa de vigencia → mapa de citas cruzadas → recién ahí, renombrado).
4. Retomar la tarea 0 pendiente de logs anteriores (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline) — no se tocó esta sesión.
5. Inventario completo del material de archivo (tarea 1 de logs anteriores) — sigue pendiente, sin cambios.

---

## QUÉ NO HACER — VIGENTE + AGREGADOS DE ESTA SESIÓN

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes.
- No tocar el mod.
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual.
- No bajar el estatus de ningún documento sin el inventario de DR-07.
- No asumir que algo "puede avanzar en paralelo" sin confirmación del operador.
- No narrar logros, "calibre", ni dramatizar decisiones propias.
- No llamar a actualizar el log sin instrucción explícita del operador.
- No proponer métricas sin anclarlas a una pregunta concreta.
- No afirmar novedad del proyecto sin búsqueda más profunda — solo "ausencia en fuentes revisadas el 19/06".
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).
- No presentar el timeline como fechas confirmadas — siempre con "(condicionado — ver DR-18)".
- No usar cifras de hitos de autoría sin verificación de línea en hitos_v7.
- No confundir la prueba de memoria de esta cuenta (DR-29, sin fugas) con la prueba real que importa (DR-30, sobre las 5 cuentas del corpus, todavía no hecha) — son pruebas distintas con distinto poder de detección, no ejecutar como si la primera ya respondiera la pregunta completa.
- No renombrar archivos de `fuentes de documentacion` sin haber hecho antes el mapa de vigencia y citas cruzadas (DR-32).

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
