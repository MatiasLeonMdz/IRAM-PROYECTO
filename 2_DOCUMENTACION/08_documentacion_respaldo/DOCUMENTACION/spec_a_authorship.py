#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spec_a_authorship.py — Extracción de candidatos a "decisión de diseño" (Spec A).

Ver SESSION_LOG_CONSOLIDADO_2026-06-18.md, sección "SPEC A — ANÁLISIS DE AUTORÍA" y
"NOTAS TÉCNICAS PARA LOS SCRIPTS" para la definición operacional completa, el esquema
de codificación (OP_ARCH / IA_PROP_AC / IA_PROP_RJ / COLAB / IA_DIAG_OP_DEC) y el
formato de JSON esperado.

Este script NO clasifica decisiones — eso es trabajo manual de Sesión 3. Solo identifica
y puntúa candidatos para que la anotación humana/IA-con-extended-thinking sea sobre una
lista corta en vez de sobre el historial completo.

USO:
    python3 spec_a_authorship.py claude_1_processed.json claude_2_processed.json ...
    (sin argumentos: busca claude_1_processed.json .. claude_5_processed.json en el cwd)

OUTPUT:
    spec_a_candidates.json — hasta 150 candidatos, score descendente.

Si el formato real de los JSON difiere del esperado, ajustar las funciones de la
sección NORMALIZACIÓN — son las primeras del archivo y no dependen del resto.
"""

import json
import re
import sys
from pathlib import Path

MAX_CANDIDATES = 150
MIN_SCORE = 2          # candidatos por debajo de esto no se reportan
CONTEXT_N = 2           # mensajes de contexto antes/después
CONTEXT_TRUNC = 500
TEXT_TRUNC = 2000

# ============================================================
# NORMALIZACIÓN — ajustar acá si el formato real difiere
# ============================================================

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_conversations(data):
    """Devuelve una lista de conversaciones sea cual sea la estructura raíz."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "conversations" in data and isinstance(data["conversations"], list):
            return data["conversations"]
        # algunos exports tienen un dict de cuentas -> lista de conversaciones
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
# INFERENCIA DE FASE
# ============================================================

def infer_phase(conv_name, conv_date):
    name = (conv_name or "").lower()
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", conv_date or "")
    year = month = day = None
    if m:
        year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))

    if "v5" in name:
        return "v5"
    if year == 2026 and month == 6:
        return "v5"
    if "v4" in name:
        return "v4"
    if year == 2026 and month == 5 and (day or 0) >= 16:
        return "v4"
    if "v3" in name:
        return "v3"
    return "v1-v2"


# ============================================================
# SEÑALES DE "DECISIÓN DE DISEÑO" (heurística por keywords)
# ============================================================
# Cada señal: (regex, peso, etiqueta para score_reasons)

SIGNALS_POSITIVE = [
    (r"\b(arquitectura|alcance|estructura|namespace|prefijo|convenci[oó]n(es)?|patr[oó]n(es)?)\b", 3, "architecture_keyword"),
    (r"\b(decid[ií]|decidimos|vamos a usar|opt[ée] por|elijo|elegimos|optamos por)\b", 3, "decision_verb"),
    (r"\b(rechaz[oóeé]|descart[oóeé]|prefiero no|no va a funcionar|no sirve as[ií])\b", 2, "rejection"),
    (r"\b(trade-?off|en vez de|en lugar de|ventaja|desventaja)\b", 2, "tradeoff"),
    (r"\b(regla|criterio|de ahora en m[aá]s|a partir de ahora|siempre que|como convenci[oó]n)\b", 2, "rule_definition"),
    (r"\b(porque|ya que|debido a|la raz[oó]n es|el motivo es)\b", 1, "justification"),
    (r"\b(en vez de mantener|reemplaza(mos)?|migra(mos)?|reestructura(mos)?)\b", 2, "structural_change"),
]

SIGNALS_NEGATIVE = [
    (r"^\s*(listo|gracias|ok|okay|dale|perfecto|genial)\s*[.!]?\s*$", -5, "pure_ack"),
    (r"^\s*(s[ií]|no)\s*[.!]?\s*$", -5, "single_word"),
]


def code_ratio(text):
    if not text:
        return 0.0
    code_chars = len(re.findall(r"```.*?```", text, flags=re.S))
    fence_len = sum(len(m) for m in re.findall(r"```.*?```", text, flags=re.S))
    if len(text) == 0:
        return 0.0
    return fence_len / max(len(text), 1)


def score_message(text):
    if not text or len(text.strip()) < 20:
        return 0, []
    reasons = []
    score = 0
    for pattern, weight, label in SIGNALS_POSITIVE:
        if re.search(pattern, text, re.IGNORECASE):
            score += weight
            reasons.append(label)
    for pattern, weight, label in SIGNALS_NEGATIVE:
        if re.search(pattern, text, re.IGNORECASE):
            score += weight
            reasons.append(label)

    cr = code_ratio(text)
    if cr > 0.6:
        score -= 3
        reasons.append("mostly_code")

    if len(text) > 400 and cr < 0.3:
        score += 1
        reasons.append("substantial_length")

    if "decision_verb" in reasons and "justification" in reasons:
        score += 1
        reasons.append("decision_with_justification")

    return score, reasons


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


def process_file(path, candidates):
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
        phase = infer_phase(conv_name, conv_date)

        for m_idx, msg in enumerate(messages):
            n_msgs_total += 1
            text = get_text(msg)
            score, reasons = score_message(text)
            if score < MIN_SCORE:
                continue
            before, after = build_context(messages, m_idx)
            candidates.append({
                "id": f"{account}_{conv_uuid}_{m_idx}",
                "account": account,
                "conversation_uuid": conv_uuid,
                "conversation_name": conv_name,
                "conversation_date": conv_date,
                "phase": phase,
                "message_index": m_idx,
                "sender": get_sender(msg),
                "text": text[:TEXT_TRUNC],
                "context_before": before,
                "context_after": after,
                "score": score,
                "score_reasons": reasons,
            })
    return n_msgs_total


def main():
    inputs = sys.argv[1:] if len(sys.argv) > 1 else default_inputs()
    candidates = []
    total_msgs = 0

    print("Spec A — extracción de candidatos a decisión de diseño")
    print("-" * 60)
    for path in inputs:
        print(f"Procesando {path} ...")
        total_msgs += process_file(path, candidates)

    candidates.sort(key=lambda c: c["score"], reverse=True)
    top = candidates[:MAX_CANDIDATES]

    by_phase = {}
    for c in top:
        by_phase[c["phase"]] = by_phase.get(c["phase"], 0) + 1

    output = {
        "summary": {
            "total_messages_scanned": total_msgs,
            "total_candidates_above_threshold": len(candidates),
            "candidates_in_output": len(top),
            "min_score_threshold": MIN_SCORE,
            "distribution_by_phase": by_phase,
        },
        "candidates": top,
    }

    out_path = "spec_a_candidates.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("-" * 60)
    print(f"Mensajes escaneados: {total_msgs}")
    print(f"Candidatos sobre umbral (score >= {MIN_SCORE}): {len(candidates)}")
    print(f"Candidatos en output (top {MAX_CANDIDATES}): {len(top)}")
    print(f"Distribución por fase en el output: {by_phase}")
    print(f"Escrito: {out_path}")


if __name__ == "__main__":
    main()
