#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Hogwards subjects """
# ~~~~~~~~~~~~~~~~~~~ZADANI ULOHA II~~~~~~~~~~~~~~~~~~~
# Promenne
PREDMETY = (
    'Premenovani',
    'Astronomie',
    'Obrana_proti_cerne_magii',
    'Bylinkarstvi',
    'Lektvary'
)

SKUP_PREMENOVANI = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann', 'Ron', 'Hermiona']
SKUP_ASTRONOMIE = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_OBRANA = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_BYLINKARSTVI = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_LEKTVARY = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']
# ~~~~~~~~~~~~~~~~~~~~KONEC ZADANI~~~~~~~~~~~~~~~~~~~~

# I. KROK
# Vytvorim prazdny slovnik "rozvrh"
from pprint import pprint as pp
ROZVRH = {}

# II. KROK
# Klice slovniku budou stringy z promenne PREDMETY
# Hodnoty klicu jsou seznamy skupin
ROZVRH[PREDMETY[0]] = SKUP_PREMENOVANI
ROZVRH[PREDMETY[1]] = SKUP_ASTRONOMIE
ROZVRH[PREDMETY[2]] = SKUP_OBRANA
ROZVRH[PREDMETY[3]] = SKUP_BYLINKARSTVI
ROZVRH[PREDMETY[4]] = SKUP_LEKTVARY
# pp(ROZVRH)

# III. KROK
# Vytvorime sety studentu v jednotlivych klicich
set_premenovani = set(ROZVRH["Premenovani"])
set_astronomie = set(ROZVRH["Astronomie"])
set_obrana = set(ROZVRH["Obrana_proti_cerne_magii"])
set_bylinkarstvi = set(ROZVRH["Bylinkarstvi"])
se_lektvary = set(ROZVRH["Lektvary"])

# IV. KROK
# Do *set_premenovani* studenta se jmenem *Harry*
set_premenovani.add('Harry')

# Ze setu *set_astronomie* odebereme *Samuel*
set_premenovani.add('Alex')

# V. KROK
# Vypiseme zmeny po pridani/odebrani
print("PRED PRIDANIM STUDENTA: ")
print(ROZVRH["Premenovani"])
print("PO PRIDANI STUDENTA: ")
print(set_premenovani)

# VI. KROK
# Zjistime, kdo navstevuje vsechny predmety
print("Kdo se ucastni vsech predmetu: ")
print(
    set_premenovani &
    set_astronomie &
    set_obrana &
    set_bylinkarstvi &
    se_lektvary
)

# VII. KROK
# bool test na podmnoziny (S.issubset())
# Je vsichni studenti z hodin obrany v hodine premenovani
dotaz_1 = set_obrana.issubset(set_premenovani)
print(f"ODPOVED NA PODMNOZINY --> {dotaz_1}")


# VIII. KROK
# S.isdisjoint()
# Jsou studenti v prom. *NOVI_STUDENTI* uplne odlisne hodnoty
NOVI_STUDENTI = {"Matous", "Monika", "Aneta"}
dotaz_2 = NOVI_STUDENTI.isdisjoint(set_astronomie)
print(f"ODPOVED NA DISJUNKCI --> {dotaz_2}")