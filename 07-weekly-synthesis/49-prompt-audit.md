# 49-prompt-audit - Prompt Audit
- **Task name:** `49-prompt-audit`
- **Schedule:** First Sunday of the month at 1:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + Gmail connector + web browsing / Agent Tools
- **Writes to:** Prompt Audit page + Gmail delivery + Run Log

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Monthly meta-review: read 30 days of run-log rows, find recurring FAILURES/PARTIALs, dead sites, and config drift, then write a 'Prompt Audit YYYY-MM' page with concrete proposed edits per task; HUMAN APPROVAL required.
GOAL: One dated audit page listing evidence-backed problems per task and exact proposed prompt/config edits for a human to approve.

CONFIG: Use the Notion connector to read row '49-prompt-audit' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: internal Notion only (Grok Run Log, Grok Task Config); web browsing only to verify a candidate dead site.
DEFAULTS - Keywords: n/a (internal meta task); window is the last 30 days.
DEFAULTS - Extra: proposed edits are suggestions only (never rewrite task prompts or config rows yourself); destination is the 'Prompt Audit YYYY-MM' page (create if missing).
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Using the Notion connector, read all Grok Run Log rows dated in the last 30 days.
2. Group by Task; for each task tally Status counts (OK, PARTIAL, FAILED, CONFIG MISSING) and note failure patterns from Notes (recurring errors, blocked sites, missing DBs).
3. Flag tasks with 2+ FAILED runs or 5+ PARTIAL runs in the window as recurring-failure candidates.
4. Identify dead sites: domains named in 3+ failure Notes across tasks; optionally open each candidate once to confirm it is down, blocked, or paywalled.
5. Detect config drift: tasks whose run notes say 'CONFIG MISSING' repeatedly, config rows whose Sites/Keywords no longer match what tasks actually use, and enabled rows pointing at dead domains.
6. For each flagged task, draft one concrete proposed edit: the exact prompt line or config field to change and the new text/value, grounded in the evidence.
7. Rank proposals by expected reliability gain (recurring failures first).
8. Mark every proposal 'HUMAN APPROVAL REQUIRED - not applied' and never edit task prompts or config rows in this run.
9. Note tasks that ran cleanly all month (one line each) so the audit is balanced.
10. If the run log window is thinner than 7 days of data, note the thin sample and set Status PARTIAL.
11. If the run log or config DB is unreachable, write nothing and set Status FAILED with the reason.
12. Keep the page structured: summary counts, recurring failures, dead sites, config drift, proposed edits, healthy tasks.
13. Every proposal must cite the run-log rows (dates or row titles) that justify it.

CONFIDENCE GATE: Every flag and proposal must be backed by run-log rows you actually read this run, with dates or row references. No speculative rewrites for tasks without evidence.
Any proposal with fewer than two supporting run-log rows is downgraded to an 'observation' instead of a proposed edit.

NOTION WRITE: Using the Notion connector, first check whether this month's audit already exists (idempotency - do not duplicate). Then find or create the 'Prompt Audit YYYY-MM' page (create if missing, using the current month) and add the structured audit content: summary counts, recurring failures (task + evidence), dead sites, config drift items, and proposed edits each marked 'HUMAN APPROVAL REQUIRED - not applied' with the exact proposed text. Every factual claim must include its source URL or row reference.
- Destination: the 'Prompt Audit YYYY-MM' page (create if missing, using the current month).
- Sections in order: summary counts, recurring failures, dead sites, config drift, proposed edits, healthy tasks.
- Each proposed edit: task name, current line or value, proposed replacement, and the run-log evidence (dates or row titles).
- Every proposal is labeled 'HUMAN APPROVAL REQUIRED - not applied'.
- Update-in-place: if this month's audit already exists, edit it instead of appending a duplicate.
- Never modify task prompt files, config rows, or Notion DB schemas in this run.

DELIVERABLE: One 'Prompt Audit YYYY-MM' page with evidence-backed problems and approval-gated proposed edits.

EMAIL STEP: After the audit page is written, use the Gmail connector to email tinydigitalproductlab@gmail.com the summary counts plus a link to the audit page, with subject 'Prompt Audit YYYY-MM - approval needed'. If Gmail is unavailable, add 'audit email not sent' to Notes; do not fail the run.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 49-prompt-audit, Date = today, Items = tasks audited, Notes = errors, blocked sites, surprises, proposals pending approval.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
