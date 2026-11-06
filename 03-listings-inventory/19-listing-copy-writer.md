# 19-listing-copy-writer - Listing Copy Writer
- **Task name:** `listing-copy`
- **Schedule:** Every day at 4:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Listing Drafts (updates)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Turn drafting jewelry listings into publish-ready copy.
GOAL: for every Listing Drafts
row with Status=Drafting, research sold comps and search-demand phrasing, then write an
optimized title, description, tag set, and comp-based price, and set Status=Ready.

CONFIG: Use the Notion connector to read row 'listing-copy' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = comp sources, Keywords = niche terms, Extra =
store niche and voice notes). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, etsy.com, worthpoint.com; Keywords = sold comps, completed
listings, jewelry resale pricing; Extra = small pre-owned/estate jewelry reseller.

PROCEDURE:
1. Using the Notion connector, query Listing Drafts for rows where Status=Drafting.
2. For each item web-search recent SOLD/completed comps on eBay and config sites matching
   brand, material, type, and size; capture 3-6 sold prices with their listing URLs.
3. Check search autocomplete and related queries for how buyers phrase this exact item.
4. Pull condition details only from the Item field; never upgrade or invent condition claims.
5. Compute the median comp; suggested price = median x 1.1, rounded to a clean .95/.99 ending.
6. Draft title, description, tags, and price for each row before touching Notion.

CONFIDENCE GATE: Only set Status=Ready when at least 3 genuine sold comps were found and the
item identity (type, material, brand if stated) is clear. If comps are thin (fewer than 3) or
identity is uncertain, leave Status=Drafting and note that row as needing human research.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then update each processed Listing Drafts row
with EXACTLY these properties: Suggested Title (text: brand, material, type, size if known,
key attribute), Description (text: 5-8 sentences, honest condition, flaws stated,
measurements, what is included), Tags (text: 10-13 comma-separated buyer search phrases),
Suggested Price (number: median comp x 1.1), Status (select: Ready), Comp Links (text: URL of
each comp used). Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (listing-copy), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of rows set Ready), Notes (errors,
blocked sites, rows left Drafting, surprises). Create the 'Grok Run Log' DB with this schema
if missing: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING),
Items (number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; never reuse remembered prices as current comps.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim. No
comp found means no price guess; leave the row in Drafting instead.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
