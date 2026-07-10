# tarea_UTN/

Material de una cursada de UTN (Ciencia de Datos / IA), ajeno al desarrollo
del mod IRAM en sí — se conserva en el proyecto por estar en la misma
cuenta/backup de origen, no porque forme parte del corpus IRAM.

## Contenido

- Subcarpeta `consignas/` — las 3 consignas en `.md`
  (`Consigna.md`, `Consigna_1.md`, `Consigna_2.md`), más su versión en
  `.pdf` (`Consigna.pdf`, `Consigna_1.pdf`, `Consigna_2.pdf`)
- 16 archivos de contenido de módulos (`Modulo1_Unidad1_...md` a
  `Modulo4_Unidad4_...md`), cubriendo Ciencia de Datos, análisis
  exploratorio, Machine Learning, NLP, visión por computadora, y
  automatización no-code/low-code

## Duplicado resuelto

La raíz de esta carpeta tenía copias sueltas de las 3 consignas
(`Consigna.md`, `Consigna_1.md`, `Consigna_2.md`), **idénticas** (ignorando
CRLF/LF) a sus contrapartes dentro de `consignas/`. El operador confirmó
`consignas/` como versión canónica —es la más completa, ya que además
incluye el `.pdf` de cada consigna— y se eliminaron las 3 copias sueltas de
la raíz con `git rm` (ítem #9 de pendientes organizativos, resuelto).
