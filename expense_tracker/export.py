from storage import load_expenses, save_expenses
from logic import filter_by_month, sum_total, sum_by_category, get_available_months
from datetime import date

CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]

def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """Ievada jaunu izdevumu ar validāciju."""
    today = date.today().strftime("%Y-%m-%d")
    date_input = input(f"Datums (YYYY-MM-DD) [{today}]: ") or today

    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")
    cat_input = input("Izvēlies (1-7): ")
    category = CATEGORIES[int(cat_input) - 1]

    amount = float(input("Summa (EUR): "))
    description = input("Apraksts: ")

    expense = {
        "date": date_input,
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")

def show_expenses(expenses):
    """Formatēti rāda visus izdevumus un kopsummu."""
    if not expenses:
        print("Nav ierakstu.")
        return
    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<20} {'Apraksts'}")
    print("-" * 55)
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['amount']:>8.2f} EUR {exp['category']:<20} {exp['description']}")
    print("-" * 55)
    print(f"  Kopā: {sum_total(expenses):.2f} EUR ({len(expenses)} ieraksti)")

def main():
    """Galvenā programmas cilpa."""
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "7":
            print("Uz redzēšanos!")
            break

if __name__ == "__main__":
    main()