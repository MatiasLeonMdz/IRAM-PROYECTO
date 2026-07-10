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

## Segunda purga (2026-07-10) — subcarpeta `07_fuentes_documentacion_duplicados_2026-07-08/`

Entre la purga de arriba (557 archivos, 08-07) y la sesión de unificación del
10-07, se generó una segunda tanda de cuarentena: al subdividir
`2_DOCUMENTACION/07_fuentes_documentacion/` en 10 carpetas temáticas, aparecieron
27 archivos duplicados (22 hashes únicos) que fueron a parar acá, en una
subcarpeta nueva. Esta subcarpeta no llegó a documentarse en la fuente de verdad
ni en el log de continuidad — se detectó y verificó recién en la sesión de
unificación del 10-07, como parte del trabajo de armar `IRAM_UNIFICADO/`.

**Verificación (10-07):** se recalculó hash SHA-256 (normalizado CRLF/LF) de los
27 archivos, se confirmó que coinciden exactamente con los 22 hashes que el
README de esa subcarpeta declaraba, y se verificó independientemente — sin
confiar solo en lo que decía el README — que los 22 tienen gemelo idéntico en
el resto del árbol activo (mayormente en
`2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/`, organizado
por tema). Cero huérfanos.

**Resultado: 27/27 archivos 100% redundantes, sin excepción.** Confirmado con
el operador y borrados el 2026-07-10. Igual que la purga anterior, sin copia de
resguardo separada — el contenido sigue disponible en su ubicación organizada.
