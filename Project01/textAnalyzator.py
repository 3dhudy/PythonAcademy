from pprint import pprint as pp

ODDELOVAC = '=' * 40
UZIVATELE = {
    'bob' : '123', 
    'ann' : 'pass123', 
    'mike' : 'password123', 
    'liz' : 'pass123'
}

# TEXTS = 

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


# 5. Pro vybraný text spočítá následující statistiky:
# - počet slov,
# - počet slov začínajících velkým písmenem, .title()
# - počet slov psaných velkými písmeny, .isupper()
# - počet slov psaných malými písmeny, .islower()
# - počet čísel (ne cifer!). .isnumeric()

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

# 7. Program spočítá součet všech čísel (ne cifer!) v textu.