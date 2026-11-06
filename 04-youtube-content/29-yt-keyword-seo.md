# 29-yt-keyword-seo - YT Keyword SEO
- **Task name:** `yt-keyword-seo`
- **Schedule:** Every Wednesday at 10:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue (Status=Queued) or a "Keyword Map" page (create if missing)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Research how buyers and viewers phrase jewelry-resale searches.
GOAL: capture real
search-demand phrasing from autocomplete and related searches, then produce 5 optimized video
titles with matching tag sets for evergreen content.

CONFIG: Use the Notion connector to read row 'yt-keyword-seo' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = search surfaces, Keywords = seed terms, Extra =
title and tag rules). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com, google.com, etsy.com, ebay.com; Keywords = how to sell
jewelry, estate jewelry, jewelry flipping, shopgoodwill, whatnot jewelry, thrift jewelry,
silver jewelry value; Extra = titles 55-80 characters, main phrase in the first 5 words, 10-13
tags mixing broad and long-tail.

PROCEDURE:
1. For each config seed term, run web searches and open the search results pages to capture
   autocomplete suggestions, related searches, and People Also Ask phrasings.
2. Repeat the seed on YouTube search specifically to capture video-side phrasing.
3. Record each distinct phrase verbatim with its source URL; dedupe near-identical variants.
4. Rank phrases by how directly they match an evergreen topic I can film (sourcing, flipping,
   lot breakdowns, market pricing) and keep the top 5.
5. For each phrase write an optimized title (config title rules) and a 10-13 tag set: exact
   phrase, broad category tags, and 3 long-tail variants.
6. Prepare the output rows described below.

CONFIDENCE GATE: Only use phrases you actually saw in autocomplete or related-search output
this run. Never guess at keyword volume or search counts; if a phrase has no captured source,
drop it.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create 5 rows in Content Queue with
EXACTLY these properties: Title (title: optimized title), Status (select: Queued), Type
(select: Long), Hook (text: the target search phrase and why it is evergreen), Outline (text:
10-13 comma-separated tags plus the 5-7 talking beats the phrase implies), Reference (url:
search results page where the phrase was captured), Date (today). Every factual claim must
include its source URL. If Content Queue should stay draft-only this week, instead create the
"Keyword Map" page (create if missing) with the same five entries and their tags. Create
Content Queue with this schema if missing: Title (title), Status (select
Queued|Drafted|Scheduled|Published|Killed), Type (select Long|Short), Hook (text), Outline
(text), Reference (url), Date (date).

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (yt-keyword-seo), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of keyword entries), Notes (errors,
blocked sites, surfaces unavailable, surprises). Create it with this schema if missing: Task
(title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes
(text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
