# 35-social-queue-builder - Social Queue Builder
- **Task name:** `35-social-queue-builder`
- **Schedule:** Every day at 10:15 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + Buffer connector + web browsing / Agent Tools
- **Writes to:** Social Queue + Buffer drafts

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Read today's Content Queue rows (Status=Queued) plus the top Lot Radar find of the day, and convert them into 2-3 platform-specific post drafts (TikTok caption, IG carousel outline, X thread opener), each with a media note describing the shot or clip to attach.
GOAL: 2-3 ready-to-shoot draft rows in Social Queue, every one traceable to a real queue item or the day's top lot.

CONFIG: Use the Notion connector to read row '35-social-queue-builder' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Content Queue, Lot Radar, Social Queue DBs); web browsing only if a draft needs a source link.
DEFAULTS - Keywords: not applicable (internal read task); use row titles and hooks as the drafting context.
DEFAULTS - Extra: target platforms TikTok, Instagram, X; 2-3 drafts per run; if Content Queue has no Queued rows, draft from the Lot Radar top find alone and say so in Notes.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read Content Queue rows where Status = Queued and Date is today or earlier; take the 2 oldest as candidates.
2. Read the Lot Radar DB for today's highest-score find (fallback: most recent day) and note its lot title and source URL.
3. If there are no Queued rows and no Lot Radar rows, write no drafts and set Status PARTIAL with Notes 'nothing to draft from'.
4. Assign each candidate a platform by fit: video-first item -> TikTok caption; multi-angle or educational item -> IG carousel outline; newsy or listable item -> X thread opener.
5. TikTok caption draft: hook line, 2-4 line caption, 3-5 relevant hashtags, sound note if applicable.
6. IG carousel outline draft: slide-by-slide outline of 5-7 slides with the cover hook as slide 1.
7. X thread opener draft: first post under 280 characters plus bullets for the 2-4 follow-up points.
8. Media Note for every draft: the exact shot or clip to attach (for example 'macro of clasp hallmark', 'haul flip-through'), tied to the real item.
9. Keep every factual claim (price, lot, find) tied to its Notion row or source URL; never import facts from memory.
10. Cap output at 3 drafts; prefer 2 strong drafts over 3 weak ones.
11. Do not duplicate a Post title already sitting in Social Queue for today.
12. Write in my voice: direct, no hype, specific about jewelry and lots.
13. If a source lot is no longer active, say so in Media Note and soften urgency language in Copy.

CONFIDENCE GATE: Every draft must trace to a row you actually read this run (Content Queue or Lot Radar). Drafts without a source row are dropped.
If you skipped a candidate for missing detail, note it; set Status PARTIAL whenever fewer than 2 drafts were written.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Social Queue with EXACTLY these properties: Post (title), Platform (select TikTok|Instagram|X|Pinterest|Buffer), Copy (text), Media Note (text), Status (select Queued|Ready|Posted), Date (date).
- Create one row per draft, 2-3 rows total. Status = Queued. Date = today.
- Post (title): source item title plus platform suffix.
- Copy (text): the platform-specific draft written this run.
- Media Note (text): shot/clip instructions plus the source row URL.
- Platform (select): the platform assigned in the procedure.
- Every factual claim must include its source URL (a Notion row URL is acceptable).

BUFFER STEP: After the Social Queue rows exist, also create one matching DRAFT post per row in Buffer via the Buffer connector, on the row's Platform channel, with Copy as the caption, left UNQUEUED - NEVER publish or auto-schedule to a live slot. If the Buffer connector is unavailable or no channels are linked in Buffer, skip this step and add 'Buffer drafts not created' to Notes; do not fail the run.

DELIVERABLE: 2-3 Social Queue draft rows with copy and media notes (each linked to its source row), plus matching Buffer drafts where the connector allows.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 35-social-queue-builder, Date = today, Items = rows written to Social Queue, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
