# 31-series-builder - Series Builder
- **Task name:** `series-builder`
- **Schedule:** Every Sunday at 10:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue (updates)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Organize queued videos into a coherent series.
GOAL: read queued Content Queue rows and
pick a 4-episode series (for example a pound-lot challenge arc) with episode order, titles,
and inter-video CTAs, then mark those rows Scheduled.

CONFIG: Use the Notion connector to read row 'series-builder' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Keywords = themes I want to build series around, Extra =
series rules such as length and episode spacing). If the row or DB is missing, use the
DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS: Keywords = pound lot challenge, estate lot breakdown, sourcing trip, sold comp
pricing; Extra = 4 episodes, one per week, long videos, cliffhanger CTA between episodes.

PROCEDURE:
1. Using the Notion connector, query Content Queue for rows with Status=Queued, Type=Long.
2. If fewer than 4 queued rows exist, do not force a series: leave statuses unchanged, set
   Items=0, and note the shortfall in the Run Log.
3. Group candidates by theme (lot challenge, sourcing trip, market pricing, haul review) and
   choose the strongest group of exactly 4 that tells a progressing story.
4. Order the episodes so each one raises stakes: setup, first results, complication, payoff.
5. Write an inter-video CTA for each episode pointing at the next one, plus a series title and
   per-episode titles.
6. Prepare the four Content Queue updates described below.

CONFIDENCE GATE: Only schedule a series built entirely from existing Queued rows you read this
run. Never invent an episode to fill a slot; if the group is short, report the shortfall and
leave the remaining rows Queued.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then update the 4 selected Content Queue rows
with EXACTLY these properties: Title (title: series-titled episode title), Status (select:
Scheduled), Hook (text: keep existing hook plus series title and episode number), Outline
(text: keep existing outline plus episode order rationale and the inter-video CTA), Date (date:
its scheduled weekly release date starting next week). Leave Type, Reference, and all
non-selected rows untouched. Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (series-builder), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of rows scheduled), Notes (errors,
shortfalls, rows left Queued, surprises). Create it with this schema if missing: Task (title),
Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; re-read the queue rather than trusting a prior run's list.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
