from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months
from datetime import date, datetime

CATEGORIES = [
    "Ediens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]

def show_menu():
    """Parāda galveno izveli un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Paradīt izdevumus")
    print("3) Filtrēt pec mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """Ievada jaunu izdevumu / validācija."""
    today = date.today().strftime("%Y-%m-%d")
    while True:
        date_input = input(f"Datums (YYYY-MM-DD vai DD.MM.YYYY) vai enter [{today}] (0 - atpakal): ") or today
        if date_input == "0":
            return
        try:
            if "." in date_input:
                date_input = datetime.strptime(date_input, "%d.%m.%Y").strftime("%Y-%m-%d")
            else:
                datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Nepareizs datums. Ievadi formata YYYY-MM-DD vai DD.MM.YYYY")

    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")

    while True:
        cat_input = input("Izvēlies (1-7) (0 - atpakal): ")
        if cat_input == "0":
            return
        try:
            cat_index = int(cat_input) - 1
            if 0 <= cat_index < len(CATEGORIES):
                category = CATEGORIES[cat_index]
                break
            else:
                print("Ievadi skaitli no 1 lidz 7.")
        except ValueError:
            print("Ievadi skaitli no 1 lidz 7.")

    while True:
        amount_input = input("Summa (EUR) (0 - atpakal): ")
        if amount_input == "0":
            return
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Summai jābut pozitīvam skaitlim.")
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

def filter_menu(expenses):
    """Rada pieejamos menesus, filtre un izvada."""
    if not expenses:
        print("Nav ierakstu.")
        return
    months = get_available_months(expenses)
    print("\nPieejamie menesi:")
    for i, (year, month) in enumerate(months, 1):
        print(f"  {i}) {year}-{month:02d}")
    while True:
        choice = input("Izvēlies menesi (0 - atpakal): ")
        if choice == "0":
            return
        try:
            index = int(choice) - 1
            if 0 <= index < len(months):
                year, month = months[index]
                filtered = filter_by_month(expenses, year, month)
                show_expenses(filtered)
                break
            else:
                print(f"Ievadi skaitli no 1 lidz {len(months)}.")
        except ValueError:
            print(f"Ievadi skaitli no 1 lidz {len(months)}.")

def category_summary(expenses):
    """Rada kopsavilkumu pa kategorijam."""
    if not expenses:
        print("Nav ierakstu.")
        return
    totals = sum_by_category(expenses)
    print(f"\n{'Kategorija':<20} {'Summa':>10}")
    print("-" * 32)
    for cat, total in totals.items():
        print(f"{cat:<20} {total:>8.2f} EUR")
    print("-" * 32)
    print(f"{'Kopa:':<20} {sum_total(expenses):>8.2f} EUR")

def delete_expense(expenses):
    """Numerēts saraksts, lietotājs izvelas dzēšamo."""
    if not expenses:
        print("Nav ko dzēst.")
        return
    print("\nIzdevumi:")
    for i, exp in enumerate(expenses, 1):
        print(f"  {i}) {exp['date']} | {exp['amount']:.2f} EUR | {exp['category']} | {exp['description']}")
    while True:
        choice = input("Kuru dzēst? (numurs vai 0 - atpakaļ): ")
        if choice == "0":
            return
        try:
            index = int(choice) - 1
            if 0 <= index < len(expenses):
                removed = expenses.pop(index)
                save_expenses(expenses)
                print(f"Dzests: {removed['date']} | {removed['amount']:.2f} EUR | {removed['category']} | {removed['description']}")
                break
            else:
                print(f"Ievadi skaitli no 1 lidz {len(expenses)}.")
        except ValueError:
            print(f"Ievadi skaitli no 1 lidz {len(expenses)}.")

def main():
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            filter_menu(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "7":
            print("Programma ir izslēgta, uz redzēšanos!")
            break

if __name__ == "__main__":
    main()