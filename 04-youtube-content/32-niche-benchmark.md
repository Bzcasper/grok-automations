# 32-niche-benchmark - Niche Benchmark
- **Task name:** `niche-benchmark`
- **Schedule:** Every Sunday at 12:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** "Trend Briefs" DB (create if missing: Brief (title), Summary (text), Link
  (url), Date (date))

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Benchmark what won in the jewelry-resale niche this week.
GOAL: determine which formats
(haul, review, tutorial, sourcing trip), lengths, and hook types performed best over the last
7 days and deliver an 8-bullet brief with links.

CONFIG: Use the Notion connector to read row 'niche-benchmark' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = platforms, Keywords = search terms, Extra =
formats and channels to include). If the row or DB is missing, use the DEFAULTS below and
include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = youtube.com; Keywords = jewelry resale, estate jewelry haul, shopgoodwill
haul, pound lot jewelry, thrift jewelry flip, whatnot jewelry, selling jewelry online;
Extra = include haul, review, tutorial, sourcing trip formats; include my competitor channels
if listed.

PROCEDURE:
1. Web-search each config keyword for videos uploaded in the last 7 days; capture title,
   channel, upload date, views, and length for every candidate you open.
2. Also open the videos pages of any channels listed in config Extra and do the same for their
   uploads this week.
3. Note each video's format bucket (haul, review, tutorial, sourcing trip, other), its length
   bucket (under 5, 5-10, 10-15, over 15 minutes), and its hook type (curiosity, dollar claim,
   transformation, listicle, controversy).
4. Rank by views relative to each channel's typical size where you can observe it, otherwise by
   raw views with that caveat stated.
5. Distill the week's winners into 8 bullets: best format, best length band, best hook type,
   one standout video, one rising pattern, one underperforming pattern, one gap I can exploit,
   and one action for next week's Content Queue.
6. Prepare the brief row described below.

CONFIDENCE GATE: Only cite videos whose views, length, and upload date you read directly this
run. If too few videos load to rank formats, mark Status=PARTIAL and report only what the
evidence supports - no speculative trend claims.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create a row in the "Trend Briefs" DB
(create it with this schema if missing: Brief (title), Summary (text), Link (url), Date (date))
with EXACTLY these properties: Brief (title: weekly niche benchmark plus date), Summary (text:
the 8 bullets, each with its supporting video URL inline), Link (url: the top winner's watch
URL), Date (date: today). Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (niche-benchmark), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of videos reviewed), Notes (errors,
blocked sites, thin sample warnings, surprises). Create it with this schema if missing: Task
(title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes
(text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; only videos from the last 7 days count toward this brief.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
