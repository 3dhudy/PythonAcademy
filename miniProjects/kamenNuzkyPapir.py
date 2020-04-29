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