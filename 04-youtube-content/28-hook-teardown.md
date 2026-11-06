# 28-hook-teardown - Hook Teardown
- **Task name:** `hook-teardown`
- **Schedule:** Every day at 11:45 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** "Hook Library" DB (create if missing: Hook (title), Type (select
  Title|Open|Structure), Notes (text), Link (url), Date (date))

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Tear down the best hook in the niche from the last 24 hours.
GOAL: find the single
most-viewed jewelry-resale video published in the last 24 hours and extract its title formula,
opening structure, and retention devices into 3 transferable lessons.

CONFIG: Use the Notion connector to read row 'hook-teardown' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = platforms, Keywords = search terms, Extra =
hook devices I am allowed to study). If the row or DB is missing, use the DEFAULTS below and
include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com; Keywords = jewelry resale, estate jewelry haul, shopgoodwill
haul, pound lot jewelry, thrift jewelry flip, whatnot jewelry, selling jewelry online; Extra =
pattern interrupts, open loops, payoff previews, dollar stakes, before/after reveals.

PROCEDURE:
1. Web-search each config keyword for videos uploaded in the last 24 hours; widen to 48 hours
   only if the 24-hour pool is empty, and note the extension.
2. Collect candidates with visible view counts and open each watch page to read the exact
   view count, upload time, and description.
3. Select the single highest view count; tie-break by newest upload.
4. Watch/read closely: transcribe the title structure as a formula, outline the first 15
   seconds beat by beat, and list the retention devices used (open loop, pattern interrupt,
   payoff preview, stakes).
5. Extract 3 transferable lessons I could apply to my own sourcing/flipping videos.
6. Prepare the Hook Library rows described below.

CONFIDENCE GATE: Only tear down a video whose view count and upload time you read directly on
its watch page this run. If no video meets the window, skip writing lessons and record
Items=0 with reason in Notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in the "Hook Library" DB
(create it with this schema if missing: Hook (title), Type (select Title|Open|Structure),
Notes (text), Link (url), Date (date)) with EXACTLY these properties, one row per device:
Hook (title: the hook phrase or formula as written), Type (select: Title, Open, or Structure),
Notes (text: how it works plus the 3 transferable lessons on the Structure row), Link (url:
video watch URL), Date (date: today). Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (hook-teardown), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of Hook Library rows), Notes (errors,
blocked sites, window extensions, surprises). Create it with this schema if missing: Task
(title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes
(text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
