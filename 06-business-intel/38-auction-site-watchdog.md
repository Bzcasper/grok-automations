# 38-auction-site-watchdog - Auction Site Watchdog
- **Task name:** `38-auction-site-watchdog`
- **Schedule:** Every Monday at 10:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Platform News

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Watch the 9 tracked auction sites (shopthesalvationarmy, hibid, proxibid, govdeals, municibid, bidrl, auctionninja, ebth, maxsold) for NEW fees, buyer-premium changes, shipping-policy changes, and category redesigns.
GOAL: One Platform News row per confirmed new change, each with a link and a one-line impact for a small jewelry seller.

CONFIG: Use the Notion connector to read row '38-auction-site-watchdog' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: shopthesalvationarmy.com, hibid.com, proxibid.com, govdeals.com, municibid.com, bidrl.com, auctionninja.com, ebth.com, maxsold.com.
DEFAULTS - Keywords: buyer premium, buyer's premium, fees, shipping policy, pickup policy, terms update, category redesign, added fee.
DEFAULTS - Extra: watch window is the last 7 days since the previous Monday run; official terms/help pages outrank forum rumors; only NEW changes count, standing policies do not.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Build the watch list from the config Sites field; if it is empty, use the 9 default domains above.
2. For each site, open its terms, fees, shipping, and help pages and look for change notices, updated dates, or restructured category menus.
3. Run a web search per site limited to the last 7 days (examples: 'hibid buyer premium change this week', 'proxibid shipping policy update').
4. Read the previous week's Platform News rows for this task so you do not re-report last week's change as new.
5. For each candidate change, capture: what changed, effective date if stated, source URL, and whether it came from the official page or secondary coverage.
6. Open at least one live page per candidate; a search snippet alone never qualifies.
7. Classify each confirmed change: fee, buyer premium, shipping policy, or category redesign.
8. Write a one-line impact for a small jewelry seller (for example 'adds 3% to winning bids under $50', 'kills parcel shipping, pickup only').
9. Discard anything you could not open, anything older than the watch window unless it takes effect inside the window, and standing policies unchanged since last run.
10. If a site blocks access or times out, record it in Notes and continue with the remaining sites.
11. If no site is reachable at all, write no rows and set Status FAILED with the reason.
12. If every site was checked and nothing new appeared, write no rows and log Status OK with Items 0 and Notes 'no changes detected'.
13. Cap output at 10 rows so one noisy week cannot flood Platform News.

CONFIDENCE GATE: Only report a change you verified on a live, opened page dated inside the watch window (or an official page announcing an in-window effective date). Forum rumors without an official or reputable source are dropped.
If some sites were unreachable but at least one was checked, write the verified rows and set Status PARTIAL, listing blocked sites in Notes.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Platform News with EXACTLY these properties: Source (title), Change (text), Impact (text), Link (url), Date (date).
- Create one row per confirmed change, maximum 10. Date = today.
- Source (title): the auction site name (for example 'HiBid').
- Change (text): what changed, plus effective date if stated.
- Impact (text): one line on how it affects a small jewelry seller.
- Link (url): the official or reputable source URL you opened.
- Every factual claim must include its source URL.

DELIVERABLE: 0-10 Platform News rows for confirmed, new, in-window auction-site changes.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 38-auction-site-watchdog, Date = today, Items = rows written to Platform News, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
