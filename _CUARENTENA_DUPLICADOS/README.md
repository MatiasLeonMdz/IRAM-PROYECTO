# _CUARENTENA_DUPLICADOS/

## Estado: PURGADA (2026-07-08)

Esta carpeta contenía 557 archivos duplicados exactos (verificados por hash MD5,
uno por uno, contra su copia vigente en el resto del árbol). El operador confirmó
la purga definitiva tras revisar el detalle de la verificación.

## Verificación que respaldó la purga

- `raiz_duplicados_SESSION_LOG_REPLANTEO/` — 6 archivos, 6/6 hash idéntico a
  `2_DOCUMENTACION/01_logs_replanteo/`
- `raiz_duplicados_volcados_memoria/` — 5 archivos, 5/5 hash idéntico a
  `3_ANALISIS/` (uno con nombre distinto por sufijo `(2)`, contenido idéntico)
- `raiz_duplicados_varios/` — 1 archivo, hash idéntico a
  `2_DOCUMENTACION/02_charlas_y_resumenes/`
- `fuentes de documentacion (subcopia anidada)/` — 267 archivos, 267/267 —
  incluye 2 `.zip` sin par `.zip` en el árbol, pero su contenido descomprimido
  se comparó archivo por archivo (`diff -rq`) contra
  `1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/`: idéntico
- `documentacion iram 10-06-2026 00.30 (subcopia anidada)/` — 278 archivos,
  278/278 hash idéntico a su par ya organizado (incluye los 13 de
  `historial viejo/` ya verificados manualmente en la sesión de la tarea #19,
  ver §19.2 de la fuente de verdad)

**Resultado: 557/557 archivos eran 100% redundantes, sin excepción.** No se
encontró ningún archivo huérfano ni ninguna diferencia de contenido.

## Nota sobre el conteo

El número real verificado en esta sesión fue 557 archivos, no ~745 (como
constaba en el pendiente de la sesión anterior) ni 758. La discrepancia se
debe a conteos previos hechos de memoria/estimación, no a una recontabilización
del zip real. Este README documenta el conteo exacto con el que se ejecutó
la purga.

## Qué hacer si hace falta recuperar algo de acá

No hay copia de seguridad separada de esta carpeta — la purga fue borrado
directo, con verificación de hash 1:1 confirmada antes de ejecutar, tal como
pidió el operador (Opción A: purga completa, sin conservar zip de resguardo).
Cualquier contenido que estaba acá sigue disponible en su ubicación organizada
original (ver detalle arriba).
