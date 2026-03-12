Izdevumu izsekotājs:
Komandrindas Python lietojums personīgo izdevumu uzskaitei un analīzei.


Uzstādīšana:

    git clone https://github.com/krispits/expense_tracker.git
    cd expense_tracker
    python expense_tracker/app.py

    Nav nepieciešamas papildus bibliotēkas — tikai Python 3.10+.


Programma darbojas interaktīvā režīmā ar izvēlni:

1) Pievienot izdevumu — ievada datumu, kategoriju, summu un aprakstu. Datumu var ievadīt formātā YYYY-MM-DD vai YYYY.MM.DD.
2) Parādīt izdevumus — rāda visus ierakstus formatētā tabulā ar kopsummu.
3) Filtrēt pēc mēneša — izvēlies mēnesi no pieejamajiem un redzi tikai tā izdevumus.
4) Kopsavilkums pa kategorijām — rāda cik iztērēts katrā kategorijā.
5) Dzēst izdevumu — izvēlies ierakstu pēc numura vai ievadi ALL lai dzēstu visus.
6) Eksportēt CSV — eksportē izdevumus CSV failā pēc kategorijas, mēneša vai visus.
7) Iziet - izslēdz programmu

Projekta struktūra
expense_tracker/
├── app.py        # Galvenā programma
├── storage.py    # JSON datu lasīšana un rakstīšana
├── logic.py      # Biznesa loģika
├── export.py     # CSV eksports
└── expenses.json # Dati (izveidojas automātiski)
docs/
├── plan.md       # Projekta plāns
└── DEVLOG.md     # Izstrādes žurnāls
README.md




Autors
Kristaps Ezeriņš — FITA studiju ietvaros "Programmēšanas pamati", 2026