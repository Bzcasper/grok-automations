# 15-retail-gap-scan — Retail Gap Scan
- **Task name:** `retail-gap`
- **Schedule:** Every Wednesday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Price Reference

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Weekly retail-vs-sold gap scan for five common jewelry categories.
GOAL: Compare live retail asking prices with typical sold-online prices and flag the biggest gaps.

CONFIG: Use the Notion connector to read row 'retail-gap' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com (sold side); retail side from config Sites such as etsy.com, 1stdibs.com, jamesallen.com.
DEFAULTS - Keywords (fixed five categories): sterling rings, gold-fill chains, costume brooches, gemstone studs, watches.
DEFAULTS - Gap formula: (retail median - sold median) / sold median.
DEFAULTS - Extra: sample 10 live listings and 10 sold comps per category; min 5 observations each side.
DEFAULTS - Callout: the top 2 categories by gap size are the biggest-gap finding.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. For each of the five fixed categories, sample 10 live retail listings and record the median asking price.
2. Keep one representative live-listing URL per category (the listing the median came from or the closest match).
3. For each category, pull eBay sold comps from the last 90 days, sample 10, and take the median sold price:
   ebay.com/sch/i.html?_nkw=<category>&LH_Sold=1&LH_Complete=1
4. Compute the gap per category: (retail median - sold median) / sold median, as a percentage.
5. Rank the five categories by gap size; the top two are the biggest-gaps callout for the Run Log.
6. Skip any category that cannot reach 5 observations on either side, and say so in Notes.
7. Record both medians in USD together with the sample counts used for each side.
8. If a retail median comes in below the sold median, re-verify both samples before reporting a negative gap.

CONFIDENCE GATE: Both sides of every gap need at least 5 real observations opened this run, each with a URL.
- Asking prices and sold prices must never be mixed in one row.
- No observations, no gap: report the category as skipped, not estimated.
- If eBay or the retail sites are unreachable, report FAILED rather than reusing old figures.
- Gaps must be computed from this run's observations, never from remembered prices.
- Two rows per category only; do not add extra rows for sub-categories.

NOTION WRITE: Using the Notion connector, first check whether rows for today already exist for this task (idempotency - do not duplicate). Then create rows in Price Reference with EXACTLY these properties:
- Item (title) - "<category> retail" or "<category> sold"
- Platform (select) - "Retail" for live listings, "eBay" for the sold baseline
- Price (number) - the category median in USD
- Link (url) - representative live listing or the eBay search URL
- Date (date) - today
Two rows per category (ten at defaults). Keep Item names identical across runs so rows stay comparable.
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: ranked gap list, categories skipped, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
