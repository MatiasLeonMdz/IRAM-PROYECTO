# LOG DE SESIÓN — Hallazgo en `08_documentacion_respaldo`, resolución y commit único de cierre (2026-07-10, continuación)

**Punto de partida:** `IRAM_UNIFICADO_corregido_10-07-2026.zip`, exactamente
en el estado que describía `LOG_SESION_2026-07-10_auditoria-verificacion-cierre.md`
(50 cambios sin commitear: 29 borrados sin stage + 6 borrados en stage + 1
modificación + 2 renombres + 12 untracked; 4 commits intactos). Re-verificado
de forma independiente al arrancar esta sesión, coincidía en todo.

**Punto de llegada:** un nuevo commit en git (el commit único de cierre que
venía pendiente desde §24.5 de la fuente de verdad), con dos correcciones
adicionales encontradas y resueltas en el camino (ver §1). La planificación
de los 4 productos del proyecto queda para la próxima sesión, a pedido
explícito del operador.

---

## 1. Qué se hizo esta sesión

### 1.1 — Hallazgo: `08_documentacion_respaldo/` y `datos_config_mod_rescatados/` no coincidían con lo que la fuente de verdad decía

El operador adjuntó, junto con logs de sesiones anteriores, dos READMEs
sueltos (`README_datos_config_mod_rescatados.md` y
`README_08_documentacion_respaldo.md`) que **no coincidían** con las
versiones reales dentro del zip:

- El README de `08_documentacion_respaldo/` que vive en el zip listaba 4
  subcarpetas (`historiales_completos/`, `reorganizaciones/`,
  `borradores_planificacion/`, `readmes_indices_historicos/`) como vigentes.
  El README suelto, y también §23.3 de la propia fuente de verdad (más
  arriba en el mismo documento), decían que las primeras 3 **ya habían sido
  eliminadas** por 100% redundantes. Pero en el zip, las 3 seguían
  físicamente presentes y trackeadas en git, sin ningún `D` en `git status`
  — a diferencia de `03_rescatados_274/` y `herramientas_backups_rescatados/`,
  que sí estaban correctamente borradas.
- El README de `datos_config_mod_rescatados/` que vive en el zip decía "8
  archivos, sin verificar todavía si hay redundancia". El README suelto
  decía "5 archivos, 3 duplicados ya eliminados". En el zip real, seguían
  los 8.

Ninguno de los 6 logs de sesión posteriores a §23 (fix-encoding,
rescatados-corpus, duplicados-menores, ni la propia sesión de auditoría de
verificación) había detectado esta discrepancia — la auditoría de
verificación se había enfocado en los ítems #6, #7 y #9, no en
`08_documentacion_respaldo/` ni en `datos_config_mod_rescatados/`.

### 1.2 — Verificación por hash antes de tocar nada

Se re-verificó cada afirmación, sin dar por buena ninguna de las dos
versiones de README, con hash normalizado (CRLF→LF) contra el contenido
real del árbol:

- **`historiales_completos/`** (15 archivos): 11 idénticos por nombre a
  `1_MOD/06_historial_desarrollo/`; 3 idénticos a
  `2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`; 1
  idéntico a `1_MOD/IRAM_legacy v1 v2 v3 v4/IRAM_SUPERBACKUP_v2_1.md`. 15 de
  15 confirmados redundantes.
- **`reorganizaciones/`** (4 archivos): idénticos a los 4 archivos que
  vivían en `00_fuente_de_verdad/` hasta que se borraron de ahí en una
  sesión previa (ver `PROMPT_CONTINUACION_2026-07-10.md`, punto #2). 4 de 4
  confirmados redundantes.
- **`borradores_planificacion/`** (5 archivos): idénticos a material en
  `00b_descartables/` (2), `3_ANALISIS/04_prueba_fuga_memoria/` (2) y
  `2_DOCUMENTACION/02_charlas_y_resumenes/` (1). 5 de 5 confirmados
  redundantes.
- **`datos_config_mod_rescatados/`** (8 archivos): comparados por hash
  contra **todo** el contenido de
  `1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/`
  (no solo por nombre, porque los nombres reales no coinciden 1:1). Los 5
  `exodus_*` no tienen gemelo de contenido — únicos. `tgl_decisions.txt`,
  `tlv_decisions.txt` y `tlv_events.txt` sí son duplicados exactos con otro
  nombre (`exodos_decisions_tgl.txt`, `exodos_decisions_tlv.txt`,
  `events/tlv_events.txt`).

### 1.3 — Aplicación

Con las 27 redundancias confirmadas (24 + 3), se aplicó con autorización
explícita del operador (elegida entre tres opciones ofrecidas: verificar y
borrar si procede / dejar sin tocar / borrar sin re-verificar — se eligió
"verificar y borrar"):

- `git rm -r` sobre `historiales_completos/`, `reorganizaciones/` y
  `borradores_planificacion/` completas (24 archivos).
- `git rm` sobre los 3 archivos duplicados de `datos_config_mod_rescatados/`
  (`tgl_decisions.txt`, `tlv_decisions.txt`, `tlv_events.txt`).
- README de `08_documentacion_respaldo/` reescrito: refleja que solo queda
  `readmes_indices_historicos/`, documenta cada subcarpeta eliminada y su
  equivalente vigente, y corrige la cita a la fuente de verdad (apuntaba a
  la versión `_11`, vieja; ahora apunta a `_12`, la vigente).
- README de `datos_config_mod_rescatados/` actualizado a partir del que
  adjuntó el operador (con la cita al README de `08_documentacion_respaldo`
  corregida al nombre de archivo real).

### 1.4 — Fuente de verdad actualizada (§25, append-only)

Se agregó §25 a `FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md`, consolidando en
un solo lugar (append-only, sin reescribir §1-§24) las seis sesiones que
pasaron entre el cierre de §24 y este commit: fix de encoding (§25.2),
resolución de `rescatado__*` (§25.3), duplicados menores (§25.4), auditoría
de verificación (§25.5), el hallazgo y resolución de esta sesión en
`08_documentacion_respaldo/` (§25.6) y `datos_config_mod_rescatados/`
(§25.7), verificación de integridad (§25.8), el commit (§25.9) y pendientes
para la próxima sesión (§25.10) — incluida la advertencia explícita de que
`plan.md` es previo a la resolución de DR-54 y a la reorganización de
§17-§24, y no debe tomarse como estructura de carpetas vigente sin cotejar.

### 1.5 — Commit único de cierre

A pedido explícito del operador, se ejecutó el commit que quedaba pendiente
desde §24.5 (re-confirmado pendiente en cada sesión intermedia), sobre el
estado final tras 1.1-1.4.

## 2. Verificación de integridad antes del commit

- Conteo de archivos: 1839 → 1812 (`find` sin `.git`), diferencia de
  exactamente 27, consistente con los 27 archivos eliminados en 1.3.
- git status inmediatamente antes de commitear: 33 borrados en stage (6
  heredados + 27 nuevos de esta sesión), 29 borrados sin stage (sin
  cambios), 3 modificaciones (`conversations.json` de la sesión de
  rescatados-corpus + README de `08_documentacion_respaldo` + la fuente de
  verdad, ambos editados esta sesión), 2 renombres (heredados del fix de
  encoding), 12 untracked (los READMEs de segundo nivel nunca trackeados,
  incluido el de `datos_config_mod_rescatados`).
- git log antes del commit: los mismos 4 commits intactos
  (`10240bb`, `1ee1018`, `5902c7e`, `f43b2f9`).

## 3. Estado de git al cierre de esta sesión

**Commit ejecutado.** Ver hash y mensaje exactos en el historial de git del
repo — este log no repite el hash para no arriesgar una transcripción
incorrecta; confirmar con `git log -1` sobre el zip entregado.

## 4. Estado consolidado de pendientes organizativos

| # | Ítem | Estado a cierre de esta sesión |
|---|---|---|
| 5 | READMEs de segundo nivel | ✅ Completo |
| 6 | `.gitattributes` / renormalize LF-CRLF | ⚠️ Sin cambios — sigue pendiente del lado del operador/git |
| 7 | `3_ANALISIS/portafolio/` vacía | ⏸️ Sin cambios — contenido faltante, no limpieza |
| 8 | Bug de encoding en `1_MOD/06_historial_desarrollo/` | ✅ Resuelto (sesión previa) |
| 9 | Duplicados menores detectados | ✅ Resuelto (sesión previa) |
| 10 | Relación `rescatado__*` vs. batches originales | ✅ Resuelto (sesión previa) |
| 11 (nuevo) | `08_documentacion_respaldo/`: 3 carpetas (24 archivos) que la fuente de verdad decía eliminadas pero seguían presentes | ✅ **Resuelto esta sesión** — verificado por hash y eliminadas |
| 12 (nuevo) | `datos_config_mod_rescatados/`: 8 archivos en vez de los 5 que la fuente de verdad decía | ✅ **Resuelto esta sesión** — verificado por hash y eliminados los 3 duplicados |
| 13 (nuevo) | Commit único de cierre | ✅ **Ejecutado esta sesión** |

**No quedan ítems abiertos de limpieza/organización.** Los que siguen sin
cerrar (#6, #7) no son de naturaleza "archivos sueltos en un zip": #6
depende de una operación de git del operador, #7 de contenido que todavía
no existe.

## 5. Qué NO se hizo esta sesión

- No se planificaron los 4 productos del proyecto ni se tocó `plan.md` —
  explícitamente diferido a la próxima sesión, a pedido del operador.
- No se resolvió DR-54 (sigue bloqueante, sin resolver).
- No se avanzó en el ítem #6 (renormalize LF/CRLF) ni en el #7 (contenido de
  `portafolio/`).
- No se subió el commit a GitHub — eso queda del lado del operador.

## 6. Qué adjuntar y cómo arrancar la próxima sesión

- Adjuntar el zip resultante de esta sesión (con el commit ya hecho) y,
  opcionalmente, este log — la fuente de verdad (`FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md`,
  §25) ya incorpora todo el detalle relevante, no hace falta releer los 6
  logs de sesión anteriores para retomar.
- Confirmar contra el zip real (`git log -1`, `git status`) que el commit se
  aplicó como se espera y que el working tree quedó limpio, antes de asumir
  cualquier otra cosa.
- **Primera tarea de la próxima sesión, según pidió el operador:** empezar a
  planear los 4 productos del proyecto, con base en `plan.md` y la fuente de
  verdad. Punto de partida obligatorio antes de plantear nada: `plan.md`
  (v1.3, 2026-07-05) es anterior a la resolución de DR-54 (que sigue sin
  resolver — ver §25.10) y anterior a toda la reorganización de §17-§24; su
  estructura de carpetas (Anexo A) ya no coincide con el árbol real de
  `IRAM_UNIFICADO/`. Cotejar contra el árbol real y contra el estado de
  DR-54 antes de usarlo como plan operativo, no asumir que sigue vigente
  tal cual está escrito.
