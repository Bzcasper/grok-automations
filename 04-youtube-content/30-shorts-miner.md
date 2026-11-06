# 30-shorts-miner - Shorts Miner
- **Task name:** `shorts-miner`
- **Schedule:** Every day at 5:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue (Type=Short)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Turn fresh finds and niche news into short-form scripts.
GOAL: mine today's Lot Radar
finds plus niche news for 30-60 second Shorts scripts, each with a hook line, beat-by-beat
breakdown with on-screen prop suggestions, and a CTA.

CONFIG: Use the Notion connector to read row 'shorts-miner' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = news sources, Keywords = search terms, Extra =
Shorts length and CTA style). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com, ebay.com, whatnot.com; Keywords = jewelry resale news, auction
site, lot find, sold comp; Extra = 30-60 seconds, 3 Shorts per run max, CTA asks a question
to drive comments.

PROCEDURE:
1. Using the Notion connector, query Lot Radar for rows found in the last 7 days with Status
   New, Watching, or Bought, ordered by Score descending.
2. Web-search the config Keywords for niche news from the last 48 hours as a second source of
   material when finds are thin.
3. Pick up to 3 subjects: a standout find (great price or rare piece) or a timely news item.
4. For each subject verify the core fact with a source URL before writing anything about it.
5. Write the script: 1 hook line under 8 seconds, 4-6 beats with the on-screen prop for each
   (lot bag, loupe, scale, price sold screen), and a question-style CTA.
6. Prepare the Content Queue rows described below.

CONFIDENCE GATE: Only script a subject whose core fact you verified with a source this run. If
fewer than 3 subjects qualify, script only those and record the real count - never pad with
invented finds.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in Content Queue with
EXACTLY these properties: Title (title: Short title), Status (select: Queued), Type (select:
Short), Hook (text: hook line), Outline (text: beats with on-screen prop per beat plus the
CTA), Reference (url: Lot Radar Link or news source URL), Date (today). Every factual claim
must include its source URL. Create Content Queue with this schema if missing: Title (title),
Status (select Queued|Drafted|Scheduled|Published|Killed), Type (select Long|Short), Hook
(text), Outline (text), Reference (url), Date (date).

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (shorts-miner), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of Shorts queued), Notes (errors,
blocked sites, subjects skipped, surprises). Create it with this schema if missing: Task
(title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes
(text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
