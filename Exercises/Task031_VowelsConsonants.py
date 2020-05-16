# Napiš skript, který spočítá kolik samohlásek a souhlásek obsahuje následující string s anglickou větou:
sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

vowels = 'aeiouy'

counts = {'cons' : 0, 'vows' : 0}

for char in sentence:
    if not char.isalpha():
        continue
    
    if char.lower() in vowels:
        counts['vows'] += 1
        
    else:
        counts['cons'] += 1
        
print('Pocet samoshlasek: ' + str(counts['cons']), 'Pocet souhlasek: ' + str(counts['vows']))

# Reseni
# 1.Musíme mít sekvenci samohlásek, kterými rozlišíme souhlásky,
# 2. dále budeme potřebovat slovník, kde budeme nahrávat naše počty,
# 3. smyčku, kterou projdeme string,
# 4. kde nejdříve zkontrolujeme, jestli se jedná o písmeno
#     pokud ano, jdeme na další podmínku
#     pokud ne, přeskakujeme na další písmeno pomocí continue
# 5. dále zkontrolujeme, jestli se jedná o samohlásku,
#     pokud ano, připočítáme písmeno do slovníku pod samohlásky
#     pokud ne, připočítáme písmeno do sllovníku pod souhlásky
# 6. Vytiskneme počty