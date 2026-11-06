# lot-scout — jewelry pound-lot discovery

- **Task name:** `lot-scout`
- **Schedule field:** `Every day at 8:00 AM and 6:00 PM`
  (if your Grok UI only allows one time per task, create two copies: 8:00 AM / 6:00 PM)
- **Requires:** web browsing / Agent Tools enabled

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Lot Scout — jewelry pound-lot discovery on auction sites

Scan online auction sites for jewelry LOTS (bulk pound lots, mixed jewelry
bags/tubs, estate jewelry job lots) that look undervalued. shopgoodwill.com
is EXCLUDED — it is already covered by my separate sgw-sniper task.

SITES TO SCAN (priority order):
1. shopthesalvationarmy.com — browse the "Fine Jewelry Lots" category
   (/Browse/C2407100/Fine-Jewelry-Lots)
2. hibid.com — search "jewelry lot", "mixed jewelry", "estate jewelry"
3. proxibid.com — search "bulk jewelry", "jewelry lot" (Jewelry, Gemstones
   & Watches category)
4. govdeals.com — Jewelry & Watches category, search "jewelry"
5. municibid.com — search "jewelry lot", "miscellaneous jewelry"
6. bidrl.com — search "jewelry" across regional sale pages
7. auctionninja.com — search "jewelry lot", "estate jewelry"
8. ebth.com — search "jewelry"
9. maxsold.com — search "jewelry"

PROCEDURE:
1. For each site, search for active lots matching: "jewelry", "jewelry lot",
   "mixed jewelry", "pound lot", "estate jewelry", "bag of jewelry",
   "costume jewelry lot", "fine jewelry lot". Skip single-item lots, empty
   lots, and pure wire/plastic scrap unless silver or gold content is noted.
2. Take up to 10 candidate lots per run, best-looking first. For each:
   a. Open the listing.
   b. IMAGE FILTER: view the first couple images to kill junk fast
      (hangers, wire scraps, plastic costuming). If it passes, view ALL images.
   c. In every image note: gold/silver marks, gemstones, brand names
      (Tiffany, Pandora, Monet, Trifari...), weight clues, condition.
3. CONFIDENCE GATE: continue only if you judge the lot likely contains at
   least one item worth more than current bid + shipping. Otherwise drop it.
4. EBAY SOLD COMPS: for confident lots, check eBay sold listings from the
   last 90 days:
   ebay.com/sch/i.html?_nkw=<item>&LH_Sold=1&LH_Complete=1
   Find comps for the 1-3 most valuable identifiable items in the lot.
5. SCORE 1-5: (top comps x 0.6 realistic resale haircut) - (current bid +
   buyer premium + shipping) = rough net. Score 5 = strong profit,
   3 = marginal, 1-2 = skip.

OUTPUT (always produce, even if nothing found):

## LOT SCOUT REPORT — {date}
### HIGH PRIORITY (score 4-5)
For each lot: link, site, current bid, time remaining, top finds from
images, eBay sold comp evidence (price + link), est. net profit.
### WATCH (score 3)
Same fields, one line each.
### NO ACTION
Sites scanned with nothing worth reporting; any site that blocked access
or failed.

END EVERY REPORT WITH:
"TO SAVE IN NOTION — paste HIGH PRIORITY and WATCH rows into the Lot Radar
DB under Pre-Owned Jewelry Store OS (Name, Site, Link, Bid, Est. Profit,
Score, Date Found)."

RULES:
- Never fabricate lots, bids, view counts, or comps. Cite a link for
  everything you claim.
- Discovery and reporting only — never bid or buy.
- If more than 10 lots qualify, report only the 10 highest-scoring.
```
