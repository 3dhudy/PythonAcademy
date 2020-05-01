# Na řádku 2 a 3 vytvoř do proměnných 'muj_slovnik' a 'novy_slovnik' prázdné slovníky,
# na řádku 6 a 7 do proměnné 'muj_slovnik' vlož tyto klíče: 'jméno', 'přijmení'. Pro klíče vytvoř jejich libovolné hodnoty,
# na řádku 11 vytvoř pomocí vhodné metody z tuple 'muj_tuple' slovník a ten ulož do slovníku 'novy_slovnik',
# na řádku 14 slovník 'muj_slovnik' doplň o 'novy_slovnik' pomocí metody update,
# na řádku 17 a 18 vyplň klíče 'věk' a 'email'. 

# vytvor prazdne slovniky do slovníků
muj_slovnik = dict()
novy_slovnik = dict()

# vloz klice 'jméno', 'přijmení' do 'muj_slovnik' a přidej libovolne hodnoty
muj_slovnik['jméno'] 	= 'Ondrej'
muj_slovnik['přijmení'] 	= 'Hudecek'

# vytvor z tuple 'muj_tuple' slovnik do slovniku 'novy_slovnik'
muj_tuple = 'věk', 'email'
novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

# dopln muj_slovnik o novy_slovnik
muj_slovnik.update(novy_slovnik)

# vypln klice 'věk' a 'mail'
muj_slovnik['věk'] = 30
muj_slovnik['email'] = '3dhudy@gmail.com'

# TADY NIC NEPIŠ!! Slouží pro kontrolu :)
if (len(muj_slovnik) + 1) % 5 == 0 and '@' in muj_slovnik['email']:
	print('Paráda, metody slovníků ovládáš na jedničku, blahopřejeme!')
else:
	print('Bohužel jsi někde udělal chybku :(\nPodívej se ještě jednou na tabulku s metodami.\n\npozn. Obsahuje tvůj email "@"?')
	