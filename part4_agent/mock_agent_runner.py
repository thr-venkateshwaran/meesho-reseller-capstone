import sys
sys.path.append("part2_engine")
from growth_engine import mom_growth, is_flagged, validate_feed
import csv

def load_revenue(csv_path):
    revenue = {}
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            revenue[row["category"]] = float(row["revenue"])
    return revenue

def draft_message(category, mom_pct, previous_revenue, current_revenue):
    return (f"{category} revenue moved from {previous_revenue} to {current_revenue}, "
            f"a Month-on-Month change of {mom_pct}%. This exceeds the flagging "
            f"threshold and should be reviewed.")

def run(month, previous_month_csv, current_month_csv):
    result = {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": [],
        "suppressed_categories": [],
        "escalated_categories": [],
        "action_taken": "drafted_and_held_for_approval"
    }

    is_valid, errors = validate_feed(current_month_csv)
    if not is_valid:
        result["validation_status"] = "invalid"
        result["validation_errors"] = errors
        result["action_taken"] = "hard_stop"
        return result

    previous_revenue_map = load_revenue(previous_month_csv)
    current_revenue_map = load_revenue(current_month_csv)

    all_flagged = []
    for category, current_revenue in current_revenue_map.items():
        previous_revenue = previous_revenue_map.get(category)
        if previous_revenue is None:
            continue
        mom_pct = mom_growth(previous_revenue, current_revenue)
        status = is_flagged(mom_pct)
        if status == "flagged":
            all_flagged.append({
                "category": category,
                "mom_pct": mom_pct,
                "previous_revenue": previous_revenue,
                "current_revenue": current_revenue
            })
        elif status == "escalate_exact_boundary":
            result["escalated_categories"].append(category)

    all_flagged.sort(key=lambda x: abs(x["mom_pct"]), reverse=True)

    top3 = all_flagged[:3]
    rest = all_flagged[3:]

    for item in top3:
        message = draft_message(item["category"], item["mom_pct"],
                                 item["previous_revenue"], item["current_revenue"])
        result["flagged_categories"].append({
            "category": item["category"],
            "mom_pct": item["mom_pct"],
            "previous_revenue": item["previous_revenue"],
            "current_revenue": item["current_revenue"],
            "drafted": True,
            "message": message
        })

    for item in rest:
        result["suppressed_categories"].append(item["category"])

    return result
import json

print("=== MAY SCENARIO (April -> May) ===")
result_may = run("May", "part4_agent/fixtures/april_feed.csv", "part4_agent/fixtures/may_feed.csv")
print(json.dumps(result_may, indent=2))

print("\n=== JUNE SCENARIO (May -> June) ===")
result_june = run("June", "part4_agent/fixtures/may_feed.csv", "part4_agent/fixtures/june_feed.csv")
print(json.dumps(result_june, indent=2))

print("\n=== CORRUPTED FEED SCENARIO ===")
result_bad = run("July", "part4_agent/fixtures/june_feed.csv", "part2_engine/fixtures/corrupted_feed.csv")
print(json.dumps(result_bad, indent=2))