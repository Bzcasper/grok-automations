# 27-competitor-watch - Competitor Watch
- **Task name:** `competitor-watch`
- **Schedule:** Every day at 6:30 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** "Competitor Channels" DB (create if missing: Channel (title), Video (title),
  Views (number), Hook (text), Link (url), Date (date))

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Track new uploads from competitor jewelry-resale channels.
GOAL: log each new video from
tracked channels today - channel, title, views so far, and the hook pattern it leads with.

CONFIG: Use the Notion connector to read row 'competitor-watch' from the 'Grok Task Config'
DB. Use its Sites/Keywords/Extra fields (Sites = platforms, Keywords = channel list separated
by commas, Extra = discovery terms if the channel list is empty). If the row or DB is missing,
use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com; Keywords = empty channel list; Extra = discovery terms: jewelry
reseller, estate jewelry haul, shopgoodwill, lot flipping, jewelry sourcing.

PROCEDURE:
1. Read the config Keywords field. If it lists tracked channels, go to step 3.
2. If the channel list is empty: search the Extra discovery terms, pick 5 credible competitor
   jewelry-resale channels, log them in the Run Log Notes for human approval, and STOP - do
   not track or record their videos until a human adds them to config.
3. For each tracked channel, open its videos page and identify uploads from the last 24 hours.
4. Open each new video and record exact view count, title, thumbnail subject, and the hook
   pattern (curiosity gap, dollar claim, transformation, listicle, controversy).
5. Compare against that channel's typical view level to note whether the hook is over or under
   performing for them.
6. Prepare one Notion row per new video.

CONFIDENCE GATE: Only record videos uploaded within the last 24 hours whose view count you read
directly on the watch page. If a channel or page will not load, skip it, mark Status=PARTIAL,
and name the blocked channel in Notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in the "Competitor Channels"
DB (create it with this schema if missing: Channel (title), Video (title), Views (number),
Hook (text), Link (url), Date (date)) with EXACTLY these properties: Channel (title: channel
name), Video (title: video title), Views (number: exact current view count), Hook (text: hook
pattern plus the first-line title device), Link (url: watch URL), Date (date: today). Every
factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (competitor-watch), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of new videos recorded, 0 if discovery
only), Notes (errors, blocked channels, discovered channels awaiting approval, surprises).
Create it with this schema if missing: Task (title), Date (date), Status (select
OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
