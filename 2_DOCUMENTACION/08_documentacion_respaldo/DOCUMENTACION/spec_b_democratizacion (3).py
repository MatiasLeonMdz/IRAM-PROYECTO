#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spec_b_democratizacion.py — Rastreo de apariciones del principio de "democratización"
en el historial (Spec B).

Ver SESSION_LOG_CONSOLIDADO_2026-06-18.md, sección "SPEC B — RASTREO DE LA
DEMOCRATIZACIÓN" para el problema que resuelve (DC-06 / PC2) y la lista completa
de términos.

Este script NO decide nada — extrae TODAS las apariciones (con ruido incluido en el
nivel terciario) para que Sesión 3 filtre y reconstruya la cronología real.

USO:
    python3 spec_b_democratizacion.py claude_1_processed.json ... claude_5_processed.json
    (sin argumentos: busca claude_1_processed.json .. claude_5_processed.json en el cwd)

OUTPUT:
    spec_b_democratizacion.json — todas las apariciones, ordenadas cronológicamente.
"""

import json
import re
import sys
from pathlib import Path

CONTEXT_N = 5
CONTEXT_TRUNC = 400
TEXT_TRUNC = 1500

# ============================================================
# NORMALIZACIÓN — idéntico a spec_a_authorship.py, ajustar acá si difiere
# ============================================================

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_conversations(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "conversations" in data and isinstance(data["conversations"], list):
            return data["conversations"]
        for v in data.values():
            if isinstance(v, list):
                return v
        return [data]
    return []


def get_messages(conv):
    if not isinstance(conv, dict):
        return []
    for key in ("chat_messages", "messages", "msgs"):
        if key in conv and conv[key]:
            return conv[key]
    return []


def get_text(msg):
    if not isinstance(msg, dict):
        return ""
    for key in ("text", "content"):
        if key in msg and msg[key]:
            val = msg[key]
            if isinstance(val, str):
                return val
            if isinstance(val, list):
                parts = []
                for block in val:
                    if isinstance(block, dict):
                        parts.append(block.get("text", ""))
                    elif isinstance(block, str):
                        parts.append(block)
                return "\n".join(p for p in parts if p)
    return ""


def get_sender(msg):
    val = (msg.get("sender") or msg.get("role") or "").lower()
    if val in ("human", "user"):
        return "human"
    if val in ("assistant", "bot", "claude"):
        return "assistant"
    return val or "unknown"


def get_conv_name(conv):
    return conv.get("name") or conv.get("title") or conv.get("uuid") or "sin_nombre"


def get_conv_uuid(conv, fallback_idx):
    return conv.get("uuid") or conv.get("id") or f"conv_{fallback_idx}"


def get_conv_date(conv):
    return conv.get("created_at") or conv.get("date") or conv.get("updated_at") or ""


def get_msg_date(msg, fallback):
    return msg.get("created_at") or msg.get("date") or fallback


# ============================================================
# TÉRMINOS DE BÚSQUEDA (de SESSION_LOG_CONSOLIDADO, Spec B)
# ============================================================

SECONDARY_TERMS = [
    r"sin saber programar",
    r"sin programaci[oó]n",
    r"cualquiera puede",
    r"no t[eé]cnico",
    r"barrera t[eé]cnica",
]

TERTIARY_TERMS = [
    r"principio central",
    r"argumento del paper",
    r"el paper dice",
    r"conclusi[oó]n del proyecto",
    r"lo que el paper",
    r"tesis del",
]

TERM_TIERS = [
    ("secondary", SECONDARY_TERMS),
    ("tertiary", TERTIARY_TERMS),
]


def find_matches(text):
    """Devuelve lista de (match_level, match_term) encontrados en el texto.

    Para el tier primario, 'no democratiza' y 'democratiz' se solapan textualmente
    (la primera contiene a la segunda) — se registra solo el más específico, una
    vez, para no duplicar la misma evidencia. 'democratize' (inglés) es independiente
    y se registra aparte si aparece.
    """
    found = []
    if not text:
        return found

    if re.search(r"\bno\s+democratiz\w*", text, re.IGNORECASE):
        found.append(("primary", "no democratiza (negación explícita)"))
    elif re.search(r"democratiz\w*", text, re.IGNORECASE):
        found.append(("primary", "democratiz (stem)"))
    if re.search(r"\bdemocratize\w*\b", text, re.IGNORECASE):
        found.append(("primary", "democratize (inglés)"))

    for level, terms in TERM_TIERS:
        for term_pattern in terms:
            if re.search(term_pattern, text, re.IGNORECASE):
                found.append((level, term_pattern))
    return found


# ============================================================
# CONTEXTO
# ============================================================

def build_context(messages, idx, n=CONTEXT_N, trunc=CONTEXT_TRUNC):
    before, after = [], []
    for j in range(max(0, idx - n), idx):
        before.append({"sender": get_sender(messages[j]), "text": get_text(messages[j])[:trunc]})
    for j in range(idx + 1, min(len(messages), idx + 1 + n)):
        after.append({"sender": get_sender(messages[j]), "text": get_text(messages[j])[:trunc]})
    return before, after


# ============================================================
# MAIN
# ============================================================

def default_inputs():
    return [f"claude_{i}_processed.json" for i in range(1, 6)]


def account_from_filename(path):
    m = re.search(r"claude_(\d+)_processed", Path(path).name)
    return m.group(1) if m else Path(path).stem


def process_file(path, occurrences):
    try:
        data = load_json(path)
    except FileNotFoundError:
        print(f"  [omitido] no existe: {path}")
        return 0
    except json.JSONDecodeError as e:
        print(f"  [ERROR] {path} no es JSON válido: {e}")
        return 0

    account = account_from_filename(path)
    conversations = get_conversations(data)
    n_msgs_total = 0

    for c_idx, conv in enumerate(conversations):
        messages = get_messages(conv)
        conv_name = get_conv_name(conv)
        conv_uuid = get_conv_uuid(conv, c_idx)
        conv_date = get_conv_date(conv)

        for m_idx, msg in enumerate(messages):
            n_msgs_total += 1
            text = get_text(msg)
            matches = find_matches(text)
            if not matches:
                continue
            before, after = build_context(messages, m_idx)
            msg_date = get_msg_date(msg, conv_date)
            for level, term in matches:
                occurrences.append({
                    "id": f"{account}_{conv_uuid}_{m_idx}_{term[:15]}",
                    "account": account,
                    "conversation_uuid": conv_uuid,
                    "conversation_name": conv_name,
                    "conversation_date": conv_date,
                    "message_date": msg_date,
                    "sender": get_sender(msg),
                    "match_level": level,
                    "match_term": term,
                    "text": text[:TEXT_TRUNC],
                    "context_before": before,
                    "context_after": after,
                })
    return n_msgs_total


def sort_key(occ):
    # ordena por fecha de mensaje si existe, sino por fecha de conversación
    return occ.get("message_date") or occ.get("conversation_date") or ""


def main():
    inputs = sys.argv[1:] if len(sys.argv) > 1 else default_inputs()
    occurrences = []
    total_msgs = 0

    print("Spec B — rastreo de democratización")
    print("-" * 60)
    for path in inputs:
        print(f"Procesando {path} ...")
        total_msgs += process_file(path, occurrences)

    occurrences.sort(key=sort_key)

    primary_occs = [o for o in occurrences if o["match_level"] == "primary"]
    first_primary = primary_occs[0] if primary_occs else None

    by_account = {}
    by_sender = {"human": 0, "assistant": 0, "unknown": 0}
    by_level = {"primary": 0, "secondary": 0, "tertiary": 0}
    for o in occurrences:
        by_account[o["account"]] = by_account.get(o["account"], 0) + 1
        by_sender[o["sender"]] = by_sender.get(o["sender"], 0) + 1
        by_level[o["match_level"]] += 1

    output = {
        "summary": {
            "total_messages_scanned": total_msgs,
            "total_occurrences": len(occurrences),
            "by_match_level": by_level,
            "by_account": by_account,
            "by_sender": by_sender,
            "first_primary_occurrence": first_primary,
        },
        "occurrences": occurrences,
    }

    out_path = "spec_b_democratizacion.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("-" * 60)
    print(f"Mensajes escaneados: {total_msgs}")
    print(f"Apariciones totales: {len(occurrences)} (primary={by_level['primary']}, "
          f"secondary={by_level['secondary']}, tertiary={by_level['tertiary']})")
    print(f"Escrito: {out_path}")


if __name__ == "__main__":
    main()
