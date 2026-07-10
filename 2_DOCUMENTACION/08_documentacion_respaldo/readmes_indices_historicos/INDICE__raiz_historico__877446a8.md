# ÍNDICE — Proyecto IRAM
Guía de 30 segundos: ¿qué carpeta mirar según tu pregunta?

## ¿Tu pregunta es sobre...?

**El mod en sí (código, versiones, mecánicas de juego)** → `1_MOD/`

**Cómo se documentó el proceso de creación del mod / metodología de trabajo con Claude (Paper C1, Skill C2)** → `2_DOCUMENTACION/`

**El análisis A/B, la diplomatura UTN, o el portafolio final** → `3_ANALISIS/` (ver `tarea_UTN/` y `portafolio/` adentro)

**El estado actual y las decisiones vigentes de TODO el proyecto** → `FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md` (en esta misma carpeta) — leer primero, siempre

**Contexto histórico de cómo evolucionó la documentación (wiki de wikis)** → `WIKI_DOCUMENTACION_v3.md` (en esta misma carpeta)

**Versiones anteriores de la fuente de verdad (histórico, no citable como vigente)** → `00_fuente_de_verdad/`

**Material descartado pero conservado por precaución** → `00b_descartables/`

**Archivos duplicados (histórico)** → `_CUARENTENA_DUPLICADOS/` — PURGADA el 2026-07-08 (557 archivos, verificados por hash antes de borrar, ver README de la carpeta). Vacía, se conserva solo como registro.

**Un script de auditoría/verificación reusable** → `verificar_iram.py` (raíz)

## Regla de oro
Si tu sesión es corta: leé `FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md` primero, después este índice para saber dónde profundizar. No releas `_CUARENTENA_DUPLICADOS/` ni `00_fuente_de_verdad/` salvo que necesites evidencia histórica puntual.

## Estructura de primer nivel

```
IRAM PROYECTO/
├── FUENTE_DE_VERDAD_IRAM_2026-07-07_11.md   ← leer primero
├── WIKI_DOCUMENTACION_v3.md
├── INDICE.md                                 ← este archivo
├── verificar_iram.py
├── 1_MOD/              → el mod (Objetivo 1)
├── 2_DOCUMENTACION/    → proceso y metodología (Objetivo 2)
├── 3_ANALISIS/         → análisis A/B + UTN + portafolio (Objetivo 3)
├── 00_fuente_de_verdad/    → histórico, no vigente
├── 00b_descartables/       → descartado, conservado por precaución
└── _CUARENTENA_DUPLICADOS/ → vacía, purgada 2026-07-08 (ver README)
```

Cada carpeta de primer nivel (`1_MOD/`, `2_DOCUMENTACION/`, `3_ANALISIS/`, `00_fuente_de_verdad/`, `00b_descartables/`, `_CUARENTENA_DUPLICADOS/`) tiene su propio `README.md` con más detalle sobre qué contiene y qué NO va ahí.

---
*Generado en la sesión de reorganización 2026-07-08, tarea #19 (§17.3/§18.1 de la fuente de verdad).*
