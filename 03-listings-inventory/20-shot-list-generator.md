# 20-shot-list-generator - Shot List Generator
- **Task name:** `shot-list`
- **Schedule:** Every day at 9:15 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Listing Drafts rows (Status=Needs Photos) if missing

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Build a per-item photo shot list for inventory that is bought or waiting on photos.
GOAL: every ready-to-shoot jewelry item has a clear, complete checklist of the shots needed
before it can move to drafting.

CONFIG: Use the Notion connector to read row 'shot-list' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Extra = camera/props notes, Sites = example listings to
benchmark photo counts). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, etsy.com; Keywords = jewelry listing photos, white background
jewelry photography; Extra = smartphone camera, white poster board, ruler, loupe.

PROCEDURE:
1. Using the Notion connector, query Lot Radar for rows with Status=Bought.
2. Also query Listing Drafts for rows with Status=Needs Photos to catch items added directly.
3. For each item, confirm identifying details (metal, stones, hallmarks, dimensions) from the
   row fields; web-search a comparable listing only if the item type is ambiguous.
4. Note any damage or missing parts recorded in the row so damage shots are included.
5. Produce the five required shot types per item: hero on white background, hallmark and
   stamp close-up, size or scale reference (ruler/coin/on-hand), damage and wear shots if any,
   and one styling shot showing real-world wear context.
6. Count items and prepare the Notion updates listed below.

CONFIDENCE GATE: Only generate a shot list when the item identity is clear from the row data.
If an item is unidentifiable, skip it, leave its status unchanged, and list it in Notes as
needing human identification rather than guessing what photos to take.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then for each identified item, create the
missing Listing Drafts row if none exists with EXACTLY these properties: SKU (title: existing
SKU or generated item code), Item (text: item description copied from Lot Radar), Status
(select: Needs Photos), Suggested Title (text: left blank or provisional), Description (text:
shot list checklist, one shot type per line), Tags (text: blank), Suggested Price (number:
blank), Comp Links (text: blank). For rows already in Needs Photos, append the shot list to
the Description field. Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (shot-list), Date (today), Status
(OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of shot lists produced), Notes (errors,
blocked sites, skipped items, surprises). Create the 'Grok Run Log' DB with this schema if
missing: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items
(number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.
Describe only what the row data actually shows about the item.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
