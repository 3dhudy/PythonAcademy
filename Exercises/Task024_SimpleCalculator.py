# Tvým úkolem v této části bude napsat jednoduchý skript, který bude umět provádět se dvěma zadanými hodnotami volitelné matematické operace (součet, odčítání, násobení, dělení) Řekněme, že si uživatel vybere cislo01 = 3 a cislo02 = 4. 
# Dále si vybere, že chce provést operaci soucet. Výsledkem by měl vypsaný výpočet 3 + 4 = 7.

# Nejprve si ukážeme, jak bychom měli u tvorby takového kódu přemýšlet.

# Na začátek budeme chtít pozdravit uživatele a říct, aby vepsal dvě libovolná čísla.
# Další částí bude nadepsaný výběr operací, které může s čísly provádět.
# Nakonec budeme potřebovat spojit operaci, kterou uživatel vybral s výpočtem, který má provést a následně vypsat.
# Pomocí cyklu bychom chtěli zopakovat, aby se uživateli nabízely operace tak dlouho, dokud je nebude chtít příkazem ukončit.


# Pozdrav uživatele a umožni mu zapsat dvě vstupní proměnné
print('Dobry den, vitejte v teto male kalkulacce.')
print()
cislo01 = float(input('Zadejte prvni cislo:'))
cislo02 = float(input('Zadejte druhe cislo:'))

# Tento text nechceme opakovat, proto patří před smyčku while
print('Zvolte operaci, kterou chcete provest:')
print()

# Zapiš nekonečnou smyčku
# mod kalkulacky je ON
# Podminka nekonecne smycky
mod = True
while mod == True:

# Vypiš jaké operace může uživatel provádět a možnost zapsat input()
    operace = str(input('''
----------------------
Scitani:    "+",
Odcitani:   "-",
Nasobeni:   "*",
Deleni:     "/",
Ukonci:     "=",
----------------------
Vyber operaci: '''))

# Sem zapiš podmínky, které spojí tebou nabízené operace a následný print() výsledku
    if operace == '+':
        print('     >>> ' + str(cislo01)+ ' + ' + str(cislo02) + ' = ' + str(cislo01 + cislo02))
    elif operace == '-':
        print('     >>> ' + str(cislo01) + ' - ' + str(cislo02) + ' = ' + str(cislo01 - cislo02))
    elif operace == '*':
        print('     >>> ' + str(cislo01) + ' * ' + str(cislo02) + ' = ' + str(cislo01 * cislo02))
    elif operace == '/':
        print('     >>> ' + str(cislo01) + ' / ' + str(cislo02) + ' = ' + str(cislo01 / cislo02))
    elif operace == '=': # prepnu mod OFF
        print('Nashledanou.')
        mod = False