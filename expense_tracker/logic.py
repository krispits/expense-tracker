from datetime import datetime

def sum_total(expenses):
    """Atgriez visu izdevumu kopsummu."""
    return round(sum(expense["amount"] for expense in expenses), 2)

def filter_by_month(expenses, year, month):
    """Atgriez izdevumus tikai no noradita menesa."""
    result = []
    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            result.append(expense)
    return result

def sum_by_category(expenses):
    """Atgriez vardnicu: {kategorija: summa}."""
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        totals[cat] = totals.get(cat, 0) + expense["amount"]
    return {cat: round(total, 2) for cat, total in totals.items()}

def get_available_months(expenses):
    """Atgriez sarakstu ar menesiem, kuros ir ieraksti."""
    months = set()
    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        months.add((d.year, d.month))
    return sorted(months)