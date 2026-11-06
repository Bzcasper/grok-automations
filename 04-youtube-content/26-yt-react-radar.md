# 26-yt-react-radar - YT React Radar
- **Task name:** `yt-react-radar`
- **Schedule:** Every day at 1:30 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Content Queue (Type=Long)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Catch breaking niche news worth reacting to.
GOAL: find fresh news on auction sites,
eBay policy, Whatnot, or Depop relevant to jewelry resellers and draft one reaction-video idea
per story with an angle and hook.

CONFIG: Use the Notion connector to read row 'yt-react-radar' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = news sources to scan, Keywords = story terms,
Extra = angles I take). If the row or DB is missing, use the DEFAULTS below and include
'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, whatnot.com, depop.com, shopgoodwill.com, prnewswire.com; Keywords
= eBay seller policy, Whatnot update, Depop fees, auction site news, estate sale news,
jewelry market; Extra = angle is what it means for small-lot jewelry flippers.

PROCEDURE:
1. Web-search each config keyword plus the date, restricted to the last 24-48 hours.
2. Open the primary article and confirm who, what, when, and the effective date if applicable.
3. Reject speculation pieces and anything older than 48 hours; keep at most the 2 strongest
   stories so the queue is not padded.
4. For each kept story, define the reaction angle: the specific claim I would agree with,
   challenge, or clarify for a small jewelry reseller.
5. Write a hook line (first spoken sentence), 3 talking points with source URLs, and the
   target length; set format to Long.
6. Skip the run cleanly if nothing qualifies.

CONFIDENCE GATE: Only queue a story confirmed by the primary source or two dated sources. If
no story meets the bar this run, do not create any Content Queue rows - record Items=0 and
'no qualifying news' in Notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in Content Queue with
EXACTLY these properties: Title (title: reaction title with the news subject), Status (select:
Queued), Type (select: Long), Hook (text: hook line plus reaction angle), Outline (text: 3
talking points with source URLs), Reference (url: primary article URL), Date (today). Every
factual claim must include its source URL. Create Content Queue with this schema if missing:
Title (title), Status (select Queued|Drafted|Scheduled|Published|Killed), Type (select
Long|Short), Hook (text), Outline (text), Reference (url), Date (date).

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (yt-react-radar), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of stories queued), Notes (errors,
blocked sites, why nothing qualified if skipped, surprises). Create it with this schema if
missing: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items
(number), Notes (text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; news older than 48 hours is not breaking news.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
