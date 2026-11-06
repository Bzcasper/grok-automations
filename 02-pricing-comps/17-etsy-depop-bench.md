# 17-etsy-depop-bench — Etsy Depop Bench
- **Task name:** `etsy-depop-bench`
- **Schedule:** Every Thursday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Price Reference

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Weekly Etsy and Depop asking-price benchmark for watched categories.
GOAL: Benchmark current asking prices (not sold) on Etsy and Depop and compare them against eBay sold medians.

CONFIG: Use the Notion connector to read row 'etsy-depop-bench' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: etsy.com, depop.com, ebay.com
DEFAULTS - Keywords: read active Watched Keywords rows; fallback rings, necklaces, earrings, brooches, watches.
DEFAULTS - Labeling: Etsy and Depop rows are asking prices; eBay rows are sold baselines.
DEFAULTS - Extra: sample 10 live listings per platform per category; min 5 to report; flag beyond +/-25 percent.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Read active Watched Keywords rows for the category list; fall back to the defaults if that DB is missing.
2. For each category, sample 10 live asking prices on Etsy and take the median; keep one representative URL.
3. Repeat for Depop: 10 live asking prices, median, one representative URL.
4. Pull eBay sold comps for the last 90 days for the same category and take the median sold price:
   ebay.com/sch/i.html?_nkw=<category>&LH_Sold=1&LH_Complete=1
5. Compute premium or discount per platform: (platform median - eBay sold median) / eBay sold median.
6. Flag any platform/category combo more than 25 percent above or below the eBay sold median.
7. Skip a platform/category with fewer than 5 live listings and note it in Notes.
8. Prefer distinct sellers when sampling so one seller's shelf does not skew the median.
9. Record the per-platform sample counts in Run Log Notes alongside the premium math.

CONFIDENCE GATE: Asking prices are NOT sold prices; every row must be labeled as asking.
- Need at least 5 live listings per platform per category opened this run, else skip it.
- The eBay sold baseline needs its own comp URLs; no baseline, no premium math.
- Never present an asking price as a realized sale.
- The eBay baseline must come from sold listings only, never from active ones.
- If a platform blocks access, report PARTIAL for that platform instead of guessing.

NOTION WRITE: Using the Notion connector, first check whether rows for today already exist for this task (idempotency - do not duplicate). Then create rows in Price Reference with EXACTLY these properties:
- Item (title) - "<category> ask" for Etsy/Depop rows, "<category> sold" for the eBay baseline
- Platform (select) - "Etsy", "Depop", or "eBay"
- Price (number) - the platform median in USD
- Link (url) - representative listing or the eBay search URL
- Date (date) - today
Premium or discount percentages belong in Run Log Notes, never in the Price field.
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: premiums/discounts found, combos skipped, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
