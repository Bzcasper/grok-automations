# 46-queue-prune - Queue Prune
- **Task name:** `46-queue-prune`
- **Schedule:** Every Saturday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue (updates) + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Clean up the Content Queue: ideas queued more than 14 days go to Killed with a reason; strong fits move to Status=Drafted with an assigned week; report the counts.
GOAL: Updated Content Queue statuses plus a run log row reporting killed / promoted / remaining counts.

CONFIG: Use the Notion connector to read row '46-queue-prune' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Content Queue DB); no web browsing required.
DEFAULTS - Keywords: n/a (internal hygiene task); stale threshold = 14 days from the Date field.
DEFAULTS - Extra: promote at most 5 rows per run to Drafted; strong fit = complete Hook + Outline + niche relevance to estate/pre-owned jewelry; never touch rows already Published or Scheduled.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, make no edits, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read all Content Queue rows with Status = Queued.
2. For each row, compute age = today minus its Date field; rows with no Date are treated as unknown-age and must not be killed (flag them in Notes instead).
3. Rows older than 14 days: set Status = Killed and append to Outline the reason 'Killed YYYY-MM-DD: queued >14 days without drafting' (append, never wipe existing Outline text).
4. Rows 14 days old or younger: assess strength (Hook present, Outline present, fits estate/pre-owned jewelry niche, not a duplicate of a recent draft).
5. Select up to 5 strongest rows; set Status = Drafted and append 'Assigned week of YYYY-MM-DD' (next Monday's date) to Outline.
6. Leave every other row untouched in Queued.
7. Never edit rows whose Status is Drafted, Scheduled, Published, or Killed; read-only for those.
8. Keep all other fields (Title, Type, Hook, Reference) unchanged in every edit.
9. Count the changes: killed count, promoted count, remaining queued count.
10. If no Queued rows exist, make no edits and log Status OK with Items 0 and Notes 'queue empty'.
11. If the Content Queue DB is unreachable, make no edits and set Status FAILED with the reason.
12. If the DB read but writes failed, set Status PARTIAL and list the failed row IDs in Notes.
13. Dedupe: if today's run already pruned (an existing run-log row for today), update that instead of re-editing.

CONFIDENCE GATE: Only edit rows you actually read this run. Never guess a row's age or content; no Date means no kill. Edits must be limited to Status and Outline appends.
If more than half of the queued rows lack a Date field, stop editing, set Status PARTIAL, and put 'missing Date fields' in Notes so the human can fix the data first.

NOTION WRITE: Using the Notion connector, first check whether this task already ran today (idempotency - do not duplicate edits). Then apply the Status and Outline updates to Content Queue as described: EXACTLY these properties may change: Status (select Queued|Drafted|Scheduled|Published|Killed) and Outline (text, append-only reason or assignment line). Report counts, not row dumps.
- Properties allowed to change: Status (select Queued|Drafted|Scheduled|Published|Killed) and Outline (append-only text).
- Kill reason appended to Outline: 'Killed YYYY-MM-DD: queued >14 days without drafting'.
- Promotion line appended to Outline: 'Assigned week of YYYY-MM-DD' (the next Monday).
- Title, Type, Hook, Reference, and Date must remain unchanged in every edit.
- Re-check each row's current Status immediately before writing; skip rows edited since your read.
- Report counts (killed / promoted / remaining), not row dumps, in the run log.

DELIVERABLE: Content Queue status updates (killed stale, promoted strong fits) plus the counts for the run log.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 46-queue-prune, Date = today, Items = rows edited, Notes = killed N / promoted N / remaining N plus errors or surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
