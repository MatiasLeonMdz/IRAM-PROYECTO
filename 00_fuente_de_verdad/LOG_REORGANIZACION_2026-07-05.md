# LOG DE REORGANIZACIÓN FÍSICA — 2026-07-05

**Corresponde a:** Tarea 1 de PRÓXIMAS TAREAS (aplicar estructura de carpetas DR-27), ejecutada tras confirmación del operador sobre la corrección de clasificación Corpus A/B (candidato a DR-50, ver nota al final).
**Método:** movimiento de archivos únicamente. **No se renombró ningún archivo** (eso es DR-32, plan de 3 capas, todavía pendiente). No se abrió ni modificó el contenido de ningún archivo, salvo lectura de nombres para clasificar.
**Verificación:** 1991 archivos totales antes y después del movimiento — conteo exacto, ninguno se perdió ni se duplicó.

---

## Estructura resultante

```
IRAM PROYECTO/
├── 1_MOD/                          (1320 archivos — fuera de alcance, no tocar)
│   ├── game/
│   ├── IRAM mod v5/                (sin los 10 docs, movidos a Documentación)
│   ├── IRAM_legacy v1 v2 v3 v4/
│   ├── mod_pack_IRAM_v5_5_2026-06-09_03-22/         ← rescatado de "fuentes de documentacion" (DR-48)
│   ├── mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/     ← ídem
│   ├── corpus_A_crudo/             ← 5 data-*-batch-0000.zip (corrección a DR-46, ver nota)
│   ├── achievements_imperator.xlsx
│   └── wiki_imperator.txt
│
├── 2_DOCUMENTACION/                 (241 archivos)
│   ├── 01_logs_replanteo/           (todos los SESSION_LOG_REPLANTEO_* sueltos de la raíz)
│   ├── 02_charlas_y_resumenes/      (CHARLA REPLANTEO 1/2, RESUMEN_CHARLAS*, SESION TRUNCADA, sigue log.md)
│   ├── 03_prueba_fuga_memoria/      (instruccion_/resultado_/memoria_claude_volcado/volcado_memoria)
│   ├── 04_corpus_A_mod_docs/        (10 docs reales que vivían dentro de "IRAM mod v5/")
│   ├── 05_corpus_B_crudo/           (documentacion claude 1.zip … 5.zip)
│   ├── 06_historial_desarrollo_mod/ (resto de "historial viejo/", sin los data-*.zip)
│   ├── 07_fuentes_documentacion/    ("fuentes de documentacion/" completa, sin subcopia anidada ni mod packs)
│   │   └── (incluye claude_1_processed.json … claude_5_processed.json — Corpus B procesado, DR-47 sigue abierto)
│   └── 08_documentacion_respaldo/   (carpeta "DOCUMENTACION/" completa — copia de respaldo, DR-45)
│
├── 3_PORTAFOLIO_UTN/                (6 archivos)
│   └── consignas/                   (Consigna.md/pdf, Consigna_1.*, Consigna_2.*)
│
└── _CUARENTENA_DUPLICADOS/          (424 archivos — duplicados byte-a-byte, NO borrados, solo aislados)
    ├── fuentes de documentacion (subcopia anidada)/       (161 archivos, dup exacto del padre)
    └── documentacion iram 10-06-2026 00.30 (subcopia anidada)/  (261 archivos, dup exacto del padre)
```

---

## Corrección aplicada esta sesión (candidato a DR-50)

DR-46 (en `SESSION_LOG_REPLANTEO_2026-07-05_00-32.md`) etiquetó los 5 `data-*-batch-0000.zip` como "Corpus B crudo adicional". El operador corrigió esto en conversación: por la definición de origen (*"el mod IRAM (Corpus A) y el proceso de documentación de IRAM (Corpus B)"*) y por timestamp (comienzos de enero de 2026, anterior a que existiera el proceso de documentación), estos 5 archivos son **Corpus A crudo** — conversaciones sobre el desarrollo del mod, no sobre su documentación. Se movieron a `1_MOD/corpus_A_crudo/` en lugar de a `2_DOCUMENTACION/05_corpus_B_crudo/`.

Los `claude_N_processed.json` de DR-47 sí se confirmaron como Corpus B (procesado) y quedaron sin mover, dentro de `07_fuentes_documentacion/`.

**Esto no reescribe DR-46 en el log existente — queda para que la próxima sesión lo incorpore formalmente como DR-50, citando este log y la conversación donde se confirmó.**

---

## Pendiente — no se tocó en este paso

- **Duplicados dentro de `_CUARENTENA_DUPLICADOS/`**: no se borraron. Es información redundante confirmada por hash MD5, pero la decisión de eliminarlos definitivamente queda para el operador.
- **Renombrado**: nada se renombró. Corresponde al plan de 3 capas de DR-32 (mapa de vigencia → mapa de citas cruzadas → renombrado), todavía no ejecutado.
- **Contenido de `claude_N_processed.json`**: sigue sin abrirse (DR-47 sigue abierto).
- **Contenido de `corpus_A_crudo/*.zip`**: no se abrió su interior, solo se reclasificó su carpeta contenedora.
