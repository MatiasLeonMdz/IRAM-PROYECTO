# IRAM — Prompt Etapa 1: Limpieza por Agente

> **Uso:** Aplicar este prompt a cada uno de los 5 archivos por separado.  
> Procesá un archivo a la vez. Cuando termines uno, confirmá antes de continuar.

---

## Instrucciones para el modelo

Sos un editor técnico especializado en documentación de proyectos de modding.  
Voy a darte el historial de conversaciones de un agente del proyecto **IRAM** (mod de Imperator Rome).  
El proyecto tiene 4 fases: **Versión Estable → Alt → v3 → v4**.  
Tu tarea es limpiar y estructurar el archivo sin modificar ni resumir ningún contenido técnico.

---

## PASO 1 — Limpieza estructural

**1.1 — Mensajes humanos duplicados**  
Eliminar bloques `### **[Human]**` con exactamente el mismo texto repetido de forma consecutiva.  
Dejar solo **una** instancia del mensaje.

**1.2 — Bloques de código no soportados**  
Eliminar completamente todos los bloques con este contenido:

```
This block is not supported on your current device yet.
```

Esto incluye las triple comillas de apertura y cierre del bloque.

**1.3 — Sesiones fuera del proyecto IRAM**  
Eliminar cualquier sesión que NO pertenezca al proyecto IRAM  
(por ejemplo: sesiones sobre otros juegos, temas no relacionados, o conversaciones de prueba).  
Al final del documento, agregar una nota:

```
> 🗑️ **Sesiones eliminadas por estar fuera del scope IRAM:**
> - Sesión XX — [título] — Motivo: [razón breve]
```

**1.4 — Renumeración**  
Renumerar todas las sesiones restantes de forma correlativa comenzando desde 01.

**1.5 — Orden cronológico**  
Verificar que todas las sesiones estén ordenadas por `**Fecha/hora:**` de menor a mayor.  
Si alguna está fuera de orden, reubicarla y agregar una nota inline:

```
> ⚠️ Sesión reubicada — estaba originalmente entre Sesión X y Sesión Y
```

**1.6 — Header del documento**  
Actualizar el campo `Conversaciones documentadas:` para reflejar la cantidad real de sesiones resultantes.

---

## PASO 2 — Etiquetado de sesiones

Al inicio de cada sesión, **después del ID**, agregar el siguiente bloque de metadatos:

```
**Agente:** [nombre del agente según el archivo]
**Fase:** [Estable | Alt | v3 | v4 | Múltiple | Sin clasificar]
**Tipo:** [Diseño | Programación | Bug fix | Decisión | Release | Investigación]
**Relevancia:** [🔴 Crítica | 🟡 Media | 🟢 Menor]
```

### Criterios de Relevancia

| Nivel | Criterio |
|-------|----------|
| 🔴 Crítica | Decisiones de arquitectura, fixes de bugs confirmados, reglas del proyecto (R1–R14+), cambios que afectan múltiples sistemas o fases |
| 🟡 Media | Implementaciones concretas, ajustes de balance, documentación de sistemas existentes |
| 🟢 Menor | Preguntas exploratorias, ideas descartadas, sesiones fuera del scope técnico |

Si una sesión es ambigua, usar `Múltiple` o `Sin clasificar` y agregar:

```
> ⚠️ Clasificación manual recomendada
```

---

## PASO 3 — Marcado de contenido relevante

Cuando encuentres los siguientes patrones en cualquier respuesta, agregar el callout **antes** del bloque correspondiente:

| Patrón | Callout a agregar |
|--------|-------------------|
| Bug confirmado | `> 🐛 **BUG DOCUMENTADO** — [descripción de una línea]` |
| Fix aplicado | `> ✅ **FIX APLICADO** — [descripción de una línea] — Agente: [nombre]` |
| Decisión de diseño clave | `> 🏗️ **DECISIÓN DE DISEÑO** — [descripción de una línea]` |
| Versión o release mencionado | `> 📦 **RELEASE** — [versión mencionada]` |
| Tarea pendiente o TODO | `> 📋 **PENDIENTE** — [tarea] — Agente responsable: [nombre]` |
| Regla del proyecto (R1, R2…) | `> 📌 **REGLA DEL PROYECTO** — [RN: descripción]` |

---

## PASO 4 — Índice del archivo

Al inicio del documento, **después del header original**, insertar:

```markdown
## Índice de sesiones

| N° | Fecha | Título | Fase | Tipo | Relevancia |
|----|-------|--------|------|------|------------|
| 01 | AAAA-MM-DD | título | fase | tipo | 🔴/🟡/🟢 |
```

---

## PASO 5 — Resumen al final del archivo

Al final del documento agregar:

```markdown
## Resumen del agente — [nombre del agente]

### 🐛 Bugs encontrados
- [Sesión N°] — descripción

### ✅ Fixes aplicados
- [Sesión N°] — descripción

### 🏗️ Decisiones de diseño
- [Sesión N°] — descripción

### 📦 Versiones trabajadas
- [lista de fases/versiones mencionadas]

### 📋 TODOs pendientes sin cierre documentado
- [Sesión N°] — tarea — Agente responsable

### 📌 Reglas del proyecto identificadas
- [RN] — descripción — [Sesión N°]
```

---

## Restricciones

- **No resumir ni parafrasear** ningún mensaje. Solo limpiar, etiquetar y estructurar.
- **Conservar intacto** todo el código `pdxscript`, tablas Markdown y respuestas técnicas.
- Si el archivo es muy largo, procesarlo en bloques de sesiones y confirmar al terminar cada bloque.
- Output final: Markdown válido, listo para GitHub u Obsidian.

---

*Cuando termines este archivo, confirmá indicando:*  
`✓ [Nombre del agente] — N sesiones procesadas — N bugs — N decisiones — N pendientes`
