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
    print('Muzete pokracovat.')

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
for slova in vybrany_text:
    jednotliva_slova = vybrany_text.split()
    vycistena_slova = [slovo.strip(".,/") for slovo in vybrany_text.split()]

# - počet slov,
pocet_slov = len(vycistena_slova)
print(f"Pocet slov ve vybranem textu je: {pocet_slov}")

pocet_velkych = 0
pocet_velkymi = 0
pocet_malymi = 0
pocet_cisel = 0

for slovo in vycistena_slova:
    sum(slovo.title)
    

# for slova in vycistena_slova:
#     if slova.title():
#         pocet_velkych += 1
#     elif slova.isupper():
#         pocet_velkymi += 1
#     elif slova.islower():
#         pocet_malymi += 1
#     elif slova.isnumeric():
#         pocet_cisel += 1
    
# - počet slov začínajících velkým písmenem, .title()
print(f"Pocet slov zacinajicich velkymi pismeny je: {pocet_velkych}")

# - počet slov psaných velkými písmeny, .isupper()
print(f"Pocet slov psanych velkymi pismeny je: {pocet_velkymi}")

# - počet slov psaných malými písmeny, .islower()
print(f"Pocet slov psanych malymi pismeny je: {pocet_malymi}")

# - počet čísel (ne cifer!). .isnumeric()
print(f"Pocet cisel je: {pocet_cisel}")

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

# 7. Program spočítá součet všech čísel (ne cifer!) v textu.