# 16-whatnot-comps — Whatnot Comps
- **Task name:** `whatnot-comps`
- **Schedule:** Every day at 3:00 PM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Price Reference

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Whatnot jewelry auction comps pull for watched categories.
GOAL: Collect recent sold and live lot results on Whatnot for the watched jewelry categories.

CONFIG: Use the Notion connector to read row 'whatnot-comps' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: whatnot.com
DEFAULTS - Keywords: read active Watched Keywords rows with Category Jewelry; fallback jewelry lot, rings, earrings, necklaces, watches.
DEFAULTS - Labeling: every Item title ends in (sold) or (live) to match the page.
DEFAULTS - Extra: max 15 results per run; sold results and live estimates must be labeled apart.
DEFAULTS - Fallback categories apply only when the Watched Keywords DB is missing.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Read active Watched Keywords rows (Keyword, Category, Active) and use the Jewelry ones as your category list; fall back to defaults if that DB is missing.
2. Search Whatnot for each category and open the live and recently ended jewelry shows and lots.
3. Record each result's lot name, hammer or sold price when the page shows one, or the current bid if still live.
4. Label every price honestly as sold or live/estimate; never present a live bid as a hammer price.
5. Keep the exact URL of each lot or show page you opened.
6. Stop at 15 results across all categories.
7. Cross-check any price above 100 USD against a second Whatnot page before recording it.
8. Note show names and seller handles in Run Log Notes so results stay traceable.
9. Prefer recently ended lots over week-old shows when candidates exceed the cap.

CONFIDENCE GATE: Only record a price you actually saw on a Whatnot page you opened this run.
- If Whatnot blocks access or shows no prices, report FAILED with the reason and write nothing.
- Categories with no live or ended lots today are noted as zero, not filled from memory.
- No page URL, no row.
- Categories with zero results today get no row at all, just a mention in Notes.
- Never average a sold price with a live estimate.

NOTION WRITE: Using the Notion connector, first check whether rows for today already exist for this task (idempotency - do not duplicate). Then create rows in Price Reference with EXACTLY these properties:
- Item (title) - lot or category name, with " (sold)" or " (live)" suffix
- Platform (select) - set to Whatnot for every row in this task
- Price (number) - hammer, sold, or current bid in USD as seen on the page
- Link (url) - the exact Whatnot page
- Date (date) - today
Rows written count toward the 15-result cap; zero-result categories are never written.
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: categories covered, sold vs live counts, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
