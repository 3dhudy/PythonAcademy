# Máme slovník:
# data = {'uzivatel1': 'heslo1', 'Marek': '1234', 'Danko': 'qwert'}

# V tomto úkolu se pokusíme ověřit, jestli heslo vložené uživatelem skutečně patří k jeho účtu.

# Na řádku 9 a 10 získej vstup od uživatele,
# na řádku 13 ověř, zda vstup uživatele odpovídá kombinaci uživatelského jména a hesla,
# pokud je podmínka na řádku 13 splněná, vytiskni na následujícím řádku pozitivní odpověď,
# na řádku 16 zapiš alternativní podmínkový výraz,
# pokud je podmínka na řádku 16 splněná, vytiskni na následujícím řádku vhodnou odpověď.

# Nas slovnik
data = {
	'uzivatel1': 'heslo',
	'Marek': '1234',
	'Danko': 'qwert',
			}

# Zeptej se na uzivatelske jmeno a heslo
jmeno = str(input('Zadejte jmeno:'))
heslo = str(input('Zadejte heslo:'))

# Podminkovy vyraz
if data.get(jmeno) != heslo:
	print('Jmeno nebo heslo neni spravne')

elif data.get(jmeno) == heslo:
	print('Muzete pokracovat')