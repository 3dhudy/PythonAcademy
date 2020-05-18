"""Lekce #9 - Uvod do programovani, kontrola cisel"""
from pprint import pprint as pp
from typing import List

# I. KROK
# Vytvoreni hlavni funkce
def main() -> None:
    nactena_cisla = nacitani_udaju("Lesson09/numbers.txt")
    ostripovana_data = ocisti_udaje(nactena_cisla)
    zkontroluj_typ_udaju(ostripovana_data)

# II. KROK
# Potrebujeme nacist soubor s udaji
def nacitani_udaju(soubor) -> list():
    with open(soubor, "r") as txt:
        return txt.readlines()

# III. KROK
# Ciselne udaje zbavime symbolu pro novy radek "\n"
def ocisti_udaje(neupravene) -> list(): 
    return [naformatuj_data(radek.strip()) for radek in neupravene]

# IV. KROK
# Udaj naformatovat dle dohodnuteho vzoru
def naformatuj_data(udaj: str) -> str():
    return f"UDAJ: {udaj}, TYPE: {type(udaj)}"

# V. KROK
# Kontrolujeme spravny vstupni datovy typ
def zkontroluj_typ_udaju(upravene):
    overene_udaje = []

    while upravene:
        try:
            vyber_cislo = upravene.pop().split()[1][:-1]
            prevedeni_hodnoty = int(vyber_cislo)
        
        except ValueError as ve:
            print(f"NEKONVERTOATELNE --> {vyber_cislo}, {ve.__class__.__name__}")

        else:
            print(f"{vyber_cislo} --> OK, pokracuji ...")
            overene_udaje.append(prevedeni_hodnoty)

        finally:
            print("-" * 39)

# VI. KROK
# Napiseme funkci, ktera bude chtit zkontrolovat typ kazdeho detailu
# Pokud je to cislo, melo by byt zmenitelne pomoci funkce int()

# ad. I. KROK
main()