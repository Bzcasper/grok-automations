# 13-brand-price-index — Brand Price Index
- **Task name:** `brand-index`
- **Schedule:** Every Friday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Brand Index

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Weekly eBay sold price index for watched costume and fine jewelry brands.
GOAL: Compute median sold price, sample size, and week-over-week trend for each watched brand.

CONFIG: Use the Notion connector to read row 'brand-index' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com
DEFAULTS - Keywords (brand list): Trifari, Monet, Sarah Coventry, Pandora, Tiffany, Gorham.
DEFAULTS - Exclusion: drop non-jewelry hits (clothing, fragrance, housewares) before computing anything.
DEFAULTS - Extra: 30-day sold window; trend bands +10 percent Up, -10 percent Down, else Flat; min sample 5.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Read existing Brand Index rows first so you have last run's Category Avg for each brand.
2. For each brand, search eBay sold listings from the last 30 days:
   ebay.com/sch/i.html?_nkw=<brand>+jewelry&LH_Sold=1&LH_Complete=1
3. Keep only real jewelry results; discard clothing, fragrance, and other non-jewelry hits.
4. Compute the median sold price (Category Avg) and the number of listings used (Sample Size).
5. Compare this run's median to the most recent existing row for that brand.
6. Trend is Up if the median rose more than 10 percent, Down if it fell more than 10 percent, otherwise Flat.
7. If Sample Size is under 5, set Trend to Flat and note the thin sample in the Run Log.
8. Record how many listings you saw before filtering as well as after, in Run Log Notes.
9. A brand whose search returns zero sold items is reported in Notes with no row written.
10. Stop after one row per brand for this run (six rows at defaults).

CONFIDENCE GATE: Only index a brand when you have at least 5 real sold comps opened this run.
- Fewer than 5 comps means skip that brand and say so in Notes; do not estimate.
- Medians must come from the listed comp URLs, never from memory.
- If eBay is unreachable, report FAILED rather than reusing last week's numbers.
- Brands that fail the sample test are noted in Notes only, never estimated into a row.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create rows in Brand Index with EXACTLY these properties:
- Brand (title)
- Category Avg (number) - median sold price in USD
- Sample Size (number)
- Trend (select Up|Flat|Down)
- Link (url) - the eBay search URL used
- Date (date) - today
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: brands skipped, thin samples, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
