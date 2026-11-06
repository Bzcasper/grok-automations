# 39-ebay-policy-watch - eBay Policy Watch
- **Task name:** `39-ebay-policy-watch`
- **Schedule:** Every day at 8:30 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Platform News (Source="eBay")

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Run an eBay seller-policy, fee, and news scan; report only changes that affect small jewelry sellers; hard cap of 3 bullets per run.
GOAL: 0-3 tight, linked Platform News rows (Source = 'eBay') covering material seller-affecting changes.

CONFIG: Use the Notion connector to read row '39-ebay-policy-watch' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com announcement board, ebayinc.com news, ebay seller center policy pages, reputable eBay seller blogs.
DEFAULTS - Keywords: eBay fee change, eBay seller update, promoted listings change, eBay policy change, authenticity guarantee, jewelry category change.
DEFAULTS - Extra: window is the last 24-72 hours; only material changes for a small jewelry seller count; Source must be exactly 'eBay' in Notion; 3-bullet max.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Open the eBay announcement board and seller-center policy pages and list posts from the last 24-72 hours.
2. Search the web for fresh eBay seller news limited to the last 3 days (examples: 'eBay fee change announcement', 'eBay seller policy update this week').
3. Open each candidate article or announcement; a headline alone never qualifies.
4. Filter hard to changes that materially touch a small jewelry seller: final-value or promoted-listing fees, payment holds, shipping-label pricing, jewelry category requirements, authentication-gateway changes, search-ranking rule changes.
5. Drop buyer-only features, corporate PR, international-only changes, and enterprise programs with no small-seller effect.
6. Rank remaining items by dollar or operational impact on my shop; keep the top 3.
7. Write each as one bullet: what changed, when it takes effect, and the concrete effect on a small jewelry seller (one sentence each).
8. Attach the source URL to every bullet; prefer eBay's own announcement over blogs.
9. Dedupe: skip anything already in Platform News with Source 'eBay' in the last 7 days; read those rows first.
10. If nothing material appeared in the window, write no rows and log Status OK with Items 0 and Notes 'no material changes in window'.
11. If all sources were unreachable, write no rows and set Status FAILED with the reason.
12. Never speculate about future policy; report only what announcements actually say.
13. Cap output at 3 rows even if more candidates surface; note overflow items in the run log only.

CONFIDENCE GATE: Each bullet needs an opened source dated inside the window; eBay-official pages are strongly preferred over blogs. Undated or unopenable items are dropped.
If 1-2 bullets qualify, write them and set Status OK; reserve PARTIAL for runs where a source failure cut the search short.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Platform News with EXACTLY these properties: Source (title), Change (text), Impact (text), Link (url), Date (date).
- Create one row per bullet, maximum 3. Date = today.
- Source (title): eBay (exactly).
- Change (text): the single bullet - what changed and the effective date.
- Impact (text): one sentence on the effect on a small jewelry seller.
- Link (url): the source URL you opened.
- Every factual claim must include its source URL.

DELIVERABLE: 0-3 Platform News rows (Source='eBay') of material, linked seller-policy changes.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 39-ebay-policy-watch, Date = today, Items = rows written to Platform News, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
