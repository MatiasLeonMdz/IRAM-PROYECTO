# corpus_A_crudo/

Exports crudos de conversaciones de Claude relacionadas al desarrollo del
mod IRAM ("corpus A"), sin procesar. Es material fuente, no documentación
organizada — la versión procesada/curada de este corpus vive en
`2_DOCUMENTACION/04_corpus_A_mod_docs/`.

## Contenido

5 batches de exportación, cada uno con su `.zip` original y su carpeta ya
descomprimida (`conversations.json`, `users.json`, `projects/*.json`):

- `data-4fce9ea4-...-batch-0000` (16-05-2026)
- `data-6a75897c-...-batch-0000` (18-05-2026)
- `data-7f3f05d6-...-batch-0000` (18-05-2026)
- `data-a158d766-...-batch-0000` (18-05-2026)
- `data-d64c441d-...-batch-0000` (16-05-2026)

Existían además 4 carpetas `rescatado__*` (`rescatado__data-4fce9ea4`,
`rescatado__data-d64c441d`, `rescatado__data-4fce9ea4-dd95-4`,
`rescatado__data-d64c441d-0410-4`), ya eliminadas — ver nota siguiente.

## Nota sobre las carpetas `rescatado__*` (eliminadas)

Se confirmó que las carpetas `rescatado__*` eran la exportación **previa a
la purga** aplicada durante la consolidación del proyecto: cada batch
`data-*` es el resultado de remover, de esa exportación más amplia,
conversaciones ajenas al proyecto IRAM (de otros mods/juegos — se
identificaron entradas de "Surviving the Aftermath" y "Microcivilization").
Comparación por UUID confirmó que cada batch `data-*` está 100% contenido
en su `rescatado__*` correspondiente, con el resto siendo exclusivamente
ese contenido ajeno. Con esto confirmado por el operador, las carpetas
`rescatado__*` se eliminaron por no aportar nada adicional al corpus del
proyecto. Si en el futuro reaparece una carpeta `rescatado__*` en este
directorio, es señal de una exportación sin purgar, no de material nuevo
legítimo — conviene aplicar el mismo criterio antes de incorporarla.
