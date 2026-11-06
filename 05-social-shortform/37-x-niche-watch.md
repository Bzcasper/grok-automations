# 37-x-niche-watch - X Niche Watch
- **Task name:** `37-x-niche-watch`
- **Schedule:** Every day at 7:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Platform News

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Digest today's X/Twitter chatter from resale and jewelry accounts - policy news, platform outages, and big solds - capped at 5 items, each with a link and a one-line note on why it matters.
GOAL: At most 5 fresh, linked Platform News rows capturing seller-relevant X chatter from the last 24 hours.

CONFIG: Use the Notion connector to read row '37-x-niche-watch' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: x.com and twitter.com public pages, Google site:x.com searches, resale news roundups quoting X threads, reachable mirror or archive pages.
DEFAULTS - Keywords: reseller Twitter, jewelry seller account, platform outage, fee change, big sold, Whatnot Depop eBay seller news.
DEFAULTS - Extra: max 5 items; categories limited to policy news, outages or bugs, and notable big solds; window is today or last 24 hours; impact line must address a small jewelry seller.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Run site-restricted web searches (site:x.com plus the configured keywords) for today's resale and jewelry discussion.
2. Open the configured Sites and each candidate post or reputable article covering it.
3. Verify each item is from today or the last 24 hours; discard older chatter unless the breaking itself is dated today.
4. Classify each item: policy news, platform outage, or big sold highlight.
5. Keep at most 5 items; rank by impact on a small jewelry seller, not by engagement.
6. For each kept item write a one-line summary, a why-it-matters impact line, and the link.
7. Big sold items must quote the item description and price exactly as the source states them; never guess numbers.
8. Policy items must link to the official post or a reputable report - not a screenshot you could not open.
9. If X itself blocks access, fall back to secondary coverage and mark the item 'secondary source' in the impact line.
10. Skip gossip, unverified screenshots, and account drama with no seller impact.
11. Dedupe against Platform News rows already created today for this task.
12. If nothing qualifies but sources were reachable, write no rows and log Status OK with Items 0 and Notes 'no qualifying chatter today'.
13. Note every blocked or login-walled URL in the run log.

CONFIDENCE GATE: Each item needs a live link you opened plus a timestamp inside the window. Impact lines must describe seller effect, never engagement numbers you did not read.
If fewer than 5 items qualify, report the verified set and set Status PARTIAL only when a source failure limited the search; otherwise Status OK.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Platform News with EXACTLY these properties: Source (title), Change (text), Impact (text), Link (url), Date (date).
- Create one row per item, maximum 5. Date = today.
- Source (title): 'X: <topic or account>' .
- Change (text): the one-line summary of what happened.
- Impact (text): why it matters for my jewelry resale business.
- Link (url): the post or article URL you opened.
- Every factual claim must include its source URL.

DELIVERABLE: 0-5 Platform News rows of fresh, linked, seller-relevant X chatter.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 37-x-niche-watch, Date = today, Items = rows written to Platform News, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
