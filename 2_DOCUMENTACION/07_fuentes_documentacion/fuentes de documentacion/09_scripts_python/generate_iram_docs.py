#!/usr/bin/env python3
"""
generate_iram_docs.py — Genera historial unificado y hitos IRAM
Uso: python3 generate_iram_docs.py [fecha]
     Ej: python3 generate_iram_docs.py 2026-06-10
Output:
  IRAM_historial_unificado_[fecha].md
  IRAM_hitos_metodologicos_[fecha].md
"""

import json
import sys
import os
from datetime import datetime

DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-06-10"

ACCOUNTS = ["claude_1", "claude_2", "claude_3", "claude_4", "claude_5"]
INPUT_DIR = "/home/claude"

HITO_LABELS = {
    "primeros_scripts":        "Primeros scripts del mod",
    "primer_session_log":      "Primer SESSION_LOG",
    "primera_wiki":            "Primera wiki (ACTIVE)",
    "separacion_active_archive": "Separación ACTIVE / ARCHIVE",
    "primer_prompt_maestro":   "Primer PROMPT_MAESTRO",
    "primeros_wip":            "Primeros WIPs (remake v5)",
    "primera_auditoria":       "Primera auditoría formal",
    "sistema_versiones":       "Sistema de versiones vX.X.X",
    "minilogs":                "MINILOGs por tarea",
    "zips_wip":                "ZIPs WIP por tarea",
}


# ── CARGA ────────────────────────────────────────────────────────────────────

def load_all():
    all_convs = []
    all_data = {}
    for acc in ACCOUNTS:
        path = os.path.join(INPUT_DIR, f"{acc}_processed.json")
        if not os.path.exists(path):
            print(f"  ⚠ No encontrado: {path}")
            continue
        with open(path) as f:
            d = json.load(f)
        all_data[acc] = d
        for conv in d["conversations"]:
            all_convs.append(conv)

    # Ordenar por fecha de creación
    all_convs.sort(key=lambda c: c["created_at"])
    return all_convs, all_data


# ── HELPERS ──────────────────────────────────────────────────────────────────

def fmt_duration(mins):
    if mins <= 0:
        return "< 1 min"
    if mins < 60:
        return f"{mins} min"
    h = mins // 60
    m = mins % 60
    return f"{h}h {m}m" if m else f"{h}h"


def msg_preview(msg, max_chars=600):
    """Genera preview de un mensaje para el historial."""
    text = msg.get("text", "")
    is_log = msg.get("is_log", False)
    tools = msg.get("tools", [])
    hitos = msg.get("hitos", [])
    sender = msg.get("sender", "?")
    ts = msg.get("ts_short", "??:??")
    block = msg.get("block", 1)
    new_block = msg.get("new_block", False)
    pause = msg.get("pause_min", 0)

    parts = []

    # Marcador de bloque temático
    if new_block:
        parts.append(f"\n  ┈┈ **[Bloque {block}** — pausa {pause} min] ┈┈")

    # Header del mensaje
    sender_icon = "👤" if sender == "human" else "🤖"
    hito_flags = ""
    if hitos:
        hito_flags = " 🏁 " + ", ".join(f"`{h}`" for h in hitos)

    # Contenido
    if is_log:
        content_str = f"    *{text}*"
    elif not text:
        if tools:
            content_str = f"    *[Solo herramientas]*"
        else:
            content_str = "    *[Vacío]*"
    elif len(text) <= max_chars:
        content_str = indent_text(text, "    ")
    else:
        content_str = indent_text(text[:max_chars], "    ")
        content_str += f"\n    *[...{len(text) - max_chars} chars más — total {len(text)} chars]*"

    # Tools usadas
    tools_str = ""
    if tools:
        tools_str = "\n    🔧 " + " | ".join(tools[:6])
        if len(tools) > 6:
            tools_str += f" + {len(tools)-6} más"

    line = f"  **{ts}** {sender_icon}{hito_flags}"
    return line + "\n" + content_str + tools_str


def indent_text(text, prefix="    "):
    """Indenta texto para el MD."""
    lines = text.split("\n")
    result = []
    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
        if in_code or stripped.startswith("```"):
            result.append(prefix + line)
        else:
            result.append(prefix + line)
    return "\n".join(result)


def conv_header(conv, idx_global, total_convs):
    """Genera header de conversación para el historial."""
    period_icon = "⚔️" if conv["period"] == "IRAM" else "📘"
    hito_list = conv.get("hitos", [])
    hito_str = ""
    if hito_list:
        hito_str = "\n  🏁 **Hitos:** " + ", ".join(f"`{h}`" for h in hito_list)

    tools_str = ""
    if conv.get("tools_used"):
        tools_str = "\n  🔧 **Tools:** " + ", ".join(conv["tools_used"][:8])

    blocks = conv.get("block_count", 1)
    block_str = f" | {blocks} bloques" if blocks > 1 else ""

    header = f"""
---

### [{conv['date']}] {period_icon} **{conv['account'].upper()}** — {conv['name'][:70]}
  `uuid: {conv['uuid'][:12]}...`
  📊 {conv['msg_count']} msgs (raw: {conv['msg_count_raw']}, dups: -{conv['dup_count']}) | ⏱ {fmt_duration(conv['duration_min'])}{block_str}{hito_str}{tools_str}
"""
    return header


# ── HISTORIAL UNIFICADO ──────────────────────────────────────────────────────

def generate_historial(all_convs, output_path):
    """Genera el historial unificado completo."""
    print(f"Generando historial unificado → {output_path}")

    # Estadísticas globales
    total_msgs = sum(c["msg_count"] for c in all_convs)
    total_dups = sum(c["dup_count"] for c in all_convs)
    iram_convs = [c for c in all_convs if c["period"] == "IRAM"]
    pre_convs = [c for c in all_convs if c["period"] == "pre-IRAM"]
    accounts_present = sorted(set(c["account"] for c in all_convs))

    with open(output_path, "w", encoding="utf-8") as f:

        # ── ENCABEZADO ─────────────────────────────────────────────────────
        f.write(f"""# IRAM — Historial Unificado
**Generado:** {DATE}
**Fuente:** {', '.join(accounts_present)}

---

## ESTADÍSTICAS GLOBALES

| Métrica | Valor |
|---------|-------|
| Total conversaciones | {len(all_convs)} |
| Total mensajes (post-dedup) | {total_msgs} |
| Duplicados removidos | {total_dups} |
| Período pre-IRAM | {len(pre_convs)} convs ({len([c for c in pre_convs for a in [1]])} sesiones) |
| Período IRAM (desde 2026-04-09) | {len(iram_convs)} convs |

| Cuenta | Convs | Msgs | Período |
|--------|-------|------|---------|
""")
        for acc in ACCOUNTS:
            acc_convs = [c for c in all_convs if c["account"] == acc]
            if acc_convs:
                acc_msgs = sum(c["msg_count"] for c in acc_convs)
                d_start = min(c["date"] for c in acc_convs)
                d_end = max(c["date"] for c in acc_convs)
                f.write(f"| {acc.upper()} | {len(acc_convs)} | {acc_msgs} | {d_start} → {d_end} |\n")

        f.write("\n---\n\n")

        # ── ÍNDICE RÁPIDO ───────────────────────────────────────────────────
        f.write("## ÍNDICE RÁPIDO (conversaciones con hitos)\n\n")
        for i, conv in enumerate(all_convs):
            if conv["hitos"]:
                hitos_str = ", ".join(conv["hitos"])
                f.write(f"- `{conv['date']}` **{conv['account'].upper()}** — {conv['name'][:55]} — *{hitos_str}*\n")

        f.write("\n---\n\n")

        # ── BLOQUE PRE-IRAM ─────────────────────────────────────────────────
        if pre_convs:
            f.write("## PRE-IRAM (oct 2025 – abr 2026)\n\n")
            f.write(f"> *{len(pre_convs)} conversaciones anteriores al inicio de IRAM (R6: 2026-04-09).*\n")
            f.write("> *Marcadas por completitud del registro — no son desarrollo del mod.*\n\n")

            for conv in pre_convs:
                f.write(conv_header(conv, 0, 0))
                # En pre-IRAM: solo mostrar los primeros 2 mensajes por conversación
                for msg in conv["messages"][:2]:
                    f.write(msg_preview(msg, max_chars=300) + "\n")
                if conv["msg_count"] > 2:
                    f.write(f"\n  *[{conv['msg_count'] - 2} msgs adicionales no mostrados — período pre-IRAM]*\n")

            f.write("\n---\n\n")

        # ── BLOQUE IRAM ─────────────────────────────────────────────────────
        f.write("## IRAM (2026-04-09 en adelante)\n\n")

        current_month = ""
        for conv in iram_convs:
            # Separador por mes
            month = conv["date"][:7]
            if month != current_month:
                month_label = datetime.strptime(month, "%Y-%m").strftime("%B %Y").upper()
                f.write(f"\n### ── {month_label} ──\n")
                current_month = month

            f.write(conv_header(conv, 0, 0))

            if conv["msg_count"] == 0:
                f.write("  *[Sin mensajes]*\n")
                continue

            # Decidir nivel de detalle según relevancia
            has_hitos = bool(conv["hitos"])
            is_long = conv["msg_count"] > 30

            if has_hitos or not is_long:
                # Mostrar todos los mensajes
                max_preview = 800 if has_hitos else 400
                for msg in conv["messages"]:
                    f.write(msg_preview(msg, max_chars=max_preview) + "\n")
            else:
                # Conversación larga sin hitos: mostrar primeros 5 y últimos 3
                for msg in conv["messages"][:5]:
                    f.write(msg_preview(msg, max_chars=300) + "\n")
                if conv["msg_count"] > 8:
                    f.write(f"\n  *[... {conv['msg_count'] - 8} msgs en el medio ...]*\n")
                for msg in conv["messages"][-3:]:
                    f.write(msg_preview(msg, max_chars=300) + "\n")

        f.write("\n---\n\n*IRAM Historial Unificado — " + DATE + "*\n")

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  ✅ Historial generado — {size_kb:.0f} KB")


# ── HITOS METODOLÓGICOS ──────────────────────────────────────────────────────

def generate_hitos(all_data, output_path):
    """Genera el documento de hitos con las primeras apariciones cross-account."""
    print(f"Generando hitos metodológicos → {output_path}")

    # Consolidar: para cada hito, la PRIMERA aparición entre todos los accounts
    global_hitos = {}
    all_conv_hitos = []

    for acc, data in all_data.items():
        for hito, info in data["hito_first_seen"].items():
            existing = global_hitos.get(hito)
            if existing is None or info["date"] < existing["date"]:
                global_hitos[hito] = dict(info, account=acc)

        # Recopilar todas las conversaciones con hitos para la sección de evidencia
        for conv in data["conversations"]:
            for h in conv["hitos"]:
                all_conv_hitos.append({
                    "hito": h,
                    "date": conv["date"],
                    "account": acc,
                    "conv_name": conv["name"][:60],
                    "conv_uuid": conv["uuid"][:12],
                    "period": conv["period"],
                })

    # Ordenar evidencia por hito + fecha
    all_conv_hitos.sort(key=lambda x: (x["hito"], x["date"]))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"""# IRAM — Hitos Metodológicos
**Generado:** {DATE}
**Fuente:** {', '.join(ACCOUNTS)}

> Primera aparición verificada de cada hito en los 5 historiales.
> Fechas obtenidas por búsqueda de keywords en el contenido de mensajes.
> ⚠ Requieren revisión manual para confirmar contexto (ver sección EVIDENCIA).

---

## CHECKLIST DE HITOS

| Estado | Hito | Primera aparición | Cuenta | Conversación |
|--------|------|------------------|--------|-------------|
""")
        for hito_key, label in HITO_LABELS.items():
            info = global_hitos.get(hito_key)
            if info:
                status = "✅"
                date = info["date"]
                acc = info["account"].upper()
                name = info["conv_name"][:45]
            else:
                status = "❌"
                date = "no encontrado"
                acc = "—"
                name = "—"
            f.write(f"| {status} | **{label}** | `{date}` | {acc} | {name} |\n")

        f.write("\n---\n\n")

        # ── SECCIÓN DE EVIDENCIA ────────────────────────────────────────────
        f.write("## EVIDENCIA POR HITO\n\n")
        f.write("> Todas las conversaciones donde aparece el keyword de cada hito.\n")
        f.write("> La primera fila marcada ⭐ es la primera aparición global.\n\n")

        for hito_key, label in HITO_LABELS.items():
            convs_with_hito = [c for c in all_conv_hitos if c["hito"] == hito_key]
            first_date = global_hitos.get(hito_key, {}).get("date", "?")

            f.write(f"### {label}\n\n")
            if not convs_with_hito:
                f.write("*No encontrado en ningún historial.*\n\n")
                continue

            f.write(f"| Fecha | Cuenta | Período | Conversación |\n")
            f.write(f"|-------|--------|---------|-------------|\n")

            seen_dates = set()
            for c in convs_with_hito:
                key = (c["date"], c["account"])
                if key in seen_dates:
                    continue
                seen_dates.add(key)
                star = "⭐ " if c["date"] == first_date and c["account"] == global_hitos.get(hito_key, {}).get("account") else ""
                f.write(f"| {star}`{c['date']}` | {c['account'].upper()} | {c['period']} | {c['conv_name']} |\n")
            f.write("\n")

        f.write("---\n\n")

        # ── NOTAS DE REVISIÓN ───────────────────────────────────────────────
        f.write("""## NOTAS PARA REVISIÓN MANUAL

Los siguientes hitos requieren revisión del contenido real del mensaje
para confirmar que la detección es correcta (no solo keyword match):

1. **primer_prompt_maestro** — Keyword "PASO 1" aparece en contextos genéricos.
   Verificar que la primera aparición sea el PROMPT_MAESTRO real, no una referencia casual.

2. **separacion_active_archive** — "ARCHIVE" puede referirse a cualquier archivo.
   Verificar que sea el momento donde se crea la separación ACTIVE/ARCHIVE del wiki.

3. **primera_wiki** — Verificar que sea la creación del IRAM_TECHNICAL_WIKI, no otra wiki.

4. **sistema_versiones** — Patrones como `v1.0` aparecen en contextos no-IRAM.
   La primera aparición relevante para IRAM es cuando se adopta el sistema de versiones del mod.

5. **primeros_scripts** — Keywords de código PDX son muy comunes desde 2026-04-16.
   El hito real es la sesión donde se decide crear IRAM como mod propio.

6. **primer_session_log** — Verificar que sea el primer SESSION_LOG del formato actual,
   no cualquier referencia a "logs de sesión".

---

*IRAM Hitos Metodológicos — """ + DATE + "*\n")

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  ✅ Hitos generados — {size_kb:.0f} KB")


# ── SESSION LOG DE DOCUMENTACIÓN ─────────────────────────────────────────────

def generate_session_log(all_convs, output_path):
    """Genera el SESSION_LOG de esta sesión de documentación."""
    total_msgs = sum(c["msg_count"] for c in all_convs)
    total_dups = sum(c["dup_count"] for c in all_convs)
    iram_convs = [c for c in all_convs if c["period"] == "IRAM"]
    pre_convs = [c for c in all_convs if c["period"] == "pre-IRAM"]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"""# SESSION LOG — Documentación IRAM
**Tipo:** Plantilla A — Procesamiento de historial
**Fecha:** {DATE}
**Ejecutado por:** Claude (Sonnet 4.6) — sesión de documentación

---

## QUÉ SE HIZO

1. ✅ Exploración de estructura de los 5 conversations.json
   - Confirmado: cada zip contiene `conversations.json` (+ users.json + projects.json)
   - Confirmado: mensajes de assistant usan `content[type=text]` como campo canónico
     (el campo `text` incluye "not supported" por tool_use blocks)

2. ✅ Script `process_iram_v2.py` creado y ejecutado en los 5 accounts
   - Extrae texto limpio, deduplicación, detección de hitos, tools usadas
   - Detecta logs de juego → trunca (R3)
   - Identifica bloques temáticos por pausa > 30 min

3. ✅ Archivos generados:
   - `IRAM_historial_unificado_{DATE}.md`
   - `IRAM_hitos_metodologicos_{DATE}.md`
   - `SESSION_LOG_DOCUMENTACION_{DATE}.md` (este archivo)

---

## ESTADÍSTICAS DEL HISTORIAL

| Cuenta | Convs | Msgs (post-dedup) | Dups removidos |
|--------|-------|------------------|---------------|
""")
        for acc in ACCOUNTS:
            acc_convs = [c for c in all_convs if c["account"] == acc]
            if acc_convs:
                acc_msgs = sum(c["msg_count"] for c in acc_convs)
                acc_dups = sum(c["dup_count"] for c in acc_convs)
                f.write(f"| {acc.upper()} | {len(acc_convs)} | {acc_msgs} | {acc_dups} |\n")

        f.write(f"| **TOTAL** | **{len(all_convs)}** | **{total_msgs}** | **{total_dups}** |\n\n")
        f.write(f"""
- Período pre-IRAM: {len(pre_convs)} conversaciones (oct 2025 – abr 2026)
- Período IRAM: {len(iram_convs)} conversaciones (2026-04-09 en adelante)
- Claude 3 y Claude 5: íntegramente IRAM

---

## HITOS DETECTADOS (requieren revisión manual)

Ver `IRAM_hitos_metodologicos_{DATE}.md` para tabla completa.

Fechas primera aparición por keyword (pendiente verificación):
- primeros_scripts: 2026-04-16 (CLAUDE_1)
- primer_session_log: 2026-05-25 (CLAUDE_1)
- primera_wiki: 2026-05-28 (CLAUDE_1)
- separacion_active_archive: 2026-04-16 (CLAUDE_1) — probablemente falso positivo
- primer_prompt_maestro: 2026-04-22 (CLAUDE_1) — probablemente falso positivo
- primera_auditoria: 2026-05-28 (CLAUDE_1)
- sistema_versiones: 2026-04-13 (CLAUDE_1) — contexto pre-IRAM posible
- minilogs: 2026-06-06 (CLAUDE_1)
- primeros_wip: 2026-06-06 (CLAUDE_1)
- zips_wip: 2026-05-05 (CLAUDE_1)

---

## QUÉ FALTA

- [ ] Revisión manual de falsos positivos en hitos (especialmente `separacion_active_archive`,
      `primer_prompt_maestro`, `sistema_versiones`)
- [ ] Verificar contexto exacto de la conversación 45 (2026-05-16, claude_1):
      "PROMT PARA DOCUMENTACION DE CHATS" — primera referencia al sistema de documentación
- [ ] Verificar conversación 6 (2026-04-09, claude_1) — primer mensaje del período IRAM
- [ ] Identificar la sesión donde se adoptó formalmente el nombre "IRAM"
- [ ] Plantilla B: análisis de gaps (conocimiento en chats pero no en wiki)
- [ ] Plantilla C: construcción del SKILL.md

---

## ARCHIVOS GENERADOS

| Archivo | Tamaño | Descripción |
|---------|--------|-------------|
| `IRAM_historial_unificado_{DATE}.md` | — | Timeline completo todos los Claudes |
| `IRAM_hitos_metodologicos_{DATE}.md` | — | Checklist de hitos con evidencia |
| `SESSION_LOG_DOCUMENTACION_{DATE}.md` | — | Este archivo |

---

## PREGUNTA DE CIERRE (R14)

*¿Qué se decidió hoy que no estaba documentado antes?*

→ La estructura real de los conversations.json exportados por Claude:
  - `text` en mensajes de assistant incluye placeholders "not supported" por tool_use
  - El campo canónico para assistant es `content[type=text]`
  - Los zips contienen también `projects.json` y en claude_5 `memories.json`
  - Claude 1 y 2 empiezan 2025-10-22; Claude 3 y 5 empiezan directo en IRAM (2026-04-16/17)
  - Claude 4 tiene 3 archivos `projects.json` en su zip

*Cuándo:* {DATE}
*Por qué:* Descubierto al explorar la estructura del JSON antes de escribir el procesador.

---

*SESSION LOG DOCUMENTACIÓN IRAM — {DATE}*
*Plantilla A completada | script process_iram_v2.py generado*
*Próxima sesión: Plantilla B (análisis de gaps) o revisión manual de hitos*
""")

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  ✅ Session log generado — {size_kb:.0f} KB")


# ── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"=== Generador IRAM Docs — {DATE} ===\n")

    all_convs, all_data = load_all()
    print(f"Cargadas {len(all_convs)} conversaciones de {len(all_data)} accounts\n")

    historial_path = f"/home/claude/IRAM_historial_unificado_{DATE}.md"
    hitos_path = f"/home/claude/IRAM_hitos_metodologicos_{DATE}.md"
    log_path = f"/home/claude/SESSION_LOG_DOCUMENTACION_{DATE}.md"

    generate_historial(all_convs, historial_path)
    generate_hitos(all_data, hitos_path)
    generate_session_log(all_convs, log_path)

    print("\n=== ENTREGABLES ===")
    for path in [historial_path, hitos_path, log_path]:
        kb = os.path.getsize(path) / 1024
        print(f"  {path.split('/')[-1]} — {kb:.0f} KB")
