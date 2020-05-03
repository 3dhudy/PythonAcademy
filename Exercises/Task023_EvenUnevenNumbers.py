# Napiš Python skript, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu. 
# Na konci by měl program vytisknout absolutní hodnotu rozdíu mezi těmito součty.

# Ukázka, jak by měl program fungovat:

# Máme seznam čísel: [1,2,3,4,5,6,7,8]
# Sečteme všechna sudá čísla a výsledek uložíme do proměnné suda = 2 + 4 + 6 + 8
# Sečteme všechna lichá čísla a výsledek uložíme do proměnné licha = 1 + 3 + 5 + 7
# Nakonec získéme rozdíl mezi těmito dvěmi součty (proměnná rozdil)
# Měli bychom zajistit, že výsledek nebude záporné číslo (k tomu bi ti mohly pomoci built-in funkce pro numerické typy, zmiňované v první lekci)
# Tvým ukolem je samozřejmě zjistit, jak iterovat každým prvkem v seznamu čísel, ne psát součet manuálně.

cisla = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]
        
suda = 0
licha = 0

while len(cisla) > 0:
    cislo = cisla.pop()
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo
        
vysledek = abs(suda - licha)

print('Rozdil je:', vysledek)

# Reseni
# 1. čísla uložíme do proměnné cisla
# 2. vytvoříme 2 proměnné, kde budeme uchovávat součty sudých, resp. lichých čísel
# 3. hodnoty v proměnných suda and licha budou opakovaně navyšovány uvnitř smyčky while
# 4. uvnitř while smyčky extrahujeme další číslo z konce listu cisla a uložíme ho do proměnné číslo
# 5. pokud vysledek vyrazu num%2 bude 0, navýšíme proměnnou suda
# 6. pokud vysledek vyrazu num%2 bude 1, navýšíme proměnnou licha
# 7. nakonec vypočítáme rozdíl mezi suda a licha a získámé jeho absolutní honotu pomocí funkce abs()