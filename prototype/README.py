def mandatory_status(licence_held_by_bidder, wsib_clearance, liability_insurance_cad):
    checks = [licence_held_by_bidder is True,
              wsib_clearance is True,
              liability_insurance_cad is not None and liability_insurance_cad >= 5_000_000]
    if any(value is False for value in checks):
        return "ineligible"
    if not all(value is True for value in checks):
        return "flagged"
    return "eligible"

if __name__ == "__main__":
    print("Starter only: connect validated, human-reviewed extraction data before scoring.")
