# 03-hibid-sweep — HiBid Sweep
- **Task name:** `hibid-sweep`
- **Schedule:** Every day at 10:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Lot Radar

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Daily jewelry-lot sweep of hibid.com.
GOAL: Surface up to 10 hibid lots where 1+ item inside is worth more than the current bid plus shipping.

CONFIG: Use the Notion connector to read row 'hibid-sweep' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: hibid.com
DEFAULTS - Keywords: jewelry lot, mixed jewelry, estate jewelry, watches.
DEFAULTS - Extra: max 10 lots per run; score bands net USD >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2, <=0 skip; prefer 2+ comps (single comp caps Score at 3).
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

BROWSING LIMITS: max 3 search-result pages per site; if a site blocks or CAPTCHAs, retry once via a Google site: operator, then log and move on.

PROCEDURE:
1. Search hibid.com for each keyword (site search, or Google with site:hibid.com if site search is weak).
2. Also browse upcoming and live auction catalogs that list a Jewelry, Estate, or Coins-and-Jewelry category.
3. Keep only multi-piece lots; skip single rings, single watches, and other single-item listings.
4. Image filter, stage one: view only the FIRST 2-3 images of the lot to kill obvious junk fast. 'Plausible jewelry' = at least one of: a visible metal mark (14K/18K/925/sterling), a recognizable gemstone or brand, or multi-piece weight/quantity. Hangers, wire scraps, plastic costuming, empty bags = not plausible.
5. If none of those first 2-3 images show plausible jewelry, close the lot and move on.
6. Image filter, stage two: if stage one passed, view ALL images for the lot.
7. In the full image set, note gold or silver marks (14K, 18K, 925, sterling), visible gemstones, recognizable brands, and overall condition.
8. Pick the 1-3 items in the lot that look most valuable from those notes.
9. For each picked item, pull eBay sold comps from the last 90 days:
   ebay.com/sch/i.html?_nkw="<item>"&LH_Sold=1&LH_Complete=1
10. Record the current bid, shipping cost (incl. buyer premium if stated), and the top comp prices for the lot's best items.
11. Compute net = (top comp x 0.6) - (current bid + buyer premium + shipping). Map net to Score per config Extra bands (default >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2). A single comp caps Score at 3. If net <= 0, skip the lot (do not write). Then stop at 10 qualifying lots.

CONFIDENCE GATE: Only report a lot if 1+ item inside is worth more than the current bid plus shipping, backed by at least one sold comp URL.
- No comp, no entry. Weak lots are skipped, not padded into the run.
- Comps older than 90 days do not count; a lot with no in-window comp is skipped.
- A single comp caps Score at 3; 2+ comps are required for Score 4-5.
- Skip any lot whose images are too poor to verify at least one item.
- If net <= 0, skip the lot; do not write a row.
- If nothing qualifies, report Items 0 rather than lowering the bar.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Lot Radar with EXACTLY these properties:
- Name (title)
- Site (select) - set to HiBid for this task
- Link (url)
- Bid (number)
- Est. Profit (number)
- Score (number 1-5)
- Date Found (date)
- Status (select New|Watching|Bought|Sold|Skipped)
Every factual claim must include its source URL. New rows get Status New. Before creating, read existing Lot Radar Link values; if this lot's Link already exists, update that row's Bid and Score instead of creating a duplicate. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: errors, blocked sites, surprises). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
