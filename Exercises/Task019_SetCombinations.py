# Budeme pracovat s těmito stringy:

# str1 - 'New York'
# str2 - 'Yorkshire'

# Na řádku 6 ulož do proměnné spolecne prvky, které mají str1 a str2 společné,
# na řádku 9 ulož do proměnné unikatni prvky, které jsou unikátní pro str1,
# na řádku 12 ulož do proměnné nesdilene prvky, které str1 a str2 nesdílí. Jinak řečeno, prvky, které se nachází v str1, str2, ale ne v obou,
# na řádku 15 ulož do proměnné vsechny prvky, které str1 a str2 sdílí i nesdílí - všechny prvky,
# na řádku 18, 19, 20, a 21 postupně vypiš jednotlivé proměnné.

# Prirazeni promennych
str1 = 'New York'
str2 = 'Yorkshire'

# Najde spolecne prvky
spolecne = set(str1) & set(str2)

# Najde unikatni prvky
unikatni = set(str1) - set(str2)

# Najde nesdilene prvky
nesdilene = set(str1) ^ set(str2)

# Najde vsechny prvky
vsechny = set(str1) | set(str2)

# Vypis vsechno
print('spolecne prvky:', spolecne)
print('unikatni prvky:', unikatni)
print('nesdilene prvky:', nesdilene)
print('vsechny prvky:', vsechny)