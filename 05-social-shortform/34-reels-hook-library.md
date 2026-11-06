# 34-reels-hook-library - Reels Hook Library
- **Task name:** `34-reels-hook-library`
- **Schedule:** Every Friday at 2:00 PM
- **Requires:** Notion connector (grok.com/connectors -> Notion) + web browsing / Agent Tools
- **Writes to:** Hook Library (create if missing: Hook (title), Type (select Title|Open|Structure), Notes (text), Link (url), Date (date))

Paste everything inside the code block into the Grok task prompt:

```text
TASK: Research 10 fresh Instagram Reels and TikTok hooks that worked this month in resale niches, then rewrite each in my jewelry-resale voice.
GOAL: 10 rewritten hooks saved to the Hook Library, each traceable to a real, current example; or an honest PARTIAL with fewer.

CONFIG: Use the Notion connector to read row '34-reels-hook-library' from the 'Grok Task Config' DB. Use its Sites/Keywords/Extra fields. If the row or DB is missing, use the DEFAULTS below and include 'CONFIG MISSING' in the run log.
DEFAULTS - Sites: reseller and creator-economy blogs, hook-teardown articles, short-form video marketing newsletters, web-openable TikTok/Reels example posts.
DEFAULTS - Keywords: viral hooks Reels, TikTok hooks resale, thrift TikTok hooks, hooks that worked this month, hook formulas small business.
DEFAULTS - Extra: hooks must be from this month (last 30 days); rewrite in my voice - direct, specific to estate and pre-owned jewelry, no hype; classify each as Title, Open, or Structure.
CONFIG NOTE: If the row exists but Enabled is unchecked, stop, create no rows, and log Status OK with Items 0 and Notes 'disabled in config'.

PROCEDURE:
1. Run date-restricted web searches (last 30 days) for Reels and TikTok hooks that performed well in resale, thrift, and flipping niches this month.
2. Open the configured Sites and collect candidate hooks with example URLs and dates.
3. Verify each candidate by opening at least one live example post or a dated article from this month; drop anything you cannot date to this month.
4. Extract 10 distinct hooks - one concept each, no near-duplicates of the same formula.
5. For each hook, classify Type: Title (text on screen), Open (first spoken line), or Structure (repeatable template such as curiosity open, proof stack, before/after).
6. Rewrite each hook in my jewelry-resale voice: keep the underlying psychology, change the words to fit estate jewelry, lots, and small-seller POV.
7. For each rewritten hook, add one-line usage guidance: listing tease, sold recap, haul, or education.
8. Keep the original example URL per hook as proof it worked this month.
9. Before saving, check the Hook Library for the same source URL so you do not re-save an existing hook.
10. Record the original hook wording briefly in Notes so future runs can spot drift and duplication.
11. If fewer than 10 hooks pass the freshness gate, save only the verified set; never pad with stale or invented hooks.
12. Flag in the run log any source from outside the resale niche and why its hook still maps to mine.
13. Note blocked, paywalled, or login-only sources in the run log.

CONFIDENCE GATE: Every hook needs an opened source dated within the last 30 days (example post or dated article). No undated listicles, no last-month recycles.
If fewer than 10 qualify, save the verified set, set Status PARTIAL, and state the verified count in the run log notes.

HYGIENE: skip if an identical Title already exists in the last 7 days; keep Notion text fields concise (Notes <= 500 chars).

NOTION WRITE: Using the Notion connector, first check whether a row for today already exists for this task (idempotency - do not duplicate). Then create/update rows in the Hook Library DB (create it with this schema if missing) with EXACTLY these properties: Hook (title), Type (select Title|Open|Structure), Notes (text), Link (url), Date (date).
- Create one row per hook, maximum 10. Date = today.
- Hook (title): the rewritten jewelry-resale version of the hook.
- Type (select): Title, Open, or Structure.
- Notes (text): original hook wording, niche it came from, why it works, and when to use it.
- Link (url): source URL proving the hook worked this month.
- Every factual claim must include its source URL.
- Skip any hook whose source URL already exists in the Hook Library; note skipped duplicates in the run log.

DELIVERABLE: 0-10 Hook Library rows of fresh, sourced, rewritten hooks (PARTIAL if under 10).

RUN LOG: Finally create a row in the 'Grok Run Log' DB with EXACTLY these properties: Task (title), Date (date), Status (select OK|PARTIAL|FAILED|CONFIG MISSING), Items (number), Notes (text).
Set Task = 34-reels-hook-library, Date = today, Items = rows written to Hook Library, Notes = errors, blocked sites, surprises.

STALE-DATA POLICY: If a site or DB is unreachable, mark Status FAILED with the reason. Never use old data as if it were fresh.

NO FABRICATION: Never invent lots, prices, videos, view counts, or news. Link every claim.

APPROVAL BOUNDARY: Discovery and drafts only. Never bid, buy, publish, send, or delete.
```
