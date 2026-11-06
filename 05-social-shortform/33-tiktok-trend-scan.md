# 33-tiktok-trend-scan - TikTok Trend Scan
- **Task name:** `33-tiktok-trend-scan`
- **Schedule:** Every day at 12:30 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Social Queue

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Scan web-visible TikTok for trending sounds and formats in jewelry resale, thrift flips, and estate sales, then map the top 3 to my niche with a post draft each.
GOAL: Up to 3 verified, current trends, each mapped to estate-jewelry resale with one ready-to-film draft, or an honest PARTIAL with fewer.

CONFIG: Use the Notion connector to read row '33-tiktok-trend-scan' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: tiktok.com discover and hashtag pages (#jewelryflip, #resellertiktok, #thriftflip, #estatejewelry, #vintagejewelry), Google results that surface TikTok pages, dated trend roundups.
DEFAULTS - Keywords: trending sounds, viral format, thrift haul, jewelry flip, estate sale finds, what I sold, small seller POV.
DEFAULTS - Extra: niche is estate and pre-owned jewelry resale; only trends visible without login; skip singing, dancing, or brand-mismatched trends; prefer trends a solo seller can film with lots on hand.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no Social Queue rows, and log Status OK with Items 0 and Notes 'disabled in config'.
FRESHNESS: All trend evidence must be dated within the last 7 days. A trend with only old sources is dropped, no matter how well known.

PROCEDURE:
1. Run fresh web searches for TikTok trends from the last 7 days using the configured keywords (examples: 'TikTok trending sounds jewelry resale this week', 'thrift flip TikTok format trending').
2. Open the configured Sites and collect every candidate sound or format with its source URL and source date.
3. Verify each candidate by actually opening at least one live page: a TikTok page or embed, or a reputable trend roundup you can date to the last 7 days.
4. Discard anything you could not open, anything without a fresh date, and anything off-niche (no clear fit for jewelry, thrifting, estate sales, or resale business content).
5. For each survivor, rate niche fit as high, medium, or low with a one-line justification.
6. Rank survivors by niche fit first and evidence freshness second; keep the top 3.
7. For each top-3 trend, write the mapped angle: why it fits estate-jewelry resale, the exact sound or format name, and what to show on camera (lot close-up, try-on, shelf restock, estate haul).
8. Draft a hook line for the first 2 seconds of each video, in my voice: direct, specific about jewelry and lots, no hype, no fake scarcity.
9. Draft one caption opener per trend that names a concrete item type (brooch, ring, chain, lot) instead of the generic word 'jewelry'.
10. Keep the source URL next to every trend and every factual claim in the draft.
11. If two candidates are variations of the same sound, keep the stronger one and note the dedupe in the run log.
12. If no trend survives the freshness filter, write no Social Queue rows and set Status PARTIAL with Notes 'no trends verified today'.
13. Note in the run log which configured site blocked access, timed out, or required login.

CONFIDENCE GATE: Only report a trend if you opened a live, dated source from the last 7 days that shows it is currently circulating. If you cannot verify currency, drop the trend.
If fewer than 3 trends pass the gate, write rows only for those that passed, set Status PARTIAL, and state the verified count in the run log notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Social Queue with EXACTLY these properties: Post (title), Platform (select TikTok|Instagram|X|Pinterest|Buffer), Copy (text), Media Note (text), Status (select Queued|Ready|Posted), Date (date).
- One row per mapped trend, maximum 3. Platform = TikTok. Status = Queued. Date = today.
- Post (title): trend name plus the niche angle, short and scannable.
- Copy (text): the post draft - hook line, caption opener, sound or format to use.
- Media Note (text): what to film, plus the source URL proving the trend is current.
- Every factual claim must include its source URL in either Copy or Media Note.
- If today's rows already exist from an earlier run today, update them instead of creating duplicates.

DELIVERABLE: 0-3 Social Queue rows containing verified, current, niche-mapped TikTok trend drafts.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 33-tiktok-trend-scan, Date = today, Items = rows written to Social Queue, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
