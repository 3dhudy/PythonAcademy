# Tvým úkolem je napsat kód, který:

# proměnné kandidati přiřadí prázdný list,
# vytiskne obsah proměnné kandidati za větu 'Kandidáti na začátku: ',
# do proměnné zamestnanci přiřadí list, který bude obsahovat stringy: 'František', 'Anna', 'Jakub', 'Klára',
# vytiskne obsah zamestnanci za větu 'Zaměstnanci na začátku: ',
# do prázdného listu kandidáti přidá jména 'Bruno' a 'Anežka',
# vytiskne obsah listu kandidati za string 'Nová jména přidána do kandidati: ',
# vloží jméno 'Bruno', uložené v listu kandidati, do listu zamestnanci na pozici index 1,
# vytiskne obsah proměnné zamestnanci za string: 'Nová jména vložena do zamestnanci:
# Příklad fungujícího kódu:

# Vytvoreni kandidatu
kandidati = []

# Tisk kandidatu na zacatku
print('Kandidáti na začátku: ', str(kandidati))

# Vytvoreni zamestnancu
zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']

# Tisk zamestnancu na zacatku
print('Zaměstnanci na začátku: ', str(zamestnanci))

# Pridani novych kandidatu
kandidati.append('Bruno')
kandidati.append('Anežka')

# Tisk novych kandidatu
print('Nová jména přidána do kandidati: ', str(kandidati))

# Vlozeni jmena
zamestnanci.insert(1, 'Bruno')

# Tisk listu zamestnanci po vlozeni noveho jmena
print('Nová jména vložena do zamestnanci:', str(zamestnanci))