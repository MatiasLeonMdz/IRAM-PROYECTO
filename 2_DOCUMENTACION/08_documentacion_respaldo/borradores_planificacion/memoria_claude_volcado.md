# Volcado de memoria — Claude Sonnet 5 (claude.ai)
Fecha de extracción: 2026-07-03
Modelo: Claude Sonnet 5

> Nota: esto es un resumen de lo que se me inyectó como memoria persistente al inicio
> de ESTA conversación puntual — no una garantía de volcado completo de todo lo que
> el sistema de memoria de Anthropic pueda tener almacenado. No es un log textual ni
> tiene marcas de tiempo exactas por dato; se reconstruye por categorías. Puede haber
> conversaciones recientes aún no procesadas hacia memoria, y no tengo forma de
> verificar si existe contenido adicional que no se me haya pasado en este contexto.
> Usar como insumo de contraste, no como fuente canónica ni completa.

---

## 1. Contexto académico (Diplomatura UTN)

- Cursando la Diplomatura en Ciencia de Datos e Inteligencia Artificial, UTN BA
  (5 módulos, 21 semanas).
- El proyecto IRAM conecta directamente con el proyecto final de Módulo 5.
- Nivel relativo por módulo:
  - Módulo 4 (IA Generativa): la profundidad práctica del usuario en GenAI
    **supera** el contenido del curso.
  - Módulo 3 (teoría de ML): territorio genuinamente nuevo para el usuario.

## 2. Perfil personal / estilo de trabajo

- Background en modding de juegos: EU4, Imperator Rome.
- Metodología: enfoque lógico-primero — construye modelos abstractos antes
  de escribir código.
- Comunicación: terca/directa, corrige errores de framing con precisión.
- Preferencia: sistemas estructurados y versionados para gestionar
  conocimiento en proyectos de largo aliento.

## 3. Proyecto IRAM — estado "top of mind" (más reciente)

- Fase avanzada de documentación y análisis.
- Arquitectura de tres sesiones (**DC-08**) en curso para analizar el historial
  completo de conversación (~7.345 mensajes deduplicados, 5 cuentas de Claude)
  y mejorar tanto el mod como el paper de investigación (`IRAM_C1_final.md`).
  - Sesión 1: diseñó 3 specs de investigación + scripts Python de extracción:
    - **Spec A**: análisis de autoría
    - **Spec B**: trazado del principio de "democratización"
    - **Spec C**: completar Sección 21 de la wiki
  - Sesión 2: ejecución mecánica de esos scripts (scoped, aún no ejecutada
    según la última info que tengo).
  - Sesión 3: síntesis.
- **Problema estructural abierto (DC-06)**: la wiki etiqueta incorrectamente
  el principio "la IA no democratiza la programación" como el claim central
  del paper — el paper no dice eso. Pendiente de corrección.

## 4. Historial reciente (meses previos, según memoria)

- Revisión estructural significativa del paper C1 a mediados de junio 2026,
  en múltiples sesiones.
- Sesiones tempranas de ese período:
  - Recuperación de logs de sesión perdidos por interrupciones.
  - Corrección de un framing obsoleto: **SKILL v1.0 NO es la base estructural
    de C1** — la base real es el "esqueleto" de la sesión 17 (s17).
  - Identificación de "nueve correcciones de criterio" como columna vertebral
    analítica de C1.
- Sesión de crítica rigurosa reveló:
  - Un error de categoría: se aplicaban estándares académicos a un documento
    de aprendizaje.
  - Patrón de "tiering": diseño en alta capacidad de IA, ejecución en baja
    capacidad de IA — no documentado en ningún lado hasta ese momento.
  - El **PROMPT_MAESTRO** identificado como el artefacto transferible
    genuinamente central del proyecto.
  - Tres patrones operativos nunca antes capturados en documentación.
- Estado de secciones del paper en ese momento:
  - S1–S4: ✅
  - S6–S7: ✅
  - S5: ❌ (bloqueada, pendiente de datos cuantitativos)
- Sistema multi-sesión de 4 archivos interconectados:
  - `PROMPT_REGLAS`
  - `WIKI_DOCUMENTACION`
  - `SESSION_LOG`
  - `TEMPLATES_DOCUMENTACION`
- Protocolo de trabajo clave (posiblemente ya en tus reglas, pero lo repito
  por completitud):
  - Claude debe leer todos los archivos subidos antes de actuar.
  - No debe escribir ni ejecutar sin confirmación.
  - No debe afirmar haber leído material que no verificó.
- Nota explícita: los SESSION_LOG funcionan como **specs ejecutables** para
  futuras instancias de Claude, no como registro histórico pasivo.

## 5. Historial anterior (principios / mediados de junio 2026)

- Fase de análisis cuantitativo (**Plantilla D**) completada en varias sesiones.
- 5 archivos JSON procesados (`claude_1` a `claude_5`).
- Hallazgo central: el ratio creciente Investigación/Código a través de las
  fases (1.8x → 2.9x) refleja **planificación estructurada antes de actuar**,
  no debugging reactivo — confirmado por tasa de error plana y % creciente
  de `doc_plan`.
- **Corrección factual crítica**: las 5 cuentas de Claude fueron reinicios
  secuenciales tras cortes de contexto / errores de conexión — **no** trabajo
  paralelo deliberado. Esto pone en riesgo supuestos de documentos previos:
  - `PROMPT_MAESTRO R18`
  - `Plantilla D Block 2`
  - Un hito llamado "cuentas_paralelas"
  → revisar si esos documentos asumen paralelismo real y corregir si es así.
- Pipeline de procesamiento completo produjo un historial unificado:
  **441 conversaciones, 7.345 mensajes post-deduplicación**.
- Se identificó y corrigió una violación de reglas: se habían acumulado
  múltiples logs de sesión separados en vez de un único log consolidado
  (como exige el sistema de documentación).

## 6. Trasfondo de largo plazo

- **Origen del proyecto**: IRAM (Imperator Rome Alternative Mechanics Mod)
  nace de la experiencia en modding de EU4.
- Construido con un modelo lógico abstracto (analogía tablero/casillero/pieza)
  como herramienta de razonamiento **antes** de escribir código.
- **Evolución en 5 versiones**:
  - v1–v2: Drago Mod Pack, mecánicas básicas de spawn.
  - v3: renombrado a IRAM, unificación de código.
  - v4: expansión económica/demográfica; forzó el split ACTIVE/ARCHIVE de la
    wiki por tamaño del backup.
  - v5: reorganización final, corrección de bugs.
- El rename a "IRAM" marcó un cambio de identidad: de utilidad personal a
  overhaul completo de mecánicas.
- **Hallazgo metodológico clave**: tres capas de lenguaje en conflicto —
  terminología del wiki del juego base, terminología del código del engine,
  y vocabulario del modelo lógico propio del proyecto — mutuamente
  incompatibles. Esto explica por qué una wiki propia del proyecto era
  cualitativamente necesaria (no solo conveniente).
- El sistema de documentación (PROMPT_MAESTRO, SESSION_LOG, TECHNICAL_WIKI)
  emergió causalmente:
  - Cortes de sesión → crecimiento de backups.
  - Instrucciones/contexto mezclado → Claude se saltaba reglas.
  - Complejidad creciente del proyecto → necesidad del SESSION_LOG.
- Carga de contexto del proyecto bajó de ~5MB (archivos del juego + wiki +
  código base) a ~350KB (wiki propia + PROMPT_MAESTRO + SESSION_LOG) —
  constituye una serie temporal interrumpida natural con 4 puntos de
  intervención fechados.

---

## Preguntas para cruzar contra wikis/logs

Al comparar esto contra `WIKI_DOCUMENTACION`, `SESSION_LOG` y `PROMPT_MAESTRO`
actuales, conviene chequear puntualmente:

1. ¿El hallazgo de las "5 cuentas secuenciales" (no paralelas) ya está
   propagado y corregido en `PROMPT_MAESTRO R18` y `Plantilla D Block 2`?
   ¿Y en el hito "cuentas_paralelas"?
2. ¿El problema **DC-06** (mislabel del principio "democratización" como
   claim central) sigue abierto o ya se corrigió en la wiki?
3. ¿Los tres patrones operativos "nunca antes documentados" (de la sesión
   de crítica rigurosa) ya fueron incorporados a algún archivo, o siguen
   solo en esta memoria y en ningún .md?
4. ¿El estado S5 ❌ del paper (bloqueado por falta de datos cuantitativos)
   sigue así, o ya se resolvió con la Plantilla D / Spec A-B-C?
5. ¿La corrección "SKILL v1.0 no es la base estructural — es el esqueleto
   de s17" está reflejada consistentemente en todos los documentos, o
   quedó alguna referencia vieja sin actualizar?
6. ¿DC-08 Sesión 2 (ejecución de los scripts A/B/C) ya se corrió? Esta
   memoria no tiene ese dato confirmado.
