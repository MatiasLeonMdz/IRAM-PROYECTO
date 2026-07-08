#!/usr/bin/env python3
"""
process_iram_v2.py — Procesador de historiales IRAM
Uso: python3 process_iram_v2.py <conversations.json> <account_label>
     Ej: python3 process_iram_v2.py /home/claude/work/claude_1/conversations.json claude_1
Output: <account_label>_processed.json en el directorio actual
"""

import json
import sys
import os
import re
from datetime import datetime, timedelta

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────

IRAM_START_DATE = "2026-04-09"  # R6: desarrollo real comienza aquí

# Keywords de hitos metodológicos (R9)
HITOS = {
    "primeros_scripts": [
        r"iram_exodos", r"iram_bom", r"iram_tgl", r"\.pdxscript", r"scripted_effect",
        r"on_action", r"\.mod\b", r"iram_work/"
    ],
    "primer_session_log": [
        r"SESSION[_\s]LOG", r"session log", r"SESSION LOG"
    ],
    "primera_wiki": [
        r"TECHNICAL[_\s]WIKI", r"wiki.activ", r"wiki\s+activ", r"ACTIVE.*wiki|wiki.*ACTIVE",
        r"WIKI_ACTIVE", r"wiki técnico", r"WIKI ACTIVE"
    ],
    "separacion_active_archive": [
        r"ARCHIVE", r"WIKI.*ARCHIVE|ARCHIVE.*WIKI", r"separar.*wiki|wiki.*separar",
        r"ACTIVE.*ARCHIVE|ARCHIVE.*ACTIVE"
    ],
    "primer_prompt_maestro": [
        r"PROMPT[_\s]MAESTRO", r"prompt maestro", r"PASO\s*1", r"PASO 1"
    ],
    "primeros_wip": [
        r"\bWIP\b", r"work.in.progress", r"remake.*v5|v5.*remake",
        r"zip.*wip|wip.*zip"
    ],
    "primera_auditoria": [
        r"\bauditoría\b", r"\bauditoria\b", r"\baudit\b", r"35\s+hallazgos",
        r"hallazgos?\s+únicos"
    ],
    "sistema_versiones": [
        r"\bv\d+\.\d+\b", r"versión\s+v?\d", r"vX\.X\.X", r"sistema.*versión"
    ],
    "minilogs": [
        r"\bMINILOG\b", r"minilog", r"MINILOG"
    ],
    "zips_wip": [
        r"zip.*wip|wip.*zip", r"zip.*canónico|canónico.*zip",
        r"mod_pack.*zip|zip.*mod_pack"
    ],
}

# Patrones de logs de juego → TRUNCAR (R3)
GAME_LOG_PATTERNS = [
    r"pdx_script_error", r"game\.log", r"\[ERROR\].*pdx", r"script_error\.log",
    r"error\.log.*pdx", r"<error>", r"SCRIPT ERROR"
]

# Patrones para detectar bloques temáticos
BLOCK_MARKERS = [
    r"^#{1,3}\s+", r"^---+$", r"^===+$", r"SIGUIENTE\s+TAREA",
    r"PASO\s+\d", r"FASE\s+\d", r"TAREA\s+\d"
]

TOOL_NAMES = {
    "bash_tool": "🔧 bash",
    "create_file": "📄 create_file",
    "str_replace": "✏️ str_replace",
    "view": "👁 view",
    "web_search": "🔍 web_search",
    "web_fetch": "🌐 web_fetch",
    "present_files": "📦 present_files",
}

# ── HELPERS ──────────────────────────────────────────────────────────────────

def extract_text(msg):
    """Extrae texto limpio de un mensaje (maneja content array y text field)."""
    content = msg.get("content", [])
    
    # Para assistant: usar content[type=text] (evita "not supported" del text field)
    if msg.get("sender") == "assistant":
        parts = []
        for item in content:
            if item.get("type") == "text":
                t = str(item.get("text", "")).strip()
                if t:
                    parts.append(t)
        if parts:
            return "\n\n".join(parts)
    
    # Para human o fallback: usar text field
    text = msg.get("text", "").strip()
    if text:
        return text
    
    # Fallback: concatenar content[type=text]
    parts = []
    for item in content:
        if item.get("type") == "text":
            t = str(item.get("text", "")).strip()
            if t:
                parts.append(t)
    return "\n\n".join(parts)


def extract_tools_used(msg):
    """Lista de herramientas usadas en un mensaje de assistant."""
    tools = []
    for item in msg.get("content", []):
        if item.get("type") == "tool_use":
            name = item.get("name", "unknown")
            label = TOOL_NAMES.get(name, f"🔨 {name}")
            inp = item.get("input", {})
            # Extraer info clave del input
            if name == "bash_tool":
                cmd = str(inp.get("command", ""))[:60]
                tools.append(f"{label}: `{cmd}`")
            elif name == "create_file":
                path = inp.get("path", "?")
                tools.append(f"{label}: `{path}`")
            elif name == "str_replace":
                path = inp.get("path", "?")
                tools.append(f"{label}: `{path}`")
            elif name == "view":
                path = inp.get("path", "?")
                tools.append(f"{label}: `{path}`")
            elif name == "web_search":
                q = str(inp.get("query", ""))[:60]
                tools.append(f"{label}: `{q}`")
            else:
                tools.append(label)
    return tools


def is_game_log(text):
    """Detecta si el contenido es un log de error del juego (R3: truncar estos)."""
    for pattern in GAME_LOG_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False


def truncate_game_log(text):
    """Trunca logs de juego a una línea de resumen."""
    lines = text.split("\n")
    error_lines = [l for l in lines if any(
        re.search(p, l, re.IGNORECASE) for p in GAME_LOG_PATTERNS
    )]
    return f"[LOG DE JUEGO TRUNCADO — {len(lines)} líneas, {len(error_lines)} errores]"


def detect_hitos(text, conv_name=""):
    """Detecta qué hitos metodológicos aparecen en un texto."""
    found = []
    combined = (text + " " + conv_name).lower()
    for hito, patterns in HITOS.items():
        for p in patterns:
            if re.search(p, combined, re.IGNORECASE):
                found.append(hito)
                break
    return found


def detect_block_start(text):
    """Detecta si un mensaje marca el inicio de un bloque temático."""
    for pattern in BLOCK_MARKERS:
        if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
            return True
    return False


def is_iram_period(date_str):
    """R6: ¿La fecha es período IRAM o pre-IRAM?"""
    return date_str[:10] >= IRAM_START_DATE


def dedup_messages(messages):
    """Elimina mensajes duplicados consecutivos (mismo sender + mismo inicio)."""
    deduped = []
    seen = {}
    for msg in messages:
        sender = msg.get("sender", "")
        text = extract_text(msg)
        key = (sender, text[:100])
        if key not in seen:
            seen[key] = True
            deduped.append(msg)
        # Si es dup, lo marcamos pero no lo incluimos
    return deduped


def parse_timestamp(ts_str):
    """Parsea timestamp ISO a datetime."""
    try:
        return datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    except:
        return None


# ── PROCESAMIENTO PRINCIPAL ──────────────────────────────────────────────────

def process_conversation(conv, account_label):
    """Procesa una conversación y devuelve estructura enriquecida."""
    uuid = conv.get("uuid", "")
    name = conv.get("name", "").strip() or f"[sin título — {uuid[:8]}]"
    created_at = conv.get("created_at", "")
    updated_at = conv.get("updated_at", "")
    raw_messages = conv.get("chat_messages", [])
    
    date_str = created_at[:10]
    period = "IRAM" if is_iram_period(date_str) else "pre-IRAM"
    
    # Deduplicar
    messages = dedup_messages(raw_messages)
    dup_count = len(raw_messages) - len(messages)
    
    # Calcular duración
    ts_list = [parse_timestamp(m.get("created_at", "")) for m in messages]
    ts_list = [t for t in ts_list if t is not None]
    duration_min = 0
    if len(ts_list) >= 2:
        duration_min = int((max(ts_list) - min(ts_list)).total_seconds() / 60)
    
    # Procesar mensajes
    processed_msgs = []
    all_hitos = set()
    tools_used = set()
    
    prev_ts = None
    block_num = 1
    
    for i, msg in enumerate(messages):
        sender = msg.get("sender", "human")
        ts_raw = msg.get("created_at", "")
        ts = parse_timestamp(ts_raw)
        
        text = extract_text(msg)
        tools = extract_tools_used(msg) if sender == "assistant" else []
        
        # Calcular pausa desde mensaje anterior
        pause_min = 0
        if prev_ts and ts:
            pause_min = int((ts - prev_ts).total_seconds() / 60)
        
        # Nuevo bloque temático: pausa > 30 min o marcador explícito
        new_block = False
        if pause_min > 30 or (text and detect_block_start(text)):
            if i > 0:
                block_num += 1
                new_block = True
        
        # Truncar logs de juego (R3)
        is_log = is_game_log(text)
        if is_log:
            text_stored = truncate_game_log(text)
        else:
            text_stored = text
        
        # Detectar hitos
        msg_hitos = detect_hitos(text_stored, name)
        all_hitos.update(msg_hitos)
        
        for t in tools:
            tools_used.add(t.split(":")[0].strip())
        
        processed_msgs.append({
            "idx": i,
            "sender": sender,
            "ts": ts_raw,
            "ts_short": ts_raw[11:16] if ts_raw else "??:??",
            "block": block_num,
            "new_block": new_block,
            "pause_min": pause_min,
            "text": text_stored,
            "text_len": len(text),
            "is_log": is_log,
            "tools": tools,
            "hitos": msg_hitos,
        })
        
        prev_ts = ts
    
    return {
        "account": account_label,
        "uuid": uuid,
        "name": name,
        "date": date_str,
        "created_at": created_at,
        "updated_at": updated_at,
        "period": period,
        "msg_count_raw": len(raw_messages),
        "msg_count": len(messages),
        "dup_count": dup_count,
        "duration_min": duration_min,
        "block_count": block_num,
        "hitos": sorted(all_hitos),
        "tools_used": sorted(tools_used),
        "messages": processed_msgs,
    }


def process_file(json_path, account_label, output_path):
    """Procesa un conversations.json completo."""
    print(f"[{account_label}] Cargando {json_path}...")
    with open(json_path) as f:
        data = json.load(f)
    
    print(f"[{account_label}] {len(data)} conversaciones encontradas")
    
    conversations = []
    hito_first_seen = {}  # hito → primera ocurrencia
    
    for i, conv in enumerate(data):
        result = process_conversation(conv, account_label)
        conversations.append(result)
        
        # Rastrear primera aparición de cada hito (R9)
        for hito in result["hitos"]:
            if hito not in hito_first_seen:
                hito_first_seen[hito] = {
                    "date": result["date"],
                    "account": account_label,
                    "conv_name": result["name"],
                    "conv_uuid": result["uuid"]
                }
        
        # Progreso
        if (i + 1) % 20 == 0:
            print(f"[{account_label}]   {i+1}/{len(data)} conversaciones procesadas...")
    
    output = {
        "account": account_label,
        "source": json_path,
        "total_conversations": len(conversations),
        "total_messages": sum(c["msg_count"] for c in conversations),
        "total_dups_removed": sum(c["dup_count"] for c in conversations),
        "date_range": {
            "start": min(c["date"] for c in conversations),
            "end": max(c["date"] for c in conversations),
        },
        "hito_first_seen": hito_first_seen,
        "conversations": conversations,
    }
    
    print(f"[{account_label}] Guardando {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    size_mb = os.path.getsize(output_path) / 1024 / 1024
    print(f"[{account_label}] ✅ {len(conversations)} convs | {output['total_messages']} msgs | {size_mb:.1f} MB")
    return output


# ── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 process_iram_v2.py <conversations.json> <account_label>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    account_label = sys.argv[2]
    output_path = f"{account_label}_processed.json"
    
    process_file(json_path, account_label, output_path)
