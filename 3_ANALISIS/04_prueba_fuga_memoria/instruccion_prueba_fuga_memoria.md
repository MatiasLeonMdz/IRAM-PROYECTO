# Instrucción para pegar en cada cuenta (claude_1 a claude_5)

Copiar y pegar tal cual, adjuntando el ZIP completo del proyecto IRAM
(o al menos la carpeta "fuentes de documentacion" + el SESSION_LOG_REPLANTEO
más reciente) en el mismo mensaje.

---

Necesito que hagas una prueba de "fuga de memoria" sobre el proyecto IRAM.
El objetivo: comprobar si tu memoria de conversaciones pasadas conmigo sobre
este proyecto contiene algo que NO esté ya documentado en los archivos reales
(logs, wiki, paper) que te adjunto.

Hacé esto en dos pasos, sin saltarte ninguno:

**Paso 1 — Volcá tu memoria primero, antes de mirar los archivos adjuntos.**
Escribí en un .md todo lo que recordás sobre el proyecto IRAM: decisiones,
hallazgos, nombres de archivos, fechas, cualquier detalle operativo de
sesiones pasadas. No inventes ni completes huecos - si no estás seguro de
un dato, marcalo explícitamente como "no confirmado" o "reconstrucción
aproximada", no lo presentes como hecho. Esto es importante para que la
comparación del paso 2 sea válida — si mezclás memoria con lectura de
archivos antes de terminar este paso, contaminás la prueba.

**Paso 2 — Recién ahora, cruzá ese volcado contra los archivos adjuntos.**
Para cada afirmación de tu memoria, buscá si existe evidencia en los
archivos reales (grep, lectura directa, lo que haga falta). Clasificá cada
punto en una de tres categorías:
- ✅ CONFIRMADO: existe en los archivos, tal como lo recordabas.
- ⚠️ DESACTUALIZADO: existe pero cambió después (ej. vos recordás algo
  como "pendiente" y ya está resuelto, o al revés).
- 🚨 FUGA: NO encontraste ese dato en ningún archivo. Esto es lo que
  estamos buscando — información que solo existe en tu memoria y en
  ningún documento del proyecto.

**Entregable:** una tabla con las 3 columnas (afirmación / categoría /
evidencia o ausencia de ella), y al final un resumen: cuántas fugas reales
encontraste, si las hay, y cuáles son en una frase cada una.

No hace falta que seas exhaustivo con cosas triviales — enfocate en
decisiones, hallazgos técnicos, o detalles operativos que, si se pierden,
le costarían tiempo real al proyecto reconstruir.
