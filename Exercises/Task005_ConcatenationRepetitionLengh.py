# Vytvoř skript, který:

# vyžádá jméno od uživatele a uloží jej do proměnné jmeno,
# vytiskne proměnnou jmeno,
# vyžádá přijmení od uživatele a uloží jej do proměnné prijmeni,
# vytiskne proměnnou prijmeni,
# vytvoří proměnnou cele_jmeno, do které uložíš spojení proměnné jmeno a prijmeni,
# vytiskne proměnnou delka_jmena`, která bude obsahovat délku celého jména
# vytiskne proměnnou cele_jmeno, ktetá bude shora i zespoda ohraničená řadami rovnítek. 
# K tomu použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje cele_jmeno

# Ukladani jmena
jmeno = input(str("Vase jmeno: "))

# Tisk jmena
print("Jmeno:", jmeno)

# Ukladani prijmeni
prijmeni = input(str("Vase prijmeni: "))

# Tisk prijmeni
print("Prijmeni:", prijmeni)

# Vytvoreni a tisk promenne cele_jmeno
cele_jmeno = (jmeno + " " + prijmeni)
print("Cele jmeno:", cele_jmeno)

# Vytvoreni a tisk promenne delka_jmena
delka_jmena = len(cele_jmeno)
print("Delka jmena: ", delka_jmena)

# Tisk ohranicene promenne cele_jmeno
oddelovac = ("=" * delka_jmena)
print(oddelovac)
print(cele_jmeno)
print(oddelovac)