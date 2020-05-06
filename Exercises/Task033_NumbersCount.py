# Vytvoř program, který vytiskne, kolikrát se každý objekt nachází v daném listu, tuplu, nebo stringu (u stringu chceme počet jednotlivých znaků).

# Výstupem programu by měl být slovník, který se skládá z následující dvojice klíč - hodnota:

# klíč - string reprezentace počítaného objektu,
# hodnota - celé číslo, které značí počet výskytu daného objektu.

# Zopakuješ si zde práci s:

# podmínkovými výrazy,
# sekvencemi,
# slovníky,
# for loop,

seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

counts = {}

for num in seq:
    counts[str(num)] = counts.setdefault(str(num), 0) + 1
    
print(counts)

# Zde ti pomůže metodu .setdefault(). Dejme tomu, že máme slovník s jedním počtem:

# counts = {'1':4}
# Slovník říká, číslo '1' máme čtyřikrát.

# Co kdybychom chtěli připočítat další výskyt, ale nevíme, jestli už toto číslo máme v našem slovníku? Zde nám pomůže metoda .setdefault(). 
# Fungovalo by to následovně:

# counts = {'1':4}
# counts['1'] = counts.setdefault('1',0) + 1

# Když pochopíme metodu .setdefault(), pochopíme celý řádek. 
# Metoda: 1. vrátí hodnotu v druhém argumentu, pokud klíč neexistuje 2. vrátí hodnotu klíče, pokud klíč existuje
# Čili v našem případě (1.) by to vypadalo následovně:

# counts = {'1':4}
# counts['1'] = 4 + 1
# >>> counts['1']

# V opačném případě (2.) by to vypadalo následovně:

# counts = {}
# counts['1'] = 0 + 1
# >>> counts['1']