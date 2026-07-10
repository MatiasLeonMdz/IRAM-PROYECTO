# ÍNDICE — Proyecto IRAM
Guía de 30 segundos: ¿qué carpeta mirar según tu pregunta?

## ¿Tu pregunta es sobre...?

**Cómo y cuándo se redefinió el encuadre del proyecto (qué piezas lo componen, reglas de trabajo, DR-01 a DR-54)** → `0_REPLANTEOS_Y_DECISIONES/` — leer su README primero, tiene índice por archivo

**El mod en sí (código, versiones, mecánicas de juego)** → `1_MOD/`

**Cómo se documentó el proceso de creación del mod / metodología de trabajo con Claude (Paper C1, Skill C2)** → `2_DOCUMENTACION/`

**El análisis A/B, la diplomatura UTN, o el portafolio final** → `3_ANALISIS/` (ver `tarea_UTN/` y `portafolio/` adentro)

**El estado actual y las decisiones vigentes de TODO el proyecto** → `FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md` (en esta misma carpeta) — leer primero, siempre

**Contexto histórico de cómo evolucionó la documentación (wiki de wikis)** → `WIKI_DOCUMENTACION_v3.md` (en esta misma carpeta)

**Versiones anteriores de la fuente de verdad (histórico, no citable como vigente)** → `00_fuente_de_verdad/`

**Material descartado pero conservado por precaución** → `00b_descartables/`

**Archivos duplicados (histórico)** → `_CUARENTENA_DUPLICADOS/` — vacía (salvo su README). Purga grande del 2026-07-08 (557 archivos) + segunda purga del 2026-07-10 (27 archivos de una subdivisión posterior), ambas verificadas 100% redundantes por hash antes de borrar. Ver README de la carpeta para el detalle de ambas.

**Contenido rescatado de las copias de seguridad viejas (274 archivos, sesión 2026-07-10)** → no vive en una carpeta aparte — se integró directamente en las carpetas temáticas de arriba, según su contenido real (mismo criterio que el resto del árbol). De los 274, una revisión posterior en la misma sesión encontró que buena parte ya era redundante con lo que existía (ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` para el detalle completo, incluida la corrección). Lo que quedó, genuinamente único:
- `2_DOCUMENTACION/08_documentacion_respaldo/readmes_indices_historicos/` → 9 versiones históricas de README/INDICE de otras carpetas, distintas por contenido de la vigente
- `1_MOD/datos_config_mod_rescatados/` → 5 archivos de datos/config del mod (`exodus_*`) que no estaban en el árbol activo
- Ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` (raíz) para la auditoría completa archivo por archivo de este rescate: qué es cada familia, por qué se conserva, y qué relación tiene con lo que ya existía.

**Un script de auditoría/verificación reusable** → `verificar_iram.py` (raíz)

## Regla de oro
Si tu sesión es corta: leé `FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md` primero, después este índice para saber dónde profundizar. No releas `_CUARENTENA_DUPLICADOS/` ni `00_fuente_de_verdad/` salvo que necesites evidencia histórica puntual.

## Estructura de primer nivel

```
IRAM PROYECTO/
├── FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md   ← leer primero
├── WIKI_DOCUMENTACION_v3.md
├── INDICE.md                                 ← este archivo
├── verificar_iram.py
├── 0_REPLANTEOS_Y_DECISIONES/  → replanteo transversal de encuadre (DR-01 a DR-54)
├── 1_MOD/              → el mod (Objetivo 1)
├── 2_DOCUMENTACION/    → proceso y metodología (Objetivo 2)
├── 3_ANALISIS/         → análisis A/B + UTN + portafolio (Objetivo 3)
├── 00_fuente_de_verdad/    → histórico, no vigente
├── 00b_descartables/       → descartado, conservado por precaución
└── _CUARENTENA_DUPLICADOS/ → vacía (purgada 2026-07-08 y 2026-07-10, ver README)
```

Cada carpeta de primer nivel (`0_REPLANTEOS_Y_DECISIONES/`, `1_MOD/`, `2_DOCUMENTACION/`, `3_ANALISIS/`, `00_fuente_de_verdad/`, `00b_descartables/`, `_CUARENTENA_DUPLICADOS/`) tiene su propio README con más detalle sobre qué contiene y qué NO va ahí. Desde el 2026-07-10 estos READMEs ya no se llaman `README.md` a secas: el nombre incluye la ruta de la carpeta que documentan (ej. `README__1_MOD.md`, `README__2_DOCUMENTACION__07_fuentes_documentacion.md`), justamente para poder identificarlos si se descargan sueltos, fuera de su carpeta. Ver la nota de pie de página para el detalle de este cambio.

---
*Generado en la sesión de reorganización 2026-07-08, tarea #19 (§17.3/§18.1 de la fuente de verdad). Actualizado la misma fecha, sesión posterior: carpeta `0_REPLANTEOS_Y_DECISIONES/` nueva, subcarpetas de `3_ANALISIS/`, `06_historial_desarrollo` movido a `1_MOD/`, purga de duplicado en `1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/`, 4 archivos sueltos de raíz movidos a `00_fuente_de_verdad/`.*

*Actualizado 2026-07-10: esta carpeta (`IRAM_UNIFICADO/`) es ahora el único punto de verdad del proyecto — reemplaza las 15+ copias sueltas de escritorio, que dejan de usarse (backup en adelante solo vía GitHub). Se integraron los 274 archivos de contenido único rescatados de esas copias viejas, verificados por hash/diff uno por uno (ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` en esta raíz para el detalle completo de esa auditoría). Ningún archivo del árbol activo fue sobrescrito: donde hubo mismo nombre y contenido distinto (README/INDICE de otras carpetas, `conversations.json` de distintos lotes), la versión rescatada se conservó aparte con nombre calificado por carpeta/lote de origen, nunca reemplazando a la vigente. En el mismo proceso se detectaron y purgaron, con confirmación del operador, dos carpetas de contenido 100% redundante que no estaban documentadas: 27 archivos en `2_DOCUMENTACION/08_documentacion_respaldo/` (backup viejo pre-subdivisión temática) y 27 archivos más en una subcarpeta de `_CUARENTENA_DUPLICADOS/` (residuo de esa misma subdivisión) — ver README de cada carpeta para el detalle de verificación. Se agregaron además las 3 herramientas de auditoría que produjeron el rescate de los 274 (`1_descomprimir_copias.py`, `2_buscar_contenido_unico.py`, `3_copiar_candidatos_valiosos.py`) a `2_DOCUMENTACION/07_fuentes_documentacion/.../09_scripts_python/`, junto a `verificar_iram.py`. Finalmente, `FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md` se consolidó en `FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md` (nueva versión vigente, fusiona §19-§22 que existían como archivos sueltos sin integrar) y se archivó en `00_fuente_de_verdad/` junto con `_2` a `_10`, mismo criterio que cada versión anterior de este documento.*

*Actualizado 2026-07-10 (revisión general posterior, mismo día): a pedido del operador se hizo una auditoría de duplicados sobre todo el árbol ya unificado. Se encontró que el chequeo de colisiones original (§22.1) comparó los 274 contra el repo activo tal como estaba **antes** de empezar a copiar, pero no volvió a cruzar cada lote nuevo contra las carpetas que la propia sesión iba creando en el camino — resultado: 5 de las 6 carpetas nuevas creadas para el rescate resultaron ser, total o parcialmente, contenido ya redundante. Se corrigió: `0_REPLANTEOS_Y_DECISIONES/03_rescatados_274/` (20 archivos, 100% redundante) y `1_MOD/herramientas_backups_rescatados/` (3 archivos, 100% redundante) se eliminaron enteras; `2_DOCUMENTACION/08_documentacion_respaldo/historiales_completos/` (15), `.../reorganizaciones/` (4) y `.../borradores_planificacion/` (5) también se eliminaron enteras; `1_MOD/datos_config_mod_rescatados/` bajó de 8 a 5 archivos genuinos. Solo `2_DOCUMENTACION/08_documentacion_respaldo/readmes_indices_historicos/` resultó limpia desde el principio (se le quitaron 2 duplicados internos entre sí, quedando 9). Verificado con un segundo escaneo completo del árbol tras la limpieza: cero duplicados restantes en ninguna carpeta creada por esta sesión de rescate. Ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` para el detalle completo de esta corrección.*

*Actualizado 2026-07-10 (continuación de la misma sesión, revisión general de referencias): se retomó y completó el barrido de rutas/nombres de archivo citados en todo el árbol para detectar referencias colgadas tras las purgas de esta sesión. Se encontró y corrigió una: esta misma sección del índice todavía mencionaba `0_REPLANTEOS_Y_DECISIONES/03_rescatados_274/` y `1_MOD/herramientas_backups_rescatados/`, ambas eliminadas en la corrección anterior. El resto de las menciones a `README.md` sin ruta encontradas en el barrido viven dentro de secciones históricas append-only (§19-§21 de la fuente de verdad, logs de auditoría de continuidad) y no se tocaron, para no reescribir registro histórico. Además, los 11 READMEs vigentes de carpeta —que hasta ahora se llamaban todos `README.md` a secas, indistinguibles entre sí si se descargaban sueltos— se renombraron incluyendo la ruta de su carpeta (ej. `README__1_MOD.md`, `README__2_DOCUMENTACION__08_documentacion_respaldo.md`); los históricos de `readmes_indices_historicos/` ya seguían un patrón similar y no se tocaron. Ver `LOG_CONTINUIDAD_IRAM_UNIFICADO_2026-07-10.md` para el detalle completo.*
