import csv
import os

def export_to_csv(expenses, filename):
    """Eksportē izdevumus CSV faila."""
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
        for expense in expenses:
            writer.writerow([
                expense["date"],
                f"{expense['amount']:.2f}",
                expense["category"],
                expense["description"],
            ])