# SESSION LOG — Replanteo del proyecto IRAM/Documentación
**Fecha:** 2026-06-20 | **Reemplaza como punto de partida operativo:** SESSION_LOG_REPLANTEO_2026-06-19_2.md (queda como archivo histórico, no como insumo a recargar completo)

---

## LEER ESTO PRIMERO — Y SOLO ESTO, ANTES DE ABRIR CUALQUIER OTRO ARCHIVO

Si esta sesión se corta, la siguiente sesión carga **únicamente este documento** para saber qué hacer. No carga logs anteriores, no carga la serie v1-v5, no carga el log del 19/06 completo. Esos quedan como evidencia histórica, citables si hace falta el detalle de algo puntual, pero no como punto de partida.

**Prioridad única de esta fase, en una línea:** construir una base de hechos verificada (sin narrativa, sin proxies) para dos corpus paralelos — el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B) — y desde ahí, recién, generar la skill (C2), reescribir el paper (C1), y armar el portfolio de data science.

Si en algún momento una decisión de esta sesión entra en conflicto con esa línea, esa línea gana.

---

## DECISIONES ANTERIORES VIGENTES — NO REDEBATIR

Las decisiones DR-01 a DR-09 del SESSION_LOG_REPLANTEO_2026-06-19_2.md siguen vigentes sin modificación. No se repiten acá — se citan por ID. Si hace falta el detalle, ir al log del 19/06.

---

## DECISIONES DE ESTA SESIÓN — NO REDEBATIR

| ID | Decisión |
|----|----------|
| DR-10 | El proyecto tiene un tercer objetivo operativo además del mod y la metodología: **portfolio de data science**. No es un objetivo nuevo — estaba en el STRATEGIC LOG del 27/05 ("objetivo real: ciencia de datos") pero nunca había entrado al sistema operativo del replanteo. Desde esta sesión vive acá. |
| DR-11 | El análisis comparativo Corpus A/B es el **núcleo único** que sirve para los tres usos: paper (C1), skill (C2) y portfolio. No son tres trabajos separados — es un solo análisis bien hecho presentado para tres audiencias. |
| DR-12 | La WIKI_DOCUMENTACION_v2.md **no se toca todavía**. Corregirla antes de tener la base de hechos del análisis A/B produce el mismo error que se está corrigiendo. DR-07 aplica: inventario ítem por ítem antes de cualquier baja de estatus. |
| DR-13 | El portfolio se presenta como **trabajo sin equivalente publicado verificado**: un proyecto donde el objeto de documentación es el propio proceso de trabajar con IA, con evidencia trazable hora por hora, donde el instrumento de diagnóstico reprodujo en vivo la falla que estaba diagnosticando. Caveat obligatorio: esto es ausencia en las fuentes revisadas el 19/06, no confirmación de novedad — requiere búsqueda más profunda antes de afirmarlo en el paper. |
| DR-14 | El portfolio habla a **dos audiencias simultáneas**: mercado de data science (dataset real, análisis comparativo, metodología reproducible) y mercado de IA aplicada (cómo trabajar con IA con evidencia, no con opinión). No son presentaciones separadas — el mismo trabajo, dos ángulos. |
| DR-15 | Las métricas del análisis se organizan en **tres grupos** con distinto nivel de esfuerzo (ver sección DISEÑO DEL ANÁLISIS abajo). No medir todo junto sin filtro — eso reproduce el error de T2 a mayor escala. |
| DR-16 | El mismo set de métricas se aplica a **los dos corpus en paralelo** para poder comparar cómo se comportó el sistema operador+IA en tarea técnica (Corpus A) vs. tarea metodológica (Corpus B). Ese contraste es el hallazgo más interesante del proyecto y todavía no tiene evidencia cuantitativa. |
| DR-17 | El Corpus B tiene los zips crudos disponibles. El operador los agrupa cuando sea el momento. No es un bloqueo — es una tarea pendiente con material ya disponible. |
| DR-18 | El timeline tentativo (listo para postularse a puestos remotos entry-level en noviembre/diciembre 2026) está **condicionado a los números reales del Corpus A**. No es una proyección confirmada — es lo que resulta de cruzar el ritmo estimado (3 horas/día promedio, picos de 6 en reworks pesados) con el stack técnico que falta aprender. Los números reales los da el análisis. |
| DR-19 | Stack técnico pendiente para data science, en orden de prioridad: Python con pandas (base ya existe en scripts del proyecto), SQL básico, Power BI o Tableau. Ninguno requiere prerequisito que el operador no tenga. |
| DR-20 | El proyecto final integrador de la diplomatura UTN se presenta usando IRAM como caso real — no un dataset de ejercicio. Es más sólido que el 95% de los proyectos entry-level que usan datasets de Kaggle genéricos. |

---

## DISEÑO DEL ANÁLISIS — MÉTRICAS POR GRUPO

### Grupo 1 — Métricas directas del corpus (salen de los JSON sin anotación manual)
Aplicar a Corpus A y Corpus B para comparación:

- Horas totales del proyecto
- Horas por sesión
- Distribución por fase (diseño vs. ejecución vs. debugging vs. documentación)
- Duración promedio de sesión
- Picos de intensidad (sesiones con más de X horas)
- Volumen por cuenta (Corpus A: 5 cuentas)
- Ratio mensajes operador/IA por fase
- Distribución temporal (hora del día, día de semana)
- Sesiones cortadas vs. completadas
- Velocidad de respuesta por tipo de tarea

### Grupo 2 — Autoría y decisiones (requieren categorización asistida + anotación manual)
Categorías DR-06 corregidas — aplicar a los dos corpus:

- OP_ARCH: operador originó la decisión de arquitectura
- IA_PROP_AC: IA propuso, operador aceptó
- IA_PROP_RJ: IA propuso, operador rechazó
- COLAB: resultado emergió de la interacción
- IA_DIAG_OP_DEC: diagnóstico técnico de IA, decisión del operador (categoría nueva DR-06 — casos tipo 4B, INC-13)
- Instancias DR-08: narrativa sin respaldo (estados internos inventados, mérito propio no solicitado)
- Instancias DR-09: acción sin autorización (IA edita o ejecuta sin instrucción explícita)
- Ratio propuestas IA aceptadas vs. rechazadas por fase

### Grupo 3 — Ciclo de vida del sistema de documentación (para DR-05, Corpus B principalmente)
- Cuándo apareció cada práctica, con fecha exacta
- Qué la detonó (pérdida, fricción, decisión explícita)
- El arco completo simple→complejo→intento de vuelta a simple, con timestamps
- Costo de cada transición (sesiones perdidas, trabajo rehecho)

---

## EVALUACIÓN DEL OPERADOR — VERIFICADA EN ESTA SESIÓN

Registrado como hecho, no como valoración subjetiva. Fuentes: STRATEGIC LOG 2026-05-27, hitos_v7, SESSION_LOG_DOCUMENTACION_s24, IRAM_C1_final.md S6, sesión de hoy.

### Lo que está verificado con evidencia directa:
- Detectó los dos errores sistémicos del proyecto (democratización + proxy de autoría) rastreando hasta fuente primaria, sin conocer los nombres técnicos de esos errores antes de hacerlo.
- 6 hitos con autoría "Operador-iniciativa" en el historial; 7 hitos colaborativos donde el operador inició o eligió la dirección.
- Decisiones de arquitectura del mod que la IA no pudo resolver (spawn de unidades v1, scope global v3, workaround de rivales v2) — confirmado en STRATEGIC LOG línea 2269.
- Detectó en tiempo real narrativa sin respaldo y acción sin autorización de la IA en la sesión del 19/06 (DR-08, DR-09).
- Trabajo cuantitativo real en el mod: modelo económico, simuladores Optimize, grid search de 17 combinaciones de parámetros — confirmado en STRATEGIC LOG línea 2274.

### Conexión IRAM → data science (verificada en STRATEGIC LOG + paper S6):
- Modelo económico → modelado estadístico
- Simuladores Optimize → simulación y análisis de sensibilidad
- ETL: conversations.json → deduplicación → historial unificado (process_iram_v2.py)
- Interrupted time series: 4 puntos de corte con métricas consistentes
- Grid search: barrido de 17 combinaciones de parámetros
- RAG manual, HITL, deuda técnica en tres formas, ADRs, specification-driven development — todos llegados por fricción, no por conocimiento previo.

### Lo que esta evaluación no puede confirmar todavía:
- Horas reales por sesión y por fase — lo da el Corpus A.
- Comparación contra "alguien con el mismo background" — no hay vara objetiva.
- Novedad real del proyecto vs. ausencia en fuentes revisadas — requiere búsqueda más profunda.

---

## CONTEXTO DE DATA SCIENCE Y MERCADO LABORAL — VERIFICADO EN ESTA SESIÓN

### La diplomatura UTN (Ciencia de Datos e IA, 21 semanas, 157 horas):
- Enfoque no-code/low-code — objetivo explícito: sin necesidad de programar.
- Cubre: pensamiento analítico, cultura data-driven, herramientas visuales, ML conceptual, IA generativa, automatización no-code, NLP introductorio, visión por computadora introductoria.
- No cubre: Python técnico, pandas, SQL, estadística formal, Jupyter notebooks, scikit-learn.
- Valor real: certificado UTN + marco conceptual + proyecto final integrador (usar IRAM como caso real — DR-20).

### Stack técnico pendiente para rol técnico remoto:
| Skill | Estado | Tiempo estimado con ritmo actual |
|-------|--------|----------------------------------|
| Python con pandas | En desarrollo — base en scripts del proyecto | 3-4 meses |
| SQL básico | No tocado | 1 mes en paralelo |
| Power BI o Tableau | No tocado | 3-4 semanas |
| Portfolio con Corpus A presentable | Depende de los anteriores | 1 mes adicional |

### Mercado laboral Mendoza / remoto (verificado en búsqueda de esta sesión):
- Mendoza presencial: ~12 ofertas activas de analista de datos, 1 sin experiencia.
- Mercado relevante: remoto Argentina + exterior — ahí está el volumen real.
- Lo que piden los puestos remotos entry-level: SQL, Python con pandas, Power BI o Tableau, proyecto propio que mostrar.
- No filtran por título universitario — filtran por stack técnico y evidencia de trabajo real.
- El Corpus A/B resuelve el problema más común del candidato entry-level: no tener nada real que mostrar.

### Timeline tentativo (condicionado a números reales del Corpus A):
- Agosto 2026: cierre diplomatura + Python funcional con pandas
- Septiembre 2026: SQL básico
- Octubre 2026: Power BI o Tableau
- Noviembre/Diciembre 2026: portfolio con Corpus A presentable, listo para postularse

---

## ESTADO REAL — ACTUALIZADO AL 2026-06-20

| Cosa | Estado |
|------|--------|
| Mod IRAM | Sustancialmente cerrado. BUG-1, BUG-3, BUG-4 corregidos en v5.6. Quedan bugs menores — no se tocan en esta fase. |
| Paper C1 (IRAM_C1_final.md) | Cerrado en s34, con dos afirmaciones sin respaldo (S4A, S5) — se corrigen después del análisis A/B, no antes. |
| WIKI_DOCUMENTACION_v2.md | Sigue con la frase de democratización como "principio central (definitivo)" — no se toca hasta tener base de hechos (DR-12). |
| Corpus A (5 JSON del mod) | Disponible. Sin procesar con categorización corregida (DR-06). Primer paso del análisis. |
| Corpus B (conversaciones de documentación) | Zips crudos disponibles. El operador los agrupa. No es bloqueo. |
| Specs A/B/C viejos | Reusar lógica de normalización de JSON. Reemplazar heurísticas de scoring para cubrir DR-06 y DR-16 antes de correr. |
| Diplomatura UTN | Recién empezada. Cierre estimado agosto 2026. |
| Python | Recién empezando. En desarrollo activo. |
| Stack DS restante | SQL, Power BI/Tableau — pendiente después de Python. |

---

## PRÓXIMO PASO INMEDIATO

Dos decisiones que siguen sin resolverse desde el 19/06 — elegir una antes de arrancar:

**(a)** Corregir spec_a_authorship.py (DR-06 + DR-16) y correr sobre Corpus A ahora, sin esperar Corpus B.
**(b)** Esperar a tener Corpus B agrupado para diseñar las tres tablas de hechos de forma unificada antes de correr nada.

No elegir por defecto. Preguntar al operador al abrir la próxima sesión.

---

## QUÉ NO HACER — VIGENTE DE SESIONES ANTERIORES + AGREGADOS DE ESTA SESIÓN

- No copiar el historial completo de sesiones anteriores hacia este log ni hacia los siguientes.
- No tocar el mod.
- No declarar nada "✅ completado" sobre una pregunta de autoría sin categoría real con cita textual.
- No bajar el estatus de ningún documento sin el inventario de DR-07.
- No asumir que algo "puede avanzar en paralelo" sin confirmación del operador.
- No narrar logros, "calibre", ni dramatizar decisiones propias.
- No llamar a actualizar el log sin instrucción explícita del operador (DR-09 — aprendido en sesión del 19/06 y reincidente en sesión del 20/06).
- No proponer métricas sin anclarlas a una pregunta concreta — evitar repetir el error de T2 a mayor escala.
- No afirmar novedad del proyecto sin búsqueda más profunda — solo "ausencia en fuentes revisadas el 19/06".
- No tocar WIKI_DOCUMENTACION_v2.md hasta tener la base de hechos del análisis A/B (DR-12).

---

*Este log se mantiene corto a propósito. Si crece más allá de esto, es señal de que está absorbiendo trabajo que debería vivir en la base de hechos, no en el log.*
