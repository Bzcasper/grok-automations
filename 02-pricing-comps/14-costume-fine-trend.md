# 14-costume-fine-trend — Costume Fine Trend
- **Task name:** `costume-fine-trend`
- **Schedule:** Every Monday at 9:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Price Reference (Trend brief rows) or Trend Briefs DB

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Weekly costume vs fine jewelry trend brief.
GOAL: Produce a five-bullet, link-backed brief on whether costume or fine jewelry is trending up in sold data and social interest.

CONFIG: Use the Notion connector to read row 'costume-fine-trend' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: ebay.com, google trends, reddit.com, etsy.com, plus recent news sources.
DEFAULTS - Keywords: costume jewelry, fine jewelry, estate jewelry, vintage jewelry.
DEFAULTS - Sources: at least one eBay sold dataset, one interest source, one dated news item.
DEFAULTS - Window: last 30 days vs the prior 30 days for sold-data comparisons.
DEFAULTS - Extra: exactly 5 bullets; each bullet must carry one supporting link.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Pull eBay sold-listing volume and median prices for costume jewelry vs fine jewelry, last 30 days vs prior 30 days.
2. Check search and social interest (Google Trends, Reddit jewelry communities) and capture the URLs you used.
3. Skim recent news or resale reports on jewelry demand; keep only items with a URL and a visible date.
4. Synthesize exactly 5 bullets: what is up, what is down, each bullet carrying its supporting link.
5. End with a one-line verdict: costume, fine, or split, and the reason.
6. Run the idempotency check before writing (step in NOTION WRITE).
7. Discard any source that is undated, paywalled, or behind a login.
8. Draft the five bullets first, then verify every link opens before any Notion write.
9. Count the bullets: exactly five, no more, no fewer; merge or cut as needed.
10. Note in the Run Log which sources carried sold data and which carried interest data.

CONFIDENCE GATE: Every bullet must cite a live URL you actually opened this run.
- If you cannot support a direction with data, write "no signal" instead of guessing.
- No links, no brief: report FAILED and write nothing.
- Social chatter without dates does not count as a trend signal.
- Sold-data claims and interest claims must each carry their own link.
- If you can support fewer than 5 bullets, report PARTIAL and say exactly what is missing.

NOTION WRITE: Using the Notion connector, first check whether a row or page for today already exists for this task (idempotency - do not duplicate). Primary target is the 'Trend Briefs' DB with EXACTLY these properties:
- Brief (title) - "Costume vs fine trend brief <today's date>"
- Summary (text) - the 5 bullets, each with its link
- Link (url) - the single strongest source for this week
- Date (date) - today
Brief titles must match exactly: "Costume vs fine trend brief <today's date>".
Create the Trend Briefs DB with this schema if missing. Fallback if that DB cannot be created: one Price Reference row with Item "Trend brief <today's date>", Platform "Market", Price left empty (not applicable), Link = strongest source, Date = today. Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: where the brief was written, sources tried, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
