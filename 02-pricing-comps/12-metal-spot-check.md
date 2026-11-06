# 12-metal-spot-check — Metal Spot Check
- **Task name:** `metal-spot`
- **Schedule:** Every day at 6:00 AM
- **Requires:** Notion connector (grok.com/connectors → Notion) + web browsing / Agent Tools
- **Writes to:** Price Reference

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Daily precious-metal spot price check.
GOAL: Fetch current gold, silver, and platinum spot prices from multiple sources, cross-check them, record the consensus.

CONFIG: Use the Notion connector to read row 'metal-spot' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: at least 3 of kitco.com, goldprice.org, lbma.org.uk, apmex.com, bullionvault.com.
DEFAULTS - Keywords: gold spot price, silver spot price, platinum spot price.
DEFAULTS - Metals: gold, silver, platinum (one Price Reference row each).
DEFAULTS - Extra: units USD per troy ounce; cross-check tolerance 1 percent; at least 3 sources per metal.
DEFAULTS - Cross-check rule: the median of agreeing sources is the recorded value.
If the config row exists but Enabled is unchecked, skip this run and log Status OK with Items 0.

PROCEDURE:
1. Fetch the current spot price of gold (USD per troy ounce) from at least three independent sources.
2. Repeat the same fetch for silver and for platinum.
3. Cross-check each metal: if sources disagree by more than 1 percent, fetch a fourth source and note the spread.
4. Use the median of the agreeing sources as the recorded price for that metal.
5. Keep the primary source URL you are citing for each metal (one URL per metal row).
6. Note the fetch time in UTC in the Run Log Notes so later runs can judge freshness.
7. Confirm every source quotes USD per troy ounce before comparing any numbers.
8. If one source sits more than 10 percent away from the others, treat it as an error and refetch it.
9. Attach the source URL to each metal value before any Notion write happens.
10. Compare today's median against yesterday's only to spot anomalies, never to fill a gap.

CONFIDENCE GATE: Only record a metal price when at least two independent sources agree within tolerance.
- Fewer than two agreeing sources means do not write that metal; note it in Notes.
- Never carry yesterday's spot price forward as today's.
- If a metal has fewer than two agreeing sources, write no row for that metal.
- If all three metals fail, report FAILED with the reason.

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create rows in Price Reference with EXACTLY these properties:
- Item (title) - exactly "Gold spot", "Silver spot", or "Platinum spot"
- Platform (select) - set to Market for every row in this task
- Price (number) - USD per troy ounce
- Link (url) - the primary source you cited
- Date (date) - today
Three rows are expected per run at defaults: Gold spot, Silver spot, Platinum spot.
Every factual claim must include its source URL. Create the DB with this schema if missing.

RUN LOG: Finally create a row in the 'Grok Run Log' DB with properties Task (title), Date (date, today), Status (select OK/PARTIAL/FAILED/CONFIG MISSING), Items (number), Notes (text: per-metal source agreement, spreads, errors). Create the DB with this schema if missing.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
