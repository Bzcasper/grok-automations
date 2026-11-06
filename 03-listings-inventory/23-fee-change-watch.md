# 23-fee-change-watch - Fee Change Watch
- **Task name:** `fee-watch`
- **Schedule:** Every Friday at 11:00 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** "Platform News" DB (create if missing: Source (title), Change (text), Impact
  (text), Link (url), Date (date))

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Watch for platform fee and policy changes that hit small sellers.
GOAL: find recent
seller-fee, payment-processor, or shipping-policy changes on eBay, Etsy, Whatnot, Depop, and
Mercari, and write a one-paragraph impact assessment for a small jewelry reseller.

CONFIG: Use the Notion connector to read row 'fee-watch' from the 'Grok Task Config' DB. Use
its Sites/Keywords/Extra fields (Sites = platforms to watch, Keywords = announcement terms,
Extra = my volume/type context). If the row or DB is missing, use the DEFAULTS below and
include 'CONFIG MISSING' in the run log.
DEFAULTS: Sites = ebay.com, etsy.com, whatnot.com, depop.com, mercari.com; Keywords = seller
fees, final value fee, payment processing, shipping policy, fee change, effective date;
Extra = low-volume US seller of pre-owned jewelry, ships small parcels.

PROCEDURE:
1. Web-search each config platform for fee and policy announcements from the last 30 days,
   prioritizing the platform's own seller announcement or help pages.
2. Open the primary source and confirm: what changed, the effective date, and who it affects.
3. Search reputable secondary coverage (industry press, seller forums) to confirm the same
   change; note any disagreement between sources.
4. Ignore rumors, undated posts, and changes that only affect buyers.
5. For each confirmed change, draft a one-paragraph impact note: extra cost per typical
   jewelry sale, benefit or risk for low-volume sellers, and one action worth considering.
6. Prepare one Notion row per confirmed change.

CONFIDENCE GATE: Only report changes confirmed on the platform's own site or by two
independent sources with dates. Undated or single-source rumors are excluded and listed only
in Run Log Notes.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists
for this task (idempotency - do not duplicate). Then create rows in the "Platform News" DB
(create it with this schema if missing: Source (title), Change (text), Impact (text), Link
(url), Date (date)) with EXACTLY these properties: Source (title: platform name plus
announcement name), Change (text: what changed and effective date), Impact (text: one
paragraph on effect for a small jewelry reseller), Link (url: primary source), Date (date:
today). Every factual claim must include its source URL.

RUN LOG: Finally create a row in the 'Grok Run Log' DB: Task (fee-watch), Date (today), Status
(OK/PARTIAL/FAILED/CONFIG MISSING), Items (number of confirmed changes), Notes (errors, blocked
sites, rumors excluded, surprises). Create 'Grok Run Log' with this schema if missing: Task
(title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes
(text).

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never
use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
