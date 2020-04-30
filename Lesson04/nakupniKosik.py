#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
from pprint import pprint as pp
# I. KROK
# Vytvorime promenne, se kterymi budeme pracovat
# Nabidku potravin, *POTRAVINY*
# Prazdny slovnik, *KOSIK*
# Oddelovac, *ODDELOVAC*
KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": 30,
    "maso": 100,
    "banan": 30,
    "jogurt": 10,
    "chleb": 20,
    "jablko": 10,
    "pomeranc": 15,
}
# II. KROK
# Vypiseme nabidku potravin a oddelime ji
pp(POTRAVINY)
print(ODDELOVAC)

# III. KROK
# Vlozit 3 potraviny z vyberu do kosiku
# Pomoci input() + metod spojenymi se slovniky
# vyber1 = input("VYBERTE ZBOZI c.1: ")
# vyber2 = input("VYBERTE ZBOZI c.2: ")
# vyber3 = input("VYBERTE ZBOZI c.3: ")
#
# KOSIK[vyber1] = POTRAVINY.get(vyber1, "NENI SKLADEM")
# KOSIK[vyber2] = POTRAVINY.get(vyber2, "NENI SKLADEM")
# KOSIK[vyber3] = POTRAVINY.get(vyber3, "NENI SKLADEM")
#
# print(ODDELOVAC)
# print(KOSIK)
# print(ODDELOVAC)
# print(f"CELKOVA CENA: {sum(KOSIK.values())} CZK")
# IV. KROK
# Zakomentuj predchozi kod!
# Celou ulohu predelame pomoci smycky *while*
# Plnime kosik, dokud v nem nejsou 3 predmety
# while len(KOSIK) < 3:
#     vyber_n = input(f"VYBERTE ZBOZI (AKTUALNI POCET: {len(KOSIK)}): ")
#     KOSIK[vyber_n] = POTRAVINY.get(vyber_n, "NENI SKLADEM")
# V. KROK
# Vytvorim *else* vetev
# Doplnime sumu veskereho zbozi v kosiku
# else:
#     print(ODDELOVAC)
#     print(KOSIK)
#     print(ODDELOVAC)
#     CELKEM = sum(KOSIK.values())
#     print(f"CENA CELKEM: {CELKEM} CZK")
# VI. KROK
# Zakomentuj predchozi kod!
# Aplikujeme nekonecnou smycku
# Koncept *break/continue* statement
# pokracovat = True
#
# while pokracovat:
#     vyber_n = input(f"VYBERTE ZBOZI (AKTUALNI POCET: {len(KOSIK)}): ")
#     if vyber_n not in POTRAVINY.keys():
#         print(f"ZBOZI NENI SKLADEM! --> {vyber_n}")
#         continue
#     else:
#         KOSIK[vyber_n] = POTRAVINY[vyber_n]
#
#     kontrola = input("PRO UKONCENI NAPIS 'q': ")
#     if kontrola == 'q':
#         pokracovat = False
#
# else:
#     print(ODDELOVAC)
#     print(KOSIK)
#     print(ODDELOVAC)
#     CELKEM = sum(KOSIK.values())
#     print(f"CENA CELKEM: {CELKEM} CZK")
# VII. KROK
# Zakomentuj predchozi kod!
# pouziti prirazovaciho operatoru *walrus operator* --> Python 3.8+
while (vyber_n:=input("VYBERTE ZBOZI: ")) != "exit":
    if vyber_n not in POTRAVINY.keys():
        print(f"ZBOZI NENI SKLADEM! --> {vyber_n}")
        continue
    else:
        KOSIK[vyber_n] = POTRAVINY[vyber_n]
else:
    print(ODDELOVAC)
    print(KOSIK)
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(f"CENA CELKEM: {CELKEM} CZK")