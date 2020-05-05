# Tvým úkolem bude napsat skript, který příjme od uživatele string s čísly, která jsou oddělena čárkou a vygeneruje list celých čísel ze zadaného stringu (datový typ integer). 
# Program by měl následně list vypsat.

# Také budeš muset ošetřit kód tak, aby si uměl poradit se situací, kdy by součástí stringu byly mezery.

# Pracuj s následujícími proměnnými:

# inpt - získej vstup uživatele
# nums - vlož čísla do listu s mezerama
# result - vlož čísla do listu bez mezer

vstup = input('Vlozte vase cisla oddelena carkou, prosim:')
cisla = vstup.split(',')
vystup = []
 
for cislo in cisla:
     cislo = int(cislo.strip())
     vystup.append(cislo)
     
print('Vase cisla:', vystup)

# Reseni
# Nejdřív musíme rozdělit na jednotlivá čísla pomocí metody .split(),
# a n ásledně musíme projít jednotlivé prvky nového seznamu a pomocí metody .strip() odstranit mezery.