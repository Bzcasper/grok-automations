# 08-closing-soon-sniper — Closing Soon Sniper
- **Task name:** `closing-sniper`
- **Schedule:** Every 6 hours
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Lot Radar (Status=Watching) + Grok Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Cross-site sniper for jewelry lots ending within 24 hours at bids well under comp value.
GOAL: Surface up to 10 ending-soon lots where the current bid is well under eBay-comp value, sorted by hours left.

CONFIG: Use the Notion connector to read row 'closing-sniper' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: shopthesalvationarmy.com, hibid.com, proxibid.com, govdeals.com, municibid.com, bidrl.com, auctionninja.com, ebth.com, maxsold.com.
DEFAULTS - Exclusion: shopgoodwill.com is ALWAYS excluded; it is covered by the separate sgw-sniper task.
DEFAULTS - Keywords: jewelry lot, mixed jewelry, estate jewelry, watches.
DEFAULTS - Extra: window 24 hours; max 10 lots per run; well under means top-item comp value at least 2x (current bid + shipping); score bands net USD >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2, <=0 skip; prefer 2+ comps (single comp caps Score at 3).
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

BROWSING LIMITS: max 3 search-result pages per site; if a site blocks or CAPTCHAs, retry once via a Google site: operator, then log and move on.

PROCEDURE:
1. On each site, use the ending-soonest or time-remaining sort and list jewelry lots ending within 24 hours.
2. Work that list in ascending order of hours left, soonest-ending first.
3. For each candidate record the current bid, shipping cost, and exact time remaining.
4. Image filter, stage one: view only the FIRST 2-3 images to kill obvious junk fast; close the lot if none show plausible jewelry. 'Plausible jewelry' = at least one of: a visible metal mark (14K/18K/925/sterling), a recognizable gemstone or brand, or multi-piece weight/quantity. Hangers, wire scraps, plastic costuming, empty bags = not plausible.
5. Image filter, stage two: if stage one passed, view ALL images and note gold/silver marks, gemstones, brands, condition.
6. Pick the 1-3 most valuable items and pull eBay sold comps for the last 90 days:
   ebay.com/sch/i.html?_nkw="<item>"&LH_Sold=1&LH_Complete=1
7. Keep the lot only if top-item comp value is at least 2x (current bid + shipping).
8. Compute net = (top comp x 0.6) - (current bid + buyer premium + shipping). Map net to Score per config Extra bands (default >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2). A single comp caps Score at 3. If net <= 0, skip the lot (do not write).
9. Sort the final list by hours left ascending, then stop at 10 qualifying lots.

CONFIDENCE GATE: Only report a lot that ends within 24 hours AND shows top-item comp value of at least 2x (bid + shipping), each backed by a comp URL.
- No comp, no entry. Weak lots are skipped, not padded into the run.
- Comps older than 90 days do not count; a lot with no in-window comp is skipped.
- A single comp caps Score at 3; 2+ comps are required for Score 4-5.
- Skip any lot whose images are too poor to verify at least one item.
- If net <= 0, skip the lot; do not write a row.
- If nothing qualifies, report Items 0 rather than lowering the bar.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Lot Radar with EXACTLY these properties:
- Name (title)
- Site (select)
- Link (url)
- Bid (number)
- Est. Profit (number)
- Score (number 1-5)
- Date Found (date)
- Status (select Watching for every row from this task)
If a row with the same Link already exists, update that row's Bid and Score instead of creating a duplicate. Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: errors, blocked sites, surprises). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
