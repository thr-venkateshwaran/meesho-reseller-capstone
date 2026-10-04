import csv
def mom_growth(previous, current):
    return round((current - previous) / previous * 100, 2)

def is_flagged(mom_pct, threshold=8.0):
    if abs(mom_pct) > threshold:
        return "flagged"
    elif abs(mom_pct) < threshold:
        return "not_flagged"
    else:
        return "escalate_exact_boundary"

def validate_feed(csv_path):
    errors = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            month = row.get("month", "").strip()
            category = row.get("category", "").strip()
            revenue_str = row.get("revenue", "").strip()

            if category == "":
                errors.append(f"line {i}: missing category (month={month})")
                continue
            if revenue_str == "":
                errors.append(f"line {i}: missing revenue (category={category})")
                continue
            try:
                revenue = float(revenue_str)
            except ValueError:
                errors.append(f"line {i}: revenue not numeric: {revenue_str!r}")
                continue
            if revenue < 0:
                errors.append(f"line {i}: negative revenue ({revenue}) for category={category}")

    if len(errors) == 0:
        return (True, [])
    else:
        return (False, errors)