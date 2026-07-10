# LOG DE CONTINUIDAD IRAM — DOCUMENTO UNIFICADO

**Fecha de esta unificación:** 2026-07-10
**Fuentes:** este documento consolida en un solo archivo la cadena completa
de logs de continuidad de la auditoría de contenido único de IRAM-PROYECTO,
verificada eslabón por eslabón antes de unificar (no se aceptó ninguna
afirmación de "esto reemplaza a lo anterior" sin comprobar por contención
real de texto — ver métodología abajo).

## Cómo se armó este documento (auditoría de la propia unificación)

Se partió de 34 archivos `.md` sueltos (logs + addons + notas de sesión).
Cada uno fue verificado por **contención real de texto** (muestreo de
bloques de 2-3 líneas comparados literalmente, y luego verificación
puntual de afirmaciones/hashes/cifras clave cuando el matching literal
bajaba, para no confundir "resumido con otras palabras" con "perdido") —
no por lo que el propio archivo afirmaba de sí mismo en su encabezado.
Resultado:

- **Cadena troncal real** (3 piezas, cada una aporta contenido propio sin
  solaparse con la anterior):
  1. `LOG_CONTINUIDAD_IRAM_2026-07-10_v25.md` — consolida internamente
     toda la cadena `v2` a `v23` + `LOG_v24.md` (verificado: 93-98% de
     contención literal en cada salto de la cadena; el resto son solo
     portadas/colas de sesión que cambian cada vez, sin pérdida de
     hallazgos sustantivos — confirmado caso por caso donde el ratio
     bajaba de 90%).
  2. `ADDON_LOG_CONTINUIDAD_IRAM_2026-07-10_v27.md` — addon conjunto de
     las sesiones v26+v27. **Incluye también el contenido de v26**: se
     verificó que toda afirmación sustantiva de `ADDON_..._v26 2.md`
     (hashes, veredictos, cifras de la reconciliación FUENTE_DE_VERDAD
     12→11 y el cierre del suelto s18) está presente en v27, solo
     redactada de forma más condensada. Incluir v26 aparte hubiera
     duplicado ~240 líneas de contenido ya cubierto.
  3. `LOG_CONTINUIDAD_IRAM_2026-07-10_v29.md` — **incluye a v28
     completo**: verificado que v29 contiene el 97% del texto literal de
     `v28 (incompleto).md` (el 3% restante es el propio párrafo de
     cierre de la sección 8 que v29 reescribió al resolver el hallazgo
     del SVG). Cierra la cadena `SESSION_LOG_DOCUMENTACION` (s18→s34),
     el grupo `SESION*`, `IRAM_PROMPT_MAESTRO` vs `PROMPT_MAESTRO`, la
     verificación del alcance real de los 274, y el hallazgo del SVG.

- **Archivos verificados como ya absorbidos, no incluidos en el cuerpo**
  (contención ≥93% del contenido sustantivo confirmada por muestreo, con
  revisión manual de cada discrepancia para descartar pérdida real):
  `LOG_CONTINUIDAD_IRAM_2026-07-09.md` (sin versión), `_v2.md` a `_v23.md`,
  `LOG_v24.md`, `ADDON_LOG_CONTINUIDAD_IRAM_2026-07-10_v24_ADDON.md`,
  `ADDON_LOG_CONTINUIDAD_IRAM_2026-07-10_v25_ADDON.md`,
  `ADDON_LOG_CONTINUIDAD_IRAM_2026-07-10_v26.md` y `"v26 2.md"` (ambas
  absorbidas por v27, ver arriba), `ADDON_LOG_v21_bloque_no_mapeado.md` y
  `" 2"` (absorbidos por `" 3"`, y su contenido sustantivo confirmado
  presente en v25 §2.8 y §3.6.sedecies), `INVENTARIO_SECCION_3_6.md`
  (snapshot de trabajo de la sesión v3, su contenido vive integrado y
  actualizado en la sección 3.6 de v25), `a continuar.md` (transcripción
  cruda ya formalizada como sección "0.bis" de `v10.md`), y
  `LOG_CONTINUIDAD_IRAM_2026-07-10_v28.md` /
  `LOG_CONTINUIDAD_IRAM_2026-07-10_v28 (incompleto).md` (ambas versiones
  de v28 absorbidas dentro de v29, verificado por contención 97%).

- **Notas importantes encontradas durante la verificación:**
  - El propio `v28.md` afirma en su encabezado "reemplaza operativamente"
    a v25 y a los addons v26/v27 — se comprobó por contención de texto
    que **esto no es así al pie de la letra respecto de v25/v27** (0% de
    coincidencia literal con esos dos): v28 no reproduce ese texto, solo
    **cita y construye sobre sus conclusiones** ("heredado de v27,
    resumen", "ya cerrado en v25"). Por eso este documento sí incluye el
    cuerpo completo de v25 y v27 por separado.
  - La primera versión de este ensamblaje incluyó v26 y v27 como piezas
    separadas; una segunda pasada de verificación (comparando afirmaciones
    clave, no solo bloques literales) detectó que v27 ya incorporaba todo
    el contenido sustantivo de v26 en forma condensada — se corrigió antes
    de entregar la versión final. Se deja esta nota como registro del
    propio proceso de auditoría, siguiendo el mismo estándar de
    transparencia que exige el resto del corpus.

**Metodología aplicada en toda la verificación:** la misma regla de oro
que rige el resto de esta auditoría — no asumir relación de contenido por
lo que un documento dice de sí mismo, confirmar siempre por comparación
directa de texto (y de afirmaciones puntuales cuando el texto se resume
con otras palabras) antes de descartar algo como "ya incluido".

---


# ═══════════════════════════════════════════════════════════════════
# PARTE 1 — LOG BASE (consolida sesiones desde el inicio hasta v25)
# ═══════════════════════════════════════════════════════════════════

# LOG DE CONTINUIDAD — Auditoría de contenido único IRAM-PROYECTO
**Fecha de este log:** 2026-07-10 (v25 — consolida v23, v24 y v25 en un
único documento integrado. Con esta versión, **las secciones 3.4, 3.9 y
la familia `FUENTE_DE_VERDAD_IRAM_2026-07-07` quedan completamente
cerradas** — no queda ninguna sección numerada grande (3.2 a 3.9) sin
cerrar. Ver 2.9/2.9.c, 2.10 y 2.11 para el detalle completo caso por
caso. Resumen:**

1. **`SESION TRUNCADA.md` contiene, como prefijo textual exacto,
   completo, a `IRAM_SUPERBACKUP_v2_1.md`** (pendiente que figuraba en
   3.8/3.9) **+ 216 líneas propias** de un turno de chat posterior. Se
   descarta `IRAM_SUPERBACKUP_v2_1.md` por redundante; se conserva
   `SESION TRUNCADA.md`. (v23)
2. **`fallo sesiones transcript 16-06-2026.md` y `fallo sesiones
   16-06-2026.md` comparten el 95% de sus líneas** (bloque continuo de
   3712 líneas) — el primero es la transcripción cruda que termina
   generando literalmente el `s19` ya cerrado en 3.6.sedecies; el
   segundo es un extracto editado de la misma sesión. **Se conservan
   ambos.** (v23)
3. **`fallo DOCUMENTACION 19-06-2026.md` es independiente** de los otros
   tres `fallo*` (menos del 1% de líneas compartidas) y también del
   resto del corpus grande — verificado por diff directo, no solo por
   lo que narra el documento (hallazgo del header roto de
   `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md` confirmado carácter por
   carácter). **Se conserva completo. Con esto, 3.4 queda cerrada por
   completo.** (v24, ver 2.9.c)
4. **La familia `FUENTE_DE_VERDAD_IRAM_2026-07-07` no era 1 archivo
   suelto — son 11** (`base`, `_2` a `_11`). Hallazgo principal: el
   sufijo numérico del nombre de archivo en disco puede estar
   **invertido respecto a la versión real** que cada archivo declara
   internamente — confirmado por diff, no solo por la advertencia en
   texto del propio documento. **Se conservan los 11 completos, sin
   descartes.** (v25, ver 2.10)
5. **Sección 3.9 completa:** los 2 sueltos reales que quedaban
   (`IRAM_Historial_Unificado_v2.md` e
   `IRAM_historial_unificado_2026-06-12.md`) no son versión/bifurcación
   entre sí pese al nombre parecido — son dos productos de granularidad
   y metodología distintas sobre el mismo material fuente. **Se
   conservan ambos, sin descarte.** (v25, ver 2.11)

**Resumen histórico de v22 (para contexto, no acción pendiente de acá):**

1. **De ~13 archivos presentados como "no mapeados", 10 ya estaban
   cubiertos** por el log (4 con cierre firme en 2.4.a/2.4.c, 7 ya
   anotados en la lista de "sueltos sin familia clara" desde antes de
   v21) — no era territorio nuevo, era información ya escrita que no se
   había cruzado bien contra el cuerpo del log antes de reportarla como
   hallazgo.
2. **2 archivos sí eran nuevos de verdad:** `correccion de
   documentacion.md` y `correccion de documentacion 2.md` — dos sesiones
   de trabajo secuenciales sobre el sistema de documentación del
   proyecto (meta-nivel, no contenido de desarrollo del mod). El segundo
   cita textualmente al primero como su input. **Se conservan ambos.**
3. **Esos 2 archivos destaparon una cadena completa sin tocar:**
   `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19` (que además
   resultó tener 2 versiones, no 1) → `_s20` → `_ESPECIAL_s21` → `s22`.
   **Cerrada en esta sesión, ver 3.6.sedecies.** Hallazgo relevante: el
   propio proyecto documentó y corrigió, en `s21`, una pérdida real de
   contenido ocurrida en el paso `s19→s20` — es meta-evidencia directa a
   favor del criterio de v8 (conservar cadenas completas). Falta ubicar
   `..._CONSOLIDADO_s18.md`, citado por los tres como predecesor pero
   ausente de los 274 archivos indexados — puede ser pérdida real y
   definitiva, no solo alcance sin revisar.

**Resumen v21 (histórico):** se cierra la
sección **3.3 — Charlas sueltas (charla_7 a charla_12)**, 6 archivos,
la segunda de las secciones sueltas (3.2/3.3/3.4/3.9) que quedaban
pendientes tras completarse 3.6 en v19. **Resultado: se conservan las 6
completas, sin descartes.** Comparación por `SequenceMatcher` (ratio +
substring) entre las 6, más inspección de contexto de cada bloque
grande de coincidencia. Ninguna de charla_7 a charla_11 es substring ni
está absorbida por charla_12 (ratios 0.01–0.56, ningún caso de
`contenida=True`) — el ratio más alto (charla_7 vs charla_12, 0.56) es
solo texto de header/instrucciones de adjuntos repetido al inicio de
cada sesión, no contenido compartido real, confirmado por inspección
directa de los bloques de coincidencia. **charla_12 es una sesión
nueva que sintetiza en prosa propia el estado del proyecto, no una
copia textual de las 5 anteriores** — matiza (no contradice) el dato
de `FUENTE_DE_VERDAD_11 §16` citado en 2.2: reconstruye el *estado*,
no reemplaza el *contenido* único de cada sesión (razonamiento,
decisiones puntuales, diagramas). Único solapamiento real de contenido
encontrado: un bloque de ~1578 caracteres compartido entre charla_8 y
charla_11, explicado por contexto — charla_11 ejecuta `tail -20
charla_8.md` para releer el cierre de la sesión cortada anterior, y ese
output queda pegado en su propia transcripción (cita de relectura
operativa, no duplicado accidental). Resto de pares: ratios 0.014–0.14,
en rango de independencia genuina ya calibrado en el proyecto
(0.03–0.08). Ver 2.7 para el detalle completo caso por caso. Sigue
pendiente: 3.4 (sesiones falladas/truncadas), 3.9 (sueltos) y el
archivo suelto `FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md`.

**Resumen v20 (histórico):** se cierra la
sección **3.2 — Familia "gap" (sesión v4.1-4.3)**, 7 archivos, la
primera de las secciones sueltas (3.2/3.3/3.4/3.9) que quedaban
pendientes tras completarse 3.6 en v19. **Resultado: se conservan los 7
completos, sin descartes**, organizados en 3 sub-grupos:
(1) 4 transcripciones de chat, donde `sesion gap v4.1 - 4.3 parte 1`
resultó ser superset exacto por substring de `sesion gap v4.1 - 4.3`
(sin sufijo) — el checkpoint de una sesión cortada, más 4681 caracteres
de continuación —, y esa misma cola de continuación está además
duplicada aparte como `parte 2` (substring exacto, 4813 B); `parte 3`
es una sesión posterior e independiente (ratio 0.009 contra las otras,
edición real de HISTORIA_COMPLETA/hitos); (2) 2 documentos formales con
relación de reemplazo declarado (`CERRADO` dice textualmente "Reemplaza
a" `nota_deuda`) pero sin superset textual (ratio 0.053) — superset
semántico confirmado por lectura completa, cada punto de la nota
original aparece resuelto o corregido con evidencia ampliada (5 cuentas
en paralelo trabajando el período, no solo 2); (3) 1 documento
independiente (`IRAM_gaps_conocimiento_2026-06-12`, Plantilla B sobre
otro corpus, ratios 0.014–0.053 contra los demás — independencia
genuina, mismo patrón que 3.6.quindecies). Ver 3.2 para el detalle
completo caso por caso. Sigue pendiente: 3.3 (charlas sueltas), 3.4
(sesiones falladas/truncadas), 3.9 (sueltos) y el archivo suelto
`FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md`.

**Resumen v19 (histórico):** Se cierra el
último sub-grupo de 3.6.6 (sesiones sueltas), que había quedado
pendiente desde v17: `sesion cortada.md` contra las 2 partes de
`transcripcion de SESSION_LOG_CONSOLIDADO_2026-06-1*` (sufijos
`__1f5727a2` y `__56abcedb`), más el archivo final
`SESSION_LOG_CONSOLIDADO_2026-06-18` (sin sufijo de transcripción, que
apareció al buscar los otros 2 y se incorpora al mismo análisis).
**Resultado: los 4 archivos son independientes entre sí, ninguno
descartable.** `sesion cortada.md` es un draft del paper metodológico
final (Sección 7, s25, 2026-06-17, línea s21/s23/PROMPT_MAESTRO v1.9) —
tema completamente distinto al de las otras 3. Las 2 transcripciones NO
son dos mitades de una sesión cortada: son 2 sesiones de chat separadas
y secuenciales (18:06 y 19:43) que arrancan del mismo archivo pegado
(`SESSION_LOG_ANALISIS_C1_2026-06-18_v2 (2).md`) pero divergen desde ahí
— la de 18:06 diseña las specs A/B/C y crea el `SESSION_LOG_CONSOLIDADO`
como output sin ejecutarlas; la de 19:43 va más allá y ejecuta/prueba
`spec_a_authorship.py`, `spec_b_democratizacion.py` y
`spec_c_zip_history.py`. El archivo final `SESSION_LOG_CONSOLIDADO_2026-06-18`
es el artefacto real de ese trabajo, no otra transcripción. Todos los
ratios de similitud entre los 4 dieron 0.03–0.08 (sin relación de
substring), muy por debajo incluso de los pares más débiles vistos
hasta ahora; los pocos bloques coincidentes grandes son frases-tesis
repetidas en todo el proyecto ("la IA no democratiza la programación",
etc.), no estructura compartida. Ver 3.6.quindecies para el detalle
completo. **Se conservan los 4 archivos, sin descartes.**

**Con este cierre, se completan TODOS los grupos chicos/pares de 3.6**
listados originalmente — no queda ningún sub-grupo de 3.6 sin revisar.
Resumen de v18 (6 grupos chicos anteriores) y v16 a continuación.**

**Resumen v18 (histórico):** Se re-verificaron desde cero, contra los
archivos reales del zip, los 6 grupos chicos que la nota de continuidad
de v17 afirmaba haber cerrado pero que no tenían respaldo como sección
propia en el cuerpo del log (ver el aviso de integridad documental más
abajo): `critica 1` / `critica a la critica` / `IRAM_critica_rigurosa`
(bifurcación real, mismo patrón que 3.6.septies), `PASO_0_grupos_divergentes_checklist`
base+`(2)` (superset limpio confirmado por substring, +9740 caracteres),
`bloque3_analysis` base+`v2` (reescritura metodológica reconocida por
el propio autor en el código, no checkpoint simple), `spec_c_zip_history`
base+`(3)` (corrección de bug puntual y documentada, BUG-C1),
`IRAM_Prompt_Etapa1_Limpieza` + `Etapa2_Unificacion` (documentos
hermanos de un flujo en 2 etapas, sin relación de versión) y
`Consigna`/`Consigna_1`/`Consigna_2` (3 piezas curriculares distintas de
la Diplomatura UTN, sin solapamiento). Ver 3.6.quaterdecies para el
detalle completo caso por caso. **Se conservan los 10 archivos de estos
6 grupos, sin descartes.** Todos los números y citas de la nota de v17
se confirmaron exactos contra los archivos fuente — no hubo
discrepancias, solo falta de respaldo documental en el log mismo (ya
corregido en v18).

**Resumen v16 (histórico):** Se CIERRAN las 4
familias grandes restantes de 3.6 que quedaban sin tocar:
`SESSION_LOG_AUDITORIA_CONTINUIDAD` (2 archivos, ver 3.6.decies),
`IRAM_analisis_cuantitativo` (3 archivos, ver 3.6.undecies),
`IRAM_SESSION_LOG` (4 archivos, ver 3.6.duodecies) y
`PROMPT_DOCUMENTACION_IRAM_v1` (5 archivos, ver 3.6.terdecies).
Resultado en las 4: se conservan los 19 archivos completos entre las
cuatro familias — cero duplicados exactos por hash normalizado en
ninguna. Hallazgo transversal más importante de esa sesión: dentro de
`IRAM_analisis_cuantitativo` y de `PROMPT_DOCUMENTACION_IRAM_v1` aparece
el mismo ciclo de revisión metodológica real del propio proyecto sobre
el modelo de las 5 cuentas de Claude — de "secuencial" a "paralelas
simultáneas" y de ahí de nuevo a "rotación secuencial rápida" (veredicto
final, con dato duro: 0 interleavings en 7.313 mensajes) — confirmado
de forma cruzada entre ambas familias, cada una narrándolo desde un
documento distinto. No es una contradicción a resolver: es trazabilidad
real de cómo cambió el criterio del proyecto en el tiempo, y se
conserva como tal bajo el criterio de v8. Ver 3.6.undecies y
3.6.terdecies para el detalle completo caso por caso.
Con ese cierre, de las familias grandes originales de 3.6 (ver listado
completo en la sección homónima) no quedó ninguna sin tocar — solo
restaban los grupos chicos/pares y los sueltos de 3.6, más las secciones
3.2 (gap), 3.3 (charlas), 3.4 (falladas/truncadas) y 3.9 (3 sueltos).
Resumen de v15 a continuación, sin cambios.**

**Resumen v15 (histórico):** Se CIERRA
el rescate de los 16 módulos UTN (`Modulo*_Unidad*`), pendiente de
ejecución desde que se aclaró su alcance en v9 (ver sección 0).
Resultado: se rescatan los 16 completos, sin descartes. Verificado:
grilla completa Módulo 1–4 × Unidad 1–4 sin huecos ni duplicados de
nombre; 16 hashes SHA-256 distintos entre sí (ningún duplicado exacto);
cada archivo tiene `cantidad_lugares_donde_aparece = 1` en el índice
(sin copias en otras rutas del corpus de 15 backups); título de Módulo
y de Unidad dentro del contenido de cada archivo coincide exactamente
con lo que indica su nombre de archivo, en los 16 casos (no hubo ningún
caso de nombre engañoso, a diferencia de otras familias); ninguno vacío
ni truncado (105–282 líneas c/u). No hizo falta diff entre ellos porque
no forman una cadena de versiones — son 16 unidades de contenido
distinto por diseño, tratadas como rescate de bajo esfuerzo según lo ya
decidido en la sección 0. **No queda nada pendiente de este bloque.**
Resumen de v14 a continuación, sin cambios.**

**Resumen v14 (histórico):** Se CIERRA
3.6.novies: familia `IRAM_C1` (18 archivos) completamente revisada.
Resultado: se conservan los 18 completos — esqueleto de planificación
con mapping único de fuentes, 14 drafts por sección verificados como
supersets limpios por diff (incluido el tercer archivo de Sección 4,
caracterizado como la versión s32 real que resuelve INC-13), la versión
`completo_s32` con una Sección 4D propia no reproducida en ningún
suelto, y `final` como reescritura editorial con contenido sustantivo
verificado intacto por muestreo de términos clave. Ver 3.6.novies para
el detalle completo. Resumen de v13 a continuación, sin cambios.**

**Resumen v13 (histórico):** Se CIERRA 3.6.octies: familia
`SESSION_LOG_REPLANTEO` (19 archivos) completamente revisada. Resultado:
se conservan los 19 completos —
ninguno es duplicado exacto por hash normalizado (verificado CRLF→LF
sobre los 19, cero coincidencias de hash entre ningún par). A
diferencia de las familias anteriores, esta NO se estructura como una
cadena lineal simple sino como una cadena con **puntos de ramificación
por checkpoints intra-sesión**: 6 archivos citan al mismo predecesor
(`06-20_5`) y 3 archivos citan a otro mismo predecesor (`07-03_02-43`)
— verificado por diff encadenado que cada uno de esos grupos es una
progresión real (cada paso agrega contenido sobre el anterior dentro de
la misma sesión de trabajo), no una bifurcación incompatible tipo
3.6.septies. **Hallazgo operativo nuevo:** 6 de los 19 archivos estaban
en la carpeta `_CUARENTENA_DUPLICADOS/raiz_duplicados_SESSION_LOG_REPLANTEO`
del propio proyecto, puestos ahí por el operador o un proceso previo
por sospecha de duplicado — verificado que NO solapan en nombre-base ni
en hash con ningún archivo de la carpeta oficial (`01_logs_replanteo`/
`02_logs_replanteo_cola`): son pasos genuinos de la cadena, mal
clasificados en cuarentena, mismo patrón de falso positivo por
heurística de carpeta/nombre ya visto en 2.5 y 3.6.ter. Ver 3.6.octies
para el detalle completo. Sigue vigente el criterio de v8 sin cambios.
`IRAM_C1` (18) quedó CERRADA en esta sesión (v14) — ver 3.6.novies:
se conservan los 18 completos. Quedan pendientes el resto de familias
grandes de 3.6: `IRAM_SESSION_LOG` (4), `IRAM_analisis_cuantitativo`
(3), `PROMPT_DOCUMENTACION_IRAM_v1` (5),
`SESSION_LOG_AUDITORIA_CONTINUIDAD` (2), `SESSION_LOG_CONSOLIDADO`
suelto (1), `CORRECCIONES_SESION` suelto (1), `transcripcion de
SESSION_LOG_CONSOLIDADO` (2), y el bloque de sesiones
falladas/truncadas/gap (13) — ninguna tocada todavía.**

## 0.bis — PROPÓSITO FINAL DEL PROCESO (aclarado en v10, leer junto con la sección 0)

**Contexto agregado en esta sesión, no cambia nada operativo, pero es
importante para no perder de vista el destino de este trabajo:**

El usuario aclaró el plan de fondo detrás de esta auditoría, en tres
etapas de aproximadamente un mes cada una:
1. **Mes 1:** desarrollo del mod.
2. **Mes 2:** primer estudio de procesos y documentación.
3. **Mes 3:** análisis extremadamente exigente, con el objetivo explícito
   de que sea **defendible en ámbito académico o en trabajos exigentes**.

El destino final de todo este trabajo es un **anexo metodológico al
paper y al trabajo de la Diplomatura UTN**, que presente el análisis
realizado y **cómo se elaboró** — es decir, el anexo no va a ser este
log tal cual, sino una **síntesis** posterior de él.

**Relación entre las dos capas de documentación (aclarada en esta
sesión):**
- **Este log de continuidad** es el **registro de trabajo crudo**:
  sesión a sesión, con todos los hallazgos, reglas descubiertas y
  correcciones de criterio tal como fueron ocurriendo (incluida la
  corrección de v8 y los casos de evidencia mixta como 3.6.sexies). Debe
  seguir siendo exhaustivo — no conviene "limpiarlo" ni resumirlo
  prematuramente, porque es la fuente primaria que el anexo va a auditar
  más adelante.
- **El anexo** (a redactar más adelante, en la etapa del mes 3) va a
  contener la **metodología declarada de antemano** (definición
  operacional de "duplicado", criterios de inclusión/exclusión,
  procedimiento de verificación cruzada) y los hallazgos presentados
  como resultados — no la bitácora completa de idas y vueltas.

**Consecuencia práctica, sin cambios de método:** se sigue auditando con
el mismo nivel de rigor de siempre (diff línea a línea, normalización
CRLF/LF, no asumir por nombre/fecha/versión, cruzar contenido "que
desaparece" contra su destino declarado antes de concluir). El log
crudo se mantiene exhaustivo a propósito. La tarea de síntesis para el
anexo es un trabajo aparte, a futuro, y no se aborda todavía.

---

## ⚠️ CORRECCIÓN DE CRITERIO — LEER ANTES QUE NADA (aplica retroactivamente)

**El criterio de "qué se descarta" que veníamos aplicando estaba mal
calibrado y quedó corregido en esta sesión.** Hasta v7, cada vez que se
confirmaba que una versión más nueva era "superset funcional" de una más
vieja (misma cadena v1→v2→v3...), la conclusión era "conservar solo la
última, las anteriores son redundantes/candidatas a descarte de
cuarentena". **Eso fue un error de alcance del inventario.**

**Criterio correcto, confirmado explícitamente por el usuario en esta
sesión:** el inventario de "contenido único" solo elimina **duplicados
verdaderos** — mismo contenido, hash idéntico tras normalizar CRLF/LF (o
diferencia puramente cosmética equivalente). **Una versión distinta
dentro de una cadena (v1, v2, v3...) NO es un duplicado verdadero,
aunque la versión más nueva sea superset funcional confirmado de la más
vieja.** Cada paso de una cadena de versiones es un estado histórico
real del desarrollo del proyecto y se conserva como parte de la
documentación — el criterio "todo lo único va en las carpetas y no se
purga" (sección 0/regla de oro) incluye esta trazabilidad, no solo el
contenido "no repetido en ningún lado".

**Qué NO cambia:** todo el trabajo de diff/hash ya hecho sigue siendo
válido y no hay que rehacerlo — la relación de superset entre versiones
sigue siendo la evidencia correcta de que "no hay pérdida de contenido
semántico". Lo único que cambia es la conclusión final: donde decía
"conservar solo X, las demás son descartables", ahora dice "conservar
TODAS las versiones de la cadena, ninguna se descarta salvo que sea un
duplicado exacto por hash normalizado".

**Alcance de la corrección — afecta estas conclusiones ya cerradas,
todas actualizadas en este mismo log más abajo (buscar "CORREGIDO EN
v8"):**
- 2.2 — familia FUENTE_DE_VERDAD_IRAM_2026-07-07 (12 versiones)
- 2.3 — familia IRAM_historial_desarrollo_2/3/4/5 (crudas vs curadas)
- 2.4.b — IRAM_HISTORIA_COMPLETA v1_1 vs v1_2 (2)
- 3.6.bis — cadena WIKI_DOCUMENTACION (v1/v2/v3)
- 3.6.ter — cadena IRAM_hitos_metodologicos (v5/v6/v7 + b44210ab)
- 3.6.quater — cadena PROMPT_MAESTRO / IRAM_PROMPT_MAESTRO
- 3.6.quinquies (nueva en esta sesión) — cadena SESSION_LOG_ANALISIS_C1

**Lo que NO cambia de alcance:** los duplicados exactos por hash
normalizado (ej. los pares README/INDICE colapsados en 2.5.a/2.5.b, o
`failed (3).md` en 2.1) siguen siendo duplicados verdaderos — esos sí
se descartan. La corrección solo aplica a relaciones de "superset
funcional/versión distinta", no a "mismo contenido, hash idéntico".

---

**Motivo del corte anterior:** ninguno — v8 se cerró de forma preventiva
a pedido del usuario, sin corte abrupto. Esta sesión (v9) arrancó
retomando v8, descomprimiendo el zip de nuevo (filesystem no persiste
entre chats), preguntó cuál era la prioridad antes de tocar nada, y
trabajó la cadena `TECHNICAL_WIKI ACTIVE/ARCHIVE` según lo recomendado
por la prioridad sugerida de v8. A mitad de la revisión el usuario
preguntó por el ritmo de avance general (cuántas sesiones faltan) y
luego confirmó mantener el mismo nivel de rigor sin atajos automatizados
— no hubo cambio de método, solo una pausa de balance que no afectó el
trabajo de esta cadena.

---

## ⚠️ AVISO DE INTEGRIDAD DOCUMENTAL (descubierto y corregido en v18)

**Lección aprendida:** la nota de continuidad al final de v17 (sección
5, "prompt sugerido para el próximo chat") afirmaba haber cerrado 6
grupos chicos con números y citas específicas, y remitía repetidamente
a una sección "3.6.quaterdecies" para el detalle — pero esa sección
nunca se había escrito en el cuerpo del log. La única evidencia de ese
trabajo era la afirmación de resultado en la nota, no el trabajo de
verificación (diffs, hashes, casos puntuales) que sí respalda todas las
demás cadenas cerradas (3.6.septies en adelante).

**Consecuencia práctica:** no basta con que una nota de continuidad
declare algo como "cerrado" — cada cadena/grupo cerrado necesita su
propia sección con el respaldo real (evidencia de diff/hash/contenido),
igual que las demás. En v18 se re-verificaron los 6 grupos desde cero
contra los archivos del zip (ver 3.6.quaterdecies) — no se encontraron
discrepancias, pero el ejercicio confirma que declarar un cierre en
prosa no sustituye escribir la sección con su evidencia. **Regla desde
v18 en adelante: toda sección que la nota de continuidad marque como
"cerrada" debe tener su propio encabezado `####` con el detalle
verificable, antes de darse por completada en la sección 5.**

---

## 0. CONTEXTO GENERAL DEL PROYECTO

Repo fuente de verdad: `IRAM-PROYECTO` en GitHub
(`https://github.com/MatiasLeonMdz/IRAM-PROYECTO.git`), clonado localmente.
Es un proyecto con dos ramas de trabajo: un mod de Imperator: Rome (IRAM)
y documentación/trabajo de investigación para la Diplomatura UTN.

El problema que se viene resolviendo desde hace varias sesiones: existen
**15 copias de seguridad** viejas (zips/carpetas sueltas) en
`C:\Users\matia\Desktop\testear`, con mucho contenido duplicado y algo de
contenido único que nunca llegó al repo actual. Hay que encontrar ese
contenido único, decidir qué vale la pena rescatar, y solo entonces
ordenar/purgar la carpeta `_CUARENTENA_DUPLICADOS`.

**Regla de oro que se viene siguiendo (§22/§23 de logs previos):** nunca
asumir por nombre o tamaño de archivo. Siempre verificar contenido real
(hash, diff, lectura de inicio/medio/final) antes de decidir si algo es
basura, duplicado, o contenido legítimo a rescatar.

**Regla nueva confirmada en ESTA sesión, agregar a la lista de trampas
conocidas:** el hash SHA-256 por sí solo también puede engañar — dos
archivos con el **mismo contenido real** pueden tener hash distinto solo
por diferencia de terminador de línea (CRLF `\r\n` vs LF `\n`). Hay que
normalizar (`.replace('\r\n','\n')`) antes de comparar por hash o por
diff, o se sobreestima la cantidad de contenido "único" cuando en
realidad es el mismo texto con distinto guardado. A la inversa, nombres
casi idénticos con el mismo número de versión (ej. dos archivos "v1_0")
NO garantizan que sean el mismo contenido — puede ser texto totalmente
distinto que casualmente comparte el string de versión.

**Alcance de la auditoría, aclarado en esta sesión:** el criterio real es
"¿es contenido único de desarrollo, no recuperable en otro lado, y no
es un archivo base del juego bajo `\game\`?" — no "¿es específicamente
del mod IRAM?". Los 16 `Modulo*_Unidad*` (Diplomatura UTN) **SÍ entran
en el alcance**: son insumo para las Tareas 1 y 2 de la UTN. Se trataron
como rescate de bajo esfuerzo (copiar y ubicar) y **quedaron
rescatados y verificados en v15** — los 16 completos, sin duplicados de
hash entre ellos, sin huecos en la grilla Módulo 1–4 × Unidad 1–4, ver
detalle en el encabezado de v15 y en 3.8. Sigue pendiente, aparte de
esto, convertir más material de PDF a .md si hubiera más unidades del
curso sin pasar todavía (no urgente, no forma parte de este bloque ya
cerrado).

---

## 1. HERRAMIENTAS YA CONSTRUIDAS (3 scripts, todos de solo lectura salvo el 3° que copia)

Ubicación en la PC del usuario: `C:\Users\matia\Downloads\`

### `1_descomprimir_copias.py`
Descomprime todos los .zip/.rar/.7z encontrados dentro de una carpeta
origen (busca en todos los subniveles) a una carpeta destino, con
carpetas numeradas cortas (`0001_nombre`, `0002_nombre`...) para evitar
el límite de 260 caracteres de rutas en Windows. Genera
`_mapa_carpetas.csv` (trazabilidad) y `_log_descompresion.txt`.

Ya se corrió una vez:
```
python 1_descomprimir_copias.py "C:\Users\matia\Desktop\testear" "C:\Users\matia\Desktop\copias_descomprimidas"
```

### `2_buscar_contenido_unico.py`
Compara por hash SHA-256 el repo (fuente de verdad) contra una carpeta de
copias. Genera `reporte.csv` y `reporte.md` con todo lo que aparece en
las copias pero NO existe (por contenido, no por nombre) en el repo.
100% solo lectura, no borra ni mueve nada.

Ya se corrió dos veces:
```
# Corrida 1 — contra el contenido ya descomprimido de los zips (93 hallazgos)
python 2_buscar_contenido_unico.py "C:\Users\matia\Documents\IRAM PROYECTO\IRAM PROYECTO" "C:\Users\matia\Desktop\copias_descomprimidas" "C:\Users\matia\Desktop\reporte.csv"

# Corrida 2 — contra la carpeta madre completa "testear" (incluye sueltos, 3334 hallazgos)
python 2_buscar_contenido_unico.py "C:\Users\matia\Documents\IRAM PROYECTO\IRAM PROYECTO" "C:\Users\matia\Desktop\testear" "C:\Users\matia\Desktop\reporte_sueltos.csv"
```
**`reporte_sueltos.csv`/`.md` es el reporte vigente y más completo — usar
ese, no el primero (`reporte.csv` quedó obsoleto/parcial).**

### `3_copiar_candidatos_valiosos.py`
Lee un reporte.csv (de arriba) y copia a una carpeta chica SOLO los
archivos "valiosos" por extensión (.md .txt .json .py .html .csv),
excluyendo ruido conocido (`.git`, `localization`, `mod_pack`,
`by_other_means`, `exodos`). Copia cada hash único una sola vez. Genera
`_indice_copiados.csv` con hash, ruta original, nombre final. Excluye por
default archivos >50MB (parametrizable con `--max-mb`).

Ya se corrió una vez contra `reporte_sueltos.csv`, resultado: 1135
archivos copiados (~132MB) a `C:\Users\matia\Desktop\candidatos_valiosos`,
comprimidos y subidos como `candidatos_valiosos.zip`.

**IMPORTANTE — filtro adicional descubierto y aplicado manualmente (no
está todavía en el script):** de esos 1135, **861 eran archivos base del
juego Imperator Rome** (mod ya terminado, sin valor de desarrollo),
identificables porque su ruta contiene la carpeta `\game\` (ej.
`...\1_MOD\game\common\...`, `...\1_MOD\game\events\...`). El usuario
confirmó: todo lo que esté agrupado bajo una carpeta/zip llamada "game"
se puede descartar sin revisión — son archivos base del juego, no
desarrollo propio.

**Confirmado de nuevo por script en esta sesión:** de los 1135 registros
totales en `_indice_copiados.csv`, exactamente 861 tienen `\game\` en la
ruta original y 274 no — coincide con el conteo del log anterior.

Filtrando `\game\` de la ruta quedan **274 archivos reales** de
desarrollo/documentación (239 .md, 13 .txt, 11 .py, 9 .json, 1 .html,
1 .csv), ~119 MB en total (pesan tanto por varios `.json` de volcados de
chat, ver más abajo).

**Hallazgo nuevo de esta sesión — importante para no repetir el paso "prioridad 1"
tal como estaba planteado:** dentro de esos 274 archivos, **los 274 hashes
SHA-256 son todos distintos entre sí** (verificado con script). Es decir,
el propio `3_copiar_candidatos_valiosos.py` ya deduplicó por hash exacto
al armar el índice ("copia cada hash único una sola vez", como dice su
descripción) — así que la idea original de "barrer duplicados exactos por
hash como paso barato" **ya está hecha implícitamente** y no hay trabajo
adicional de ese tipo para hacer sobre este set de 274. Lo que sí sigue
habiendo son archivos con **el mismo nombre-base pero contenido realmente
distinto** (ver sección 2 nueva más abajo) — esos SÍ requieren diff/lectura,
no hash.

**Sigue pendiente:** actualizar `3_copiar_candidatos_valiosos.py`
agregando `"\\game\\"` a `FILTROS_RUIDO_DEFAULT`, para que el filtrado
sea automático la próxima vez.

---

## 2. QUÉ SE REVISÓ Y SE CONFIRMÓ HASTA AHORA (conclusiones ya cerradas)

### 2.1 — `failed 3.md` (179153 bytes, en `07_sesiones_fallidas/` del repo activo)
- **Es contenido legítimo**, tercera variante distinta de `failed.md` y
  `failed (2).md` (verificado por lectura de inicio/medio/final + hash).
  Transcripción real de sesiones ~s10–s13 (12–16 junio 2026) sobre
  desarrollo de C1/C2 y crítica rigurosa del proyecto.
- **Hallazgo de nombre engañoso confirmado por hash MD5:** el archivo de
  cuarentena `_CUARENTENA_DUPLICADOS/.../failed (3).md` (5272 bytes) NO
  es la copia de respaldo de `failed 3.md` (el grande). Por hash, es en
  realidad un duplicado exacto de `failed (2).md` (el chico). El nombre
  sugiere correspondencia 1-a-1 pero el contenido dice otra cosa.
- **Consecuencia:** `failed 3.md` (el grande, 179KB, contenido único) NO
  tiene ningún backup en ningún lado. Vive solo en `07_sesiones_fallidas/`
  activa del repo.
- **Pendiente de decisión del usuario:** el usuario declaró el principio
  general "todo lo único va en las carpetas y no se purga" — es decir,
  antes de purgar la cuarentena hay que asegurarse de que todo contenido
  único (como este archivo) tenga un lugar seguro/definitivo primero.
  Recomendación pendiente de confirmar: darle un backup explícito en
  `08_documentacion_respaldo/` (o donde corresponda) antes de cerrar el
  caso de la redundancia de cuarentena.
- La cuarentena de `failed (3).md` SÍ es redundante (duplicado exacto por
  hash de `failed (2).md` activo) → candidata segura a purga, una vez
  que se resuelva el punto anterior.

### 2.2 — Familia `FUENTE_DE_VERDAD_IRAM_2026-07-07*` (12 versiones) — ⚠️ CONTRADICE A 2.10, VER NOTA DE RECONCILIACIÓN AL FINAL DE 2.10, NO DAR ESTA SECCIÓN POR BUENA SIN LEER ESA NOTA
- Confirmado por diff exacto: son la MISMA cadena documental creciendo
  por versiones append-only (regla DR-42 mencionada en el propio
  documento). La versión corta (`FUENTE_DE_VERDAD_IRAM_2026-07-07.md`,
  28.8KB) es un prefijo textual EXACTO de la versión `_11` (124KB, la más
  grande y nueva).
- **CONCLUSIÓN CORREGIDA EN v8** (originalmente decía "solo rescatar
  `_11`, las otras 11 son redundantes" — ver corrección de criterio al
  inicio del log): **rescatar las 12 versiones completas.** La relación
  de superset (`_11` contiene textualmente a todas las anteriores) sigue
  confirmada y es la evidencia de que no hay pérdida de contenido, pero
  cada versión intermedia es un estado histórico real del documento
  append-only (regla DR-42) y se conserva como trazabilidad, no se
  purga. No hace falta revisarlas de nuevo ni volver a diffearlas — el
  trabajo de comparación ya está hecho y es válido, solo cambia qué se
  hace con el resultado.
- **Dato importante que el propio documento `_11` revela sobre sí
  mismo** (seteado en sus secciones §12 a §18, ya redactadas por una
  sesión anterior del usuario):
  - Documenta **7 incidentes de "fuga de continuidad"**: archivos de
    trabajo que se redactaron en una sesión pero nunca se subieron como
    adjunto, por lo que no estaban disponibles en la sesión siguiente.
    Esto explica por qué existen tantas variantes sueltas de historiales
    y sesiones "cortadas"/"falladas"/"gap" en las copias de seguridad.
  - **§17 declara como "tarea prioritaria número 1"** (por encima de
    otro pendiente marcado DR-54) ordenar/purgar el árbol de
    documentación — mencionando explícitamente los **544 archivos** de
    `_CUARENTENA_DUPLICADOS` (dos subcopias anidadas casi completas del
    proyecto) cuyo destino nunca se decidió. Es decir: la auditoría que
    se viene haciendo en esta conversación es exactamente la tarea que
    el propio proyecto ya se había marcado como prioritaria.
  - §18: el criterio de diseño del árbol de documentación definitivo
    tiene que ser legible específicamente para "instancias de IA simples
    y tareas cortas", no solo para sesiones largas de reconstrucción.
  - §18 también registra que errores de servicio de Anthropic del
    6-7/07/2026 le costaron al usuario "un día entero de trabajo
    perdido" (código generado a medias, no recuperable).

### 2.3 — Familia `IRAM_historial_desarrollo_2/3/4/5` (crudas vs versiones curadas)
Se descubrió que cada número corresponde a una **cuenta de Gmail
distinta** usada durante el proyecto (exports de historial de chat, no
versiones incrementales del mismo documento):

| Familia | Cuenta Gmail | Cruda | Curada | Veredicto (confirmado por diff) |
|---|---|---|---|---|
| 2 | matileon1990@gmail.com | 819KB, 47 sesiones | `_LIMPIO`, 745KB, 43 sesiones | Curada quita sesiones ajenas (ej. "Microcivilization cheat table", no es de IRAM). **Quedarse con LIMPIO.** |
| 3 | matiasleon1990mza@gmail.com | 527KB, 34 sesiones | `_LIMPIO`, 481KB, 26 sesiones | Mismo patrón. **Quedarse con LIMPIO.** |
| 4 | cristianleonmza@gmail.com | 637KB, 30 sesiones | `_limpio`, 577KB, 21 conversaciones | Mismo patrón. **Quedarse con LIMPIO.** |
| 5 | matiasleon.cmlc@gmail.com | **10.4MB**, 33 sesiones | `_clean(1).md`, 877KB, mismas 33 sesiones | Mismo número de sesiones; la limpia solo remueve basura de exportación ("This block is not supported on your current device yet."), verificado que NO pierde contenido real, incluso tiene más texto legible en algunos tramos. **Quedarse con clean.** |

**CONCLUSIÓN CORREGIDA EN v8** (originalmente decía "solo conservar las
4 curadas, las crudas se descartan" — ver corrección de criterio al
inicio del log): **rescatar los 8 archivos, crudas y curadas.** La
curada no es un duplicado verdadero de la cruda (quita sesiones ajenas
al proyecto, reordena numeración) — es una versión distinta del mismo
documento y ambas cuentan como estado histórico a conservar. Único caso
dentro de este grupo que sí sigue siendo elegible para colapsar sería si
alguna cruda y su curada resultaran ser hash-idénticas tras normalizar
(no es el caso confirmado acá — hay diferencia real de sesiones
incluidas).

### 2.4 — Sección 3.1 del log anterior: familia de "históricos"

**a) `IRAM_Diseñador1_Historial.md` (cruda, 1182785B) vs
`IRAM_Diseñador1_Historial_LIMPIO.md` (1018589B)**
- Mismo patrón que la familia 2.3: confirmado por diff línea a línea y
  por comparación de IDs de sesión (UUID), que la LIMPIA elimina
  exactamente 3 sesiones ajenas al desarrollo de IRAM — "Eliminar
  efectos de hambre en Surviving the Aftermath" (otro juego), "Consola
  de Imperator Rome con cheat engine" (configuración personal de
  achievements, no desarrollo del mod), y "Finding a mod without owning
  the game" (búsqueda de un mod ajeno). Las 24 sesiones restantes tienen
  IDs y contenido idénticos entre cruda y limpia, solo renumeradas.
- **CONCLUSIÓN CORREGIDA EN v8** (originalmente decía "quedarse solo con
  LIMPIO" — ver corrección de criterio al inicio del log): **rescatar
  ambas, cruda y LIMPIO.** La LIMPIA no es un duplicado verdadero de la
  cruda (quita 3 sesiones ajenas, renumera) — mismo patrón que 2.3, es
  una versión distinta a conservar como trazabilidad, no se descarta.

**b) `IRAM_HISTORIA_COMPLETA_v1_1.md` (260589B) vs
`IRAM_HISTORIA_COMPLETA_v1_2 (2).md` (268444B)**
- Confirmado por diff estructural (288 secciones `#`/`##` idénticas en
  orden y texto en ambos) más diff línea a línea: v1_2 es un superset
  estricto de v1_1. La ÚNICA diferencia real es que la sección "1.2 Qué
  se implementó en v4.x" fue expandida en v1_2 con el resultado del
  análisis del gap v4.1→v4.3.16 (que se había cerrado el 2026-06-11,
  ver también el archivo `IRAM_gap_v4_1_a_v4_3_16_CERRADO_2026-06-11.md`
  de la sección 3.2 pendiente): agrega tabla completa de versiones
  v4.3.2 a v4.3.16, el hallazgo de "cuentas paralelas" (las 5 cuentas de
  Gmail trabajaban en simultáneo en mayo 2026, no secuencialmente como
  se asumía antes), y una lista de deuda residual. El resto del
  documento, verificado con diff de línea, es **idéntico byte a byte**
  antes y después de esa sección.
- **CONCLUSIÓN CORREGIDA EN v8** (originalmente decía "solo rescatar
  v1_2, v1_1 no aporta nada" — ver corrección de criterio al inicio del
  log): **rescatar ambas, `IRAM_HISTORIA_COMPLETA_v1_1.md` y
  `IRAM_HISTORIA_COMPLETA_v1_2 (2).md`.** La relación de superset sigue
  confirmada (v1_2 expande la sección 1.2 sin perder nada de v1_1), pero
  v1_1 es un estado histórico real (anterior al cierre del gap
  v4.1→v4.3.16) y se conserva como trazabilidad, no se descarta.

**c) `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md` (239703B) vs
`IRAM_PROYECTO_REORGANIZADO_06-07-2026.md` (402041B) — ⚠️ CASO QUE ROMPIÓ
LA HIPÓTESIS INICIAL, NO ASUMIR NUNCA POR FECHA**
- El log anterior especulaba "probablemente la del 06 sea superset de la
  del 05 (misma lógica que FUENTE_DE_VERDAD)". **Verificado por diff:
  ESO ES FALSO.** No es una relación prefijo/superset.
- Son **dos transcripciones de sesión de auditoría distintas**, una por
  día. La del 05-07 empieza con `INICIO SESION 05-07-2026 20:20` y
  termina con `FIN SESION 05-07-2026 22:45` (cierra revisando el corpus
  B crudo, carpeta `05_corpus_B_crudo`). La del 06-07 arranca con un
  prompt de continuación distinto ("continua el análisis del proyecto
  leyendo las transcripciones de las sesiones cortadas del 05/07 y 06/07
  en ese orden...") y termina con un bloque de verificación puntual de
  hashes de duplicados (`IRAM_C1_s3_draft_s20.md`,
  `IRAM_hitos_metodologicos_2026-06-11_v6.md`, etc.), trabajo que no
  aparece en la del 05.
- Ambas transcriben una auditoría del mismo inventario
  (`IRAM_PROYECTO3.zip`) y por eso comparten 25 títulos de sección
  idénticos al principio (el mismo inventario fue reutilizado/adjuntado
  en ambas sesiones), pero el cuerpo real de cada transcripción — lo que
  se hizo, se preguntó y se concluyó ese día — es distinto y no
  redundante.
- **CONCLUSIÓN CERRADA: hay que rescatar LOS DOS archivos, no solo el
  más nuevo.** Cada uno documenta trabajo de auditoría de un día
  distinto, con hallazgos propios no repetidos en el otro.

### 2.5 — NUEVO EN ESTA SESIÓN — Grupos chicos de 3.6, prioridad 1 (README/INDICE/paper/skill)

**Contexto:** al intentar aplicar la "prioridad 1: duplicados baratos por
hash" del log v3, se descubrió que **no hay ningún duplicado exacto por
hash** dentro de los 274 archivos filtrados (ver hallazgo en sección 1).
Así que se pasó directamente a diff/lectura de los pares y grupos chicos
que el log v3 marcaba como sospechosos de duplicado. Resultados:

**a) READMEs de carpeta (15 archivos, todos con nombre `README.md` o
`README (2).md`, cada uno de una carpeta/backup distinto)**
- Verificado con normalización CRLF→LF antes de comparar: de los 15,
  **14 tienen contenido único** (son READMEs de carpetas distintas del
  árbol del proyecto — `1_MOD/`, `2_DOCUMENTACION/`, `3_ANALISIS/`,
  `_CUARENTENA_DUPLICADOS/`, o snapshots de distintos backups como
  `IRAM_PROYECTO_REORGANIZADO_v6` — por diseño no son la misma familia
  versionada).
- **Único duplicado real encontrado:** `README__7efad22a.md` (1553B) y
  `README__cc62dfe9.md` (1525B) son **el mismo contenido exacto**, la
  diferencia de tamaño era solo CRLF vs LF. Colapsar a uno solo.
- **Caso especial detectado dentro de este grupo — mismo patrón que
  2.4.c, agregar a la lista de "cadenas con snapshots intermedios
  reales":** `README__63be8f4a.md` (1118B, ruta
  `IRAM PROYECTO/2_DOCUMENTACION/README.md`, backup plano) es una
  **versión anterior genuina** del README de `2_DOCUMENTACION/`, de
  antes de la "mudanza del 2026-07-08" que describe explícitamente
  `README__7efad22a.md`/`README__cc62dfe9.md` (que documentan mover
  `01_logs_replanteo/` a `0_REPLANTEOS_Y_DECISIONES/` y
  `06_historial_desarrollo_mod/` a `1_MOD/06_historial_desarrollo/`).
  No es superset ni redundante — es un snapshot de una estructura de
  carpetas real y anterior. **Rescatar los 3 (63be8f4a, más el par
  colapsado 7efad22a=cc62dfe9) como documentación histórica de la
  reorganización.**
- **Veredicto: de 15 README → quedan 14 archivos finales tras colapsar
  el único duplicado real.** Los otros 13 no tienen relación entre sí
  (una carpeta cada uno), no requieren más comparación.

**b) INDICE.md (4 archivos, todos de la raíz del proyecto en distintos
backups)**
- Verificado con normalización CRLF→LF: **hay un duplicado exacto**
  (`INDICE__877446a8.md` = `INDICE__df6ac725.md`, 2530B, mismo
  contenido salvo CRLF).
- Los otros 3 valores de contenido (`25c3aac9` 2478B, `877446a8`≡`df6ac725`
  2530B, `09199357` 3208B — este último es el único con sufijo "(2)" en
  el nombre original) son **3 pasos reales y sucesivos de la misma
  sesión de reorganización 2026-07-08**, NO duplicados:
  1. `25c3aac9` (más antiguo): sin sección `0_REPLANTEOS_Y_DECISIONES/`,
     nota de cuarentena dice "pendiente de purga".
  2. `877446a8`/`df6ac725` (intermedio): agrega mención a
     `WIKI_DOCUMENTACION_v3.md`, cuarentena ya dice "vacía, purgada
     2026-07-08" — pero todavía sin `0_REPLANTEOS_Y_DECISIONES/`.
  3. `09199357` (más nuevo): sí agrega `0_REPLANTEOS_Y_DECISIONES/` como
     primera entrada, y suma una nota de "sesión posterior" con más
     cambios (carpeta nueva, subcarpetas de `3_ANALISIS/` movidas,
     purga de un duplicado puntual, 4 archivos de raíz reubicados).
- **Verificado explícitamente (no asumido) si el más nuevo es superset
  literal de los otros dos: NO lo es al 100%** — hay 2 líneas del
  intermedio (la lista de carpetas de primer nivel sin
  `0_REPLANTEOS_Y_DECISIONES/`, y el pie de nota sin la frase de
  "sesión posterior") que no aparecen literalmente en el más nuevo,
  porque son las líneas que el propio cambio de contenido reemplazó.
  Diferencia esperable y menor, no oculta contenido real perdido.
- **CONCLUSIÓN CERRADA: rescatar los 3 INDICE con contenido distinto**
  (`25c3aac9`, `877446a8`≡`df6ac725` colapsado a 1, `09199357`) como
  snapshots reales de la evolución del índice. De 4 archivos → 3 finales.

**c) `IRAM_paper_metodologia_v1_0.md` (128e4c6c, 24570B) vs
`IRAM_paper_metodologia_v1_0(1).md` (2658a8be, 20630B)**
- ⚠️ **El log v3 sospechaba duplicado por compartir el mismo número de
  versión "v1_0". Verificado por comparación de encabezados y contenido:
  FALSO — son dos borradores completamente distintos del mismo paper
  (Paper C1).** Comparten tema general y estructura de alto nivel
  (resumen ejecutivo, "el proyecto en números", "las dos historias en
  paralelo", hallazgos con evidencia, qué transfiere y qué no), pero
  **el título, el framing y la redacción de cada hallazgo son distintos
  en cada versión** — no es la misma versión copiada dos veces, ni una
  contiene a la otra (`a not in b`, `b not in a`, confirmado).
- **CONCLUSIÓN: contenido único en los dos, rescatar ambos.** Ninguno
  subsume al otro — son iteraciones alternativas de redacción del mismo
  paper, no una cadena de versiones lineal.

**d) `IRAM_skill_desarrollo_ia_v2_0.md` (4d388c49, 4454B) vs
`IRAM_skill_desarrollo_ia_v2_0 (3).md` (e6874d63, 5307B)**
- Mismo patrón que (c): ambos "v2.0" pero **contenido y estructura
  completamente distintos**. El primero (4d388c49) tiene 6 secciones
  numeradas (Cuándo usar / Arranque / Durante / Cierre / Si falla /
  Principio de operación) y termina con una nota de procedencia
  ("Extraído de: IRAM_paper_metodologia_v1_0.md / Reemplaza:
  IRAM_SKILL_desarrollo_con_IA_v1_0.md"). El segundo (e6874d63) tiene
  secciones temáticas en mayúsculas (ARQUITECTURA DE CONTEXTO / DIVISIÓN
  DE TRABAJO / DIAGNÓSTICO DE MODOS DE FALLA / DECISIONES DESCARTADAS /
  OVERHEAD DE DOCUMENTACIÓN / CONDICIONES DE TRANSFERENCIA), sin esa
  nota de procedencia.
- **CONCLUSIÓN: contenido único en los dos, rescatar ambos.** Dos
  redacciones alternativas del mismo skill operacional, no versión+copia.

---

### 2.6 — CERRADA EN ESTA SESIÓN (v20): Familia "gap" (sesión v4.1-4.3), 7 archivos

**Archivos:**
- `IRAM_gap_v4_1_a_v4_3_16_CERRADO_2026-06-11__48eb619e.md` (15776 B)
- `IRAM_gap_v4_1_a_v4_3_16_nota_deuda_1__e4fc50b3.md` (4276 B)
- `IRAM_gaps_conocimiento_2026-06-12__fbf00383.md` (27996 B)
- `sesion gap v4.1 - 4.3__5e1c015f.md` (161224 B)
- `sesion gap v4.1 - 4.3 parte 1__9d868df0.md` (166037 B)
- `sesion gap v4.1 - 4.3 parte 2__c893bd95.md` (4813 B)
- `sesion gap v4.1 - 4.3 parte 3__98f5fa12.md` (49736 B)

Los 7 tienen hash distinto entre sí en `_indice_copiados.csv` (todos con
`cantidad_lugares_donde_aparece = 2`, todos provenientes de carpetas
`_CUARENTENA_DUPLICADOS` — recordatorio de 3.6.octies de que esa
etiqueta de carpeta no implica nada por sí sola). Se dividen en 3
sub-grupos con relaciones internas distintas.

**Sub-grupo 1 — transcripciones de chat (4 archivos):**
- `sesion gap v4.1 - 4.3__5e1c015f.md` (161224 B): checkpoint de una
  sesión cortada a mitad de trabajo.
- `sesion gap v4.1 - 4.3 parte 1__9d868df0.md` (166037 B): **superset
  exacto por substring** del anterior (confirmado con
  `SequenceMatcher`, ratio 0.985, y `b in a → True`) — contiene el
  checkpoint completo más 4681 caracteres de continuación (la sesión
  que retoma el trabajo después del corte, "estabamos en esta sesion y
  se corto").
- `sesion gap v4.1 - 4.3 parte 2__c893bd95.md` (4813 B): duplicado por
  substring exacto de esa misma cola de continuación — ya está contenida
  íntegramente dentro de `parte 1` (`p2 in a → True`, tamaños
  coincidentes: 4681 vs 4813 con separador). Contiene un hallazgo
  metodológico relevante como historia real del razonamiento del
  proyecto: la hipótesis inicial de "cuentas trabajando en paralelo"
  (5 Claudes simultáneos en mayo 2026), que después fue corregida a
  "rotación secuencial, 0 interleavings en 7313 mensajes" (ver
  3.6.undecies/3.6.terdecies) — se conserva como estado intermedio real,
  no se descarta por estar superado.
- `sesion gap v4.1 - 4.3 parte 3__98f5fa12.md` (49736 B): sesión
  **independiente y posterior**, ratio de similitud 0.009 contra
  `parte 1` (`p3 in a → False`) — trabajo distinto: edición real de
  `IRAM_HISTORIA_COMPLETA_v1_1` → `v1_2` e `hitos_metodologicos`,
  incorporando la narrativa del gap ya cerrado.

**Sub-grupo 2 — documentos formales, relación de reemplazo declarado (2 archivos):**
- `IRAM_gap_v4_1_a_v4_3_16_nota_deuda_1__e4fc50b3.md` (4276 B): nota de
  deuda original, 2026-06-10, con implementaciones confirmadas por
  evidencia indirecta (sin conversations.json) y estimación de que el
  período involucraba solo CLAUDE_1 y CLAUDE_3.
- `IRAM_gap_v4_1_a_v4_3_16_CERRADO_2026-06-11__48eb619e.md` (15776 B):
  declara textualmente **"Reemplaza a: `IRAM_gap_v4_1_a_v4_3_16_nota_deuda.md`"**.
  No es superset textual (ratio 0.053, no substring) — es una
  reescritura completa a partir de fuente primaria real (los 5
  `conversations.json`, ~441 conversaciones). **Superset semántico
  confirmado por lectura completa de ambos documentos, punto por
  punto**: cada implementación, sesión y "dónde incorporar" de la nota
  original aparece resuelta, corregida o expandida en `CERRADO` — con
  corrección crítica incluida (v4.3.16 no fue generada por la sesión
  que la nota original suponía, sino por otra sesión distinta del mismo
  día) y evidencia ampliada (5 cuentas trabajando el período en
  paralelo, no solo 2). Mismo patrón que `PROMPT_MAESTRO` v1.6/v1.8
  (3.6.quater) e `IRAM_analisis_cuantitativo` base→v2 (3.6.undecies):
  evidencia mixta, no asumir "más nuevo = superset" sin leer completo.

**Sub-grupo 3 — documento independiente (1 archivo):**
- `IRAM_gaps_conocimiento_2026-06-12__fbf00383.md` (27996 B): sin
  relación real con el resto de la familia — Plantilla B (análisis de
  gaps de conocimiento wiki vs. chats), sobre un corpus distinto
  (`IRAM_historial_unificado_2026-06-12.md`, 7345 msgs, no el gap
  v4.1→v4.3.16). Ratios de similitud contra los otros dos documentos
  formales: 0.014 (vs. CERRADO) y 0.026 (vs. nota_deuda) — en el rango
  de independencia genuina confirmado en 3.6.quindecies (0.03–0.08),
  incluso más bajo.

**CONCLUSIÓN CERRADA: se conservan los 7 archivos completos, sin
descartes** (criterio de v8: solo se descarta duplicado exacto por
hash — acá no hay ninguno, ni siquiera `parte 2`, que aunque es
redundante en contenido tiene hash propio y forma parte legítima de la
trazabilidad histórica).

### 2.7 — Sección 3.3: Charlas sueltas (charla_7 a charla_12) — CERRADA EN v21

- `charla_7__dc251fc9.md` (56544 B, 548 líneas)
- `charla_8__974dda23.md` (37270 B, 377 líneas)
- `charla_9__5b5d4dc1.md` (146700 B, 1125 líneas)
- `charla_10__e0c336da.md` (55852 B, 596 líneas)
- `charla_11__277ee07b.md` (56963 B, 496 líneas)
- `charla_12__4ae96032.md` (144244 B, 1588 líneas)

**Confirmación de la cadena narrativa por texto propio:** `charla_9`
arranca literalmente diciendo "sesiones 7 y 8 cortadas, adjunto los
archivos .md más recientes y un .zip actualizado", y su propio
razonamiento describe leer `charla_7.md` y `charla_8.md` desde disco
para retomar el trabajo — consistente con el dato ya citado en 2.2
(`FUENTE_DE_VERDAD_11 §16`: "charla_7 a charla_11 fueron cinco
sesiones cortadas… charla_12 reconstruyó el contenido recuperable").
Por header de adjuntos (`charla_10` adjunta charla_9+charla_7;
`charla_11` adjunta charla_10+charla_9+charla_7; `charla_12` adjunta
las 5 completas), se confirma que son sesiones consecutivas que se
retoman unas a otras, no documentos independientes por azar.

**Comparación por contenido (`SequenceMatcher`, ratio + substring),
las 5 sueltas contra `charla_12`:**

| Par | len(A) | ratio | ¿A ⊂ B? |
|---|---|---|---|
| charla_7 vs charla_12 | 55681 | 0.5632 | No |
| charla_8 vs charla_12 | 36806 | 0.0929 | No |
| charla_9 vs charla_12 | 146361 | 0.0133 | No |
| charla_10 vs charla_12 | 55219 | 0.0262 | No |
| charla_11 vs charla_12 | 56447 | 0.0816 | No |

Ninguna es substring de `charla_12`. El ratio de `charla_7` (0.56,
notablemente más alto que el resto) se investigó bloque por bloque:
de solo 2 bloques de coincidencia >200 caracteres, uno es el header de
instrucciones de adjuntos que se repite al inicio de cada sesión
nueva (mismo texto pegado por el usuario en varias charlas: "Adjunto
FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md — es el único punto de partida
operativo…") y el otro es una frase de transición genérica ("Lo que
confirmé leyendo ambas completas..."). **No hay bloque de contenido
sustantivo compartido entre charla_7 y charla_12** — el ratio alto es
artefacto del texto repetido de instrucciones, no absorción real.

**Conclusión sobre el dato de FUENTE_DE_VERDAD_11 §16:** el dato es
correcto en cuanto a que `charla_12` reconstruye el *estado* del
proyecto después de las 5 sesiones cortadas, pero **no reemplaza el
*contenido* de esas 5** — cada una conserva razonamiento, decisiones
puntuales y al menos un diagrama SVG propio (ver contenido de
`charla_7`, tail) que no vuelve a aparecer en `charla_12`. Es una
síntesis narrativa nueva, no una copia textual.

**Comparación de las 5 sueltas entre sí:**

| Par | ratio |
|---|---|
| 7 vs 8 | 0.0556 |
| 7 vs 9 | 0.0141 |
| 7 vs 10 | 0.0272 |
| 7 vs 11 | 0.0301 |
| 8 vs 9 | 0.0185 |
| 8 vs 10 | 0.0497 |
| **8 vs 11** | **0.1379** |
| 9 vs 10 | 0.0179 |
| 9 vs 11 | 0.0384 |
| 10 vs 11 | 0.0616 |

Todos los pares caen en el rango de independencia genuina ya calibrado
en el proyecto (0.03–0.08), salvo `charla_8` vs `charla_11` (0.14),
investigado en detalle: `charla_8 in charla_11` → False y viceversa
(no hay relación de substring), pero sí hay un bloque de coincidencia
de ~1578 caracteres. Por contexto: el texto compartido es el cierre
real de la sesión `charla_8` (la respuesta final sobre "Caso #8",
skills C1/C2), y aparece dentro de `charla_11` porque esa sesión
**ejecuta `tail -20 charla_8.md` como comando de verificación** para
releer el corte exacto de la sesión anterior antes de continuar — el
output de ese comando queda pegado en la transcripción de `charla_11`.
Es una cita operativa de relectura, mismo patrón que otras familias
del log donde una sesión relee a la anterior desde disco antes de
retomar el trabajo (confirmado también con `grep` de patrones
`tail -`/`cat /mnt` en `charla_9`, `charla_10`, `charla_11` y
`charla_12`: las 4 tienen entre 1 y 5 ocurrencias, consistente con este
mismo patrón de relectura puntual, no con absorción de contenido
completo).

**CONCLUSIÓN CERRADA: se conservan las 6 charlas completas, sin
descartes** (criterio de v8: no hay ningún duplicado exacto por hash
ni por substring; el único solapamiento real es una cita operativa
puntual dentro de su contexto normal de trabajo, no un documento
redundante).

### 2.8 — Aclaración sobre el "bloque de ~13 archivos no mapeados" — CERRADA EN v22

**Contexto:** en el chat de esta sesión se planteó como hallazgo nuevo un
bloque de ~13 archivos "no mapeados por el log" (ni 3.4, ni 3.9, ni
FUENTE_DE_VERDAD): `IRAM_Diseñador1_Historial` (+LIMPIO), `correccion de
documentacion` (+"2"), `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD`,
`INVENTARIO_COMPLETO_MATERIAL`, `IRAM_PROYECTO_REORGANIZADO` (x2 fechas),
`LOG_REORGANIZACION`, `Qwen_markdown`, `memoria_claude_volcado`,
`resultado_prueba_fuga_memoria`, `sigue log`.

**Antes de escribir este addon se verificó cada nombre contra el cuerpo
real del log v21 (no contra la nota de continuidad ni contra la memoria
de la sesión anterior).** Resultado: el bloque **no es tan nuevo como
parecía** — 10 de los 12 archivos ya estaban identificados en el log, en
tres estados distintos. Solo 1 par (2 archivos) es un hallazgo genuinamente
nuevo, sin ninguna mención previa.

#### a) Ya CERRADOS con veredicto firme (4 archivos, no requieren trabajo)

- `IRAM_Diseñador1_Historial.md` y `IRAM_Diseñador1_Historial_LIMPIO.md`
  — resueltos en 2.4.a, con corrección explícita registrada bajo el
  criterio de v8 (línea 2319: "CORREGIDO EN v8"). **Se conservan ambas
  versiones**, no es un archivo suelto sin tratar.
- `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md` y
  `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md` — resueltos en 2.4.c, caso
  marcado explícitamente como "CASO QUE ROMPIÓ LA HIPÓTESIS INICIAL, NO
  ASUMIR NUNCA POR FECHA": no es relación superset/prefijo, son dos
  transcripciones de auditoría de días distintos (05-07 y 06-07), cada
  una con hallazgos propios no repetidos en la otra. **Conclusión
  cerrada: se rescatan los dos.**

#### b) Ya IDENTIFICADOS pero pendientes de revisión individual (7 archivos)

Estos 7 ya figuran, tal cual, dentro de la lista "Otros sueltos sin
familia clara — revisar uno por uno — sin tocar" (línea 1078 en
adelante del cuerpo del log): `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`,
`INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`,
`Qwen_markdown_20260705_q4xkzeqjf (2).md`, `memoria_claude_volcado.md`,
`volcado_memoria (2).md`, `LOG_REORGANIZACION_2026-07-05.md`,
`resultado_prueba_fuga_memoria.md`, `sigue log.md`.

No son un descubrimiento nuevo: el log ya los tenía anotados como
pendientes desde antes de v21, dentro de esa lista de "sueltos sin
familia clara". Lo único nuevo acá es la confirmación (contra
`_indice_copiados.csv`, filtrando `\game\`) de que efectivamente están
dentro del universo real de 274 archivos y no son ruido del zip completo.
Sobre `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` el log ya deja una
nota propia (línea 1088): posible fuente del bloque "INVENTARIO COMPLETO
DEL MATERIAL DE ARCHIVO" citado en 2.4.c — pendiente de revisar junto
con esa familia, no de forma aislada.

**Estado: sigue pendiente su revisión uno por uno, tal como decía el log
original. Este addon no cambia ese estado — solo confirma que no son un
grupo nuevo.**

#### c) Hallazgo genuinamente NUEVO (2 archivos, sin ninguna mención previa en el log)

`correccion de documentacion.md` (21965B) y `correccion de documentacion
2.md` (25366B) — ambos en
`_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/`
del repo `IRAM_PROYECTO_FIX2_cuarentena_completa`. Verificado por
inspección directa de contenido (no solo nombre):

- **No son duplicados entre sí ni versiones de una cadena simple.** Son
  dos sesiones de trabajo secuenciales sobre el sistema de documentación
  del proyecto (meta-nivel: cómo documentar, no contenido de desarrollo
  del mod en sí).
- `correccion de documentacion.md` (sin sufijo) es la sesión más
  temprana: diagnostica problemas estructurales del sistema de
  documentación vigente en ese momento (PROMPT_MAESTRO como "monolito",
  templates que generan ruido de contexto, R14 sin mecanismo de
  promoción) y termina generando `SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md`
  como output.
- `correccion de documentacion 2.md` **cita explícitamente al primero
  como su propio input** ("The user has uploaded two files:
  correccion_de_documentacion.md [...] SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md")
  — es decir, hay relación de continuación textual directa y verificable,
  no una hipótesis por nombre similar. Esta sesión ejecuta la corrección
  diagnosticada en la primera y termina generando 3 archivos nuevos:
  `PROMPT_REGLAS_DOCUMENTACION_v2.md`, `SESSION_LOG_DOCUMENTACION_s22.md`
  y `WIKI_DOCUMENTACION_v1.md`.
- **Relación:** progresión real de una misma línea de trabajo
  (diagnóstico → corrección ejecutada), no bifurcación ni duplicado.
  Mismo patrón ya calibrado en el proyecto para pares checkpoint→ejecución
  (ver regla de v13 en 3.6.octies sobre progresión vs. bifurcación).
- **Bajo el criterio de v8: se conservan ambos**, íntegros, como estados
  reales y distintos del proceso de corrección del sistema de
  documentación. Ninguno es descartable.
- **Verificación cruzada de los 3 archivos generados por `correccion de
  documentacion 2.md` — completada:**
  - `WIKI_DOCUMENTACION_v1.md` (hash `d491f4ac...`, 10781B) es, por hash
    exacto, **el mismo archivo** ya cerrado en 3.6.bis dentro de la
    cadena `WIKI_DOCUMENTACION_v1/v2/v3` (conservar las 3 versiones). El
    propio `_indice_copiados.csv` lo marca con
    `cantidad_lugares_donde_aparece: 2` — vivía en dos rutas del disco
    original y ya fue dedupicado a una sola entrada. No requiere trabajo
    nuevo.
  - `PROMPT_REGLAS_DOCUMENTACION_v2.md` (6624B) — sigue en la lista de
    "sueltos sin familia clara — sin tocar" (línea 1069). Sigue
    pendiente de revisión, pero ahora con procedencia confirmada: es el
    output real de la sesión `correccion de documentacion 2.md`, no un
    suelto sin origen.
  - `SESSION_LOG_DOCUMENTACION_s22.md` (11382B) — **sin ninguna mención
    previa en el log, hallazgo nuevo real.** Declara textualmente en su
    encabezado: "Reemplaza: SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s20.md
    + SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md" — hay una
    cadena de 3 eslabones completa y sin tocar: `_s20` (9859B) → `_s21`
    (13278B, generado por `correccion de documentacion.md`) → `s22`
    (11382B, generado por `correccion de documentacion 2.md`). Ninguno
    de los tres tiene sección propia todavía. Por la regla de "reemplazo
    declarado" de v20 (2.6), la declaración textual no basta para
    confirmar superset — falta diff/lectura —, pero bajo v8 se
    conservan los 3 de cualquier forma.

#### d) Cadena nueva identificada para la próxima sesión (mapeada, no cerrada en este addon)

Queda mapeada, pero sin diff, la cadena completa del ciclo de corrección
del sistema de documentación del 17/06/2026:
`SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s20.md` (9859B) →
`correccion de documentacion.md` diagnostica sobre esa base → genera
`SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md` (13278B) → es
reemplazado (declarado, no verificado) por `SESSION_LOG_DOCUMENTACION_s22.md`
(11382B), generado junto con `PROMPT_REGLAS_DOCUMENTACION_v2.md` en la
sesión `correccion de documentacion 2.md`.
**Recomendación: abrir como sección nueva de 3.6 en la próxima sesión
(cadena SESSION_LOG_DOCUMENTACION s20→s21→s22 + prompt asociado), con
diff completo entre los 3 SESSION_LOG antes de aceptar el "Reemplaza"
textual como superset real.**

#### Nota metodológica de este addon

Este addon es en sí mismo un ejemplo del mismo patrón que motivó el
aviso de integridad documental de v18: un hallazgo presentado como
"nuevo" en el chat resultó, al verificarlo contra el cuerpo real del
log (no contra la nota de continuidad ni contra el resumen de la
sesión anterior), estar mayormente ya cubierto. Se documenta acá para
que quede trazado, siguiendo la misma regla que ya rige el resto del
log: todo cierre o corrección debe respaldarse con encabezado propio y
evidencia verificable, no solo con la afirmación de resultado.

---

---

### 2.9 — CERRADA (v23 + v24): `SESION TRUNCADA` ⊃ `IRAM_SUPERBACKUP_v2_1` (resuelve un pendiente de 3.9), y los 4 `fallo*`/`SESION TRUNCADA` de 3.4 — **sección 3.4 completa desde v24**

**Contexto:** continuación directa de 3.4 (sesiones "falladas"/"truncadas"
sueltas). Antes de escribir este addon se repitió cada verificación desde
cero en el contenedor de esta sesión (descompresión propia del zip, hash
y diff propios) — no se dio por buena ninguna conclusión heredada de un
chat anterior sin recalcularla.

#### a) `SESION TRUNCADA.md` ⊃ `IRAM_SUPERBACKUP_v2_1.md` — verificado por prefijo exacto

`IRAM_SUPERBACKUP_v2_1__a97ba375.md` (224167 bytes, listado como
pendiente sin comparar en 3.8 y 3.9) resultó ser **un prefijo textual
exacto** de `SESION TRUNCADA__42654d23.md` (234348 bytes), verificado con
`nb.startswith(na)` sobre el texto completo normalizado (CRLF→LF): el
resultado es `True`, carácter por carácter, sin ninguna divergencia en
las ~220 mil letras compartidas.

`SESION TRUNCADA` = `IRAM_SUPERBACKUP_v2_1` completo + 216 líneas
adicionales al final. Esas 216 líneas no son contenido técnico del mod:
son un fragmento de conversación posterior (el operador preguntando qué
archivos cargar en la sesión siguiente, y la respuesta armando un plan
de "Track 1 / Track 2"). El cuerpo técnico (Secciones 0 a los ERROR 1–26
de mecánicas del mod) es idéntico entre ambos, sin variaciones.

**Veredicto:** `IRAM_SUPERBACKUP_v2_1.md` se descarta por ser subconjunto
exacto y estrictamente inferior. Se conserva únicamente `SESION
TRUNCADA.md`, que es la versión más completa. Esto cierra el pendiente
de `IRAM_SUPERBACKUP_v2_1.md` que figuraba abierto en **3.8 y 3.9**
simultáneamente con el cierre de este ítem de 3.4.

#### b) Los 3 `fallo*` — relación real verificada, no solo por nombre

Se comparó línea por línea (no por caracteres sueltos, que en corridas
previas dio un ratio engañoso por `quick_ratio`/autojunk con textos
largos) entre los tres archivos:

- **`fallo sesiones transcript 16-06-2026.md` (730530 bytes) vs `fallo
  sesiones 16-06-2026.md` (328442 bytes):** 95.2% de las líneas del
  archivo corto (4192 de 4403) están presentes en el largo, con un bloque
  continuo de 3712 líneas coincidentes. El archivo corto **no es
  substring exacto** del largo (`a in b` → `False`) — hay reescritura
  parcial, no solo recorte —, pero la relación de contenido compartido es
  real y mayoritaria: el transcript largo es la conversación cruda
  completa; el corto es un extracto/resumen editado de la misma sesión.
- El transcript largo **termina generando literalmente** el archivo
  `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19.md` (confirmado
  leyendo las últimas líneas del archivo: contiene el comando `cat > ...
  <<EOF`, el contenido completo del s19, y el eco `wc -l` de salida). Ese
  `s19` ya está **cerrado en 3.6.sedecies** como parte de la cadena
  s19→s22.
- **`fallo DOCUMENTACION 19-06-2026.md` (67718 bytes):** verificado como
  **independiente** de los otros dos — menos del 1% de líneas
  coincidentes contra cualquiera de ellos (6 de 747, puro boilerplate).
  No comparte contenido real con el grupo `fallo sesiones*`.

**Veredicto:**
- `fallo sesiones transcript 16-06-2026.md`: **conservar** — es la
  transcripción cruda de una sesión que ya dejó su destilado formal
  (`s19`) cerrado en otra sección, mismo patrón que `failed 3.md` en 2.1
  (transcript crudo vs. destilado formal, se conservan ambos porque
  cubren estados distintos del proceso).
- `fallo sesiones 16-06-2026.md`: **conservar** — aunque comparte el 95%
  de sus líneas con el transcript, no es substring exacto (tiene
  reescritura editorial propia), así que no es un duplicado limpio
  descartable sin revisión editorial más fina. Se deja conservado bajo
  el criterio general de v8 (ante la duda, no descartar).
- `fallo DOCUMENTACION 19-06-2026.md`: conservar, verificación contra el
  corpus grande completada en v24 — ver 2.9.c.

#### c) `fallo DOCUMENTACION 19-06-2026.md` — CERRADO EN v24, verificado contra el corpus grande

**Qué es realmente:** no es una transcripción cortada pese al nombre de
la familia — es una **transcripción de sesión completa y cerrada**,
donde Claude lee 27 archivos de un zip (`DOCUMENTACION.zip`, distinto
del zip de esta auditoría) en orden cronológico real de metadata
interna (no por sufijo de nombre) y entrega una síntesis final (líneas
703–746 del archivo). Las primeras ~50 líneas muestran un intento
fallido de upload de una sesión previa dentro del mismo archivo —
probable origen del nombre "fallo", pero no es un corte de este
documento.

**Verificación contra el corpus (lo que quedaba pendiente desde v23):**
se comprobó que todos los archivos que el documento menciona/analiza
existen en el corpus real de 274:
`IRAM_C1_final.md`, `WIKI_DOCUMENTACION_v2.md`,
`spec_c_zip_history.py` (base y variante "(3)"),
`SESSION_LOG_ANALISIS_C1_2026-06-18.md` y sus versiones v2 (y variante
"(2)"), v3, v4, v5. Los `.json` de output de las specs A/B/C que
menciona (`spec_a_candidates.json`, `spec_b_democratizacion.json`,
`spec_c_zip_history.json`) **no están** en el corpus — coherente con
ser productos efímeros de ejecución, no documentación, no se marca
como pérdida.

**Hallazgo verificado por diff directo** (no aceptado solo porque el
propio documento lo narra, mismo criterio que 3.6.sexies/3.6.septies):
el documento afirma que `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md`
tiene el encabezado roto — promete acumular "incidente del mod (DC-11)
+ hallazgo de proceso (H-PROC1)" pero el cuerpo no contiene ninguna
sección nueva. Verificado de forma independiente:
- `grep -n "DC-11\|H-PROC1"` sobre v5.md → las únicas 2 apariciones de
  esos términos en todo el archivo están en el encabezado (líneas 4 y
  6). Cero apariciones en el cuerpo.
- Tamaños: v4 = 42.066 bytes, v5 = 42.413 bytes (+347 bytes).
- `diff` completo v4 vs v5: la única diferencia real son 5 líneas de
  encabezado (fecha, versión, "Reemplaza", "Producido por"). El resto
  del cuerpo es idéntico carácter por carácter.
→ Confirmado exacto: `v5.md` tiene el encabezado desincronizado de su
  cuerpo — mismo tipo de riesgo que advierte el aviso de integridad
  documental (v18), pero ocurriendo dentro del propio corpus del mod,
  no en el log de auditoría.

**Veredicto:** conservar `fallo DOCUMENTACION 19-06-2026.md` completo.
No es duplicado ni superset de ningún otro archivo del corpus — es un
documento de síntesis/auditoría independiente, con valor propio: narra
el incidente operativo "EL MOD NO SE TOCA HASTA TERMINAR LA
DOCUMENTACION" (con evidencia de ambas partes) y documenta con detalle
no replicado en ningún otro archivo el desperfecto real de `v5.md`.

**3.4 queda así, completamente CERRADA:** los 4 ítems con veredicto de
conservación cerrado y verificado (`SESION TRUNCADA`, `fallo sesiones
transcript 16-06-2026`, `fallo sesiones 16-06-2026`, `fallo
DOCUMENTACION 19-06-2026`) — no queda ningún pendiente de esta
sección.

### 2.10 — CERRADA EN v25: familia `FUENTE_DE_VERDAD_IRAM_2026-07-07` completa (11 archivos, no 1 suelto como se creía)

**Corrección de alcance:** la nota de continuidad heredada de v23
identificaba solo "el archivo suelto `FUENTE_DE_VERDAD_IRAM_2026-07-07
2.md`, nunca revisado desde que se priorizó TECHNICAL_WIKI en v9". Al
listar el corpus real se encontró que la familia completa tiene **11
archivos**: `base` (sin sufijo), `_2`, `_3`, `_4`, `_5`, `_6`, `_7`,
`_8`, `_9`, `_10`, `_11`. Ninguno era un simple "suelto" — toda la
familia estaba sin auditar.

**Inventario (tamaño/hash, sin duplicados exactos entre los 11):**

```
base   28.834 bytes  (175 líneas)  hash ab05831a...
_2     39.942 bytes  (263 líneas)  hash 474f8cfa...
_3     53.150 bytes  (334 líneas)  hash c54e45c9...
_4     48.371 bytes  (316 líneas)  hash 88d1343d...
_5     55.236 bytes  (338 líneas)  hash 714d1545...
_6     70.067 bytes  (396 líneas)  hash c56a3d1c...
_7     81.265 bytes  (444 líneas)  hash c2675cc0...
_8     90.645 bytes  (490 líneas)  hash 9a0c414d...
_9    109.404 bytes  (585 líneas)  hash e797f0a4...
_10   118.816 bytes  (644 líneas)  hash b23cd740...
_11   124.424 bytes  (678 líneas)  hash 34c0e373...
```

El orden por sufijo de nombre NO es monótono en tamaño (`_3` > `_4` en
bytes) — primera señal de alarma, mismo tipo de trampa que 2.4.c.

**HALLAZGO PRINCIPAL — el sufijo de archivo no siempre es la versión
real.** Cada archivo declara internamente su "VERSIÓN _N" real en su
banner, y esa numeración no siempre coincide con el sufijo del nombre
de archivo en disco. Confirmado por texto explícito dentro de los
propios documentos (`_5`, `_6`, `_7` incluyen la frase "nombrada
correctamente según la cadena real de versiones, no según el sufijo de
archivo") y **verificado de forma independiente por diff**, no
aceptado solo por la declaración del documento (mismo criterio que el
aviso de integridad documental de v18):

- **Versión interna "_3" real → dos archivos en disco: nombre `_3`
  (c54e45c9) y nombre `_4` (88d1343d).** Diff: 0 líneas agregadas, 18
  líneas removidas en un único bloque contiguo — falta completa la
  sección "## 12. PROCESO DE LAS 4 CHARLAS QUE PRODUJERON EL CIERRE DEL
  PAQUETE A". El propio contenido de esa sección explica el motivo: la
  "charla_3" que la redactó "corta justo cuando se iba a redactar el
  contenido final de esas secciones". Conclusión: el archivo con
  nombre de disco "_4" es un **checkpoint intermedio truncado** de la
  misma versión real _3 (guardado antes de terminar §12); el archivo
  con nombre de disco "_3" es el guardado posterior y completo de esa
  misma versión. El sufijo de archivo quedó invertido respecto al
  contenido real. Sin pérdida real — mismo patrón de checkpoints
  intra-sesión que 3.6.octies.
- **Versión interna "_6" real → dos archivos en disco: nombre `_6`
  (c56a3d1c) y nombre `_7` (c2675cc0).** Acá el sufijo SÍ coincide con
  el orden real: diff de 50 líneas agregadas, solo 2 removidas. Las 2
  líneas removidas no son pérdida: una es actualización de una fila de
  tabla de estado ("Parcialmente cerrado" → estado más resuelto, con
  nueva referencia a §13), la otra es la nota de cierre de documento
  que se reemplaza por la vigente. Mismo patrón que 2.4.c/3.6.bis:
  actualización de estado, no pérdida.

**Verificación de los tramos "simples" de la cadena:**
- `base → _2`: 0 líneas removidas en el diff — `_2` es superset
  limpio, solo agrega.
- `_5 → _6(real) → _8 → _9 → _10 → _11`: progresión de tamaño
  estrictamente creciente. Se comparó el índice de secciones (`##`) de
  `_9` y `_11`: ambos comparten exactamente la misma estructura de §0
  a §15 con líneas de inicio crecientes en cada sección — consistente
  con acumulación pura (append-only, regla DR-42 declarada por el
  propio documento), sin reestructuración de fondo.
- `_10` agrega §17 (árbol definitivo de documentación como tarea
  prioritaria — duplicación real detectada de `SESSION_LOG_REPLANTEO_*`
  en el zip: 15 copias organizadas + 13 sueltas en raíz + 544 en
  `_CUARENTENA_DUPLICADOS`, destino sin decidir).
- `_11` agrega §18 (dos precisiones del operador sobre §17: el árbol
  debe ser legible para instancias de IA simples/tareas cortas; costo
  real de un día de trabajo perdido por errores de servicio de
  Anthropic del 6–7/07, dato no registrado antes en ningún documento
  persistente).

**Veredicto: conservar los 11 archivos completos, sin descartes.**
Cadena real de versión (por contenido, no por sufijo de nombre):

```
base(0) → _2 → _3[real: "_4" truncado + "_3" completo] → _5
  → _6[real: "_6" + "_7", éste sí en orden con el nombre]
  → _8 → _9 → _10 → _11
```

Contenido de valor propio, no replicado con este detalle en ningún
otro archivo del corpus: el "Paquete A/B/C/D/E/F" del proyecto y su
cierre progresivo, el cambio de principio "más que"→"tanto como"
(documentado en §12, visible solo en el guardado completo de "_3"), el
hallazgo de duplicación física de `SESSION_LOG_REPLANTEO_*` en el zip
(§17), y el registro de incidentes de fuga de continuidad entre
sesiones (§2, §16, §18).

**Recordatorio metodológico nuevo de esta sesión (añadir a la lista de
"ojo con" general del proyecto):** dentro de una misma familia de
versiones, el sufijo numérico del nombre de archivo puede estar
directamente invertido o desalineado respecto a la versión real
declarada dentro del documento. No asumir nunca que sufijo mayor =
contenido más nuevo/completo. Verificar siempre la autodeclaración de
versión interna (si existe) y confirmarla por diff antes de ordenar la
cadena — la advertencia en texto del propio documento no sustituye la
verificación por diff.

**⚠️ NOTA DE RECONCILIACIÓN — ESTA SECCIÓN (2.10) CONTRADICE A 2.2, UNA
SECCIÓN MUCHO MÁS VIEJA DEL MISMO LOG, SOBRE LA MISMA FAMILIA DE
ARCHIVOS. No se resuelve unilateralmente acá — se deja señalado
explícitamente, tal como exige el aviso de integridad documental de
v18 (no dar por buena una conclusión sin verificación, y no ocultar una
contradicción real dentro del propio historial de auditoría).
Discrepancias concretas entre 2.2 (sesión vieja, sin fecha de versión
de log identificada, previa a la numeración v-actual) y 2.10 (esta
sesión, v25):**
- **Conteo:** 2.2 dice "12 versiones". 2.10 encontró **11 archivos
  físicos en disco** en el corpus de 274 (`base`, `_2` a `_11`). No se
  identificó un 12º archivo de esta familia en esta sesión — puede que
  2.2 contara mal, contara una versión que ya no está en este corpus de
  274, o contara `_4` y `_3` como si fueran 2 versiones reales distintas
  en vez de 2 guardados de la misma versión "_3" (ver hallazgo de
  2.10). **No verificado cuál es la explicación correcta — pendiente.**
- **Relación entre versiones:** 2.2 afirma que la versión corta (`base`,
  28.8KB) es **prefijo textual EXACTO** de `_11` (124KB) — es decir, un
  superset lineal limpio de punta a punta. 2.10 no verificó ese
  substring exacto extremo a extremo (base contra _11 directamente),
  solo verificó tramos consecutivos — y encontró que la cadena real
  tiene 2 pares de checkpoints con sufijo de archivo desalineado
  respecto a la versión interna real (`_3`/`_4` y `_6`/`_7`), lo cual es
  compatible con que el contenido final siga siendo superset de todo lo
  anterior, pero **no fue confirmado explícitamente en esta sesión que
  `base` sea substring exacto de `_11`** de punta a punta.
- **Lo que si coincide:** ambas secciones coinciden en el veredicto
  final de fondo — conservar toda la familia completa, sin descartar
  ninguna versión, por ser una cadena append-only con valor de
  trazabilidad histórica (criterio de v8). La discrepancia es de
  detalle (conteo exacto y método de verificación), no de la decisión
  de qué conservar.
- **Tarea pendiente para la próxima sesión:** releer 2.2 contra el
  corpus real de 274 para decidir cuál de las dos secciones tiene la
  cuenta correcta (12 vs 11), y si hace falta, verificar por substring
  exacto `base` vs `_11` de punta a punta para confirmar o refutar la
  afirmación de 2.2. No cambia el veredicto de conservar todo, pero sí
  es una inconsistencia de detalle que el log no debería arrastrar sin
  resolver.

### 2.11 — CERRADA EN v25: sección 3.9 completa (los 2 sueltos reales, sin contar `IRAM_SUPERBACKUP_v2_1.md` ya resuelto en 2.9.a)

**Archivos:** `IRAM_Historial_Unificado_v2.md` (957 KB, 15.788 líneas,
hash 1c99ab42...) e `IRAM_historial_unificado_2026-06-12.md` (3,79 MB,
65.375 líneas, hash 316dc20f...). Hashes distintos, sin duplicado
exacto. Diferencia de tamaño ~4x — no se asumió superset por tamaño
(trampa 2.4.c), se verificó por contenido.

**No son versión/bifurcación de la misma cadena — son dos productos de
naturaleza distinta**, pese al nombre casi idéntico:
- **`v2`** (generado 19/05): índice-resumen ejecutivo organizado por
  **Agente** (Diseñador 1, Agente Principal, Agente 3/4/5), 135
  sesiones, rango 09/04→16/05/2026. Cada sesión ocupa 2-4 líneas (tipo
  "🐛 BUG DOCUMENTADO / ✅ FIX APLICADO").
- **`2026-06-12`**: extracción casi cruda de mensajes reales,
  organizada por **cuenta de Claude** (CLAUDE_1 a CLAUDE_5), 441
  conversaciones, 7.345 mensajes post-dedup (419 duplicados
  removidos), rango 22/10/2025→10/06/2026 — casi un mes más de
  cobertura que `v2`.

**Verificación de solapamiento real** (no asumida por el ratio global
`quick_ratio` de 0.40, que por sí solo no prueba nada — mismo
principio que 2.7/3.6.quindecies): se cruzaron los títulos de sesión
de ambos índices. 82 de 117 títulos de `v2` reaparecen en
`2026-06-12`. Al comparar el contenido real de una sesión compartida
("Errores de scope en decisiones de Imperator Roma 2.0", 29/04), se
confirmó que **`v2` la resume en 2 líneas** mientras **`2026-06-12` la
reproduce con timestamps, herramientas usadas (str_replace, view,
bash, present_files) y fragmentos de mensaje real con conteo de
caracteres**. No hay redundancia textual — son dos niveles de
granularidad distintos sobre el mismo material fuente subyacente.
Confirmado también por rango de fechas: `v2` termina el 16/05, `2026-
06-12` llega hasta el 10/06 — casi un mes más de cobertura, no
solo más detalle.

**Veredicto: conservar ambos, sin descarte.** No hay pérdida de
contenido porque no hay superset textual — `v2` no es un resumen *de*
`2026-06-12` (es anterior y cubre menos sesiones), y `2026-06-12` no
reemplaza a `v2` (organiza por criterio distinto — cuenta vs. agente —
y tiene otro nivel de detalle). Son complementarios: `v2` da la vista
ejecutiva por agente/fase del proyecto, `2026-06-12` da la traza cruda
por cuenta con deduplicación de mensajes.

**Con esto, la sección 3.9 queda completamente CERRADA** — sus 3
archivos verificados: `IRAM_SUPERBACKUP_v2_1.md` (descartado en v23,
ver 2.9.a), `IRAM_Historial_Unificado_v2.md` (conservado, este
addon), `IRAM_historial_unificado_2026-06-12.md` (conservado, este
addon).

## 3. PENDIENTE — NO REVISADO TODAVÍA (esto es lo que sigue)

Archivos ya identificados en el set de 274 filtrados (sin `\game\`) que
**todavía no se abrieron ni se compararon**.

### 3.2 — Familia "gap" (sesión v4.1-4.3) — **CERRADA EN v20, ver 2.6**
Movida a la sección 2 (conclusiones cerradas). Los 7 archivos se
conservan completos, sin descartes. Ver 2.6 para el detalle completo.

### 3.3 — Charlas sueltas (charla_7 a charla_12) — **CERRADA EN v21, ver 2.7**
Movida a la sección 2 (conclusiones cerradas). Las 6 charlas se
conservan completas, sin descartes. Ver 2.7 para el detalle completo.

### 3.4 — Sesiones "falladas"/"truncadas" sueltas — **CERRADA POR COMPLETO EN v24 (ver 2.9 y 2.9.c)**
Movida en su totalidad a la sección 2 (conclusiones cerradas). Detalle:
- `SESION TRUNCADA.md` (234348 bytes) — **CERRADA.** Contiene íntegro a
  `IRAM_SUPERBACKUP_v2_1.md` (que se descarta por redundante) + 216
  líneas propias. Conservar. Ver 2.9.a.
- `fallo sesiones transcript 16-06-2026.md` (730530 bytes) — **CERRADA.**
  Transcript crudo que genera el `s19` ya cerrado en 3.6.sedecies.
  Conservar. Ver 2.9.b.
- `fallo sesiones 16-06-2026.md` (328442 bytes) — **CERRADA.** 95% de
  líneas compartidas con el transcript de arriba, pero con reescritura
  propia (no es substring exacto). Conservar. Ver 2.9.b.
- `fallo DOCUMENTACION 19-06-2026.md` (67718 bytes) — **CERRADA EN v24.**
  Verificado contra el corpus grande (no solo contra sus "hermanos" de
  nombre): todos los archivos que menciona/analiza
  (`IRAM_C1_final.md`, `WIKI_DOCUMENTACION_v2.md`,
  `SESSION_LOG_ANALISIS_C1_2026-06-18` v1 a v5, `spec_c_zip_history.py`)
  existen en el corpus real de 274. Se confirmó por diff directo (no
  solo por lo que narra el propio archivo) su hallazgo central: `v5.md`
  tiene el encabezado roto — promete "DC-11 + H-PROC1" pero el cuerpo
  es copia literal de `v4.md` (única diferencia: 5 líneas de
  encabezado). Los `.json` de output de las specs A/B/C que menciona
  NO están en el corpus (coherente, productos efímeros de ejecución).
  Conservar completo — documento de síntesis independiente, sin
  duplicado ni superset con nada más del corpus. Ver 2.9.c para el
  detalle completo.
- Las 3 variantes de `failed*` que ya se revisaron (ver 2.1) también
  están en esta carpeta con nombres saneados:
  `failed 3__513ec7d6.md`, `failed (2)__cc393de0.md` (aparece como
  `failed _3__...` por el saneo de paréntesis, cuidado con esto),
  `failed__1e77a076.md` — no hace falta releerlas, ya están cerradas.

**Con esto, la sección 3.4 queda completamente cerrada — no queda
ningún ítem pendiente.**

### 3.5 — Volcados de chat en crudo (NO leer entero, solo consultar puntualmente si hace falta buscar algo)
- `conversations__4bff53c0.json` (46.8 MB) — el más grande de todo el
  set.
- `conversations__c5c15d0d.json` (15.9 MB)
- `conversations__214fef87.json` (14.9 MB)
- `claude_1_processed.json` a `claude_5_processed.json` (~1.5–2 MB c/u)
- `reporte_comparacion.json` (2.5 MB) — probablemente metadata de un
  script/comparación anterior, no contenido de proyecto en sí.

### 3.6 — Inventario de 222 archivos sin listar por nombre, agrupados por familia

**Total real 274 − ya nombrados/resueltos 56 (ver 2.x/3.2-3.5/3.6.bis/
3.6.ter/3.9) = 218 sin listar por nombre individual** (los 4 de
`hitos_metodologicos` se suman a los 52 ya resueltos en v5: 3 cerrados
por la cadena WIKI_DOCUMENTACION no se restaban de este número porque
esos 3 ya estaban nombrados explícitamente en la familia de 3.6 debajo;
los 4 de `hitos_metodologicos` tampoco estaban nombrados aparte, así que
el conteo baja de 222 a 218).

**Todavía NO se comparó nada del resto por diff/hash — falta hacer el
trabajo de verificación real de cada familia grande.**

#### Familias grandes (agrupadas por prefijo — candidatas a comparación por lote, TODAS SIN TOCAR AÚN)
- **SESSION_LOG_DOCUMENTACION_*** (22 archivos, ~324 KB) — sufijos `_sNN`
  (s7-s34) y `_CONSOLIDADO_sNN`. Verificar si los `_CONSOLIDADO` absorben
  a los sueltos del mismo rango. Variantes `(1)(2)(3)` = posibles dups
  (recordar: verificar por hash normalizado CRLF, no solo hash crudo).
- **SESSION_LOG_REPLANTEO_*** (19 archivos, ~302 KB) — **RESUELTO EN
  ESTA SESIÓN (v13), ver 3.6.octies.** Fechados 2026-06-19 a 07-05. El
  `(2)` en varios nombres NO era duplicado re-copiado (hipótesis
  original descartada): es parte del nombre real de archivo en la
  carpeta oficial del proyecto. **Conservar los 19 completos** — cero
  duplicados por hash normalizado. Cadena con 2 grupos de checkpoints
  intra-sesión (progresión real, no bifurcación) y hallazgo de 6
  archivos mal clasificados en carpeta de cuarentena del propio
  proyecto sin ser duplicados reales. Sacar de la cola de pendientes de
  3.6.
- **IRAM_C1_*** (18 archivos, ~223 KB) — **RESUELTO EN ESTA SESIÓN
  (v14), ver 3.6.novies.** Se conservan los 18 completos: esqueleto de
  planificación (único), 14 drafts por sección (supersets limpios
  verificados por diff), `completo_s32` (con Sección 4D propia) y
  `final` (reescritura editorial, contenido intacto verificado por
  muestreo). No era superset simple `_final` sobre el resto — cada capa
  aporta algo distinto. Sacar de la cola de pendientes de 3.6.
- **Modulo*_Unidad*_*.md** (16 archivos, ~562 KB) — **RESUELTO Y
  CERRADO EN v15** (alcance ya venía resuelto desde v9, ver sección 0;
  el trabajo de verificación real se hizo recién en v15, ver 3.8).
  Son insumo para Tareas 1 y 2 de la Diplomatura UTN. Nombres: "Que es
  la IA", "Machine Learning", "NLP", "Vision por Computadora", "Ciencia
  de Datos", "Analisis Exploratorio EDA"... **Se conservan los 16
  completos** — grilla Módulo 1–4 × Unidad 1–4 sin huecos, 16 hashes
  SHA-256 distintos entre sí (cero duplicados), título interno de
  Módulo/Unidad coincide con el nombre de archivo en los 16 casos.
  Definir dónde deben vivir en el árbol final del repo sigue abierto
  como tarea organizativa (no de auditoría de contenido) — no bloquea
  cerrar este punto. Sacar de la cola de pendientes de 3.6.
- **README\*.md** (15 archivos) — **RESUELTO EN ESTA SESIÓN, ver 2.5.a.**
  14 con contenido único + 1 duplicado real colapsado. Sacar de la cola
  de pendientes de 3.6.
- **SESSION_LOG_DOCUMENTACION_s*** (13 archivos, ~110 KB) — serie corta
  s22-s34, posible solapamiento con la familia SESSION_LOG_DOCUMENTACION
  de arriba (¿misma serie partida en dos por heurística de agrupamiento,
  o series distintas?). Sin tocar.
- **SESSION_LOG_ANALISIS_C1_2026-06-18_*** (6 archivos, ~150 KB) —
  **RESUELTO EN ESTA SESIÓN, ver 3.6.quinquies.** Cadena única
  confirmada v1(sin sufijo)<v2<v2(2)<v3<v4<v5 — **conservar los 6
  completos** (superset confirmado en cada salto, ninguno descartado
  bajo el criterio corregido). Sacar de la cola de pendientes de 3.6.
- **PROMPT_DOCUMENTACION_IRAM_v1_*.md** (5, ~117 KB) — v1_4,v1_5,v1_7,v1_9
  (2 copias). — **RESUELTO EN ESTA SESIÓN (v16), ver 3.6.terdecies.**
  No era lineal simple (confirmado el caso 2.4.c): 2 saltos con
  reescritura real de fondo (v1_4→v1_5 y v1_5→v1_7, ambos sobre la
  regla del modelo de cuentas paralelas/secuenciales) + 1 salto de
  reestructuración real (v1_7→v1_9, bifurca en productos C1/C2) + 1
  superset limpio (v1_9(3)→v1_9(4), ya verificado antes). **Conservar
  los 5 completos.** Sacar de la cola de pendientes de 3.6.
- **IRAM_hitos_metodologicos_*.md** (4, ~170 KB) — **RESUELTO, ver
  3.6.ter.** No era 1 cadena de 4 sino cadena v5<v6<v7 + 1 archivo
  independiente (el "sin sufijo" 06-12, b44210ab, es evidencia cruda de
  script, no versión de la narrativa) — **los 4 se rescatan completos**
  (CORREGIDO EN v8: antes decía solo v7 + b44210ab). Sacar de la cola de
  pendientes de 3.6.
- **INDICE\*.md** (4 archivos) — **RESUELTO EN ESTA SESIÓN, ver 2.5.b.**
  3 versiones reales con contenido distinto (evolución real, no
  duplicado) + 1 duplicado exacto colapsado. Sacar de la cola.
- **IRAM_TECHNICAL_WIKI_ACTIVE_v3_*.md** (3, ~449 KB) y
  **IRAM_TECHNICAL_WIKI_ARCHIVE_v3_*.md** (3, ~347 KB) — **RESUELTO EN
  ESTA SESIÓN (v9), ver 3.6.sexies.** Confirmado: no son dos series
  paralelas independientes sino un sistema de vasos comunicantes real
  entre ACTIVE y ARCHIVE (contenido movido de uno a otro). **Conservar
  los 6 completos, cerrado con salvedad** — 3 bloques de contenido
  puntual sin correlato confirmado en el set. Sacar de la cola de
  pendientes de 3.6.
- **SESION\*.md** (3, ~161 KB, incl. "SESION FALLADA 1/2/3.md") — posible
  relación con 3.4 (sesiones falladas/truncadas), revisar junto. Sin
  tocar.
- **IRAM_analisis_cuantitativo_\*.md** (3, ~40 KB) — sin sufijo, v2, v3.
  — **RESUELTO EN ESTA SESIÓN (v16), ver 3.6.undecies.** Cadena
  confirmada, pero base→v2 NO es superset simple (v2 revierte el
  veredicto de la base sobre cuentas paralelas/secuenciales); v2→v3 sí
  es superset limpio (agrega Bloque 3 completo). **Conservar los 3
  completos.** Sacar de la cola de pendientes de 3.6.
- **IRAM_PROMPT_MAESTRO_v\*.md** (3, ~46 KB) + **PROMPT_MAESTRO_v\*.md**
  (2, ~50 KB) — prefijos distintos (con IRAM_ y sin). **No asumir que son
  la misma serie**, confirmar si son prompts distintos. Sin tocar.
- **WIKI_DOCUMENTACION_v1/v2/v3.md** (3, ~37 KB) — candidato a cadena
  incremental simple. Nota: v3 es citado dentro de uno de los INDICE ya
  revisados (2.5.b) como "wiki de wikis", contexto histórico de la
  documentación — dato adicional a favor de que sea cadena real. Sin
  tocar.
- **IRAM_SESSION_LOG_\*.md** (3, ~27 KB) + `IRAM_SESSION_LOG_v5_6_...md`
  (aparte) — **RESUELTO EN ESTA SESIÓN (v16), ver 3.6.duodecies.**
  Independientes de la serie TECHNICAL_WIKI — son 4 logs de sesión de
  desarrollo del mod, cronológicamente encadenados por "Continuación
  de:", no versiones del mismo documento. **Conservar los 4 completos.**
  Sacar de la cola de pendientes de 3.6.

#### Grupos chicos / pares (2 archivos cada uno) — TODOS RESUELTOS
(actualizado en v19; lista original conservada tachada para trazabilidad)
- `sesion cortada.md` + `transcripcion de SESSION_LOG_CONSOLIDADO_2026-06-1*`
  (`__1f5727a2` + `__56abcedb`) + `SESSION_LOG_CONSOLIDADO_2026-06-18`
  (4° archivo hallado en la misma búsqueda) — **RESUELTO EN ESTA SESIÓN
  (v19), ver 3.6.quindecies.** Los 4 son independientes entre sí:
  `sesion cortada.md` es un draft del paper metodológico (tema
  distinto); las 2 transcripciones son 2 sesiones de chat separadas y
  secuenciales, no dos mitades de una sesión cortada; el 4° es el
  documento final de esa tarea. **Conservar los 4.** Sacar de la cola.
- `critica a la critica.md` + `critica 1.md` (+ `IRAM_critica_rigurosa`,
  incorporado al mismo grupo) — **RESUELTO EN v18, ver 3.6.quaterdecies
  punto 1.** Bifurcación real (ratio 0.45) + documento final idéntico
  al fragmento embebido en `critica 1`. **Conservar los 3.** Sacar de
  la cola.
- `PASO_0_grupos_divergentes_checklist.md` + `... 2.md` — **RESUELTO EN
  v18, ver 3.6.quaterdecies punto 2.** Superset exacto por substring,
  +9740 caracteres nuevos (DR-22, DR-23). **Conservar ambos.** Sacar de
  la cola.
- `IRAM_paper_metodologia_v1_0.md` + `IRAM_paper_metodologia_v1_0(1).md`
  — **RESUELTO, ver 2.5.c. Dos borradores distintos, rescatar ambos.
  Sacar de la cola.**
- `bloque3_analysis.py` + `bloque3_analysis_v2.py` — **RESUELTO EN v18,
  ver 3.6.quaterdecies punto 3.** Reescritura metodológica confirmada
  por el propio docstring y el diff completo del código, no checkpoint
  simple. **Conservar ambos.** Sacar de la cola.
- `spec_c_zip_history.py` + `spec_c_zip_history (3).py` — **RESUELTO EN
  v18, ver 3.6.quaterdecies punto 4.** Único cambio real: fix del
  BUG-C1 en el regex, confirmado línea por línea. **Conservar ambos.**
  Sacar de la cola.
- `IRAM_Prompt_Etapa1_Limpieza.md` + `IRAM_Prompt_Etapa2_Unificacion.md`
  — **RESUELTO EN v18, ver 3.6.quaterdecies punto 5.** Documentos
  hermanos secuenciales (Etapa 1 → Etapa 2), ratio 0.32, sin relación de
  substring. **Conservar ambos, no compiten.** Sacar de la cola.
- `IRAM_skill_desarrollo_ia_v2_0.md` +
  `IRAM_skill_desarrollo_ia_v2_0 (3).md` — **RESUELTO, ver 2.5.d. Dos
  redacciones distintas, rescatar ambas. Sacar de la cola.**
- `Consigna_1.md` + `Consigna_2.md` + `Consigna.md` — **RESUELTO EN v18,
  ver 3.6.quaterdecies punto 6.** 3 piezas curriculares distintas de la
  Diplomatura UTN (presentación general + Entrega 1 + Entrega 2), sin
  solapamiento (ratios 0.12–0.27). **Conservar los 3.** Sacar de la
  cola.
- `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` + `2026-07-07.md` —
  **RESUELTO EN v16, ver 3.6.decies.** No son superset ni duplicado —
  son 2 sesiones consecutivas y complementarias (07-07 se declara a sí
  mismo continuación directa de 07-06 y ejecuta su pendiente explícito).
  **Conservar ambos.** Sacar de la cola.

**Con esto, no queda ningún grupo chico/par de 3.6 sin resolver.**

#### Sueltos, un archivo cada uno (revisión individual rápida)

Scripts de Python sueltos (herramientas de auditoría de sesiones
anteriores, útiles para metodología previa, no necesariamente "contenido
a rescatar" documental) — **sin tocar**:
`generate_iram_docs (2).py`, `process_iram_v2 (2).py`,
`comparar_copias_iram.py`, `spec_a_authorship.py`,
`spec_b_democratizacion (2).py`, `build_mods.py`, `verificar_iram.py`

Archivos de datos/config del mod (.txt, fuera de `\game\`, probablemente
propios del mod — confirmar) — **sin tocar**:
`exodus_decisions.txt`, `exodus_on_action.txt`,
`exodus_scripted_effects.txt`, `exodus_units.txt`, `exodus_events.txt`,
`tgl_decisions.txt`, `tlv_decisions.txt`, `tlv_events.txt`

Documentos de metodología/plantillas (probablemente ya subsumidos en
FUENTE_DE_VERDAD_11 o HISTORIA_COMPLETA v1_2, no confirmado) — **sin
tocar**:
`TEMPLATES_DOCUMENTACION_v1.md`, `METODOLOGIA_DOCUMENTACION_v1.md`,
`PROMPT_REGLAS_DOCUMENTACION_v2.md`,
`IRAM_SKILL_desarrollo_con_IA_v1_0 (2).md` — **nota nueva de esta
sesión:** este último es mencionado por nombre dentro de
`IRAM_skill_desarrollo_ia_v2_0.md` (4d388c49, ver 2.5.d) como
"Reemplaza: IRAM_SKILL_desarrollo_con_IA_v1_0.md (borrador del paper —
audiencia distinta)" — es decir, hay indicio textual directo de que
este archivo es un borrador anterior superado, pero **falta confirmar
por diff igual**, no asumir solo por la mención.

Otros sueltos sin familia clara — revisar uno por uno — **sin tocar**:
`CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`, `reporte_resumen.txt`,
`FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md` (⚠️ **resolver primero**: nombre
casi idéntico a la familia ya cerrada en 2.2, pero con un "2" suelto al
final, distinto al patrón `_2` de esa familia — verificar si es la misma
familia con nombre corrupto o algo distinto; si es la misma, ya sabemos
el veredicto: subsumida por `_11`), `optimizador_provincial_backup_v4.md`,
`imperator_optimizer_v4.html`, `colisiones_verificadas_2026-07-06.txt`,
`Qwen_markdown_20260705_q4xkzeqjf (2).md`,
`backup_slave_distributor_v2(1).md`, `IRAM_critica_rigurosa_2026-06-12.md`,
`INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` (posible fuente del bloque
"INVENTARIO COMPLETO DEL MATERIAL DE ARCHIVO" citado en 2.4.c — revisar
junto con esa familia), `RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20 2.md`,
`CORRECCIONES_SESION_2026-06-12.md`, `memoria_claude_volcado.md`,
`volcado_memoria (2).md`, `LOG_REORGANIZACION_2026-07-05.md`,
`IRAM_INSTRUCCIONES_HUMANO_2026-05-27_20-55.md`,
`PROMPT_CONTINUACION_2026-07-07_8.md`,
`deepseek_markdown_20260705_98aa15 (2).md`, `sigue log.md`,
`instruccion_prueba_fuga_memoria.md`,
`resultado_prueba_fuga_memoria.md`,
`---------INSTRUCCIONES-------.txt`,
`-----------------LEER---------------------.txt`, `conflictos.csv`

#### 3.6.bis — CERRADO EN ESTA SESIÓN: cadena WIKI_DOCUMENTACION (v1/v2/v3)

Primera de las 5 cadenas incrementales candidatas del punto 3 de
prioridad. **Resultado: cadena confirmada y cerrada, sin necesidad de
revisarla de nuevo.**

Archivos (del set de 274, subcarpeta `candidatos_valiosos/`):
- `WIKI_DOCUMENTACION_v1__d491f4ac.md` (10781 bytes)
- `WIKI_DOCUMENTACION_v2__db0617fb.md` (12558 bytes)
- `WIKI_DOCUMENTACION_v3__2436e4de.md` (14228 bytes)

**Método:** normalización CRLF→LF antes de comparar (regla de 2.5),
luego diff línea a línea completo entre v1↔v2 y v2↔v3. NO se asumió que
v3 (nombre/fecha más alta) fuera superset sin verificar — se aplicó el
mismo cuidado que en 2.4.c.

**v1 → v2:** no es substring exacto (hay reescritura de contenido, no
solo append), pero el diff completo confirma que **todas** las líneas
que desaparecen de v1 son: (a) actualizaciones de estado en tablas
(pendiente→completado), (b) el header/pie de página con metadata de
versión, o (c) contenido reescrito *expandido en el mismo lugar*
(el Marco Conceptual pasa de 12 a 13 clusters, con el texto de los 12
originales preservado y ampliado). **Ninguna pérdida de contenido
semántico** → v2 es superset funcional confirmado de v1, aunque no
textualmente idéntico.

**v2 → v3:** diff mucho más limpio, solo 3 hunks:
1. Header (versión/fecha).
2. El bloque "PRINCIPIO CENTRAL DEL PAPER" se reemplaza por una
   corrección puntual (decisión DC-06/DR-22: la wiki tenía desactualizado
   ese resumen desde el 17/06 pese a que la corrección ya estaba aplicada
   en el resto del documento — caso real de lo que el propio v3 describe
   como "discrepancia de posición, no de contenido").
3. Pie de página con cambio a modo de changelog.
Todo el resto del cuerpo (tablas de estado, secuencia de trabajo, hitos,
fases, Marco Conceptual de 13 clusters, etc.) queda **idéntico byte a
byte** entre v2 y v3. → v3 es superset estricto de v2 + 1 corrección.

**Conclusión de la cadena:** v1 < v2 < v3 confirmado por contenido real
(no por nombre/fecha). Ambos saltos verificados independientemente, sin
asumir transitividad automática.

**Decisión CORREGIDA EN v8** (originalmente decía "solo conservar v3,
v1/v2 son descartables" — ver corrección de criterio al inicio del
log): **conservar las 3 versiones completas** — v1, v2 y v3. La relación
de superset sigue confirmada (v3 no pierde nada de v1/v2), pero cada
versión es un estado histórico real (incluye el cambio de "PRINCIPIO
CENTRAL DEL PAPER" entre v2 y v3) y se conserva como trazabilidad, no se
purga.

---

#### 3.6.ter — CERRADO EN ESTA SESIÓN: cadena IRAM_hitos_metodologicos

Segunda de las 5 cadenas incrementales candidatas del punto 3 de
prioridad. **Resultado: NO era una sola cadena de 4 pasos como suponía
v5 — son 2 productos distintos.** Cerrado, sin necesidad de revisar de
nuevo.

Archivos (del set de 274, subcarpeta `candidatos_valiosos/`), con ruta
original confirmada contra `_indice_copiados.csv`:
- `IRAM_hitos_metodologicos_2026-06-10_v5__86dcd0dc.md` (35475 B)
- `IRAM_hitos_metodologicos_2026-06-11_v6 (2)__3a7ae943.md` (43143 B)
- `IRAM_hitos_metodologicos_2026-06-12_v7 (2)__ea1f0ebc.md` (43402 B)
- `IRAM_hitos_metodologicos_2026-06-12__b44210ab.md` (52388 B) — el "sin
  sufijo de versión" que v5 marcaba como ambiguo.

**Método:** normalización CRLF→LF antes de comparar (regla de 2.5),
luego diff línea a línea completo v5↔v6 y v6↔v7. Antes de comparar el
cuarto archivo contra la cadena, se leyó su contenido completo primero
(no se asumió por nombre/fecha que fuera un paso más de la misma serie,
tal como pedía la advertencia explícita de v5 sobre este archivo).

**Hallazgo clave — el archivo sin sufijo NO es parte de la cadena
narrativa:** `IRAM_hitos_metodologicos_2026-06-12__b44210ab.md`
resultó ser un producto de **naturaleza distinta**: la salida cruda de
un script de detección de hitos por keyword-matching sobre los 5
`conversations.json` (checklist + tabla completa de evidencia
fecha/cuenta/conversación por hito, cientos de filas). Comparte fecha
(2026-06-12) y tema con v7 por casualidad de timing, pero **no es un
borrador ni una versión de la cadena v5/v6/v7** — es la materia prima
que alimentó las decisiones que sí quedaron incorporadas en la
narrativa v6/v7, con un nivel de detalle (fila por fila de
conversación) que la narrativa nunca reproduce. Confirmado por grep
puntual: contenido tabular de `b44210ab` no aparece en v7. **Mismo tipo
de trampa que 2.5.c/2.5.d (coincidencia de nombre/versión no implica
misma familia), pero en la dirección opuesta: acá la fecha coincidía y
aun así era independiente.**

**Cadena narrativa real — v5 → v6 → v7:**
- **v5→v6:** no substring exacto (hay reescritura), pero diff completo
  confirma que todas las líneas que desaparecen de v5 son (a)
  actualizaciones de estado pendiente→resuelto en las mismas entradas
  de hito (ej. "primera_wiki" pasa de "⚠️ REQUIERE DEFINICIÓN" a
  "✅ RESUELTO"), o (b) contenido reemplazado por una sección expandida
  en el mismo lugar (ej. el ítem abierto "qué reglas del PROMPT_MAESTRO
  nacieron de un bug" desaparece de la lista de pendientes de v5 porque
  v6 lo resuelve más arriba con el bloque nuevo "Auditoría formal v4 —
  confirmada"). Se verificó explícitamente esa línea puntual para no
  asumir. **Ninguna pérdida de contenido semántico → v6 es superset
  funcional de v5.**
- **v6→v7:** diff limpio, header/pie actualizado + 2 líneas que
  desaparecen de la lista "Hitos pendientes de verificación" porque ya
  habían sido resueltas en v6 (verificado cruzando contra el propio
  texto de v6, no asumido). El cuerpo central completo (líneas 9 a 580
  del archivo normalizado) es **idéntico byte a byte** entre v6 y v7.
  **v7 es superset estricto de v6.**

**Conclusión de la cadena:** v5 < v6 < v7 confirmado por contenido real.
Mismo patrón que 3.6.bis (WIKI_DOCUMENTACION): reescritura real en el
primer salto, superset estricto en el segundo.

**Decisión CORREGIDA EN v8** (originalmente decía "conservar solo v7 +
b44210ab aparte, v5/v6 descartables" — ver corrección de criterio al
inicio del log): **conservar los 4 archivos completos:**
1. `IRAM_hitos_metodologicos_2026-06-10_v5__86dcd0dc.md`
2. `IRAM_hitos_metodologicos_2026-06-11_v6 (2)__3a7ae943.md`
3. `IRAM_hitos_metodologicos_2026-06-12_v7 (2)__ea1f0ebc.md`
4. `IRAM_hitos_metodologicos_2026-06-12__b44210ab.md` — este seguía
   siempre a rescatar aparte (nunca fue "redundante", es un artefacto de
   naturaleza distinta, evidencia cruda, no versión de la narrativa).
La cadena narrativa v5<v6<v7 sigue confirmada por superset, pero bajo el
nuevo criterio ninguna versión de la cadena se descarta — las 3 se
conservan como trazabilidad histórica real.

---

---

#### 3.6.quater — CERRADO EN ESTA SESIÓN: cadena PROMPT_MAESTRO

Tercera de las 5 cadenas incrementales candidatas del punto 3 de
prioridad. **Confirmado: son 2 familias distintas**, tal como advertía
la prioridad sugerida de v6 — no una sola cadena de 5 archivos.

Archivos (del set de 274), con ruta original confirmada contra
`_indice_copiados.csv`:
- `PROMPT_MAESTRO_v1_6__38fb155d.md` (23304 B) — cuarentena, subcarpeta
  "fuentes de documentacion (subcopia anidada)".
- `PROMPT_MAESTRO_v1_8_1__d596049c.md` (27395 B) — cuarentena, subcarpeta
  "07_fuentes_documentacion_duplicados_2026-07-08".
- `IRAM_PROMPT_MAESTRO_v3_8_2026-05-27_20-55__9dd8c8be.md` (15218 B) —
  repo activo, `2_DOCUMENTACION/04_corpus_A_mod_docs`.
- `IRAM_PROMPT_MAESTRO_v3_9_2026-05-30_03-14__7e8fb490.md` (15222 B) —
  repo activo, misma carpeta que v3_8.
- `IRAM_PROMPT_MAESTRO_v5_2_2026-06-06 _2__b3424a78.md` (17127 B) —
  cuarentena, subcarpeta "07_fuentes_documentacion_duplicados_2026-07-08".

**Cómo se confirmó que son dos familias, no una:** lectura del inicio de
los 5 archivos. Título distinto ("PROMPT — SISTEMA DE DOCUMENTACIÓN
IRAM" vs "PROMPT MAESTRO — IRAM"), esquema de versión independiente
(v1.6→v1.8 fechado 12/06 vs v3.8→v5.2 fechado 27/05→06/06 — es decir,
por fecha la serie IRAM_PROMPT_MAESTRO es *anterior* a PROMPT_MAESTRO
pese a tener números de versión más altos: son dos numeraciones
independientes, no continuación una de otra), y solo IRAM_PROMPT_MAESTRO
tiene la referencia fija a "IRAM_INSTRUCCIONES_HUMANO (Sección 22 del
TECHNICAL_WIKI ACTIVE)". Se trataron como 2 cadenas separadas.

**Cadena A — `PROMPT_MAESTRO` (v1.6 → v1.8):**
No es substring exacto (reescritura real). Diff completo línea a línea:
la gran mayoría de lo que "desaparece" de v1.6 es actualización de
estado (ítems marcados "⚠️ a confirmar" que se resuelven y se retiran de
la lista de pendientes en v1.8 — mismo patrón que 3.6.bis/3.6.ter,
verificado puntualmente contra el texto de v1.8, no asumido) o expansión
real en el mismo lugar (v1.8 agrega una Plantilla C2 completa —
construcción del skill operacional — que no existía en v1.6).

**Excepción encontrada — NO se pudo confirmar superset limpio en un
bloque puntual:** el viejo esquema de v1.6 ("skill único de 13 secciones
prescriptivas", un solo entregable) se reestructura de fondo en v1.8
("paper" de 5 secciones + "skill operacional" separado de 6 secciones,
2 entregables). La mayoría de los 13 temas viejos tienen correlato en la
nueva estructura, pero **dos no tienen correlato textual explícito**:
"Cuentas paralelas — cómo gestionar múltiples contextos simultáneos" y
"Herramientas situacionales — WIPs, minilogs: cuándo activarlos y cuándo
no". Puede ser que queden subsumidos de forma genérica en secciones más
amplias del nuevo esquema, pero no se pudo confirmar por texto — a
diferencia de todos los casos anteriores (3.6.bis, 3.6.ter, y el resto
de esta misma cadena), acá la evidencia es mixta, no concluyente.

**Decisión del usuario para este caso puntual:** conservar **ambos**
`PROMPT_MAESTRO_v1_6` y `PROMPT_MAESTRO_v1_8_1` — no tratar v1.8 como
reemplazo limpio de v1.6 dado que no es superset confirmado al 100%.

**Cadena B — `IRAM_PROMPT_MAESTRO` (v3.8 → v3.9 → v5.2):**
Ninguna es substring exacta de la siguiente, pero el diff confirma
cadena de superset real, sin pérdida semántica:
- **v3.8→v3.9:** superset estricto puro. Solo header/fecha, versión del
  mod actualizada (v4.3.7→v4.3.16), y 2 reglas nuevas agregadas (R18,
  R19) — inserción pura, sin ningún delete real de contenido.
- **v3.9→v5.2:** reescritura real (no substring), pero cada delete se
  verificó individualmente: (a) reordenamiento sin pérdida (líneas en
  blanco, bloques movidos), (b) dos notas aclaratorias/históricas de
  detalle menor recortadas (contexto de justificación de reglas RE5/RE6,
  no las reglas en sí — esas siguen intactas), y (c) el bloque más
  sustancial — dos notas "CRÍTICO" inline sobre sintaxis de
  `remove_building_level` y guards obligatorios — se promueve a reglas
  formales numeradas RE1–RE6, con el bloque técnico central (FASE 1/FASE
  2/TERMINOLOGÍA OBLIGATORIA DEL ENGINE) preservado byte a byte.
  **v5.2 es superset funcional confirmado de v3.9.**

**Decisión CORREGIDA EN v8** (originalmente decía "solo conservar v5.2,
v3.8/v3.9 descartables" — ver corrección de criterio al inicio del
log): **conservar las 3 versiones completas** — v3.8, v3.9 y v5.2. La
cadena de superset sigue confirmada, pero cada versión se conserva como
trazabilidad histórica, ninguna se descarta.

**Conclusión de la sesión — 2 familias distintas, no confundir:**
- `PROMPT_MAESTRO`: **conservar ambos** (v1.6 y v1.8) — esta conclusión
  ya estaba bien desde el origen (caso especial, sin superset 100%
  confirmado, nunca se propuso descartar ninguno).
- `IRAM_PROMPT_MAESTRO`: **conservar las 3** (v3.8, v3.9, v5.2) —
  CORREGIDO EN v8, ver arriba.

---

#### 3.6.quinquies — CERRADO EN ESTA SESIÓN: cadena SESSION_LOG_ANALISIS_C1

Cuarta de las cadenas incrementales candidatas del punto 3 de prioridad.
**Resultado: distinto a los 3 casos anteriores — NO había ningún archivo
"intruso" de naturaleza distinta.** Los 6 archivos son una única cadena
secuencial confirmada, cada uno declarándose explícitamente reemplazo
del anterior en su propio encabezado.

Archivos (del set de 274, subcarpeta `candidatos_valiosos/`), con ruta
original confirmada contra `_indice_copiados.csv` (los 6 vienen de la
misma subcarpeta de cuarentena, `fuentes de documentacion (subcopia
anidada)`; nombre real de la familia es `SESSION_LOG_ANALISIS_C1`, no
`ANALISIS_C1` a secas):
- `SESSION_LOG_ANALISIS_C1_2026-06-18__9851dff1.md` (8412 B) — "v1", sin
  sufijo de versión en el nombre.
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v2__811f678f.md` (15295 B)
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v2 (2)__6eccfeaf.md` (20809 B)
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v3__8e4eefe9.md` (24979 B)
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v4__ff7b0e08.md` (42066 B)
- `SESSION_LOG_ANALISIS_C1_2026-06-18_v5__4f16cc13.md` (42413 B)

**Verificación del "sin sufijo" antes de asumir (siguiendo la advertencia
de 3.6.ter):** se leyó completo antes de compararlo. Es un log real de
sesión ("SESSION LOG — Análisis y mejora de IRAM_C1_final.md"), spec
ejecutable con tareas de mejora del paper (A/C/E/F) y estado del mod —
**sí es el primer paso genuino de esta cadena narrativa**, a diferencia
del caso análogo de `hitos_metodologicos` donde el "sin sufijo"
resultó ser un artefacto de naturaleza distinta. Aquí no hubo sorpresa
de ese tipo.

**Método:** normalización CRLF→LF antes de comparar (regla de 2.5),
diff línea a línea completo en cada salto de la cadena (v1↔v2, v2↔v2(2),
v2(2)↔v3, v3↔v4, v4↔v5), sin asumir transitividad automática entre
saltos no adyacentes.

**v1→v2:** v2 declara explícitamente en su propio encabezado
("**Reemplaza:** SESSION_LOG_ANALISIS_C1_2026-06-18.md (v1, sesión 20:08
UTC)") que reemplaza a v1, y es acumulativo por diseño. Agrega DC-05,
DC-06, DC-07 (bloqueo de tareas del paper por autoría, problema de
democratización en WIKI_DOCUMENTACION, orden de revisión del historial),
más 2 problemas críticos y hallazgos H-P1-3/H-M1-5. Confirmado por
lectura que no hay pérdida de contenido de v1 en v2.

**v2→v2(2):** ⚠️ hallazgo importante — pese al nombre "v2 (2)" que
sugiere copia/duplicado, **es un superset textual exacto (append puro)**
de v2, no una copia idéntica. El diff normalizado confirma que TODO el
contenido de v2 aparece intacto en v2(2), y v2(2) agrega una sección
completa nueva al final ("PLAN DE EJECUCIÓN — ARQUITECTURA DE SESIONES":
DC-08, arquitectura de 3 niveles, specs A/B/C, resumen de sesiones). Solo
el pie de página cambia para reflejar el contenido agregado. **Mismo tipo
de trampa que 2.5.c/2.5.d pero en dirección opuesta: acá el nombre
sugería "copia" y en realidad es una versión distinta con contenido
adicional real — no asumir por el "(2)" del nombre, se verificó por
diff.**

**v2(2)→v3:** reescritura/reorganización real ("v3 — UNIFICADO"), declara
reemplazar v1, v2, v2(2) y además un archivo externo no presente en
nuestro set de 6 (`SESSION_LOG_CONSOLIDADO_2026-06-18.md`). El diff
muestra ~243 líneas de v2(2) que "desaparecen", pero se verificó
mediante grep de todos los identificadores clave (PC-1/PC-2, H-P1-3,
H-M1-5, DC-05 a DC-08, TAREA 17B, BUG-1/3/4, referencias a Sec 21/4.3/3.4/22)
que **todo el contenido sustantivo sobrevive**, solo renombrado
(PROBLEMA CRÍTICO 1/2 → PC-1/PC-2) y reorganizado en un esquema de 3
sesiones (extended thinking / IA baja / extended thinking). v3 además
avanza el estado real: registra que la Sesión 1 (diseño de specs) se
completó, con 3 scripts producidos y verificados (DC-09). **Superset
funcional confirmado, no solo por ausencia de delete sino por grep
dirigido a cada concepto que el diff mostraba como "desaparecido".**

**v3→v4:** v4 se declara "ACUMULATIVO", reemplaza v3 explícitamente.
Registra la ejecución real de la Sesión 2 (2026-06-19): Spec A corrida
con bug abierto (BUG-A1), Spec B corrida limpia (hallazgo: cero menciones
reales de "democratización" en 7345 mensajes de las 5 cuentas), Spec C
corrida con bug encontrado y corregido (BUG-C1). Verificado por grep que
todos los identificadores de v3 (PC-1/2, H-P1-3, H-M1-5, DC-05 a DC-09,
TAREA 17B, BUG-1/3/4, Sec 21/4.3/3.4/22, OP_ARCH, referencia a
SESSION_LOG_CONSOLIDADO) siguen presentes en v4. **Superset funcional
confirmado + avance real de estado.**

**v4→v5:** el más limpio de toda la cadena — incluso ambos archivos
tienen el mismo número de líneas (599). Diff normalizado muestra que
**el cuerpo completo (líneas 7 a 599) es idéntico byte a byte**, y hash
SHA-256 del cuerpo coincide salvo el header. Solo cambian las primeras
6 líneas de metadata: v5 agrega que Sesión 2 (continuación) reprodujo y
verificó specs A/B/C como idénticas a v4, que se intentó tocar Fase 1
del mod sin reconfirmación explícita del operador, que el operador
detuvo ese avance y estableció DC-11 (incidente de alcance), y que los
pasos 6-9 del mod quedan BLOQUEADOS (no solo pendientes). Nota menor: el
pie de página de v5 quedó con un vestigio no corregido que dice "v4" —
cosmético, no afecta el contenido. **Superset estricto puro.**

**Conclusión de la cadena:** v1 < v2 < v2(2) < v3 < v4 < v5 confirmado
por contenido real en cada salto, sin asumir transitividad automática ni
relación por nombre/fecha.

**Decisión — archivos a conservar (los 6, aplicando el criterio
corregido — ver aviso al inicio del log):** ningún archivo de esta
cadena es un duplicado verdadero entre sí (todos tienen hash normalizado
distinto y contenido real distinto, aunque haya relación de superset).
Se conservan los 6 completos como trazabilidad histórica del desarrollo
de esta sub-tarea del proyecto:
1. `SESSION_LOG_ANALISIS_C1_2026-06-18__9851dff1.md`
2. `SESSION_LOG_ANALISIS_C1_2026-06-18_v2__811f678f.md`
3. `SESSION_LOG_ANALISIS_C1_2026-06-18_v2 (2)__6eccfeaf.md`
4. `SESSION_LOG_ANALISIS_C1_2026-06-18_v3__8e4eefe9.md`
5. `SESSION_LOG_ANALISIS_C1_2026-06-18_v4__ff7b0e08.md`
6. `SESSION_LOG_ANALISIS_C1_2026-06-18_v5__4f16cc13.md`

**Nota para la próxima sesión — pendiente real, no cerrado:**
`SESSION_LOG_CONSOLIDADO_2026-06-18.md`, mencionado por nombre dentro de
v3/v4/v5 como archivo que v3 reemplaza/unifica, **no está presente en el
set de 274 candidatos ni en el zip** — no se pudo confirmar si existe en
algún lado de las 15 copias de seguridad originales o si su contenido
vive únicamente absorbido dentro de v3 en adelante (lo cual, si es así,
haría innecesario rescatarlo aparte). No se investigó más en esta
sesión, queda como pendiente menor si aparece en otra búsqueda.

---

#### 3.6.sexies — CERRADA CON SALVEDAD EN ESTA SESIÓN (v9): cadena TECHNICAL_WIKI ACTIVE/ARCHIVE

Quinta de las cadenas incrementales candidatas del punto 3 de prioridad.
**Resultado distinto a las 4 cadenas anteriores: es la primera vez, ya
bajo el criterio corregido de v8, que no se puede confirmar "sin pérdida
de contenido" para el conjunto completo.** No se fuerza la conclusión —
se presenta la evidencia mixta, como pide la regla de v7/3.6.quater para
estos casos.

Archivos (del set de 274, subcarpeta `candidatos_valiosos/`), con ruta
original confirmada contra `_indice_copiados.csv`:
- `IRAM_TECHNICAL_WIKI_ACTIVE_v3_1_2026-05-27_20-55__de396c3d.md` (195311 B, 3273 líneas)
- `IRAM_TECHNICAL_WIKI_ACTIVE_v3_2_2026-05-30_03-14__33961f73.md` (165951 B, 2791 líneas)
- `IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09 _2__8d7a77a5.md` (98297 B, 1630 líneas)
- `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_1_2026-05-27_20-55__39b9e7ef.md` (89718 B, 1905 líneas)
- `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_2_2026-05-30_03-14__a90e9773.md` (95589 B, 1988 líneas)
- `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09 _2__9a276d30.md` (170017 B, 3476 líneas)

**Aviso inicial (no asumido, verificado):** dentro de ACTIVE, v3_1 (3273
líneas) es más grande que v3_2 (2791) y que v3_10 (1630) — rompe de
entrada la hipótesis "más nueva = más grande = superset". Los hashes
normalizados (CRLF→LF) de los 6 archivos son todos distintos entre sí —
ningún duplicado exacto en esta familia.

**Hallazgo estructural, nuevo respecto a las 4 cadenas anteriores:**
ACTIVE y ARCHIVE no son dos cadenas independientes en paralelo — son un
**sistema de vasos comunicantes real**. El proyecto movió contenido
activamente desde ACTIVE hacia ARCHIVE en al menos dos momentos, para
aligerar el documento operativo. El propio pie de página de v3_10 lo
declara explícitamente: *"Cambios v3.10: Secciones 1, 2, 4.1, 4.2, 4.4,
9, 10, 11, 13, 16 eliminadas (contenido en ARCHIVE)."* Esto se verificó
por diff, no se asumió por la declaración textual.

**ACTIVE v3_1 → v3_2** (549 líneas eliminadas, 67 agregadas):
- La mayoría del cambio es el patrón ya conocido: actualización de
  estado en tablas de pendientes/cerrados (mismo patrón que
  WIKI_DOCUMENTACION e hitos_metodologicos).
- **Pero hay pérdida de detalle real además de actualización de
  estado.** Un log de decisiones extenso de mayo 2026 (Sección 19:
  diseño de Migración/Ascenso/Descenso Forzado, tabla completa de
  Constructor Automático por trade good con 34 entradas, datos crudos
  de mapa — 8.062 territories, 551 areas, promedio 11,27 territories
  colonizables por area —, tabla de thresholds por tipo de territory
  con valores numéricos) se retira de ACTIVE. El propio texto de v3_2
  declara "Documentación propagada al ARCHIVE... Sección 19 del ACTIVE
  limpiada — solo entradas abiertas."
- **Verificado en ARCHIVE_v3_2: sí hay un resumen fiel** de esas
  sesiones (entradas "SUPERBACKUP v2.3" a "v2.6" con las decisiones
  principales, incluida una versión condensada de la tabla de
  Constructor Automático). Pero es un resumen de 2-3 líneas por sesión,
  no el detalle operativo completo.
- **Dos bloques de detalle técnico específico, verificados por grep
  dirigido, NO sobreviven en ninguno de los 6 archivos de la familia:**
  1. La tabla completa de thresholds por tipo de territory (Settlement
     = 15, City = 20, Metropolis = 20, con modificadores de building que
     los reducen a 10/10/15).
  2. Los datos crudos de mapa (8.062 territories totales, 1.789 no
     jugables, 6.209 colonizables, 551 areas, promedio 11,27 territories
     colonizables por area, distribución 513 de 551 areas con 10-12
     territories).

**ARCHIVE v3_1 → v3_2** (2 líneas eliminadas, 83 agregadas): superset
estricto puro, sin ambigüedad. Agrega íntegro el resumen de las sesiones
"SUPERBACKUP v2.3" a "v2.6" (ver punto anterior).

**ACTIVE v3_2 → v3_10** (1557 líneas eliminadas, 396 agregadas):
- Confirmado por comparación de tamaño de sección (líneas casi
  idénticas, diferencia de 2-3 por encabezado de archivo) que las
  Secciones 9 (Diseño v4 on_action/scripted_gui), 10 (Localización), 11
  (Cancel_all) y 13 (Pendientes) migran **completas y verificadas** a
  `ARCHIVE_v3_7`.
- Confirmado también que la Sección 16 completa ("Slave Distributor" —
  thresholds verificados ingame, tiers de distribución, pseudocódigo,
  triggers) migra completa a `ARCHIVE_v3_7` (línea 2996 en adelante),
  con el mismo nivel de detalle técnico que tenía en ACTIVE.
- Las Secciones 1 ("Historia del proyecto" — cronología de versiones
  IRAM v1→v4.3.2, matriz de evolución de funciones por versión) y 2
  ("Estado actual") no aparecen con esos títulos en ARCHIVE_v3_7, pero
  se encontró **evidencia narrativa parcial equivalente** ya presente en
  ARCHIVE desde v3_1 (entradas "IRAM v1 — Drago Mod Pack Estable...",
  "IRAM v2 — Drago Mod Pack ALT..." con el mismo contenido de fondo,
  aunque en formato narrativo en vez de tabla).
- **La Sección 20 (Protocolo de actualización del documento) y el ítem
  21.1 ("Qué cambió en cada versión de v4") NO tienen correlato
  verificado en ARCHIVE_v3_7 ni en ningún otro de los 6 archivos.**
  Confirmado por grep dirigido, no encontrado en ningún lado.

**ARCHIVE v3_2 → v3_7** (2 líneas eliminadas, 1490 agregadas): casi puro
append, coherente con ser el receptor del contenido migrado desde
ACTIVE v3_10 (Secciones 9/10/11/13/16 completas, ver arriba).

**Conclusión de la cadena — evidencia mixta, no forzada (mismo criterio
que el caso PROMPT_MAESTRO v1.6/v1.8 de 3.6.quater):** a diferencia de
WIKI_DOCUMENTACION, hitos_metodologicos, PROMPT_MAESTRO
(`IRAM_PROMPT_MAESTRO`) y SESSION_LOG_ANALISIS_C1, en esta familia **no
se pudo confirmar "sin pérdida de contenido semántico" para el conjunto
completo.** Hay 3 bloques concretos, verificados por grep dirigido, que
existieron en ACTIVE v3_1/v3_2 y no tienen correlato en ninguno de los 6
archivos:
1. Tabla completa de thresholds por tipo de territory (con valores
   numéricos exactos).
2. Datos crudos de mapa (conteos de territories/areas).
3. Sección 20 (Protocolo de actualización) + ítem 21.1.

**Decisión — archivos a conservar (aplicando el criterio de v8, sin
cambios):** se conservan los 6 archivos completos, igual que en toda
cadena anterior — el criterio de v8 no depende de si hay pérdida
confirmada o no, solo depende de si hay duplicado exacto por hash
normalizado (no lo hay en esta familia). Lo que cambia respecto a las
cadenas anteriores es que **no se puede etiquetar esta cadena como
"cerrada sin salvedad"** — queda registrada la pérdida de detalle
puntual para que quede visible en la trazabilidad, no para decidir qué
se descarta (nada se descarta).
1. `IRAM_TECHNICAL_WIKI_ACTIVE_v3_1_2026-05-27_20-55__de396c3d.md`
2. `IRAM_TECHNICAL_WIKI_ACTIVE_v3_2_2026-05-30_03-14__33961f73.md`
3. `IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09 _2__8d7a77a5.md`
4. `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_1_2026-05-27_20-55__39b9e7ef.md`
5. `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_2_2026-05-30_03-14__a90e9773.md`
6. `IRAM_TECHNICAL_WIKI_ARCHIVE_v3_7_2026-06-09 _2__9a276d30.md`

**Nota metodológica nueva de esta sesión — agregar a la lista de
trampas conocidas:** en cadenas con documento "activo + archivo"
(operativo + histórico), no basta con diffear ACTIVE contra sí mismo
(v_n vs v_n+1) para juzgar pérdida de contenido — hay que cruzar lo que
"desaparece" de ACTIVE contra el ARCHIVE correspondiente antes de
concluir. En este caso la mayoría del contenido retirado de ACTIVE sí
aparece migrado en ARCHIVE (verificado, no asumido por la declaración
del propio documento), pero no el 100% — de ahí la salvedad. Mismo
principio que ya regía (verificar, no asumir) pero aplicado ahora a
relaciones cruzadas entre dos series de archivos, no solo dentro de una
sola cadena lineal.

---

#### 3.6.octies — CERRADA EN ESTA SESIÓN (v13): familia
`SESSION_LOG_REPLANTEO` (19 archivos)

**Familia grande de 3.6, no una de las 5 cadenas incrementales
originales del punto 3 ni la misma familia que `SESSION_LOG_
DOCUMENTACION` (3.6.septies) — nombre parecido, familia distinta,
período distinto (esta va de 2026-06-19 a 2026-07-05, la otra hasta
06-12/después).**

**Paso 0 — duplicados exactos por hash:** se normalizó CRLF→LF sobre
los 19 archivos y se calculó hash normalizado de cada uno. **Los 19
hashes son distintos entre sí — cero duplicados exactos.** Ninguno se
descarta por esta vía.

**Paso 1 — método usado para ordenar la cadena:** a diferencia de
`SESSION_LOG_DOCUMENTACION` (que declaraba número de sesión), acá cada
archivo declara en su segunda línea de encabezado una fecha/hora
explícita y a qué archivo exacto "Reemplaza como punto de partida
operativo" (por nombre completo, sin sufijos de copia). Se extrajo esa
declaración de los 19 archivos para reconstruir el grafo de
precedencia.

**Hallazgo estructural — esta familia NO es una cadena lineal de 19
pasos, es una cadena con puntos de ramificación por checkpoints
intra-sesión:**
- **6 archivos** declaran reemplazar al mismo predecesor
  (`SESSION_LOG_REPLANTEO_2026-06-20_5.md`): `2026-07-03` (sin hora),
  `2026-07-03 2` (mellizo del anterior, mismo motivo declarado),
  `2026-07-03_01-52`, `2026-07-03_01-57`, `2026-07-03_02-13`,
  `2026-07-03_02-43`.
- **3 archivos** declaran reemplazar al mismo predecesor
  (`SESSION_LOG_REPLANTEO_2026-07-03_02-43.md`): `2026-07-03_17-47`,
  `2026-07-03_17-58`, `2026-07-03_17-58 2` (mellizo del anterior, mismo
  motivo declarado).
- **Verificado por diff encadenado en orden de timestamp** que ninguno
  de estos dos grupos es una bifurcación incompatible (no es el caso
  3.6.septies de "narrativas del mismo checkpoint que se contradicen"):
  es una **progresión real dentro de la misma sesión de trabajo**, cada
  paso agrega contenido sobre el anterior sin perder nada del previo.
  Diffs verificados: `07-03`→`01-52` (32 líneas de diff, agrega
  contenido), `01-52`→`01-57` (10 líneas), `01-57`→`02-13` (6 líneas),
  `02-13`→`02-43` (22 líneas) — todos crecientes, ninguno vacío.
  Coherente con que el propio `01-52` documenta haber adoptado recién
  ahí la "convención de nombres AAAA-MM-DD_HH-MM para archivos del
  replanteo" (DR-24): antes de esa convención, varios checkpoints de un
  mismo día comparten nombre-base sin hora.

**Hallazgo operativo nuevo (no visto en familias anteriores) — carpeta
de cuarentena del propio proyecto:** cruzando contra `_indice_
copiados.csv`, **6 de los 19 archivos** venían de
`_CUARENTENA_DUPLICADOS/raiz_duplicados_SESSION_LOG_REPLANTEO/` (los
mismos 6 que citan a `07-03_02-43` como predecesor más 3 del grupo de
`06-20_5`: en total `02-13`, `02-43`, `17-47`, `17-58`, `17-58 2`,
`23-17`), mientras que los otros **13** venían de la carpeta oficial
`0_REPLANTEOS_Y_DECISIONES/01_logs_replanteo/` o `02_logs_replanteo_
cola/`. Es decir, el operador (o un proceso de organización previo) ya
había marcado esos 6 como sospechosos de ser duplicados redundantes.
**Verificado que es un falso positivo:** comparando nombres-base, los
19 timestamps son todos distintos entre sí — ningún archivo de
cuarentena comparte nombre-base con ningún archivo de la carpeta
oficial — y ya se confirmó por hash que tampoco hay coincidencia de
contenido. Los 6 archivos "en cuarentena" son pasos genuinos y
distintos de la cadena real, no copias de los 13 oficiales. Mismo
patrón de falso positivo por heurística de carpeta/nombre sin verificar
contenido que ya se documentó en 2.5 y 3.6.ter — **no había que
descartarlos.**

**Los 4 pares con timestamp o motivo declarado casi idéntico —
verificados individualmente por diff, todos confirmados como supersets
reales, no duplicados:**
- `2026-06-19` vs `2026-06-19 2`: **27 líneas de diff.** `2` agrega DR-08
  (categoría "costo narrativo no solicitado") y DR-09 (categoría
  "acción sin autorización"), más una sección completa nueva de
  "INVESTIGACIÓN DE NOVEDAD" (qué de esto ya existe publicado, tabla
  comparativa contra literatura de agentes/HITL/ADR) y una entrada
  nueva en "QUÉ NO HACER". Superset real y sustancial.
- `2026-06-20 3` vs `2026-06-20 5`: **139 líneas de diff.** Reescritura
  real del framework de categorías de autoría (de "Framework A" simple
  a "Framework B — autoridad de decisión, no supervivencia de texto"),
  agrega DR-21 (pipeline Diseño→Limpieza→Análisis→Comparativa) y
  reorganiza las métricas de Grupo 1/Grupo 2. No es cosmético, es
  revisión de fondo.
- `2026-07-03` vs `2026-07-03 2`: **25 líneas de diff.** `2` agrega
  DR-22 (cadena completa verificada del origen de la frase
  "democratización", con las 7 etapas documentadas) y DR-23 (gaps de
  conocimiento del mod ya mapeados, no rehacer), más una tarea 0
  bloqueante nueva en "PRÓXIMAS TAREAS". Superset real.
- `2026-07-03_17-58` vs `2026-07-03_17-58 2`: **el más ajustado de los
  4 — solo 4 líneas de diff, 1 sola entrada de tabla (DR-33)
  modificada.** `2` amplía la verificación de zips: agrega
  `DOCUMENTACION.zip` a la lista de backups verificados como
  redundantes ("18/18 idénticos") y agrega una frase de cierre que no
  estaba en la versión anterior. Diferencia pequeña pero sustantiva —
  no es duplicado exacto (ya confirmado también por hash). **Se
  conservan ambos**, mismo criterio que el resto.

**RESULTADO FINAL — familia `SESSION_LOG_REPLANTEO` (19 archivos): se
conservan los 19 completos.** Ninguno resultó duplicado exacto por hash
normalizado. Incluye 2 grupos de checkpoints intra-sesión (6 que citan
a `06-20_5`, 3 que citan a `07-03_02-43`) confirmados como progresión
real sin pérdida, y el hallazgo de que 6 archivos estaban mal
clasificados en la carpeta de cuarentena del propio proyecto sin
corresponder a duplicados reales.

Mismo método de diff estructural que funcionó en 2.2, 2.4.b, 2.4.c,
2.5.b, 3.6.bis, 3.6.ter, 3.6.quater, 3.6.quinquies, 3.6.sexies y
3.6.septies: normalizar CRLF antes de comparar, no asumir que la
versión/fecha más alta es superset hasta confirmarlo por diff, no
asumir relación de duplicado por coincidencia de carpeta o de nombre
sin verificar contenido — y, nuevo de esta sesión (v13): **una carpeta
de "cuarentena de duplicados" creada por el propio operador/proceso
previo no es garantía de que su contenido sea efectivamente redundante
— se audita igual que cualquier otro archivo, por hash y por diff, no
por la etiqueta de la carpeta que lo contiene.**

#### 3.6.novies — CERRADA EN ESTA SESIÓN (v14): familia `IRAM_C1`
(18 archivos)

**No es una de las 5 cadenas incrementales originales del punto 3 —
familia distinta, es el entregable "C1" del Módulo 5 (paper/case study
final del proyecto), con 4 capas: 1 esqueleto de planificación, 14
drafts por sección (2 por cada Sección 1–7), 1 versión "completo"
(concatenación editorial) y 1 versión "final".**

**Paso 0 — duplicados exactos por hash:** normalizado CRLF→LF sobre los
18 archivos, hash normalizado de cada uno. **Los 18 hashes son
distintos entre sí — cero duplicados exactos.**

**Estructura real de la familia (por lectura de contenido, no solo de
nombre):**
- `IRAM_C1_esqueleto_s17` (sesión 17) — el plan: define las 7 Secciones
  del documento y trae una tabla "MAPPING SKILL v1.0 → C1" con notas de
  "Fuente en SKILL v1.0" por sección. **Contenido único, no se
  reproduce en ningún otro archivo de la familia** — verificado
  buscando "MAPPING COMPLETO" / "Fuente en SKILL" en `completo_s32` y
  en `final`: 0 apariciones en ambos.
- 14 drafts sueltos `IRAM_C1_sN_draft_sMM` — N indexa la Sección del
  documento (1 a 7), MM el número de sesión en que se escribió ese
  draft (s20, s24, s25, s28, s29, s30, s31). **No es una cadena
  secuencial única: son 2 drafts por sección** (salvo verificar
  Sección 4, que tiene 3 archivos — ver nota abajo), un borrador
  inicial y una revisión "correcciones finales" de la misma sección.
  **Verificado por diff en las 6 secciones con par simple (1, 2, 3, 5,
  6, 7):** en todas, la versión posterior es superset limpio del
  borrador — reformulación/condensación de prosa, agrega precisión
  numérica o de detalle, sin pérdida de contenido semántico. Ejemplo
  notable: Sección 2 (`s24`→`s30`) reescribe 13 líneas de prosa en un
  párrafo condensado; verificado línea a línea que las 5 piezas del
  sistema de documentación (con su función) reaparecen todas en la
  versión condensada.
  **Nota — Sección 4 tiene un tercer archivo** (`s4_draft_s30 _2`),
  **caracterizado en esta sesión: NO es mellizo de `s4_draft_s30`, es
  en realidad la versión `s32`** (mal nombrada con sufijo de copia
  ` _2` en vez de reflejar el número de sesión real — mismo tipo de
  desprolijidad de nombre que otros casos ya vistos en 2.5 y 3.6.ter,
  pero acá el contenido interno sí lo distingue con claridad). Su pie
  dice literalmente *"Sección 4 — draft s32 — correcciones finales"* y
  *"INC-13 verificado contra SESSION_LOG v5.6 del proyecto y corregido
  en s32"* — es decir, **es la fuente original de la Sección 4 que
  luego entró a `completo_s32`**, no una tercera variante redundante.
  Diff contra `s4_draft_s30` (82 líneas): reescribe el "tercer caso"
  del hallazgo 4B con el detalle técnico real y verificado
  (`trigger_event`, `on_action`, `immediate` vs. cleanup inline, tick
  de ejecución del motor) en vez de la descripción genérica que traía
  `s30` ("cierto elemento del código", "razones de limpieza") — resuelve
  exactamente la nota pendiente "INC-13" que `s30` dejaba abierta.
  Confirma además, con texto explícito, la relación de precedencia que
  ya se había inferido indirectamente al analizar `completo_s32`.
- `IRAM_C1_completo_s32` — concatenación editorial de los 7 drafts
  finales (s31/s30/s29 según sección), **con una capa de contenido
  propio no trivial:** la Sección 4 dentro de `completo_s32` está en
  versión `s32`, no `s30` como el archivo suelto — agrega el hallazgo
  "4D — El tiering no es opcional" (resolviendo la nota "INC-13
  pendiente" que traía `s4_draft_s30`) y cambia el título de la sección
  de "tres hallazgos" a "cuatro hallazgos". **Esa Sección 4D no existe
  en ningún archivo suelto de la familia — solo en `completo_s32` y en
  `final`.**
- `IRAM_C1_final` — reescritura editorial completa de `completo_s32`
  (título nuevo "Case study: IRAM...", subtítulos internos
  renombrados/reorganizados, formato de índice agregado). **Verificado
  por muestreo de 15 términos/datos clave** (cifras, nombres de
  hallazgos, conceptos formales como ADR/HITL/RAG/grid search) que el
  contenido sustantivo de `completo_s32` sobrevive intacto en `final`.
  Las únicas 2 ausencias encontradas ("INC-13", "SESSION_LOG v5.6") son
  notas de proceso editorial de la corrección aplicada en `s32`, no
  contenido del paper — coherente con que `final` es la versión pulida
  para publicación, sin metadata de trabajo interno.

**RESULTADO FINAL — familia `IRAM_C1` (18 archivos): se conservan los
18 completos.** Ninguno es duplicado exacto por hash. Cada capa aporta
algo verificablemente distinto: el esqueleto documenta la planificación
y el mapping de fuentes (único); los 14 drafts sueltos documentan la
evolución de redacción por sección; `completo_s32` es el único lugar
con la Sección 4D antes de la reescritura final; `final` es la versión
publicable. Mismo método de diff estructural que 2.2, 2.4.b, 2.4.c,
2.5.b, 3.6.bis–octies: normalizar CRLF antes de comparar, no asumir
relación de duplicado por parecido de nombre sin verificar contenido,
y verificar por muestreo de términos clave cuando el diff línea a línea
deja de ser práctico por reescritura editorial de fondo.

**Sin pendientes dentro de esta familia** — los 3 archivos de Sección 4
quedaron caracterizados: `s24` (borrador inicial), `s30` (correcciones
finales, deja INC-13 abierto), y `s30 _2` (en realidad `s32`, resuelve
INC-13 con el detalle técnico real — es la fuente que entró a
`completo_s32`).

#### 3.6.decies — CERRADA EN ESTA SESIÓN (v16): familia
`SESSION_LOG_AUDITORIA_CONTINUIDAD` (2 archivos)

**Paso 0 — duplicados exactos por hash:** normalizado CRLF→LF sobre los
2 archivos (`2026-07-06`, `2026-07-07`). **Hashes distintos — no son
duplicados.**

**No es una cadena de versiones del mismo documento — son 2 sesiones de
trabajo consecutivas y complementarias**, verificado por lectura
completa de inicio y fin de ambos:
- `2026-07-06`: continúa una auditoría zip↔inventario nacida el 05-07,
  retomada el 06-07 en una sesión que "se cortó sin cierre". Confirma
  que el ZIP no cambió desde el corte anterior (2382 archivos, mismos
  hashes en cada punto de chequeo), corrige un error de conteo propio
  (677 entradas de carpeta contadas como archivos), y dedica su cuerpo
  principal a revisar 43 grupos de colisión de nombre con hash
  distinto, dejando el "Paso 0" (abrir uno por uno los 17 grupos con
  contenido genuinamente divergente) como pendiente explícito para la
  sesión siguiente.
- `2026-07-07`: se declara a sí mismo, en su propio encabezado,
  **"continuación directa de `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`"**
  y ejecuta exactamente ese "Paso 0" pendiente — abre los 17 grupos de
  colisión con contenido real (no solo hash) y genera un checklist
  aparte (`PASO_0_grupos_divergentes_checklist.md`, no incluido en este
  set de 274). Aporta contenido propio no redundante: la resolución
  caso por caso de los 17 grupos (9 correcciones/revisiones claras + el
  resto en otras 2 categorías), el hallazgo de "fuga de memoria" (4
  archivos sueltos no catalogados en ningún log anterior), y el estado
  actualizado de DR-54 y DR-30.

**RESULTADO FINAL — familia `SESSION_LOG_AUDITORIA_CONTINUIDAD` (2
archivos): se conservan los 2 completos.** No hay relación de
duplicado ni de superset entre ellos — son dos sesiones distintas de
una misma línea de trabajo, cada una con hallazgos propios que la otra
no contiene. Mismo criterio que las cadenas de sesión ya cerradas
(3.6.septies, 3.6.octies): un log de sesión que continúa a otro no se
colapsa con su predecesor solo porque uno "complete" el trabajo que el
otro dejó pendiente.

**Sin pendientes dentro de esta familia.**

#### 3.6.undecies — CERRADA EN ESTA SESIÓN (v16): familia
`IRAM_analisis_cuantitativo` (3 archivos)

**Paso 0 — duplicados exactos por hash:** normalizado CRLF→LF sobre los
3 archivos (base sin sufijo, `v2`, `v3`). **Los 3 hashes son distintos
entre sí — cero duplicados exactos.**

**Cadena de versiones real, verificada por diff completo (no solo por
substring, siguiendo la lección de 3.6.bis):**
- **Base → v2: NO es un superset simple.** v2 rehace metodológicamente
  el Bloque 2 completo y **revierte la conclusión de la base**: la base
  declara veredicto "PARALELAS" ("La hipótesis de secuencialidad era
  incorrecta", con tabla de 89 sesiones vacías y 198 pares de sesiones
  solapadas en <30 min); v2 declara veredicto "ROTACIÓN SECUENCIAL
  RÁPIDA" ("0 casos" de interleaving real A-B-A en <5min, sobre 7.313
  mensajes con timestamp individual — metodología corregida:
  timestamps de mensaje en vez de timestamps de inicio de sesión).
  Contenido semántico real de la base (los datos y el veredicto de
  "PARALELAS") no tiene correlato en v2 — es reemplazado, no
  complementado. Caso de evidencia mixta análogo a 3.6.quater
  (PROMPT_MAESTRO v1.6→v1.8): no alcanza con "es más nuevo", hubo
  reescritura real de fondo.
- **v2 → v3: sí es superset limpio**, verificado por diff completo:
  v3 agrega el Bloque 3 entero (distribución de trabajo por tipo y
  fase — 4 tablas nuevas A/B/C/D sobre código/investigación/build por
  fase) sin tocar ni revertir nada del contenido de v2. El bloque de
  conclusiones se actualiza sumando un punto nuevo (rol de arquitecto
  del operador), coherente con lo agregado, no contradictorio.

**RESULTADO FINAL — familia `IRAM_analisis_cuantitativo` (3 archivos):
se conservan los 3 completos.** Bajo el criterio de v8 (conservar toda
la cadena de versiones distintas, no solo la más nueva) los 3 se
rescatan igual, pero se deja registrado que la relación base→v2 es de
**corrección metodológica con reversión de conclusión**, no de
superset — mismo patrón de "evidencia mixta, no forzar superset" que
3.6.quater. **Este es uno de los dos documentos donde aparece,
narrado desde el lado del análisis cuantitativo, el mismo ciclo de
revisión sobre el modelo de cuentas paralelas/secuenciales que también
aparece en `PROMPT_DOCUMENTACION_IRAM_v1` (ver 3.6.terdecies) — las dos
familias se corrigen de forma cruzada y coherente entre sí.**

**Sin pendientes dentro de esta familia.**

#### 3.6.duodecies — CERRADA EN ESTA SESIÓN (v16): familia
`IRAM_SESSION_LOG` (4 archivos)

**Paso 0 — duplicados exactos por hash:** normalizado CRLF→LF sobre los
4 archivos (`2026-05-28_17-31`, `2026-05-29_05-29`, `2026-05-30_03-14`,
`v5_6_2026-06-09_17-59 (2)`). **Los 4 hashes son distintos entre sí —
cero duplicados exactos.**

**No son versiones del mismo documento — son 4 logs de sesión de
desarrollo del mod, cronológicamente encadenados por "Continuación de:
SESSION_LOG [fecha anterior]" en cada encabezado**, verificado por
lectura de inicio de los 4:
- `2026-05-28_17-31` (IRAM v4.3.8) — continuación de SESSION_LOG
  2026-05-28 16:55, "sesión se cortó 2 veces".
- `2026-05-29_05-29` (IRAM v4.3.10→11) — continuación de SESSION_LOG
  2026-05-29 05:07.
- `2026-05-30_03-14` (IRAM v4.3.16) — continuación de SESSION_LOG
  2026-05-30 03:01, implementa los 4 fixes que esa sesión anterior
  había dejado diseñados.
- `v5_6_2026-06-09_17-59 (2)` — salto grande de versión (v4.3.16 →
  v5.5/v5.6), pero mismo patrón de log de sesión propio: auditoría
  consolidada de 35 hallazgos + plan de ejecución v5.6. **No confundir
  el "(2)" del nombre con copia redundante** (regla ya confirmada en
  3.6.octies): el propio archivo referencia internamente a
  `IRAM_SESSION_LOG_v5_6_2026-06-09_17-59.md` (sin "(2)") como si fuera
  un documento hermano — verificado contra el índice
  (`_indice_copiados.csv`) que **es el único hash rescatado de ese
  nombre-base** (`cantidad_lugares_donde_aparece = 4`, es decir existe
  replicado idéntico en 4 rutas del corpus de 15 backups, pero todas
  comparten el mismo hash — no hay una versión "(1)" distinta que haya
  llegado al set de 274 candidatos).

**RESULTADO FINAL — familia `IRAM_SESSION_LOG` (4 archivos): se
conservan los 4 completos.** Son logs de sesión de desarrollo
individuales y cronológicamente distintos, no una cadena de versiones
del mismo documento — no hay duplicado ni superset que evaluar entre
ellos, cada uno documenta un tramo de trabajo real que no se repite en
los otros.

**Sin pendientes dentro de esta familia.**

#### 3.6.terdecies — CERRADA EN ESTA SESIÓN (v16): familia
`PROMPT_DOCUMENTACION_IRAM_v1` (5 archivos)

**Paso 0 — duplicados exactos por hash:** normalizado CRLF→LF sobre los
5 archivos (`v1_4`, `v1_5`, `v1_7`, `v1_9 (3)`, `v1_9 (4)`). **Los 5
hashes son distintos entre sí — cero duplicados exactos.**

**Cadena de versiones real, verificada por diff completo salto por
salto (v1_4→v1_5→v1_7→v1_9(3)→v1_9(4)):**

| Salto | Tipo de relación confirmado por diff |
|---|---|
| v1_4 → v1_5 | **No superset simple.** Reescribe la regla sobre el modelo de las 5 cuentas de Claude: v1_4 decía "trabajando secuencialmente"; v1_5 corrige a "en paralelo — múltiples cuentas activas simultáneamente" (nace R18). También comprime la sección "5 dimensiones" de un desarrollo explicado en detalle a una lista de una línea por dimensión — se pierde texto explicativo real, no solo se resume. |
| v1_5 → v1_7 | **No superset simple — es una segunda reversión de la misma regla.** R18 se reescribe de nuevo: "paralelas" (v1_5) → "rotación secuencial rápida, no paralelismo" (v1_7), con dato duro (0 interleavings en 7.313 mensajes con timestamp individual, campo `ts`). v1_7 degrada explícitamente el hito `cuentas_paralelas` a **falso positivo** y lo reemplaza por `rotacion_de_contextos`. Agrega R19 (único SESSION_LOG, no crear logs separados por tipo de sesión). Marca Plantilla A y Plantilla D como ya ejecutadas. |
| v1_7 → v1_9(3) | **Mayormente superset con reestructuración real.** Bifurca lo que v1_7 llamaba "Plantilla C" (un solo SKILL.md) en dos productos separados: **C1** (paper/research narrative para humanos) y **C2** (skill operacional para Claude, ~40-60 líneas). Agrega R20 (verificar archivos no renderizados con bash_tool antes de asumir su contenido — no inferir desde lo que dicen otros archivos). |
| v1_9(3) → v1_9(4) | **Superset limpio, ya verificado en la sesión anterior.** Agrega un principio general ("preguntar antes de asumir/estimar/inventar") y causalidad entre paréntesis a reglas ya existentes (R1, R2, R3, R4, R5, R20), sin quitar nada. |

**RESULTADO FINAL — familia `PROMPT_DOCUMENTACION_IRAM_v1` (5
archivos): se conservan los 5 completos.** Ninguno es duplicado exacto
(5 hashes distintos). Bajo el criterio de v8, cada salto se conserva
como estado histórico real, incluidas las dos reversiones sucesivas de
R18 sobre el modelo de cuentas — es exactamente el tipo de trazabilidad
que la regla de oro del proyecto busca preservar, no purgar. **Este es
el segundo de los dos documentos (junto con `IRAM_analisis_cuantitativo`,
ver 3.6.undecies) donde aparece narrado el mismo ciclo de corrección
sobre cuentas paralelas/secuenciales — confirmado cruzado entre ambas
familias, con el mismo veredicto final y el mismo dato duro (0
interleavings / 7.313 mensajes), lo que da confianza adicional de que
no es un error de una sola fuente sino una conclusión metodológica real
del proyecto.**

**Dato adicional útil para 3.9 / trabajo futuro (no bloquea el cierre
de esta familia):** v1_9(3) es la fuente textual donde nace la
bifurcación C1/C2 que luego se convierte en la familia `IRAM_C1` (ya
cerrada, ver 3.6.novies) y en `IRAM_skill_desarrollo_ia_v2_0.md`
(mencionado en la sección 4 como "par de redacciones paralelas",
punto #8, aún sin decidir si fusionar o elegir uno). Si en el futuro se
retoma esa decisión, este documento es el origen documentado de por qué
existen dos productos en vez de uno.

**Sin pendientes dentro de esta familia.**

#### 3.6.quaterdecies — CERRADA EN ESTA SESIÓN (v18): 6 grupos chicos
re-verificados desde cero contra los archivos del zip

**Contexto:** la nota de continuidad de v17 (sección 5, prompt para el
próximo chat) afirmaba haber cerrado 6 grupos chicos con números y citas
específicas, pero esta sección — citada seis veces en el propio
documento como "3.6.quaterdecies, ver detalle completo" — nunca se
había escrito. Se re-verificó cada grupo desde cero contra los archivos
reales, sin asumir la declaración textual de la nota.

**1) `critica 1` / `critica a la critica` / `IRAM_critica_rigurosa`:**
las dos primeras comparten un arranque idéntico normalizado de 419
caracteres ("Contexto cargado. Estado al inicio de sesión 11...") y
luego divergen en sustancia — ratio de similitud global 0.45, con
bloques grandes compartidos (11.7k y 4.9k caracteres) intercalados con
contenido propio de cada una. Es una bifurcación real de la misma
sesión pegada dos veces con hilos de continuación distintos, mismo
patrón que 3.6.septies. `IRAM_critica_rigurosa` coincide byte a byte
(salvo 5 caracteres de ruido de interfaz al final) con el fragmento de
crítica embebido dentro de `critica 1` — es el documento final ya
extraído. **Conservar los 3.**

**2) `PASO_0_grupos_divergentes_checklist` base + `(2)`:** superset
exacto por substring — `(2)` (243 líneas) contiene el 100% de la base
(150 líneas) al inicio y agrega exactamente 9740 caracteres nuevos al
final, con contenido verificado sobre DR-22 (origen del error
"democratización" en `failed 3.md`) y DR-23 (gaps de conocimiento ya
mapeados). **Conservar ambos.**

**3) `bloque3_analysis` base + `v2`:** no es un checkpoint simple. El
propio docstring de v2 declara explícitamente que reemplaza la
clasificación por título/keywords de v1 ("que daba diseño 1.5%,
sospechosamente bajo") por tres señales objetivas basadas en
herramientas y texto de mensajes — confirmado por diff completo del
código, que muestra el cambio real del método de clasificación (de 4
categorías por keyword a 4 señales A/B/C/D basadas en fase y tipo de
herramienta). **Conservar ambos.**

**4) `spec_c_zip_history` base + `(3)`:** la única diferencia real en
todo el archivo es una corrección de regex documentada como BUG-C1 en
el propio comentario del código (corregido en Sesión 2, 2026-06-19): el
grupo opcional original no distinguía un tercer segmento de versión
real de un año de fecha pegado, y capturaba mal patrones como
"v5.5.2026". Corrección de bug puntual, no reescritura de fondo.
**Conservar ambos.**

**5) `IRAM_Prompt_Etapa1_Limpieza` + `Etapa2_Unificacion`:** documentos
hermanos de un mismo flujo de trabajo en 2 etapas secuenciales
(Etapa 1 = limpieza por agente, aplicada a cada uno de 5 archivos por
separado; Etapa 2 = unificación, fusiona los 5 archivos limpios en uno
solo, a aplicar DESPUÉS de completar la Etapa 1) — confirmado por el
texto de ambos documentos. Similitud baja (ratio 0.32), sin relación de
substring en ningún sentido. **Conservar ambos, no compiten.**

**6) `Consigna` / `Consigna_1` / `Consigna_2`:** 3 piezas curriculares
distintas de la Diplomatura UTN — presentación general del Trabajo
Final Integrador, consigna de Entrega 1 (Módulos 1-3) y consigna de
Entrega 2 (Módulos 4-5), confirmado por el contenido de cada una.
Ratios de similitud entre pares: 0.14, 0.12 y 0.27 — bajos en los 3
casos, sin relación de substring. Mismo patrón que los 16 módulos UTN de
3.8. **Conservar los 3.**

**RESULTADO FINAL — los 6 grupos re-verificados (10 archivos en
total): sin discrepancias respecto de lo que afirmaba la nota de v17.**
Todos los números, citas textuales y ratios de similitud se confirmaron
exactos contra los archivos fuente. El problema no era el contenido del
trabajo sino su trazabilidad documental — ya corregido al escribir esta
sección.

#### 3.6.quindecies — CERRADA EN ESTA SESIÓN (v19): último sub-grupo de
3.6.6, `sesion cortada.md` vs las 2 transcripciones de
`SESSION_LOG_CONSOLIDADO`

**Contexto:** pendiente heredado de v17, marcado como "primer pendiente
a resolver en la próxima sesión". Se localizaron los archivos
`sesion cortada.md`, `transcripcion de SESSION_LOG_CONSOLIDADO_2026-06-1__1f5727a2.md`,
`transcripcion de SESSION_LOG_CONSOLIDADO_2026-06-1__56abcedb.md`, y un
cuarto archivo que apareció en la misma búsqueda y se incorporó al
análisis: `SESSION_LOG_CONSOLIDADO_2026-06-18.md` (sin sufijo de
transcripción — es un documento final estructurado, no una
transcripción de chat).

**`sesion cortada.md` (verificado, tema real):** es un draft del paper
metodológico final del proyecto — termina en "Sección 7 — draft s25 —
2026-06-17" y contiene referencias directas a `SESSION_LOG_DOCUMENTACION_s23.md`,
`PROMPT_MAESTRO_DOCUMENTACION v1.9` y correcciones "s21". Tema: los
límites estructurales de la herramienta (falta de memoria entre
sesiones, techo operacional por sesión) versus el criterio especializado
que el proyecto generó. **No tiene relación temática con las otras 3.**

**Las 2 transcripciones NO son dos mitades de una sesión cortada.** Son
2 sesiones de chat separadas y secuenciales, ambas arrancando del mismo
archivo pegado (`SESSION_LOG_ANALISIS_C1_2026-06-18_v2 (2).md`) pero en
horarios distintos del mismo día:
- `__1f5727a2` (18:06): sesión más corta (11.470 caracteres). Diseña
  las specs A/B/C (extended thinking) y termina creando
  `SESSION_LOG_CONSOLIDADO_2026-06-18.md` como archivo de output, sin
  llegar a ejecutar las specs.
- `__56abcedb` (19:43): sesión más larga (28.364 caracteres) y más
  avanzada en la misma tarea. Va más allá: efectivamente ejecuta y
  prueba `spec_a_authorship.py`, `spec_b_democratizacion.py` y
  `spec_c_zip_history.py`, incluyendo casos de error (JSON inválido,
  archivos faltantes) — contenido que no aparece en absoluto en
  `__1f5727a2`.

Ambas comparten únicamente el nombre del archivo pegado al inicio (49
caracteres de prefijo normalizado común); el resto del contenido de
cada transcripción no coincide entre sí.

**`SESSION_LOG_CONSOLIDADO_2026-06-18` (sin sufijo):** es el documento
final estructurado — "SESSION LOG CONSOLIDADO — Diseño de Specs A/B/C",
fechado 2026-06-18, con la tabla de archivos de entrada/salida para
Sesión 2. Es el artefacto real de ese trabajo, distinto de ambas
transcripciones de chat (no se encontró embebido textualmente en
ninguna de las dos, consistente con que los artifacts se generan como
archivo aparte y las transcripciones solo registran el diálogo).

**Verificación cuantitativa:** ratios de similitud entre los 4 archivos
(las 6 combinaciones posibles) dieron entre 0.03 y 0.08 — muy por
debajo incluso de los pares "hermanos" más débiles vistos hasta ahora
en el proyecto (0.12–0.45). Sin relación de substring en ningún caso.
Los pocos bloques coincidentes grandes encontrados (37-69 caracteres)
son frases-tesis repetidas en todo el proyecto ("la IA no democratiza
la programación", "el operador fue el arquitecto"), no estructura ni
contenido compartido real.

**RESULTADO FINAL — los 4 archivos son independientes entre sí, ninguno
descartable.** Cada uno documenta un momento distinto del proyecto.
**Conservar los 4, sin descartes.**

**Con el cierre de este sub-grupo, se completan todos los grupos
chicos/pares de 3.6 listados originalmente — no queda ningún sub-grupo
de 3.6 sin revisar.**

#### Prioridad sugerida dentro de 3.6 (ACTUALIZADA — punto 3, cadenas
incrementales 5 de 5 cerradas; familias grandes adicionales cerradas:
SESSION_LOG_DOCUMENTACION, SESSION_LOG_REPLANTEO, IRAM_C1,
SESSION_LOG_AUDITORIA_CONTINUIDAD, IRAM_analisis_cuantitativo,
IRAM_SESSION_LOG, PROMPT_DOCUMENTACION_IRAM_v1 — **con esto, TODAS las
familias grandes de 3.6 quedan cerradas, ver 3.6.decies a 3.6.terdecies
para las 4 nuevas de v16**)
1. ~~Duplicados-por-copia baratos por hash~~ — **YA HECHO** (ver 2.5).
2. ~~Módulos de la Diplomatura UTN (16 archivos)~~ — **CERRADO en v15,
   ver 3.8.** Conservar los 16 completos, sin duplicados.
3. **Cadenas incrementales candidatas — LAS 5 IDENTIFICADAS EN v6/v7
   ESTÁN CERRADAS.** No quedan más cadenas de este tipo pendientes en la
   lista original — lo que sigue de 3.6 son las familias grandes sin
   agrupar como cadena (ver punto 6 más abajo) y el resto de grupos
   chicos/sueltos.
   - ~~WIKI_DOCUMENTACION~~ — **CERRADA, ver 3.6.bis.** Conservar las 3
     versiones (v1/v2/v3) — CORREGIDO EN v8, ver aviso al inicio del log
     v8.
   - ~~IRAM_hitos_metodologicos~~ — **CERRADA, ver 3.6.ter.** No era 1
     cadena de 4, sino 1 cadena de 3 (v5/v6/v7) + 1 archivo independiente
     (b44210ab) — **conservar los 4 completos** (CORREGIDO EN v8: antes
     decía conservar solo 2).
   - ~~PROMPT_MAESTRO~~ — **CERRADA, ver 3.6.quater.** Confirmado: eran 2
     familias distintas, no 1 cadena de 5. `PROMPT_MAESTRO` (v1.6/v1.8)
     → conservar ambos (sin cambios, ya era así). `IRAM_PROMPT_MAESTRO`
     (v3.8/v3.9/v5.2) → **conservar los 3** (CORREGIDO EN v8: antes decía
     conservar solo v5.2).
   - ~~SESSION_LOG_ANALISIS_C1~~ — **CERRADA en v8, ver 3.6.quinquies.**
     No había archivo "intruso": los 6 archivos (v1 sin sufijo, v2,
     v2(2), v3, v4, v5) son una única cadena secuencial confirmada por
     diff/contenido. **Conservar los 6 completos.**
   - ~~TECHNICAL_WIKI ACTIVE/ARCHIVE~~ — **CERRADA CON SALVEDAD en esta
     sesión (v9), ver 3.6.sexies.** Sistema de vasos comunicantes real
     entre ACTIVE y ARCHIVE, no dos cadenas paralelas independientes.
     **Conservar los 6 completos** (mismo criterio que el resto), pero
     con 3 bloques de contenido puntual sin correlato confirmado en
     ningún archivo del set (tabla de thresholds por tipo de territory,
     datos crudos de mapa, Sección 20/21.1) — evidencia mixta, no
     forzada, dejada asentada tal cual.
   - ~~SESSION_LOG_DOCUMENTACION~~ (35 archivos) — **CERRADA en v12,
     ver 3.6.septies.** Familia grande de 3.6, no una de las 5 cadenas
     originales del punto 3. **Conservar los 35 completos.** Incluye 2
     bifurcaciones reales sin resolución de orden posible (sesión 11 y
     19 — 4 archivos) y verificación de que 2 saltos con caída de
     tamaño (s7→s8, s9→s10) son migración de contenido a documentos de
     destino (SKILL v1.0, paper), no pérdida.
   - ~~SESSION_LOG_REPLANTEO~~ (19 archivos) — **CERRADA en v13, ver
     3.6.octies.** Familia grande de 3.6, no una de las 5 cadenas
     originales, distinta de SESSION_LOG_DOCUMENTACION pese al nombre
     parecido. **Conservar los 19 completos.** Cadena con puntos de
     ramificación por checkpoints intra-sesión (2 grupos, 6 y 3
     archivos citando al mismo predecesor cada uno) confirmados como
     progresión real, no bifurcación. Hallazgo nuevo: 6 archivos
     estaban en la carpeta `_CUARENTENA_DUPLICADOS` del propio proyecto
     sin ser duplicados reales — falso positivo de clasificación por
     carpeta, verificado y descartado.
   #### 3.6.septies — CERRADA EN ESTA SESIÓN (v12): familia
   `SESSION_LOG_DOCUMENTACION` (35 archivos)

   **Esta es una familia grande de 3.6, NO una de las 5 cadenas
   incrementales ya cerradas del punto 3 — no confundir con
   `SESSION_LOG_ANALISIS_C1` (esa sí cerrada, ver 3.6.quinquies, nombre
   parecido pero familia distinta).** Sin cerrar todavía; se completó
   solo una parte del trabajo.

   **Método usado para ordenar la cadena:** los propios documentos
   declaran número de sesión y a qué archivo "reemplazan" en su
   encabezado — se usó eso para reconstruir el orden real, no el nombre
   de archivo ni la fecha del sistema (que en varios casos coincide
   fecha entre archivos de sesiones distintas). Se hizo grep de
   "sesión [0-9]+" sobre los 35 archivos para detectar colisiones de
   número (candidatas a duplicado o bifurcación real) antes de seguir
   con el resto de la cadena.

   **Colisiones de número de sesión detectadas y resueltas:**

   - **Sesión 11** (`..._CONSOLIDADO_s_bbed7ca9.md` 194 líneas vs.
     `..._CONSOLIDADO_s_dcdc70a1.md` 144 líneas, ambos fechados
     2026-06-12, ambos declarando "reemplaza s10"): **NO es duplicado ni
     superset — es una bifurcación real.** Confirmado por diff completo:
     narran dos estados incompatibles del mismo checkpoint. Uno afirma
     que C1 y C2 quedaron completos ("Producto 2 cerrado... proyecto
     documentado en su totalidad"); el otro afirma que solo C1 quedó
     completo, con 2 gaps identificados y C2 explícitamente pendiente
     ("Producto 2: C1 ✅, C2 pendiente"). Coherente con el patrón ya
     visto en el log de múltiples cortes de sesión reconstruidos por
     separado desde transcripts distintos. **No hay forma de determinar
     cuál es cronológicamente posterior — no se descarta ninguno, se
     conservan los 2 como bifurcación documentada.**

   - **Sesión 19** (`..._CONSOLIDADO_s_6713bc7f.md` vs.
     `..._CONSOLIDADO_s_a4a8ae44.md`, ambos 439 líneas, mismo pie de
     página estructural): **misma situación — bifurcación real, no
     duplicado.** Reinterpretación incompatible sobre el rol de
     `IRAM_SKILL_desarrollo_con_IA v1.0` en el nuevo C1: uno lo marca
     "⚠️ SUPERADO EN S18" (ya no es base estructural, solo consulta
     puntual de hechos/ejemplos), el otro lo mantiene como "fuente
     principal del nuevo C1 (~80%)", a subir como input de arranque.
     `6713bc7f` contiene una entrada tachada que cita textualmente la
     postura del otro archivo como versión vieja, lo que sugeriría que
     `6713bc7f` es posterior — pero no hay marcador de fecha/hora
     independiente que lo confirme, así que se deja como evidencia
     mixta y **se conservan los 2**, sin afirmar orden causal.

   - **Sesión 13** (`..._CONSOLIDADO_s_cc9f2ef3.md` 205 líneas vs.
     `..._CONSOLIDADO_s_ed07520a.md` 221 líneas): a diferencia de los
     dos casos anteriores, **acá SÍ hay relación de superset con
     reescritura** — `ed07520a` se declara en su propio pie como
     "sesión 13 — cierre" y "Reconstruido de transcript (failed.md)",
     y expande contenido de `cc9f2ef3` (mapeo más detallado contra
     módulos/unidades de la diplomatura UTN, tabla nueva de "lo que
     falta aprender genuinamente"). Verificado por grep dirigido que
     los conceptos clave de `cc9f2ef3` (backup/PROMPT como hito
     fundacional, árbitro claro, etc.) sobreviven en `ed07520a`. **Pero
     hay un bloque puntual que no tiene correlato explícito:** la
     entrada de tabla R14 de `cc9f2ef3` con el detalle narrativo de los
     3 hallazgos de "sesión 12" se colapsa en `ed07520a` a una línea de
     resumen ("### R14 (sesiones 1–12) — ver log anterior"), y se
     confirmó que ese detalle tampoco reaparece en el siguiente archivo
     de la cadena (`9dc1e576`, sesión 14), que solo repite el estado
     final ("Estado al cierre de s12: C1 para reescribir") sin los 3
     hallazgos en sí. **Mismo patrón que 3.6.quater — evidencia mixta,
     no forzada.** Se conservan los 2, sin descartar ninguno.

   - **Falsos positivos de la búsqueda por número de sesión** (NO son
     colisiones reales, verificado antes de perder tiempo comparándolos
     como cadena): `SESSION_LOG_DOCUMENTACION_2026-06-10_22-30_1__ab3f29e4.md`
     (grep capturó "sesión 16:55", una **hora**, no un número de sesión;
     es de fecha 2026-06-10, muy anterior a la verdadera sesión 16) y
     `SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO__ee6e238d.md`
     (grep capturó "sesión 18:50", también hora). Ninguno de los 2 forma
     par con otro archivo — quedan como parte normal de la cadena
     secuencial, a revisar en su lugar cronológico correcto cuando se
     retome el resto.

   **Cadena principal `CONSOLIDADO` (s5 suelto → s6 → s7 → s8 → s9 →
   s10 → s11* → ... ; *s11 es la bifurcación ya documentada arriba):**

   - `SESSION_LOG_DOCUMENTACION_2026-06-12__357b9d52.md` — **verificado
     completo antes de asumir** (regla de 3.6.ter): es el ancestro
     genuino de la cadena, no un intruso de naturaleza distinta. Es
     literalmente el archivo `SESSION_LOG_DOCUMENTACION_2026-06-12.md`
     que `a4a61d06` (s6) declara reemplazar por nombre exacto en su
     propio encabezado. Tipo "Plantilla A", 104 líneas, previo a la
     reestructuración a formato "CONSOLIDADO".
   - **s5→s6→s7:** reestructuración de formato ("qué se hizo" →
     "estado consolidado") sin pérdida — confirmado por diff, el
     contenido de s5 se resume pero los hallazgos clave persisten
     inline en s6/s7.
   - **s7→s8 (168→138 líneas, caída de tamaño):** verificado con
     cuidado por la caída de tamaño. **NO es pérdida.** El bloque largo
     "GAPS IDENTIFICADOS — PLANTILLA B" y "MARCO TEÓRICO — ESTADO
     COMPLETO" de s7 se colapsan en s8 a referencias tipo "Sección 5
     del SKILL", "Sección 6 del SKILL" — se verificó por grep dirigido
     contra `IRAM_SKILL_desarrollo_con_IA_v1_0.md` (presente en el set)
     que los conceptos sustantivos (arquitectura de contexto,
     scripted_gui, scopes globales, ruler={}, INSTRUCCIONES_HUMANO,
     especificación ejecutable) sí están en el documento de destino
     real, no solo referenciados en el aire. **Superset funcional
     confirmado, con migración de contenido de "inline en el log" a
     "en el documento final".**
   - **s8→s9→s10:** superset limpio, sin hallazgos que requieran nota
     — el reencuadre de estado del SKILL v1.0 (de "entregable final" a
     "borrador del paper") se propaga sin pérdida de historial.
   - **Excepción puntual en s9→s10:** la entrada R14 de "sesión 8" en s9
     (3 hallazgos: recuperación tras crash, resolución de Ángulo 12,
     "quinta pieza" vs "cuarta capa") se colapsa en s10 a "### R14
     (sesiones 1–9) — [sin cambios]. Ver SESSION_LOG s9." Verificado por
     grep que el contenido conceptual sobrevive en `IRAM_paper_
     metodologia_v1_0.md` y en el SKILL v1.0 — **no es pérdida real**,
     mismo patrón de migración que s7→s8.

   **Serie `s22` a `s34` (13 archivos, "spec ejecutable", patrón
   distinto a `CONSOLIDADO` — cada uno reemplaza al inmediato anterior
   uno a uno, con pie de página que declara explícitamente "Cambios
   respecto a sXX: ..."):**

   - Cadena secuencial simple confirmada, sin bifurcaciones. Tamaños
     189→118 líneas (tendencia decreciente por colapso de detalle
     operativo ya ejecutado — TAREAs cerradas se resumen para dar lugar
     a la tarea siguiente), estabilizándose alrededor de ~120 líneas
     desde s26 en adelante.
   - **Verificación de cierre:** se confirmó que las 18 decisiones
     (DEC-01 a DEC-18) generadas a lo largo de la cadena siguen
     presentes textualmente en el archivo final (`s34`), que además
     documenta el cierre completo del proyecto hasta DEC-30 ("proyecto
     cerrado sin deuda residual"). No se detectó ningún concepto que
     desaparezca sin dejar rastro en el archivo final.
   - No se requirió abrir nota de evidencia mixta en esta serie — el
     propio formato (pie de página con changelog explícito por sesión)
     facilita la verificación y no dejó casos ambiguos.

   **RESULTADO FINAL — familia `SESSION_LOG_DOCUMENTACION` (35
   archivos): se conservan los 35 completos.** Ninguno resultó
   duplicado exacto por hash normalizado. Incluye las 2 bifurcaciones
   documentadas arriba (sesión 11 y sesión 19 — 4 archivos que no se
   pueden ordenar causalmente entre sí) y 2 casos de migración de
   contenido verificada sin pérdida (s7→s8, s9→s10) — ningún archivo se
   descarta por ninguno de estos motivos, siguiendo el criterio de v8.

   Mismo método de diff estructural que funcionó en 2.2, 2.4.b, 2.4.c,
   2.5.b, 3.6.bis, 3.6.ter, 3.6.quater, 3.6.quinquies, 3.6.sexies y (en
   curso) 3.6.septies: **normalizar CRLF antes de comparar, no asumir que la
   versión/fecha más alta es superset hasta confirmarlo por diff, no
   asumir que un archivo "suelto"/sin sufijo de versión pertenece a la
   cadena solo por compartir fecha o tema — leerlo primero —, tener
   presente que un superset puede no ser 100% confirmable (ver casos
   PROMPT_MAESTRO v1.6/v1.8 y TECHNICAL_WIKI ACTIVE/ARCHIVE): si queda
   un bloque con evidencia mixta/no concluyente, no forzar la conclusión
   de "superset" y dejarlo asentado explícitamente — y, desde v8, tener
   presente el criterio corregido: el diff/superset se usa para
   confirmar que no hay pérdida de contenido, NO como justificación para
   descartar versiones. Solo se descarta lo que sea duplicado exacto por
   hash normalizado. Y, nuevo de esta sesión (v9): en cadenas
   ACTIVE/ARCHIVE (documento operativo + histórico), cruzar lo que
   desaparece de uno contra el otro antes de concluir — no alcanza con
   diffear una serie contra sí misma.**
4. **`FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md`** — resolver primero si es
   la familia ya cerrada (2.2) con nombre corrupto. **Sigue pendiente,
   no se tocó en v9** — se priorizó cerrar la cadena TECHNICAL_WIKI
   primero, como pedía la prioridad sugerida de v8.
5. El resto de sueltos sin familia — revisión individual, bajo volumen.
6. **Ya no quedan familias grandes de 3.6 sin tocar, y ya no quedan
   grupos chicos/pares de 3.6 sin tocar (CERRADO EN v18/v19).**
   SESSION_LOG_ANALISIS_C1, TECHNICAL_WIKI ACTIVE/ARCHIVE,
   SESSION_LOG_DOCUMENTACION, SESSION_LOG_REPLANTEO, IRAM_C1,
   SESSION_LOG_AUDITORIA_CONTINUIDAD, IRAM_analisis_cuantitativo,
   IRAM_SESSION_LOG y PROMPT_DOCUMENTACION_IRAM_v1 — resueltos en
   3.6.quinquies, 3.6.sexies, 3.6.septies, 3.6.octies, 3.6.novies,
   3.6.decies, 3.6.undecies, 3.6.duodecies y 3.6.terdecies
   respectivamente. Los 7 grupos chicos/pares que quedaban (crítica,
   PASO_0, bloque3_analysis, spec_c_zip_history, Etapa1/Etapa2,
   Consigna y `sesion cortada.md`/transcripciones) — resueltos en
   3.6.quaterdecies (v18) y 3.6.quindecies (v19).
7. **Nueva en v22 — cadena SESSION_LOG_DOCUMENTACION s19→s20→s21→s22**,
   destapada de forma lateral al aclarar el bloque de "archivos no
   mapeados" del chat anterior (ver 2.8). **Resuelta y CERRADA en esta
   sesión — ver 3.6.sedecies.**

### 3.6.sedecies — CERRADA EN v22: cadena SESSION_LOG_DOCUMENTACION s19→s20→s21→s22

Continuación directa de la sección (d) del addon anterior. Se completó el
diff de toda la cadena, incluyendo un eslabón adicional no previsto
(`s19` tenía dos versiones, no una) y un archivo `s18` citado por todos
como predecesor pero ausente del índice.

#### Universo verificado

| Archivo | Bytes | Hash (8) | Estado |
|---|---|---|---|
| `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` | — | — | **No está en el índice de 274.** Citado como predecesor por s19(2), s19(sin sufijo) y s20 por igual. Puede estar perdido o no haber sido copiado — no confundir con "no existió". |
| `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19.md` (sin sufijo) | 37279 | a4a8ae44 | Versión anterior de s19, framing de SKILL v1.0 sin corregir |
| `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19 (2).md` | 37827 | 6713bc7f | Versión posterior de s19, con corrección "SUPERADO EN S18" propagada |
| `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s20.md` | 9859 | 4ffdec70 | Ya extraído/leído en este addon |
| `SESSION_LOG_DOCUMENTACION_2026-06-17_ESPECIAL_s21.md` | 13278 | b37f6b19 | Ya extraído/leído en este addon |
| `SESSION_LOG_DOCUMENTACION_s22.md` | 11382 | 8b58c287 | Ya extraído/leído en este addon |

Ninguno de los 6 nombres tenía sección propia en el log antes de este
addon. `s18` queda marcado como pendiente de ubicar (posible pérdida real,
no solo alcance no revisado).

#### a) `s19` (sin sufijo) vs `s19 (2)` — CERRADO

- **No son duplicado exacto** ni con normalización CRLF/LF (hashes
  normalizados distintos).
- Ratio de similitud 0.977 — diff de 73 líneas sobre ~439, concentrado
  en un único tipo de cambio: la corrección del criterio sobre
  `IRAM_SKILL_desarrollo_con_IA_v1_0` (de "~80% del contenido del nuevo
  C1" a "fuente de hechos y ejemplos técnicos, framing superado"),
  propagada de forma consistente en 6 puntos distintos del mismo
  documento (tabla de estado, resumen de sesión 17, decisiones clave,
  secuencia de trabajo, lista de "no eliminar").
- `s19 (2)` es la versión posterior: contiene la marca explícita
  "⚠️ SUPERADO EN S18" que `s19` (sin sufijo) no tiene, y ambas declaran
  reemplazar al mismo predecesor (`s18`), consistente con ser dos pasadas
  sucesivas sobre el mismo consolidado.
- **Bajo el criterio de v8: se conservan ambas versiones.** No hay
  pérdida de contenido semántico entre una y otra — es corrección de
  criterio propagada, mismo patrón que 3.6.bis (WIKI_DOCUMENTACION v2→v3).

#### b) `s19 (2)` vs `s20` — CERRADO, con hallazgo de pérdida real documentado por el propio proyecto

- Ratio bajo (0.27, 439 vs 148 líneas) — pero **no es evidencia de
  independencia** como en otros casos de ratio bajo del log (ver regla
  de v19): acá el propio `s20` declara remitir a `s19` para varias
  secciones completas ("Sesiones 1–19 — sin cambios desde s19, ver
  SESSION_LOG s19 para detalle completo", ídem con "Decisiones clave" y
  "Marco conceptual — sin cambios desde s19"). Es decir, `s20` es un
  documento operativo más liviano por diseño, que delega el histórico en
  `s19` en vez de reescribirlo — mismo patrón ACTIVE/ARCHIVE que la regla
  de v9 (3.6.sexies) advierte que hay que cruzar, no descartar por ratio.
- **Hallazgo importante — no es una inferencia mía, está documentado
  textualmente por el propio proyecto en `s21`:** la sección "CONTENIDO
  PERDIDO EN EL PASAJE s19 → s20" de `s21` confirma que la delegación NO
  funcionó como se pretendía. `s20` sí perdió contenido real de `s19`
  que no quedó ni resumido ni referenciado en ningún lugar recuperable:
  la advertencia "SUPERADO EN S18" sobre el SKILL v1.0 (la celda de la
  tabla fue reescrita limpia, sin la nota inline), la tabla completa
  "MAPPING CORRECCIONES S18 → EVIDENCIA PRIMARIA S19" (9 filas), 4
  hallazgos materiales de fuentes primarias, y los 3 ajustes al esqueleto
  identificados en s18.
- **Conclusión: `s20` NO es superset de `s19` — es una pérdida de
  contenido real, detectada y corregida por el propio proyecto en el
  siguiente eslabón (`s21`).** Bajo el criterio de v8, esto no cambia qué
  se conserva (las 4 versiones de todas formas se rescatan íntegras),
  pero sí es un caso de "evidencia de pérdida real" a diferencia de
  TECHNICAL_WIKI (v9, evidencia mixta) — acá la pérdida está confirmada
  explícitamente por el propio texto del proyecto, no inferida por diff.

#### c) `s20`+`s19(2)` vs `s21` vs `s22` — CERRADO

- Ratios bajos y parejos entre los tres (0.24–0.25) — cada eslabón es
  reescritura sustancial, consistente con que los tres se declaran
  "spec ejecutable para la próxima IA, no registro histórico" y cada uno
  reemplaza operativamente al anterior en vez de acumular contenido.
- `s21` es el eslabón más denso: diagnostica la causa raíz de la pérdida
  s19→s20 (8 problemas estructurales del propio sistema de
  documentación, P1–P8), recupera explícitamente el `MAPPING CORRECCIONES
  S18→S19` y los 3 ajustes al esqueleto perdidos en s20, y dos opciones
  para la sesión siguiente (Opción A: corregir el sistema antes / Opción
  B: draftear y corregir después) — se adoptó la Opción B.
- `s22` ejecuta las correcciones diagnosticadas en `s21`: formaliza
  `DECISIONES CONFIRMADAS` (DEC-01 a DEC-12, heredadas de `s21` sin
  pérdida — verificado punto por punto, coinciden), agrega un
  `PROTOCOLO DE LA IA EJECUTORA` de 7 pasos (ausente en `s21`), reorganiza
  las tareas pendientes con una `TAREA 0 — URGENTE` nueva (auditoría de
  fuentes de documentación, para no repetir la pérdida s19→s20), y
  preserva íntegro el `MATERIAL S4` (mapping + notas por subsección) que
  `s21` había recuperado.
- **`s22` sí es superset funcional confirmado de `s21`** (mismo patrón
  que WIKI_DOCUMENTACION v2→v3): todo el contenido operativo de `s21`
  reaparece en `s22`, igual o expandido (protocolo nuevo, tarea 0 nueva),
  sin pérdidas detectadas en esta pasada. A diferencia del caso s19→s20,
  acá no hay contenido de `s21` ausente en `s22`.
- **Bajo el criterio de v8: se conservan los 3 (`s20`, `s21`, `s22`)
  íntegros**, como estados históricos reales de una corrección de
  sistema en marcha — aunque `s22` sea funcionalmente completo respecto
  de `s21`, ambos documentan un momento distinto del diagnóstico/cierre.

#### Conclusión de la cadena completa (6 eslabones: s18–s22, 5 archivos localizados)

**Se conservan los 5 archivos localizados** (`s19` x2, `s20`, `s21`,
`s22`) **íntegros, sin descartes**, bajo el criterio de v8. El caso tiene
valor documental adicional más allá de la simple trazabilidad: es un
ejemplo real, dentro del propio corpus del proyecto, del patrón que la
auditoría general está diseñada para detectar — pérdida de contenido en
una transición de versión que el propio proyecto identificó, diagnosticó
y corrigió explícitamente, con el registro de las 3 etapas conservado
completo. Es meta-evidencia directa a favor del criterio de v8 (conservar
cadenas completas, no solo el estado final).

**Pendiente:** ubicar `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md`
en el resto del material no indexado (no está en los 274 ni en los 861
de `\game\`) — puede ser una pérdida real y definitiva, coherente con el
propio diagnóstico de `s21` sobre fallas de continuidad del sistema de
documentación en ese tramo del proyecto.

**Con este cierre, la sección 3.6 sigue sin pendientes propios** (los 16
grupos/familias/cadenas listados arriba + 3.6.sedecies, todos cerrados).
Al momento de escribir esto (v22), lo que seguía del proyecto estaba en
3.2 [ya cerrada en v20, ver 2.6], 3.3 [ya cerrada en v21, ver 2.7], 3.4 y
3.9 (entonces sin tocar). **Actualización de v23: 3.4 ya se cerró casi
por completo y 3.9 perdió uno de sus 3 ítems — ver 2.9.** Sigue sin
tocar el suelto `FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md` (punto 4 arriba),
y el suelto `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md`
(citado por toda la cadena de 3.6.sedecies como predecesor, no localizado
en los 274 — ver nota al final de 3.6.sedecies).

### 3.7 — Descartado, confirmado sin valor (no revisar)
- `wiki_imperator.txt` (3.8 MB) — wiki del juego base, no del desarrollo.
- Los 861 archivos bajo `\game\` (ya excluidos de `filtrado_final`).

**CORREGIDO EN v8:** `IRAM_Diseñador1_Historial.md` (cruda, 2.4.a) y
`IRAM_HISTORIA_COMPLETA_v1_1.md` (2.4.b) **ya NO están descartados** —
bajo el nuevo criterio (ver corrección de criterio al inicio del log)
son estados históricos a conservar, no duplicados verdaderos. Ver
conclusiones corregidas en 2.4.a/2.4.b más arriba. Esta sección queda
vacía de contenido real salvo `wiki_imperator.txt` y los 861 de `\game\`.

### 3.8 — Confirmado a rescatar (ambos/todos, no elegir solo uno)
- `IRAM_Diseñador1_Historial_LIMPIO.md`
- `IRAM_HISTORIA_COMPLETA_v1_2 (2).md`
- `IRAM_PROYECTO_REORGANIZADO_05-07-2026.md` **y**
  `IRAM_PROYECTO_REORGANIZADO_06-07-2026.md` (los dos, ver 2.4.c)
- `IRAM_SUPERBACKUP_v2_1.md` — **RESUELTO Y DESCARTADO EN v23 (ver
  2.9.a):** verificado como prefijo textual exacto de `SESION
  TRUNCADA.md` (3.4). Se conserva `SESION TRUNCADA.md` en su lugar por
  ser la versión más completa. Ya no figura como pendiente.
- **NUEVO EN ESTA SESIÓN:**
  - 14 de los 15 README (`README__24f01116`, `README _2__51624c6c`,
    `README__a43e8472`, `README__aeb968a3`, `README__a49cf6f0`,
    `README__6cb65402`, `README__fe636653`, `README__7efad22a` [=
    `README__cc62dfe9`, colapsar a 1], `README__d3825435`,
    `README__63be8f4a`, `README__1345e96c`, `README__2431e000`,
    `README__363d177c`, `README _2__561fa847`) — ver 2.5.a.
  - 3 de los 4 INDICE (`INDICE__25c3aac9`, `INDICE__877446a8` [=
    `INDICE__df6ac725`, colapsar a 1], `INDICE _2__09199357`) — ver
    2.5.b.
  - `IRAM_paper_metodologia_v1_0.md` (128e4c6c) **y**
    `IRAM_paper_metodologia_v1_0(1).md` (2658a8be) — los dos, ver 2.5.c.
  - `IRAM_skill_desarrollo_ia_v2_0.md` (4d388c49) **y**
    `IRAM_skill_desarrollo_ia_v2_0 (3).md` (e6874d63) — los dos, ver
    2.5.d.
- **NUEVO EN v15:**
  - Los 16 módulos `Modulo*_Unidad*` de la Diplomatura UTN —
    `Modulo1_Unidad1_Que_es_Ciencia_de_Datos__f30a1038.md`,
    `Modulo1_Unidad2_Pensar_con_Datos__927a43d2.md`,
    `Modulo1_Unidad3_Tipos_de_Datos__1077b919.md`,
    `Modulo1_Unidad4_Proceso_del_Cientista_de_Datos__cbfd0354.md`,
    `Modulo2_Unidad1_Herramientas_Basicas_Analisis_Dato__b154fb19.md`,
    `Modulo2_Unidad2_Limpieza_de_Datos__97539f79.md`,
    `Modulo2_Unidad3_Analisis_Exploratorio_EDA__d19759b0.md`,
    `Modulo2_Unidad4_Visualizacion_de_Datos__32320185.md`,
    `Modulo3_Unidad1_Que_es_la_IA__8884e36a.md`,
    `Modulo3_Unidad2_Que_es_Machine_Learning__8340dd75.md`,
    `Modulo3_Unidad3_Algoritmos_Clave_ML__8e6c010e.md`,
    `Modulo3_Unidad4_IA_Aplicada_Vida_Diaria__94614aed.md`,
    `Modulo4_Unidad1_ChatGPT_Modelos_Generativos__77bb0602.md`,
    `Modulo4_Unidad2_Automatizacion_NoCode_LowCode__ea1758d5.md`,
    `Modulo4_Unidad3_Introduccion_NLP__530a2742.md`,
    `Modulo4_Unidad4_Vision_por_Computadora__571b1095.md` — los 16
    completos. **Cerrado sin salvedad.** Grilla Módulo 1–4 × Unidad 1–4
    completa sin huecos, 16 hashes SHA-256 distintos entre sí (sin
    duplicados), cada uno con `cantidad_lugares_donde_aparece = 1` en
    el índice, y título de Módulo/Unidad dentro del contenido
    verificado igual al nombre de archivo en los 16 casos. No requirió
    diff entre ellos (no son una cadena de versiones, son 16 unidades
    de contenido distinto por diseño curricular).
- **NUEVO EN v9:**
  - Los 6 de `TECHNICAL_WIKI ACTIVE/ARCHIVE` (`ACTIVE_v3_1__de396c3d`,
    `ACTIVE_v3_2__33961f73`, `ACTIVE_v3_10 _2__8d7a77a5`,
    `ARCHIVE_v3_1__39b9e7ef`, `ARCHIVE_v3_2__a90e9773`,
    `ARCHIVE_v3_7 _2__9a276d30`) — los 6 completos, ver 3.6.sexies.
    **Cerrado con salvedad** — hay 3 bloques de contenido puntual sin
    correlato confirmado en el set (ver detalle en 3.6.sexies), pero eso
    no cambia la decisión de rescatar los 6 bajo el criterio de v8.

### 3.9 — **CERRADA POR COMPLETO EN v25 (ver 2.11)**
- `IRAM_SUPERBACKUP_v2_1.md` — descartado en v23 (ver 2.9.a), prefijo
  textual exacto de `SESION TRUNCADA.md`.
- `IRAM_Historial_Unificado_v2.md` (957767 bytes) — conservado, ver
  2.11. Índice-resumen ejecutivo por Agente, 135 sesiones, 09/04→16/05.
- `IRAM_historial_unificado_2026-06-12.md` (3795153 bytes) — conservado,
  ver 2.11. Extracción cruda por cuenta de Claude, 441 conversaciones,
  22/10/2025→10/06/2026. No es duplicado ni superset de `v2` pese al
  nombre parecido — dos niveles de granularidad distintos sobre el
  mismo material fuente, verificado por comparación de contenido real
  (no solo por el ratio global de similitud).

## 4. ARCHIVOS QUE HAY QUE SUBIR EN EL PRÓXIMO CHAT

1. **Este log actualizado** (`LOG_CONTINUIDAD_IRAM_2026-07-10_v25.md`).
2. **`_indice_copiados.csv`** (rutas originales y hashes) — sin cambios
   respecto a v3 hasta v25, sigue siendo el mismo archivo.
3. **`candidatos_valiosos.zip`** completo — con las 5 cadenas
   incrementales originales del punto 3, más SESSION_LOG_DOCUMENTACION
   (3.6.septies), SESSION_LOG_REPLANTEO (3.6.octies), IRAM_C1
   (3.6.novies), los 16 módulos UTN (ver 3.8), las 4 familias grandes
   cerradas en v16 (SESSION_LOG_AUDITORIA_CONTINUIDAD (3.6.decies),
   IRAM_analisis_cuantitativo (3.6.undecies), IRAM_SESSION_LOG
   (3.6.duodecies), PROMPT_DOCUMENTACION_IRAM_v1 (3.6.terdecies)), los
   7 grupos chicos/pares que quedaban de 3.6, cerrados entre v18 y v19
   (3.6.quaterdecies y 3.6.quindecies), la familia "gap" de 7 archivos,
   cerrada en v20 (ver 2.6), las 6 charlas sueltas (charla_7 a
   charla_12), cerradas en v21 (ver 2.7), la
   aclaración del bloque de "no mapeados" (ver 2.8) y la cadena
   SESSION_LOG_DOCUMENTACION s19→s20→s21→s22, cerradas en v22
   (ver 3.6.sedecies), **la sección 3.4 completa (los 5 archivos,
   incluido el último ítem `fallo DOCUMENTACION 19-06-2026.md`,
   cerrados en v23/v24, ver 2.9/2.9.c), la familia
   `FUENTE_DE_VERDAD_IRAM_2026-07-07` completa (11 archivos, no 1
   suelto como se creía — cerrada en v25, ver 2.10), y la sección 3.9
   completa (sus 3 archivos, el último resuelto en v23 y los 2
   restantes cerrados en v25, ver 2.11).**

   **Con esto, de las secciones numeradas grandes de auditoría (3.2 a
   3.9) no queda ninguna abierta.** Lo que sigue son piezas sueltas más
   chicas, listadas en el punto 4 de abajo. Si el próximo chat va a
   enfocarse en una sola de esas piezas, alcanza con adjuntar ese
   archivo suelto en vez del zip entero — pero como quedan varias por
   recorrer y una tarea estructural nueva (ver ítem 4), lo más práctico
   sigue siendo el zip completo.
4. Para retomar lo que sigue, ahora que 3.2 a 3.9 están completas:
   - **⚠️ RECONCILIAR 2.2 vs 2.10 (contradicción detectada dentro del
     propio log en esta sesión, ver nota al final de 2.10):** 2.2 (vieja)
     dice que la familia `FUENTE_DE_VERDAD_IRAM_2026-07-07*` tiene 12
     versiones y que `base` es prefijo textual exacto de `_11`; 2.10
     (v25) encontró 11 archivos físicos y no verificó el substring
     extremo a extremo. No cambia el veredicto (conservar todo), pero
     hay que decidir cuál cuenta es la correcta antes de citar esta
     familia como "cerrada sin ambigüedad" en el futuro.
   - `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` (citado
     como predecesor por toda la cadena s19→s22 pero no localizado en
     los 274 archivos indexados — buscar primero en el resto de
     material no indexado o en backups fuera de este zip antes de
     concluir que es una pérdida real y definitiva.)
   - **Los 7 archivos ya identificados pero aún sin revisión individual**
     de la lista "Otros sueltos sin familia clara" (línea ~1078 del
     cuerpo del log): `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md`,
     `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md`, `Qwen_markdown_20260705_q4xkzeqjf (2).md`,
     `memoria_claude_volcado.md`, `volcado_memoria (2).md`,
     `LOG_REORGANIZACION_2026-07-05.md`, `resultado_prueba_fuga_memoria.md`,
     `sigue log.md` (más el resto de la lista original) — no son
     urgentes, pero conviene sumarlos a la próxima pasada de "sueltos".
   - **TAREA ESTRUCTURAL NUEVA, distinta a las anteriores (surgida de
     §17/§18 de `FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11`, ver 2.10):**
     el árbol definitivo de documentación del proyecto, declarado por
     el propio operador como tarea prioritaria #1 (por encima de
     DR-54). No es una comparación de archivos más — es decidir la
     estructura final de carpetas y dónde vive cada cosa, con estos
     problemas ya verificados y pendientes de resolver:
       a) `SESSION_LOG_REPLANTEO_*` vive **duplicado** en el zip: 15
          copias organizadas en `2_DOCUMENTACION/01_logs_replanteo/` +
          13 sueltas en la raíz del zip, fuera de toda carpeta.
       b) Otros 33 archivos de trabajo (planes viejos, volcados de
          memoria, charlas 1-6, versiones viejas de esta misma fuente
          de verdad) tampoco están en ninguna carpeta del árbol
          reorganizado.
       c) `_CUARENTENA_DUPLICADOS/` tiene 544 archivos en dos subcopias
          anidadas casi completas del proyecto — destino nunca
          decidido (tarea #10 de §5 de la propia fuente de verdad,
          abierta desde su versión `_2`).
       d) Precisión del operador (§18): el árbol final debe ser legible
          y navegable específicamente para **instancias de IA simples y
          tareas cortas**, no solo para sesiones largas de
          reconstrucción como esta cadena de auditoría.
     Esta tarea es de **diseño y decisión**, no de verificación por
     diff/hash como el resto del log — conviene decidir junto al
     usuario si se aborda antes o después de terminar los sueltos
     menores del punto anterior.

**No hace falta re-subir ni re-verificar nada de lo ya cerrado en la
sección 2 (2.1 a 2.8) ni las cadenas/familias ya cerradas:
WIKI_DOCUMENTACION (3.6.bis), IRAM_hitos_metodologicos (3.6.ter),
PROMPT_MAESTRO (3.6.quater), SESSION_LOG_ANALISIS_C1 (3.6.quinquies),
TECHNICAL_WIKI ACTIVE/ARCHIVE (3.6.sexies), SESSION_LOG_DOCUMENTACION
(3.6.septies), SESSION_LOG_REPLANTEO (3.6.octies), IRAM_C1
(3.6.novies), los 16 módulos UTN (ver 3.8, cerrado en v15),
SESSION_LOG_AUDITORIA_CONTINUIDAD (3.6.decies), IRAM_analisis_cuantitativo
(3.6.undecies), IRAM_SESSION_LOG (3.6.duodecies), PROMPT_DOCUMENTACION_IRAM_v1
(3.6.terdecies, todas cerradas en v16), los 6 grupos chicos re-verificados
en v18 (3.6.quaterdecies: crítica, PASO_0, bloque3_analysis,
spec_c_zip_history, Etapa1/Etapa2, Consigna) ni el último sub-grupo
cerrado en v19 (3.6.quindecies: `sesion cortada.md` y las transcripciones
de SESSION_LOG_CONSOLIDADO), ni la familia "gap" cerrada en v20 (2.6),
ni las 6 charlas cerradas en v21 (2.7), ni la cadena
SESSION_LOG_DOCUMENTACION s19→s22 cerrada en v22 (3.6.sedecies) — son
conclusiones firmes, confirmadas por diff/hash/similitud real, no
hipótesis. Hay excepciones parciales, todas ya señaladas con evidencia
mixta, no forzada:**
- **`PROMPT_MAESTRO` v1.6/v1.8 dentro de 3.6.quater:** la conclusión de
  "conservar ambos" es firme por razones propias (no por el criterio de
  trazabilidad), pero si en algún momento se quiere intentar reducir a 1
  solo archivo, haría falta releer ese caso puntual (no todo
  3.6.quater).
- **`TECHNICAL_WIKI ACTIVE/ARCHIVE` dentro de 3.6.sexies (v9):** la
  decisión de "conservar los 6 completos" es firme (mismo criterio de
  v8 que el resto), pero queda registrado que 3 bloques de contenido
  puntual (tabla de thresholds por tipo de territory, datos crudos de
  mapa, Sección 20/21.1 del ACTIVE) no tienen correlato confirmado en
  ninguno de los 6 archivos del set. Si en el futuro se quiere intentar
  recuperar ese detalle específico, haría falta buscarlo en otras
  copias de seguridad no incluidas en este set de 274 — no se investigó
  más en esta sesión.
- **`SESSION_LOG_DOCUMENTACION` dentro de 3.6.septies (v12):** la
  decisión de "conservar los 35 completos" es firme, pero quedan 2
  bifurcaciones reales sin poder determinar cuál es cronológicamente
  posterior (sesión 11: 194 vs 144 líneas, narran estados
  incompatibles del checkpoint; sesión 19: reinterpretación
  incompatible sobre el rol del SKILL v1.0) — si en algún momento
  aparece evidencia externa (metadata de archivo, timestamp de sistema
  de un backup no incluido en este set) que permita ordenar alguno de
  los 2 pares, se podría cerrar esa ambigüedad puntual, pero no hace
  falta para el uso normal del material. **Nota agregada en v16:** la
  bifurcación de la sesión 19 sobre el rol del SKILL v1.0 tiene ahora
  contexto adicional gracias a `PROMPT_DOCUMENTACION_IRAM_v1_9(3)` (ver
  3.6.terdecies) — ese documento es la fuente textual donde se decide
  formalmente separar el SKILL.md único en dos productos (C1 paper /
  C2 skill operacional). No resuelve la bifurcación de la sesión 19 en
  sí, pero da la causa de fondo del cambio de interpretación.
- **`SESSION_LOG_REPLANTEO` dentro de 3.6.octies (v13):** la decisión
  de "conservar los 19 completos" es firme y no quedó ningún caso de
  evidencia mixta sin resolver (a diferencia de las excepciones
  anteriores) — el único punto a tener presente es que 6 de los 19
  estaban en la carpeta de cuarentena del propio proyecto; si en el
  árbol final se reorganiza el material, esos 6 no deberían volver a
  colocarse en una carpeta de "duplicados" sin verificar de nuevo por
  hash/diff, ya que quedó demostrado que la etiqueta de esa carpeta no
  era confiable.
- **`IRAM_analisis_cuantitativo` dentro de 3.6.undecies (v16):** la
  decisión de "conservar los 3 completos" es firme, pero la relación
  base→v2 es de evidencia mixta (v2 corrige y revierte la conclusión de
  la base sobre el modelo de cuentas, no la complementa) — mismo patrón
  que `PROMPT_MAESTRO` v1.6/v1.8. No requiere trabajo adicional, solo
  no asumir "más nuevo = superset" si se vuelve a citar este caso.
- **`PROMPT_DOCUMENTACION_IRAM_v1` dentro de 3.6.terdecies (v16):** la
  decisión de "conservar los 5 completos" es firme. Contiene 2 saltos
  de evidencia mixta (v1_4→v1_5 y v1_5→v1_7, ambos por reescrituras
  sucesivas de la regla R18 sobre cuentas paralelas/secuenciales) — ver
  detalle completo en 3.6.terdecies si se necesita releer ese punto
  puntual.
- **Cadena SESSION_LOG_DOCUMENTACION `s19`→`s20`→`s21`→`s22` dentro de
  3.6.sedecies (v22):** la decisión de "conservar los 5 archivos
  localizados completos" es firme, pero a diferencia de las excepciones
  anteriores acá la pérdida de contenido entre `s19` y `s20` está
  **confirmada explícitamente por el propio proyecto** (el documento
  `s21` la documenta y corrige, no es una inferencia por diff de esta
  auditoría). No requiere trabajo adicional para el criterio de v8 (se
  conservan igual los 5), pero es la evidencia más fuerte del proyecto
  a favor de por qué el criterio es "conservar toda la cadena" y no
  "conservar solo la versión final". Sigue pendiente ubicar `s18`
  (predecesor citado por los 3, no localizado en los 274).

**Confirmación cruzada importante entre dos familias cerradas en v16
(no es una excepción a resolver, es un hallazgo positivo a tener
presente):** `IRAM_analisis_cuantitativo` (3.6.undecies) y
`PROMPT_DOCUMENTACION_IRAM_v1` (3.6.terdecies) narran, desde documentos
distintos, el mismo ciclo real de revisión del proyecto sobre si las 5
cuentas de Claude trabajaban en paralelo o en rotación secuencial. Las
dos llegan al mismo veredicto final (rotación secuencial, 0
interleavings en 7.313 mensajes con timestamp individual) por caminos
independientes — esto da confianza de que la conclusión final es
sólida, no un artefacto de una sola fuente.

**IMPORTANTE — criterio de descarte corregido en v8 (sigue vigente, sin
cambios en v9):** de acá en adelante, cuando se cierre una cadena de
versiones nueva, la conclusión correcta es "conservar todas las
versiones distintas, descartar solo duplicados exactos por hash
normalizado" — NO "conservar solo la versión más nueva/superset". El
trabajo de diff sigue siendo necesario (para confirmar que no hay
pérdida de contenido y detectar archivos intrusos que no son parte de la
cadena, o —nuevo en v9— relaciones cruzadas entre series ACTIVE/ARCHIVE),
pero ya no determina qué se descarta.

**Nota operativa importante (confirmada de nuevo en esta sesión):** el
entorno de trabajo (archivos descomprimidos, carpetas de análisis) NO
persiste entre sesiones/chats — solo lo que vos volvés a adjuntar. Cada
chat nuevo arranca reconstruyendo el zip desde cero. Esto no cambia qué
hay que adjuntar (ya listado arriba), pero explica por qué a veces el
primer paso del chat siguiente es "descomprimir de nuevo" aunque ya se
haya hecho antes.

---

## 5. PROMPT SUGERIDO PARA ARRANCAR EL PRÓXIMO CHAT

Copiar y pegar esto como primer mensaje, junto con los archivos de la
sección 4 adjuntos:

```
Retomo una auditoría de contenido único del repo IRAM-PROYECTO que veníamos
haciendo en otro chat. Te adjunto el log completo de continuidad
(LOG_CONTINUIDAD_IRAM_2026-07-10_v25.md), el índice de hashes
(_indice_copiados.csv) y el zip completo de candidatos
(candidatos_valiosos.zip).

**⚠️ LEÉ ESTO PRIMERO, ANTES DE ABRIR EL ZIP — filtro `\game\`:**
El zip `candidatos_valiosos.zip` tiene **1135 archivos**, pero de esos,
**861 son archivos base del videojuego Imperator Rome** (el juego sobre
el que corre el mod IRAM), identificables porque su ruta original en
`_indice_copiados.csv` (columna `ruta_original_completa`) contiene la
carpeta `\game\` (ej. `...\1_MOD\game\common\...`,
`...\1_MOD\game\events\...`). Son datos de juego sin valor de
desarrollo: nombres de eventos, facciones, mecánicas — cosas como
`tribal_politics`, `wiki_imperator` (3.8MB), `warfare_events`, `yuezhi`,
`umbrian`, `west_levantine`, `tlv_decisions`, `war_council`, etc.
**El usuario confirmó que todo archivo bajo `\game\` se descarta sin
revisión — no es parte de esta auditoría.**
El universo real de esta auditoría son los **274 archivos restantes**
(239 .md, 13 .txt, 11 .py, 9 .json, 1 .html, 1 .csv) — filtrar `\game\`
de la ruta antes de mirar cualquier listado o conteo del zip, o el
panorama va a parecer mucho más grande y caótico de lo que es en
realidad. Ver sección 3.7 del log para la confirmación completa de este
filtro, y la sección 1 para el conteo exacto (861 vs 274).
Al inspeccionar `_indice_copiados.csv` con script, filtrar así (Python):
`[row for row in rows if '\\game\\' not in row['ruta_original_completa']]`

**Estado general:** ya resuelto y **verificado** el
rescate de los 16 módulos UTN (16/16, sin duplicados, ver 3.8), la
familia "gap" de 7 archivos (sesión v4.1-4.3, ver 2.6, cerrada en v20),
las 6 charlas sueltas (charla_7 a charla_12, ver 2.7, cerradas en v21),
la aclaración del bloque de "archivos no mapeados" y la cadena
SESSION_LOG_DOCUMENTACION s19→s22 (ver 2.8 y 3.6.sedecies, ambas
cerradas en v22), los
grupos chicos README/INDICE/paper/skill de la sección 3.6, y ya
cerradas las 5 cadenas incrementales que se habían identificado como
candidatas (WIKI_DOCUMENTACION v1/v2/v3, ver 3.6.bis; IRAM_hitos_
metodologicos, ver 3.6.ter; PROMPT_MAESTRO / IRAM_PROMPT_MAESTRO, ver
3.6.quater; SESSION_LOG_ANALISIS_C1, ver 3.6.quinquies; y TECHNICAL_WIKI
ACTIVE/ARCHIVE, ver 3.6.sexies — esta última CERRADA CON SALVEDAD, no
sin salvedad como las otras 4, ver detalle en el log), siete familias
grandes de 3.6 ya cerradas fuera de esas 5 cadenas originales
(SESSION_LOG_DOCUMENTACION, 35 archivos, ver 3.6.septies;
SESSION_LOG_REPLANTEO, 19 archivos, ver 3.6.octies; IRAM_C1, 18
archivos, ver 3.6.novies; SESSION_LOG_AUDITORIA_CONTINUIDAD, 2 archivos,
ver 3.6.decies; IRAM_analisis_cuantitativo, 3 archivos, ver
3.6.undecies; IRAM_SESSION_LOG, 4 archivos, ver 3.6.duodecies; y
PROMPT_DOCUMENTACION_IRAM_v1, 5 archivos, ver 3.6.terdecies), y también
los 7 grupos chicos/pares restantes de 3.6, cerrando la sección
3.6 por completo (6 grupos en v18, ver 3.6.quaterdecies; el último
sub-grupo — `sesion cortada.md` vs transcripciones de
SESSION_LOG_CONSOLIDADO — en v19, ver 3.6.quindecies).

**Con v23, v24 y v25, además, quedaron completamente cerradas las
secciones 3.4, 3.9, y la familia `FUENTE_DE_VERDAD_IRAM_2026-07-07`
(que no era 1 archivo suelto, sino una cadena de 11 — ver nota de v25
más abajo). Con esto, de 3.2 a 3.9 no queda ninguna sección numerada
grande sin cerrar.** Lo que sigue son piezas sueltas más chicas y una
tarea estructural nueva (árbol definitivo de documentación) — ver la
nota de v25 y la sección 4 del log para el detalle completo.

**Nota sobre v23 (la más reciente):** retomó exactamente 3.4 (sesiones
"falladas"/"truncadas" sueltas), verificando desde cero — sin dar por
buena ninguna conclusión heredada de un chat anterior — cada relación
entre los 4 archivos de esa sección. Resultado (ver 2.9 para el
detalle completo con hashes y diffs):
- `SESION TRUNCADA.md` resultó contener, **como prefijo textual exacto**,
  a `IRAM_SUPERBACKUP_v2_1.md` (que figuraba pendiente en 3.8 y 3.9) +
  216 líneas propias de un turno de chat posterior. Se descarta
  `IRAM_SUPERBACKUP_v2_1.md` por redundante y se conserva `SESION
  TRUNCADA.md`. Esto resuelve, de paso, uno de los 3 pendientes de 3.9.
- `fallo sesiones transcript 16-06-2026.md` y `fallo sesiones
  16-06-2026.md` comparten 95% de sus líneas (bloque continuo de 3712
  líneas), y el primero termina generando literalmente el `s19` ya
  cerrado en 3.6.sedecies. Ambos se conservan (mismo patrón que
  transcript-crudo-vs-destilado ya visto en 2.1).
- `fallo DOCUMENTACION 19-06-2026.md` es independiente de los otros
  tres (menos del 1% de líneas compartidas) — quedaba como único ítem
  de 3.4 sin comparar contra el resto del corpus grande. **Resuelto en
  v24, ver nota de v24 más abajo.**

**Nota sobre v24 (cierre completo de 3.4):** se retomó exactamente
donde dejó v23 — comparar `fallo DOCUMENTACION 19-06-2026.md` contra el
corpus grande (no solo contra sus "hermanos" de nombre). Resultado (ver
2.9.c para el detalle completo): no es una transcripción cortada pese
al nombre de la familia — es una transcripción de sesión **completa y
cerrada**, donde Claude lee 27 archivos de un zip distinto
(`DOCUMENTACION.zip`) en orden cronológico real y entrega una síntesis
final. Se confirmó que todos los archivos que menciona (`IRAM_C1_final.md`,
`WIKI_DOCUMENTACION_v2.md`, `spec_c_zip_history.py`, la cadena completa
`SESSION_LOG_ANALISIS_C1_v2` a `_v5`) existen en el corpus real de 274
— y se verificó **por diff directo**, no solo por lo que narra el
documento, su hallazgo central: `SESSION_LOG_ANALISIS_C1_2026-06-18_v5.md`
tiene el encabezado desincronizado del cuerpo (promete "DC-11 +
H-PROC1" pero el cuerpo es copia literal de v4, sin ninguna sección
nueva — únicas 2 apariciones de esos términos están en el encabezado).
**Veredicto: conservar completo, sin descarte.** Con esto, **la
sección 3.4 queda completamente cerrada: sus 5 archivos físicos
verificados** (`SESION TRUNCADA.md` conservado, `IRAM_SUPERBACKUP_v2_1.md`
descartado por redundante, los 2 `fallo sesiones...16-06-2026.md`
conservados, y `fallo DOCUMENTACION 19-06-2026.md` conservado). Quedan
2 frentes abiertos, ya identificados desde antes: el archivo suelto
`FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md` y los 2 sueltos reales de 3.9.

**Nota sobre v25 (dos cierres en la misma sesión — CERRADA la familia
`FUENTE_DE_VERDAD` completa y CERRADA la sección 3.9):**

1) **`FUENTE_DE_VERDAD_IRAM_2026-07-07` no era 1 archivo suelto — es
   una familia de 11** (`base`, `_2` a `_11`). Ver 2.10 para el detalle
   completo con hashes. **Hallazgo principal, verificado por diff, no
   solo por lo que dice el propio documento:** el sufijo numérico del
   nombre de archivo en disco no siempre coincide con la "VERSIÓN _N"
   real que cada archivo declara internamente en su banner. Dos casos
   concretos: (a) el archivo con nombre de disco `_4` es en realidad un
   **checkpoint intermedio truncado** de la misma versión real "_3"
   que el archivo con nombre de disco `_3` (diff: 0 líneas agregadas,
   18 removidas — falta completa la §12, cortada a mitad de redacción,
   tal como el propio documento narra); (b) el archivo con nombre `_7`
   sí es superset correcto de `_6` (50 líneas agregadas, 2 removidas
   por actualización de estado, no pérdida). **Veredicto: conservar
   los 11 completos, sin descartes** — mismo criterio que checkpoints
   intra-sesión de 3.6.octies. Contenido de valor propio: el "Paquete
   A/B/C/D/E/F" del proyecto, el cambio de principio "más que"→"tanto
   como" (§12), y el hallazgo de duplicación física de
   `SESSION_LOG_REPLANTEO_*` en el zip (§17, ver también la tarea
   estructural nueva en la sección 4 del log).

2) **Sección 3.9 completa** (ver 2.11): los 2 sueltos reales que
   quedaban (`IRAM_Historial_Unificado_v2.md` e
   `IRAM_historial_unificado_2026-06-12.md`) **no son versión/bifurcación
   de la misma cadena** pese al nombre casi idéntico — son dos
   productos de naturaleza distinta: `v2` es un índice-resumen
   ejecutivo por Agente (135 sesiones, 09/04→16/05), `2026-06-12` es
   una extracción casi cruda de mensajes reales por cuenta de Claude
   (441 conversaciones, 22/10/2025→10/06/2026, con deduplicación
   explícita). Verificado por comparación de contenido real de una
   sesión compartida entre ambos (no solo por el ratio global de
   similitud, que por sí solo no prueba nada): `v2` la resume en 2
   líneas, `2026-06-12` la reproduce con timestamps y mensajes reales.
   **Veredicto: conservar ambos, sin descarte** — son complementarios,
   no compiten.

Con v25, **de las secciones grandes numeradas (3.2 a 3.9) no queda
ninguna abierta.** Lo que sigue: el suelto
`SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` (posible
pérdida real, no localizado en los 274), los 7 "sueltos sin familia
clara" listados en la sección 4 del log, y la **tarea estructural nueva**
del árbol definitivo de documentación (surgida de §17/§18 de
`FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11` — ver sección 4 del log
para el detalle completo de los 4 problemas ya verificados que hay que
resolver ahí). Esta última es de diseño/decisión, no de verificación
por diff — conviene preguntar al usuario cómo priorizarla frente a los
sueltos menores.

**Nota sobre v22:** surgió de una aclaración lateral,
no de continuar 3.4/3.9. Un bloque de ~13 archivos se había presentado
como "no mapeado por el log" — al verificar contra el cuerpo real del
log (no contra la nota de continuidad), 10 de esos 13 ya estaban
cubiertos (ver 2.8). Los otros 2 (`correccion de documentacion.md` y
`correccion de documentacion 2.md`) eran nuevos de verdad, y destaparon
una cadena completa sin tocar: `SESSION_LOG_DOCUMENTACION_2026-06-17_
CONSOLIDADO_s19` (2 versiones) → `_s20` → `_ESPECIAL_s21` → `s22` — los
5 archivos localizados quedaron verificados y CERRADOS en 3.6.sedecies.
Hallazgo con valor propio: `s21` documenta y corrige, con sus propias
palabras, una pérdida real de contenido en el paso `s19→s20` — evidencia
directa del propio proyecto a favor del criterio de v8. Sigue pendiente
ubicar `..._CONSOLIDADO_s18.md`, citado por toda la cadena como
predecesor pero no localizado en los 274.

**Nota sobre v10:** la sesión v10 NO agregó trabajo de auditoría — solo
se aclaró el propósito final de todo este proceso (ver sección "0.bis"
del log): este log de continuidad es el registro crudo de trabajo; en
una etapa posterior (aprox. mes 3 de un plan de 3 meses: mod → estudio
de procesos → análisis exigente) se va a destilar de acá un **anexo
metodológico** para el paper y el trabajo de la Diplomatura UTN, que
presente el análisis y cómo se elaboró — no la bitácora completa, sino
su síntesis defendible académicamente. Esto no cambia nada operativo.

**Nota sobre v11→v12:** la familia `SESSION_LOG_DOCUMENTACION` (35
archivos, ver 3.6.septies) quedó completamente revisada y CERRADA. Se
conservan los 35 completos — ninguno duplicado exacto por hash. Incluye
2 bifurcaciones reales sin resolución de orden posible (sesión 11 y
sesión 19, 4 archivos) y 2 saltos con caída de tamaño verificados como
migración de contenido a documentos de destino reales (SKILL v1.0,
paper), no pérdida (s7→s8, s9→s10). Un caso de evidencia mixta menor en
sesión 13 (detalle puntual sin correlato textual explícito pero con
supervivencia conceptual confirmada). **No queda nada pendiente de esta
familia.**

**Nota sobre v12→v13:** la familia
`SESSION_LOG_REPLANTEO` (19 archivos, ver 3.6.octies) quedó
completamente revisada y CERRADA. Se conservan los 19 completos —
ninguno duplicado exacto por hash. A diferencia de las familias
anteriores, tiene 2 grupos de checkpoints intra-sesión (6 y 3 archivos
citando al mismo predecesor cada uno) verificados como progresión real
con contenido creciente, no bifurcación. Hallazgo nuevo: 6 de los 19
archivos estaban en la carpeta `_CUARENTENA_DUPLICADOS` del propio
proyecto sin ser duplicados reales — falso positivo de clasificación
por carpeta, verificado por hash y descartado. **No queda nada
pendiente de esta familia.**

**Nota sobre v13→v14:** la familia `IRAM_C1` (18 archivos, ver
3.6.novies) quedó completamente revisada y CERRADA. Se conservan los
18 completos: esqueleto de planificación con mapping único de fuentes,
14 drafts por sección verificados como supersets limpios por diff, la
versión `completo_s32` (con una Sección 4D propia no reproducida en
ningún suelto) y `final` como reescritura editorial con contenido
sustantivo verificado intacto por muestreo. **No queda nada pendiente
de esta familia.**

**Nota sobre v14→v15:** el rescate de los 16
módulos UTN (`Modulo*_Unidad*`, cuyo alcance ya se había resuelto en
v9, ver sección 0) quedó **verificado y CERRADO**. Se conservan los 16
completos: grilla Módulo 1–4 × Unidad 1–4 sin huecos, 16 hashes
SHA-256 distintos entre sí (cero duplicados), cada archivo con
`cantidad_lugares_donde_aparece = 1` en el índice, y título de
Módulo/Unidad dentro del contenido verificado igual al nombre de
archivo en los 16 casos — sin ningún caso de nombre engañoso. No
formaban una cadena de versiones, así que no requirió diff entre ellos.
**No queda nada pendiente de este bloque** (definir dónde viven en el
árbol final del repo es una tarea organizativa, no de auditoría de
contenido, y no bloquea este cierre).

**Nota sobre v15→v16:** se revisaron las 4
familias grandes de 3.6 que quedaban sin tocar. Las 4 quedaron
**verificadas y CERRADAS, se conservan los 19 archivos completos entre
las cuatro:**
- `SESSION_LOG_AUDITORIA_CONTINUIDAD` (2 archivos, ver 3.6.decies): no
  son duplicado ni superset entre sí — son 2 sesiones consecutivas y
  complementarias (07-07 se declara a sí mismo continuación directa de
  07-06). Conservar ambos.
- `IRAM_analisis_cuantitativo` (3 archivos, ver 3.6.undecies): cadena
  confirmada, pero base→v2 es evidencia mixta (v2 corrige y revierte
  el veredicto de la base sobre el modelo de cuentas de Claude, no lo
  complementa); v2→v3 sí es superset limpio. Conservar los 3.
- `IRAM_SESSION_LOG` (4 archivos, ver 3.6.duodecies): no son versiones
  del mismo documento — son 4 logs de sesión de desarrollo del mod
  cronológicamente encadenados por "Continuación de:". Conservar los 4.
- `PROMPT_DOCUMENTACION_IRAM_v1` (5 archivos, ver 3.6.terdecies): cadena
  con 2 saltos de evidencia mixta (v1_4→v1_5 y v1_5→v1_7, dos
  reescrituras sucesivas de la regla sobre el modelo de cuentas) + 1
  salto de reestructuración real (v1_7→v1_9, bifurca el SKILL.md único
  en productos C1/paper y C2/skill operacional) + 1 superset limpio
  (v1_9(3)→v1_9(4)). Conservar los 5.

**Hallazgo transversal de v16:** `IRAM_analisis_cuantitativo` y
`PROMPT_DOCUMENTACION_IRAM_v1` narran, desde documentos distintos, el
mismo ciclo real de revisión metodológica del proyecto sobre si las 5
cuentas de Claude trabajaban en paralelo o en rotación secuencial —
ambas llegan al mismo veredicto final (rotación secuencial, 0
interleavings en 7.313 mensajes) por caminos independientes. No es una
contradicción a resolver, es confirmación cruzada. **No queda nada
pendiente de ninguna de las 4 familias.** Con v16, ya no quedó ninguna
familia grande de 3.6 sin tocar.

**Nota sobre v16→v17:** se revisaron 6 de los grupos chicos/pares de
3.6 pendientes en la nota de continuidad de esa sesión (`critica 1` /
`critica a la critica` / `IRAM_critica_rigurosa`, `PASO_0_grupos_divergentes_checklist`
base+(2), `bloque3_analysis` base+v2, `spec_c_zip_history` base+(3),
`IRAM_Prompt_Etapa1_Limpieza`+`Etapa2_Unificacion`, y
`Consigna`/`Consigna_1`/`Consigna_2`), pero **esa nota citaba una
sección "3.6.quaterdecies" para el detalle que en realidad nunca se
había escrito en el cuerpo del log** — ver el aviso de integridad
documental al principio de este log.

**Nota sobre v17→v18 (integridad documental + re-verificación):** se
detectó que la sección 3.6.quaterdecies citada por v17 no existía, y se
re-verificaron los 6 grupos desde cero contra los archivos reales del
zip (ver 3.6.quaterdecies, ahora sí escrita). **Resultado: sin
discrepancias — se confirmaron exactos todos los números, citas y
ratios de similitud que afirmaba la nota de v17.** Se conservan los 10
archivos entre los 6 grupos, sin descartes:
- `critica 1` / `critica a la critica` / `IRAM_critica_rigurosa`:
  bifurcación real (ratio 0.45, mismo arranque de 419 caracteres) +
  documento final idéntico al fragmento embebido en `critica 1`.
  Conservar los 3.
- `PASO_0_grupos_divergentes_checklist` base + `(2)`: superset exacto
  por substring, +9740 caracteres nuevos (DR-22, DR-23). Conservar
  ambos.
- `bloque3_analysis` base + `v2`: reescritura metodológica confirmada
  por el propio docstring y diff completo del código, no checkpoint
  simple. Conservar ambos.
- `spec_c_zip_history` base + `(3)`: único cambio real es el fix del
  BUG-C1 en el regex, confirmado línea por línea. Conservar ambos.
- `IRAM_Prompt_Etapa1_Limpieza` + `Etapa2_Unificacion`: documentos
  hermanos secuenciales, ratio 0.32, sin relación de substring.
  Conservar ambos, no compiten.
- `Consigna` / `Consigna_1` / `Consigna_2`: 3 piezas curriculares
  distintas de la Diplomatura UTN, sin solapamiento (ratios 0.12–0.27).
  Conservar los 3.

**Nota sobre v18→v19 (CERRADO en esta sesión):** se cerró el último
sub-grupo de 3.6.6 que había quedado pendiente desde v17: `sesion cortada.md`
contra las 2 transcripciones de `SESSION_LOG_CONSOLIDADO_2026-06-1*`
(sufijos `__1f5727a2` y `__56abcedb`), más un 4° archivo hallado en la
misma búsqueda (`SESSION_LOG_CONSOLIDADO_2026-06-18`, sin sufijo — es
el documento final, no otra transcripción). Ver 3.6.quindecies para el
detalle completo. **Resultado: los 4 son independientes entre sí, sin
descartes.** `sesion cortada.md` es un draft del paper metodológico
final (Sección 7, s25, línea s21/s23/PROMPT_MAESTRO v1.9) — tema
distinto al de las otras 3. Las 2 transcripciones NO son dos mitades de
una sesión cortada: son 2 sesiones de chat separadas y secuenciales
(18:06 y 19:43) que arrancan del mismo archivo pegado pero divergen —
la primera diseña las specs A/B/C y crea el `SESSION_LOG_CONSOLIDADO`
como output; la segunda va más allá y ejecuta/prueba las 3 specs. Ratios
de similitud entre los 4: 0.03–0.08, sin relación de substring.
**Conservar los 4, sin descartes.**

**Con el cierre de v19, la sección 3.6 completa queda cerrada: no queda
ninguna familia grande ni ningún grupo chico/par sin revisar.**

**Nota sobre v19→v20 (CERRADO en esa sesión):** se cerró la sección
**3.2 — familia "gap" (sesión v4.1-4.3)**, 7 archivos. Ver 2.6 para el
detalle completo. **Resultado: se conservan los 7 completos, sin
descartes**, en 3 sub-grupos: 4 transcripciones de chat (con relación
de superset por substring parcial entre 3 de ellas, más una sesión
posterior independiente), 2 documentos formales con relación de
reemplazo declarado pero superset semántico (no textual), y 1 documento
independiente. **No queda nada pendiente de esta familia.**

**Nota sobre v20→v21 (CERRADO en esta sesión):** se cerró la sección
**3.3 — charlas sueltas (charla_7 a charla_12)**, 6 archivos. Ver 2.7
para el detalle completo. **Resultado: se conservan las 6 completas,
sin descartes.** Ninguna de charla_7 a charla_11 es substring de
charla_12 (ratios 0.01–0.56); el ratio más alto es artefacto de texto
de header repetido, no contenido compartido — charla_12 sintetiza el
*estado* del proyecto en prosa nueva, pero no reemplaza el *contenido*
único de cada sesión cortada. Único solapamiento real: un bloque de
~1578 caracteres entre charla_8 y charla_11, explicado porque
charla_11 ejecuta `tail -20 charla_8.md` para releer el corte de la
sesión anterior (cita operativa, no duplicado). **No queda nada
pendiente de esta sección.**

IMPORTANTE — leé primero el aviso de "CORRECCIÓN DE CRITERIO" al
principio del log v8 (referenciado desde el encabezado de v9 en
adelante) y el aviso de "INTEGRIDAD DOCUMENTAL" agregado en v18, ambos
son lectura obligatoria antes de seguir. El primero cambia qué se
considera descartable: solo los duplicados exactos por hash normalizado
se eliminan; toda versión distinta dentro de una cadena (aunque sea
superset funcional confirmado de la anterior) se conserva como
trazabilidad histórica del desarrollo. Esto ya está aplicado a todas las
cadenas/familias cerradas — no hace falta re-hacer el trabajo de diff,
solo tener el criterio correcto de acá en adelante. El segundo establece
que toda sección marcada como "cerrada" en una nota de continuidad debe
tener su propio encabezado `####` con el detalle verificable (diff,
hash, contenido) antes de darse por completada — no alcanza con la
afirmación de resultado en la nota. No hay corrección de criterio nueva
desde v9 en adelante, sigue vigente tal cual desde v8.

Leé el log completo (incluida la sección 0.bis sobre el propósito
final, el aviso de integridad documental, 3.6.septies a 3.6.terdecies,
el bloque de módulos UTN en 3.8, 3.6.quaterdecies con los 6 grupos
chicos de v18, la 3.6.quindecies con el cierre de `sesion cortada.md`
en v19, la 2.6 con el cierre de la familia "gap" en v20, la 2.7 con el
cierre de las charlas sueltas en v21, la 2.9/2.9.c con el cierre
completo de 3.4 en v23/v24, la 2.10 con el cierre de la familia
`FUENTE_DE_VERDAD_IRAM_2026-07-07` completa (11 archivos) en v25, y la
2.11 con el cierre completo de 3.9 en v25 — todos CERRADOS). Con esto,
**no queda ninguna sección numerada grande (3.2 a 3.9) sin cerrar.**

Lo que sigue del proyecto ahora son piezas más chicas: **una
reconciliación interna del propio log** (2.2, una sección vieja, dice
que `FUENTE_DE_VERDAD_IRAM_2026-07-07*` tiene 12 versiones con `base`
como prefijo exacto de `_11`; 2.10, de esta sesión v25, encontró 11
archivos y no verificó ese substring extremo a extremo — no cambia el
veredicto de conservar todo, pero hay que decidir cuál cuenta es la
correcta, ver nota al final de 2.10), el suelto
`SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` (posible
pérdida real, citado como predecesor por toda la cadena s19→s22 pero no
localizado en los 274), los 7 "sueltos sin familia clara" (ver sección
4 del log para la lista completa), y una **tarea estructural nueva**
que no es de auditoría de contenido sino de diseño: el árbol definitivo
de documentación del proyecto, declarado por el propio operador como
tarea prioritaria #1 (surgida de §17/§18 de
`FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11`, ver 2.10 y la sección 4 del
log para los 4 problemas ya verificados que hay que resolver ahí:
duplicación física de `SESSION_LOG_REPLANTEO_*`, 33 archivos de trabajo
sin ubicar, 544 archivos sin decidir en `_CUARENTENA_DUPLICADOS`, y el
criterio de legibilidad para instancias de IA simples). Preguntá cómo
priorizar entre estas opciones antes de arrancar.

Aplicá la misma metodología que ya se usó y quedó confirmada en la
sección 2 del log (y reconfirmada en 3.6.bis a 3.6.quindecies) — no
asumir por nombre ni tamaño ni fecha ni carpeta de origen, comparar por
diff/hash/similitud de contenido antes de decidir si algo es duplicado
verdadero, versión a conservar, o documento independiente sin relación
real. Ojo en particular con:
- el caso 2.4.c: una fecha o versión más nueva NO implica que sea
  superset de la más vieja, hay que verificarlo siempre.
- el hallazgo de 2.5: el hash SHA-256 crudo puede marcar como
  "distintos" archivos con contenido idéntico solo por diferencia de
  CRLF/LF — normalizar antes de comparar. Y a la inversa, dos archivos
  con el mismo número de versión en el nombre (ej. dos "v1_0") pueden
  tener contenido totalmente distinto — no asumir por el nombre.
- en 3.6.bis se vio un caso intermedio: v1→v2 no fue substring exacto
  (hubo reescritura real) pero SÍ fue superset semántico confirmado por
  diff completo línea a línea — no alcanza con probar "substring", hay
  que revisar cada línea que "desaparece" y confirmar que es
  actualización de estado, no pérdida de contenido.
- el hallazgo de 3.6.ter: un archivo "suelto" sin sufijo de versión, con
  la misma fecha que el último paso de una cadena, NO necesariamente es
  parte de esa cadena — puede ser un producto de naturaleza
  completamente distinta (en ese caso, evidencia cruda de un script en
  vez de una versión narrativa). Leer el contenido completo antes de
  asumir que "pertenece" a la familia por coincidencia de fecha o
  nombre parecido.
- el hallazgo de 3.6.quater: no siempre se puede confirmar un superset
  al 100% — en el caso PROMPT_MAESTRO v1.6→v1.8 hubo una
  reestructuración de fondo donde 2 temas puntuales no tuvieron
  correlato textual explícito en la versión nueva. Cuando pase esto, no
  forzar la conclusión de "v-nueva es superset" — presentar el caso
  puntual con la evidencia mixta.
- el hallazgo de 3.6.quinquies: un nombre con "(2)" no implica que sea
  copia/duplicado — puede ser una versión distinta con contenido
  adicional real (caso v2 vs v2(2) de ANALISIS_C1). Verificar siempre
  por diff, nunca por la presencia de "(2)"/"(3)" en el nombre.
- **el hallazgo de 3.6.sexies (NUEVO EN v9):** en cadenas con documento
  "activo + archivo" (ej. TECHNICAL_WIKI ACTIVE/ARCHIVE), no alcanza con
  diffear una serie contra sí misma — hay que cruzar lo que "desaparece"
  de un lado contra el otro antes de concluir si hay pérdida real. En
  ese caso concreto, la mayoría del contenido retirado de ACTIVE sí
  aparece migrado en ARCHIVE (verificado, no asumido por la declaración
  textual del propio documento), pero no el 100% — quedaron 3 bloques
  de contenido puntual sin correlato confirmado, y se dejaron asentados
  como evidencia mixta en vez de forzar la conclusión de "sin pérdida".
- **el hallazgo de 3.6.septies (CERRADO EN v12):** dentro de familias
  grandes tipo `SESSION_LOG_DOCUMENTACION`, dos archivos distintos
  pueden declarar el mismo número de sesión y la misma relación de
  "reemplaza" al anterior, siendo **bifurcaciones reales**
  (reconstrucciones independientes de una sesión cortada, con
  contenido incompatible entre sí) en vez de duplicado o superset. En
  ese caso no hay forma de establecer orden causal — se conservan
  ambos, documentados como bifurcación, sin forzar cuál es "el bueno".
  Antes de comparar por número de sesión, verificar con grep de
  contexto que el número capturado es realmente un número de sesión y
  no una hora (ej. "sesión 16:55") — hubo 2 falsos positivos de este
  tipo en esta familia.
- **el hallazgo de 3.6.octies (NUEVO EN v13):** dos cosas nuevas en
  esta familia. Primero, no todo grupo de archivos que cita al mismo
  predecesor es una bifurcación tipo 3.6.septies — puede ser una
  **progresión real de checkpoints dentro de la misma sesión de
  trabajo** (varios guardados seguidos el mismo día, antes de adoptar
  una convención de nombre con hora), verificable porque el diff
  encadenado en orden de timestamp da siempre contenido creciente, no
  contradictorio. Segundo: una carpeta de "cuarentena de duplicados"
  creada por el propio operador o un proceso previo **no es evidencia
  de que su contenido sea redundante** — hay que auditarla con el mismo
  rigor que cualquier otro archivo (hash normalizado + diff), no asumir
  por la etiqueta de la carpeta. En este caso, 6 archivos "en
  cuarentena" resultaron ser pasos genuinos y únicos de la cadena.
- **el hallazgo de v15 (módulos UTN):** a diferencia de todas las
  familias anteriores, este bloque no es una cadena de versiones —
  son 16 unidades de contenido temáticamente distinto por diseño
  curricular, así que no aplica diff entre ellos. La verificación
  correcta acá fue otra: (1) confirmar que la grilla Módulo × Unidad
  está completa sin huecos, (2) chequear hash normalizado entre los 16
  para descartar duplicados exactos, y (3) — el paso que en otras
  familias reveló nombres engañosos — confirmar que el número de
  Módulo/Unidad en el nombre de archivo coincide con el título real
  dentro del contenido. En este caso los 16 coincidieron sin
  excepción, pero no había que asumirlo por defecto.
- **el hallazgo de 3.6.undecies/3.6.terdecies (NUEVO EN v16):** cuando
  un salto de versión "corrige" una conclusión anterior (no solo
  agrega detalle), no alcanza con diffear y ver qué desaparece —
  primero hay que leer si lo que desaparece fue **reemplazado por una
  conclusión distinta y explícita**, no solo omitido. En este caso
  concreto (el modelo de cuentas paralelas/secuenciales), dos familias
  independientes narraron el mismo ciclo de corrección con el mismo
  veredicto final — cuando eso pasa, es una señal fuerte de que la
  corrección es real y no un error de una sola fuente. Al mismo tiempo,
  cada estado intermedio se sigue conservando igual (criterio de v8):
  que una conclusión haya sido corregida después no la vuelve
  descartable, sigue siendo un estado histórico real del razonamiento
  del proyecto.
- **el criterio corregido de v8 (sigue vigente sin cambios desde v9):**
  confirmar superset por diff sirve para verificar que no hay pérdida
  de contenido semántico, NO como justificación para descartar las
  versiones anteriores. Solo se descarta lo que sea duplicado exacto
  por hash normalizado (CRLF/LF u equivalente cosmético). Toda cadena
  de versiones se conserva completa, tenga o no evidencia de pérdida
  puntual (ver 3.6.sexies: se conservan los 6 igual, la salvedad solo
  queda registrada, no cambia qué se guarda).
- **el hallazgo de integridad documental (NUEVO EN v18):** una nota de
  continuidad puede afirmar un cierre con números y citas específicas
  sin que exista la sección de respaldo en el cuerpo del log — se
  detectó porque la nota citaba "3.6.quaterdecies" seis veces y esa
  sección no existía como encabezado. La re-verificación desde cero no
  encontró discrepancias (la nota decía la verdad), pero el episodio
  confirma la regla: declarar un cierre en prosa no sustituye escribir
  la sección con su evidencia real. Antes de dar por cerrado algo solo
  porque la nota de continuidad lo dice, verificar que existe el
  encabezado `####` correspondiente con el diff/hash/contenido real.
- **el hallazgo de 3.6.quindecies (NUEVO EN v19):** no todos los
  archivos "candidatos a relacionados" (agrupados juntos por el script
  de descubrimiento, o mencionados juntos en una nota anterior) están
  realmente relacionados entre sí. Cuando el ratio de similitud entre
  documentos da un orden de magnitud por debajo de cualquier par
  "hermano" ya confirmado en el proyecto (acá: 0.03–0.08, contra 0.12–0.45
  de los pares hermanos reales), y los pocos fragmentos coincidentes son
  frases-tesis genéricas repetidas en todo el corpus (no estructura ni
  contenido específico compartido), la conclusión correcta es
  **independencia genuina**, no versión/bifurcación/hermano — y eso
  también es un resultado válido de cierre, no un "no se pudo determinar
  la relación". Además: dos transcripciones de chat que arrancan del
  mismo archivo pegado a horas distintas del mismo día no son
  automáticamente "dos mitades de una sesión cortada" — pueden ser dos
  sesiones separadas que reaccionan de forma independiente al mismo
  input, una de las cuales avanza más lejos en la misma tarea que la
  otra (verificable por qué outputs efectivamente llegó a producir cada
  una, no solo por el texto de entrada compartido).
- **el hallazgo de 2.7 (NUEVO EN v21):** un bloque de coincidencia
  grande entre dos transcripciones de chat no siempre implica relación
  de versión/duplicado — puede ser una **cita operativa de relectura**:
  una sesión posterior ejecuta un comando (`tail`, `cat`, etc.) sobre el
  archivo de la sesión anterior para releer un punto de corte antes de
  continuar, y ese output queda pegado en su propia transcripción. Se
  detecta por contexto (el bloque coincidente aparece precedido de un
  comando bash y su salida en una de las dos transcripciones) y no
  cambia la conclusión de "conservar ambas completas" — es lectura
  normal de continuidad entre sesiones, no redundancia documental.
  También confirmado: un ratio de similitud alto entre dos documentos
  no implica relación de contenido si el único bloque grande compartido
  es texto de instrucciones/header repetido al inicio de cada sesión
  (boilerplate del propio flujo de trabajo) — hay que abrir cada bloque
  de coincidencia grande y leer su contexto antes de concluir, el ratio
  global no alcanza como evidencia por sí solo.
- **el hallazgo de 2.8/3.6.sedecies (NUEVO EN v22):** antes de reportar
  cualquier bloque de archivos como "no mapeado" o "hallazgo nuevo",
  cruzarlo primero contra el cuerpo real del log (grep por nombre en
  todo el `.md`), no solo contra la nota de continuidad ni contra la
  memoria de la sesión anterior — de un bloque de ~13 archivos
  presentados como nuevos, 10 ya estaban cubiertos. Además: cuando una
  cadena de versiones declara textualmente "Reemplaza a" pero el ratio
  de similitud contra el predecesor es bajo, no asumir independencia
  sin más — puede ser un documento operativo que delega su histórico en
  el anterior en vez de reescribirlo (mismo patrón ACTIVE/ARCHIVE de v9)
  y, si la delegación falla, la pérdida real puede estar documentada
  por el propio proyecto en el eslabón siguiente de la cadena — buscar
  esa auto-corrección antes de concluir por diff solo.
- **el hallazgo de 2.9.c (NUEVO EN v24):** cuando un archivo de una
  familia "sueltos/fallados" haya sido ya comparado contra sus
  "hermanos" de nombre, eso no cierra el caso — falta compararlo contra
  el resto del corpus grande completo, porque puede mencionar/analizar
  archivos que sí están indexados en otro lado (en este caso, confirmar
  por diff directo un hallazgo que el propio documento narra en prosa,
  en vez de aceptarlo solo por su palabra, sigue siendo obligatorio —
  mismo principio que el aviso de integridad documental de v18).
- **el hallazgo de 2.10 (NUEVO EN v25) — el más importante de esta
  sesión:** dentro de una misma familia de versiones, el sufijo
  numérico del nombre de archivo en disco puede estar **directamente
  invertido o desalineado** respecto a la versión real declarada dentro
  del propio documento (banner interno tipo "VERSIÓN _N"). No asumir
  nunca que sufijo mayor = contenido más nuevo/completo — verificar
  siempre la autodeclaración de versión interna (si existe) y
  confirmarla por diff antes de ordenar la cadena. Ojo: la advertencia
  explícita en texto del propio documento ("nombrada correctamente
  según la cadena real de versiones, no según el sufijo de archivo") no
  sustituye la verificación por diff — se verificó de forma
  independiente en vez de aceptarla solo por esa declaración.
- **el hallazgo de 2.11 (NUEVO EN v25):** dos archivos con nombre casi
  idéntico (mismo prefijo, sufijo de fecha/versión distinto) no son
  necesariamente la misma familia de versiones — pueden ser dos
  productos de naturaleza y metodología completamente distintas sobre
  el mismo material fuente (acá: un índice-resumen ejecutivo vs. una
  extracción cruda de mensajes). El ratio global de similitud (`quick_ratio`)
  por sí solo no alcanza para decidir — hay que cruzar contenido real
  compartido (ej. títulos de sesión en ambos índices) y comparar cómo
  cada uno trata el mismo ítem compartido antes de concluir si hay
  redundancia, complementariedad, o independencia genuina.

Nota operativa: el entorno de trabajo no persiste entre chats — arrancá
descomprimiendo el zip de nuevo como primer paso, no asumas que hay algo
ya armado en el filesystem. **Recordatorio del filtro `\game\`:** al
descomprimir vas a ver 1135 archivos — 861 de ellos son del videojuego
base (ruta con `\game\`) y se descartan sin revisión, quedan 274 reales.
No te alarmes por el volumen total del zip ni lo reportes como hallazgo:
ya está filtrado y explicado arriba y en la sección 1 del log.

No perdés nada de contexto: todo lo que hace falta saber (scripts ya
construidos, reportes ya generados, conclusiones ya cerradas —incluidas
las de esta última sesión— y qué falta) está en el log.
```

---

## 6. RECORDATORIOS DE REGLAS DEL PROYECTO (no perder de vista)

- Ningún script borra ni modifica nada — son de solo lectura salvo el 3°
  que copia (nunca mueve ni borra el origen).
- Regla explícita del usuario: **"todo lo único va en las carpetas y no
  se purga"** — no tocar `_CUARENTENA_DUPLICADOS` hasta tener el mapeo
  completo de qué es único y dónde debe vivir definitivamente.
- No asumir redundancia ni basura por nombre/tamaño/fecha de archivo —
  siempre verificar por contenido (hash o diff) antes de descartar algo.
  Ni siquiera "más nuevo = superset" es seguro asumir (caso REORGANIZADO
  05-07/06-07, sección 2.4.c) — confirmado de nuevo con el caso INDICE
  en 2.5.b.
- **Regla de la sesión v5:** el hash SHA-256 sin normalizar
  terminadores de línea (CRLF/LF) puede sobreestimar cuántos archivos
  son "únicos" — siempre normalizar antes de hashear/diffear archivos
  de texto. Y nombres con el mismo número de versión no garantizan
  mismo contenido — puede ser una redacción alternativa completa.
- **Regla nueva de la sesión v6 (ver 3.6.ter):** un archivo sin sufijo
  de versión que comparte fecha o nombre parecido con el último paso de
  una cadena candidata no se puede asumir como parte de esa cadena —
  hay que leer su contenido completo primero. Puede ser un producto de
  naturaleza distinta (ej. evidencia cruda de un script en vez de una
  versión narrativa de un documento) que igual vale la pena rescatar
  por separado, no como parte de la serie versionada.
- **Regla de la sesión v7 (ver 3.6.quater):** no siempre el diff
  completo permite confirmar "superset" al 100% — puede haber una
  reestructuración de fondo (ej. 1 entregable prescriptivo se divide en
  2 entregables con esquema de secciones distinto) donde algunos temas
  puntuales de la versión vieja no tienen correlato textual explícito
  en la nueva, sin que se pueda determinar con certeza si están
  subsumidos genéricamente o realmente se perdieron. En ese caso: no
  forzar la conclusión de "es superset", presentar la evidencia mixta
  tal cual es, y dejar que el usuario decida cómo proceder.
- **Regla nueva de esta sesión (v8, ver 3.6.quinquies) — un nombre con
  "(2)"/"(3)" no implica copia/duplicado:** puede ser una versión
  distinta con contenido adicional real (caso v2 vs v2(2) de la cadena
  SESSION_LOG_ANALISIS_C1, donde v2(2) resultó ser un superset con una
  sección completa nueva, no una copia idéntica). Verificar siempre por
  diff, nunca por la presencia del sufijo numérico entre paréntesis.
- **⚠️ CORRECCIÓN DE CRITERIO MÁS IMPORTANTE DE ESTA SESIÓN (v8) — leer
  el aviso completo al inicio del log:** el inventario de "contenido
  único" **solo elimina duplicados verdaderos** (mismo contenido, hash
  idéntico tras normalizar CRLF/LF). Confirmar que una versión más nueva
  es "superset funcional" de una más vieja sirve para verificar que no
  hay pérdida de contenido semántico al pasar de una a otra — **NO es
  justificación para descartar la versión vieja**. Cada versión distinta
  dentro de una cadena (v1, v2, v3...) es un estado histórico real del
  desarrollo del proyecto y se conserva como parte de la documentación,
  aunque su contenido esté subsumido en una versión posterior. Esto
  corrige retroactivamente las conclusiones de 2.2, 2.3, 2.4.a, 2.4.b,
  3.6.bis, 3.6.ter y 3.6.quater (ver detalle en cada sección) — todas
  esas cadenas pasan de "conservar solo la última versión" a "conservar
  todas las versiones". De acá en adelante (empezando por
  SESSION_LOG_ANALISIS_C1 en 3.6.quinquies, que ya aplica el criterio
  correcto) toda cadena nueva se cierra con esta misma conclusión: se
  conservan todas las versiones distintas, se descartan solo los
  duplicados exactos por hash normalizado.
- **Regla nueva de esta sesión (v13, ver 3.6.octies) — una carpeta de
  "cuarentena de duplicados" no es garantía de que su contenido sea
  redundante:** si el operador o un proceso previo ya movió archivos a
  una carpeta con nombre tipo `_CUARENTENA_DUPLICADOS`, eso es una
  hipótesis a verificar, no un hecho confirmado. En el caso de
  `SESSION_LOG_REPLANTEO`, 6 archivos estaban en esa carpeta y
  resultaron ser pasos únicos y necesarios de la cadena real —
  ninguno coincidía en hash ni en nombre-base con los archivos de la
  carpeta oficial. Auditar el contenido de cualquier carpeta de
  cuarentena con el mismo rigor (hash normalizado + diff) antes de
  asumir que puede purgarse.
- **Regla nueva de esta sesión (v13, ver 3.6.octies) — grupos de
  archivos que citan al mismo predecesor no son automáticamente
  bifurcaciones:** a diferencia del patrón de 3.6.septies (donde el
  mismo número de sesión con narrativas incompatibles señalaba una
  bifurcación real), varios archivos pueden citar al mismo predecesor
  simplemente por ser checkpoints seguidos dentro de la misma sesión de
  trabajo (antes de adoptar una convención de nombre con hora). Se
  distingue por diff encadenado en orden de timestamp: progresión real
  = contenido siempre creciente; bifurcación real = contenido
  incompatible entre sí en algún punto. No asumir bifurcación solo
  porque varios archivos declaren el mismo "reemplaza".
- El propio proyecto (§17 de FUENTE_DE_VERDAD_11) ya marcó esta tarea de
  ordenar el árbol de documentación como prioridad #1, por lo que vale
  la pena llevarla hasta el final antes de retomar otras tareas (DR-54,
  fases de UTN, etc.).
- **Regla nueva de esta sesión (v9, ver 3.6.sexies) — en cadenas
  "activo + archivo" (ACTIVE/ARCHIVE), diffear una serie contra sí misma
  no alcanza:** cuando un documento operativo (ACTIVE) tiene un
  complemento histórico declarado (ARCHIVE) al que se le migra
  contenido para aligerarlo, hay que cruzar lo que "desaparece" de
  ACTIVE contra el ARCHIVE correspondiente antes de concluir si hubo
  pérdida real — no basta con el diff interno de la serie ACTIVE ni con
  confiar en la declaración textual del propio documento ("propagado al
  ARCHIVE"). En el caso de TECHNICAL_WIKI, la mayoría del contenido
  retirado de ACTIVE sí se verificó migrado a ARCHIVE, pero no el 100%
  — quedaron 3 bloques puntuales (una tabla de valores numéricos, datos
  crudos de conteo, y una sección de protocolo) sin correlato en ningún
  archivo del set. Ese resultado se dejó asentado como evidencia mixta,
  sin forzar la conclusión de "sin pérdida", siguiendo el mismo
  principio que ya regía desde 3.6.quater (PROMPT_MAESTRO). Importante:
  esto no cambió qué se conserva — bajo el criterio de v8 los 6 archivos
  se rescatan igual, tenga o no evidencia de pérdida puntual.
- Alcance de la auditoría: incluye tanto desarrollo del mod IRAM como
  material de la Diplomatura UTN (ej. los 16 Modulo*_Unidad*) — el
  criterio es "contenido único de desarrollo/documentación no
  recuperable en otro lado y fuera de `\game\`", no "es específicamente
  IRAM".
- **Regla nueva de esta sesión (v18) — un cierre declarado en la nota de
  continuidad no es un cierre real hasta que tiene su sección propia:**
  la nota de continuidad de v17 afirmó el cierre de 6 grupos citando
  seis veces una sección "3.6.quaterdecies" que nunca se había escrito
  en el cuerpo del log — la única evidencia era la afirmación de
  resultado, no el trabajo de verificación. De acá en adelante, todo
  cierre mencionado en la sección 5 (prompt para el próximo chat) debe
  tener su encabezado `####` correspondiente con el detalle verificable
  (diff, hash, contenido) en el cuerpo del log antes de considerarse
  cerrado — la nota de continuidad resume, no reemplaza, la sección de
  respaldo.
- **Regla nueva de esta sesión (v19, ver 3.6.quindecies) — un ratio de
  similitud casi nulo (muy por debajo de cualquier par "hermano" ya
  confirmado en el proyecto) es evidencia suficiente de independencia
  genuina entre documentos, y ese es un resultado de cierre válido:**
  no todo lo agrupado por un script de descubrimiento o mencionado junto
  en una nota anterior está necesariamente relacionado. Además: dos
  transcripciones de chat que arrancan del mismo archivo pegado, a horas
  distintas del mismo día, no son automáticamente "dos mitades de una
  sesión cortada" — verificar qué outputs produjo efectivamente cada una
  antes de asumir que se trata de continuación/corte, ya que pueden ser
  sesiones independientes que reaccionan por separado al mismo input.
- **Regla nueva de esta sesión (v20, ver 2.6) — una relación de
  "reemplazo declarado" en el propio texto ("Reemplaza a: X") no
  garantiza superset textual, hay que confirmar el superset semántico
  por lectura completa:** en la familia "gap", `CERRADO` declara
  reemplazar a `nota_deuda` pero el ratio de similitud textual es bajo
  (0.053, sin relación de substring) porque es una reescritura completa
  desde fuente primaria distinta. El superset solo se confirma leyendo
  ambos documentos punto por punto, no por la declaración de reemplazo
  en sí ni por el ratio. Además: dentro de una misma familia de
  transcripciones de chat puede haber una relación de superset por
  substring exacto entre algunas (checkpoint + continuación) y al mismo
  tiempo un archivo hermano completamente independiente (ratio
  <0.01) — no asumir que toda la familia comparte el mismo tipo de
  relación solo porque el nombre de archivo es casi idéntico.
- **Regla nueva de esta sesión (v21, ver 2.7) — un bloque de
  coincidencia textual grande entre dos transcripciones de chat puede
  ser una cita operativa de relectura (un comando tipo `tail`/`cat`
  ejecutado sobre el archivo anterior, con su output pegado en la
  transcripción de la sesión nueva), no una relación de versión ni un
  duplicado accidental — se identifica abriendo el bloque coincidente
  en contexto y verificando si está precedido de un comando de lectura
  de archivo. Tampoco alcanza con mirar el ratio global de similitud
  para concluir relación de contenido: si el único bloque grande
  compartido es texto de instrucciones/header que el usuario repite al
  pegar en cada sesión nueva (boilerplate del propio flujo de trabajo,
  no contenido del proyecto), un ratio aparentemente alto puede no
  significar nada — siempre hay que inspeccionar el contenido de cada
  bloque de coincidencia grande antes de sacar conclusiones del ratio
  solo.

# ═══════════════════════════════════════════════════════════════════
# PARTE 2 — ADDON v26+v27 (2026-07-10): reconciliación FUENTE_DE_VERDAD
#           (12→11 versiones), cierre del suelto s18, y revisión de los
#           21 sueltos sin familia clara
#
#           NOTA: v27 es el addon conjunto de las sesiones v26 y v27 —
#           ya incorpora (de forma condensada, mismas conclusiones y
#           evidencia) el contenido íntegro de "ADDON v26 2.md".
#           Verificado: toda afirmación sustantiva de v26 (hashes,
#           veredictos, cifras) está presente en v27. Por eso no se
#           incluye v26 por separado — hacerlo hubiera duplicado ~240
#           líneas de contenido ya cubierto.
# ═══════════════════════════════════════════════════════════════════

# ADDON — Log de continuidad IRAM, sesiones v26 + v27 (2026-07-10)

**Se adjunta a:** `LOG_CONTINUIDAD_IRAM_2026-07-10_v25.md`. No reemplaza el log
— es un anexo que documenta el trabajo de dos sesiones nuevas (v26: verificación
de arranque y reconciliación 2.2 vs 2.10; v27: cierre del s18 y revisión de los
21 sueltos sin familia clara), siguiendo el aviso de integridad documental
(v18): ninguna sección se da por cerrada solo por afirmarlo en prosa, tiene que
tener su propio encabezado con evidencia verificable.

**Nota de continuidad del entorno:** el filesystem de trabajo no persiste
entre chats — cada sesión nueva tuvo que re-descomprimir el zip y reconstruir
el universo de 274 desde cero. En ambos casos el resultado fue idéntico
(274 archivos, 0 faltantes), confirmando que el universo de auditoría es
estable y no depende de artefactos de sesión.

---

## 0. Verificación de arranque (previa a cualquier auditoría)

Antes de tocar el contenido, se re-verificó desde cero el universo de trabajo,
sin asumir nada heredado del log:

- El zip `candidatos_valiosos.zip` se descomprimió de nuevo (el entorno no
  persiste entre chats). Extracción física: **1136 archivos**, no 1135.
- Investigado el archivo de más: es una **copia de `_indice_copiados.csv`**
  incluida dentro del propio zip — no es un candidato del proyecto, es el
  índice mismo. Confirmado por diff de nombres contra las 1135 filas de datos
  reales del CSV (`_indice_copiados.csv` tiene 1136 líneas = 1135 filas de
  datos + 1 header). Descartado de la auditoría por ser el índice, no un
  documento del proyecto.
- Con ese archivo descartado, el universo es exactamente **1135 candidatos**,
  tal como dice el log.
- Aplicado el filtro `\game\` sobre `ruta_original_completa` (Python,
  `'\\game\\' not in row['ruta_original_completa']`): **861 descartados / 274
  reales**. Desglose por extensión verificado de cero:
  - 239 `.md`, 13 `.txt`, 11 `.py`, 9 `.json`, 1 `.html`, 1 `.csv` = 274.
  - **Coincide exactamente con lo que afirma el log v25.** Sin discrepancias.
- Confirmado que los 274 archivos reales existen físicamente en el zip (0
  faltantes) y se copiaron a una carpeta de trabajo separada
  (`real_274/`) para las comparaciones de esta sesión.

**Conclusión de este paso:** el universo de auditoría (274 archivos) queda
re-confirmado de forma independiente, con una aclaración menor nueva (el
archivo 1136 del zip es el propio índice CSV, no un candidato — vale la pena
que quede anotado para que una sesión futura no lo cuente como discrepancia).

---

## 1. Reconciliación 2.2 vs 2.10 — CERRADA en esta sesión

**Problema de partida:** la sección 2.2 (vieja, de un chat anterior) afirmaba
que la familia `FUENTE_DE_VERDAD_IRAM_2026-07-07*` tiene **12 versiones**, con
`base` como prefijo textual exacto de `_11`. La sección 2.10 (v25) había
encontrado **11 archivos** y no había verificado ese substring extremo a
extremo. Tarea de esta sesión: decidir cuál cuenta es la correcta, verificando
por diff directo, no aceptando ninguna de las dos narrativas por su palabra.

### 1.1 Conteo físico

Listado directo del filesystem, 11 archivos confirmados:

```
FUENTE_DE_VERDAD_IRAM_2026-07-07              (sin sufijo — "base")
FUENTE_DE_VERDAD_IRAM_2026-07-07 2            (sufijo " 2" CON ESPACIO)
FUENTE_DE_VERDAD_IRAM_2026-07-07_3
FUENTE_DE_VERDAD_IRAM_2026-07-07_4
FUENTE_DE_VERDAD_IRAM_2026-07-07_5
FUENTE_DE_VERDAD_IRAM_2026-07-07_6
FUENTE_DE_VERDAD_IRAM_2026-07-07_7
FUENTE_DE_VERDAD_IRAM_2026-07-07_8
FUENTE_DE_VERDAD_IRAM_2026-07-07_9
FUENTE_DE_VERDAD_IRAM_2026-07-07_10
FUENTE_DE_VERDAD_IRAM_2026-07-07_11
```

**Hallazgo clave:** no existe ningún archivo `_2` con guion bajo. Lo que existe
es `" 2"` con **espacio** — patrón de nombre típico de copia/duplicado (estilo
Windows "archivo (2)"), no de sufijo de versión secuencial `_N` como el resto
de la familia. Es razonable que la nota vieja 2.2 haya contado ese archivo como
un escalón numerado más, inflando el conteo real de 11 a 12.

**Veredicto parcial: el conteo correcto es 11, no 12.**

### 1.2 Verificación `base` → `"2"` (espacio)

Hash normalizado (CRLF→LF) de ambos, y diff completo:

- `base`: 175 líneas.
- `"2"` (espacio): 263 líneas.
- Diff: **0 líneas removidas, 88 líneas agregadas** — el agregado es la §9
  completa ("PAQUETES DE DEBATE", Paquetes A a F), insertada al final.//
  Las primeras 175 líneas de `"2"` son idénticas carácter por carácter a las
  175 líneas de `base`.

**Confirmado por diff directo: `base` es prefijo textual exacto de `"2"`.**
Superset limpio, sin pérdida — mismo patrón que otras cadenas ya cerradas
(3.6.octies, checkpoints intra-sesión).

### 1.3 Verificación `base` → `_11` (cadena completa)

Acá la nota 2.2 se queda corta si se toma literal. Diff de `base` (175 líneas)
contra las primeras 175 líneas de `_11`:

- **No es substring exacto.** El banner interno de versión (bloque que narra
  la historia de `_2` a `_11`, en formato `> **VERSIÓN _N ...**`) se reescribe
  y **crece con cada versión intermedia** — es texto nuevo insertado *en medio*
  del documento (después del encabezado, antes de la §0), no solo agregado al
  final.
- Además, el bloque de cierre de `base` ("Sin cambios respecto a lo que ya
  decía `plan.md`...", las últimas ~13 líneas) **no se reproduce igual** en
  `_11` — probablemente reescrito o movido en alguna versión intermedia.

**Veredicto: evidencia mixta, no superset por substring puro.** Hay
continuidad real de contenido semántico (las secciones numeradas §0 a §18 se
van agregando sin reescribirse entre sí — política append-only DR-42
verificada en el propio texto), pero el banner introductorio sí se reescribe
versión a versión. Mismo patrón que 3.6.bis / 3.6.quater: no forzar la
conclusión de "superset exacto" cuando la evidencia es mixta — se deja
registrado así, sin que esto cambie el veredicto de conservar los 11
completos.

### 1.4 Verificación de los dos casos puntuales que citaba 2.10

**Caso (a) — `_4` es checkpoint truncado de `_3`, no una versión distinta:**

- `_3`: 334 líneas. `_4`: 316 líneas.
- Diff: **0 líneas agregadas por `_4` que no estén en `_3`, 18 líneas
  removidas** — falta completa la §12 ("PROCESO DE LAS 4 CHARLAS QUE
  PRODUJERON EL CIERRE DEL PAQUETE A"), cortada exactamente donde el propio
  documento narra que se truncó la redacción.
- **Confirmado por diff directo, no solo por la narración del documento.**
  Coincide exactamente con lo que afirmaba 2.10.

**Caso (b) — `_7` es superset correcto de `_6`:**

- `_6`: 396 líneas. `_7`: 444 líneas.
- Diff: **50 líneas agregadas, 2 removidas** (actualización de estado, no
  pérdida de contenido).
- **Confirmado por diff directo.** Coincide exactamente con lo que afirmaba
  2.10.

### 1.5 Veredicto final de la reconciliación

- **Conteo correcto: 11 archivos**, no 12. La cifra vieja de 2.2 era un error
  de conteo, explicado por el archivo `"2"` con espacio (patrón de copia, no
  de versión secuencial) contado de más.
- **Se conservan los 11 completos, sin descartes** — mismo criterio ya
  aplicado en v25 y en toda cadena de versiones desde el criterio corregido
  de v8.
- La cadena real por contenido (no por sufijo de disco) queda:
  `base → "2" → _3 → _4(checkpoint truncado de _3, mismo contenido real) →
  _5 → _6 → _7 → _8 → _9 → _10 → _11`.
- **Esta reconciliación queda CERRADA.** No quedan dudas de conteo pendientes
  sobre esta familia.

---

## 2. Estado general al cierre de v26

Con este addon, la familia `FUENTE_DE_VERDAD_IRAM_2026-07-07` queda
doblemente verificada (v25 + reconciliación v26) sin discrepancias de fondo
— solo la corrección de conteo 12→11, ya explicada.

**Pendiente para la próxima sesión** (sin cambios respecto a lo que ya
señalaba v25):

1. El suelto `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` —
   posible pérdida real, citado como predecesor por la cadena s19→s22 pero no
   localizado en los 274. **Es la siguiente tarea de esta sesión.**
2. Los 7 "sueltos sin familia clara" (ver sección 4 del log v25).
3. La tarea estructural nueva: árbol definitivo de documentación (prioridad
   #1 declarada por el operador, surgida de §17/§18 de
   `FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11`).

Aplica la misma metodología de siempre (sección 2 del log, reconfirmada en
3.6.bis a 3.6.quindecies): no asumir por nombre, tamaño, fecha o carpeta de
origen — comparar por diff/hash/similitud real antes de decidir.

---

## 3. El suelto `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` — NO estaba perdido (CERRADA)

**Premisa de partida (v25):** "posible pérdida real, citado como predecesor por
la cadena s19→s22 pero no localizado en los 274."

**Resultado: la premisa era incorrecta.** El archivo está presente y
físicamente íntegro:

- Nombre original: `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md`
- Nombre en destino (zip): `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s__760c6d24.md`
- 180 líneas, contenido íntegro y legible. Declara explícitamente
  **Reemplaza:** `SESSION_LOG_DOCUMENTACION_2026-06-16_CONSOLIDADO_s16.md` y
  narra que s17 y s18 fueron sesiones cortadas, reconstruidas desde
  transcripts (`failed.md`, `failed (2).md`, `failed_3.md`) + PROMPT v1.9.

**Por qué parecía perdido — advertencia metodológica nueva:** el esquema de
nombres del zip trunca los nombres largos justo antes del hash de destino,
cortando exactamente donde va el número de sesión (`..._s18` queda como
`..._s__760c6d24`). Cualquier búsqueda por "s18" contra el `nombre_en_destino`
truncado, o contra un listado físico del zip, falla en encontrarlo aunque esté
ahí. La búsqueda correcta es siempre contra `nombre_original` en el CSV, nunca
contra el nombre físico truncado.

### 3.1 Relación con la cadena s19 → s20

Se encontró que existen **dos redacciones distintas de la sesión 19**, no un
duplicado exacto:

- `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19.md` (37279 bytes,
  hash `a4a8ae44`)
- `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19 (2).md` (37827 bytes,
  hash `6713bc7f`)

Ambas tienen 439 líneas y el mismo banner ("sesión 19", mismo "Reemplaza:
...s18.md"). Diff normalizado: **7 cambios puntuales**, todos del mismo tipo —
la versión "(2)" revisa explícitamente el rol de `IRAM_SKILL_desarrollo_con_IA
v1.0`, corrigiendo el framing de "~80% del contenido del nuevo C1" (versión sin
sufijo) a "fuente de hechos y ejemplos técnicos, no base estructural — framing
superado en s18" (versión "(2)").

**Cuál es la posterior, confirmado por evidencia de contenido, no por el
sufijo de nombre:** el propio `s20` declara en su banner **Reemplaza:**
`SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s19__2_.md` — cita
explícitamente a la versión **"(2)"** como predecesor directo. **Veredicto:
`s19 (2)` es la redacción vigente/posterior; `s19` sin sufijo queda como
redacción intermedia superada — ambas se conservan.**

**Esta sección queda CERRADA.**

---

## 4. Los "sueltos sin familia clara" — revisados uno por uno (CERRADA)

**Corrección de cifra:** la nota de pendientes decía "7 sueltos", pero la
lista real de "Otros sueltos sin familia clara" del log v25 (línea ~1625)
tiene **21 archivos**, no 7. Se revisaron los 21 contra el universo de 274,
localizando cada uno por `nombre_original` (aplicando la lección de la
sección 3) y leyendo el contenido completo de cada uno — sin asumir nada por
nombre.

### 4.1 Clasificación resultante

**A — Material de proceso/metodología genuino del proyecto IRAM, sin
duplicado conocido (se conservan, valor propio):**

| Archivo | Qué es |
|---|---|
| `LOG_REORGANIZACION_2026-07-05.md` | Log de la reorganización física real (Tarea 1/DR-27 aplicada). Confirma el conteo de **1991 archivos** antes de que se detectara el 2382. Estructura de carpetas resultante completa, con nota de corrección candidata a DR-50 (recasificación de los 5 `data-*.zip` como Corpus A, no B). |
| `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` | Inventario ítem por ítem sobre el ZIP de 1991 archivos: 244 en alcance documental, 188 únicos por hash, 56 duplicados en 43 grupos. Confirma sospecha de v25 (es la fuente del bloque "INVENTARIO COMPLETO" citado en 2.4.c). |
| `IRAM_critica_rigurosa_2026-06-12.md` | Análisis crítico independiente de C1/C2/análisis cuantitativo/SKILL v1.0, en 10 ángulos de rigor. Documento sustantivo único. |
| `RESUMEN_CHARLAS_REPLANTEO_2026-06-19_20 2.md` | Narrativa del "por qué" detrás de las decisiones DR de las charlas 19-20/06 (distinto de los SESSION_LOG_REPLANTEO, que registran el "qué"). |
| `CORRECCIONES_SESION_2026-06-12.md` | Corrección metodológica real: las "sesiones vacías" del análisis cuantitativo no eran fallos de contexto, sino testeos de restauración de tokens — corrige una interpretación errónea ya propagada. |
| `IRAM_INSTRUCCIONES_HUMANO_2026-05-27_20-55.md` | Manual operativo del "sistema de control" original del mod (pre-replanteo, 27/05). Único en su tipo — protocolo de arranque/cierre de sesión, smoke test, protocolo de reanudación tras pausa larga. |
| `PROMPT_CONTINUACION_2026-07-07_8.md` | Prompt de continuación real para retomar sobre `FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md`. Confirma de forma independiente el contenido de `_8` (§15, Paquete C Caso #7/#8) ya reconstruido en la familia FUENTE_DE_VERDAD. |
| `memoria_claude_volcado.md` | Volcado de memoria extenso (157 líneas, 2026-07-03) — ya citado por la propia `FUENTE_DE_VERDAD` (base) como origen del Paquete B. No duplicado de `volcado_memoria (2).md`. |
| `volcado_memoria (2).md` | Volcado corto (30 líneas, 2026-07-04) — es el "Paso 1" explícito de la prueba formal de fuga de memoria, cuyo "Paso 2" es `resultado_prueba_fuga_memoria.md`. Confirmado por diff: **no es duplicado** de `memoria_claude_volcado.md` (contenido y extensión distintos). |
| `instruccion_prueba_fuga_memoria.md` | Plantilla de instrucción para la prueba de fuga de memoria en las 5 cuentas (DR-30). |
| `resultado_prueba_fuga_memoria.md` | Resultado de la prueba en la cuenta claude.ai: 2 fugas reales confirmadas (Módulos UTN "16 unidades" y convención de nombres `ModuloN_UnidadM`), ninguna otra. Cadena completa: `instruccion_...` → `volcado_memoria (2)` (Paso 1) → `resultado_...` (Paso 2). |
| `Qwen_markdown_20260705_q4xkzeqjf (2).md` | Uno de los "3 borradores de plan" que `FUENTE_DE_VERDAD` declara reemplazados. Confirma de forma independiente el conteo de 1991 archivos y el estado pre-DR-54. Evidencia histórica citable, no defectuosa. |
| `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` | Transcripción cruda (119KB) de la sesión de auditoría de continuidad del 07-06. Cita directamente `LOG_REORGANIZACION_2026-07-05.md` e `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` como insumos de esa sesión — confirma el vínculo entre ambos. |
| `sigue log.md` | Transcripción cruda de una sesión cerca de DR-25/DR-26 (03/07, 02:43). Material fuente, no producto terminado. |

**B — Fuera del alcance de la auditoría documental IRAM/UTN (mod técnico, no
tocar, ya excluidos de facto por no ser el foco del proyecto de
documentación):**

| Archivo | Qué es |
|---|---|
| `optimizador_provincial_backup_v4.md` + `imperator_optimizer_v4.html` | Backup técnico + herramienta HTML del "Optimizador Provincial", una utilidad separada para Imperator Rome. Ajeno al proyecto de documentación/diplomatura. |
| `backup_slave_distributor_v2(1).md` | Backup técnico de diseño de una función del mod ("Exodos: Repartir Esclavos"). Mismo caso — fuera de alcance documental. |

**C — Artefactos de auditoría (evidencia de proceso, no documentación del
proyecto en sí, pero útiles como respaldo cruzado):**

| Archivo | Qué es |
|---|---|
| `colisiones_verificadas_2026-07-06.txt` | Reporte de colisiones de nombre con hash MD5 (212 líneas): 76 grupos con nombre base repetido, 43 con contenido distinto pese al nombre similar. Confirma con hash independiente algunos grupos ya tratados (p. ej. `SESSION_LOG_REPLANTEO_2026-07-03_17-58` vs `"2"`). |
| `reporte_resumen.txt` | **Hallazgo más significativo de esta sección.** Comparación de **7 copias completas de la carpeta madre** (`IRAM PROYECTO`, `v1`, `v2`, `v3`, `_REORGANIZADO`, `V2`, `V3`), con conteos de hasta **4384 archivos** en la copia más grande — muy por encima del máximo de 2382 confirmado hasta ahora en el log. El propio reporte declara **0 conflictos reales de contenido** entre copias; todas las diferencias listadas explícitamente caen dentro de `1_MOD/` (`game/`, `corpus_A_crudo/`), fuera del alcance documental filtrado por `\game\`. Es decir: las copias divergen en qué archivos del mod están extraídos en cada una, pero no hay evidencia de divergencia en el material documental de los 274. El detalle completo de los 4342 archivos adicionales queda solo en un JSON no incluido en este corpus — si se quisiera cerrar esto con el mismo rigor que el resto, haría falta ese JSON. |
| `-----------------LEER---------------------.txt` | Nota de 1 línea, etiqueta de contexto de un adjunto ("estado total del proyecto iram previo al ultimo testeo"). Sin contenido documental propio. |
| `---------INSTRUCCIONES-------.txt` | Instrucciones operativas del operador sobre qué adjuntar según el tipo de tarea (siempre / para Plantilla B / para Plantilla C). Metodología operativa del propio operador. |
| `conflictos.csv` | Archivo vacío — solo header, 0 filas de datos. Artefacto residual de una corrida de script. |

**Ya resuelto en sesión anterior (no vuelve a evaluarse acá):**
`FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md` — es parte de la familia de 11
versiones cerrada en la reconciliación 2.2 vs 2.10 (v26), no un suelto
independiente.

### 4.2 Veredicto de esta sección

Ninguno de los 21 resultó ser duplicado exacto de otro dentro del propio
grupo revisado. Los 15 de la categoría A tienen valor documental propio y se
conservan sin descartes. Los 3 de la categoría B están fuera del alcance del
proyecto de documentación (son del mod técnico) y no requieren acción en esta
auditoría. Los 5 de la categoría C son artefactos de proceso/auditoría —
útiles como respaldo cruzado, en particular `reporte_resumen.txt`, que amerita
quedar señalado para la próxima sesión por el conteo de 4384 archivos (no
bloqueante para el árbol de documentación, ya que la divergencia cae fuera de
`\game\`, pero vale la pena entender de dónde salen esas 7 copias distintas
de la carpeta madre antes de dar por cerrado el inventario físico general del
proyecto).

**Esta sección queda CERRADA** en cuanto a "revisar uno por uno" — quedan dos
hilos abiertos menores para quien continúe: (a) conseguir el JSON completo
de `reporte_resumen.txt` si se quiere auditar el detalle de las 7 copias con
el mismo rigor que el resto, y (b) decidir si `IRAM_critica_rigurosa`,
`CORRECCIONES_SESION` y `RESUMEN_CHARLAS_REPLANTEO` deben incorporarse
formalmente al árbol de documentación definitivo (tarea #2 de la lista de
pendientes) o quedar solo como evidencia histórica citable.

---

## 5. Pendiente para la próxima sesión (actualizado)

1. La tarea estructural nueva: árbol definitivo de documentación (prioridad
   #1 declarada por el operador, surgida de §17/§18 de
   `FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11`).
2. Hilo menor abierto en 4.2: entender el origen de las 7 copias de la
   carpeta madre y el conteo de 4384 archivos en `reporte_resumen.txt`
   (no bloqueante, la divergencia cae fuera de `\game\`).
3. Decidir destino documental de los 3 archivos de categoría A que son
   análisis/corrección sustantivos (crítica rigurosa, correcciones de
   sesión, resumen de charlas) — ¿se incorporan al árbol definitivo o quedan
   como evidencia histórica citable únicamente?
4. Nota metodológica ya aplicada y a seguir aplicando: verificar siempre
   contra `nombre_original` del CSV antes de declarar cualquier archivo como
   "no localizado" — el truncamiento de nombres en destino puede ocultar
   coincidencias reales.

# ═══════════════════════════════════════════════════════════════════
# PARTE 4 — LOG v28→v29 (2026-07-10): cadena SESSION_LOG_DOCUMENTACION
#           completa (s18→s34), grupo SESION*, IRAM_PROMPT_MAESTRO vs
#           PROMPT_MAESTRO, verificación del alcance real de los 274,
#           e inspección y cierre del hallazgo estructura_objetivos_iram.svg
#
#           NOTA: v29 es superset verificado de v28 (97% de contención
#           directa; el resto es el propio párrafo de cierre de la
#           sección 8 que v29 reescribió al resolver el SVG). Por eso
#           solo se incluye v29 aquí — incluir ambos hubiera duplicado
#           ~330 líneas de contenido idéntico.
# ═══════════════════════════════════════════════════════════════════

# LOG DE CONTINUIDAD IRAM — v28 (2026-07-10) — CONSOLIDACIÓN FINAL

**Reemplaza operativamente a:** `LOG_CONTINUIDAD_IRAM_2026-07-10_v25.md` +
`ADDON_LOG_CONTINUIDAD_IRAM_2026-07-10_v26.md` (reconciliación 2.2 vs 2.10) +
el trabajo de v27 (cierre del s18 y revisión de los 21 sueltos, incorporado
más abajo). Este documento absorbe el contenido de los tres — no hace falta
cargar los tres por separado, aunque quedan como evidencia histórica citable.

**Regla que este documento sigue, igual que sus predecesores:** ninguna
sección se da por cerrada solo por afirmarlo en prosa — cada cierre tiene
evidencia verificable (diff, hash, ratio de similitud, o cita textual del
propio archivo).

---

## 0. Respuesta directa a la pregunta de esta sesión

**Pregunta:** "¿con este listado terminamos el inventario y podemos rescatar
los archivos únicos?"

**Respuesta corta: no del todo — faltaban 5 piezas genuinas, ahora sí
cerradas en esta sesión.** El log v25 dejaba en su sección 3 (línea 1452 en
adelante) una lista de "familias grandes, TODAS SIN TOCAR AÚN" que en su
mayoría ya estaban resueltas en otras partes del mismo log (la lista nunca se
había actualizado tras cerrarlas) — pero **3 grupos eran pendientes reales**,
y al revisarlos apareció **una cadena completa nunca antes localizada**
(`SESSION_LOG_DOCUMENTACION_s23` a `s34`, 12 archivos). Con esta sesión, sí
se puede decir que el inventario de contenido único está completo.

---

## 1. Verificación de arranque (repetida, sin asumir nada heredado)

El entorno no persiste entre chats — se re-verificó desde cero en esta
sesión, como en v26/v27:

- Zip descomprimido de nuevo: 1136 archivos físicos.
- Confirmado (ya sabido de v26): 1 de esos 1136 es una copia de
  `_indice_copiados.csv` incluida dentro del propio zip — no es un candidato.
- Universo real tras el filtro `\game\`: **274 archivos**, 0 faltantes al
  copiar contra el índice. Mismo resultado que v26 y v27 — el universo de
  auditoría es estable.

---

## 2. Reconciliación de la lista "familias grandes sin tocar" del log v25

La lista de la sección 3 del log v25 (línea 1452) tenía 17 entradas. Se
revisó cada una contra el resto del propio log v25 antes de tocar nada, para
no repetir trabajo ya hecho:

| Entrada de la lista | Estado real encontrado |
|---|---|
| `SESSION_LOG_REPLANTEO_*` | Ya resuelta (3.6.octies) — la lista no estaba tachada. |
| `IRAM_C1_*` | Ya resuelta (3.6.novies) — ídem. |
| `Modulo*_Unidad*` | Ya resuelta (3.8/v15) — ídem. |
| `README*.md` | Ya resuelta (2.5.a) — ídem. |
| `SESSION_LOG_ANALISIS_C1_2026-06-18_*` | Ya resuelta (3.6.quinquies) — ídem. |
| `PROMPT_DOCUMENTACION_IRAM_v1_*` | Ya resuelta (3.6.terdecies) — ídem. |
| `IRAM_hitos_metodologicos_*` | Ya resuelta (3.6.ter) — ídem. |
| `INDICE*.md` | Ya resuelta (2.5.b) — ídem. |
| `TECHNICAL_WIKI ACTIVE/ARCHIVE` | Ya resuelta (3.6.sexies) — ídem. |
| `IRAM_analisis_cuantitativo_*` | Ya resuelta (3.6.undecies) — ídem. |
| `IRAM_SESSION_LOG_*` (mod) | Ya resuelta (3.6.duodecies) — ídem. |
| `WIKI_DOCUMENTACION_v1/v2/v3` | Ya resuelta (3.6.bis) — la lista decía "sin tocar", pero está cerrada 800 líneas antes en el mismo log. **Confirmado por comprobación directa en esta sesión: existen exactamente los 3 archivos que 3.6.bis ya analizó, ningún archivo nuevo con ese prefijo.** |
| `SESSION_LOG_DOCUMENTACION_*` (22) + `SESSION_LOG_DOCUMENTACION_s*` (13) | **Genuinamente pendiente — ver sección 3 de este documento.** No eran dos series solapadas: es una sola cadena cronológica continua con dos convenciones de nombre. |
| `SESION*.md` (3, "SESION FALLADA 1/2/3") | **Genuinamente pendiente — ver sección 4.** |
| `IRAM_PROMPT_MAESTRO_v*` vs `PROMPT_MAESTRO_v*` | **Genuinamente pendiente — ver sección 5.** |
| Volcados JSON en crudo (3.5) | No requieren veredicto de "único/duplicado" — son datos de proceso masivos, se consultan puntualmente, no se leen enteros. Presencia confirmada, sin cambio de estado. |

**Conclusión de esta reconciliación:** de 17 entradas, 12 ya estaban resueltas
y solo no se habían tachado de la lista; 3 eran pendientes reales (resueltas
en las secciones 3-5 de este documento); 1 no requiere veredicto (JSONs).

---

## 3. Cadena `SESSION_LOG_DOCUMENTACION` completa: s18 → s34 (CERRADA)

### 3.1 El s18 — heredado de v27, resumen

Contrario a lo que creía v25 ("posible pérdida real, no localizado en los
274"), `SESSION_LOG_DOCUMENTACION_2026-06-17_CONSOLIDADO_s18.md` **está
presente** en el corpus (nombre en destino truncado a `..._s__760c6d24.md`,
lo que impedía encontrarlo buscando literalmente "s18"). Ver el detalle
completo en el addon v27 — no se repite acá.

### 3.2 s19 y su doble versión — heredado de v27, resumen

Existen dos redacciones de la sesión 19 (`s19` sin sufijo y `s19 (2)`), con 7
cambios puntuales sobre el rol del SKILL v1.0. `s19 (2)` es la posterior
(confirmado porque `s20` cita explícitamente a `s19 (2)` como predecesor).
Ambas se conservan.

### 3.3 s20 → s21 → s22 → s23 — ya cerrado en el propio log v25 (3.6.sedecies)

El log v25 ya tenía este tramo cerrado con evidencia de diff completo: `s20`
perdió contenido real de `s19` (confirmado por el propio `s21`, que lo
diagnostica textualmente); `s21` recupera lo perdido y diagnostica 8 problemas
estructurales (P1-P8); `s22` es superset funcional de `s21` (protocolo nuevo +
Tarea 0 nueva). Las 5 versiones (`s19`×2, `s20`, `s21`, `s22`) se conservan
íntegras — sin cambios respecto a lo que v25 ya decía.

### 3.4 s23 — NUEVO HALLAZGO DE ESTA SESIÓN, no localizado por ninguna sesión anterior

`SESSION_LOG_DOCUMENTACION_s23__f4fdcae4.md` (199 líneas) existe físicamente
en el corpus y **no aparecía citado ni localizado en el log v25 ni en los
addons v26/v27**. Se encontró al revisar el archivo suelto `sesion
cortada.md` (grupo "SESION*.md"), que menciona `SESSION_LOG_DOCUMENTACION_s23.md`
como uno de los 4 archivos que recibió esa sesión.

- **Declara explícitamente:** `**Reemplaza:** SESSION_LOG_DOCUMENTACION_s22.md`.
- **Diff s22 → s23:** ratio de similitud 0.686 (60 líneas removidas, 70
  agregadas) — reescritura operativa sustancial, mismo patrón que
  s20→s21→s22 (spec ejecutable que se reemplaza, no acumula).
- **Verificado que no es pérdida real:** la "TAREA 0 — URGENTE" heredada de
  `s21`/`s22` se ejecuta parcialmente en `s23` (marca "Marco conceptual
  recuperado → en WIKI_DOCUMENTACION_v1.md" como completo, 1 de 3
  condiciones) y dos quedan explícitamente abiertas ("SKILL v1.0 auditado" y
  "`fallo_sesiones_16-06-2026.md` bloqueado — archivo no disponible"), en vez
  de desaparecer sin registro.
- Nota irónica pero no contradictoria: el propio `s23` declara que `s18` "no
  está directamente disponible" — coherente con que, en su momento, el
  proyecto no lo tenía a mano (aunque hoy, con el índice completo de 274,
  sabemos que sí existe físicamente).

**Se conserva íntegro.**

### 3.5 s24 → s34 — CADENA COMPLETA, NUNCA ANTES LOCALIZADA (NUEVO HALLAZGO)

Al confirmar `s23`, se buscó el resto de la serie corta `SESSION_LOG_
DOCUMENTACION_sNN.md` (sin fecha en el nombre) y aparecieron **11 archivos
adicionales**, formando una cadena lineal perfecta hasta el cierre del
proyecto de documentación:

| Archivo | Líneas | Declara reemplazar a |
|---|---|---|
| `s24` | 155 | s23 |
| `s25` | 145 | s24 |
| `s26` | 117 | s25 |
| `s27` | 128 | s26 |
| `s28` | 129 | s27 |
| `s29` | 125 | s28 |
| `s30` | 128 | s29 |
| `s31` | 120 | s30 |
| `s32` | 125 | s31 |
| `s33` | 119 | s32 |
| `s34` | 118 | s33 |

**Verificación de la cadena:** cada archivo declara textualmente su
predecesor exacto (`**Reemplaza:**`), sin bifurcaciones ni sufijos
ambiguos — cadena lineal confirmada por cita textual, no solo por
numeración de nombre. Ratios de similitud consecutivos calculados
(0.52–0.82), consistentes con el patrón "spec ejecutable reescrito cada
sesión" ya visto en s20-s23 — ninguno anómalamente bajo (que indicaría
independencia real) ni igual a 1.0 (duplicado).

**`s34` es el cierre declarado del proyecto de documentación** (fecha
2026-06-18, tipo "Cierre de proyecto — no hay sesión s35 prevista"),
coherente con lo que la familia `IRAM_C1` (3.6.novies) ya mencionaba de
pasada ("Paper C1: CERRADO en s34").

**Se conservan los 12 archivos completos (s23 a s34), sin descartes** — bajo
el mismo criterio de v8 aplicado a toda la auditoría: cada eslabón es un
estado histórico real de la corrección de sistema en marcha.

### 3.6 Conclusión de la cadena completa: s18 → s34 (18 eslabones, 17 archivos)

Con este cierre, la cadena completa de `SESSION_LOG_DOCUMENTACION` (que
empezó siendo "un suelto sospechoso de pérdida" en v25) queda reconstruida
extremo a extremo: **s18 → s19 → s19(2) → s20 → s21 → s22 → s23 → s24 → s25
→ s26 → s27 → s28 → s29 → s30 → s31 → s32 → s33 → s34.** Se conservan los 17
archivos íntegros (18 eslabones porque s19 tiene 2 versiones).

**Esta sección queda CERRADA.**

---

## 4. Grupo "SESION*.md" — CERRADO

Revisados los 3 archivos "SESION FALLADA 1/2/3" (los únicos de este grupo
que no estaban ya cerrados en 3.4/2.9 bajo otros nombres como `SESION
TRUNCADA` y `sesion gap v4.1-4.3`):

- **`SESION FALLADA 1/2/3.md`** — transcripciones crudas de tres sesiones
  distintas trabajando sobre `SESSION_LOG_ANALISIS_C1_2026-06-18_v3.md`
  (parte de la familia `SESSION_LOG_ANALISIS_C1`, ya cerrada en 3.6.quinquies).
  Son el material fuente/transcripción que generó esa familia, no duplicados
  de ella — tienen valor propio como registro de proceso. Se conservan.
- **`sesion cortada.md`** — transcripción que llevó al hallazgo del s23 (ver
  sección 3.4 de este documento). Se conserva por valor propio y porque cita
  contenido (`SESSION_LOG_DOCUMENTACION_s23.md`, `WIKI_DOCUMENTACION_v1.md`,
  `METODOLOGIA_DOCUMENTACION_v1.md`, `TEMPLATES_DOCUMENTACION_v1.md`) que
  ayuda a fechar y contextualizar esa sesión.
- **`sesion fallada.md`** — transcripción corta (131 líneas) sobre el estado
  de la sesión 7 (Plantilla B ejecutada, Plantilla C desbloqueada). Material
  de proceso, se conserva.

**Esta sección queda CERRADA.**

---

## 5. `IRAM_PROMPT_MAESTRO_v*` vs `PROMPT_MAESTRO_v*` — CERRADO, dos series confirmadas independientes

Confirmado por contenido (no solo por nombre) que son **dos series
completamente distintas**, sin relación entre sí:

- **`IRAM_PROMPT_MAESTRO_v3.8 / v3.9 / v5.2`** — "PROMPT MAESTRO — IRAM",
  para sesiones de código/desarrollo del mod (versionado v3.x-v5.x, fechas
  mayo-junio, referencia a `TECHNICAL_WIKI ACTIVE`). Serie del sistema de
  control original del mod, distinta del sistema de documentación.
- **`PROMPT_MAESTRO_v1.6 / v1.8.1`** — "PROMPT — SISTEMA DE DOCUMENTACIÓN
  IRAM", para sesiones de documentación (versionado v1.x independiente,
  no confundir con la familia ya cerrada `PROMPT_DOCUMENTACION_IRAM_v1_4
  /v1_5/v1_7/v1_9`, que tiene otro nombre de archivo pese a la similitud).

**Verificación de contenido — v1.6 → v1.8.1:** ratio de similitud 0.664, con
crecimiento neto (508→604 líneas). El contenido removido/reescrito es **la
misma corrección metodológica ya documentada dos veces** en el log (familias
`PROMPT_DOCUMENTACION_IRAM_v1` y `IRAM_analisis_cuantitativo`): v1.6 todavía
describe el modelo de "5 cuentas trabajando en paralelo"; v1.8.1 ya tiene la
corrección completa (R18 "rotación secuencial", `cuentas_paralelas`
formalmente descartado). **Esta es una tercera fuente independiente
confirmando el mismo hallazgo metodológico del proyecto** — refuerza la
confianza de que no es un error de una sola fuente.

**Se conservan las 5 (3 + 2), sin descartes.**

**Esta sección queda CERRADA.**

---

## 6. Estado final del inventario

Con las secciones 2-5 de este documento, **no queda ninguna familia, cadena
o suelto pendiente de comparar por diff/hash** en el universo de 274
archivos. El único material sin veredicto de "único/duplicado" son los
volcados de chat en crudo (JSONs, sección 3.5 del log v25 original) — por
diseño, no se auditan como documentos sino como datos de consulta puntual.

### 6.1 Qué significa esto para "rescatar los archivos únicos"

**Sí — con esta sesión, el criterio de qué conservar queda completamente
resuelto para los 274.** Bajo el criterio de v8 (aplicado consistentemente
desde entonces): **se conservan los 274 completos, sin descartar ninguno**,
salvo los casos puntuales ya identificados de duplicado exacto real:

- `IRAM_SUPERBACKUP_v2_1.md` — descartado en v23 (2.9.a), prefijo textual
  exacto de `SESION TRUNCADA.md`.
- Colapsos de duplicado exacto dentro de grupos ya cerrados (1 README, 1
  INDICE, ver 2.5.a/2.5.b) — mencionados en su momento, no vuelven a listarse
  acá.

Es decir: de los 274, el número real de duplicados exactos descartables es
mínimo (2-3 archivos). El resto — incluidas las cadenas de versiones
sucesivas — se conserva íntegro porque cada versión es un estado histórico
real, no un archivo redundante, bajo el criterio corregido desde v8.

### 6.2 Hilos menores que NO bloquean el rescate, quedan anotados para después

1. `reporte_resumen.txt` (ver addon v27, sección 4, categoría C): compara 7
   copias completas de la carpeta madre con conteos de hasta 4384 archivos.
   0 conflictos reales de contenido declarados, y toda la divergencia visible
   cae fuera de `\game\` — no amenaza el universo de 274, pero el detalle
   completo depende de un JSON no incluido en este corpus.
2. Decidir destino documental (¿árbol definitivo, o solo evidencia histórica
   citable?) de: `IRAM_critica_rigurosa_2026-06-12.md`,
   `CORRECCIONES_SESION_2026-06-12.md`, `RESUMEN_CHARLAS_REPLANTEO_2026-06-
   19_20 2.md`, `LOG_REORGANIZACION_2026-07-05.md`,
   `INVENTARIO_COMPLETO_MATERIAL_2026-07-05.md` — todos con valor documental
   propio, ninguno bloqueante.
3. La tarea estructural real que sigue: **árbol definitivo de documentación**
   (prioridad #1 del operador, surgida de §17/§18 de
   `FUENTE_DE_VERDAD_IRAM_2026-07-07_10`/`_11`). Con el inventario de
   contenido ya cerrado, este es el único trabajo grande que queda.

---

## 7. Nota metodológica acumulada (para cualquier sesión futura)

- El entorno no persiste entre chats — reconstruir el universo de 274 desde
  cero al empezar cualquier sesión nueva (zip + índice + filtro `\game\`).
- Verificar siempre contra `nombre_original` del CSV antes de declarar
  cualquier archivo "no localizado" — el esquema de nombres trunca nombres
  largos justo antes del hash de destino (caso s18).
- Nombre parecido no implica misma familia (caso `IRAM_PROMPT_MAESTRO_v*` vs
  `PROMPT_MAESTRO_v*`, y antes `PROMPT_DOCUMENTACION_IRAM_v1_*` vs
  `PROMPT_MAESTRO_v1.6/v1.8.1`) — comparar siempre por contenido real.
- Una lista de "pendientes" dentro de un log largo puede quedar desactualizada
  si se cierra un ítem en otra sección sin volver a tachar la entrada original
  (caso `WIKI_DOCUMENTACION` en esta sesión) — antes de trabajar un pendiente,
  buscar en todo el documento si ya se cerró en otro lado.
- Ratio de similitud bajo entre versiones consecutivas no es evidencia de
  independencia por sí solo si el propio texto declara relación de reemplazo
  — revisar el banner interno antes de asumir.

---

## 8. Verificación del alcance real: ¿qué quedó fuera de los 274? (NUEVO, esta sesión)

**Pregunta que motivó esta verificación:** si los 274 son un subconjunto (ya
filtrado por comparación contra el repo activo, por extensión, y por tamaño),
¿hay contenido de valor documental que haya quedado afuera sin revisar?

**Aclaración de alcance, confirmada por el operador:** `IRAM PROYECTO\IRAM
PROYECTO` (el repo pasado como primer argumento al script 2) **es el último
backup / repo activo** — no una copia más. Es decir, el diseño del análisis
es correcto por construcción: todo lo que ya vive en ese repo no necesita
"rescatarse" (ya está en el lugar correcto); los 274 son exactamente lo que
las copias viejas (`testear`) tienen y el backup más reciente no — el
contenido que se perdería si esas copias se borraran sin revisar.

**Verificación realizada:** se comparó el reporte completo antes del filtro
de extensión/tamaño (`reporte_sueltos.csv`, 3334 hashes únicos — el insumo
crudo del que salieron los 1135→274) contra lo que efectivamente llegó al
zip de 274, para confirmar que nada de valor quedó excluido solo por el
filtro de extensión.

### 8.1 Desglose por extensión de los 3334 hashes únicos (antes de cualquier filtro)

| Extensión | Cantidad | Veredicto |
|---|---|---|
| (sin extensión) | 1914 | **100% objetos internos de `.git/objects/`** (blobs comprimidos, `refs`, `packed-refs`) de los distintos repos git encontrados en las copias. Verificado: cero excepciones. Correctamente excluido — no es contenido legible. |
| `.txt` | 1013 (900 en `\game\`, 113 fuera) | De los 113 fuera de `\game\`: ~95% son variantes históricas de scripts del mod (`exodos_decisions*.txt`, `iram_bom_*.txt`, `tgl_decisions.txt`, etc.) dentro de `mod_pack_IRAM_v4_*` viejos — iteraciones anteriores del mismo contenido técnico ya representado en su versión final entre los 274 (ver addon v27, categoría B). El resto (`wiki_imperator.txt`, `colisiones_verificadas...`, `reporte_resumen.txt`, `---------INSTRUCCIONES-------.txt`, `-----LEER-----.txt`) **ya está identificado y tratado** — el primero descartado explícitamente en 3.7, los otros 4 ya llegaron a los 274 y fueron revisados en el addon v27. **Nada nuevo de valor documental quedó afuera en esta extensión.** |
| `.md` | 243 | 239 de estos llegaron a los 274 (coincide con el conteo ya conocido); la diferencia (4) corresponde a variantes que el propio script 3 deduplicó por hash antes de copiar — ya contemplado. |
| `.yml` | 70 | Archivos de localización del mod (traducciones `l_english`/`l_spanish`). Fuera de alcance documental — mismo criterio que el resto del contenido técnico del mod. |
| `.zip` | 32 | Contenedores de backups completos (`IRAM PROYECTO.zip`, `mod___SUPERBACKUP_.zip`, etc.) — su contenido interno ya se descomprimió y pasó por el análisis por separado vía `1_descomprimir_copias.py`. No es contenido adicional, es el mismo contenido empaquetado. |
| `.mod`, `.pack`, `.idx`, `.rev`, `.info`, `.gitignore`, `.gitattributes`, `.sample` | 27+2+2+2+1+1+1+1 | Metadata técnica de git y del formato de mod de Imperator Rome (descriptors, hooks, packfiles). Sin contenido documental. |
| `.rar` | 1 | Backup comprimido (`documentacion iram 10-06-2026 00.30.rar`) — mismo caso que `.zip`, contenido ya descomprimido y analizado por separado. |
| `.svg` | 1 | **`estructura_objetivos_iram.svg`** — **INSPECCIONADO en v29, ver sección 9.** |

### 8.2 Veredicto de esta verificación

**Confirmado: no hay contenido documental de valor (texto/markdown/código)
que haya quedado fuera de los 274 solo por el filtro de extensión o tamaño.**
Los 3334 hashes únicos del reporte completo, descontando lo ya excluido por
buenas razones (`.git` interno, mod técnico, contenedores ya descomprimidos),
no aportan ningún documento nuevo distinto de lo ya inventariado.

**Única excepción real, no bloqueante:** `estructura_objetivos_iram.svg` —
inspeccionado en la sección 9 de este mismo log (v29). No bloqueaba el cierre
del inventario de contenido textual, que ya quedaba confirmado completo.

**Esta sección queda CERRADA.**

---

## 9. `estructura_objetivos_iram.svg` — INSPECCIONADO Y CERRADO (v29)

**Punto de partida:** único ítem que la sección 8 (v28) dejó sin confirmar,
por no estar incluido en los 274 ni descargado aparte.

### 9.1 Localización de las copias

El operador aportó una búsqueda por nombre en el propio filesystem de origen
(Windows, carpeta `Escritorio` y subcarpetas), que arrojó **11 copias**
físicas del archivo, repartidas en distintos backups/carpetas de trabajo
(`copias_descomprimidas\...`, `testear\Proyecto-IRAM--rework-...`,
`testear\IRAM_PROYECTO_REORGANIZADO_v6\...`, `testear\IRAM PROYECTO
\3_ANALISIS`, etc.), con fechas de modificación entre el 7/7/2026 22:10 y el
8/7/2026 23:39. Se aportaron las 11 copias directamente para esta sesión.

### 9.2 Verificación por hash — no es una familia de versiones

Hash SHA-256 de las 11 copias:

```
7f844e7f1c38da7690059485f491a669ce0d34c9d392c924e0d3990e9511548c
```

**Las 11 son byte-idénticas** (mismo hash, mismo tamaño: 9173 bytes cada una).
No hay familia de versiones que reconciliar aquí — es un único archivo
duplicado mecánicamente entre backups sucesivos del proyecto, mismo patrón ya
visto con otros archivos "sueltos" de esta auditoría. **No aplica el
criterio de conservar múltiples versiones**, porque no hay divergencia de
contenido: alcanza con un solo ejemplar.

### 9.3 Contenido del archivo

El SVG contiene un diagrama de flujo vertical de 4 nodos con metadata
descriptiva embebida (`<title>`, `<desc>`) que declara explícitamente su
propio propósito: **"Estructura de dependencia del proyecto IRAM"**, con esta
cadena narrada en el `<desc>`:

- **Mod** → genera el historial del proceso
- **Análisis** → transforma logs en hallazgos
- **Documentación** → objetivo 2 · productos C1 y C2
- **Portafolio UTN** → objetivo 3 · aún vacío
- Flecha adicional directa **Análisis → Portafolio UTN**, marcada como
  atajo correspondiente a "DR-54".

### 9.4 Hallazgo importante — origen probable del archivo

**Este SVG no es documentación fuente del proyecto IRAM en el sentido de los
demás 274 candidatos.** La evidencia:

- La paleta de colores, la tipografía (`"Anthropic Sans"`) y el estilo de
  markers/flechas coinciden exactamente con el sistema visual de salida de
  Claude (Visualizer), no con ningún estilo de diagrama propio del proyecto
  visto en el resto del corpus.
- El contenido mismo — una síntesis de "Mod → Análisis → Documentación →
  Portafolio UTN" con referencia a "objetivo 2", "objetivo 3" y "DR-54" — es
  lenguaje de meta-auditoría (la clasificación de objetivos y decisiones
  registradas, "DR-N", es terminología ya vista en el propio corpus de logs
  de continuidad), no contenido original del mod o de su documentación
  técnica.

**Conclusión razonable, no forzada:** este archivo es casi con certeza un
artefacto generado por un Claude anterior *durante* alguna sesión de este
mismo proceso de auditoría/documentación — probablemente un diagrama
ilustrativo pedido en el momento — y terminó guardado y luego duplicado entre
backups como cualquier otro archivo del escritorio. No es un documento que
el proyecto haya perdido y haya que "rescatar"; es un subproducto del propio
trabajo de análisis.

### 9.5 Veredicto final

- **No requiere rescate ni inclusión en los 274** — no es documentación
  fuente del proyecto, es un artefacto de sesión.
- Se conserva **una sola copia de referencia** (ya extraída en esta sesión)
  por si resulta útil como resumen visual del propio proceso de auditoría,
  sin que esto implique tratarlo como candidato del corpus original.
- **Esta sección queda CERRADA.** Con esto, el pendiente que dejaba abierto
  la sección 8 de v28 queda resuelto — el inventario de "qué quedó fuera de
  los 274" está ahora completo al 100%, sin cabos sueltos.

---

## 10. Estado general al cierre de v29

No quedan pendientes de la línea de auditoría "¿qué quedó fuera de los 274?"
abierta en v28. Los pendientes que siguen en pie son los ya heredados de
sesiones anteriores (ver sección 6.2 de este mismo log): los hilos menores
que no bloquean el rescate, y la tarea estructural del árbol definitivo de
documentación.

---

## Continuación de sesión (2026-07-10, retomada tras corte por límite de mensajes)

**Contexto:** la sesión anterior se quedó sin mensajes justo cuando estaba
a mitad de un barrido general de referencias rotas en el árbol, pedido por
el operador ("¿la documentación interna apunta correctamente a todo, no
queda nada colgado?"). Esta continuación retoma exactamente ese punto.

**Hallazgo adicional antes de retomar:** el zip `IRAM_UNIFICADO_con_git.zip`
que el operador adjuntó para continuar correspondía a un commit de git del
2026-07-08 — anterior a toda la sesión de unificación/rescate/limpieza del
2026-07-10 (§22-§23 de la fuente de verdad). El operador confirmó que había
commiteado su carpeta de referencia antes de arrancar el proceso de
unificación, y nunca volvió a commitear en el camino. Se reconstruyó el
árbol de trabajo combinando el `.git` real (con el historial verdadero) con
el contenido final correcto del árbol (tomado del zip sin git, que sí
reflejaba el estado post-limpieza). Ningún commit se perdió; el resultado
queda con 158 archivos modificados/nuevos/borrados sin commitear, a la
espera de que el operador decida cuándo consolidar esto en un solo commit.

**Barrido de referencias, completado:** se extrajeron todas las rutas con
forma de carpeta citadas entre backticks en cualquier `.md` del árbol y se
cruzaron contra el filesystem real. Resultado: la única referencia colgada
real (fuera de narrativa histórica) era en `INDICE.md`, que todavía
mencionaba dos carpetas eliminadas en la corrección de §23
(`0_REPLANTEOS_Y_DECISIONES/03_rescatados_274/` y
`1_MOD/herramientas_backups_rescatados/`). Se corrigió. El resto de las
menciones a rutas ya inexistentes viven dentro de secciones append-only ya
cerradas de la fuente de verdad (§19-§21) o de logs de auditoría — no se
tocaron, para no reescribir registro histórico (violaría DR-42).

**Renombrado de READMEs de carpeta:** el operador señaló un problema
práctico real — los 11 READMEs vigentes de carpeta se llamaban todos
`README.md` a secas, indistinguibles entre sí al descargarlos sueltos (le
pasó literalmente durante esta sesión, con los 3 READMEs que adjuntó para
darme contexto). Se renombraron los 11 con la ruta de su carpeta incluida
en el nombre (`README__CARPETA.md`, o `README__CARPETA__SUBCARPETA.md`),
mismo espíritu que ya usa `readmes_indices_historicos/` pero sin hash, ya
que estos son únicos por definición. Ver §24.3 de la fuente de verdad para
la tabla completa de renombrados.

Ver §23 y §24 de `FUENTE_DE_VERDAD_IRAM_2026-07-10_12.md` para el detalle
completo de ambos temas (la corrección de duplicados que motivó esta
continuación, y el cierre del barrido + renombrado).
