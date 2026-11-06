# 42-shipping-watch - Shipping Watch
- **Task name:** `42-shipping-watch`
- **Schedule:** Every Monday at 11:30 AM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Platform News (Source="Shipping")

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Scan for USPS, UPS, and FedEx rate, surcharge, or service-level change news, and write an impact line for lightweight jewelry parcels on each item.
GOAL: 0-6 linked Platform News rows (Source = 'Shipping') covering carrier changes that move the cost or speed of small parcel delivery.

CONFIG: Use the Notion connector to read row '42-shipping-watch' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: about.usps.com news, pressroom.ups.com, news.fedex.com, shipping-trade press (PostalMagazine, Parcel, Stamps.com blog).
DEFAULTS - Keywords: USPS rate change, USPS Ground Advantage, UPS surcharge, UPS rate increase, FedEx rate change, FedEx surcharge, shipping surcharge, dim weight.
DEFAULTS - Extra: window is last week since the previous Monday run plus announced future-effective changes; my parcels are typically under 8 oz, zone 3-5, no signature; Source must be exactly 'Shipping'.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.
FRESHNESS: Only in-window carrier changes or announcements with in-window effective dates count; old rate cycles already recorded in Platform News are dropped.

PROCEDURE:
1. Open the official newsroom or rate-announcement pages for USPS, UPS, and FedEx.
2. Run one web search per carrier limited to the last 7 days plus announced future changes (examples: 'USPS shipping rate change announcement', 'UPS surcharge 2026 announcement').
3. Open each candidate article or official announcement; a search snippet alone never qualifies.
4. Filter to changes that could touch a small parcel shipper: per-ounce or per-zone rate moves, fuel or residential/DIM surcharges, service renames or retirements, delivery-speed or holiday-surge changes.
5. Drop consumer retail moves with no effect on shipping labels (for example package-store hours, unrelated corporate news).
6. Dedupe against Platform News rows with Source 'Shipping' from the last 30 days; read those rows first so old rate cycles are not re-reported.
7. For each verified change, write Impact (text) specifically for lightweight jewelry parcels: cents per parcel, delivery-time risk, or a workaround (cheaper service tier, mail).
8. Note effective dates; distinguish 'announced, future effective' from 'already in effect'.
9. If no carrier news surfaced in the window, write no rows and log Status OK with Items 0 and Notes 'no carrier changes detected'.
10. If official pages and trade press are all unreachable, set Status FAILED with the reason.
11. If only one or two carriers were verifiable, write what you verified and set Status PARTIAL.
12. Cap at 6 rows; rank by dollar impact on a jewelry parcel first.
13. Log blocked sites and anything suspicious (blog-only rumors with no official backing) in Notes.

CONFIDENCE GATE: Each item needs an opened source (official carrier page or reputable trade press) dated inside the window or announcing an in-window effective date. Unlinked or undated claims are dropped.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in Platform News with EXACTLY these properties: Source (title), Change (text), Impact (text), Link (url), Date (date).
- Create one row per verified change, maximum 6. Date = today.
- Source (title): Shipping (exactly).
- Change (text): carrier + what changed + effective date.
- Impact (text): one line on the effect on lightweight jewelry parcels.
- Link (url): the source URL you opened.
- Every factual claim must include its source URL.

DELIVERABLE: 0-6 Platform News rows (Source='Shipping') with jewelry-parcel impact lines.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 42-shipping-watch, Date = today, Items = rows written to Platform News, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
