def calculate_total(price, tax):
    total = price + tax
    if total > 100:
        total = total - 10
    return total


def calculate_invoice(price, tax):
    # ❌ duplicated logic (radon + maintainability)
    total = price + tax
    if total > 100:
        total = total - 10
    return total
