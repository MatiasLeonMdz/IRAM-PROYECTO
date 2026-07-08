# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-07-04 23:17 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-07-03_17-58.md (queda como archivo histórico, no como insumo a recargar completo)
**Motivo de esta versión:** cierre de DR-30 — prueba de fuga de memoria ejecutada en las 5 cuentas del corpus (`claude_1` a `claude_5`), con hallazgo de causa raíz distinta a la buscada en `claude_5` (DR-34).

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-33 de los logs anteriores siguen vigentes sin modificación. No se repiten acá — se citan por ID. Si hace falta el detalle, ir a `SESSION_LOG_REPLANTEO_2026-06-19_2.md` (DR-01 a DR-09), `SESSION_LOG_REPLANTEO_2026-07-03_02-43.md` (DR-10 a DR-26) y `SESSION_LOG_REPLANTEO_2026-07-03_17-58.md` (DR-27 a DR-33).

**Nota especial sobre DR-12:** sigue vigente sin cambios. Esta sesión no tocó WIKI_DOCUMENTACION_v2.md.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-34 | **Cierre de DR-30 — prueba de fuga de memoria ejecutada en las 5 cuentas del corpus.** Resultado desagregado: **`claude_1` a `claude_4`**: memoria persistente no activada en ninguna de las 4 — negativo limpio, sin fugas porque no había volcado que cruzar. **`claude_5`**: memoria persistente había sido activada en algún momento y luego desactivada *sin borrar el contenido ya guardado*; ese contenido —información sobre IRAM desactualizada respecto al estado real del proyecto— se propagó a otro chat distinto dentro de la misma cuenta. **Esto no es el fenómeno que DR-30 estaba diseñada para detectar** (detalle operativo fino no documentado, retenido correctamente por logs/wiki) sino un mecanismo distinto: contaminación cruzada entre chats de una misma cuenta por manejo de memoria persistente (activar/desactivar sin limpiar), independiente de si el sistema de logs/wiki es suficiente o no. Se cierra como hallazgo aparte, no se mezcla con el resultado de las otras 4 cuentas. **DR-30 queda formalmente cerrada.** |

---

## ESTADO REAL — ACTUALIZADO AL 2026-07-04 23:17

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. Sin cambios. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34. Sin cambios. |
| WIKI_DOCUMENTACION_v2.md | Sin tocar (DR-12 sigue vigente). |
| Corpus A / Corpus B | Sin cambios de estado — sigue sin procesar. |
| Estructura física de carpetas | Diseñada y acordada (DR-27). **No aplicada todavía.** |
| Nomenclatura — Mod | ✅ Resuelta. |
| Nomenclatura — Documentación del mod | ❌ No resuelta (DR-31). Plan de 3 capas acordado (DR-32), no ejecutado. |
| Nomenclatura — UTN/Portafolio | ✅ Resuelta — vive en este chat (DR-28). |
| Prueba de fuga de memoria — Claude (claude.ai) | Ejecutada. Sin fugas (DR-29). Cobertura de zips anidados verificada (DR-33). |
| Prueba de fuga de memoria — 5 cuentas del corpus | **Cerrada (DR-34).** `claude_1`–`claude_4`: negativo. `claude_5`: memoria activada/desactivada sin borrar → propagación de info desactualizada a otro chat de esa cuenta (fenómeno distinto al buscado). |
| Diplomatura UTN | Entrega Parte 1: 15/07/2026 (sin cambios). |
| Tarea 0 (criterios de forma/fondo) | Sin cambios esta sesión — sigue con el mismo sub-punto abierto. |

---

## PRÓXIMAS TAREAS — en orden de prioridad

1. **Aplicar físicamente la estructura de carpetas DR-27** (mover archivos, no renombrar todavía).
2. **Ejecutar el plan de 3 capas de DR-32** sobre `fuentes de documentacion` (mapa de vigencia → mapa de citas cruzadas → recién ahí, renombrado).
3. Retomar la tarea 0 pendiente de logs anteriores (umbrales concretos del criterio B, nota de vínculo diplomatura↔pipeline).
4. Inventario completo del material de archivo (tarea 1 de logs anteriores) — sigue pendiente.
5. *(Opcional, no bloqueante)* Si se quiere cerrar el tema memoria por completo: confirmar en `claude_5` que la memoria persistente quedó efectivamente desactivada y, si la interfaz lo permite, borrar el contenido residual para que no vuelva a propagarse a un tercer chat.

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
- No afirmar novedad del proyecto sin búsqueda más profunda.
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).
- No presentar el timeline como fechas confirmadas — siempre con "(condicionado — ver DR-18)".
- No usar cifras de hitos de autoría sin verificación de línea en hitos_v7.
- No renombrar archivos de `fuentes de documentacion` sin haber hecho antes el mapa de vigencia y citas cruzadas (DR-32).
- **No confundir el hallazgo de `claude_5` (DR-34, contaminación por memoria mal desactivada) con una fuga tipo DR-30 (detalle operativo no documentado) — son mecanismos distintos y no deben mezclarse si se reporta este resultado más adelante.**

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
