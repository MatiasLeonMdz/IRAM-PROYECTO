# PLAN DE TRABAJO — IRAM / Documentación / Diplomatura UTN

**Versión:** 1.0  
**Fecha:** 2026-07-05  
**Base:** Logs de replanteo hasta DR-54, reorganización física completada (DR-51), inventario completado (DR-45–49)  
**Próximo hito crítico:** Entrega Parte 1 UTN → **2026-07-15**

---

## Índice

1. [Estado actual resumido](#1-estado-actual-resumido)
2. [Objetivos finales del proyecto](#2-objetivos-finales-del-proyecto)
3. [Dependencias críticas](#3-dependencias-críticas)
4. [Fases de trabajo detalladas](#4-fases-de-trabajo-detalladas)
   - [Fase 0 — Resolución de DR-54](#fase-0--resolución-de-dr-54)
   - [Fase 1 — Procesamiento de datos](#fase-1--procesamiento-de-datos)
   - [Fase 2 — Entrega Parte 1 UTN](#fase-2--entrega-parte-1-utn)
   - [Fase 3 — Entrega Parte 2 UTN](#fase-3--entrega-parte-2-utn)
   - [Fase 4 — Corrección del Paper C1 y Skill C2](#fase-4--corrección-del-paper-c1-y-skill-c2)
   - [Fase 5 — Tareas de limpieza y cierre](#fase-5--tareas-de-limpieza-y-cierre)
5. [Cronograma tentativo](#5-cronograma-tentativo)
6. [Entregables esperados](#6-entregables-esperados)
7. [Notas operativas para la IA de bajo nivel](#7-notas-operativas-para-la-ia-de-bajo-nivel)
8. [Próximo paso inmediato](#8-próximo-paso-inmediato)
9. [Anexo — Estructura de carpetas actual](#9-anexo--estructura-de-carpetas-actual)

---

## 1. Estado actual resumido

| Área | Estado |
|------|--------|
| **Estructura física** | ✅ Aplicada (DR-51): `1_MOD/`, `2_DOCUMENTACION/`, `3_PORTAFOLIO_UTN/`, `_CUARENTENA_DUPLICADOS/` |
| **Inventario de archivos** | ✅ Completado (DR-45–49): 1991 archivos, corpus A/B identificados |
| **Corpus A crudo** | ✅ En `1_MOD/corpus_A_crudo/` (5 `data-*-batch-0000.zip` – enero 2026) |
| **Corpus B crudo** | ✅ En `2_DOCUMENTACION/05_corpus_B_crudo/` (5 `documentacion claude 1-5.zip` – 10-20/06) |
| **Corpus B procesado parcial** | ⚠️ Existen `claude_1_processed.json` … `claude_5_processed.json` en `07_fuentes_documentacion/` – sin abrir (DR-47) |
| **Paper C1** | ⚠️ Cerrado en s34, pero con S4A y S5 sin respaldo cuantitativo – pendiente de corrección |
| **Skill C2** | ❌ No existe – pendiente de generación |
| **DR-54 (diseño de tabla)** | ❌ **BLOQUEANTE** – sin resolver |
| **Diplomatura UTN – Parte 1** | ⚠️ Vence 2026-07-15 – requiere tabla de análisis para responder |

---

## 2. Objetivos finales del proyecto

| # | Objetivo | Productos | Estado |
|---|----------|-----------|--------|
| 1 | Mod IRAM | Código jugable v5.6 (bugs menores) | ✅ Cerrado – no tocar en esta fase |
| 2 | Documentación del proceso | (a) Paper C1 corregido, (b) Skill C2 operacional | 🔧 Pendiente |
| 3 | Análisis A/B + Diplomatura UTN | (a) Base de hechos verificada, (b) Entregas Parte 1 y 2, (c) Portafolio GitHub | ⏳ En diseño – DR-54 bloquea |

---

## 3. Dependencias críticas
