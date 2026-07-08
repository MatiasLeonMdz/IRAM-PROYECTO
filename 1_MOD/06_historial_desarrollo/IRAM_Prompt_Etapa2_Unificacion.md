# IRAM — Prompt Etapa 2: Unificación de los 5 Agentes

> **Uso:** Aplicar este prompt DESPUÉS de completar la Etapa 1 en los 5 archivos.  
> Proporcionar los 5 archivos limpios juntos. El resultado es un único `.md` unificado.

---

## Instrucciones para el modelo

Sos un editor técnico especializado en documentación de proyectos de modding.  
Voy a darte 5 archivos Markdown ya limpios, uno por cada agente IA del proyecto **IRAM** (mod de Imperator Rome):

- Diseñador 1  
- Diseñador 2  
- Programador 1  
- Programador 2  
- [Agente 5]

El proyecto tiene 4 fases en orden: **Estable → Alt → v3 → v4**.  
Tu tarea es fusionar los 5 archivos en **un único documento Markdown unificado**.

---

## PASO 1 — Header del documento unificado

Al inicio del documento generar:

```markdown
# IRAM Project — Historial Unificado

> Proyecto: Mod de Imperator Rome (IRAM)
> Fases: Estable → Alt → v3 → v4
> Agentes: Diseñador 1, Diseñador 2, Programador 1, Programador 2, [Agente 5]
> Total de sesiones: [N]
> Rango temporal: [fecha más antigua] → [fecha más reciente]
> Generado: [fecha de hoy]
```

---

## PASO 2 — Índice maestro

Después del header, insertar:

```markdown
## Índice maestro

| N° Global | Fecha | Agente | Título | Fase | Tipo | Relevancia |
|-----------|-------|--------|--------|------|------|------------|
```

**Tipos posibles:** Diseño | Programación | Bug fix | Decisión | Release | Investigación  
**Relevancia:** 🔴 Crítica | 🟡 Media | 🟢 Menor

---

## PASO 3 — Línea de tiempo por fase

Antes del historial de sesiones, insertar:

```markdown
## Línea de tiempo del proyecto

### Fase: Versión Estable
- [AAAA-MM-DD] — [evento clave] — Agente: X

### Fase: Alt
- ...

### Fase: v3
- ...

### Fase: v4
- ...
```

> Incluir **solo** eventos 🔴 Críticos y 📦 Releases.

---

## PASO 4 — Reglas de fusión del historial

**4.1 — Orden cronológico global**  
Tomar todas las sesiones de los 5 archivos y ordenarlas por `Fecha/hora` en una única línea de tiempo.  
Si dos sesiones tienen la misma fecha/hora, el orden de desempate es:  
`Diseñador 1 → Diseñador 2 → Programador 1 → Programador 2 → Agente 5`

**4.2 — Numeración global**  
Renumerar todas las sesiones con un número global único (N° Global) que no repita el número de sesión original por agente.  
Conservar el número de sesión original como referencia:

```markdown
## Sesión 042 (Diseñador 2 — Sesión 07 original)
```

**4.3 — Identificación de agente visible**  
Cada sesión debe mostrar claramente de qué agente proviene. El bloque de metadatos ya incluye `**Agente:**`.

**4.4 — Detección de sesiones relacionadas (trabajo paralelo)**  
Si dos o más sesiones de agentes distintos ocurren el **mismo día** y tratan el **mismo tema**  
(mismo bug, mismo sistema, misma decisión), agruparlas bajo un encabezado:

```markdown
### 🔗 Trabajo paralelo — [AAAA-MM-DD] — [tema]
```

Y listar las sesiones una debajo de la otra en orden de agente.

**4.5 — Detección de duplicados entre archivos**  
Si el mismo mensaje humano o la misma pregunta aparece en más de un archivo  
(mismo texto, distinto agente), conservar **solo la instancia con la respuesta más completa**.  
Agregar nota:

```
> ⚠️ Duplicado entre agentes — versión más completa conservada.
> Versión descartada: [Agente X — Sesión Y original]
```

---

## PASO 5 — Documento de cierre

Al final del documento unificado, agregar:

```markdown
---

## Estado del proyecto al cierre del historial

### 🐛 Bugs confirmados sin fix documentado
<!-- Todo 🐛 que no tenga un ✅ asociado en ningún agente -->
- [Sesión N° Global] [Agente] — descripción

### ✅ Fixes aplicados (resumen cruzado)
- [Sesión N° Global] [Agente] — descripción — cierra Bug de Sesión: X

### 🏗️ Decisiones de diseño vigentes
<!-- Todos los 🏗️ que no fueron revertidos por una decisión posterior -->
- [Sesión N° Global] [Agente] — descripción

### 📋 TODOs pendientes sin resolver
<!-- Todos los 📋 sin cierre documentado en ningún agente -->
- [Sesión N° Global] [Agente responsable] — tarea

### 📌 Reglas del proyecto vigentes
<!-- Todos los 📌 en orden numérico, sin importar el agente que las definió -->
- R1 — descripción — definida en Sesión N° Global [Agente]
- R2 — ...

### 📦 Historial de releases
- [fecha] — [versión] — Agente: X — Sesión N° Global

### Versión más reciente documentada
[último 📦 Release mencionado en cualquier agente]
```

---

## Restricciones

- **No resumir ni parafrasear** ningún mensaje. Solo estructurar, etiquetar y fusionar.
- **Conservar intacto** todo el código `pdxscript`, tablas Markdown y respuestas técnicas.
- Si una sesión es ambigua en fase o tipo, usar `Múltiple` o `Sin clasificar` y agregar:  
  `> ⚠️ Clasificación manual recomendada`
- Si el documento resultante es muy largo, procesarlo en bloques y confirmar al terminar cada uno.
- Output final: **un único archivo Markdown válido**, listo para GitHub u Obsidian.

---

## Orden de trabajo sugerido

1. Leer los 5 archivos completos antes de empezar a escribir.
2. Construir el índice maestro primero (te da el mapa completo).
3. Detectar y marcar trabajo paralelo y duplicados entre agentes.
4. Generar la línea de tiempo por fase.
5. Escribir el historial fusionado en orden cronológico.
6. Generar el documento de cierre cruzando todos los callouts.

---

*Al terminar, confirmar con:*  
`✓ Historial unificado — N sesiones totales — N bugs — N fixes — N decisiones — N pendientes — N reglas`
