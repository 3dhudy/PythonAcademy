# Vytvoř prográmek, který využije indexingu tak, aby vytiskl a extrahoval:

# prvních 5 písmen slova 'indexování' a ulož je do proměnné prvnich_pet,
# posledních 5 písmen slova 'indexování' a ulož je do proměnné poslednich_pet,
# každé třetí písmeno slova 'indexování' a ulož je do proměnné kazde_treti.
# Příklad fungování skriptu:

# Poznámka: Při speficikaci v hranatých závorkách použij vždy jen jedno číslo.

slovo = "indexování"
prvnich_pet = (slovo[:5])
poslednich_pet = (slovo[5:])
kazde_treti = (slovo[::3])

# Extrahuj a vytiskni prvních 5 písmen
print("Prvních 5 pímen: ", (prvnich_pet))

# Extrahuj a vytiskni posledních 5 písmen
print("Posledních 5 písmen: ", (poslednich_pet))

# Extrahuj a vytiskni každé 3 písmeno
print("Každé 3. písmeno (počínaje prvním): ", (kazde_treti))