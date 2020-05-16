# Napiš program, který bude mít 3 vstupy a všechny budou celá čísla:

# start
# stop
# divisor (dělitel)
# Všechny by měly být poskytnuty uživatelem.

# Program by měl:

# vygenerovat sbírku celých čísel v rozmezí mezi start (včetně) a stop (včetně)
# vytisknout list v rozmezí čísel start - stop, která jsou dělitelná vstupem divisor
# Pokud je dělitel 0, program by měl vytisknout string Dělit 0 není možné.

# 1. Vstup uzivatele
start = int(input("Zadejte pocatecni cislo:"))
stop = int(input("Zadejte konecne cislo:"))
divisor = int(input("Zadejte delitele:"))

# 2. List cisel mezi star a stop
numbers = []

# 3. Vytisknout list cisel delitelnych zvolenym cilem
if divisor:
    for num in range(start, stop + 1):
        if num % divisor == 0:
            numbers.append(num)

    print('Tato cisla v rozsahu(' + str(start) +' - ' + str(stop) + ') jsou delitelna ' + str(divisor) + ':')
    print(numbers)

# 4. pokud je delitel 0 vytisknout chybove hlaseni
else:
    print("Dělit 0 není možné.")