import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "expenses.json")


def load_expenses():
    """Nolasa expenses.json; ja faila nav vai ir tukss — atgriez tuksu sarakstu."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                save_expenses([])
                return []
            return json.loads(content)
    except FileNotFoundError:
        save_expenses([])
        return []
    except json.JSONDecodeError:
        save_expenses([])
        return []

def save_expenses(expenses):
    """Saglaba izdevumu sarakstu expenses.json."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)