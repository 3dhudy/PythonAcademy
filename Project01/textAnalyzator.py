from pprint import pprint as pp

oddelovac = '=' * 40
uvivatele = {
    'bob' : '123', 
    'ann' : 'pass123', 
    'mike' : 'password123', 
    'liz' : 'pass123'
}

# 1. Na začátku přivítá uživatele.
print(oddelovac)
print('Vytejte v aplikaci, prihlaste se prosim: ')
print(oddelovac)

# 2. Vyžádá si od uživatele přihlašovací jméno a heslo. 
jmeno = str(input('Zadejte jmeno: '))
heslo = str(input('Zadejte heslo: '))

# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.


# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS. 


# 5. Pro vybraný text spočítá následující statistiky:
# - počet slov,
# - počet slov začínajících velkým písmenem,
# - počet slov psaných velkými písmeny,
# - počet slov psaných malými písmeny,
# - počet čísel (ne cifer!).

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

# 7. Program spočítá součet všech čísel (ne cifer!) v textu.