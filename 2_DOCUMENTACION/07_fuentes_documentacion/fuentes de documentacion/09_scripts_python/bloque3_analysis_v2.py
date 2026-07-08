#!/usr/bin/env python3
"""
bloque3_analysis_v2.py — Distribución de trabajo por tipo y fase (v2)
Bloque 3 del análisis cuantitativo IRAM — continuación de sesión cortada

Reemplaza la clasificación por título/keywords de v1 (que daba "diseño 1.5%",
sospechosamente bajo) por tres señales objetivas basadas en herramientas y
texto de mensajes:

  A. Código / Investigación / Build — por fase, mod-dev vs meta-documentación
  B. Tipo de "Investigación" (error / doc-plan / code-mod / other) — por fase
  C. Densidad de lenguaje de decisión/diseño en mensajes humanos y de Claude
  D. Top conversaciones v5 que explican el shift en (A) y (B)

Input: claude_1_processed.json … claude_5_processed.json (×5)
"""

import json
import re
from collections import defaultdict, Counter

# ── FASES (de IRAM_analisis_cuantitativo_2026-06-12_v2, Bloque 1) ──────────
def get_phase(date_str):
    if date_str <= '2026-04-21':
        return 'v1-v2'
    elif date_str <= '2026-05-21':
        return 'v3'
    elif date_str <= '2026-06-03':
        return 'v4'
    else:
        return 'v5'

PHASES = ['v1-v2', 'v3', 'v4', 'v5']

# ── Separar mod-dev de meta-documentación (sesiones sobre el propio
#    sistema de documentación: historial, wikis, skill, análisis) ──────────
DOC_SESSIONS_KEYWORDS = [
    'historial', 'markdown', 'superbackup', 'plantilla',
    'análisis cuantitativo', 'gaps', 'skill', 'unificar', 'consolidar',
    'documentación', 'session log', 'marco teórico'
]

def is_meta_doc(conv_name):
    return any(kw in conv_name.lower() for kw in DOC_SESSIONS_KEYWORDS)

# ── Señales de herramientas ─────────────────────────────────────────────
DEBUG_BASH = ['grep ', 'cat ', 'find ', 'head ', 'tail ', 'unzip -l']
IMPL_BASH = ['mkdir', 'zip -r', 'cp ', 'mv ', 'printf', 'python3']

# ── Targets para clasificar "Investigación" (señal B) ──────────────────────
ERROR_TARGET = re.compile(r'error\.log|game\.log|pdx_script_error|\berror\b|\bbug\b|crash', re.I)
DOC_TARGET   = re.compile(r'wiki|session_log|sesion|\.md\b|plan|gaps|hitos|skill|historial|prompt_maestro|revision', re.I)
CODE_TARGET  = re.compile(r'\.txt|on_action|scripted|exodos|iram_|\.gui|\.yml|events/|common/|decisions/|localization', re.I)

# ── Lenguaje de decisión/diseño (señal C) ───────────────────────────────────
DECISION_KW = re.compile(
    r'\bdiseñ|\bpropuesta|\bpropongo|\bopci[oó]n|\balternativa|\bcriterio|\bdecisi[oó]n|'
    r'\benfoque|\bestrategia|\bestructura\b|plan de|planificar|planificando|'
    r'qu[ée] te parece|qu[ée] opin|antes de tocar|pensar (todo )?primero|'
    r'\bprioridad|cu[aá]l (es )?(la )?mejor', re.I)


def load_convs():
    files = [f'/mnt/user-data/uploads/claude_{i}_processed.json' for i in range(1, 6)]
    all_convs = []
    for fp in files:
        with open(fp) as f:
            d = json.load(f)
        for conv in d['conversations']:
            if conv['period'] == 'IRAM' and conv['msg_count'] > 0:
                all_convs.append(conv)
    return all_convs


def conv_tool_counts(conv):
    """Cuenta create/replace (Código), bash-debug (Investigación), bash-impl (Build)."""
    cr = bd = bi = 0
    for msg in conv['messages']:
        for t in msg.get('tools', []):
            if '📄 create_file' in t or '✏️ str_replace' in t:
                cr += 1
            elif '🔧 bash' in t:
                t_l = t.lower()
                if any(x in t_l for x in DEBUG_BASH):
                    bd += 1
                elif any(x in t_l for x in IMPL_BASH):
                    bi += 1
    return cr, bd, bi


# ── TABLA A: Código / Investigación / Build — mod-dev vs meta-doc ──────────
def tabla_a(all_convs):
    phase_mod = defaultdict(lambda: {'convs': 0, 'msgs': 0, 'cr': 0, 'bd': 0, 'bi': 0})
    phase_meta = defaultdict(lambda: {'convs': 0, 'msgs': 0, 'cr': 0, 'bd': 0, 'bi': 0})

    for conv in all_convs:
        target = phase_meta if is_meta_doc(conv['name']) else phase_mod
        phase = get_phase(conv['date'])
        cr, bd, bi = conv_tool_counts(conv)
        target[phase]['convs'] += 1
        target[phase]['msgs'] += conv['msg_count']
        target[phase]['cr'] += cr
        target[phase]['bd'] += bd
        target[phase]['bi'] += bi

    print("=" * 76)
    print("TABLA A — CÓDIGO / INVESTIGACIÓN / BUILD por fase (mod-dev, excl. meta-doc)")
    print("=" * 76)
    print(f"{'Fase':<7} {'Convs':>6} {'Msgs':>6} | {'Código':>11} {'Investig':>12} {'Build':>10} | {'Ratio Inv/Cód':>13}")
    print("-" * 76)
    prev_ratio = None
    for phase in PHASES:
        s = phase_mod[phase]
        c, m, cr, bd, bi = s['convs'], s['msgs'], s['cr'], s['bd'], s['bi']
        ratio = bd / cr if cr > 0 else 0
        delta = f"  ({'+' if prev_ratio and ratio>prev_ratio else ''}{(ratio-prev_ratio)/prev_ratio*100:+.0f}%)" if prev_ratio else ""
        print(f"{phase:<7} {c:>6} {m:>6} | {cr:>5}({cr/m*100:>4.1f}%) {bd:>6}({bd/m*100:>4.1f}%) {bi:>4}({bi/m*100:>4.1f}%) | {ratio:>9.1f}x{delta}")
        prev_ratio = ratio

    print()
    print("META-DOCUMENTACIÓN (excluida de Tabla A — analizada en Bloque 0/2)")
    print(f"{'Fase':<7} {'Convs':>6} {'Msgs':>6}")
    for phase in PHASES:
        s = phase_meta[phase]
        print(f"{phase:<7} {s['convs']:>6} {s['msgs']:>6}")
    print()
    return phase_mod


# ── TABLA B: Tipo de Investigación — error / doc-plan / code-mod / other ───
def tabla_b(all_convs):
    investig_by_target = defaultdict(Counter)
    phase_total = defaultdict(int)

    for conv in all_convs:
        if is_meta_doc(conv['name']):
            continue
        phase = get_phase(conv['date'])
        for msg in conv['messages']:
            for t in msg.get('tools', []):
                if '🔧 bash' in t:
                    t_l = t.lower()
                    if any(x in t_l for x in DEBUG_BASH):
                        phase_total[phase] += 1
                        if ERROR_TARGET.search(t):
                            investig_by_target[phase]['error'] += 1
                        elif DOC_TARGET.search(t):
                            investig_by_target[phase]['doc_plan'] += 1
                        elif CODE_TARGET.search(t):
                            investig_by_target[phase]['code_mod'] += 1
                        else:
                            investig_by_target[phase]['other'] += 1

    print("=" * 76)
    print("TABLA B — TIPO DE 'INVESTIGACIÓN' (bash grep/cat/find/...) por fase")
    print("=" * 76)
    print(f"{'Fase':<7} {'Total':>6} {'error':>11} {'doc_plan':>11} {'code_mod':>11} {'other':>10}")
    print("-" * 76)
    for phase in PHASES:
        tot = phase_total[phase]
        c = investig_by_target[phase]
        print(f"{phase:<7} {tot:>6} "
              f"{c['error']:>5}({c['error']/tot*100:>4.0f}%) "
              f"{c['doc_plan']:>5}({c['doc_plan']/tot*100:>4.0f}%) "
              f"{c['code_mod']:>5}({c['code_mod']/tot*100:>4.0f}%) "
              f"{c['other']:>5}({c['other']/tot*100:>4.0f}%)")
    print()
    print("Nota: 'error' se mantiene en 1-3% en TODAS las fases — descarta")
    print("'más bugs' como explicación del ratio Inv/Cód creciente (Tabla A).")
    print("En v1-v2/v3, gran parte de 'other' es exploración de mecánicas del")
    print("juego (grep por términos como heir_weight, treasury, succession) —")
    print("investigación de diseño/calibración con vocabulario distinto al de")
    print("doc_plan/code_mod, que están orientados a la estructura propia del")
    print("proyecto (predominante en v4/v5).")
    print()


# ── TABLA C: Densidad de lenguaje de decisión/diseño ───────────────────────
def tabla_c(all_convs):
    stats = defaultdict(lambda: {'h_msgs': 0, 'h_kw': 0, 'h_len': 0, 'a_msgs': 0, 'a_kw': 0})

    for conv in all_convs:
        if is_meta_doc(conv['name']):
            continue
        phase = get_phase(conv['date'])
        for msg in conv['messages']:
            text = msg.get('text', '') or ''
            if msg['sender'] == 'human':
                stats[phase]['h_msgs'] += 1
                stats[phase]['h_len'] += msg.get('text_len', 0) or 0
                if text and DECISION_KW.search(text):
                    stats[phase]['h_kw'] += 1
            elif msg['sender'] == 'assistant':
                stats[phase]['a_msgs'] += 1
                if text and DECISION_KW.search(text):
                    stats[phase]['a_kw'] += 1

    print("=" * 76)
    print("TABLA C — DENSIDAD DE LENGUAJE DE DECISIÓN/DISEÑO por fase (mod-dev)")
    print("=" * 76)
    print(f"{'Fase':<7} {'H-msgs':>7} {'H-kw%':>7} {'H-avg-chars':>12} | {'A-msgs':>7} {'A-kw%':>7}")
    print("-" * 76)
    for phase in PHASES:
        s = stats[phase]
        h_kw_pct = s['h_kw'] / s['h_msgs'] * 100 if s['h_msgs'] else 0
        h_avg = s['h_len'] / s['h_msgs'] if s['h_msgs'] else 0
        a_kw_pct = s['a_kw'] / s['a_msgs'] * 100 if s['a_msgs'] else 0
        print(f"{phase:<7} {s['h_msgs']:>7} {h_kw_pct:>6.1f}% {h_avg:>12.0f} | {s['a_msgs']:>7} {a_kw_pct:>6.1f}%")
    print()
    print("H-kw% / A-kw% = % de mensajes humano/assistant con lenguaje de")
    print("decisión-diseño (propuesta, opción, criterio, estructura, plan...).")
    print("H-avg-chars = longitud promedio de mensaje humano, en caracteres.")
    print()


# ── TABLA D: Top conversaciones v5 que explican el shift ───────────────────
def tabla_d(all_convs):
    v5_mod = []
    for conv in all_convs:
        if get_phase(conv['date']) == 'v5' and not is_meta_doc(conv['name']):
            cr, bd, bi = conv_tool_counts(conv)
            v5_mod.append((conv, cr, bd, bi))
    v5_mod.sort(key=lambda x: x[2], reverse=True)

    print("=" * 76)
    print("TABLA D — TOP CONVERSACIONES v5 (mod-dev) por bash-debug (Investig.)")
    print("=" * 76)
    print(f"{'Fecha':<12} {'Cód':>4} {'Inv':>4} {'Bld':>4} {'Msgs':>5}  Nombre")
    print("-" * 76)
    for conv, cr, bd, bi in v5_mod[:8]:
        print(f"{conv['date']:<12} {cr:>4} {bd:>4} {bi:>4} {conv['msg_count']:>5}  {conv['name'][:55]}")
    print()
    print(f"Top 5 acumulan {sum(x[2] for x in v5_mod[:5])}/{sum(x[2] for x in v5_mod)} de la 'Investigación' v5,")
    print(f"pero solo {sum(x[1] for x in v5_mod[:5])}/{sum(x[1] for x in v5_mod)} del 'Código' v5.")
    print()
    print("Lectura de los nombres: 'audit', 'Confirmación de cambios/estructura',")
    print("'Plan de ejecución unificado v5.0', 'Verificación de tareas' — son")
    print("sesiones de planificación, auditoría y verificación del remake")
    print("modular v5.0→v5.5, no debugging reactivo.")
    print()


if __name__ == '__main__':
    all_convs = load_convs()
    print(f"Total conversaciones IRAM (msg_count>0): {len(all_convs)}\n")
    tabla_a(all_convs)
    tabla_b(all_convs)
    tabla_c(all_convs)
    tabla_d(all_convs)
