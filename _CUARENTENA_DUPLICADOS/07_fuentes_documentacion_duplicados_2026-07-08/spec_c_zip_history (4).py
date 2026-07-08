#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spec_c_zip_history.py — Historia de versiones de zips + gaps técnicos no documentados
(Spec C).

Ver SESSION_LOG_CONSOLIDADO_2026-06-18.md, sección "SPEC C — GAPS TÉCNICOS DEL MOD /
HISTORIA DE ZIPS" para la pregunta que resuelve (TAREA 17B: completar Sec 21 del ACTIVE,
que termina en v4.0).

Este script NO redescubre los 35 hallazgos ya cubiertos por SESSION_LOG v5.6. Busca
únicamente menciones de versiones de zip (para reconstruir qué cambió entre v4.0 y v5.5)
y, como tarea secundaria opcional, decisiones técnicas que puedan haber quedado solo en
conversaciones.

USO:
    python3 spec_c_zip_history.py claude_1_processed.json ... claude_5_processed.json
    (sin argumentos: busca claude_1_processed.json .. claude_5_processed.json en el cwd)

OUTPUT:
    spec_c_zip_history.json
"""

import json
import re
import sys
from pathlib import Path

CONTEXT_N = 3
CONTEXT_TRUNC = 400
TEXT_TRUNC = 1500
MAX_SECONDARY = 50

EXPECTED_VERSIONS = [
    "v4.1", "v4.2", "v4.3", "v4.3.16",
    "v5.0", "v5.1", "v5.2", "v5.3", "v5.4", "v5.5",
]

ZIP_CONTEXT_WORDS = re.compile(
    r"\b(zip|mod_pack|entregable|listo|gener[oóeé]|generando|comprim\w*|package|paquete)\b",
    re.IGNORECASE,
)

# Patrones de versión: cubren notación con punto en prosa (v5.5) y la notación con
# guion bajo de los nombres de archivo reales (mod_pack_IRAM_v5_5_2026-06-09_03-22.zip).
# El patrón de guion bajo va anclado al prefijo IRAM_v / mod_pack_IRAM_v: sin el ancla,
# un \d+ greedy se come también la fecha que sigue (v4_3_16_2026-05-20 → "v4.3.16.2026").
DOT_PATTERNS = [
    re.compile(r"\bv4\.\d+(?:\.\d+)?\b", re.IGNORECASE),
    re.compile(r"\bv5\.\d+(?:\.\d+)?\b", re.IGNORECASE),
]
FILENAME_PATTERNS = [
    re.compile(r"(?:mod_pack_)?IRAM_v(\d+_\d+(?:_\d+)?)", re.IGNORECASE),
]

# ============================================================
# NORMALIZACIÓN — idéntico a los otros dos scripts, ajustar acá si difiere
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


def build_context(messages, idx, n=CONTEXT_N, trunc=CONTEXT_TRUNC):
    before, after = [], []
    for j in range(max(0, idx - n), idx):
        before.append({"sender": get_sender(messages[j]), "text": get_text(messages[j])[:trunc]})
    for j in range(idx + 1, min(len(messages), idx + 1 + n)):
        after.append({"sender": get_sender(messages[j]), "text": get_text(messages[j])[:trunc]})
    return before, after


def find_versions(text):
    found = set()
    if not text:
        return found
    for pattern in DOT_PATTERNS:
        for m in pattern.findall(text):
            found.add(m.lower())
    for pattern in FILENAME_PATTERNS:
        for m in pattern.findall(text):
            found.add("v" + m.replace("_", "."))
    return found


# ============================================================
# DECISIONES TÉCNICAS SIN DOCUMENTAR (heurística secundaria, opcional)
# ============================================================

TECH_SIGNALS = [
    (r"\b(bug|gltch|error)\b", 1, "bug_mention"),
    (r"\b(guard|namespace|trigger_event|scope|alcance)\b", 2, "technical_term"),
    (r"\b(decisi[oó]n t[eé]cnica|decid[ií] t[eé]cnicamente)\b", 3, "explicit_technical_decision"),
    (r"\b(corregido|corregimos|soluci[oó]n|causa ra[íi]z|diagn[oó]stico)\b", 1, "fix_or_diagnosis"),
    (r"\b(implementé|implementamos|agregu[eé]|agregamos)\b", 1, "implementation"),
]


def tech_score(text):
    if not text or len(text.strip()) < 30:
        return 0, []
    score, reasons = 0, []
    for pattern, weight, label in TECH_SIGNALS:
        if re.search(pattern, text, re.IGNORECASE):
            score += weight
            reasons.append(label)
    return score, reasons


# ============================================================
# MAIN
# ============================================================

def default_inputs():
    return [f"claude_{i}_processed.json" for i in range(1, 6)]


def account_from_filename(path):
    m = re.search(r"claude_(\d+)_processed", Path(path).name)
    return m.group(1) if m else Path(path).stem


def process_file(path, zip_mentions, secondary_candidates):
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
            if not text:
                continue

            versions = find_versions(text)
            if versions:
                before, after = build_context(messages, m_idx)
                has_zip_context = bool(ZIP_CONTEXT_WORDS.search(text))
                msg_date = get_msg_date(msg, conv_date)
                for v in versions:
                    zip_mentions.append({
                        "id": f"{account}_{conv_uuid}_{m_idx}_{v}",
                        "version": v,
                        "account": account,
                        "conversation_uuid": conv_uuid,
                        "conversation_name": conv_name,
                        "conversation_date": conv_date,
                        "message_date": msg_date,
                        "sender": get_sender(msg),
                        "has_zip_context": has_zip_context,
                        "text": text[:TEXT_TRUNC],
                        "context_before": before,
                        "context_after": after,
                    })

            score, reasons = tech_score(text)
            if score >= 3:
                secondary_candidates.append({
                    "id": f"{account}_{conv_uuid}_{m_idx}_tech",
                    "account": account,
                    "conversation_uuid": conv_uuid,
                    "conversation_name": conv_name,
                    "conversation_date": conv_date,
                    "sender": get_sender(msg),
                    "text": text[:TEXT_TRUNC],
                    "score": score,
                    "score_reasons": reasons,
                })
    return n_msgs_total


def sort_key(mention):
    return mention.get("message_date") or mention.get("conversation_date") or ""


def main():
    inputs = sys.argv[1:] if len(sys.argv) > 1 else default_inputs()
    zip_mentions = []
    secondary_candidates = []
    total_msgs = 0

    print("Spec C — historia de zips + gaps técnicos")
    print("-" * 60)
    for path in inputs:
        print(f"Procesando {path} ...")
        total_msgs += process_file(path, zip_mentions, secondary_candidates)

    zip_mentions.sort(key=sort_key)
    secondary_candidates.sort(key=lambda c: c["score"], reverse=True)
    secondary_top = secondary_candidates[:MAX_SECONDARY]

    versions_found = sorted({m["version"] for m in zip_mentions})
    versions_missing = [v for v in EXPECTED_VERSIONS if v not in versions_found]

    mentions_by_version = {}
    for m in zip_mentions:
        mentions_by_version.setdefault(m["version"], 0)
        mentions_by_version[m["version"]] += 1

    output = {
        "summary": {
            "total_messages_scanned": total_msgs,
            "total_zip_mentions": len(zip_mentions),
            "distinct_versions_found": versions_found,
            "expected_versions": EXPECTED_VERSIONS,
            "expected_versions_not_found": versions_missing,
            "mentions_per_version": mentions_by_version,
            "secondary_candidates_total": len(secondary_candidates),
            "secondary_candidates_in_output": len(secondary_top),
        },
        "zip_mentions": zip_mentions,
        "secondary_undocumented_decisions": secondary_top,
    }

    out_path = "spec_c_zip_history.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("-" * 60)
    print(f"Mensajes escaneados: {total_msgs}")
    print(f"Menciones de zip encontradas: {len(zip_mentions)}")
    print(f"Versiones encontradas: {versions_found}")
    print(f"Versiones esperadas NO encontradas: {versions_missing}")
    print(f"Candidatos secundarios (gaps técnicos) en output: {len(secondary_top)}")
    print(f"Escrito: {out_path}")


if __name__ == "__main__":
    main()
