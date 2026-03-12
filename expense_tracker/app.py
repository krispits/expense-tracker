from storage import load_expenses, save_expenses
from logic import filter_by_month, sum_total, sum_by_category, get_available_months
from datetime import date

CATEGORIES = [
    "Ediens",
    "Transports",
    "Izklaide",
    "Komunalie maksajumi",
    "Veseliba",
    "Iepirksanas",
    "Cits",
]

def show_menu():
    """Parada galveno izveli un atgriez lietotaja izveli."""
    print("\n1) Pievienot izdevumu")
    print("2) Paradīt izdevumus")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """Ievada jaunu izdevumu ar validaciju."""
    today = date.today().strftime("%Y-%m-%d")
    date_input = input(f"Datums (YYYY-MM-DD) [{today}] (0 - atpakal): ") or today
    if date_input == "0":
        return

    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")
    cat_input = input("Izvēlies (1-7) (0 - atpakal): ")
    if cat_input == "0":
        return
    category = CATEGORIES[int(cat_input) - 1]

    while True:
        amount_input = input("Summa (EUR) (0 - atpakal): ")
        if amount_input == "0":
            return
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Summai jabut pozitivam skaitlim.")
                continue
            break
        except ValueError:
            print("Ievadi skaitli, piemeram: 12.50")

    description = input("Apraksts (0 - atpakal): ")
    if description == "0":
        return

    expense = {
        "date": date_input,
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")

def show_expenses(expenses):
    """Formateti rada visus izdevumus un kopsummu."""
    if not expenses:
        print("Nav ierakstu.")
        return
    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<20} {'Apraksts'}")
    print("-" * 55)
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['amount']:>8.2f} EUR {exp['category']:<20} {exp['description']}")
    print("-" * 55)
    print(f"Kopa: {sum_total(expenses):.2f} EUR ({len(expenses)} ieraksti)")

def main():
    """Galvena programmas cilpa."""
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "7":
            print("Uz redzesanos!")
            break

if __name__ == "__main__":
    main()