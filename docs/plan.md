                                A.Programmas apskats.

Izdevumu izsekotājs ir python programma, kas ļauj lietotājam reģistrēt ikdienas izdevumus, grupēt tos pa kategorijām un eksportēt datus CSV failā. Programma ir paredzēta, lai tajā varētu ērti uzskaitīt savus ikdienas tēriņus, sadalīt datus kategorijās kā arī validēt tos.

                                B.Datu struktūra.

{
  "date": "2025-03-10",
  "amount": 1.50,
  "category": "Transports",
  "description": "Autobusa biļete uz darbu"
}

*date - kā virkne "YYYY-MM-DD" lai būtu viegli salīdzināt un filtrēt
*amount - kā skaitlis (float) lai aprēķinus varētu veikt bez konvertēšanas
*category - kā virkne no iepriekšdefinēta saraksta lai atvieglotu grupēšanu
*description - brīva formāta piezīmes, lai lietotājam būtu vieglāk orientēties savās izmaksās

                                C. Moduļu plāns.

storage.py:
    load_expenses() - ielādē sarakstu no expenses.json, ja failu nav - izdod tukšu
    save_expenses() - saglabā jaunus datus expenses.json sarakstā
logic.py:
    sum_total(expenses)
    filter_by_month(expenses, year, month) - atgriež izdevumus no konkrētā mēneša
    sum_by_category(expenses) - atgriež kategorijas summu
    get_available_months(expenses) - atgriež sarakstus ar mēnešiem, kuros ir ieraksts
export.py:
    export_to_csv(expenses, filename) - eksportē datus CSV failā enkodējot UTF-8-sig kodējumā
app.py:
    main() - galvenā cilpa, ielādē datus, rāda izvēlni
    show_menu() - izvada izvēlni, atgriež lietotāja izvēlni
    add_expense() - ievada jaunu izdevumu kā arī validācija
    add_expenses(expenses) - formēti rāda visus izdevumus un kopsummu
    filter_menu(expenses) - rāda pieejamos mēnešus un izvada
    delite_expense(expenses) - saraksts no kura lietotājs var izvēlēties dzēšamo
    export_menu(expenses) - eksportē CSV failu

                                D. Lietotāja scenāriji.

Scenārijs 1 — Izdevuma pievienošana
    Lietotājs palaiž programmu un izvēlas "Pievienot izdevumu". Programma jautā datumu (piedāvā šodienu kā noklusējumu), kategoriju no saraksta, summu un aprakstu. Pēc ievades programma apstiprina: Pievienots: 2025-03-10 | Ēdiens | 5.20 EUR | Saldēta lazanja.
Scenārijs 2 — Mēneša pārskats
    Lietotājs izvēlas  "Filtrēt pēc mēneša". Programma parāda pieejamos mēnešus (2025-02, 2025-03), lietotājs izvēlas vienu, un programma izvada tikai tā mēneša izdevumus ar kopsummu apakšā.
Scenārijs 3 — Nepareiza ievade
    Lietotājs laukā "Summa" ieraksta "divi". Programma neapstājas — tā parāda kļūdas paziņojumu "Summai jābūt pozitīvam skaitlim". un ļauj mēģināt vēlreiz.

                                E. Robežgadījumi

Saraksts ir tukšs (parādīt) - izvada "Nav ierakstu" un atgriež izvēlnē
Saraksts ir tukšs (dzēst) - izvada "Nav dzēšamo failu" un atgriež izvēlnē
Nederīgu datu ievade - pieprasa ievadīt vēlreiz / piedāvā iespēju atgriesties izvēlnē