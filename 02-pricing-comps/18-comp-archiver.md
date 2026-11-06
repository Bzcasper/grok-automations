# 18-comp-archiver — Comp Archiver
- **Task name:** `comp-archiver`
- **Schedule:** Every Sunday at 6:00 PM
- **Requires:** Notion connector (grok.com/connectors → Notion) + Google Drive connector + web browsing / Agent Tools
- **Writes to:** Comp Archive page + Drive CSV export + Grok Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Weekly comp evidence archiver for recently updated Lot Radar rows.
GOAL: Collect the comp evidence URLs for lots touched this week into one Comp Archive page with a section per lot.

CONFIG: Use the Notion connector to read row 'comp-archiver' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com plus each row's original listing Link.
DEFAULTS - Keywords: derived from each Lot Radar row's Name and top items.
DEFAULTS - Extra: lookback 7 days; one archive section per qualifying row; archive page title "Comp Archive".
DEFAULTS - Section fields: Name, Link, Bid, Score, every comp URL, date collected.
DEFAULTS - Heading format: "Week of <date>" once per weekly run.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Read Lot Radar rows from the last 7 days by Date Found, plus any rows updated by this week's comps-refresh runs.
2. For each target row, open the lot Link and re-pull the eBay sold comps (last 90 days) for its top items:
   ebay.com/sch/i.html?_nkw=<item>&LH_Sold=1&LH_Complete=1
3. In Notion, find the page titled "Comp Archive"; create it if it does not exist.
4. Add a dated heading for this week's run if it is not already present (idempotency - do not duplicate a heading).
5. Under it, add one section per lot: lot name, lot Link, current bid, Score, every comp URL used, and the date collected.
6. If a section for a lot already exists under this week's heading, update it in place instead of adding a second one.
7. Lots with no verifiable comps get a "no comps found" note instead of numbers.
8. Stop after one section per qualifying row; do not re-archive older weeks.
9. Cite this week's comp URLs, not numbers copied from earlier rows or notes.
10. If a lot's listing has ended, still archive its comps and mark the lot link as ended.
11. Order sections by Date Found, newest first, under the dated heading.
12. Cap at 30 sections per run; note any leftovers for next Sunday.

CONFIDENCE GATE: Only archive comp URLs you actually opened during this run.
- No invented numbers in the archive: no comps found is an acceptable and expected entry.
- Rows outside the 7-day window are not archived this run.
- One section per lot; sections without a comp URL say "no comps found" plainly.
- Old weeks are never edited retroactively; only the current heading changes.
- Comp URLs must be opened during this run; old notes and screenshots do not count.
- If Notion or eBay is unreachable, report FAILED rather than copying stale evidence.

NOTION WRITE: Using the Notion connector, this task writes a PAGE titled "Comp Archive" (create the page if missing), not a database row. First check whether this week's dated heading already exists (idempotency - do not duplicate). Each section must include Name, Link, Bid, Score, and every comp source URL for that lot.
If several pages share the title, pick the most recently edited one. Never collapse two lots into one section.
Every factual claim must include its source URL.

EXPORT STEP: After the archive sections are written, use the Google Drive connector to upload a CSV named 'comp-archive-YYYY-MM-DD.csv' into a 'Grok Exports' folder in Drive (create the folder if missing), one row per archived lot: lot name, lot link, bid, score, comp URL, date collected. If Drive is unavailable, add 'CSV export skipped' to Notes; do not fail the run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: sections archived, rows skipped, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
