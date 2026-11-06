# 45-lot-radar-review - Lot Radar Review
- **Task name:** `45-lot-radar-review`
- **Schedule:** Every Sunday at 8:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Weekly Report page section + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Run the weekly Lot Radar close-out: rows added, rows scored, won vs lost vs missed; distill 5 lessons and propose Score-calibration tweaks for human review.
GOAL: A dated 'Lot Radar Review' section in this week's Weekly Report page plus this run's row in the Grok Run Log.

CONFIG: Use the Notion connector to read row '45-lot-radar-review' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Lot Radar DB, Grok Run Log); no web browsing required except to spot-check a lot URL.
DEFAULTS - Keywords: n/a (internal synthesis task); window is Monday 00:00 through today.
DEFAULTS - Extra: 5 lessons hard cap; Score-calibration tweaks are proposals only (human applies them); destination is the 'Week of YYYY-MM-DD' Weekly Report page section 'Lot Radar Review'.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read all Lot Radar rows created or updated in the last 7 days.
2. Tally the counts: rows added, rows scored (with the score distribution: how many high/mid/low), rows marked won, rows marked lost, rows missed (expired or watched but never acted on).
3. For won and lost rows, note the auction site, price band, and category where those fields exist; leave blanks blank.
4. If any lot outcome looks wrong or stale, spot-check its listing URL; note discrepancies instead of trusting the row.
5. Identify patterns: which sites or categories produced wins, which produced misses, where scores disagreed with outcomes.
6. Write exactly 5 lessons, each traceable to specific row IDs, row titles, or URLs from this week's read.
7. Propose 2-3 Score-calibration tweaks grounded in the data (for example 'raise weight on lots under $10', 'penalize auction houses with 3+ recent misses').
8. Label every tweak 'PROPOSED - HUMAN APPROVAL REQUIRED'; never edit scoring rules or config yourself.
9. If the Lot Radar DB is empty for the week, write the section with zeros and set Status OK with Notes 'no rows this week' (unless the DB itself was unreachable).
10. If the Lot Radar DB was unreachable, write nothing and set Status FAILED with the reason.
11. Keep the whole section to one page: counts table, 5 lessons, 2-3 tweaks.
12. Include raw counts as numbers you computed, never rounded estimates.
13. Log anything surprising (a big win, a missed high-scorer) in the run log Notes.

CONFIDENCE GATE: Every tally and lesson must come from rows you actually read this run, with row references or URLs. No remembered numbers from prior weeks; re-read instead of recalling.
- If fewer than 3 source rows exist this week, set Status PARTIAL and skip the proposed tweaks.
If fewer than 5 lessons are supported by real rows, write the supported lessons and set Status PARTIAL with the shortfall in Notes.

NOTION WRITE: Using the Notion connector, first check whether this week's section already exists (idempotency - do not duplicate). Then find or create the Weekly Report page titled 'Week of YYYY-MM-DD' (create if missing, using today's date) and add/update a section 'Lot Radar Review' containing: the counts tally (added/scored/won/lost/missed), the 5 lessons, and the 2-3 proposed Score-calibration tweaks each marked 'PROPOSED - HUMAN APPROVAL REQUIRED'. Every factual claim must include its source URL or row reference.
- Destination: this week's 'Week of YYYY-MM-DD' Weekly Report page (create if missing), section 'Lot Radar Review'.
- Section contents in order: counts tally (added / scored / won / lost / missed), the 5 lessons, then the proposed tweaks.
- Tweak format: the proposed rule change plus the data point that motivated it, each labeled 'PROPOSED - HUMAN APPROVAL REQUIRED'.
- Every lesson and tally must carry its row reference or URL.
- Update-in-place: if this week's section already exists, edit it instead of appending a duplicate.
- Do not touch other sections on the same page (for example Ops Report).

DELIVERABLE: One 'Lot Radar Review' section (tally + 5 lessons + proposed tweaks) in the Weekly Report page.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 45-lot-radar-review, Date = today, Items = Lot Radar rows reviewed, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
