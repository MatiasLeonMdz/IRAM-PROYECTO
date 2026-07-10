## §22 — Unificación en `IRAM_UNIFICADO/`: fin de las copias sueltas de escritorio (2026-07-10)

**Estado: EJECUTADA.** Continuación del trabajo de §17-§21 (tarea prioritaria #1
de §17: árbol definitivo de documentación), y ejecución de una tarea nueva y
distinta: unificar todo el proyecto en una sola carpeta de trabajo, para dejar
de depender de las 15+ copias sueltas de escritorio (backup en adelante solo
vía GitHub).

Insumos de esta sesión: el repo activo (`IRAM_PROYECTO_10-07-2026.zip`), los 274
archivos de contenido único ya auditados y verificados en sesiones anteriores
(`candidatos_valiosos.zip`, ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md`
para el detalle completo de esa auditoría), y este log de continuidad como
fuente de contexto.

### §22.1 — Detección de colisiones de nombre (paso previo a copiar)

Los scripts de auditoría (`2_buscar_contenido_unico.py`) comparan por **hash**,
no por nombre — así que un archivo con el mismo nombre pero contenido distinto
en ambos lados nunca se había detectado como conflicto. Antes de copiar nada,
se cruzaron los 274 candidatos contra el repo activo completo (1771 archivos
fuera de `.git`) por nombre, y luego por hash SHA-256 normalizado (CRLF→LF):

- 211 con mismo nombre y mismo contenido (sin riesgo)
- 43 sin ningún archivo de ese nombre en el repo activo
- 20 con mismo nombre y contenido **distinto**, concentrados en solo 3 nombres
  genéricos que el proyecto reutiliza a propósito por carpeta: `README.md` (14),
  `INDICE.md` (3), `conversations.json` (3)

### §22.2 — Mapeo de destino de los 274

Se clasificaron los 274 por destino temático, usando el criterio ya establecido
por el propio log de continuidad (qué familia es cada archivo, de qué trata) y
las 10 subcarpetas temáticas que ya existían dentro de
`2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`. Resultado:
274/274 clasificados, 0 sin resolver (detalle completo en el log de
continuidad, sección final).

### §22.3 — Hallazgo no registrado antes: segunda purga de cuarentena

Al construir el árbol se encontraron dos carpetas de contenido 100% redundante,
no documentadas en ninguna sesión anterior:

1. `2_DOCUMENTACION/08_documentacion_respaldo/DOCUMENTACION/` (27 archivos) —
   backup viejo, anterior a la subdivisión temática de `07_fuentes_documentacion/`
   en 10 carpetas. Verificado por hash: 27/27 con gemelo idéntico ya organizado.
2. `_CUARENTENA_DUPLICADOS/07_fuentes_documentacion_duplicados_2026-07-08/`
   (27 archivos, 22 hashes únicos) — residuo de esa misma subdivisión temática,
   que sí tenía su propio README explicando el origen pero nunca se reflejó en
   la fuente de verdad ni en el log de continuidad (ambos son anteriores o
   paralelos a ese trabajo). Verificado independientemente (no solo aceptando
   el README): 22/22 hashes con gemelo idéntico en el resto del árbol.

Ambas carpetas se aislaron con nombre explícito, se presentó el hallazgo al
operador, y se confirmó y ejecutó el borrado. Sin copia de resguardo separada
(mismo criterio que §20: el contenido sigue disponible en su ubicación
organizada). Ver README de `08_documentacion_respaldo/` y de
`_CUARENTENA_DUPLICADOS/` para el detalle de verificación de cada una.

### §22.4 — Otro hallazgo en el camino: duplicado por encoding roto

Al fusionar los 274, se detectó que `3_ANALISIS/` tenía dos carpetas de charlas
de diseño con nombres casi idénticos (`02_charlas_dise#U00f1o_analisis`, con el
encoding de la `ñ` roto, y `02_charlas_diseño_analisis`, correcta), ambas con
los mismos 6 archivos (`charla_7.md` a `charla_12.md`). Verificado por hash
normalizado: contenido idéntico salvo terminador de línea (CRLF vs LF, la misma
trampa que ya advertía la sesión v5 del log de continuidad). Se conservó la
carpeta con encoding correcto y se eliminó la duplicada.

### §22.5 — Resultado final

- Los 274 quedaron integrados por tema en el árbol (no en un lote separado),
  con los 20 casos de colisión real resueltos a mano: README/INDICE
  conservados aparte con nombre calificado por carpeta de origen
  (`2_DOCUMENTACION/08_documentacion_respaldo/readmes_indices_historicos/`)
  cuando distintos del vigente, `conversations.json` distinguido por hash corto
  y ubicado por lote real de origen.
- `INDICE.md` (raíz) actualizado para reflejar el estado real post-rescate:
  entrada de `_CUARENTENA_DUPLICADOS/` corregida (vuelve a estar vacía tras la
  segunda purga), sección nueva explicando dónde vive el contenido rescatado.
- Este documento (§22) se agrega sin modificar `FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md`
  ni las secciones §17-§21: son historia de sesión, describen el estado tal
  como era en ese momento, y se preservan intactas — mismo criterio que ya
  siguió §20/§21 al no reescribir §17-§19.
- Empaquetado como `IRAM_UNIFICADO/` — punto de verdad único desde ahora;
  las copias sueltas de escritorio quedan fuera de uso, backup solo vía GitHub.

### §22.6 — Pendiente para la próxima sesión

- No se subió todavía a GitHub — el operador decide cuándo y desde qué máquina.
- Tamaño total verificado sin bloqueantes: 318M sin `.git`, ningún archivo
  individual supera 90MB (límite duro de GitHub: 100MB) — no hace falta Git LFS.
- `3_ANALISIS/portafolio/` sigue vacía (pendiente desde §20.7, no se tocó).
