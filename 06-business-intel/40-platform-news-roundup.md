# 40-platform-news-roundup - Platform News Roundup
- **Task name:** `40-platform-news-roundup`
- **Schedule:** Every Thursday at 8:30 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Platform News rows + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Compile the week's seller-relevant news for Whatnot, Depop, Etsy, and Mercari, ranked by impact on a small jewelry seller.
GOAL: 0-8 linked Platform News rows plus this run's row in the Grok Run Log, covering the last 7 days across the four platforms.

CONFIG: Use the Notion connector to read row '40-platform-news-roundup' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: whatnot.com news/help, depop.com news/updates, etsy.com/news and Etsy seller handbook updates, mercari.com news/help, plus reputable seller-press blogs per platform.
DEFAULTS - Keywords: Whatnot seller update, Depop fees, Etsy seller policy, Mercari seller news, seller fees, shipping change, payout change.
DEFAULTS - Extra: window is the last 7 days; rank strictly by impact on a small jewelry seller; 1-3 items per platform, 8 rows total maximum.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.
FRESHNESS: Only items announced or effective within the last 7 days count; older stories drop even if they still seem important.

PROCEDURE:
1. For each of the four platforms (Whatnot, Depop, Etsy, Mercari), open its official news, blog, or help-updates page and list items from the last 7 days.
2. Run one web search per platform for seller news limited to the last week (examples: 'Whatnot seller update this week', 'Mercari fee change news').
3. Open each candidate source; a search snippet alone never qualifies.
4. Filter to seller-relevant items only: fees, payout rules, shipping/label changes, listing or category policy, verification requirements, ranking or reach changes, downtime.
5. Drop funding announcements, marketing campaigns, buyer-only perks, and celebrity partnerships.
6. Pool all filtered items and rank by impact on a small jewelry seller (dollar cost and operational friction first).
7. Select up to 8 items overall, aiming for coverage of every platform that had news; note platforms with zero news in the run log rather than padding.
8. Write each item: one-line Change (what happened plus date) and one-line Impact (why it matters to my shop).
9. Dedupe against Platform News rows from the last 7 days before writing; read those rows first.
10. If two sources disagree on a fact, prefer the official platform page and note the conflict in Notes.
11. If fewer than 2 of the 4 platforms were reachable, set Status FAILED with the reason; if 2-3 reachable, write what you verified and set Status PARTIAL.
12. If all four were checked and nothing new appeared, log Status OK with Items 0 and Notes 'no seller-relevant news this week'.
13. Cap output at 8 rows; overflow items go in the run log Notes only.

CONFIDENCE GATE: Every item needs an opened source dated within the last 7 days. Impact ranking must be justifiable in one sentence per item. Unverifiable or undated items are dropped.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Platform News with EXACTLY these properties: Source (title), Change (text), Impact (text), Link (url), Date (date).
- Create one row per selected item, maximum 8. Date = today.
- Source (title): the platform name (Whatnot, Depop, Etsy, or Mercari).
- Change (text): what changed, with the date it was announced or took effect.
- Impact (text): one line on the effect on a small jewelry seller, including its rank position if useful.
- Link (url): the source URL you opened.
- Every factual claim must include its source URL.

DELIVERABLE: 0-8 ranked Platform News rows plus one Grok Run Log row for this run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 40-platform-news-roundup, Date = today, Items = rows written to Platform News, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
