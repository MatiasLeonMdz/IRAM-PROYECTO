## §20 — Purga de `_CUARENTENA_DUPLICADOS/` (2026-07-08)

**Estado: EJECUTADA.** Continuación directa de §19.6 (pendiente #1: decidir si se
purga o se conserva `_CUARENTENA_DUPLICADOS/`). Se recibió `IRAM_PROYECTO_REORGANIZADO_v4.zip`
al inicio de esta sesión, se verificó su contenido en detalle antes de tocar nada, y
se ejecutó la purga recién con confirmación explícita del usuario.

### §20.1 — Corrección al conteo de §19.1/§19.6

El conteo real de `_CUARENTENA_DUPLICADOS/` en el zip v4 era **557 archivos**, no
~745 (estimado en §19.6) ni 758 (§19.1). La discrepancia se debe a que los números
previos eran estimaciones, no un recuento directo sobre el zip entregado. Desglose:

- `raiz_duplicados_SESSION_LOG_REPLANTEO/` — 6 archivos
- `raiz_duplicados_volcados_memoria/` — 5 archivos
- `raiz_duplicados_varios/` — 1 archivo
- `fuentes de documentacion (subcopia anidada)/` — 267 archivos
- `documentacion iram 10-06-2026 00.30 (subcopia anidada)/` — 278 archivos

### §20.2 — Verificación previa a la purga

Antes de proponer nada, se verificó por hash MD5 archivo por archivo cada uno de los
557 contra el resto del árbol ya organizado (`1_MOD/`, `2_DOCUMENTACION/`,
`3_ANALISIS/`):

- 555/557 con match directo de hash idéntico a su copia organizada.
- 2/557 eran un `.zip` (`mod_pack_IRAM_v5_5_2026-06-09_03-22.zip`) y su copia
  interna `(2)` — idénticos entre sí por hash, y sin par `.zip` en el árbol
  organizado porque ahí vive descomprimido. Se descomprimió y se comparó archivo
  por archivo (`diff -rq`) contra `1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/`:
  contenido 100% idéntico.

**Resultado: 557/557 archivos eran 100% redundantes, sin excepción.** No se encontró
ningún archivo huérfano ni ninguna diferencia de contenido. Se presentó este detalle
al usuario antes de ejecutar nada, tal como pidió la regla de trabajo (proponer,
esperar OK, categoría por categoría).

### §20.3 — Ejecución

Con confirmación explícita del usuario (Opción A: purga completa, sin conservar zip
de resguardo separado), se ejecutó:

1. Borrado de las 5 subcarpetas dentro de `_CUARENTENA_DUPLICADOS/` (557 archivos).
   La carpeta queda vacía salvo su `README.md`, reescrito para documentar la purga
   y la verificación que la respaldó (mismo contenido que este §20.1-§20.2, en
   versión resumida).
2. Actualización de `INDICE.md` en la raíz del proyecto: la entrada de
   `_CUARENTENA_DUPLICADOS/` ya no dice "pendiente de purga", dice "PURGADA
   2026-07-08, vacía, se conserva solo como registro".
3. Commit de git sobre el repo existente (que ya tenía los 2 commits de la tarea
   #19): `0d9ae6371e23679778700bfdb2aed5c71634e0d5` — "Purga tarea #19.6 / #5-10:
   _CUARENTENA_DUPLICADOS (557 archivos)". El repo queda con 3 commits en total,
   `git status` limpio tras el commit.

### §20.4 — Árbol final tras la purga

```
IRAM PROYECTO/
├── FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md
├── WIKI_DOCUMENTACION_v3.md
├── INDICE.md
├── verificar_iram.py
├── 1_MOD/                       (1491 archivos)
├── 2_DOCUMENTACION/             (267 archivos)
├── 3_ANALISIS/                  (30 archivos)
│   ├── portafolio/              ← sigue vacía, pendiente de contenido real
│   └── tarea_UTN/consignas/
├── 00_fuente_de_verdad/         (12 archivos)
├── 00b_descartables/            (5 archivos)
└── _CUARENTENA_DUPLICADOS/      (1 archivo: solo README.md, vacía de contenido)
```

Total de archivos de trabajo (sin `.git`): **1815** (bajó de 2371 antes de la purga).
Empaquetado como `IRAM_PROYECTO_REORGANIZADO_v5.zip` — reemplaza al v4.

### §20.5 — Aclaración sobre el `.git`

Durante esta sesión el usuario preguntó si el `.git` estaba "solo para la carpeta
del mod". Se verificó: el `.git` vive en la raíz de `IRAM PROYECTO/`
(`git rev-parse --show-toplevel` lo confirma) y `git ls-files` mostró que las 7
carpetas de primer nivel están trackeadas (1_MOD, 2_DOCUMENTACION, 3_ANALISIS,
00_fuente_de_verdad, 00b_descartables, _CUARENTENA_DUPLICADOS, y los archivos
sueltos de raíz). El usuario confirmó que fue una confusión de su parte — el repo
sí cubre todo el proyecto, no solo el mod. No se hizo ningún cambio de estructura
de git por este punto; se deja constancia de la verificación para no repetirla.

### §20.6 — Pendiente detectado, no resuelto en esta sesión

Durante la orientación inicial se notaron 4 archivos sueltos en la raíz de
`IRAM PROYECTO/` que **no** aparecen en el árbol declarado de §19.3 ni tienen
entrada en `INDICE.md`:

- `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`
- `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md`
- `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md`
- `LOG_REORGANIZACION_2026-07-05.md`

Son logs de sesiones previas a la reorganización de la tarea #19 (05 y 06 de julio).
No se tocaron. Candidatos naturales para mover a `00_fuente_de_verdad/` (histórico,
no vigente), pero falta decisión del usuario.

### §20.7 — Pendiente para la próxima sesión

- Resolver §20.6 (los 4 archivos sueltos en la raíz).
- Generar READMEs de segundo nivel (subcarpetas específicas), si se considera
  necesario — sigue pendiente desde §19.6, no se abordó en esta sesión.
- `3_ANALISIS/portafolio/` sigue vacía — pendiente de contenido real del
  portafolio GitHub.
