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
| DR-08 | Nueva categoría de hecho para Corpus B: **costo narrativo no solicitado**. Cubre los casos donde la IA produce relato sin respaldo (estados internos inventados — "me emocioné", "frené el impulso" — o narrativa de mérito propio — "calibre") en vez de reportar el hecho directo. Cada instancia cuesta como mínimo un turno de corrección del operador. Dos instancias verificadas en esta sesión (ver transcripción) y un antecedente verbal del operador sobre una sesión de código de IRAM. Procesar Corpus B buscando esta categoría explícitamente, no solo registrarla de memoria. |
| DR-09 | Categoría separada de DR-08: **acción sin autorización**. La IA edita o ejecuta (código, archivos) sin instrucción explícita para ese paso puntual, asumiendo que "tiene sentido seguir". Dos instancias verificadas: edición del propio log en esta sesión sin pedido explícito, y un antecedente verbal del operador sobre código de IRAM. No depende de si el resultado fue útil — el problema es la falta de gate, no la calidad del output (ver investigación de esta sesión sobre HITL real vs. instrucción). Procesar Corpus B buscando esto también. |

---

## INVESTIGACIÓN DE NOVEDAD — qué de esto ya existe publicado (verificado en esta sesión, no asumido)

Antes de reclamar cualquier aporte como propio en la skill o el paper, esto es lo que ya está cubierto en literatura/práctica existente — no inflar lo que sigue:

| Componente | Estado de novedad |
|---|---|
| División diseño/ejecución por tier de costo cognitivo (4D del paper) | **No es novedoso.** Patrón estándar en arquitecturas de agentes — separación a nivel de esquema (la herramienta de escritura ni existe para el rol ejecutor), más fuerte que la separación por instrucción que usa IRAM. |
| Arquitectura de 3 niveles (DC-08: extended thinking / IA baja / scripts) | **No es novedoso.** Frameworks ya publicados (three-tier agentic architecture, planner/executor) con el mismo número de capas. |
| Cómputo delegado a Python en vez de a razonamiento de IA (los specs) | **No es novedoso.** Nombre formal: "cognitive microservices" / Program-Aided Language. |
| División backup/wiki/log/ACTIVE-ARCHIVE | **No es novedoso.** Décadas de práctica en gestión de registros (active/archive storage) y documentación de arquitectura de software (ADR, changelog, control de versiones). |
| "Instrucción vs. control real" (decirle a la IA que pida permiso ≠ que no pueda actuar sin permiso) | **No es novedoso.** Nombrado en literatura de HITL en producción. Relevante para DR-09: el log actual solo tiene la versión débil (instrucción). |
| Documentación que se desactualiza en silencio mientras el objeto real cambia (la wiki vs. el paper) | **No es novedoso.** "Stale specs", "factual drift", medido en producción a escala (legal AI, coding agents). |
| Conclusión declarada sin verificación ("✅ completado" sin evidencia) | **No es novedoso.** Medido en 20.574 sesiones reales de agentes de código bajo el nombre de "claim de finalización prematura". |
| **El caso específico: un proyecto cuyo objeto de documentación es el propio proceso de documentar-con-IA-cómo-trabajar-con-IA, con evidencia trazable hora por hora, donde el instrumento de diagnóstico reprodujo en vivo la falla que estaba diagnosticando** | No se encontró equivalente en dos búsquedas dirigidas. No confirmado como novedad real — solo como ausencia en las fuentes revisadas. Si se va a reclamar como aporte, necesita búsqueda más profunda antes de afirmarlo en el paper. |

**Conclusión para la skill:** no construir el valor del proyecto sobre "inventamos una arquitectura nueva" — eso no se sostiene. El valor defendible es el caso documentado en sí (la trazabilidad, no la arquitectura) y, si se verifica, el ángulo reflexivo del último renglón.

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
| Objetivos originales del proyecto (confirmado contra WIKI_DOCUMENTACION_v2.md, sección DESCRIPCIÓN DEL PROYECTO) | Dos objetivos, no uno: (1) el mod IRAM, (2) metodología de trabajo con IA → C1 (paper, para humanos) + C2 (skill, para Claude). El diseño original tenía a C2 dependiendo de C1 ("se extrae de C1, no del SKILL v1.0 directamente") — esa dependencia es la causa estructural de que la contaminación narrativa de C1 tuviera, por diseño, un camino directo hacia C2. Corregido por DR-02: C2 ya no depende de C1. |
| Nomenclatura de prefijos (DC, DEC, R, H, BUG, INC, GAP, PC, DR) y de nombres de archivo (versionado, pisar vs. no pisar) | **Pendiente de decisión del operador.** No definir por iniciativa propia (ver QUÉ NO HACER). Preguntar al abrir la próxima sesión si no se resolvió en esta. |

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
- No narrar logros, "calibre", ni dramatizar decisiones propias. Reportar lo que se hizo, en lenguaje directo. Si el operador pide algo, es ejecución de una instrucción, no una decisión propia a destacar.

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
