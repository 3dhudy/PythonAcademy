# BMI (Body Mass Index) je míra, která vyčísluje obezitu u lidí.

# BMI rovnice výpočtu:
# váha / výška2
# Váha se udává v kilogramech a výška v metrech. Hodnoty, které z tohoto vzorečku dostaneme, škálujeme podle této tabulky:

# Hodnota	Význam
# do 18,5	Podvýživa
# 18,5 – 25	Zdravá váha
# 25 – 30	Mírná nadváha
# 30 – 40	Obezita
# 40 a více	Těžká obezita
# Tvoje úloha

# Chceš vypočítat BMI uživatele Martin, který měří 200 centimerů a váží 80 kilogramů. Vytvoř proměnné jmeno, vaha, vyska a zadej do nich hodnoty.
# Vytvoř proměnnou bmi a přiřaď k ní vzorec, pomocí proměnných vaha, vyska a aritmetického operátoru na druhou (zkus si vzpomenout, jak se zapisuje).
# Vytvoř proměnnou kategorie, které se bude pomocí podmínek měnit podle hodnoty BMI.
# Vytiskni výsledek - proměnná jmeno, text "tvé BMI je", a proměnnou bmi, což spadá do kategorie", proměnná kategorie.

# Vstupni hodnoty
jmeno = str(input('Zadejte vase jmeno: '))
vyska = int(input('Zadejte svoji vysku: '))
vaha = int(input('Zadejte svoji vahu: '))

# Vypocet
bmi = vaha / vyska ** 2

# Vytvor promennou kategorie a prirad ji pomoci podminek
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'
    
# Vytiskni odpoved s vysledkem
print(jmeno, "tvé BMI je", str(bmi), "což spadá do kategorie", kategorie, '.')