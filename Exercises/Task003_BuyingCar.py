# V Python oknu už máš vypsané ceny Mercedesu a Rolls-Royce. Musíš navíc vytvořit proměnou, které si od uživatele vyžádá cenu za příplatkovou výbavu. Poté bude třeba spočítat:

# Cenu za dva Mercedesy,
# cenu za Mercedes a Rolls-Royce,
# cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich),
# cenu za Mercedes s příplatkovou výbavou.
# Nakonec by měl program všechno přehledně vypsat. Pusť se do toho.

# Cenik
mercedes    = 150
rolls_royce = 400

# Vlozeni informace o priplatku

priplatek = int(input('Zadej cenu priplatkove vybavy: '))

# Vypocet

dva_mercedesy   = mercedes * 2
rolls_mercedes  = mercedes + int(rolls_royce)
dva_rollsy      = int(rolls_royce) * 2 + 2 * priplatek
mercedes_pripl  = mercedes + priplatek

# Vypis informaci

print('Cena za dva Mercedesy je', dva_mercedesy , 'tisíc USD.')
print('Cena za Mercedes a Rolls-Royce je', rolls_mercedes , 'tisíc USD.')
print('Cena za dva Rolls-Royce s příplatkovou výbavou je', dva_rollsy , 'tisíc USD.')
print('Cena za dva Mercedesy s příplatkovou výbavou', mercedes_pripl , 'tisíc USD.')