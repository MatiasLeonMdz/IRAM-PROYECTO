# 03_auditoria_continuidad/

## Qué contiene
Verificación de integridad física de archivos/zips del proyecto, sesiones del
06 y 07/07 — anterior y distinta a la purga de `_CUARENTENA_DUPLICADOS/`
(§20 de la fuente de verdad).

## Archivos
- `SESSION_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` / `...-07.md` — logs de
  la auditoría
- `CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md` — transcripción de la
  sesión de auditoría
- `colisiones_verificadas_2026-07-06.txt` — 76 grupos con nombre repetido en
  la misma carpeta, 43 con contenido genuinamente distinto pese al nombre
- `PASO_0_grupos_divergentes_checklist.md` (150 líneas) — checklist base,
  revisión de los 43 grupos
- `PASO_0_grupos_divergentes_checklist 2.md` (243 líneas) — **la vigente**:
  mismas primeras 150 líneas que la base, agrega al final la sección "Grupo A
  resuelto" con hallazgos nuevos sobre el origen del error "democratización"
  (ver DR-22 en `0_REPLANTEOS_Y_DECISIONES/`) y la fecha de entrega de la
  diplomatura UTN. No es un duplicado — es la misma relación
  base→extendida que tienen las versiones de `FUENTE_DE_VERDAD` entre sí.
  **Conservar ambas**: la base como referencia rápida de los 13 casos con
  contenido real, la `2.md` para el detalle del Grupo A.

## Conclusión de esta auditoría
Ningún caso de los 13 grupos revisados con contenido real resultó ser un
duplicado seguro de borrar — motivo por el cual la purga real de duplicados
se hizo después, sobre `_CUARENTENA_DUPLICADOS/` (557 archivos, ver §20 de
la fuente de verdad), que sí eran 100% redundantes verificados por hash.
