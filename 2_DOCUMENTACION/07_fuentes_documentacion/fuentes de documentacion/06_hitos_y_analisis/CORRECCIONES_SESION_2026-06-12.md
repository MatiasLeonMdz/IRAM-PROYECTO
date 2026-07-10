# CORRECCIONES Y ADDENDUM — Sesión 2026-06-12
**Leer antes de usar IRAM_analisis_cuantitativo_2026-06-12.md**
**Incorporar al SESSION_LOG al inicio de la próxima sesión**

---

## ERRORES COMETIDOS EN ESTA SESIÓN — A CORREGIR

### Error 1 — Interpretación de sesiones vacías (0 msgs)
**Lo que se documentó:** "sesiones vacías = reinicios de página / fallos de carga de contexto"
**Lo que era en realidad:** testeos de restauración de tokens. Cuando se agotaban los tokens, el operador enviaba un "hola" o "sigue" para verificar si se habían restaurado. No son artefactos del sistema de documentación.

**Impacto en el análisis cuantitativo:**
- El 21% de sesiones vacías no dice nada sobre la calidad del sistema de contexto
- La tabla de Bloque 0 ("% vacías" por período) está mal interpretada — esa columna no mide overhead del proceso
- Las frases sobre "fallos de carga" en el documento deben eliminarse
- El párrafo "Las 89 sesiones vacías (21% del total) son overhead real" en la Síntesis es **incorrecto**

**Corrección:** las sesiones vacías son comportamiento externo al proceso IRAM (gestión de límite de tokens de la plataforma). No son un indicador del sistema. Eliminar del análisis o reclasificar como dato operacional sin implicación metodológica.

---

### Error 2 — Metodología del Bloque 2 (paralelismo de cuentas)
**Lo que se hizo:** comparar timestamps de INICIO de sesión entre cuentas para detectar solapamiento.
**El problema:** el timestamp de inicio no dice si los mensajes reales se solapaban. Una sesión de C1 puede empezar a las 20:09 y terminar a las 20:30; una de C2 puede empezar a las 21:04. Eso es secuencial, no paralelo.

**Conclusiones afectadas:**
- "85% de días con múltiples cuentas activas" → válido como dato de día, inválido como evidencia de paralelismo simultáneo
- "198 pares de sesiones sustantivas a menos de 30 minutos" → calculado sobre starts, no sobre mensajes reales
- "C2 y C3 iniciaron con 46 segundos de diferencia" → los starts pueden solaparse aunque los mensajes no

**Conclusión real del Bloque 2:** INCOMPLETO. El veredicto "cuentas genuinamente paralelas" no está demostrado con la metodología usada.

**Cómo rehacerlo en la próxima sesión:**
- Los processed JSONs tienen campo `ts` (timestamp) por mensaje individual
- Extraer todos los mensajes IRAM con su ts real, agrupar por franja horaria (ej. ventanas de 15 min)
- Si hay mensajes de distintas cuentas en la misma ventana → paralelismo real
- Si los mensajes de distintas cuentas no se solapan aunque las sesiones sí → secuencial con rotación

**Nota adicional del operador:** posible causa de sesiones consecutivas en distintas cuentas = error de Claude que requería procesamiento alto → el operador abría otra cuenta mientras esperaba. Esto sería paralelismo forzado por error, no paralelismo deliberado. A verificar con timestamps de mensajes.

---

## QUÉ SÍ ES VÁLIDO DEL ANÁLISIS — MANTENER

### Bloque 0 (evolución del contexto): válido con una corrección
- La tabla de períodos y promedios de msgs/sesión es correcta
- El Bloque 0 sigue siendo analíticamente útil como "interrupted time series"
- **Eliminar:** la columna "% vacías" como indicador del sistema (ver Error 1)
- **Mantener:** promedio msgs/sesión por período, % sesiones de arranque de contexto, el patrón de caída de msgs/sesión con el PROMPT_MAESTRO

### Bloque 1 (velocidad por fase): válido sin correcciones
- La tabla de sesiones/día y msgs/sesión por fase es correcta
- El patrón v1-v2 (37 msgs/ses) → v5 (9.6 msgs/ses) es un hallazgo real

### Candidato ángulo 10: válido e independiente de los errores
- El evento 2026-05-18/19 (5 cuentas en documentación simultánea) está en los datos
- El memories.json de C5 lo confirma de forma independiente
- No depende de la interpretación de sesiones vacías ni del Bloque 2

### memories.json de C5: disposiciones confirmadas
1. Ángulo 10 → candidato desde datos — discutir en Plantilla C
2. INSTRUCCIONES_HUMANO → revisar en Plantilla B si hay archivos disponibles
3. "SESSION_LOGs take priority over prompt" → parche de sesión puntual, no regla permanente — no incorporar

---

## ADDENDUM AL SESSION_LOG — SESIÓN 5 (2026-06-12)

**Reemplazar el bloque "Sesión 5" del SESSION_LOG con esto:**

```
### Sesión 5 — Plantilla D parcial (2026-06-12)
- ✅ memories.json de C5 revisado — 3 hallazgos, disposiciones documentadas en CORRECCIONES_SESION_2026-06-12.md
- ✅ Bloque 1 completado — velocidad por fase: patrón v1-v2→v5 confirmado con datos
- ✅ Bloque 0 completado parcialmente — evolución de msgs/sesión por período válida; columna "% vacías" inválida (ver corrección)
- ⚠️ Bloque 2 INCOMPLETO — metodología usada (timestamps de inicio de sesión) no es suficiente para concluir paralelismo. Requiere rehacer con timestamps de mensajes individuales (campo `ts` en processed JSONs)
- ⚠️ IRAM_analisis_cuantitativo_2026-06-12.md contiene los dos errores documentados arriba — no usar directamente hasta corregir
- ✅ Candidato ángulo 10 identificado desde datos: evento 2026-05-18/19 + confirmación memories.json
```

**Agregar a DECISIONES CLAVE:**

| Qué | Sesión | Por qué importa |
|-----|--------|-----------------|
| Sesiones vacías = testeos de restauración de tokens, no artefactos del sistema | 5 (12/06) | Eliminar del análisis cuantitativo como indicador del proceso |
| Bloque 2 requiere rehacer con timestamps de mensajes, no de sesiones | 5 (12/06) | La conclusión "85% paralelas" no está demostrada — pendiente verificación real |
| Ángulo 10 tiene candidato desde datos (2026-05-18/19) | 5 (12/06) | Independiente de los errores del Bloque 2 — válido para Plantilla C |

---

## PRÓXIMA SESIÓN — ORDEN DE TRABAJO

1. Incorporar este documento al SESSION_LOG (reemplazar Sesión 5, agregar decisiones)
2. Rehacer Bloque 2 con timestamps de mensajes individuales
3. Corregir IRAM_analisis_cuantitativo_2026-06-12.md (eliminar sesiones vacías como indicador; actualizar Bloque 2)
4. Si Bloque 2 queda resuelto → Plantilla B

**Archivos a cargar:**
- PROMPT_MAESTRO v1.6 (bloque pegado)
- IRAM_TECHNICAL_WIKI_ACTIVE_v3_10_2026-06-09.md
- IRAM_hitos_metodologicos_2026-06-12_v7.md
- SESSION_LOG_DOCUMENTACION_2026-06-12_CONSOLIDADO.md
- CORRECCIONES_SESION_2026-06-12.md (este archivo)
- claude_N_processed.json ×5 — para rehacer Bloque 2
- IRAM_analisis_cuantitativo_2026-06-12.md — para corregir

---

*Generado al cierre de sesión 2026-06-12*
*Prioridad: leer antes de usar el analisis_cuantitativo*
