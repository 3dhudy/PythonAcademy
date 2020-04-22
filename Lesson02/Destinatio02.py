# ~~~~~~~~~~~~~~~~~~~ZAPIS Z LEKCE #01~~~~~~~~~~~~~~~~~~~
...

#!/usr/bin/env python3
""" Lekce #1 - Uvod do programovani, 1/2 Destinatio """

# I. KROK:
# Definujeme promenne, se kterymi chceme pracovat
MESTA = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# II. KROK:
# Pozdravime uzivatele a doplnime oddelovace '='
# Zobrazit uzivateli nasi nabidkou - lokalita | cena
print(ODDELOVAC)
print("Vitejte u nasi aplikace Destinatio!")
print(ODDELOVAC)
print(
    """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)
print(ODDELOVAC)

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstupy
# Cislo destinace, jmeno, prijmeni, rok_narozeni, email, heslo
por_cislo = int(input("Vyberte cislo lokality: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)

# IV. KROK:
# Modifikujeme tyto hodnoty,
destinace = MESTA[por_cislo - 1]
cena = CENY[por_cislo - 1]

# V. KROK:
# Vystupni sekce, vypisujeme konkretni udaje
# Jmeno, destinaci, cenu, email
print("UZIVATEL: " + jmeno)
print("DESTINACE: " + destinace)
print("CENA(cil:" + destinace + "): " + str(cena))
print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")

# ~~~~~~~~~~~~~~~~~~~KONEC ZAPISU Z LEKCE #01~~~~~~~~~~~~~~~~~~~

#!/usr/bin/env python3
""" Lekce #2 - Uvod do programovani, 2/2 Destinatio """


# I. KROK:
# Doplnit zadani (sleva 25%)
SLEVY = ("Olomouc", "Ostrava")

# II. KROK:
# Spravne cislo lokality! Podm. zapis x --> (1, 6)
por_cislo = int(input("Vyberte cislo lokality"))

if por_cislo > 1 or por_cislo < 6:
    print("Cislo neni v nabidce")
else:
    destinace = MESTA[por_cislo - 1]
    cena = CENY[por_cislo - 1]
    print(f"DESTINACE: {destinace}")
    print(ODDELOVAC)

# III. KROK:
# Vyresime pouziti slevy. Membership testing.
if destinace in SLEVY:
    cena_po_sleve = 0.75 * cena
else:
    cena_po_sleve = cena

# IV. KROK:
# Jmeno + prijmeni obsahuje jen pismena

# V. KROK:
# Aktualni rok - datum narozeni >= 18

# VI. KROK:
# Spravny email obsahuje "@"

# VII. KROK:
# Heslo obsahuje jak cisla, tak pismena + delka >= 8
# Zaverecny vystup pro uzivatele


