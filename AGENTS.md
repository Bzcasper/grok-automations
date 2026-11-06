# grok-automations — AGENTS.md

Scheduled-task prompt pack for a Grok web account that runs 49 routines against a
Notion workspace via Grok's native Notion connector. **No code, build, or tests.**
Editing here means editing Markdown prompt files.

## Read first
- `README.md` — index of all 49 tasks (file, task name, schedule, connectors).
- `NOTION-GROK-PLAYBOOK.md` — connector facts, the 9-part prompt skeleton,
  exact DB schemas, operating hacks, setup ritual, security.
- `scripts/verify-prompts.py` — lint for the 9-part skeleton and arrow-style
  consistency. Run after editing any task file.
- `.github/workflows/ci.yml` and `.gitlab-ci.yml` — run the same checks in CI
  (skeleton lint, README index, secret scan, markdown lint, link check).

## Layout
- `01-sourcing-auctions/` … `07-weekly-synthesis/` — one folder per category,
  files named `NN-slug.md` (NN = task number 01–49).
- Root `lot-scout.md` / `yt-content-scout.md` are **v1 legacy** prompts,
  superseded by `01/01-lot-scout.md` and `04/25-yt-content-scout.md`. Do not
  edit them as if current.

## Task file shape
Each task file has a header (`Task name`, `Schedule`, `Requires`, `Writes to`)
followed by a single ```text code block pasted into Grok. The block follows the
9-part skeleton: TASK/GOAL → CONFIG → PROCEDURE → CONFIDENCE GATE →
NOTION WRITE → RUN LOG → STALE-DATA POLICY → NO FABRICATION → APPROVAL BOUNDARY.
When adding or editing a task, keep all nine parts and the `CONFIG MISSING`
fallback.

## Gotchas
- **Two task-naming schemes coexist.** Tasks 1–32 use short slugs as the Grok
  task name / Notion `Grok Task Config` row key / Run Log `Task` value
  (e.g. `lot-scout`, `comps-refresh`). Tasks 33–49 use the numbered filename
  slug (e.g. `33-tiktok-trend-scan`). The README index uses short slugs for all.
  Do not "normalize" one to the other without checking whether Notion rows already
  exist under a given key — the key must match the live Grok task name.
- **Files 33–49 include an explicit `Set Task = …` line** in their RUN LOG
  instruction; files 1–32 do not. Match the style of the file you are editing.
- `shopgoodwill.com` is excluded from every sourcing task (covered by the
  separate `sgw-sniper`). Never add it to a Sites default.
- Sourcing tasks share one scoring convention: net = (top comp × 0.6) − (bid +
  buyer premium + shipping), mapped to 1–5 via bands in config Extra (default
  ≥75→5, 40–74→4, 15–39→3, 1–14→2, ≤0 skip); a single comp caps Score at 3.
  Keep these in sync across tasks 01–10 and 11 when editing any one.
- Idempotency: every write checks "row for today exists?" first; never duplicate.
- Stale-data policy: unreachable source/DB = `FAILED` with reason, never
  fake-fresh. Tasks 48–49 write recommendations only; config/prompt changes
  require human approval.
- Approval boundary: discovery and drafts only — never bid, buy, publish, send,
  or delete.
- Platform limits: 50 routines per Bot, 20 recent run records kept, schedules
  must be ≥ 5 minutes apart (this pack staggers ≥ 15 min). "Test run" performs
  real work.

## Secrets
Notion token lives at `~/.config/notion/token` and
`~/.vscode-cline/mcp_settings.json` (both mode 0600). Never put tokens in these
docs. The token was pasted in chat once — regenerate in Notion after setup.

## DB schemas
All exact property names are in playbook §5 (Grok Task Config, Grok Run Log,
Lot Radar, Watched Keywords, Price Reference, Brand Index, Content Queue,
Listing Drafts, Social Queue, Platform News, Competitor Channels, plus one-off
pages). Use those exact names; tasks scaffold DBs on first run if missing.