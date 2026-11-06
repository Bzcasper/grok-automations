# 25-yt-content-scout - YT Content Scout
- **Task name:** `yt-content-scout`
- **Schedule:** Every day at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Scout this week's niche winners and turn them into video ideas.
GOAL: scan YouTube for
top-performing pre-owned/secondhand jewelry resale videos, then queue 3 ranked video ideas
with hooks and outlines.

CONFIG: Use the Notion connector to read row 'yt-content-scout' from the 'Grok Task Config'
DB. Use its Sites/Keywords/Extra fields (Sites = video platforms, Keywords = search terms,
Extra = format and length preferences). If the row or DB is missing, use the DEFAULTS below
and include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com; Keywords = jewelry resale, estate jewelry haul, shopgoodwill
haul, pound lot jewelry, selling jewelry online, thrift jewelry flip, whatnot jewelry; Extra =
voice is sourcing, flipping, lot breakdowns, market pricing; long videos 8-14 minutes.

PROCEDURE:
1. Web-search YouTube for each config keyword, filtered to uploads from the last 7 days.
2. Open the top result pages and record title, channel, upload date, views, and thumbnail
   subject for each candidate.
3. Pick the top 3-5 performers measured by views relative to that channel's usual size, and
   note the title and thumbnail hook pattern for each.
4. Identify content gaps: angles the winners did not cover for the same keyword.
5. Generate 3 ranked video ideas from the gaps: for each write 2 title variants, a 15-second
   hook seed, a 5-7 bullet outline, the reference videos used, format, and target length.
6. Prepare the three Content Queue rows described below.

CONFIDENCE GATE: Only use videos whose view counts and upload dates you actually read on the
watch page this run. If view counts are hidden or the page fails to load, exclude the video
and list it in Notes rather than estimating.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in Content Queue with
EXACTLY these properties: Title (title: chosen title variant), Status (select: Queued), Type
(select: Long), Hook (text: 15-second hook seed plus the winning hook pattern observed), Outline
(text: 5-7 bullets plus both title variants), Reference (url: strongest reference video URL),
Date (today). Every factual claim must include its source URL. Create Content Queue with this
schema if missing: Title (title), Status (select Queued|Drafted|Scheduled|Published|Killed),
Type (select Long|Short), Hook (text), Outline (text), Reference (url), Date (date).

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (yt-content-scout), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of ideas queued), Notes (errors,
blocked sites, videos excluded, surprises). Create it with this schema if missing: Task (title),
Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
