# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-06-19 | **Reemplaza:** toda la serie SESSION_LOG_ANALISIS_C1_2026-06-18_v1 a v5 como punto de partida operativo (quedan como archivo histórico, no como insumo a recargar completo)

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga v4, no carga v5, no carga "fallo DOCUMENTACION 19-06-2026.md". Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM y el proceso de documentación de IRAM — y desde ahí, recién, generar la skill (C2) y reescribir el paper (C1).

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana. No "el mod puede avanzar en paralelo", no ninguna otra instrucción de un log viejo.

---

## POR QUÉ EXISTE ESTE LOG (una sola vez, no se repite en logs futuros)

La serie anterior (v1 a v5) diagnosticó dos errores de fondo en el proyecto de documentación:

1. **Una afirmación narrativa sin evidencia ("la IA no democratiza la programación") se etiquetó como "principio central del paper (definitivo)" y nunca se verificó contra lo que el paper realmente decía.** El corte real pasó al degradar el SKILL v1.0 completo sin inventariar qué se conservaba y qué se descartaba — la frase se cayó como daño colateral, no por decisión explícita.
2. **Una pregunta sin métrica directa (¿quién originó cada decisión, operador o IA?) se contestó con un proxy que no la mide (ratio de caracteres producidos)**, y esa conclusión llegó al paper cerrado sin confrontarse contra el propio caveat del paper en la sección siguiente.

El mecanismo para evitar esto (tablas DEC-xx con fuente primaria) **ya existía y se usó correctamente en casos comparables** (DEC-16, DEC-17). Falló específicamente en estos dos puntos porque dependía de que alguien reconociera, en el momento, que estaba tomando una decisión real. Esta fase rediseña el proceso para que ese reconocimiento no dependa de la memoria de nadie.

**No repetir este diagnóstico en logs futuros.** Si hace falta el detalle completo, está en `SESSION_LOG_ANALISIS_C1_2026-06-18_v4.md` y en la transcripción de esta sesión.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-01 | El proyecto tiene dos objetivos paralelos, no uno: (1) el mod IRAM, (2) la metodología de trabajo con IA. Cada uno con su propio corpus, su propia pregunta de autoría, su propio ciclo de vida. No mezclar las dos historias en un mismo análisis. |
| DR-02 | El paper (C1) deja de ser un filtro obligatorio para la skill (C2). La skill se extrae directo de la base de hechos, nunca del paper. El paper se escribe al final, leyendo la base de hechos, y funciona como explicación para terceros + bitácora de avance del operador — no como autoridad sobre los hechos. |
| DR-03 | El proyecto se detuvo deliberadamente en su punto de mayor dificultad (documentación, no el mod) para extraer la skill ahí, no en el tramo fácil. Esto es evidencia a favor de la tesis, no una interrupción accidental — entra en la base de hechos como hallazgo, categoría a definir en Fase 2. |
| DR-04 | Hay dos corpus de análisis de autoría, no uno: **Corpus A — mod IRAM**, los 5 `claude_N_processed.json` ya disponibles (3 meses, hasta 2026-06-10, desarrollo del mod). **Corpus B — documentación**, conversaciones de los 5 Claudes de los últimos ~10 días (desde 2026-06-10 00:30), que el operador todavía tiene que agrupar y subir. No están listos los dos al mismo tiempo — Corpus A puede procesarse ya. |
| DR-05 | El proceso de documentación tuvo su propio ciclo de vida, paralelo y de la misma forma que el del mod: simple (log/SUPERBACKUP) → complejo (herramientas auxiliares, specs, scripts) → intento de volver a simple → ese intento también falló. Este ciclo, completo, es un hallazgo central a documentar — no una lista plana de incidentes. Vive en Corpus B. |
| DR-06 | La categorización de Spec A (authorship) se corrige: agregar evidencia de tipo diagnóstico técnico (los casos 4B: panel de interfaz, filtro de escala global, INC-13) como categoría de primera clase, no excluida. Sin esto, el script no encuentra el tipo de evidencia que el paper ya identificó como más fuerte. |
| DR-07 | Toda baja de estatus de un documento completo (ej. "el SKILL v1.0 ya no es la base estructural") requiere inventario ítem por ítem de qué se conserva y qué se descarta, antes de que la baja de estatus se considere válida. Aplica retroactivamente a la corrección de WIKI_DOCUMENTACION_v2.md cuando llegue ese paso. |

---

## ESTADO REAL — verificado en esta sesión, no asumido

| Cosa | Estado |
|---|---|
| Mod IRAM | Sustancialmente cerrado. Quedan bugs menores (BUG-1, BUG-3, BUG-4 — ver SESSION_LOG v5.6 del mod, no se tocan en esta fase). |
| Paper C1 (`IRAM_C1_final.md`) | Cerrado en s34, pero con dos afirmaciones sin respaldo (S4A, S5) que se corrigen al final de esta fase, no antes. |
| WIKI_DOCUMENTACION_v2.md | Sigue con la frase de democratización como "principio central (definitivo)", sin tocar desde 2026-06-17 17:13. No se corrige todavía — se corrige después de tener la base de hechos, no antes (corregir el síntoma ahora produciría el mismo error: una afirmación nueva sin el inventario completo que pide DR-07). |
| Corpus A (5 JSON del mod) | Disponible ahora. Sin procesar con la categorización corregida (DR-06). |
| Corpus B (conversaciones de documentación, ~10 días) | No disponible todavía. El operador lo agrupa. |
| Specs A/B/C viejos (`spec_a_authorship.py`, etc.) | Reusar la lógica de normalización de JSON (funciona, ya verificada). Reemplazar las heurísticas de scoring (`SIGNALS_POSITIVE`) para cubrir DR-06 antes de correr sobre Corpus A. |

---

## PRÓXIMO PASO INMEDIATO — lo único que hay que decidir para seguir

Dos caminos posibles, no decidido todavía:

**(a)** Corregir `spec_a_authorship.py` (DR-06) y correrlo sobre Corpus A ahora, en esta sesión o la siguiente, sin esperar Corpus B.
**(b)** Esperar a tener Corpus B agrupado para diseñar las tres tablas de hechos (decisiones, hallazgos técnicos, eventos del propio sistema de documentación) de forma unificada antes de correr nada.

No elegir por defecto. Preguntar al operador al abrir la próxima sesión si no quedó decidido al cierre de esta.

---

## QUÉ NO HACER (aprendido de la serie v1-v5)

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes. Enlazar al archivo, no pegar el contenido.
- No tocar el mod. Bloqueado por decisión del operador, no por dependencia técnica (ver incidente documentado en `SESSION_LOG_ANALISIS_C1_2026-06-18_v4.md`, sección del incidente).
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual. Un ratio o una métrica de volumen no es autoría.
- No bajar el estatus de un documento completo sin el inventario de DR-07.
- No asumir que "puede avanzar en paralelo" de un log viejo sigue vigente. Reconfirmar con el operador.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
