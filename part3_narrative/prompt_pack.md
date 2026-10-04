# Prompt Pack — Flagged Category Stakeholder Update

## Trigger
This prompt runs whenever a category's `is_flagged` result equals "flagged" — 
meaning its Month-on-Month (MoM) revenue growth has moved beyond the 8% threshold 
in either direction (increase or decrease).

## Input List
- {category} — the product category name (e.g. "Ethnic Wear")
- {prev_month} — the earlier month being compared (e.g. "April")
- {month} — the current month being compared (e.g. "May")
- {previous_revenue} — revenue for {prev_month}
- {current_revenue} — revenue for {month}
- {mom_pct} — the calculated MoM growth percentage

## Prompt
You are writing a short update for a regional manager. Using ONLY the values 
supplied below, write a narrative in three parts — Context, Insight, Implication.

Context: [State what is being measured — {category} revenue, comparing {prev_month} 
to {month}.]
Insight: [State the fact — revenue moved from {previous_revenue} to {current_revenue}, 
a {mom_pct}% change. Label this explicitly as a FACT.]
Implication: [Give one specific, actionable next step. If you propose a reason WHY 
this happened, label it explicitly as a HYPOTHESIS, since the data alone does not 
prove causation.]

Rules:
- Never state a number that is not one of the supplied placeholder values above.
- Do not invent causes, reseller names, or events not present in the input.
- Keep the tone factual and business-appropriate for a regional manager audience.

## Checklist (run before using the output)
1. Does every number in the draft match a supplied placeholder value exactly?
2. Is every claim labeled as either FACT or HYPOTHESIS?
3. Is the recommendation specific and actionable (not a vague "look into this")?
4. Is any reseller referenced only by coded alias (ALIAS-XX), never by raw name?