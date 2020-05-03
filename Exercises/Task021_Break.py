# Tvým úkolem bude napsat skript, který nechá uživatele hádat slovo z tříčlenného listu 'ovoce'. Uživatel má 2 pokusy na odpověď, jinak prohrál.
# Na řádku 2, 3, a 4 je předepsaný kód, který pomocí importu modulu random a jeho metody .choice() vybere z listu 'ovoce' náhodné slovo. 
# Tomotu se říká 'importing' a probírá se v pokročilejších kurzech. Ty nyní potřebuješ vědět, že v proměnné 'slovo' máš uložené náhodné slovo z listu 'ovoce'.
# Na řádku 7 máš přednastavený počet pokusů na 2, jelikož nemá smysl mít více pokusů pro tříčlenný.
# Na řádku 10 nastav správně počítadlo.
# Na řádku 13 nastav správně podmínku.
# Na řádku 19 ověř, zda se typ zadaný uživatelem rovná proměnné slovo. Pokud ano, tak na řádku 20 rozbij smyčku.
# Na řádku 23 zvyš hodnotu počítadla o 1.
# Na řádku 26 nastav podmínku pro prohru.
# Na řádku 29 do funkce print za string 'Správně! Počet pokusů:' a čárku nastav počítadlo tak, aby ukazovalo správný počet pokusů.

# Ziskani nahodneho slova z listu 'ovoce'
import random
ovoce = ['Jablko', 'Banán', 'Hruška']
slovo = random.choice(ovoce)

# Pocet pokusu na uhodnuti
pocet_pokusu = 2

# Nastaveni pocitadla
i = 0
print(slovo)

# While smycka s podminkou - napis podminku za while a před dvoujčeku
while i < pocet_pokusu:

    # Zadani tipu
    tip = input('Vlož svůj tip: ')

    # Kontrola spravnosti slova - nastav podminku za if
    if tip == slovo:
        break

    # Zvetseni pocitadla
    i = i + 1

# Podminka pro vyhru
if i == pocet_pokusu:
    print("Prohrál jsi")
else:
    print('Správně! Počet pokusů:', )