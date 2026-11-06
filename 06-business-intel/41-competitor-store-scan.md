# 41-competitor-store-scan - Competitor Store Scan
- **Task name:** `41-competitor-store-scan`
- **Schedule:** Every Wednesday at 1:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Competitor Channels DB reused as Competitor Stores (create if missing: Channel (title), Video (title), Views (number), Hook (text), Link (url), Date (date)) or a "Competitor Stores" page

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Scan 5 competitor pre-owned jewelry online stores for new stock, pricing posture, shipping offers, and what sold. If the config list is empty, discover candidates and log them for human approval before tracking.
GOAL: One scan row per competitor store, or a shortlist of discovered candidates awaiting human approval when no list exists.

CONFIG: Use the Notion connector to read row '41-competitor-store-scan' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: none hardcoded; the config Extra field should hold 5 competitor store URLs or names.
DEFAULTS - Keywords: pre-owned jewelry store, estate jewelry online shop, vintage jewelry seller, signed costume jewelry shop, estate sale company store.
DEFAULTS - Extra: if no list is configured, discover 5 candidate stores via search, write them to the run log and to a 'Competitor Stores' Notion page marked 'AWAITING HUMAN APPROVAL', and scan only 1-2 of them this run.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Read the config Sites/Extra fields for the competitor store list.
2. If the list is empty or missing: run discovery searches for pre-owned and estate jewelry online stores, pick 5 plausible candidates (live sites that actually sell used, vintage, or estate jewelry), and flag all 5 for human approval before treating any as tracked.
3. For each store being scanned this run (5 if configured, 1-2 if newly discovered), open its new-arrivals or most-recent-listing pages.
4. Record new stock: notable arrivals, categories, and brands/signatures spotted, each with the listing URL.
5. Record pricing posture: a few example asking prices with links (say 'entry', 'mid', or 'premium' positioning relative to what you observe; do not compare to my prices unless you just read them).
6. Record shipping offers: free-shipping threshold, flat-rate deals, or 'local pickup only' notices, with the page URL where you saw them.
7. Record what sold: open sold, sold-out, or just-sold pages if the store exposes them; if not exposed, write 'sold data not public' instead of guessing.
8. Write a 3-5 line per-store summary in plain language: stock flow, pricing posture, shipping offer, sold signals.
9. Verify every claim by keeping its URL; claims without a URL are dropped.
10. If a store blocks access or times out, record it as blocked and continue with the others.
11. New discoveries from an empty config still get logged for approval even if you could not scan them fully.
12. Cap at 5 stores per run; no deep per-item inventory pulls.
13. Note in the run log which stores are new discoveries vs previously approved.

CONFIDENCE GATE: Only claim what you saw on an opened page this run, with its URL. No revenue estimates, no traffic estimates, no guessed sold counts. If fewer than 3 configured stores were reachable, set Status PARTIAL; if none, FAILED.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in the Competitor Channels DB reused as Competitor Stores (create it with this schema if missing: Channel (title), Video (title), Views (number), Hook (text), Link (url), Date (date)) with EXACTLY these properties:
- One row per store scanned this run. Date = today.
- Channel (title): the competitor store name.
- Video (title): 'Scan YYYY-MM-DD: <new stock / pricing / shipping / sold headline>'.
- Views (number): leave empty or 0 (this task does not count views).
- Hook (text): the 3-5 line per-store summary plus the itemized claims.
- Link (url): the store homepage or the key page you opened.
- Every factual claim must include its source URL inside Hook.
If no Competitor Stores destination exists, instead create a 'Competitor Stores' page (create if missing) and append a dated section with the same per-store content.

DELIVERABLE: 0-5 Competitor Stores rows (or page entries), plus human-approval flags for any newly discovered candidates.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 41-competitor-store-scan, Date = today, Items = stores scanned, Notes = errors, blocked sites, surprises, and any candidates awaiting approval.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
