# Notion + Grok Playbook

Research notes for the 49 Grok scheduled automations in this folder.
Sources: docs.x.ai (Grok Connectors + Skills/Routines, Oct 2026),
x.ai announcements, Notion MCP docs, setup guides.

## 1. The big correction

Grok HAS a Notion connector. In Grok's OAuth catalog since May 6,
2026: "Notion - Pages, databases, and workspaces in Notion." Add it
at grok.com/connectors -> New Connector -> Notion -> sign in. Grok
can then search or edit pages, databases, and wikis your account can
open. All 49 tasks read config from Notion and write result rows
directly through this connector - no copy-paste handoff needed.

## 2. Grok platform facts (official docs)

- Connectors: built-ins (Gmail+Calendar, Drive, OneDrive, Outlook,
  Teams, SharePoint, Salesforce), OAuth catalog (Notion, GitHub,
  Linear, Box, Canva, Gamma, Meltwater, S&P), custom MCP servers
  (must be public-internet reachable; local needs a tunnel).
- Skills = reusable instruction sets; routines = scheduled or
  event-triggered runs owned by a Bot.
- Limits: 50 routines per Bot, 20 recent run records kept, schedules
  >= 5 minutes apart. Background routines run with laptop closed.
- "Test run" performs real work - run it after any prompt edit.
- Teach-by-demonstration: record a browser workflow (<=10 min) and
  Grok drafts a skill from it.

## 3. Notion connector facts

- Grok's Notion connector acts with ALL your Notion permissions.
  Assume it can see and change whatever your account can.
- Optional hardening: route Grok -> Upsy (free) -> Notion MCP for
  read-only or per-action permissions plus a full audit history.
- Internal tokens (ntn_...) only see pages SHARED with the
  integration (page ... menu -> Connections -> integration). An
  unshared token returns an empty search result - this is why the
  initial API test found zero pages.
- Notion search from connectors is keyword search unless the
  workspace has Notion AI: always reference DBs by exact title.
- Notion runs its own MCP server (mcp.notion.com). For local
  agent-side scaffolding: npx @domdomegg/notion-mcp-server with
  NOTION_API_KEY (configured in ~/.vscode-cline/mcp_settings.json).

## 4. The 9-part skeleton in every task prompt

1 TASK + goal | 2 CONFIG read from "Grok Task Config" DB (sites,
keywords, toggles - edit in Notion, not in prompts) | 3 PROCEDURE |
4 CONFIDENCE GATE | 5 NOTION WRITE (idempotent: check today's row
first, then create with EXACT property names) | 6 RUN LOG row |
7 STALE-DATA POLICY (unreachable source = FAILED, never fake-fresh)
| 8 NO FABRICATION (link every claim) | 9 APPROVAL BOUNDARY (drafts
only; never bid, buy, publish, send, delete).

## 5. Databases (create-on-first-use; exact property names)

- Grok Task Config: Task Name, Enabled (cb), Sites, Keywords, Extra
- Grok Run Log: Task, Date, Status (OK|PARTIAL|FAILED|CONFIG
  MISSING), Items (num), Notes
- Lot Radar: Name, Site, Link (url), Bid (num), Est. Profit (num),
  Score 1-5, Date Found, Status (New|Watching|Bought|Sold|Skipped)
- Watched Keywords: Keyword, Category, Active (cb), Notes
- Price Reference: Item, Platform, Price (num), Link, Date
- Brand Index: Brand, Category Avg (num), Sample Size (num), Trend
  (Up|Flat|Down), Link, Date
- Content Queue: Title, Status (Queued|Drafted|Scheduled|Published|
  Killed), Type (Long|Short), Hook, Outline, Reference, Date
- Listing Drafts: SKU, Item, Suggested Title, Description, Tags,
  Suggested Price (num), Status, Comp Links
- Social Queue: Post, Platform, Copy, Media Note, Status, Date
- Platform News: Source, Change, Impact, Link, Date
- Competitor Channels: Channel, Video, Views (num), Hook, Link, Date
(Plus one-off pages: Comp Archive, Trend Briefs, Hook Library, Field
Guide, Weekly Digest "Week of YYYY-MM-DD", Site Scorecard, Prompt
Audit - each task creates its page if missing.)

## 6. Operating hacks

1 Config-in-Notion: toggle sites/keywords/off-switch per task without
  touching Grok prompts (Grok Task Config DB).
2 Idempotency: every write checks "row for today exists?" first.
3 Create-if-missing: tasks scaffold their own DB on first run.
4 Run Log = permanent history (Grok keeps only 20 run records).
5 Test-run ritual after every prompt or site change.
6 Schedules pre-staggered >= 15 min (platform needs >= 5).
7 Approval buys/posts stay human; tasks only draft - matches Grok's
  own "design routines for trust" guidance.
8 Stale-data policy: dead sites get logged, never papered over.
9 Publish-to-web trick: publish the config page if another AI
  assistant needs the same live config.
10 Monthly meta-loop: site scorecard (task 48) + prompt audit
  (task 49) read the Run Log and propose fixes for your approval.
11 Custom MCP bridge available later for anything native can't do
  (e.g. auto-push Social Queue to Buffer).
12 Upsy optional when unattended writes need per-action limits.

## 7. Security (the API key)

- Stored at ~/.config/notion/token and ~/.vscode-cline/
  mcp_settings.json (both chmod 600). Never inside these docs.
- It was pasted in plain chat: regenerate it in Notion
  (Settings -> Connections -> integration -> regenerate) after
  setup, update both files, and do not clip/export chats containing
  it.
- Share pages with the integration: "Pre-Owned Jewelry Store OS"
  parent page + "Content Queue" DB (covers Lot Radar + Grok
  Scheduled Tasks).

## 8. Setup ritual per task

1 grok.com/connectors: confirm Notion connected.
2 Create task; name matches file header.
3 Paste the inside of the code block.
4 Set schedule string exactly from the header.
5 Enable web browsing / Agent Tools.
6 Test run once; confirm a Grok Run Log row appeared.
7 Trust the schedule.

## 9. Your Grok inventory (as connected)

Connectors actually used by these tasks:
- Notion: all 49 tasks (config + results).
- Gmail: digest delivery for tasks 44, 47, 49 - emailed to
  tinydigitalproductlab@gmail.com.
- Buffer: task 35 pushes drafts only (never auto-publish); link your
  channels in Buffer first or the task skips the step with a note.
- Google Drive: CSV exports for tasks 18 and 48 into a "Grok Exports"
  folder (created on first run).
Unused by design: HubSpot, Whop (unused unless you sell there - an
order-check task could be added later), Netlify, Vercel, GitHub.

Skills: none of the installed packs (addyosmani, brandkit, caveman-*
family, design-taste, imagegen, ponytail, superpowers, office file
skills) apply directly to these scheduled ops tasks. Options:
- caveman: prepend "respond caveman mode, full intensity" to any task
  prompt for compressed run output.
- Spreadsheets/PDF: use manually on the Drive CSV exports if you want
  formatted reports offline.