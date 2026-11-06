# 48-site-scorecard - Site Scorecard
- **Task name:** `48-site-scorecard`
- **Schedule:** First Sunday of the month at 11:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + Google Drive connector + web browsing / Agent Tools
- **Writes to:** "Site Scorecard" page (create if missing) + Drive CSV export + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Monthly per-auction-site scorecard: lots found, lots bought, profit per tracked site; recommend add/keep/demote in config, with HUMAN APPROVAL required before any config change.
GOAL: A dated 'Site Scorecard' page listing each tracked site's numbers and a clearly approval-gated recommendation.

CONFIG: Use the Notion connector to read row '48-site-scorecard' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: shopthesalvationarmy, hibid, proxibid, govdeals, municibid, bidrl, auctionninja, ebth, maxsold.
DEFAULTS - Keywords: n/a (internal synthesis task); window is the last 30 days.
DEFAULTS - Extra: profit comes only from Lot Radar won/loss fields actually present; recommendations are advisory; never edit Grok Task Config automatically; destination is the 'Site Scorecard' page (create if missing).
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Build the tracked-site list from config Sites; if empty, use the 9 default sites above and note CONFIG MISSING.
2. Using the Notion connector, read all Lot Radar rows from the last 30 days.
3. Group rows by auction site; for each site tally: lots found (rows observed), lots bought (rows marked won/bought), lots missed or passed.
4. Sum profit only from rows that record a profit or sale-price-minus-cost field; sites with no such data get 'profit not tracked' - never estimate.
5. Note per-site failure signals from the week's run log: blocked domains, captcha walls, zero-yield scans.
6. For each site write a one-line performance summary with the underlying numbers.
7. Recommend one of: ADD (new or underused site with promise), KEEP (steady yield), DEMOTE (persistent failures or no yield in 30 days).
8. For DEMOTE recommendations, cite the specific evidence (missed scans, zero buys, blocked pages).
9. For ADD recommendations, name the candidate site and the one search that surfaced it; discovery only.
10. Mark every recommendation 'HUMAN APPROVAL REQUIRED - no config change applied' - never edit Grok Task Config in this run.
11. If Lot Radar was unreachable, set Status FAILED with the reason and write nothing.
12. If only partial site data was readable, write what you verified and set Status PARTIAL.
13. Keep the page scannable: one table-like block per site plus a recommendation list.

CONFIDENCE GATE: Every number must be computed from rows read this run. No invented profit, no guessed buy counts. Recommendations must cite evidence from this month's data only.
If fewer than 3 of the 9 tracked sites had readable 30-day data, set Status PARTIAL and list the unreadable sites in Notes before any recommendation is acted on.

NOTION WRITE: Using the Notion connector, first check whether this month's scorecard already exists (idempotency - do not duplicate). Then find or create the 'Site Scorecard' page (create if missing) and add a dated section 'Scorecard YYYY-MM-DD' containing one block per tracked site (lots found, lots bought, profit or 'profit not tracked', failure signals, one-line summary) plus the recommendations list, every recommendation marked 'HUMAN APPROVAL REQUIRED'. Every factual claim must include its source URL or row reference.
- Destination: the 'Site Scorecard' page (create if missing), dated section 'Scorecard YYYY-MM-DD'.
- Per-site block: lots found, lots bought, profit or 'profit not tracked', failure signals, one-line summary.
- Recommendation line: ADD / KEEP / DEMOTE plus its evidence, each labeled 'HUMAN APPROVAL REQUIRED'.
- Profit comes only from rows with real profit fields; missing data is written as 'profit not tracked', never estimated.
- Update-in-place: if this month's scorecard already exists, edit it instead of appending a duplicate.
- No config writes: Grok Task Config stays untouched; the human applies approved recommendations.

DELIVERABLE: One dated 'Scorecard YYYY-MM-DD' section with per-site numbers and approval-gated add/keep/demote recommendations.

EXPORT STEP: After the scorecard section is written, use the Google Drive connector to upload a CSV named 'site-scorecard-YYYY-MM-DD.csv' into a 'Grok Exports' folder in Drive (create the folder if missing), with one row per site: site, lots_found, lots_bought, profit_or_not_tracked, recommendation. If Drive is unavailable, add 'CSV export skipped' to Notes; do not fail the run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 48-site-scorecard, Date = today, Items = sites scored, Notes = errors, blocked sites, surprises, approval flags pending.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
