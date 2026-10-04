# Meesho Reseller Growth & Alert Intelligence Pipeline

A 4-part data pipeline that generates a seeded Meesho reseller dataset, 
answers business questions with SQL, computes Month-on-Month growth with 
guardrails, turns flagged results into stakeholder-ready narratives, and 
ties it all together in a guarded mock agent runner — with zero paid 
services or API keys required anywhere in the pipeline.

## Requirements
- Python 3.x (no external packages beyond the standard library — sqlite3, 
  csv, json are all built in)

## How to Run (in order)

### Step 0 — Generate the dataset

python data/generate_dataset.py

This creates `data/meesho_reseller.db`, `data/orders.csv`, and 
`data/resellers.csv` using a fixed random seed (42), so output is identical 
on every run.

### Part 1 — SQL Business Query Engine

python part1_sql/queries.py

Runs all 5 required SQL queries (monthly category revenue, region-wise 
revenue, top resellers >50000 spend, zero-order reseller via LEFT JOIN, 
June Delivered AOV) and saves outputs to `part1_sql/output/`.

### Part 2 — Python Guardrail & Growth-Detection Engine

python part2_engine/test_growth_engine.py

Runs all 4 Given-When-Then unit tests against `growth_engine.py`'s 
`mom_growth`, `is_flagged`, and `validate_feed` functions. Prints 
"All GWT tests passed!" on success.

### Part 3 — AI Narrative & Prompt-Pack Report

python part3_narrative/masking.py

Runs the masking policy tests (`alias_for`, `assert_no_raw_names_leak`). 
The written narrative content is in `part3_narrative/prompt_pack.md` and 
`part3_narrative/narrative_report.md` (read, not run).

### Part 4 — Agentic Workflow + Mock Agent Runner

python part4_agent/mock_agent_runner.py

Runs the mock agent across three scenarios (May, June, and a corrupted 
feed) and prints the structured JSON output for each. The agent spec is 
documented in `part4_agent/agent_spec.md`.

## Zero-API-Key Confirmation
This entire pipeline runs offline with no API keys, no paid services, and 
no network calls. All narrative generation (Part 3) uses a template-fill 
approach — placeholders filled from Part 1/Part 2's verified numbers — not 
a live AI API call. The `part4_agent/mock_agent_runner.py` similarly drafts 
and holds messages locally; nothing is sent over a network.

## Project Structure and Workflow Pattern Mapping
- **Part 1 (`part1_sql/`)** — SQL Business Query Engine. Pattern: data 
  retrieval and aggregation (GROUP BY, JOIN, LEFT JOIN).
- **Part 2 (`part2_engine/`)** — Guardrail & Growth-Detection Engine. 
  Pattern: input validation guardrail + business-rule classification 
  (flagged/not_flagged/escalate_exact_boundary).
- **Part 3 (`part3_narrative/`)** — Reliable AI Narrative & Prompt-Pack. 
  Pattern: reusable prompt template with a validation checklist, plus a 
  data-masking guardrail (no raw names leak).
- **Part 4 (`part4_agent/`)** — Agentic Workflow Spec + Mock Agent Runner. 
  Pattern: full agentic loop — Goal, Tools, Memory, Planner, Feedback Loop 
  — with Input/Action/Output guardrails and a human-approval checkpoint 
  before any message is considered sent.

## Author
Built by Thiru as part of an AI analytics capstone project.