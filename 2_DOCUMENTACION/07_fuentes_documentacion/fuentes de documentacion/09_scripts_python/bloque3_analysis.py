#!/usr/bin/env python3
"""
bloque3_analysis.py — Distribución de trabajo por tipo y fase
Bloque 3 del análisis cuantitativo IRAM

Clasifica conversaciones IRAM en:
  - DISEÑO: planificación, arquitectura, análisis, decisiones
  - IMPLEMENTACIÓN: escritura de código, construcción de features
  - DEBUGGING: detección y corrección de errores
  - DOCUMENTACIÓN: logs, wikis, backups, historial
  - MIXED: señales mixtas / no clasificable con certeza
"""

import json
import re
from collections import defaultdict, Counter

# ── FASES DEL PROYECTO (de análisis cuantitativo Bloque 1) ──────────────────
# Drago v1-v2: 2026-04-09 → 2026-04-21
# IRAM v3:     2026-04-22 → 2026-05-21
# IRAM v4:     2026-05-22 → 2026-06-03
# IRAM v5:     2026-06-04 → 2026-06-10

def get_phase(date_str):
    if date_str <= '2026-04-21':
        return 'v1-v2 (Drago)'
    elif date_str <= '2026-05-21':
        return 'v3 (IRAM)'
    elif date_str <= '2026-06-03':
        return 'v4 (IRAM)'
    else:
        return 'v5 (IRAM)'

# ── SEÑALES DE CLASIFICACIÓN ────────────────────────────────────────────────

# Palabras clave en títulos de conversación
TITLE_DESIGN = [
    r'diseño', r'arquitectura', r'propuesta', r'plan', r'estrategia',
    r'análisis', r'analiz', r'cómo hacer', r'model', r'sistema',
    r'mecánica', r'criterio', r'scope', r'estructura', r'lógica',
    r'brainstorm', r'rediseño', r'refactor', r'fuentes', r'cálculo',
    r'balanceo', r'balance', r'investigar', r'research', r'comparar'
]

TITLE_DEBUG = [
    r'bug', r'error', r'fix', r'falla', r'arregl', r'correg',
    r'problema', r'issue', r'no funciona', r'roto', r'crash',
    r'revisar', r'verificar', r'test', r'prueba', r'chequear'
]

TITLE_IMPL = [
    r'implementar', r'implementación', r'construir', r'crear',
    r'escribir', r'generar', r'hacer\b', r'coding', r'desarrollo',
    r'v\d+\.\d+', r'update', r'upgrade', r'feature', r'nueva versión',
    r'integrar', r'añadir', r'agregar', r'módulo'
]

TITLE_DOC = [
    r'session.?log', r'backup', r'wiki', r'documentar', r'documentación',
    r'historial', r'log\b', r'notas', r'superbackup', r'skill',
    r'prompt.?maestro', r'registro', r'archivo', r'markdown',
    r'exportar', r'consolidar', r'análisis cuantitativo', r'gaps'
]

# Herramientas como señales
TOOLS_IMPL = {'📄 create_file', '✏️ str_replace'}
TOOLS_DEBUG_COMMANDS = ['grep ', 'cat ', 'find ', 'head ', 'tail ', 'diff ', 'unzip -l', 'ls ']
TOOLS_IMPL_COMMANDS = ['mkdir', 'zip -r', 'zip -u', 'cp ', 'mv ', 'printf ', 'python3 -c']

# Palabras clave en texto de mensajes humanos
MSG_DEBUG_KW = [
    r'\berror\b', r'\bbug\b', r'no funciona', r'falla', r'fallo',
    r'arregla', r'corrige', r'no aparece', r'no se', r'problema\b',
    r'roto', r'sale mal', r'equivocado', r'incorrecto', r'mal\b'
]

MSG_DESIGN_KW = [
    r'\bdiseñ', r'\bpropone', r'\bpropuesta', r'\bcómo hacer',
    r'\bqué approach', r'\banaliza', r'\brevisar el diseño',
    r'\bopinión', r'\bcriterio', r'\bdecisión', r'\balternativa'
]

# ── CLASIFICADOR ─────────────────────────────────────────────────────────────

def score_text(text, patterns):
    """Cuenta cuántos patrones matchean en el texto."""
    text_lower = text.lower()
    return sum(1 for p in patterns if re.search(p, text_lower))

def classify_conversation(conv):
    """
    Clasifica una conversación. Retorna tipo y scores.
    
    Estrategia multicapa:
    1. Título tiene peso alto
    2. Herramientas usadas (create_file, str_replace → impl; bash con grep → debug)
    3. Keywords en mensajes humanos
    """
    title = conv.get('name', '').lower()
    messages = conv.get('messages', [])
    
    scores = {'design': 0, 'impl': 0, 'debug': 0, 'doc': 0}
    
    # Capa 1: Título (peso 3x)
    title_weight = 3
    scores['design'] += score_text(title, TITLE_DESIGN) * title_weight
    scores['debug'] += score_text(title, TITLE_DEBUG) * title_weight
    scores['impl'] += score_text(title, TITLE_IMPL) * title_weight
    scores['doc'] += score_text(title, TITLE_DOC) * title_weight
    
    # Capa 2: Herramientas
    tools_all = ' '.join(t for m in messages for t in m.get('tools', []))
    
    # create_file y str_replace son señal fuerte de implementación
    impl_tool_count = sum(1 for m in messages 
                          for t in m.get('tools', []) 
                          if any(it in t for it in TOOLS_IMPL))
    scores['impl'] += impl_tool_count * 2
    
    # bash commands: clasificar por contenido
    for msg in messages:
        for tool in msg.get('tools', []):
            if '🔧 bash' in tool:
                tool_content = tool.lower()
                if any(dc in tool_content for dc in TOOLS_DEBUG_COMMANDS):
                    scores['debug'] += 0.5
                if any(ic in tool_content for ic in TOOLS_IMPL_COMMANDS):
                    scores['impl'] += 0.5
    
    # Capa 3: Keywords en mensajes humanos
    human_texts = [m['text'] for m in messages if m.get('sender') == 'human' and m.get('text')]
    combined_human = ' '.join(human_texts[:5])  # primeros 5 msgs humanos son más representativos
    
    scores['debug'] += score_text(combined_human, MSG_DEBUG_KW)
    scores['design'] += score_text(combined_human, MSG_DESIGN_KW)
    
    # Capa 4: Si el texto tiene mucho código pdxscript (señal de implementación)
    all_text = ' '.join(m.get('text', '') for m in messages[:10])
    pdx_signals = sum(1 for pattern in [r'scripted_effect', r'on_action', r'every_owned_province',
                                        r'monthly_country_pulse', r'\.pdxscript', r'remove_variable',
                                        r'set_variable', r'trigger_event', r'iram_', r'exodos_']
                      if re.search(pattern, all_text, re.IGNORECASE))
    scores['impl'] += pdx_signals * 0.3
    
    # Determinar tipo
    max_score = max(scores.values())
    if max_score == 0:
        return 'mixed', scores
    
    top_types = [t for t, s in scores.items() if s >= max_score * 0.8]
    
    if len(top_types) > 1:
        return 'mixed', scores
    
    return top_types[0], scores


# ── ANÁLISIS PRINCIPAL ───────────────────────────────────────────────────────

def run_analysis():
    files = [f'/mnt/user-data/uploads/claude_{i}_processed.json' for i in range(1, 6)]
    
    all_convs = []
    for fp in files:
        with open(fp) as f:
            data = json.load(f)
        for conv in data['conversations']:
            if conv['period'] == 'IRAM' and conv['msg_count'] > 0:
                all_convs.append(conv)
    
    print(f"Total conversaciones IRAM: {len(all_convs)}")
    print()
    
    # Clasificar todas
    results = []
    for conv in all_convs:
        tipo, scores = classify_conversation(conv)
        phase = get_phase(conv['date'])
        results.append({
            'name': conv['name'],
            'date': conv['date'],
            'phase': phase,
            'account': conv['account'],
            'tipo': tipo,
            'scores': scores,
            'msg_count': conv['msg_count'],
            'tools_used': conv.get('tools_used', []),
        })
    
    # ── TABLA 1: Distribución global por tipo ──────────────────────────────
    print("=" * 60)
    print("DISTRIBUCIÓN GLOBAL POR TIPO DE TRABAJO")
    print("=" * 60)
    
    type_counter = Counter(r['tipo'] for r in results)
    type_msgs = defaultdict(int)
    for r in results:
        type_msgs[r['tipo']] += r['msg_count']
    
    total_convs = len(results)
    total_msgs = sum(r['msg_count'] for r in results)
    
    print(f"{'Tipo':<20} {'Convs':>7} {'%convs':>8} {'Msgs':>8} {'%msgs':>8}")
    print("-" * 55)
    for tipo in ['impl', 'debug', 'design', 'doc', 'mixed']:
        c = type_counter.get(tipo, 0)
        m = type_msgs.get(tipo, 0)
        label = {'impl': 'Implementación', 'debug': 'Debugging', 
                 'design': 'Diseño', 'doc': 'Documentación', 'mixed': 'Mixto'}.get(tipo, tipo)
        print(f"{label:<20} {c:>7} {c/total_convs*100:>7.1f}% {m:>8} {m/total_msgs*100:>7.1f}%")
    print(f"{'TOTAL':<20} {total_convs:>7} {'100.0%':>8} {total_msgs:>8} {'100.0%':>8}")
    
    # ── TABLA 2: Distribución por fase ─────────────────────────────────────
    print()
    print("=" * 60)
    print("DISTRIBUCIÓN POR FASE (% de conversaciones)")
    print("=" * 60)
    
    phases = ['v1-v2 (Drago)', 'v3 (IRAM)', 'v4 (IRAM)', 'v5 (IRAM)']
    tipos = ['impl', 'debug', 'design', 'doc', 'mixed']
    tipo_labels = {'impl': 'Impl', 'debug': 'Debug', 'design': 'Diseño', 'doc': 'Doc', 'mixed': 'Mixto'}
    
    phase_data = defaultdict(lambda: defaultdict(int))
    phase_totals = defaultdict(int)
    phase_msgs = defaultdict(int)
    
    for r in results:
        phase_data[r['phase']][r['tipo']] += 1
        phase_totals[r['phase']] += 1
        phase_msgs[r['phase']] += r['msg_count']
    
    header = f"{'Fase':<16}" + "".join(f"{tipo_labels[t]:>8}" for t in tipos) + f"{'Total':>7} {'Msgs':>7}"
    print(header)
    print("-" * 70)
    
    for phase in phases:
        total = phase_totals[phase]
        row = f"{phase:<16}"
        for t in tipos:
            count = phase_data[phase].get(t, 0)
            pct = count/total*100 if total > 0 else 0
            row += f"{pct:>7.0f}%"
        row += f"{total:>7} {phase_msgs[phase]:>7}"
        print(row)
    
    # ── TABLA 3: Ratio debug/impl por fase ─────────────────────────────────
    print()
    print("=" * 60)
    print("RATIO DEBUG/IMPL POR FASE (indicador de madurez del proceso)")
    print("=" * 60)
    print(f"{'Fase':<16} {'Debug':>7} {'Impl':>7} {'Ratio D/I':>11} {'Interpretación'}")
    print("-" * 65)
    
    for phase in phases:
        d = phase_data[phase].get('debug', 0)
        i = phase_data[phase].get('impl', 0)
        ratio = d/i if i > 0 else float('inf')
        total = phase_totals[phase]
        if ratio > 1.5:
            interp = "← más debugging que implementación"
        elif ratio > 0.7:
            interp = "← balance debug/impl"
        else:
            interp = "← más implementación que debugging"
        print(f"{phase:<16} {d:>7} {i:>7} {ratio:>10.2f}x {interp}")
    
    # ── TABLA 4: Top convs de cada tipo con scores altos ───────────────────
    print()
    print("=" * 60)
    print("EJEMPLOS REPRESENTATIVOS POR TIPO (scores más altos)")
    print("=" * 60)
    
    for tipo in ['design', 'debug', 'doc']:
        typed = [r for r in results if r['tipo'] == tipo]
        typed_sorted = sorted(typed, key=lambda x: max(x['scores'].values()), reverse=True)
        label = {'design': 'DISEÑO', 'debug': 'DEBUGGING', 'doc': 'DOCUMENTACIÓN'}.get(tipo)
        print(f"\n{label} — top 5:")
        for r in typed_sorted[:5]:
            print(f"  [{r['date']}] {r['name'][:60]}")
    
    # ── TABLA 5: Sesión estratégica y días de documentación ────────────────
    print()
    print("=" * 60)
    print("DÍAS DE PURO TRABAJO DOCUMENTAL (sin implementación)")
    print("=" * 60)
    
    doc_days = defaultdict(lambda: defaultdict(int))
    for r in results:
        doc_days[r['date']][r['tipo']] += 1
    
    pure_doc_days = []
    for date, type_counts in sorted(doc_days.items()):
        total_day = sum(type_counts.values())
        doc_frac = type_counts.get('doc', 0) / total_day if total_day > 0 else 0
        impl_frac = type_counts.get('impl', 0) / total_day if total_day > 0 else 0
        if doc_frac >= 0.5:
            pure_doc_days.append((date, doc_frac, impl_frac, total_day))
    
    print(f"{'Fecha':<12} {'%Doc':>7} {'%Impl':>7} {'Convs':>7}")
    for date, df, imf, total in sorted(pure_doc_days, key=lambda x: x[1], reverse=True)[:10]:
        phase = get_phase(date)
        print(f"{date:<12} {df*100:>6.0f}% {imf*100:>6.0f}% {total:>7}  [{phase}]")
    
    return results

results = run_analysis()
