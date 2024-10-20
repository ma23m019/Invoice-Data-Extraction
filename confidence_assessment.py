# confidence_assessment

import re

def confidence_score(value, field):
    if value == "N/A":
        return 0
    if field == "Invoice Number":
        return 90 if re.match(r"INV-\d+", value) else 50
    if field == "Invoice Date" or field == "Due Date":
        return 85 if re.match(r"\d{2} \w+ \d{4}", value) else 50
    if field == "Total Amount" or field == "Taxable Amount":
        return 95 if re.match(r"[\d,.]+", value) else 50
    return 80
