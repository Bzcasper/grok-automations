# 43-counterfeit-intel - Counterfeit Intel
- **Task name:** `43-counterfeit-intel`
- **Schedule:** Every Friday at 4:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** "Field Guide" page (create if missing) + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Research current counterfeit patterns for the watched brands (fake marks, common fakes appearing in bulk lots) and produce a 5-bullet field guide update with links.
GOAL: A dated 5-bullet counterfeit intel update appended to the Field Guide page, plus this run's row in the Grok Run Log.

CONFIG: Use the Notion connector to read row '43-counterfeit-intel' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: brand authentication pages, hallmark reference sites (925, sterling marks), customs and FTC seizure press releases, reputable jewelry-authentication blogs, auction-house authentication guides.
DEFAULTS - Keywords: counterfeit hallmark, fake sterling mark, common fake jewelry brands, bulk lot fakes, costume jewelry fakes, trademark counterfeiting jewelry.
DEFAULTS - Extra: watched brands list lives in the config Keywords field; keep each bullet actionable (what the fake looks like, where it shows up, how to verify); 5-bullet cap.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Read the watched-brand list from config Keywords; if empty, use the default keyword set above and note CONFIG MISSING.
2. Open brand authentication or hallmark reference pages first; they outrank blogs for mark details.
3. Run web searches limited to the last 30 days for new counterfeit patterns on the watched brands (examples: 'fake <brand> hallmark 2026', 'counterfeit jewelry seizure news').
4. Open each candidate source; a search snippet alone never qualifies.
5. Extract candidate patterns: how the fake mark differs (spacing, font, depth, wrong metal stamp), which brands or marks are being faked, and which channels they appear in (bulk lots, estate boxes, online marketplaces).
6. Verify each pattern against at least one authoritative source (brand page, lab guide, customs release); prefer two sources for mark-specific claims.
7. Select the top 5 patterns ranked by likelihood of hitting a small jewelry buyer (bulk lots and estate mixes first).
8. Write each bullet: pattern name, what the fake looks like, where it shows up, one verification step, and the source URL.
9. Dedupe against prior Field Guide updates so the same old pattern is not recycled; read the page first and skip anything covered in the last 90 days.
10. If genuinely new patterns are scarce, include fewer bullets rather than padding; note the shortfall in the run log.
11. Keep bullets concise (3-5 lines each); this is a field checklist, not an essay.
12. Never give authentication certainty beyond what the source supports ('strong indicator', not 'guaranteed real').
13. Log blocked sites, paywalled guides, and unsourced forum claims you rejected in Notes.

CONFIDENCE GATE: Each bullet needs at least one opened, dated source URL; mark-specific claims need an authoritative source (brand, lab, customs, or major auction house). Blog-only, unlinked, or older-than-30-days claims are dropped unless they are the only coverage of a genuinely new pattern (then mark 'secondary source').
If fewer than 5 patterns survive verification, write only the survivors and set Status PARTIAL with the shortfall noted; never pad the section with recycled patterns.

NOTION WRITE: Using the Notion connector, first check whether today's update already exists for this task (idempotency - do not duplicate). Then find or create the 'Field Guide' page (create if missing) and append a dated section 'Counterfeit intel update YYYY-MM-DD' containing exactly the 5 selected bullets (or fewer with a note), each bullet ending in its source URL. Every factual claim must include its source URL. Do not overwrite prior sections on the page.
- Section heading: 'Counterfeit intel update YYYY-MM-DD' using today's date, appended below prior sections.
- Exactly 5 bullets (or fewer with an explicit shortfall note), each 3-5 lines long.
- Bullet format: pattern name, what the fake looks like, where it shows up, one verification step, then the source URL.
- Field-checklist tone: what to check before buying, not brand history or essays.
- Append only: never overwrite, reorder, or delete existing Field Guide sections.
- Every factual claim in the section must include its source URL.

DELIVERABLE: One dated section of up to 5 linked counterfeit-pattern bullets in the Field Guide page.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 43-counterfeit-intel, Date = today, Items = bullets written, Notes = errors, blocked sites, surprises, and any config gap.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
