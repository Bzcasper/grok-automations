# Grok Scheduled Automations — 49 tasks

Scheduled tasks for the Grok web account, built to run against the
Notion workspace through Grok's native Notion connector
(grok.com/connectors -> Notion).

## Read first

1. `NOTION-GROK-PLAYBOOK.md` — the research: Grok connectors, Notion
   MCP, the 9-part prompt skeleton, DB schemas, operating hacks.
2. Connect Notion in Grok (grok.com/connectors -> New Connector ->
   Notion -> OAuth). Every task assumes this is done.
3. If you use the local MCP key: share the "Pre-Owned Jewelry Store
   OS" parent page and the "Content Queue" DB with the integration.
4. For each task file: paste the inside of the code block into a new
   Grok task, set the schedule from the header, enable browsing, run
   one Test run, confirm a "Grok Run Log" row appeared.

## Index

### 01-sourcing-auctions/ (tasks 1-10)
| # | File | Task name | Schedule |
|---|---|---|---|
| 1 | 01-lot-scout.md | lot-scout | Every day at 8:00 AM and 6:00 PM |
| 2 | 02-salvation-army-lots.md | sa-lots | Every day at 7:30 AM |
| 3 | 03-hibid-sweep.md | hibid-sweep | Every day at 10:00 AM |
| 4 | 04-proxibid-sweep.md | proxibid-sweep | Every day at 10:30 AM |
| 5 | 05-gov-muni-sweep.md | gov-muni-sweep | Every day at 11:00 AM |
| 6 | 06-bidrl-ninja-sweep.md | bidrl-ninja-sweep | Every day at 11:30 AM |
| 7 | 07-ebth-maxsold-sweep.md | ebth-maxsold-sweep | Every day at 12:00 PM |
| 8 | 08-closing-soon-sniper.md | closing-sniper | Every 6 hours |
| 9 | 09-keyword-fresh-scan.md | keyword-fresh-scan | Every day at 8:00 AM and 8:00 PM |
| 10 | 10-surplus-auctions.md | surplus-sweep | Every day at 1:00 PM |

### 02-pricing-comps/ (tasks 11-18)
| # | File | Task name | Schedule |
|---|---|---|---|
| 11 | 11-ebay-comps-refresh.md | comps-refresh | Every day at 2:00 PM |
| 12 | 12-metal-spot-check.md | metal-spot | Every day at 6:00 AM |
| 13 | 13-brand-price-index.md | brand-index | Every Friday at 9:00 AM |
| 14 | 14-costume-fine-trend.md | costume-fine-trend | Every Monday at 9:00 AM |
| 15 | 15-retail-gap-scan.md | retail-gap | Every Wednesday at 9:00 AM |
| 16 | 16-whatnot-comps.md | whatnot-comps | Every day at 3:00 PM |
| 17 | 17-etsy-depop-bench.md | etsy-depop-bench | Every Thursday at 9:00 AM |
| 18 | 18-comp-archiver.md | comp-archiver | Every Sunday at 6:00 PM |

### 03-listings-inventory/ (tasks 19-24)
| # | File | Task name | Schedule |
|---|---|---|---|
| 19 | 19-listing-copy-writer.md | listing-copy | Every day at 4:00 PM |
| 20 | 20-shot-list-generator.md | shot-list | Every day at 9:15 AM |
| 21 | 21-stale-inventory-flagger.md | stale-flagger | Every Monday at 8:00 AM |
| 22 | 22-crosslist-coverage.md | crosslist-coverage | Every Tuesday at 9:00 AM |
| 23 | 23-fee-change-watch.md | fee-watch | Every Friday at 11:00 AM |
| 24 | 24-listing-quality-audit.md | listing-audit | Every Saturday at 10:00 AM |

### 04-youtube-content/ (tasks 25-32)
| # | File | Task name | Schedule |
|---|---|---|---|
| 25 | 25-yt-content-scout.md | yt-content-scout | Every day at 9:00 AM |
| 26 | 26-yt-react-radar.md | yt-react-radar | Every day at 1:30 PM |
| 27 | 27-competitor-watch.md | competitor-watch | Every day at 6:30 PM |
| 28 | 28-hook-teardown.md | hook-teardown | Every day at 11:45 AM |
| 29 | 29-yt-keyword-seo.md | yt-keyword-seo | Every Wednesday at 10:00 AM |
| 30 | 30-shorts-miner.md | shorts-miner | Every day at 5:00 PM |
| 31 | 31-series-builder.md | series-builder | Every Sunday at 10:00 AM |
| 32 | 32-niche-benchmark.md | niche-benchmark | Every Sunday at 12:00 PM |

### 05-social-shortform/ (tasks 33-37)
| # | File | Task name | Schedule |
|---|---|---|---|
| 33 | 33-tiktok-trend-scan.md | tiktok-trends | Every day at 12:30 PM |
| 34 | 34-reels-hook-library.md | reels-hooks | Every Friday at 2:00 PM |
| 35 | 35-social-queue-builder.md | social-queue | Every day at 10:15 AM |
| 36 | 36-pinterest-pin-plan.md | pin-plan | Every Tuesday at 11:15 AM |
| 37 | 37-x-niche-watch.md | x-niche-watch | Every day at 7:00 PM |

### 06-business-intel/ (tasks 38-44)
| # | File | Task name | Schedule |
|---|---|---|---|
| 38 | 38-auction-site-watchdog.md | auction-watchdog | Every Monday at 10:00 AM |
| 39 | 39-ebay-policy-watch.md | ebay-policy-watch | Every day at 8:30 AM |
| 40 | 40-platform-news-roundup.md | platform-roundup | Every Thursday at 8:30 AM |
| 41 | 41-competitor-store-scan.md | competitor-store | Every Wednesday at 1:00 PM |
| 42 | 42-shipping-watch.md | shipping-watch | Every Monday at 11:30 AM |
| 43 | 43-counterfeit-intel.md | counterfeit-intel | Every Friday at 4:00 PM |
| 44 | 44-newsletter-digest.md | newsletter-digest | Every Sunday at 5:00 PM |

### 07-weekly-synthesis/ (tasks 45-49)
| # | File | Task name | Schedule |
|---|---|---|---|
| 45 | 45-lot-radar-review.md | lot-review | Every Sunday at 8:00 AM |
| 46 | 46-queue-prune.md | queue-prune | Every Saturday at 9:00 AM |
| 47 | 47-ops-report.md | ops-report | Every Sunday at 6:00 PM |
| 48 | 48-site-scorecard.md | site-scorecard | First Sunday of the month at 11:00 AM |
| 49 | 49-prompt-audit.md | prompt-audit | First Sunday of the month at 1:00 PM |

## Notes

- shopgoodwill.com is excluded from every sourcing task — the separate
  sgw-sniper covers it.
- All schedules are staggered by >= 15 minutes where possible (Grok
  routines must be >= 5 minutes apart).
- v1 legacy prompts (root-level lot-scout.md / yt-content-scout.md)
  are superseded by files 01 and 25 in the folders above.
- Tasks 48 and 49 write recommendations only — config and prompt
  changes always require your approval.

## Your Grok connectors — how they're used

| Connector | Used by |
|---|---|
| Notion | All 49 tasks (config reads + result writes) |
| Gmail | 44-newsletter-digest, 47-ops-report, 49-prompt-audit (email to tinydigitalproductlab@gmail.com) |
| Buffer | 35-social-queue-builder (drafts only, never auto-published — link your channels in Buffer first) |
| Google Drive | 18-comp-archiver, 48-site-scorecard (CSV exports to a "Grok Exports" folder) |
| HubSpot, Whop, Netlify, Vercel, GitHub | not used by these tasks |

Skills note: none of the installed skill packs (coding/design) apply to
these ops tasks. Optionally prepend "respond in caveman mode, full
intensity" to any task prompt for compressed run output.
