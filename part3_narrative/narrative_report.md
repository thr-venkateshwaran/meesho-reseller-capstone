# Narrative Report

## 3.2 — Worked Narratives

### Narrative 1: Ethnic Wear — April to May

**Context:** This measures Ethnic Wear category revenue, comparing April 2026 to May 2026.

**Insight (FACT):** Ethnic Wear revenue moved from INR 104,520.77 in April to 
INR 185,107.61 in May, a Month-on-Month growth of +77.1%. This exceeds the 8% 
flagging threshold and is marked "flagged."

**Implication (HYPOTHESIS):** This sharp increase may be linked to a seasonal 
or promotional event in May. Recommendation: the regional team should check 
whether a specific promotion, festival-season demand, or new reseller onboarding 
drove this spike, and if confirmed, consider replicating the same promotional 
timing in future cycles for this category.

**Self-score against refinement checklist:**
- Specificity: Passes — names the exact category (Ethnic Wear), exact months 
  (April, May), and exact figures (104520.77, 185107.61, 77.1%).
- Audience fit: Passes — written in plain business language with no technical 
  jargon (no SQL, no code terms), suitable for a regional manager.
- Completeness: Passes — all three sections (Context, Insight, Implication) 
  are present and each is fully stated.
- Actionability: Passes — the implication names a specific next step (check 
  for a promotion/festival/onboarding cause) rather than a vague "look into it."

### Narrative 2: Ethnic Wear — May to June

**Context:** This measures Ethnic Wear category revenue, comparing May 2026 to June 2026.

**Insight (FACT):** Ethnic Wear revenue moved from INR 185,107.61 in May to 
INR 76,371.53 in June, a Month-on-Month growth of -58.74%. This exceeds the 8% 
flagging threshold in the negative direction and is marked "flagged."

**Implication (HYPOTHESIS):** This steep drop may indicate that the May spike 
was a one-time seasonal event that did not sustain into June, or that a key 
reseller reduced their Ethnic Wear orders. Recommendation: the regional team 
should pull reseller-level Ethnic Wear order counts for June specifically, to 
identify whether the drop is concentrated in a few resellers or spread evenly, 
before deciding on any corrective action.

**Self-score against refinement checklist:**
- Specificity: Passes — names the exact category, exact months, and exact 
  figures (185107.61, 76371.53, -58.74%).
- Audience fit: Passes — business language, no technical terms, readable by 
  a non-technical regional manager.
- Completeness: Passes — Context, Insight, and Implication are all present.
- Actionability: Passes — recommends a specific diagnostic step (pull 
  reseller-level order counts) rather than a generic suggestion.

## 3.3 — Chart-Choice Justification
### Question 1: Which month had the highest total revenue?
(April = INR 419,417.43, May = INR 444,594.25, June = INR 398,055.24)

**Chart type: Bar chart** (univariate — one variable, revenue, across three 
categories/months). A bar chart is the right choice because the message — "May 
is highest" — needs to be clear within 10 seconds, and bar height comparison 
is the fastest way for a reader to judge which of three values is largest. 
The y-axis will start at zero so the bar heights are not visually distorted, 
and no 3D effect will be used since 3D bars make exact height comparison harder, 
not easier. A legend is not needed since there is only one data series (revenue).

### Question 2: What percentage share does Ethnic Wear represent of April's total revenue?
(INR 104,520.77 of INR 419,417.43 = 24.92%)

**Chart type: Pie chart (or 100% stacked bar as an alternative)** — this is a 
part-to-whole question (one category's share of one total), which is exactly 
what a pie chart is designed to show. Since there is only one category being 
highlighted against "the rest," the message (Ethnic Wear is roughly a quarter 
of April's revenue) is readable within 10 seconds without needing precise 
angle-reading. A legend is used here since there are two segments (Ethnic 
Wear vs. all other categories combined).

### Question 3: How do the four regions compare on total revenue?
(North/South/East/West figures from Part 1)

**Chart type: Bar chart** (univariate — one variable, revenue, across four 
region categories). Same reasoning as Question 1: bar charts let a reader 
rank four values by height almost instantly, which a pie chart would not do 
as clearly once there are four roughly similar-sized segments. The y-axis 
starts at zero, no 3D is used, and no legend is needed since there is a single 
series (revenue) with region names labeled directly on the x-axis.

## 3.4 — Top Reseller Narrative (Masked)

The top-performing reseller in the West region recorded a total spend of 
INR 75,295.09, the highest among all resellers tracked in this period. 
This reseller is referenced here as ALIAS-19, in line with the masking 
policy that prevents raw reseller names from appearing in any 
external-facing summary.

**Masking verification:** `assert_no_raw_names_leak()` was run on the 
paragraph above, confirming it returns `True` — no raw reseller name 
appears in this text. A negative-case test (same paragraph with "Mumbai 
Reseller 1" substituted for "ALIAS-19") was also run and confirmed to 
return `False`, verifying the checker correctly detects a leak when one 
is present.