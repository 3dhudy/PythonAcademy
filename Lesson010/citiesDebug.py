"""Lekce #10 - Uvod do programovani, debugging"""
from typing import List

# I. KROK - Prochazime soubor radek po radku
def hlavni() -> None:
    obsah_souboru = nacti_udaje("Lesson010/Cities.txt")
    projdi_nactene_udaje(obsah_souboru)

# III. KROK - Ostripujeme jej
def nacti_udaje(jmeno_souboru) -> List[str]:
    try:
        with open(jmeno_souboru, "r") as soubor:
            return soubor.read().split("\n")
    except FileNotFoundError:
        print("Zadny takovy soubor v adresari neni.")

# IV. KROK - Pomoci podminky zastavime ("quit")
def projdi_nactene_udaje(soubor: List[str]) -> None:
    for radek in soubor:
        radek = radek.strip()
        if "quit" == radek.lower():
            return

        zeme, mesto = radek.split(",")
        zeme = zeme.strip()
        mesto = mesto.strip()
        print(zeme.title(), mesto.title(), sep=",")

# V. KROK - Rozdelit stat/mesto
# VI. KROK - Ostripovat
# VII. KROK - Prevest na zadany format
# VIII. KROK - Vypsat spravny vysledek
hlavni()