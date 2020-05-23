from pprint import pprint as pp

ODDELOVAC = '-' * 40
UZIVATELE = {
    'bob' : '123', 
    'ann' : 'pass123', 
    'mike' : 'password123', 
    'liz' : 'pass123'
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# 1. Na začátku přivítá uživatele.
print(ODDELOVAC)
print('Vytejte v aplikaci, prihlaste se prosim: ')
print(ODDELOVAC)

# 2. Vyžádá si od uživatele přihlašovací jméno a heslo. 
jmeno = str(input('Zadejte jmeno:'))
heslo = str(input('Zadejte heslo:'))

# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
if UZIVATELE.get(jmeno) != heslo:
    print('Jmeno nebo heslo neni spravne!')

elif UZIVATELE.get(jmeno) == heslo:
    print('Pokracuji ...')

# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS. 
print(ODDELOVAC)
print('Mame 3 texty k analyze: ')
volba = int(input('Zadejte cislo od 1 do 3 pro vyber: '))
print(ODDELOVAC)

if volba < 1 or volba > 3:
    print("Vami vybrane cislo neni v nabidce, ukoncuji")
    exit()
else:
    vybrany_text = TEXTS[volba - 1]
    
# 5. Pro vybraný text spočítá následující statistiky:
jednotliva_slova = vybrany_text.split()
vycistena_slova = [slovo.strip(".,/") for slovo in vybrany_text.split()]

# - počet slov,
pocet_slov = len(vycistena_slova)
print(f"V textu je: {pocet_slov}, slov celkem.")

zacina_velkymi = int(0)
psano_velkymi = int(0)
psano_malymi = int(0)
cisla = int(0)
soucet = int(0)

for slova in vycistena_slova:
    if slova.isnumeric():
        cisla += 1
        soucet += int(slova)
    elif slova.istitle():
        zacina_velkymi += 1 
    elif slova.isupper():
        psano_velkymi += 1 
    elif slova.islower():
        psano_malymi += 1


# - počet slov začínajících velkým písmenem, .title()
print(f"V textu je: {zacina_velkymi}, slov zacinajicich velkymi pismeny.")

# - počet slov psaných velkými písmeny, .isupper()
print(f"V textu je: {psano_velkymi}, slov psanych velkymi pismeny.")

# - počet slov psaných malými písmeny, .islower()
print(f"V textu je: {psano_malymi}, slov psanych malymi pismeny.")

# - počet čísel (ne cifer!). .isnumeric()
print(f"V textu je: {cisla}, cisel")

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 
delky_slov = {}
for delka in sorted(vycistena_slova, key=len, reverse=True):
     delky_slov[len(delka)] = delky_slov.setdefault(len(delka), 0) +1

nejscastejsi = sorted(delky_slov, key=delky_slov.get, reverse=True)

for  index, _ in enumerate(range(len(nejscastejsi), 0, -1), 1):
    print(ODDELOVAC)

    for slovo  in nejscastejsi:
        print(f"Delka: {slovo}, Vyskyt: {delky_slov[slovo]}x")
        nejscastejsi.remove(slovo)
        break

# 7. Program spočítá součet všech čísel (ne cifer!) v textu.
print(ODDELOVAC)
print(f"Soucet cisel ve vybranem textu je: {soucet}")
print(ODDELOVAC)
