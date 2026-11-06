# 09-keyword-fresh-scan — Keyword Fresh Scan
- **Task name:** `keyword-fresh-scan`
- **Schedule:** Every day at 8:00 AM and 8:00 PM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Lot Radar

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Drive a fresh sourcing scan from the active rows of the Watched Keywords DB.
GOAL: Run every active watched keyword across all nine sourcing sites and write only lots not already in Lot Radar.

CONFIG: Use the Notion connector to read row 'keyword-fresh-scan' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: shopthesalvationarmy.com, hibid.com, proxibid.com, govdeals.com, municibid.com, bidrl.com, auctionninja.com, ebth.com, maxsold.com.
DEFAULTS - Exclusion: shopgoodwill.com is ALWAYS excluded; it is covered by the separate sgw-sniper task.
DEFAULTS - Keywords: read from the Watched Keywords DB (step 1); if that DB is missing use jewelry lot, mixed jewelry, estate jewelry, watches.
DEFAULTS - Extra: max 10 NEW lots per run; dedupe against existing Lot Radar links; score bands net USD >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2, <=0 skip; prefer 2+ comps (single comp caps Score at 3).
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

BROWSING LIMITS: max 3 search-result pages per site; if a site blocks or CAPTCHAs, retry once via a Google site: operator, then log and move on.

PROCEDURE:
1. Read all rows of the 'Watched Keywords' DB with properties Keyword (title), Category (select Jewelry|Brands|General), Active (checkbox), Notes (text); use only rows where Active is checked. Create the DB with this schema if missing.
2. Read every existing Link value from the Lot Radar DB; this is your dedupe set for the run.
3. For each active keyword, search each of the nine sites using site search or Google with a site: operator.
4. Image filter, stage one: view only the FIRST 2-3 images to kill obvious junk fast; close the lot if none show plausible jewelry. 'Plausible jewelry' = at least one of: a visible metal mark (14K/18K/925/sterling), a recognizable gemstone or brand, or multi-piece weight/quantity. Hangers, wire scraps, plastic costuming, empty bags = not plausible.
5. Image filter, stage two: if stage one passed, view ALL images and note gold/silver marks, gemstones, brands, condition.
6. Pick the 1-3 most valuable items and pull eBay sold comps for the last 90 days:
   ebay.com/sch/i.html?_nkw="<item>"&LH_Sold=1&LH_Complete=1
7. Qualify a lot only if 1+ item is worth more than bid + shipping, backed by a comp URL.
8. DROP any result whose Link already exists in Lot Radar; never write a duplicate row.
9. Compute net = (top comp x 0.6) - (current bid + buyer premium + shipping). Map net to Score per config Extra bands (default >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2). A single comp caps Score at 3. If net <= 0, skip the lot (do not write). Then stop at 10 NEW lots per run.

CONFIDENCE GATE: Only report a lot if 1+ item inside is worth more than the current bid plus shipping, backed by at least one sold comp URL, and only if its Link is not already in Lot Radar.
- No comp, no entry. Duplicates are dropped, not rewritten.
- Comps older than 90 days do not count; a lot with no in-window comp is skipped.
- A single comp caps Score at 3; 2+ comps are required for Score 4-5.
- Skip any lot whose images are too poor to verify at least one item.
- If net <= 0, skip the lot; do not write a row.
- If nothing new qualifies, report Items 0 rather than lowering the bar.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Lot Radar with EXACTLY these properties:
- Name (title)
- Site (select)
- Link (url)
- Bid (number)
- Est. Profit (number)
- Score (number 1-5)
- Date Found (date)
- Status (select New|Watching|Bought|Sold|Skipped)
Every factual claim must include its source URL. New rows get Status New. Dedupe on Link before writing. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: errors, blocked sites, surprises). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
