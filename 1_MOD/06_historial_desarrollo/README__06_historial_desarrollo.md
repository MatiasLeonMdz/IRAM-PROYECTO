# 06_historial_desarrollo/

Historiales narrativos del desarrollo del mod IRAM: versiones sucesivas de
un relato continuo del proceso de desarrollo (`IRAM_historial_desarrollo_2`
a `_5`), cada una con una variante `_LIMPIO`/`_clean` de limpieza posterior,
más los prompts de las etapas de limpieza y unificación
(`IRAM_Prompt_Etapa1_Limpieza.md`, `IRAM_Prompt_Etapa2_Unificacion.md`) y un
historial unificado (`IRAM_Historial_Unificado_v2.md`).

Es documentación de proceso/narrativa, no el mod en sí ni su código — por
eso vive en `1_MOD/` como historial de desarrollo, separado de `game/` y de
los `mod_pack_*` (que son snapshots reales del mod y no se tocan).

## Nota sobre bug de encoding corregido

Los archivos `IRAM_Diseñador1_Historial.md` y
`IRAM_Diseñador1_Historial_LIMPIO.md` tenían el nombre corrupto
(`IRAM_Dise#U00f1ador1_Historial...`) por el mismo bug de compresión del
zip diagnosticado y corregido en `3_ANALISIS/02_charlas_diseño_analisis/`
(la "ñ" se guardaba como `#U00f1` en vez de UTF-8). Se corrigió en la
sesión del 10-07-2026: si el nombre vuelve a aparecer corrupto en un zip
nuevo, es el mismo bug reapareciendo (típicamente por comprimir sin la
opción `-X` de `zip`), no un cambio real de nombre.
