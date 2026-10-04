from growth_engine import mom_growth, is_flagged, validate_feed

# GWT 1: Ethnic Wear April to May
g1 = mom_growth(104520.77, 185107.61)
assert g1 == 77.1
assert is_flagged(g1) == "flagged"

# GWT 2: Beauty & Personal Care May to June
g2 = mom_growth(35542.11, 37559.07)
assert g2 == 5.67
assert is_flagged(g2) == "not_flagged"

# GWT 3: exact boundary
g3 = mom_growth(100000, 108000)
assert g3 == 8.0
assert is_flagged(g3) == "escalate_exact_boundary"

# GWT 4: corrupted feed
ok, errors = validate_feed("part2_engine/fixtures/corrupted_feed.csv")
assert ok == False
assert len(errors) == 3
assert errors[0] == "line 3: negative revenue (-4200.0) for category=Western Wear"
assert errors[1] == "line 4: missing category (month=July)"
assert errors[2] == "line 6: missing revenue (category=Home & Kitchen)"

# Clean feed passes
ok2, errors2 = validate_feed("part2_engine/fixtures/monthly_category_revenue.csv")
assert ok2 == True
assert errors2 == []

print("All GWT tests passed!")