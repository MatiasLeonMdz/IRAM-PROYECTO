## §21 — Árbol definitivo de documentación, parte 2: `0_REPLANTEOS_Y_DECISIONES/` y subdivisión de `3_ANALISIS/` (2026-07-08)

**Estado: EJECUTADA.** Continuación directa de §20. Retoma el pendiente §20.7
("READMEs de segundo nivel") y, en el proceso, encuentra y resuelve dos
problemas no capturados por §20: un duplicado exacto fuera de
`_CUARENTENA_DUPLICADOS/`, y una mezcla de 22 archivos sin clasificar en
`3_ANALISIS/`.

### §21.1 — Hallazgos no capturados por §20

Al inventariar el proyecto completo (no solo `3_ANALISIS/`) antes de tocar
nada, se encontraron dos cosas que la purga de §20 no cubrió porque no vivían
dentro de `_CUARENTENA_DUPLICADOS/`:

1. **`1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/`** — carpeta completa
   (52 archivos) duplicada de `1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/`.
   Verificada por `diff -rq`: cero diferencias, 100% idéntica. Purgada.
2. **`3_ANALISIS/`** tenía 22 archivos sueltos sin subclasificar (charlas
   7-12, logs de auditoría de continuidad, prueba de fuga de memoria, y los
   5 `SESSION_LOG_REPLANTEO_*` finales de la serie) — mezclados con
   `portafolio/` y `tarea_UTN/`. No eran duplicados, era falta de
   subcarpetas, mismo tipo de trabajo que ya se había hecho en
   `2_DOCUMENTACION/` en la tarea #19.

### §21.2 — Decisión de diseño: `0_REPLANTEOS_Y_DECISIONES/` como carpeta nueva de primer nivel

El operador propuso, en el curso de la sesión, que `1_MOD/`,
`2_DOCUMENTACION/` y `3_ANALISIS/` tuvieran cada una su propia carpeta de
"historial de desarrollo". Al verificar el contenido real contra esa idea,
se encontró que la serie `SESSION_LOG_REPLANTEO_*` (20 archivos, 19/06 a
05/07) no encaja como historial de ninguna sección individual: cada sesión
de esa serie mezcla decisiones sobre las 3 piezas del proyecto a la vez
(ejemplo verificado: la sesión que fija DR-25, "3 piezas, no 4", también fija
DR-24, nomenclatura del mod, y DR-26, criterio de cierre del análisis, en el
mismo archivo). Partir la serie por sección habría fragmentado decisiones
tomadas como unidad — el mismo problema de fondo que ya diagnosticó §17.1
sobre los `SESSION_LOG_REPLANTEO_*` duplicados.

El operador precisó la distinción real: el desarrollo del mod, la
documentación pormenorizada, y el análisis tienen naturaleza propia y
distinta de la serie de replanteo, que es "un cambio completo de enfoque por
acumulación" — meta-registro de las decisiones de encuadre, no contenido de
ninguna de las 3 piezas. Se acordó una carpeta nueva a la misma altura que
`1_MOD/`, `2_DOCUMENTACION/`, `3_ANALISIS/`: `0_REPLANTEOS_Y_DECISIONES/`.
Esto no reabre DR-25 ("no son 4 piezas, son 3") porque esa regla habla de
piezas *entregables* del proyecto — una carpeta de replanteos es meta-proceso,
no una 4ta pieza entregable.

### §21.3 — Ejecución

Con confirmación del operador en cada paso, se ejecutó:

1. `0_REPLANTEOS_Y_DECISIONES/01_logs_replanteo/` ← movidos los 15 archivos
   que antes vivían en `2_DOCUMENTACION/01_logs_replanteo/`.
2. `0_REPLANTEOS_Y_DECISIONES/02_logs_replanteo_cola/` ← movidos los 5
   `SESSION_LOG_REPLANTEO_*` finales que estaban sueltos en `3_ANALISIS/`
   (contienen DR-45 a DR-54, el bloqueante vigente del análisis — se
   documentó explícitamente en el README que siguen siendo el material más
   citado de `3_ANALISIS/` pese a la mudanza física).
3. `0_REPLANTEOS_Y_DECISIONES/README.md` nuevo: índice completo de los 20
   archivos con fecha, DR principales, y a qué sección afecta cada uno —
   siguiendo el criterio de §18.1 (legible sin releer toda la fuente de
   verdad).
4. `1_MOD/06_historial_desarrollo/` ← movida desde
   `2_DOCUMENTACION/06_historial_desarrollo_mod/` (13 archivos): es
   desarrollo técnico estricto del mod (código, mecánicas, eventos), no
   documentación del proceso.
5. `3_ANALISIS/` subdividida en 3 carpetas nuevas:
   - `02_charlas_diseño_analisis/` (charla_7.md a charla_12.md, 6 archivos)
   - `03_auditoria_continuidad/` (SESSION_LOG_AUDITORIA_*, CHAT_DE_LOG_*,
     colisiones_verificadas, PASO_0_checklist ×2 — con README propio que
     aclara cuál de las 2 versiones del checklist es la vigente, relación
     base→extendida verificada, no duplicado)
   - `04_prueba_fuga_memoria/` (memoria_claude_volcado, volcado_memoria,
     resultado y instrucción de la prueba, 4 archivos)
6. Purga de `1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/` (52 archivos,
   duplicado exacto verificado por `diff -rq`).
7. Los 4 archivos sueltos de la raíz pendientes de §20.6 movidos a
   `00_fuente_de_verdad/`: `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`,
   `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md`,
   `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md`, `LOG_REORGANIZACION_2026-07-05.md`.
8. READMEs actualizados con referencias cruzadas: `1_MOD/README.md` (lista
   DR-22/23/24 que afectaron al mod, con puntero a
   `0_REPLANTEOS_Y_DECISIONES/`), `2_DOCUMENTACION/README.md` (documenta las
   2 mudanzas hacia afuera), `3_ANALISIS/README.md` (documenta la mudanza de
   la cola de replanteo, aclara que sigue siendo el material más citado),
   `INDICE.md` (agrega la entrada de la carpeta nueva).
9. Commit de git: `30fff32` — "Árbol definitivo de documentación (continuación
   §20): 0_REPLANTEOS_Y_DECISIONES + reordenamiento". El repo queda con 4
   commits en total, `git status` limpio. Los movimientos se registraron
   como renames (no delete+add), historial trazable.

### §21.4 — Árbol final tras esta sesión

```
IRAM PROYECTO/
├── FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md
├── WIKI_DOCUMENTACION_v3.md
├── INDICE.md
├── verificar_iram.py
├── 0_REPLANTEOS_Y_DECISIONES/    (21 archivos: 20 logs + README)
│   ├── 01_logs_replanteo/        (15 archivos, 19/06-04/07)
│   └── 02_logs_replanteo_cola/   (5 archivos, DR-45 a DR-54)
├── 1_MOD/                        (sin mod_pack duplicado)
│   └── 06_historial_desarrollo/  (13 archivos, ex-2_DOCUMENTACION)
├── 2_DOCUMENTACION/              (sin 01_logs_replanteo ni 06_historial_desarrollo_mod)
├── 3_ANALISIS/
│   ├── portafolio/                       (sigue vacía)
│   ├── tarea_UTN/consignas/
│   ├── 02_charlas_diseño_analisis/       (6 archivos)
│   ├── 03_auditoria_continuidad/         (6 archivos + README)
│   └── 04_prueba_fuga_memoria/           (4 archivos)
├── 00_fuente_de_verdad/          (+ 4 archivos de §20.6)
├── 00b_descartables/
└── _CUARENTENA_DUPLICADOS/       (sin cambios, sigue vacía)
```

Total de archivos de trabajo (sin `.git`): **1765** (bajó de 1815 tras purgar
los 52 duplicados de `1_MOD/`). Empaquetado como
`IRAM_PROYECTO_REORGANIZADO_v6.zip` — reemplaza al v5.

### §21.5 — Pendiente detectado, no resuelto en esta sesión

- `3_ANALISIS/portafolio/` sigue vacía — pendiente de contenido real del
  portafolio GitHub (arrastrado desde §19.6/§20.7).
- No se revisó si `2_DOCUMENTACION/07_fuentes_documentacion/` (161 archivos,
  la carpeta más grande) necesita subdivisión — quedó fuera del alcance de
  esta sesión, que se centró en `3_ANALISIS/` y la serie de replanteo.
- Los READMEs de segundo nivel de `1_MOD/game/` (3 subcarpetas, 906 archivos)
  y de las subcarpetas de `2_DOCUMENTACION/` (`04_corpus_A_mod_docs`,
  `05_corpus_B_crudo`, `07_fuentes_documentacion`, `08_documentacion_respaldo`)
  no se generaron — sigue pendiente desde §19.6/§20.7, no se abordó en esta
  sesión más allá de las carpetas tocadas directamente.
