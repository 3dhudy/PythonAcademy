# Nyní dostaneš zadání úkolů, které prověří tvé porozuměnní novým metodám. Dej si na ně čas a ber jeden úkol po druhém. Pokud nevíš, neváhej se podívat do nápovědy nebo rovnou otevři řešení. Pojďme na to:

# Na řádku 5 do proměnné 'rozdeleny_string' ulož 'muj_string' jako list rozdělený podle mezer.
# Na řádku 12 a 13 do proměnné 'emaily' přidej pouze emailové adresy pomocí jejich indexu v proměnné 'rozdeleny_string'.
# Na řádku 19 a 20 získej pouze domény (text za znakem '@') z emailů v listu 'emaily'. První doménu ulož do proměnné 'domena01' a druhou do 'domena02'.
# Na řádku 23 a 24 rozděl domény podle znaku '.' a ulož pouze první prvek (na indexu 0) do stejné proměnné.
# Na řádku 29 ověř pomocí podmínky if, zda proměnná 'domena01' neobsahuje žádná čísla.
# Na řádku 30 přiřaď kód pod příkaz if, který spojí s prázdným stringem 'bez_cisel' pouze tu doménu, která neobsahuje číslice.
# Na řádku 31 přiřaď pod příkaz if funkci print(), která vypíše následující: 'Doména', <doména>, 'byla přidána.'.
# Na řádku 33 přiřaď pod příkaz else funkci print(), která vypíše následující: 'Doména <doména> nebyla přidána, protože obsahuje čísla!'.
# To samé proveď na řádku 36, 37, 38 (if), a 41 (else) proměnnou 'domena02'.

# Zadany string
muj_string = 'Abc@abc.cz a Matous@1234.cz jsou naše emailové adresy'

# Rozdel string
rozdeleny_string = list(muj_string.split())

# Tisk promenne 'rozdeleny_string'
print(rozdeleny_string)

# Ziskej emaily
emaily = list()
emaily.append(rozdeleny_string[0])
emaily.append(rozdeleny_string[2])

# Tisk promenne 'emaily'
print(emaily)

# # Ziskani domen
domena01 = emaily[0].split('@')[-1]
domena02 = emaily[1].split('@')[-1]

# Rozdel domeny podle znaku '.' a uloz je do stejne prommene
domena01 = domena01.split('.')[0]
domena02 = domena02.split('.')[0]

# Spoj promenne 'domena01' a 'domena02' s promennou 'bez_cisel'
bez_cisel = ''

# Dopln podminkovy vyraz pro 'domena01'
if domena01.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print('Domena', domena01, 'byla pridana.')
else:
    print('Domena', domena01, 'nebyla pridana, protoze obsahuje cisla.')

# Dopln podminkovy vyraz pro 'domena02'
if domena02.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print('Domena', domena02, 'byla pridana.')
else:
    print('Domena', domena02, 'nebyla pridana, protoze obsahuje cisla.')

# ZDE NIC NEDOPLNUJ, jde o nasi kontrolu :)
if (len(bez_cisel) + 1) % 4 == 0:
    print('Bezva, další zkouška úspěšně za tebou. Jen tak dál!')
else:
    print('Bohužel, někde máš chybku. Pokud si nevíš rady, mrkni se dolů na řešení.')

# Reseni
# Na řádku 5 použij metodu .split() na list 'muj_string'.
# Na řádku 11 a 12 použij metodu .append() na proměnnou 'emaily' pro přidání emailových adres na indexu 0 a 2.
# Na řádku 18 a 19 použij na list 'emaily' indexing pro výběr jednotlivých adres a metodu .split(), kterou rozdělíš emaily na 2 části pomocí znaku '@' (uživatelké jméno před znakem '@' a doména za ním. 
# Za metodu .split() ještě přidej index -1, abys vybral doménu.
# Na řádku 29 je potřeba použít podmínkový příkaz if. Za něj dej proměnnou 'domena01', na kterou použij metodu .isaplha() a zakonči řádek dvojtečkou.
# Na řádek 30 (pod if příkaz) vložíme indentaci (4 mezery, nebo 1 tabulátor) a použijeme metodu .join() na proměnnou 'bez_cisel', která spojí string 'domena01' s prázdných stringem proměnné 'bez_cisel'. 
# To celé přiřadíme stejnojmenné proměnné - 'bez_cisel'.
# Na řádku 33 vložíme opět indentaci, která přiřadí kód pod příkaz else a do funkce print() dáme tři argumenty - 'Doména', domena01, 'nebyla přidána, protože obsahuje čísla!'.
# To samé na řádcích 36, 37, 38 a 40 pro proměnnou 'domena02'.

# Poznámka: Na řádku 18 a 19 kombinujeme 2x indexing a 1x metodu .split(), což může být matoucí. Pojďme si to pro jistotu rozebrat. 
# Tento úkol se dá rozdělit na více řádků, což si můžeme demonstrovat na jedné z emailových adres.

# #Rozdeleni emailove adresy na indexu 0 na dve casti

# cely_email = emaily[0].split('@')
# print(cely_email)

# # Takto vypada promenna cely_email
# ['Abc', 'abc.cz']

# # Ziskani domeny
# domena01 = cely_email[-1]
# print(domena01)