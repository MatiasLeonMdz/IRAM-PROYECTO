# 05_corpus_B_crudo/

Exports crudos de conversaciones de Claude, "corpus B" — en paralelo a
`1_MOD/corpus_A_crudo/`, con la misma estructura y el mismo tipo de
contenido sin procesar.

## Contenido

5 batches ("documentacion claude 1" a "5"), cada uno con su `.zip` original
y su carpeta ya descomprimida (`conversations.json`, `users.json`,
`projects/*.json`):

- `documentacion claude 1/` (+ `.zip`)
- `documentacion claude 2/` (+ `.zip`)
- `documentacion claude 3/` (+ `.zip`)
- `documentacion claude 4/` (+ `.zip`)
- `documentacion claude 5/` (+ `.zip`)

Existía además una carpeta `rescatado__documentacion_claude_3/`, ya
eliminada — ver nota siguiente.

## Nota sobre `documentacion claude 3/` y el `rescatado__*` (resuelto)

A diferencia de `corpus_A_crudo`, acá el patrón no era una purga de
contenido ajeno: `documentacion claude 3/conversations.json` (versión
original, 22 conversaciones, todas fechadas 10–20 de junio de 2026) fue
el resultado de una **exportación fallida/incompleta**, confirmada por el
operador. El archivo `rescatado__documentacion_claude_3/conversations__4bff53c0.json`
(104 conversaciones, 16 de abril a 20 de junio de 2026) es la exportación
completa y correcta: contiene las 22 conversaciones originales sin
alteraciones (verificado UUID por UUID y mensaje por mensaje) más 82
conversaciones adicionales genuinas del desarrollo de IRAM (documentación,
bugs, versiones v4.3 a v5.5, backups, etc.) que la exportación fallida
había perdido. Ninguna de esas 82 aparece en ningún otro batch del corpus.

Se reemplazó el contenido de `documentacion claude 3/conversations.json`
por el del rescatado (104 conversaciones) y se eliminó la carpeta
`rescatado__documentacion_claude_3/` por quedar absorbida. El `.zip`
original de la exportación fallida (`documentacion claude 3.zip`) se dejó
sin tocar, como artefacto fuente.
