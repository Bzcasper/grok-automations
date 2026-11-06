# 44-newsletter-digest - Newsletter Digest
- **Task name:** `44-newsletter-digest`
- **Schedule:** Every Sunday at 5:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + Gmail connector
- **Writes to:** Weekly Digest page (create if missing) + Gmail delivery + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Read this week's rows across Platform News, Trend Briefs, and Competitor DBs, then compile a 'Week of YYYY-MM-DD Digest' page with the top 10 items, each one line plus a link.
GOAL: One digest page for the week ending today, holding 10 ranked one-line items with source links.

CONFIG: Use the Notion connector to read row '44-newsletter-digest' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Platform News, Trend Briefs, Competitor Channels/Competitor Stores, Hook Library); no web browsing required except to resolve a missing link.
DEFAULTS - Keywords: n/a (internal read task); rank by impact on a small jewelry seller.
DEFAULTS - Extra: window is Monday 00:00 through today; top 10 items hard cap; one line per item plus link; a 'Weekly Digest' page is the destination (create if missing).
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read all Platform News rows dated in the last 7 days; note each row's Source, Change, Impact, and Link.
2. Read all Trend Briefs rows dated in the last 7 days if that DB exists; if missing, note it in the run log and continue.
3. Read competitor rows from the Competitor Channels or Competitor Stores destination dated in the last 7 days; if missing, note and continue.
4. Pool everything into a candidate list with source links; drop any item lacking a link.
5. Rank the pool by impact on a small jewelry seller (fees and policy first, then carrier/competitor moves, then trends).
6. Select the top 10 items; if fewer than 10 linked items exist this week, include all of them and say so in the page.
7. Write each as exactly one line: what happened, why it matters (short clause), then the link.
8. Group the lines under light headings if useful (Platform changes / Carriers / Competitors / Trends) but keep the 10-line total.
9. Compose the page title as 'Week of YYYY-MM-DD Digest' using today's date.
10. Check whether a digest page for this week already exists; if so, update it rather than creating a second one (idempotency).
11. Create the 'Weekly Digest' parent page if no such destination exists, then add the dated digest under it.
12. If every source DB was unreachable, write nothing and set Status FAILED with the reason.
13. If some DBs were missing but others read fine, proceed with what you got and set Status PARTIAL.

CONFIDENCE GATE: Every item must come from a Notion row you actually read this run, inside the 7-day window, with its link preserved. No invented summaries, no carried-over items from prior weeks.
If fewer than 10 items qualify, include all verified items; a genuinely quiet week is Status OK with the item count in Notes, but a failed DB read makes the run PARTIAL or FAILED.

NOTION WRITE: Using the Notion connector, first check whether a page for this week already exists (idempotency - do not duplicate). Then find or create the 'Weekly Digest' page (create if missing) and add a child page or dated section titled 'Week of YYYY-MM-DD Digest' containing exactly the 10 (or fewer) one-line items with links. Every factual claim must include its source URL. Do not delete prior weeks' digests.
- Destination: the 'Weekly Digest' page (create if missing), then a child page or dated section titled 'Week of YYYY-MM-DD Digest'.
- Item count: up to 10 one-line items; state the actual count on the page.
- Item format: what happened, why it matters (short clause), then the link, all on one line.
- Optional grouping headings (Platform changes / Carriers / Competitors / Trends) do not count toward the 10 lines.
- Update-in-place: if this week's digest already exists, edit it instead of creating a duplicate.
- Never delete or reorder prior weeks' digests.

DELIVERABLE: One 'Week of YYYY-MM-DD Digest' page with up to 10 linked one-line items.

EMAIL STEP: After the digest page is written, use the Gmail connector to email the same up-to-10 digest lines to tinydigitalproductlab@gmail.com with subject 'Week of YYYY-MM-DD - Ops Digest'. If Gmail is unavailable, add 'digest email not sent' to Notes; do not fail the run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 44-newsletter-digest, Date = today, Items = items included in the digest, Notes = errors, missing DBs, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
