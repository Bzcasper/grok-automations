# 11-ebay-comps-refresh — eBay Comps Refresh
- **Task name:** `comps-refresh`
- **Schedule:** Every day at 2:00 PM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Lot Radar (updates) + Grok Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Refresh eBay sold comps for strong open Lot Radar rows.
GOAL: Re-verify Score>=3 rows with Status New or Watching and update Est. Profit and Score when a value moved by more than 20 percent.

CONFIG: Use the Notion connector to read row 'comps-refresh' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com plus each row's original listing Link.
DEFAULTS - Keywords: derived from each Lot Radar row's Name and top items.
DEFAULTS - Target filter: Status New or Watching AND Score >= 3.
DEFAULTS - Extra: 90-day comp window, 20 percent move threshold, max 20 rows per run.
DEFAULTS - Skip rule: never re-score a row whose comps were already refreshed today.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

BROWSING LIMITS: max 3 search-result pages per site; if a site blocks or CAPTCHAs, retry once via a Google site: operator, then log and move on.

PROCEDURE:
1. Read Lot Radar rows matching the target filter; these and only these are the run's targets.
2. Work targets in descending Score order and cap the run at 20 rows.
3. For each target, open the row Link to confirm the listing is still live and note the current bid.
4. If the listing is gone or unreachable, leave the row unchanged and note it in the Run Log.
5. Re-identify the 1-3 most valuable items from the lot images (marks, gemstones, brands, condition).
6. Pull fresh eBay sold comps (last 90 days) for each top item:
   ebay.com/sch/i.html?_nkw="<item>"&LH_Sold=1&LH_Complete=1
7. Recompute Est. Profit = (top comp x 0.6) - (current bid + buyer premium + shipping). Recompute Score 1-5 per the same net bands as lot-scout (default >=75 → 5, 40-74 → 4, 15-39 → 3, 1-14 → 2; single comp caps Score at 3; net <= 0 leaves Score unchanged and notes it).
8. Compare new vs stored values and compute the percent move for each.
9. If Est. Profit or Score moved by more than 20 percent, UPDATE that row in place with the new numbers.
10. Rows under the threshold stay untouched but still count as checked.
11. Record old vs new values for every updated row in the Run Log Notes.
12. Skip rows already updated by an earlier run today (idempotent within the day).

CONFIDENCE GATE: Only update a row when fresh comp URLs opened this run support the new numbers.
- If comps cannot be verified, leave the row unchanged and note it.
- Comps older than 90 days do not count; never re-score from stale comps.
- No comp, no update; never re-score from memory or stale notes.
- If fewer than 1 qualifying row exists, report Items 0 rather than widening the filter.
- A row whose listing has ended is left untouched; note it in Run Log Notes and move on.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then update rows in Lot Radar with EXACTLY these properties:
- Est. Profit (number)
- Score (number 1-5)
- Bid (number, only if the live listing shows a different current bid)
Do not create new rows and do not change Status in this task.
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: rows updated, old vs new values, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
