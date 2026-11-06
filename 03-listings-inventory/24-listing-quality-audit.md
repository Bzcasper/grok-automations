# 24-listing-quality-audit - Listing Quality Audit
- **Task name:** `listing-audit`
- **Schedule:** Every Saturday at 10:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Run Log + audit rows to a "Listing Audit" page (create if missing)

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Audit live listing quality against a best-practice checklist.
GOAL: sample 5 live
listings in my store's niche, score each against generic jewelry-resale quality criteria, and
flag concrete improvements.

CONFIG: Use the Notion connector to read row 'listing-audit' from the 'Grok Task Config' DB.
Use its Sites/Keywords/Extra fields (Sites = where my live listings are, Keywords = niche and
store identifiers for sampling, Extra = checklist thresholds). If the row or DB is missing,
use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, etsy.com; Keywords = store name, SKU prefix, jewelry resale;
Extra = title 55-80 characters, at least 5 photos, condition stated in first sentence, free
or stated shipping, no all-caps keyword stuffing.

PROCEDURE:
1. Using the Notion connector, read Listing Drafts rows with Status=Listed to learn my store
   niche and the identifiers needed to find my live listings.
2. Web-search each config site for my listings and pick a random sample of 5 live listings
   covering different item types; open each listing page.
3. Score each listing on the checklist from config Extra: title length and keyword order,
   photo count and hero shot, condition honesty in the first sentence, measurement presence,
   shipping terms clarity, price vs comp sanity (spot-check one comp per listing).
4. Record one concrete improvement per failing criterion, in priority order.
5. Write the findings into the audit output below; do not change any listing.

CONFIDENCE GATE: Only score a listing that was actually opened and read this run. If fewer
than 5 listings can be opened, audit what you have, mark Status=PARTIAL, and list the ones
that could not be loaded in Notes.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then find or create the "Listing Audit" page
and add today's dated section with one block per sampled listing containing EXACTLY these
fields: Listing URL (with platform), Score (pass/fail per checklist criterion), Title Length,
Photo Count, Condition Honesty, Shipping Terms, and Improvements (prioritized list). Every
factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (listing-audit), Date (today),
Status (OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of listings audited), Notes (errors,
blocked sites, listings that could not open, surprises). Create either DB if missing: 'Grok Run
Log' (Task title, Date date, Status select OK|PARTIAL|FAILED|CONFIG MISSING, Items number,
Notes text) or the "Listing Audit" page.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh; do not reuse a previous audit as this run's results.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
