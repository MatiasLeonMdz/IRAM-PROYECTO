## §19 — Ejecución de la tarea #19: árbol definitivo de documentación (2026-07-08)

**Estado: EJECUTADA.** Esta sección documenta lo que efectivamente se movió, corrigió y
verificó, y corrige un error propio cometido durante la propia ejecución (ver §19.4).

### §19.1 — Correcciones al inventario de §17

- **SESSION_LOG_REPLANTEO_* de la raíz (§17.1):** de los 11 archivos sueltos, solo 6
  eran duplicados exactos (hash idéntico) de su par en `01_logs_replanteo/`
  (`_02-13`, `_02-43`, `_17-47`, `_17-58`, `_17-58 2`, `_23-17`). Los otros 5
  (`_23-44`, y la serie del 05/07: `_00-10`, `_00-32`, `_00-52`, `_01-37`) **no tenían
  ninguna copia organizada** — son la continuación real de la serie de replanteo y
  contienen DR-45 a DR-54. No se borraron: se movieron a `3_ANALISIS/`.
- **_CUARENTENA_DUPLICADOS (§17.2.B):** conteo real 758 archivos, no 544.
- **Corrección de fondo al árbol (aportada por el usuario, no por Claude):** el
  contenido de tipo "diseño del análisis A/B" (DR-01 a DR-54, checklists, auditorías
  de continuidad) no es Objetivo 2 (documentación del proceso del mod) — es insumo
  directo del Objetivo 3 (análisis + UTN + portafolio). Se corrigió el árbol: la vieja
  `3_PORTAFOLIO_UTN/` se fusionó dentro de una `3_ANALISIS/` ampliada, que ahora
  absorbe todo el Objetivo 3 completo.

### §19.2 — Error propio detectado y corregido durante la ejecución

Durante la clasificación de `_CUARENTENA_DUPLICADOS/`, se afirmó inicialmente que 13
archivos de `historial viejo/` (dentro de la subcopia anidada `documentacion iram
10-06-2026...`) eran "únicos, sin copia en ningún otro lado organizado", y se
"rescataron" moviéndolos a `06_historial_desarrollo_mod/`. **Esto era incorrecto**: al
verificar contra el manifest de hashes original, los 13 archivos ya existían, con
hash idéntico, dentro de `06_historial_desarrollo_mod/` desde el origen. Es decir, eran
duplicados exactos preexistentes, no material único. Se corrigió restaurando los 13
archivos en su ubicación original de cuarentena (verificado byte a byte contra el
manifest original tras la restauración). **Lección operativa:** la regla de "nada se
borra, todo pasa por cuarentena antes de purga" permitió detectar y revertir este
error sin pérdida de datos — si se hubiera ejecutado un borrado directo basado en la
verificación inicial (errónea), no habría sido reversible.

### §19.3 — Árbol final (nivel 1, dentro de `IRAM PROYECTO/`)

```
IRAM PROYECTO/
├── FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md
├── WIKI_DOCUMENTACION_v3.md
├── INDICE.md                    ← entregable explícito de la tarea #19 (§18.1)
├── verificar_iram.py
├── 1_MOD/                       ← Objetivo 1 (el mod)
├── 2_DOCUMENTACION/             ← Objetivo 2 (proceso y metodología)
├── 3_ANALISIS/                  ← Objetivo 3 (análisis A/B + UTN + portafolio)
│   ├── portafolio/
│   └── tarea_UTN/consignas/
├── 00_fuente_de_verdad/         ← histórico, no vigente
├── 00b_descartables/            ← descartado, conservado por precaución
└── _CUARENTENA_DUPLICADOS/      ← duplicados exactos, pendiente de purga
```

Cada carpeta de primer nivel tiene su propio `README.md`.

### §19.4 — Verificación de integridad

Se generó un manifest MD5 de los 2405 archivos del ZIP original antes de tocar nada.
Tras la reorganización completa, se comparó el set de hashes original contra el set
de hashes del árbol final: **0 hashes del original ausentes en el final.** El árbol
final tiene 2418 archivos (2405 originales + 13 nuevos: charla_7 a charla_12,
`estructura_objetivos_iram.svg`, `WIKI_DOCUMENTACION_v3.md`,
`FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md`, `PROMPT_CONTINUACION_2026-07-07_8.md`, y las
tres fuentes de verdad `_8`, `_9`, `_10`).

### §19.5 — Git

Se inicializó un repositorio Git local dentro de `IRAM PROYECTO/` con 2 commits:
1. Reorganización completa (todo lo de §19.1-§19.3)
2. Fix de un submódulo roto: `1_MOD/IRAM mod v5/` traía su propio `.git/` interno
   (el repo de desarrollo del mod), lo que Git registró como *gitlink* (referencia
   rota, sin contenido real) en vez de archivos versionados. Se eliminó el `.git`
   anidado y se re-agregaron los 214 archivos como contenido normal.

El repositorio está listo para publicarse vía GitHub Desktop ("Add Local Repository"
→ apuntar a la carpeta `IRAM PROYECTO/` extraída del ZIP entregado).

### §19.6 — Pendiente para la próxima sesión

- Confirmar con el usuario si se purgan definitivamente los ~745 archivos de
  `_CUARENTENA_DUPLICADOS/` que son duplicados exactos verificados (o se conservan
  indefinidamente como red de seguridad).
- Generar READMEs de segundo nivel (subcarpetas específicas) si se considera
  necesario — por ahora solo existen los 6 README de primer nivel + el índice raíz.
- `3_ANALISIS/portafolio/` está vacía — pendiente de generar contenido real del
  portafolio GitHub.
