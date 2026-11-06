# 21-stale-inventory-flagger - Stale Inventory Flagger
- **Task name:** `stale-flagger`
- **Schedule:** Every Monday at 8:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Listing Drafts (Suggested Price update) + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Flag aging inventory and recommend a fix.
GOAL: for every Listing Drafts row with
Status=Listed that is older than 45 days, research current comps and propose a markdown price
plus a relist-or-bundle recommendation.

CONFIG: Use the Notion connector to read row 'stale-flagger' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = comp sources, Extra = markdown rules such as
percent off, floor price). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, etsy.com, worthpoint.com; Keywords = sold comps, completed
listings, stale listing markdown; Extra = markdown 15 percent first, floor at cost plus
shipping, bundle items under 10 dollar value.

PROCEDURE:
1. Using the Notion connector, query Listing Drafts for rows with Status=Listed.
2. Determine age from the row's listed/created date; keep only rows older than 45 days.
3. For each stale row, web-search recent sold comps on config sites for the same item to see
   whether the market moved or the listing itself is the problem.
4. Compare the current Suggested Price to the median comp; compute a markdown (per config
   Extra rules) that stays above the floor.
5. Decide the recommendation: RELIST (refresh title/photos), MARKDOWN (price is the issue),
   or BUNDLE (low-value item to pair with another), based on comp evidence.
6. Prepare the Notion updates below with the reasoning tied to comp URLs.

CONFIDENCE GATE: Only propose a markdown when at least 2 current sold comps support it. If
comps are missing or the item age cannot be confirmed, do not change the price; report the
row in Notes as unverified instead.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then update each stale Listing Drafts row with
EXACTLY these properties: Suggested Price (number: new markdown price per config rules),
Description (text: append one line - STALE REVIEW date, days listed, median comp, the
recommendation RELIST/MARKDOWN/BUNDLE, and comp URL). Leave Status unchanged at Listed. Every
factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (stale-flagger), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of stale rows reviewed), Notes (errors,
blocked sites, rows skipped, surprises). Create the 'Grok Run Log' DB with this schema if
missing: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items
(number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; stale-review notes must carry the date they were written.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
