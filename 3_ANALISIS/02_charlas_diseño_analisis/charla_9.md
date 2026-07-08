sesiones 7 y 8 cortadas, adjunto los archivos .md más recientes y un .zip actualizado


Pensó durante 1m 52s
Pensó durante 1m 52s
Looking at the files the user has uploaded for the IRAM project—they mention sessions 7 and 8 were interrupted, and they're providing the latest markdown files along with an updated zip archive to continue from where they left off. So three markdown files that should be in context aren't showing up in the documents block—FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md, charla_8.md, and charla_7.md—which means I'll need to read them directly from disk. The FUENTE_DE_VERDAD file is especially critical since the user describes it as the only operational starting point for the project, so I should check what's actually available on the filesystem rather than assuming it's missing.

The PROMPT_CONTINUACION file itself contains instructions for how to proceed this session, telling me which sections to prioritize and presenting a checklist of possible tasks to work on—but none of them are checked, so I don't yet know which direction the user wants to go. case for using ask_user_input_v0 to surface the menu options and let them specify which task(s) they want to focus on this session, since the continuation prompt explicitly presents a checklist without any selections made.

Before I do that though, I need to read the FUENTE_DE_VERDAD file from disk to understand the current state and context, so I can present the options intelligently. The continuation prompt emphasizes reading this file completely first. I also notice the uploaded zip file is version 3, not version 2 as referenced in the prompt text, so I'll need to account for that when examining the project structure. I need to follow the user's system carefully here—they've built a custom workflow for managing complex projects across sessions, and I should respect that structure. Let me start by checking what files are actually available, then read through the source-of-truth document completely to understand their methodology and current progress, followed by the session transcripts that got cut off to see what context might be…

Mostrar menos
Listo
Voy a revisar primero qué hay disponible y cómo abordar cada tipo de archivo antes de leer nada.


Archivo visualizado, ejecutó un comando
Archivo visualizado, ejecutó un comando

Revisar la guía para leer archivos subidos que no están en el contexto
Let me check what files are in the uploads directory and see their sizes.


Verificar tamaño de todos los archivos subidos antes de leerlos
bash

ls -la /mnt/user-data/uploads/ && echo "---" && for f in /mnt/user-data/uploads/*; do echo "=== $f ==="; wc -l "$f" 2>/dev/null; wc -c "$f" 2>/dev/null; done
Salida

total 89628
drwxr-xr-x 1 claude ubuntu        0 Jul  8 01:41 .
drwxr-xr-x 5 root   root       4096 Jul  8 01:41 ..
-rw-r--r-- 1 claude ubuntu    90155 Jul  8 01:38 FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md
-rw-r--r-- 1 claude ubuntu 91547104 Jul  8 01:39 IRAM_PROYECTO_REORGANIZADO3.zip
-rw-r--r-- 1 claude ubuntu     3422 Jul  8 01:38 PROMPT_CONTINUACION_2026-07-07_8.md
-rw-r--r-- 1 claude ubuntu    14031 Jul  8 01:38 WIKI_DOCUMENTACION_v3.md
-rw-r--r-- 1 claude ubuntu    57092 Jul  8 01:38 charla_7.md
-rw-r--r-- 1 claude ubuntu    37647 Jul  8 01:38 charla_8.md
-rw-r--r-- 1 claude ubuntu     9173 Jul  8 01:38 estructura_objetivos_iram.svg
---
=== /mnt/user-data/uploads/FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md ===
490 /mnt/user-data/uploads/FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md
90155 /mnt/user-data/uploads/FUENTE_DE_VERDAD_IRAM_2026-07-07_8.md
=== /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip ===
351886 /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip
91547104 /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip
=== /mnt/user-data/uploads/PROMPT_CONTINUACION_2026-07-07_8.md ===
53 /mnt/user-data/uploads/PROMPT_CONTINUACION_2026-07-07_8.md
3422 /mnt/user-data/uploads/PROMPT_CONTINUACION_2026-07-07_8.md
=== /mnt/user-data/uploads/WIKI_DOCUMENTACION_v3.md ===
197 /mnt/user-data/uploads/WIKI_DOCUMENTACION_v3.md
14031 /mnt/user-data/uploads/WIKI_DOCUMENTACION_v3.md
=== /mnt/user-data/uploads/charla_7.md ===
548 /mnt/user-data/uploads/charla_7.md
57092 /mnt/user-data/uploads/charla_7.md
=== /mnt/user-data/uploads/charla_8.md ===
377 /mnt/user-data/uploads/charla_8.md
37647 /mnt/user-data/uploads/charla_8.md
=== /mnt/user-data/uploads/estructura_objetivos_iram.svg ===
30 /mnt/user-data/uploads/estructura_objetivos_iram.svg
9173 /mnt/user-data/uploads/estructura_objetivos_iram.svg
I'm checking the file size of FUENTE_DE_VERDAD—it's 90KB across 490 lines, which exceeds the truncation threshold, so I'll need to view it in sections rather than all at once to get the full content. I'm settling on a three-chunk approach for the main file—splitting around 150 lines per view to stay well under any character limits—then I'll handle the other files similarly based on their sizes. Let me start by viewing the most critical document in sections, beginning with the first chunk.

Listo
El archivo principal (FUENTE_DE_VERDAD) tiene 490 líneas / 90KB, así que lo voy a leer en tramos completos para no perder nada por truncamiento.


The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is the summary: Reconciled project status across multiple packages and verified source transcripts
The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is the summary: Reconciled project status across multiple packages and verified source transcripts

Leer la fuente de verdad, tramo 1/4
I need to look at the missing sections that contain the key structural information—there are several important sections (§2 through §5) that got cut off, and section 5 apparently has the crucial unified task table with 18 rows that I need to see.


Leer la fuente de verdad, tramo con secciones 2-5 (tabla de tareas)
I'm checking the rows in the tasks table to make sure I have all the data I need—looks like I've seen rows 1-8 in the recent chunk, but I need to verify I have the complete set up to row 18 as specified.


Leer la fuente de verdad, tramo 2/4 (secciones 7-11 aprox)
I need to review the remaining sections and fill in the gap around lines 221-260 to get the full context on Paquete C, which is relevant to the task options ahead.


Completar la sección del Paquete C (contexto casos #7 y #8) que quedó truncada
Now I'm moving forward to review sections 12 through the end of the document, picking up from where I left off in the package definitions.


Leer la fuente de verdad, tramo 3/4 (sección 12 en adelante)
I need to go back and review the sections I missed earlier in the document, then continue reading through to the end.


Completar el tramo faltante de la sección 13 (pregunta #1 detalle)
I need to retrieve the remaining sections from the document, specifically the rest of §14 and all of §15, which covers the Paquete C partial closure and the status of Cases #7 and #8.


Leer el tramo final: resto de sección 14 y toda la sección 15 (cierre más reciente)
I see the task table originally had 17 rows, then task #18 was added later, giving us the 18 total rows mentioned in the continuation. Looking at the current state, Paquete A is closed as of the updates in sections 10 and 11.

Paquete B is also closed now—all 4 questions resolved and task #18 created to update the PROMPT_MAESTRO to a sequential rotation model. Paquete C is partially closed: Case #7 about the paper is resolved (IRAM_C1_final.md is the current version, no merge needed), but Case #8 about skill is characterized but still undecided, which matches exactly what the continuation prompt's first checklist option describes. Paquetes D, E, and F haven't been touched yet.

The critical blocker is Task #1 (DR-54) with the UTN deadline of July 15, 2026—that's 8 days away from today, July 7, 2026. Now I need to read through charla_7.md and charla_8.md to see the raw transcripts from those sessions, since section 15 notes the session was cut off before the operator could respond to the question being asked.

Looking at the version history more carefully, each numbered version corresponds to adding one section: version _2 is the original, _3 added sections 10 and 11, _5 added section 12, _6 added section 13, _7 added section 14, and _8 (the current file) added section 15. So the versioning tracks incremental progress through the document structure.

The uploaded files charla_7.md and charla_8.md are likely the raw transcripts from the sessions that produced versions _7 and _8 respectively. Section 15's own text confirms that session 8 was cut off right after characterizing Case #8, before the user could respond. For session 7, section 14 appears to have been completed with a formal closure of Package B and was explicitly delivered to the operator, though the user's mention of "sessions 7 and 8 cut off" might just mean both sessions were interrupted at some point, whether or not they were fully saved.

…

Mostrar menos
Listo
Ahora voy a revisar las transcripciones crudas de las sesiones 7 y 8, ya que el mensaje del usuario indica que se cortaron — quiero confirmar que no quedó nada sin capturar en la fuente de verdad.


The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is my summary: Reconciled file discrepancies and flagged critical documentation gaps
The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is my summary: Reconciled file discrepancies and flagged critical documentation gaps

Leer transcripción cruda de la sesión 8 (charla_8), tramo 1/2
I'm looking at a transcript where Claude was reconstructing a previous session and building an SVG diagram to organize tasks by category—Análisis, Documentación, and Portafolio UTN. The transcript reveals there were actually two separate cutoff points: the first happened right after characterizing Caso #8 (which is documented in FUENTE_DE_VERDAD_8.md), and there was a second cutoff that's partially described here.

But wait—FUENTE_DE_VERDAD_8.md doesn't mention any of this SVG work or task categorization at all. It stops at §15 with the Case #8 decision still pending. So this charla_8.md transcript shows work that happened in a follow-up session after the original document was written, and all this subsequent work—the diagram, the categorization—hasn't been captured in any FUENTE_DE_VERDAD version yet. That's exactly the kind of unabsorbed content I was concerned about. I need to keep reading to see what else is in charla_8.md and understand the full scope of what's been done but not yet documented.

Mostrar menos

Leer transcripción cruda de la sesión 8 (charla_8), tramo 2/2
I'm reviewing the charla_8.md session where I reconstructed the interrupted work, built the SVG diagram, identified which of the 18 tasks fall under "Análisis", and discovered that plan.md and SESSION_LOG_REPLANTEO_2026-07-05_01-37.md are missing from the ZIP file. For Case #8 regarding the skill decision, I recommended keeping the base version as C2 while archiving the (2)/(3) version as reference material rather than discarding it.

But now the user is correcting me—they're saying "wrong, both files that I'm sending you are also in the zip I attached," which contradicts my claim that those two files aren't in the ZIP. The user is pushing back on my search results, suggesting that both files are actually present in the ZIP they provided, so I need to reconsider my analysis.

This is a critical moment because it reveals I made an error in the previous session—I incorrectly concluded those files were missing when they're apparently there. And since we're now working with a newly reorganized ZIP (IRAM_PROYECTO_REORGANIZADO3.zip), I need to verify this claim against the current version.

What's also striking is that the entire SVG-based framework I've been discussing—the Mod → Análisis → Documentación → Portafolio UTN structure with the DR-54 shortcut—doesn't appear anywhere in the source of truth document. This is new content from a session after the source of truth was written, and it hasn't been consolidated yet. Similarly, my recommendation about Case #8 (using the base version as C2 and archiving the others as input for C1) is also a new development that hasn't made it into the official source of truth, and it could be directly relevant to answering the current question. So there's a critical gap here: charla_8.md documents work that never made it into FUENTE_DE_VERDAD_8.md—the SVG diagram categorization, the task breakdown for Análisis, and a Case #8 recommendation—all happening in a continuation session that cut off again before the operator's correction about t…

Mostrar menos
Listo
Esto es clave: charla_8.md termina con una corrección del operador sin responder. Voy a revisar charla_7.md para entender si es la sesión previa que se pegó como transcripción, o algo distinto.


Reconstructed project timeline and identified unresolved decision points
Reconstructed project timeline and identified unresolved decision points

Leer transcripción cruda de la sesión 7 (charla_7), tramo 1/4
So charla_7.md is actually a transcript from a previous session that used the exact same continuation prompt—referencing the same source file and checklist—which means the operator had already started working through this process before.

Now I'm trying to piece together the timeline: if FUENTE_DE_VERDAD_8.md itself documents where that earlier session cut off (right after characterizing Case #8, before the operator could respond), then that same document was generated during that interrupted session and delivered as an attachment. This suggests the sequence is that one session opened Package C, resolved Case #7, characterized Case #8, and then got cut off mid-exchange.

Then a new session started using the continuation prompt referencing _8.md—this appears to be charla_7.md, where the operator chose to finish Package C Case #8, and Claude re-read both skill versions to verify everything before continuing. That session likely built on the SVG diagram work or got interrupted itself.

Then charla_8.md shows yet another recovery session, where a transcript of interrupted work (possibly from charla_7) was pasted back in, Claude reconstructed the context, answered the pending Análisis question, delivered the Case #8 recommendation, and the session ended with the operator's feedback about the zip file contents. So charla_7.md and charla_8.md are both separate files from today's upload, and the user mentioned sessions 7 and 8 were cut off. It looks like charla_7.md might be the earlier interrupted session that built the SVG diagram, while charla_8.md's first message contains a pasted transcript of that same earlier session plus new file attachments for recovery.

The key thing I need to check is whether there's any information in these chat files that hasn't made it into the current source of truth document yet—specifically the SVG-based categorization model showing the pipeline from Mod through Análisis, Documentación, and Portafolio UTN, with DR-54 as a reference point.
…

Mostrar menos

Leer transcripción cruda de la sesión 7 (charla_7), tramo 2/4
I'm noticing a discrepancy between the recommendations in charla_7.md and charla_8 — the earlier version suggested merging the two C2 entries into a single one, arguing they're complementary rather than competing, and that keeping them separate creates a technical problem with duplicate frontmatter fields. The reasoning was that consolidating them preserves all the content rather than losing information by choosing one version.

But charla_8 recommended a different approach: selecting a base version and archiving the alternative. This is a meaningful shift in strategy that I should flag explicitly, especially given how carefully the project tracks reconciliation and prevents drift between sessions.

I need to trace back through charla_7 more carefully to understand why the merge recommendation was made, and then figure out what changed between sessions—whether new evidence like the DR-52 Paquete D discovery about objectives shifted the calculus, or if there's simply an unresolved inconsistency that needs operator confirmation.

Mostrar menos

Completar tramo faltante de charla_7 (transición hacia Paquete D / objetivos)
I see the operator is asking me to think deeply about the project's objectives—the four deliverables of modules, documentation, UTN work, and portfolio—and how they fit within the three main branches of modules, documentation, and analysis, before I formulate a proposal. They're also asking for my opinion on something, though the message appears to cut off mid-sentence. So the distinction is that "Análisis" actually does come from the operator's own language in charla_7, not purely from my interpretation—it's embedded in their conversational framing even if it doesn't appear in the formal document text. I need to keep reading charla_7 to see where this thread leads and how it connects to the broader project structure.


Leer transcripción cruda de la sesión 7 (charla_7), tramo 3/4
I'm continuing to read through the rest of the document to see what comes next.


Leer transcripción cruda de la sesión 7 (charla_7), tramo final
Looking at the session logs, charla_7.md cuts off mid-SVG while Claude was actively writing the diagram code, with no follow-up response from the operator after that point.

However, charla_8.md later confirms the SVG file itself (estructura_objetivos_iram.svg) was successfully saved and is complete and intact—so even though the transcript display got cut off, the actual file made it to disk.

Now I'm piecing together the full timeline: FUENTE_DE_VERDAD_8.md ended with an unresolved decision point on Case #8, then charla_7.md picked up using the continuation prompt, where Claude re-verified the two skill file versions, recommended merging them into a single C2 file, and the operator asked for clarification on what each file does in the project.

The operator then posed a larger strategic question: to reflect on the project's four products (mod, documentación, trabajo UTN, portafolio) and its three major branches (Mod, Documentación, Análisis), and to weigh in on the project's narrative arc around learning to work with AI across sessions.

Claude investigated further, uncovered a DR-52 correction showing C1/C2 are auxiliary to objetivo-3 rather than equal products, spotted a tension in Paquete D about whether C2 already exists, reasoned through whether this changes the merge approach (concluding it's still sound as consolidation rather than a post-objetivo-3 generation event), and confirmed the physical folder structure across the three main directories.

I then examined the portafolio_UTN contents—just assignment prompts so far, no actual deliverables—and mapped the four products to three structural branches with Análisis as the connective pipeline between them. I started sketching an SVG diagram showing the flow from Mod through Análisis to Documentación and Portafolio_UTN, with a bypass arrow for the Entrega 1 requirement, but the transcript cut off mid-code before I could deliver the full response with the diagram, narrative opinion, and merge proposal.

…

Mostrar menos
Listo
Voy a resolver rápidamente la disputa que quedó pendiente al final de charla_8 (si plan.md y el log de DR-54 están o no en el ZIP), verificando contra el ZIP actualizado. También quiero ver el SVG rescatado.


The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is my summary: Reconciled file structure discrepancies and verified project reorganization
The user prompt is empty, so I cannot determine the primary language. However, based on the thinking block being in English, here is my summary: Reconciled file structure discrepancies and verified project reorganization

Ver el listado del ZIP actualizado (v3) antes de extraer nada
bash

cd /home/claude && unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | head -20 && echo "..." && unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | tail -5
Salida

Archive:  /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-07-07 22:34   IRAM_PROYECTO_REORGANIZADO/
   227172  2026-07-07 01:29   IRAM_PROYECTO_REORGANIZADO/charla 1.md
    23280  2026-07-07 01:29   IRAM_PROYECTO_REORGANIZADO/charla 2.md
    28045  2026-07-07 14:20   IRAM_PROYECTO_REORGANIZADO/charla 3.md
     8707  2026-07-07 14:33   IRAM_PROYECTO_REORGANIZADO/charla 4.md
    20695  2026-07-07 15:41   IRAM_PROYECTO_REORGANIZADO/charla 5.md
   102154  2026-07-07 16:07   IRAM_PROYECTO_REORGANIZADO/charla 6.md
   120731  2026-07-06 23:16   IRAM_PROYECTO_REORGANIZADO/CHAT_DE_LOG_AUDITORIA_CONTINUIDAD_2026-07-06.md
    29761  2026-07-06 22:46   IRAM_PROYECTO_REORGANIZADO/colisiones_verificadas_2026-07-06.txt
     2910  2026-07-05 02:13   IRAM_PROYECTO_REORGANIZADO/deepseek_markdown_20260705_98aa15(1).md
     2910  2026-07-05 02:12   IRAM_PROYECTO_REORGANIZADO/deepseek_markdown_20260705_98aa15.md
    39679  2026-07-07 00:17   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07 2.md
    28659  2026-07-07 00:11   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07.md
    52816  2026-07-07 14:37   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07_3.md
    48055  2026-07-07 14:28   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07_4.md
    54898  2026-07-07 15:57   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07_5.md
    69671  2026-07-07 18:54   IRAM_PROYECTO_REORGANIZADO/FUENTE_DE_VERDAD_IRAM_2026-07-07_6.md
...
    13572  2026-07-05 23:37   IRAM_PROYECTO_REORGANIZADO/verificar_iram.py
     4844  2026-07-04 23:01   IRAM_PROYECTO_REORGANIZADO/volcado_memoria (2).md
     4844  2026-07-04 23:01   IRAM_PROYECTO_REORGANIZADO/volcado_memoria.md
---------                     -------
369143900                     3082 files
This v3 zip has a completely different structure than what was described before—it's flat with all the files directly in the root folder rather than organized into subdirectories like the previous versions had.

Let me dig deeper to understand what's actually here. The file count jumped from 2382 to 3082 files, which makes sense if this is an updated version that accumulated more charla files, additional FUENTE_DE_VERDAD versions, and wiki content. I need to check whether the reorganized folder structure (1_MOD, 2_DOCUMENTACION, etc.) actually exists in this zip, find plan.md, and get a clearer picture of the overall organization.


Buscar estructura de carpetas, plan.md, el log de DR-54 y los artefactos de la Fase 1 en el zip v3
bash

cd /home/claude && echo "=== Carpetas de primer/segundo nivel ===" && unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | awk '{print $4}' | grep -oE "^IRAM_PROYECTO_REORGANIZADO/[^/]*/[^/]*/" | sort -u | head -30
echo
echo "=== ¿plan.md existe? ==="
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | grep -i "plan\.md"
echo
echo "=== ¿01-37 existe? ==="
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | grep -i "01-37\|01_37"
echo
echo "=== ¿tabla_analisis.csv / exportar_tabla existe? ==="
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | grep -i "tabla_analisis\|exportar_tabla"
echo
echo "=== Conteo total de archivos ==="
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | tail -1
Salida

=== Carpetas de primer/segundo nivel ===

=== ¿plan.md existe? ===
    27027  2026-07-05 05:01   IRAM_PROYECTO_REORGANIZADO/plan.md

=== ¿01-37 existe? ===
    15808  2026-07-05 01:41   IRAM_PROYECTO_REORGANIZADO/SESSION_LOG_REPLANTEO_2026-07-05_01-37.md

=== ¿tabla_analisis.csv / exportar_tabla existe? ===

=== Conteo total de archivos ===
369143900                     3082 files
The files plan.md and SESSION_LOG_REPLANTEO_2026-07-05_01-37.md are actually present in the updated zip at the root level of the IRAM_PROYECTO_REORGANIZADO folder, confirming this is a reorganized version of the project.

This v3 zip appears to have a different structure than what FUENTE_DE_VERDAD describes — it has loose files at the root (charla files, FUENTE_DE_VERDAD versions, plan.md, session logs) rather than the nested 1_MOD/2_DOCUMENTACION/3_PORTAFOLIO_UTN structure with 2382 files. I should verify whether the subfolder structure still exists underneath, since my previous search might have missed it.


Entender la estructura real del zip v3 (carpetas de primer nivel)
bash

cd /home/claude && echo "=== Todas las carpetas (directorios) del zip ===" 
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | grep "/$" 
echo
echo "=== Conteo de archivos por carpeta de primer nivel dentro de IRAM_PROYECTO_REORGANIZADO/ ==="
unzip -l /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip | awk 'NR>3 {print $4}' | grep -v '^$' | sed 's|^IRAM_PROYECTO_REORGANIZADO/||' | awk -F/ '{print $1}' | sort | uniq -c | sort -rn | head -20
Salida

=== Todas las carpetas (directorios) del zip ===
        0  2026-07-07 22:34   IRAM_PROYECTO_REORGANIZADO/
        0  2026-07-05 03:48   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/
        0  2026-07-05 03:48   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/
        0  2026-07-05 19:34   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-4fce9ea4-dd95-420d-95b0-60f483da6b06-1778901623-ba4add5f-batch-0000/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-4fce9ea4-dd95-420d-95b0-60f483da6b06-1778901623-ba4add5f-batch-0000/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-6a75897c-cf3c-4d54-917c-c2ac7ed43411-1779141160-227caafc-batch-0000/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-6a75897c-cf3c-4d54-917c-c2ac7ed43411-1779141160-227caafc-batch-0000/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-7f3f05d6-4e30-458d-993a-2775665e8d57-1779142795-3a98d174-batch-0000/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-a158d766-708a-4586-b512-38b366ca7ea9-1779140644-664ff273-batch-0000/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-a158d766-708a-4586-b512-38b366ca7ea9-1779140644-664ff273-batch-0000/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-d64c441d-0410-463f-9819-e4a13ceed9c3-1778902202-94a93279-batch-0000/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/corpus_A_crudo/data-d64c441d-0410-463f-9819-e4a13ceed9c3-1778902202-94a93279-batch-0000/projects/
        0  2026-07-04 23:22   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/achievements/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/advice/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ai_budget/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ai_budget_categories/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ai_diplochance/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ai_objectives/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ai_plan_goals/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ambitions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/buildings/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/character_interactions/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/coat_of_arms/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/coat_of_arms/coat_of_arms/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/coat_of_arms/options/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/coat_of_arms/template_lists/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/combat_tactics/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/cultures/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/customizable_localization/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/deathreasons/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/defines/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/defines/audio/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/defines/graphic/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/defines/jomini/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/deities/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/deity_categories/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/diplomatic_stances/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/economic_policies/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/effect_localization/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ethnicities/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/event_pictures/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/event_themes/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/faction_impact/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/faction_impact/changing_laws/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/faction_impact/character_interactions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/faction_impact/diplomatic_actions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/game_concepts/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/genes/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/governments/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/governor_policies/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/graphical_culture_types/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_categories/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_effects/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_effect_tiers/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_materials/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_modules/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_names/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/great_work_templates/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/heritage/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/ideas/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/inventions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/laws/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/legion_distinctions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/levy_templates/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/loyalty/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/military_traditions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/missions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/modifiers/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/modifier_icons/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/named_colors/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/offices/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/on_action/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/opinions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/party_agendas/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/party_changes/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/party_types/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/pop_types/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/prices/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/province_names/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/province_ranks/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/religions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_effects/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_guis/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_lists/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_modifiers/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_tests/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/scripted_triggers/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/script_values/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/subject_types/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/technology_tables/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/terrain_types/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/titles/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/trade_goods/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/tradition_groups/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/traits/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/units/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/unit_abilities/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/common/wargoals/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/decisions/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/decisions/endgame_tags/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/decisions/tier_1_formables/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/decisions/tier_2_formables/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/1.1.0/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/1.2.0/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/dde/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/dhe/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/great_work_events/
        0  2024-04-25 16:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/1.3 - Livy/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/1.3 - Punic Wars/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/1.4 - Archimedes/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/1.4 - Magna Graecia/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/2.0 - Heirs of Alexander/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/mission_events/Epirus Pre-Order Pack/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/party_events/
        0  2024-04-25 15:55   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/game/events/religion_flavor/
        0  2026-07-05 19:34   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/hooks/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/info/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/logs/
        0  2026-05-28 03:41   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/logs/refs/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/logs/refs/heads/
        0  2026-05-28 03:41   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/logs/refs/remotes/
        0  2026-05-28 03:41   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/logs/refs/remotes/origin/
        0  2026-06-03 00:52   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/1c/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/28/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/3f/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/43/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/4c/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/6c/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/6f/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/85/
        0  2026-05-28 03:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/8a/
        0  2026-05-28 03:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/94/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/aa/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/ac/
        0  2026-05-28 03:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/ae/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/b1/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/b2/
        0  2026-05-28 03:40   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/b5/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/b7/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/c4/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/cc/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/cd/
        0  2026-05-28 04:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/da/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/df/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/ea/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/info/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/objects/pack/
        0  2026-05-28 03:41   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/refs/
        0  2026-06-03 00:18   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/refs/heads/
        0  2026-05-28 03:41   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/refs/remotes/
        0  2026-06-03 00:52   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/refs/remotes/origin/
        0  2026-05-28 03:38   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/.git/refs/tags/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/by_other_means/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/modifiers/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/on_action/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/scripted_effects/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/script_values/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/common/units/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/decisions/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/localization/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/localization/english/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/exodos/localization/spanish/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/the_great_leap/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_10_2026-05-29_05-07/the_last_vote/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/by_other_means/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/modifiers/
        0  2026-05-29 05:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/on_action/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/scripted_effects/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/script_values/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/common/units/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/decisions/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/localization/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/localization/english/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/exodos/localization/spanish/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/the_great_leap/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_16_2026-05-30_03-14/the_last_vote/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/by_other_means/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/common/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/common/modifiers/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/common/on_action/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/common/scripted_effects/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/common/units/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/decisions/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/events/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/localization/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/localization/english/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/exodos/localization/spanish/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/the_great_leap/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_8_2026-05-28_16-55/the_last_vote/
        0  2026-07-05 18:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/by_other_means/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/modifiers/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/on_action/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/scripted_effects/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/script_values/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/common/units/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/decisions/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/localization/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/localization/english/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/exodos/localization/spanish/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/by_other_means/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/modifiers/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/on_action/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/scripted_effects/
        0  2026-05-28 20:51   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/script_values/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/common/units/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/decisions/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/localization/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/localization/english/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/exodos/localization/spanish/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/the_great_leap/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/iram_v4_3_9/the_last_vote/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/the_great_leap/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM mod v5/mod_pack_IRAM_v4_3_9_2026-05-28_21-10/the_last_vote/
        0  2026-07-04 23:22   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/by_other_means/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/on_action/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/scripted_effects/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/units/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/decisions/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/events/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/english/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/spanish/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/the_great_leap/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/the_last_vote/
        0  2026-07-04 23:22   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/by_other_means/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/modifiers/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/on_action/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/scripted_effects/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/units/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/decisions/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/events/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/english/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/spanish/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/the_great_leap/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/the_last_vote/
        0  2026-07-04 23:22   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/by_other_means/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/
        0  2026-05-25 17:03   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/modifiers/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/on_action/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/scripted_effects/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/units/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/decisions/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/events/
        0  2026-05-25 17:03   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/english/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/spanish/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/the_great_leap/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/the_last_vote/
        0  2026-07-04 23:22   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/by_other_means/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/on_action/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/scripted_effects/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/scripted_guis/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/units/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/decisions/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/events/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/english/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/spanish/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/the_great_leap/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/the_last_vote/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/spanish/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/decisions/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/events/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/english/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/spanish/
        0  2026-07-04 23:23   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/common/
        0  2026-06-06 01:25   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/common/scripted_effects/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/english/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/modifiers/
        0  2026-06-06 00:58   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/on_action/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/scripted_effects/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/script_values/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/units/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/events/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/spanish/
        0  2026-07-04 23:23   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/common/
        0  2026-06-06 01:25   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/common/scripted_effects/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/english/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/modifiers/
        0  2026-06-06 00:58   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/on_action/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/scripted_effects/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/script_values/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/units/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/events/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/1_MOD/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/spanish/
        0  2026-07-05 03:48   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/01_logs_replanteo/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/02_charlas_y_resumenes/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/03_prueba_fuga_memoria/
        0  2026-07-05 03:48   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/04_corpus_A_mod_docs/
        0  2026-07-05 19:34   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 1/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 1/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 2/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 2/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 3/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 3/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 4/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 4/projects/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 5/
        0  2026-07-05 18:09   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/05_corpus_B_crudo/documentacion claude 5/projects/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/06_historial_desarrollo_mod/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/07_fuentes_documentacion/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/07_fuentes_documentacion/fuentes de documentacion/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/08_documentacion_respaldo/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/2_DOCUMENTACION/08_documentacion_respaldo/DOCUMENTACION/
        0  2026-07-05 03:48   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/3_PORTAFOLIO_UTN/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/3_PORTAFOLIO_UTN/consignas/
        0  2026-07-05 03:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/
        0  2026-07-04 23:21   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/
        0  2026-07-05 19:34   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-4fce9ea4-dd95-420d-95b0-60f483da6b06-1778901623-ba4add5f-batch-0000/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-4fce9ea4-dd95-420d-95b0-60f483da6b06-1778901623-ba4add5f-batch-0000/projects/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-6a75897c-cf3c-4d54-917c-c2ac7ed43411-1779141160-227caafc-batch-0000/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-6a75897c-cf3c-4d54-917c-c2ac7ed43411-1779141160-227caafc-batch-0000/projects/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-7f3f05d6-4e30-458d-993a-2775665e8d57-1779142795-3a98d174-batch-0000/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-a158d766-708a-4586-b512-38b366ca7ea9-1779140644-664ff273-batch-0000/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-a158d766-708a-4586-b512-38b366ca7ea9-1779140644-664ff273-batch-0000/projects/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-d64c441d-0410-463f-9819-e4a13ceed9c3-1778902202-94a93279-batch-0000/
        0  2026-07-05 18:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/historial viejo/data-d64c441d-0410-463f-9819-e4a13ceed9c3-1778902202-94a93279-batch-0000/projects/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/by_other_means/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_great_leap/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_alt___SUPERBACKUP_/the_last_vote/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_13__SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/by_other_means/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/on_action/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/scripted_effects/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/common/units/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/decisions/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/events/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/english/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/exodos/localization/spanish/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/the_great_leap/
        0  2026-05-15 23:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/by_other_means/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/modifiers/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/on_action/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/scripted_effects/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/common/units/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/decisions/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/events/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/english/
        0  2026-05-22 14:49   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/exodos/localization/spanish/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/the_great_leap/
        0  2026-05-22 14:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_15_GATHER_GLOBAL_v1_3/mod_pack/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/by_other_means/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/
        0  2026-05-25 17:03   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/modifiers/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/on_action/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/scripted_effects/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/common/units/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/decisions/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/events/
        0  2026-05-25 17:03   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/english/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/exodos/localization/spanish/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/the_great_leap/
        0  2026-05-25 17:04   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_1/mod_pack_v4_1/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/by_other_means/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/on_action/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/scripted_effects/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/scripted_guis/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/common/units/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/decisions/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/events/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/english/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/exodos/localization/spanish/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/the_great_leap/
        0  2026-05-15 16:08   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod_pack_IRAM_v4_3/mod_pack_IRAM_v4/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/by_other_means/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/on_action/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/scripted_effects/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/common/units/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/exodos/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_great_leap/localization/spanish/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/decisions/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/events/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/english/
        0  2026-07-04 23:24   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/documentacion iram 10-06-2026 00.30 (subcopia anidada)/IRAM_legacy v1 v2 v3 v4/mod___SUPERBACKUP_/the_last_vote/localization/spanish/
        0  2026-07-05 19:34   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/
        0  2026-07-05 18:11   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/common/
        0  2026-06-06 01:25   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/common/scripted_effects/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/english/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/by_other_means/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/modifiers/
        0  2026-06-06 00:58   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/on_action/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/scripted_effects/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/script_values/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/common/units/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/exodos/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_great_leap/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/events/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22/iram_work/the_last_vote/localization/spanish/
        0  2026-07-05 18:11   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/common/
        0  2026-06-06 01:25   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/common/scripted_effects/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/english/
        0  2026-06-06 01:33   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/by_other_means/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/modifiers/
        0  2026-06-06 00:58   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/on_action/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/scripted_effects/
        0  2026-06-06 00:27   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/script_values/
        0  2026-06-06 00:45   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/common/units/
        0  2026-06-09 02:53   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/events/
        0  2026-05-28 20:50   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/exodos/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_great_leap/localization/spanish/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/common/
        0  2026-06-08 20:10   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/decisions/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/events/
        0  2026-06-06 00:46   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/english/
        0  2026-06-06 01:06   IRAM_PROYECTO_REORGANIZADO/IRAM PROYECTO/_CUARENTENA_DUPLICADOS/fuentes de documentacion (subcopia anidada)/mod_pack_IRAM_v5_5_2026-06-09_03-22 (2)/iram_work/the_last_vote/localization/spanish/

=== Conteo de archivos por carpeta de primer nivel dentro de IRAM_PROYECTO_REORGANIZADO/ ===
   3035 IRAM
      6 charla
      1 volcado_memoria.md
      1 volcado_memoria
      1 verificar_iram.py
      1 sigue
      1 resultado_prueba_fuga_memoria.md
      1 reporte_resumen.txt
      1 plan.md
      1 memoria_claude_volcado.md
      1 instruccion_prueba_fuga_memoria.md
      1 deepseek_markdown_20260705_98aa15.md
      1 deepseek_markdown_20260705_98aa15(1).md
      1 colisiones_verificadas_2026-07-06.txt
      1 SESSION_LOG_REPLANTEO_2026-07-05_01-37.md
      1 SESSION_LOG_REPLANTEO_2026-07-05_00-52.md
      1 SESSION_LOG_REPLANTEO_2026-07-05_00-32.md
      1 SESSION_LOG_REPLANTEO_2026-07-05_00-10.md
      1 SESSION_LOG_REPLANTEO_2026-07-04_23-44.md
      1 SESSION_LOG_REPLANTEO_2026-07-04_23-17.md
I ran a grep search that was too broad and generated a lot of noise with folder listings, but I did confirm what I needed: the "IRAM PROYECTO" subfolder exists within the nested structure of "IRAM_PROYECTO_REORGANIZADO".

The new zip contains about 3035 files total under "IRAM_PROYECTO_REORGANIZADO/", which is more than the 2382 previously noted because the operator added additional files like charla files, more wiki versions, plan.md, deepseek/qwen drafts, SESSION_LOG_REPLANTEO logs, and memoria dumps. These loose files sit directly at the root of "IRAM_PROYECTO_REORGANIZADO/" rather than nested inside "IRAM PROYECTO/", meaning the operator consolidated all the scattered planning and session files into one place alongside the full project structure. This resolves the gap that charla_8 identified — plan.md and the SESSION_LOG_REPLANTEO series are now present, confirming the operator made a valid correction that either fixed a genuine absence in v2 or addressed a search issue on my end.

I have enough information now and should stop digging through the zip to avoid wasteful listing commands. The key facts are clear: v3 contains all the loose planning docs at the root (charla files 1-6, plan.md, all SESSION_LOG_REPLANTEO files, and FUENTE_DE_VERDAD versions 1-6), but charla_7 and charla_8 plus FUENTE_DE_VERDAD_7 and _8 are even more recent and not yet in this snapshot. The tabla_analisis.csv and exportar_tabla_analisis.py still don't exist, confirming task #2 remains blocked. The "IRAM PROYECTO" subfolder structure with its 1_MOD, 2_DOCUMENTACION, 3_PORTAFOLIO_UTN, and _CUARENTENA_DUPLICADOS directories is still intact.

Now I'll check the SVG file to complete my understanding before composing my response.

Mostrar menos
Listo
Buena información — confirmado que plan.md y el log de DR-54 sí están en el zip v3 (el operador tenía razón). Ahora reviso el SVG rescatado.


Synthesized multi-session findings and prioritized unresolved project paths
Synthesized multi-session findings and prioritized unresolved project paths

Ver el diagrama SVG rescatado (Mod → Análisis → Documentación → Portafolio UTN)
The SVG diagram confirms the flow structure with four sequential boxes—Mod, Análisis, Documentación, and Portafolio UTN—plus the bypass path from Análisis directly to Portafolio UTN that represents the DR-54 shortcut. The diagram's description clarifies how Mod generates the process history, Análisis transforms it into findings that feed into Documentación (which contains the C1 and C2 deliverables), and Documentación in turn feeds into the portfolio.

I've now fully absorbed all the source materials across the three charla sessions: the complete IRAM 2026 document with all 15 sections, the wiki documentation, and the full arc of charla_7 and charla_8, which covered skill file verification, the merge recommendation for Case #8, the four products and three branches narrative, the DR-52/Paquete D tension investigation, folder structure analysis, and the SVG diagram construction.

The critical issue I'm recognizing is that charla_7 and charla_8 generated substantial work—including the corrected Case #8 recommendation, the verification that plan.md and 01-37.md are present in the v3 zip (contrary to what was initially thought), confirmation that tabla_analisis.csv and exportar_tabla_analisis.py still don't exist, and the completed SVG—but none of this has been appended to FUENTE_DE_VERDAD_8.md. This is exactly the kind of continuity gap the project's methodology is designed to prevent, and it represents a significant unabsorbed session that needs to be documented.

The operator's original question about the project's narrative core—how they learned to work with AI—was also never answered before both sessions cut off. Given that Case #8 is the most in-flight item with two sessions of groundwork already done, I should present it as the natural next priority while still asking the operator how they want to proceed, especially since DR-54 has the external deadline pressure of the UTN delivery on 15/07. …

Mostrar menos
Listo
Voy a revisar rápidamente plan.md, ya que ahora está confirmado en el ZIP y es la fuente de varios cabos sueltos (definición de "objetivo 1", propuesta Fase 0 de DR-54).


Se ejecutaron 3 comandos
Se ejecutaron 3 comandos

Extraer plan.md y buscar las definiciones de 'objetivo' para cerrar el cabo suelto de charla_7/8
bash

cd /home/claude && unzip -p /mnt/user-data/uploads/IRAM_PROYECTO_REORGANIZADO3.zip "IRAM_PROYECTO_REORGANIZADO/plan.md" > plan.md 2>/dev/null && wc -l plan.md && echo "---objetivo mentions---" && grep -n -i "objetivo" plan.md | head -30
Salida

535 plan.md
---objetivo mentions---
6:NOTA DE CORRECCIÓN CRÍTICA: Esta versión reconoce que los conceptos DTI y FCC NO están documentados en los historiales previos. Son propuestas conceptuales nuevas generadas en la conversación del 2026-07-05. El objetivo de la Tarea 1.7 es encontrar evidencia empírica que respalde o refute las hipótesis sobre su origen.
19:2. OBJETIVOS FINALES DEL PROYECTO
20:Objetivo 1: Mod IRAM
25:Objetivo 2: Documentación del proceso
30:Objetivo 3: Análisis A/B + Diplomatura UTN
71:Objetivo: Definir la estructura exacta de la tabla que servirá de insumo para todos los análisis posteriores y para la Entrega 1 de la UTN.
178:    Variable objetivo: origen_propuesta (5 clases).
189:Objetivo: Generar tabla_analisis.csv con mínimo 50 filas, a partir de los archivos crudos.
223:Tarea 1.7: OBJETIVO PRINCIPAL: Encontrar el origen documental de los conceptos DTI y FCC
235:Objetivo: Redactar el documento de la Parte 1 siguiendo Consigna_1.md.
271:Objetivo: Diseñar prototipo de IA generativa / automatización y reflexión ética.
306:Objetivo: Usar la tabla de análisis para corregir las afirmaciones de autoría (S4A, S5) y extraer una skill operacional.
362:Objetivo: Resolver pendientes estructurales y de organización.
So plan.md actually spells out three distinct objectives—the IRAM module, process documentation, and an A/B analysis paired with a UTN diploma—but this framework contradicts what charla_7/8 established in their SVG diagram, which mapped a different progression: Mod → Análisis → Documentación → Portafolio U. I need to reconcile these two approaches. So the SVG diagram from charla_7/8 that shows Análisis as a pipeline stage between Documentación and Portafolio_UTN doesn't actually match plan.md's structure, where those two are unified under objetivo 3 rather than being sequential stages. I need to look at more context in plan.md to understand the actual objective definitions correctly.


Ver el contexto completo de la definición de objetivos en plan.md
bash

cd /home/claude && sed -n '1,45p' plan.md
Salida

PLAN DE TRABAJO INTEGRADO — IRAM / Documentación / Diplomatura UTN
Versión: 1.3 (Corregido con hipótesis de origen)
Fecha: 2026-07-05 04:30
Base: Logs de replanteo hasta DR-54, reorganización física completada (DR-51), inventario completado (DR-45–49)
Próximo hito crítico: Entrega Parte 1 UTN → 2026-07-15
NOTA DE CORRECCIÓN CRÍTICA: Esta versión reconoce que los conceptos DTI y FCC NO están documentados en los historiales previos. Son propuestas conceptuales nuevas generadas en la conversación del 2026-07-05. El objetivo de la Tarea 1.7 es encontrar evidencia empírica que respalde o refute las hipótesis sobre su origen.
1. ESTADO ACTUAL RESUMIDO

    Estructura física: APLICADA (DR-51) - carpetas 1_MOD/, 2_DOCUMENTACION/, 3_PORTAFOLIO_UTN/, _CUARENTENA_DUPLICADOS/
    Inventario de archivos: COMPLETADO (DR-45–49) - 1991 archivos, corpus A/B identificados
    Corpus A crudo: EN 1_MOD/corpus_A_crudo/ - 5 archivos data-*-batch-0000.zip de enero 2026
    Corpus B crudo: EN 2_DOCUMENTACION/05_corpus_B_crudo/ - 5 archivos documentacion claude 1-5.zip de 10-20/06
    Corpus B procesado parcial: EXISTEN claude_1_processed.json hasta claude_5_processed.json en 07_fuentes_documentacion/ - sin abrir (DR-47)
    Paper C1: CERRADO en s34, pero con S4A y S5 sin respaldo cuantitativo - pendiente de corrección
    Skill C2: NO EXISTE - pendiente de generación
    DR-54 (diseño de tabla): BLOQUEANTE - sin resolver
    Diplomatura UTN Parte 1: VENCE 2026-07-15 - requiere tabla de análisis para responder

2. OBJETIVOS FINALES DEL PROYECTO
Objetivo 1: Mod IRAM

    Producto: Código jugable v5.6 (bugs menores)
    Estado: CERRADO - no tocar en esta fase

Objetivo 2: Documentación del proceso

    Productos: (a) Paper C1 corregido, (b) Skill C2 operacional
    Estado: PENDIENTE

Objetivo 3: Análisis A/B + Diplomatura UTN

    Productos: (a) Base de hechos verificada, (b) Entregas Parte 1 y 2, (c) Portafolio GitHub
    Estado: EN DISEÑO - DR-54 bloquea

3. ARQUITECTURA DEL PROYECTO: LOS 3 NIVELES
IMPORTANTE: El mod IRAM no es el producto final. Es el vehículo para un proyecto de aprendizaje en 3 niveles.
Nivel 1 — Vehículo (el mod)

    Qué es: El mod IRAM para Imperator: Rome
    Propósito: Campo de práctica para aprender a usar IA en algo complejo y de largo plazo
    Valor: Bajo como producto (mod gratuito, sin usuarios reales)
    Destino: Descartable como producto, valioso como experiencia de aprendizaje

Nivel 2 — Habilidad técnica (la documentación)

I'm seeing the official project structure from plan.md now—there are two main objectives: the IRAM mod with playable code v5.6 marked as closed, and the process documentation with a corrected paper and operational skill guide still pending completion.

The third objective combines A/B analysis with the UTN diplomatura work, currently in design phase and blocked by DR-54. This is a critical structural difference from what charla_7 and charla_8 built in their SVG framework—they treated analysis as a separate connective stage between documentation and the portfolio, but the actual plan shows analysis and the UTN coursework are fused into a single objective, not sequential pipeline stages.

DR-52's characterization holds up: C1 and C2 are objetivo 2's products that feed into objetivo 3, which aligns with plan.md's numbering. The SVG diagram they constructed doesn't quite match this structure, which is worth flagging as a meaningful correction to their framework.

I should also check plan.md around line 360 for the "Fase 5" tasks and the "3 niveles" framework mentioned there—Nivel 1 covering the vehicle/modifications, Nivel 2 addressing technical skill and documentation, and presumably Nivel 3 dealing with analysis or meta-learning. This three-level model is distinct from the three-branch structure and might be another useful framing directly embedded in the document itself.

Mostrar menos

Ver el resto del marco de 'niveles' en plan.md (nivel 3), relevante para la reflexión de núcleo narrativo
bash

cd /home/claude && sed -n '45,70p' plan.md
Salida


    Qué es: El sistema de documentación de 5 capas (wikis ACTIVE/ARCHIVE, session logs, prompt maestro)
    Propósito: Aprender a documentar un primer proyecto real
    Valor: Alto como metodología replicable
    Destino: Parte central del portafolio y del paper

Nivel 3 — Habilidad metacognitiva (el análisis)

    Qué es: El estudio de caso de colaboración humano-IA basado en los 101 sesiones documentadas
    Propósito: Estudiar patrones de fricción y mecanismos de mitigación
    Valor: Alto como caso de estudio académico
    Destino: Trabajo de diplomatura UTN y paper

Conclusión: El valor real del proyecto está en los niveles 2 y 3, no en el nivel 1.
4. DEPENDENCIAS CRÍTICAS
DR-54 (diseño de tabla)
  ↓
Fase 1 (procesamiento de datos → tabla CSV)
  ↓
  ├──→ Fase 2 (Parte 1 UTN)
  ├──→ Fase 4 (Paper/Skill)
  └──→ Fase 3 (Parte 2 UTN)
DR-54 es el único bloqueo que impide arrancar todo lo demás.
Resuelto DR-54 → las fases 1, 2, 3 y 4 pueden ejecutarse en paralelo con supervisión.
5. FASES DE TRABAJO DETALLADAS
FASE 0 — Resolución de DR-54 (Diseño de la tabla de análisis)
Listo