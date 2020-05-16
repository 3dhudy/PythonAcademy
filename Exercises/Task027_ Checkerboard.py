# Napiš program, který vytiskne šachovnici daných rozměrů.

# Program musí používat proměnné:

# size - délka hrany šachovnice
# symbols - znaky potřebné pro černá a bílá pole
# desk - reprezentace šachovnice
# Pro otestování:

# size - musí být 10
# symbols musí být znaky # a mezeru
# desk - musí být seznam s pruhy šachovnice

# Zadej rozměry šachovnice
size = 10

# Zadej symboly
symbols = ['#',' ']

# Vytvoř šachovnici
desk = []

# Doplň smyčky for, které by měly postupně nahrát celou šachovnice do proměnné 'desk'
for row in range(size):
    line = []

    for cell in range(size):
        repete = (row+cell) % len(symbols)
        line.append(symbols[repete])

    desk.append(''.join(line))

# Vytiskni šachovnici
print('\n'.join(desk))

# Reseni
# Naše šachovnice na začátku je prázdný list, který má být naplněn dalšími listy. Další listy představují jednotlivé linie šachovnice.
# Využíváme 2členného listu (symbols), který obsahuje symbol '#' a mezeru ' '.
# Z tohoto pak pomocí vnořených for loop nahráváme dané symboly do linie (vnitřní for loop) a tu pak do šachovnice (vnější for loop).
# Jádrem celého skriptu je příhodné použití operátorů v tomto zápise i = (r + p) % len(sym).
# Tato rovnice vlastně vybere vhodný index (0, nebo 1) pro náš 2členný list (symbols) a nahraje buď '#', když je zbytek rovnice 0, nebo ' ', když je zbytek rovnice 1.