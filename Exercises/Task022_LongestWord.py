# Napiš program, který přjme jako vstup list se slovy a vytiskne do terminálu tuple s nejdelším slovem a jeho délkou.

slova = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
         
nejdelsi_slovo = ('', 0)

while slova:
    slovo = slova.pop(0)
    if len(slovo) > nejdelsi_slovo[1]:
        nejdelsi_slovo = slovo, len(slovo)
        
print(nejdelsi_slovo)

# Reseni:

# Naším cílem je iterovat listem a uchovávat nejdelší zjištěnou délku slova.
# Jakmile narazíme na delší slovo, měli bychom ho uložit a přepsat maximální zjištěnou délku.
# 1. Rozhodli jsme se uchovat nejdelší slovo a jeho déllku v tuplu.
# Kdykoliv narazíme na delší slovo, změníme i data uvnitř tuplu (nejdelsi_slovo, delka_slova). Uvnitř smyčky while můžeme tedy opakovat následující:
# 2. Vzít slovo ze začátku listu, 3. Zkontrolovat, jestli je slovo dosud nejdelší, 4. Pokud ano, uložíme ho i s jeho délkou do tuplu. 
# Nemusíme data uzavírat do závorek, python automaticky rozpozná objekt jako tuple, když je oddělený čárkou.
# 5. Nakonec pouze vytiskneme výsledný tupl.