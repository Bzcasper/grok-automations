# 36-pinterest-pin-plan - Pinterest Pin Plan
- **Task name:** `36-pinterest-pin-plan`
- **Schedule:** Every Tuesday at 11:15 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Social Queue (Platform=Pinterest)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: From active Listing Drafts and Lot Radar finds, generate 5 Pinterest pin ideas (board, keyword-stuffed title, description, image direction) - Pinterest drives estate-jewelry search traffic.
GOAL: 5 production-ready pin drafts queued in Social Queue with Platform=Pinterest, each mapped to a real listing or lot.

CONFIG: Use the Notion connector to read row '36-pinterest-pin-plan' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion (Listing Drafts, Lot Radar, Social Queue) plus pinterest.com search suggestions for keyword checks when reachable.
DEFAULTS - Keywords: estate jewelry, vintage brooch, retro necklace, signed costume jewelry, antique ring, jewelry lot, art deco brooch.
DEFAULTS - Extra: 5 pins per run; every pin needs board, keyword-first title (~100 chars max), 2-3 sentence description, and image direction; prefer evergreen search intent over trends.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Read active Listing Drafts from Notion and select up to 3 items with the strongest search appeal (distinct style, era, or hallmark).
2. Read Lot Radar top finds from this week and select up to 2 more items or themes worth pinning.
3. If fewer than 5 real items exist, log PARTIAL and create pins only from real items; never invent inventory.
4. Check pinterest.com search suggestions (or a web search) for each keyword phrase; keep phrases you can verify, and mark unverifiable phrases 'unverified' instead of asserting volume.
5. Choose the target board per pin; propose a new board name (for example 'Estate Jewelry Finds', 'Vintage Costume Jewelry') when no board fits.
6. Write a keyword-stuffed but readable title under ~100 characters leading with the strongest keyword.
7. Write a 2-3 sentence description with keywords placed naturally; include item specifics only when the source row states them.
8. Write image direction as a shot list: background, props, angle, macro hallmark detail, scale reference - specific enough to shoot without follow-up questions.
9. Map every pin back to its source row (Listing Drafts or Lot Radar) and keep that URL.
10. Avoid duplicate titles already queued in Social Queue for Pinterest this month.
11. Prioritize items with clear search intent (named styles, eras, materials) over one-off novelties.
12. Never write 'authentic', 'signed', or era claims that the source row does not support.
13. Note blocked or unreachable keyword-check sources in the run log.

CONFIDENCE GATE: Every pin must come from a real row you read this run; keyword claims need a source URL or an explicit 'unverified' mark.
If fewer than 5 pins pass, create the verified set, set Status PARTIAL, and state the count in the run log notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Social Queue with EXACTLY these properties: Post (title), Platform (select TikTok|Instagram|X|Pinterest|Buffer), Copy (text), Media Note (text), Status (select Queued|Ready|Posted), Date (date).
- Create one row per pin, maximum 5. Platform = Pinterest. Status = Queued. Date = today.
- Post (title): the keyword-stuffed pin title.
- Copy (text): board name, then title, then the 2-3 sentence description.
- Media Note (text): the image-direction shot list plus the source row URL.
- Every factual claim must include its source URL (a Notion row URL is acceptable).
- If today's Pinterest rows already exist from an earlier run today, update them instead of duplicating.

DELIVERABLE: 0-5 Social Queue rows with Platform=Pinterest, each containing title, description, and shot list.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 36-pinterest-pin-plan, Date = today, Items = rows written to Social Queue, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
