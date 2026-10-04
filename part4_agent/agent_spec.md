# Agent Specification — Meesho Category Growth Monitor

## Goal
Keep Meesho category managers informed of any category whose Month-on-Month 
revenue moves beyond the 8% threshold, with a human approving every message 
before it goes out.

## Tools
- `validate_feed` (Part 2) — checks the incoming CSV for missing/invalid data 
  before any calculation runs.
- `mom_growth` (Part 2) — computes Month-on-Month growth percentage for each category.
- `is_flagged` (Part 2) — classifies each category's growth as flagged, 
  not_flagged, or escalate_exact_boundary.
- Prompt-pack template-fill (Part 3) — turns a flagged category's numbers into 
  a Context → Insight → Implication draft message.

## Memory / State
The agent must remember the previous month's revenue per category, so that 
the next run can compute that month's MoM growth against it. In this mock 
runner, this is supplied directly as the `previous_month_csv` input rather 
than stored persistently, but in a real deployment this would be the one 
piece of state carried between runs.

## Planner
See the 8-step ordered subtask list in section 4.2 of the project brief: 
load and validate the feed, compute growth for every category, flag them, 
sort by magnitude, draft messages for the top 3, log the rest as suppressed, 
log any exact-boundary category separately, and emit one JSON result.

## Feedback Loop
No message is ever sent automatically. Every drafted message is held with 
`drafted = true` in the output JSON, simulating a queue that a human category 
manager must review and approve before anything is actually sent. This 
project does not implement real sending (no email/SMTP integration) — the 
feedback loop is simulated entirely as this approval flag.

## Guardrails

**Input guardrail:** `validate_feed` must pass (return `True`) before any 
other step runs. If it fails, the run stops immediately.

**Action guardrail:** No message is ever auto-sent. Every output is a draft 
held for human approval — this is enforced by the `drafted` flag never 
triggering any send action in this codebase.

**Output guardrail:** Every number inside a drafted message must trace back 
to a value computed in Part 1 or Part 2 (revenue figures from the feed, or 
the `mom_pct` computed by `mom_growth`). No number is invented.

## Success and Error Stopping Conditions
- **Success:** Drafts are produced for flagged categories (or zero drafts, 
  correctly, if nothing crossed the threshold), and every number in every 
  draft is traceable to Part 1/Part 2 values.
- **Error (Hard Stop):** `validate_feed` returns `False`. The run stops 
  immediately, surfaces the validation errors, and does not attempt any 
  growth calculation. This is a Hard Stop, not a silent skip — the error 
  is always visible in the output.

## Given-When-Then Specs (agent-level, reused from Part 2)

1. GIVEN April→May Ethnic Wear revenue moves from 104520.77 to 185107.61, 
   WHEN the agent runs, THEN it computes mom_pct = 77.1 and marks the 
   category "flagged".
2. GIVEN May→June Beauty & Personal Care revenue moves from 35542.11 to 
   37559.07, WHEN the agent runs, THEN it computes mom_pct = 5.67 and marks 
   the category "not_flagged" (no draft produced for it).
3. GIVEN a synthetic pair previous=100000, current=108000 (exactly on the 
   8% boundary), WHEN the agent runs, THEN it computes mom_pct = 8.0 and 
   logs the category into `escalated_categories`, never into 
   `flagged_categories` or treated as `not_flagged`.
4. GIVEN the corrupted feed fixture is used as the current-month input, 
   WHEN the agent runs, THEN `validate_feed` returns `False` with exactly 
   3 errors, and the agent performs a Hard Stop — `validation_status` = 
   "invalid", `action_taken` = "hard_stop", and no growth computation or 
   drafting is attempted.