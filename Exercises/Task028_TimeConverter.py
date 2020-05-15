# Naším úkolem je vytvořit program, který vezme vstup v 24hodinovém formátu a převede jej do anglického času, který bude zahrnovat zkratky PM a AM.

# Tvé úkoly:

# Získej vstup uživatele do proměnné time
# Rozděl do listu vstup od uživatele do proměnné hours a mins.
# Uprav proměnou 'hours' tak, aby se do proměnné adjusted_hours místo 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).
# Do proměnné daytime vyber odpovídající string z dvojčlenného listu ['AM', 'PM']
# Vytiskni převedený čas.

# Získej vstup uživatele do proměnné `time`
time = input("Zadejte prosim cas ve formatu hh:mm:")

# Rozděl do listu vstup od uživatele do proměnné `hours` a `mins`.
hours, mins = time.split(':')

# Uprav proměnou `hours` tak, aby se do proměnné `adjusted_hours` místo
# 24 hodinového
# formátu (např.: 17) uložil formát anglický (např.: 5).
adjusted_hours = hours if int(hours) == 12 else str(int(hours) % 12)

# Do proměnné `daytime` vyber odpovídající string z dvojčlenného
# listu ['AM', 'PM']
daytime = ['AM', 'PM'][int(hours) >= 12]

# Vytiskni převedený čas.
print('Vas cas', time, 'prveden na Anglicky format je', adjusted_hours, ':', mins, daytime)

# Reseni
# V řešení používáme jednořádkový podmínkový výraz. Jeho formát je: UDELEJ TOHLE if NECO else UDELEJ TOHLE. 
# Pokud se proměnná hours po převedení na celé číslo rovná 12, přiřaď tedy danou proměnou do adjusted_hours. 
# Jinak, pokud se po převedení na celé číslo rovná něčemu jinému, vezmi zbytek a ten přiřaď do proměnné adjusted_hours.

# Výraz int(hours)>=12 rozhodne, zda je před dvanáctou, nebo po dvanácté. 
# Pokud je po 12, vrátí True, čili index 1, což znamená string 'PM'. Pokud je před 12, vrátí False, čili 0, tedy string 'AM'.