# datos_config_mod_rescatados/

5 archivos de configuración del mod (`exodus_decisions.txt`, `exodus_events.txt`,
`exodus_on_action.txt`, `exodus_scripted_effects.txt`, `exodus_units.txt`),
rescatados de las copias de seguridad viejas en la sesión de unificación del
2026-07-10, verificados por hash como contenido único (sin gemelo en el resto
del árbol).

De los 8 archivos que se ubicaron acá originalmente, 3 (`tgl_decisions.txt`,
`tlv_decisions.txt`, `tlv_events.txt`) resultaron ser, en una revisión
posterior (sesión de auditoría del 2026-07-10, continuación), duplicados
exactos de archivos ya existentes en
`1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/` (con
otro nombre de archivo — `exodos_decisions_tgl.txt`, `exodos_decisions_tlv.txt`,
`events/tlv_events.txt` — mismo contenido, verificado por hash normalizado) —
se eliminaron con `git rm`. Ver
`2_DOCUMENTACION/08_documentacion_respaldo/README__2_DOCUMENTACION__08_documentacion_respaldo.md`
para el detalle de por qué pasó esto en varias carpetas de este mismo rescate.
