# yt-content-scout — YouTube research & queue builder

- **Task name:** `yt-content-scout`
- **Schedule field:** `Every day at 9:00 AM`
- **Requires:** web browsing / Agent Tools enabled

Paste everything inside the code block into the Grok task prompt:

```text
TASK: YouTube Content Scout — research and queue builder

Research YouTube for my niche — pre-owned/secondhand jewelry resale,
pawn & estate lot flipping, ShopGoodwill-style auction sourcing, and
jewelry e-commerce — and produce a ranked queue of video ideas for my
channels.

PROCEDURE:
1. SCAN:
   - YouTube search sorted by this week / most relevant:
     "jewelry resale", "estate jewelry haul", "shopgoodwill haul",
     "pound lot jewelry", "selling jewelry online", "thrift jewelry flip",
     "whatnot jewelry"
   - Identify the 3-5 best-performing videos from the last 7 days
     (views relative to channel size; strong title/thumbnail hooks).
   - Check for niche news: auction site changes, eBay policy updates,
     Whatnot/Depop trends.
2. ANALYZE: for each top video extract why it works — hook type, title
   formula, format (haul / review / tutorial / sourcing trip), length.
3. GENERATE 3 VIDEO IDEAS for my channels, each with:
   - Title (2 CTR-optimized variants)
   - Hook (seed script for the first 15 seconds)
   - Outline (5-7 bullets)
   - Reference video(s) proving demand (with links)
   - Suggested format + target length
4. RANK by opportunity: high demand + low competition first.

OUTPUT (always produce):

## CONTENT QUEUE — {date}
### Trending now
Top 3-5 videos with links + one line on why they pop.
### IDEAS FOR MY CHANNELS (3, ranked)
Full idea blocks as specified above.
### NICHE NEWS
Relevant items only, or "none this run."

END EVERY REPORT WITH:
"TO SAVE IN NOTION — paste the idea blocks into the Content Queue DB at
workspace root (Title, Status=Queued, Hook, Outline, Reference, Date)."

RULES:
- Never fabricate videos, view counts, or news. Link everything you cite.
- Ideas must fit a jewelry-resale channel voice: sourcing, flipping,
  lot breakdowns, market pricing.
```
