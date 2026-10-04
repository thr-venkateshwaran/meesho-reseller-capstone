def alias_for(reseller_id):
    return f"ALIAS-{reseller_id[3:]}"

def assert_no_raw_names_leak(text, reseller_names):
    for name in reseller_names:
        if name in text:
            return False
    return True
# Positive test
print(alias_for("RS019"))   # expect ALIAS-19
print(alias_for("RS006"))   # expect ALIAS-06

# Negative-case test
sample_text = "The top reseller, Mumbai Reseller 1, drove significant growth."
print(assert_no_raw_names_leak(sample_text, ["Mumbai Reseller 1"]))  # expect False

# Masked version
masked_text = "The top reseller (ALIAS-19) drove significant growth."
print(assert_no_raw_names_leak(masked_text, ["Mumbai Reseller 1"]))  # expect True