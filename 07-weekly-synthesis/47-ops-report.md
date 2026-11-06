# 47-ops-report - Ops Report
- **Task name:** `47-ops-report`
- **Schedule:** Every Sunday at 6:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + Gmail connector
- **Writes to:** "Week of YYYY-MM-DD" Weekly Report page (create if missing) + Gmail delivery + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Read Run Log, Lot Radar, Content Queue, Social Queue, and Platform News and write a one-page ops health report: runs OK vs FAILED, top lot, top idea, top news, and 3 action items for the human.
GOAL: One 'Week of YYYY-MM-DD' Weekly Report page section 'Ops Report' giving a scannable health snapshot plus 3 concrete human actions.

CONFIG: Use the Notion connector to read row '47-ops-report' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Grok Run Log, Lot Radar, Content Queue, Social Queue, Platform News); no web browsing required.
DEFAULTS - Keywords: n/a (internal synthesis task); window is Monday 00:00 through today.
DEFAULTS - Extra: one page maximum; action items must be specific and doable by the human this week; destination is the 'Week of YYYY-MM-DD' Weekly Report page (create if missing).
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read all Grok Run Log rows dated in the last 7 days; tally Status counts: OK, PARTIAL, FAILED, CONFIG MISSING, plus total runs.
2. List any task that failed 2+ times this week (recurring failures) with its run-log row references.
3. Read Lot Radar rows from the week; pick the top lot by score or win, with its URL if present.
4. Read Content Queue and Social Queue rows from the week; pick the top idea (strongest hook or most production-ready draft) by row title.
5. Read Platform News rows from the week; pick the top news item by small-seller impact, keeping its Link.
6. Note queue health: how many items are Queued/Drafted in Content Queue and Queued/Ready in Social Queue (counts only).
7. Draft exactly 3 action items for the human, each tied to evidence from steps 1-5 (for example 'fix config row for task X after 3 FAILED runs').
8. Rank action items by urgency; make each one sentence with a clear verb.
9. If any of the five DBs was unreachable, proceed with the rest and set Status PARTIAL; if more than half were unreachable, set Status FAILED.
10. Recompute all numbers this run; never carry last week's tallies forward without re-reading.
11. Keep the page to one page: health line, recurring failures, top lot, top idea, top news, 3 actions.
12. Include row titles or URLs beside every pick so the human can verify.
13. Note empty DBs in Notes rather than inventing entries.

CONFIDENCE GATE: Every count, pick, and action item must trace to rows you read this run, with row titles or URLs. No estimates, no recall of prior weeks.
- If fewer than 3 source rows exist this week, set Status PARTIAL and skip the action items.
If any of the five DBs failed to read, name it in the section's data-gaps line and reflect it in the run-log Status (PARTIAL for one or two DBs, FAILED for more than half).

NOTION WRITE: Using the Notion connector, first check whether a page for this week already exists (idempotency - do not duplicate). Then find or create the Weekly Report page titled 'Week of YYYY-MM-DD' (create if missing, using today's date) and add/update a section 'Ops Report' containing: run tally (OK/PARTIAL/FAILED/CONFIG MISSING counts), recurring failures list, top lot, top idea, top news, queue counts, and the 3 action items. Every factual claim must include its source URL or row reference. Do not delete other sections (for example Lot Radar Review) on the same page.
- Destination: this week's 'Week of YYYY-MM-DD' Weekly Report page (create if missing), section 'Ops Report'.
- Section contents in order: run tally, recurring failures, top lot, top idea, top news, queue counts, 3 action items.
- Every pick carries its row title or URL so the human can verify in one click.
- Action items: exactly 3, each one sentence with a clear verb and the evidence that motivated it.
- Update-in-place: if this week's section already exists, edit it instead of appending a duplicate.
- Preserve other sections on the same page (for example Lot Radar Review); edit only 'Ops Report'.

DELIVERABLE: One 'Ops Report' section in this week's Weekly Report page (tally, top picks, 3 action items).

EMAIL STEP: After the Ops Report section is written, use the Gmail connector to email the same section (tally, top picks, 3 action items) to tinydigitalproductlab@gmail.com with subject 'Week of YYYY-MM-DD - Ops Report'. If Gmail is unavailable, add 'report email not sent' to Notes; do not fail the run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 47-ops-report, Date = today, Items = number of source rows read, Notes = errors, unreachable DBs, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
