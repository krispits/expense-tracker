from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months
from datetime import date, datetime
from export import export_to_csv

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
    """Parāda galveno izveli un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pec mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """Ievada jaunu izdevumu / validācija."""
    today = date.today().strftime("%Y-%m-%d")
    while True:
        date_input = input(f"Datums (YYYY-MM-DD) vai enter [{today}] (0 - atpakaļ): ") or today
        if date_input == "0":
            return
        try:
            if "." in date_input:
                date_input = datetime.strptime(date_input, "%Y.%m.%d").strftime("%Y-%m-%d")
            else:
                datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Nepareizs datums. Ievadi formata YYYY-MM-DD vai DD.MM.YYYY")

    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")

    while True:
        cat_input = input("Izvēlies (1-7) (0 - atpakaļ): ")
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
        amount_input = input("Summa (EUR) (0 - atpakaļ): ")
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

    description = input("Apraksts (0 - atpakaļ): ")
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
    """Rāda pieejamos mēnešus, filtrē un izvada."""
    if not expenses:
        print("Nav ierakstu.")
        return
    months = get_available_months(expenses)
    print("\nPieejamie mēneši:")
    for i, (year, month) in enumerate(months, 1):
        print(f"  {i}) {year}-{month:02d}")
    while True:
        choice = input("Izvēlies mēneši (0 - atpakaļ): ")
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
    """Rāda kopsavilkumu pa kategorijām."""
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
        choice = input("Kuru dzēst? (numurs, 0 - atpakaļ, ALL - visu): ")
        if choice == "0":
            return
        if choice.upper() == "ALL":
            confirm = input("Vai tiešam dzēst visus? (j/n): ")
            if confirm.lower() == "j":
                expenses.clear()
                save_expenses(expenses)
                print("Visi izdevumi dzesti.")
            return
def export_menu(expenses):
    """Jautā eksporta veidu un eksporte CSV."""
    if not expenses:
        print("Nav ko eksportēt.")
        return
    print("\n1) Eksportēt pec kategorijas")
    print("2) Eksportēt pec mēneša")
    print("3) Eksportēt visu")
    print("0) Atpakaļ")
    choice = input("\nIzvēlies (0-3): ")
    if choice == "0":
        return
    elif choice == "1":
        print("\nKategorijas:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}) {cat}")
        while True:
            cat_input = input("Izvēlies (1-7) (0 - atpakaļ): ")
            if cat_input == "0":
                return
            try:
                cat_index = int(cat_input) - 1
                if 0 <= cat_index < len(CATEGORIES):
                    category = CATEGORIES[cat_index]
                    filtered = [e for e in expenses if e["category"] == category]
                    break
                else:
                    print("Ievadi skaitli no 1 lidz 7.")
            except ValueError:
                print("Ievadi skaitli no 1 lidz 7.")
    elif choice == "2":
        months = get_available_months(expenses)
        print("\nPieejamie mēneši:")
        for i, (year, month) in enumerate(months, 1):
            print(f"  {i}) {year}-{month:02d}")
        while True:
            month_input = input("Izvēlies saraksta nr  (0 - atpakaļ): ")
            if month_input == "0":
                return
            try:
                index = int(month_input) - 1
                if 0 <= index < len(months):
                    year, month = months[index]
                    filtered = filter_by_month(expenses, year, month)
                    break
                else:
                    print(f"Ievadi skaitli no 1 lidz {len(months)}.")
            except ValueError:
                print(f"Ievadi skaitli no 1 lidz {len(months)}.")
    elif choice == "3":
        filtered = expenses

    else:
        return # nepareiza izvēle, atgriežamies sākuma izvēlnē

    filename = input("Faila nosaukums [izdevumi.csv]: ") or "izdevumi.csv"
    if not filename.endswith(".csv"):
        filename += ".csv"
    export_to_csv(filtered, filename)
    print(f"Eksportets: {len(filtered)} ieraksti -> {filename}")  

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
        elif choice == "6":
            export_menu(expenses)
        elif choice == "7":
            print("Programma ir izslēgta, uz redzēšanos!")
            break

if __name__ == "__main__":
    main()