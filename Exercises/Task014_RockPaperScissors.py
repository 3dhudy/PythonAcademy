# Pro tuto úlohu budeme muset trochu předběhnout naše dosavadní znalosti a do skriptu si naimportujeme Python modul Random. Modulem random i importováním obecně se budeme podrobně zabývat v dalších lekcích, pro teď nám stačí vědět, že díky tomu si počítač bude moci náhodně vybírat mezi volbami kámen, nůžky a papír.
# Naimportuj modul random (již v kódu).
# Vytvoř list moznosti s prvky 'kamen', 'nuzky', 'papir'.
# Vytvoř proměnnou hrac, která požádá uživatele o jeho vstup.
# Vytvoř proměnnou pocitac, které bude náhodně přiřazen prvek z listu moznosti (již v kódu).
# Vytisni volbu hráče a počítače. 
# Rozhodni, zda uživatel zadal neplatný vstup (jiný než prvky v listu moznosti), pokud ano, vytiskni do konzole 'Neplatna volba'
# Pokud ne, napiš další podmínky, které budou kombinovat různe možnosti voleb hráče a počítače.
# Pokud hráč vyhraje, vytiskni "Vyhral jsi!", pokud prohraje, vytiskni "Prohral jsi :(", v případě remízy vytiskni "Nerozhodne"
# Naimportuj modul random
import random

# Vytvort list moznosti
moznosti = ['kamen', 'nuzky', 'papir']

# Vytvort promennou hrac
hrac = input('Zadejte Vasi volbu:')

# Vytvort promennou pocitac
pocitac = random.choice(moznosti)

# Vytiskni volbu cloveka a pocitace
print('Hrac', hrac)
print('Pocitac', pocitac)

# Vytvor podminku, zda hrac zvolil neplatnou volbu
if hrac != 'kamen' and hrac != 'nuzky' and hrac != 'papir':
    print('Neplatna volba')

# Pokud je volba v poradku, muzeme provest zbytek programu
else:
    # Podimky zahrnujici ruzne kombinace voleb hrace a pocitace a tisk vysledku
    if hrac == 'kamen' and pocitac == 'nuzky':
        print('Vyhral jsi!')
    elif hrac == 'nuzky' and pocitac == 'papir':
        print('Vyhral jsi!')
    elif hrac == 'papir' and pocitac == 'kamen':
        print('Vyhral jsi!')
    elif hrac == pocitac:
        print('Nerozhodne')
    else:
        print('Prohral jsi')