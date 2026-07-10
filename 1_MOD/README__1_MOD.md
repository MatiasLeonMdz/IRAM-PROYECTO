# 1_MOD/

## Qué contiene
Todo lo relacionado directamente con el mod IRAM en sí — código, versiones empacadas, datos crudos de origen y material de referencia del juego base.

## Subcarpetas
- `IRAM mod v5/` — línea vigente (v4.3.8 → v4.3.16) + repo Git del desarrollo
- `IRAM_legacy v1 v2 v3 v4/` — versiones históricas previas al salto arquitectónico v2→v3
- `corpus_A_crudo/` — conversaciones crudas de las 5 cuentas Claude (dato fuente sin procesar)
- `game/` — archivos de referencia de Imperator: Roma (base, no es el mod)
- `mod_pack_IRAM_v5_5_2026-06-09_03-22/` — mod v5.5 empacado, versión final. (La
  copia duplicada `(2)` de esta carpeta se purgó el 2026-07-08, verificada
  100% idéntica por `diff -rq` antes de borrar — ver `FUENTE_DE_VERDAD` para
  el registro completo de esa sesión.)
- `06_historial_desarrollo/` — sesiones de desarrollo técnico del mod (código,
  mecánicas, eventos), movida acá desde `2_DOCUMENTACION/` el 2026-07-08 por
  ser desarrollo estricto del mod, no documentación del proceso
- `achievements_imperator.xlsx`, `wiki_imperator.txt` — referencia del juego base

## Punto de entrada
Si buscás la versión jugable más reciente: `mod_pack_IRAM_v5_5_2026-06-09_03-22/`.
Si buscás el historial técnico completo: `IRAM mod v5/` → repo Git, o
`06_historial_desarrollo/` para las sesiones de diseño previas al repo.

## Replanteos que afectaron a esta sección
El mod fue objeto de decisiones tomadas en la serie de replanteo transversal
del proyecto (no vive acá, ver `0_REPLANTEOS_Y_DECISIONES/`):
- **DR-22** — origen verificado de la frase "democratización" en el marco teórico
- **DR-23** — gaps de conocimiento del mod ya mapeados (no rehacer)
- **DR-24** — convención de nombres `AAAA-MM-DD_HH-MM`, originada en una regla ya existente del mod

Ver `0_REPLANTEOS_Y_DECISIONES/01_logs_replanteo/SESSION_LOG_REPLANTEO_2026-07-03*`.
