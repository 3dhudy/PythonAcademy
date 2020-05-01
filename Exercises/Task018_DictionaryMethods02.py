# Na řádku 7 získej pomocí vhodné metody ze slovníku 'slovnik01' KLÍČE a HODNOTY a ulož je do proměnné 'klice_hodnoty',
# na řádku 10 získej pomocí vhodné metody ze slovníku 'slovnik02' KLÍČE a ulož je do proměnné 'klice',
# na řádku 13 získej pomocí vhodné metody ze slovníku 'slovnik03' HODNOTY a ulož jej do proměnné 'hodnoty',
# zkus na řádku 17 získat pomocí vhodné metody ze slovníku 'slovnik03' HODNOTY z vnitřního slovníku 'zamestnanci' a ulož jej do proměnné 'vyzva'.

# slovniky
slovnik01 = {'jmeno': 'David', 'prijmeni': 'Novak', 'vek': 33}
slovnik02 = {'pismena': ['a', 'b', 'c', 'd'], 'cisla': [1,2,3,4,5]}
slovnik03 = {'zamestnanci': {'id01': 'Marek', 'id02': 'Matous', 'id03': 'Anna'}, 'adresy': {'id01': 'Brno', 'id02': 'Praha', 'id03': 'Praha'}}

# ziskej klice i hodnoty
klice_hodnoty = slovnik01.items()

# ziskej klice
klice = slovnik02.keys()

# ziskej hodnoty
hodnoty = slovnik03.values()

# VYZVA
# ziskej hodnoty z vnitrniho slovniku
vyzva = slovnik03['zamestnanci'].values()

# ZDE NIC NEPIŠ. Slouží pouze pro kontrolu :)
if len(klice_hodnoty) == 3 and len(klice) == len(hodnoty) and (int(len(vyzva)))%3 == 0:
	print('Skvělá práce! Zvládl jsi jak naši Challenge, tak procvičení celkově!')
elif len(klice_hodnoty) == 3 and len(klice) == len(hodnoty) or (int(len(vyzva)))%3 == 0:
	print('Dobrá práce! Ještě v tom jsou chybky, ale je s čím pracovat!')
else:
	print('Bohužel :(\nMrkni se na metody ještě jednou a pak zkus úlohu znovu.')