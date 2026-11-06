# 22-crosslist-coverage - Crosslist Coverage
- **Task name:** `crosslist-coverage`
- **Schedule:** Every Tuesday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Run Log + a "Coverage Gaps" section page (create it
  if missing)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Map where my active inventory is missing from sales platforms.
GOAL: compare Listing
Drafts active items against eBay, Etsy, Whatnot, Depop, and Mercari and output a gap table of
items not present on each platform.

CONFIG: Use the Notion connector to read row 'crosslist-coverage' from the 'Grok Task Config'
DB. Use its Sites/Keywords/Extra fields (Sites = platforms to audit, Keywords = my store name
and SKU patterns used to find my own listings, Extra = which platforms are considered
required). If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in
the run log.
DEFAULTS: Sites = ebay.com, etsy.com, whatnot.com, depop.com, mercari.com; Keywords = store
name, SKU prefix, item titles; Extra = eBay and Etsy required, others optional.

PROCEDURE:
1. Using the Notion connector, query Listing Drafts for active rows (Status=Listed or Ready).
2. Build the audit list: SKU plus Suggested Title for each active item.
3. For each platform in config Sites, web-search that site for my store name and SKU, and for
   the item title, to find whether a live listing for the item exists there.
4. Record found/not-found per item per platform, with the URL of any listing found.
5. Assemble a gap table: one row per item, columns = each platform, cell = listed URL or GAP.
6. Rank gaps: required platforms first, then by item Score or price.

CONFIDENCE GATE: Only mark an item as present on a platform when a live listing URL was
actually opened and matches the item. If a platform blocks search or cannot be verified, mark
that cell UNVERIFIED rather than listed or gap.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then find or create the "Coverage Gaps"
section page and add today's dated section containing the gap table in EXACTLY this shape:
Date (heading), then one line per item: SKU - item title - platform status (URL or GAP or
UNVERIFIED) for every platform audited. Every factual claim must include its source URL. Do
not modify Listing Drafts rows.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (crosslist-coverage), Date
(today), Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of items audited), Notes
(errors, blocked platforms, unverified cells, surprises). Create either DB if missing: 'Grok
Run Log' (Task title, Date date, Status select OK|PARTIAL|FAILED|CONFIG MISSING, Items number,
Notes text) or the "Coverage Gaps" page.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; an audit older than 7 days must be re-run, not reused.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
