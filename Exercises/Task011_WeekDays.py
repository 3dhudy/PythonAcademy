# Tvým úkolem bude napsat krátký skript (malý prográmek), který bude umět následující:

# 1. Zeptá se uživatele následující otázku:
# (Správná odpověď, alespoň v Česku, je p - pátek)

# 2. Do proměnné result uloží True, jestliže uživatel odpoví správně a False v případě špatné odpovědi.

# 3. Do konzole vytiskne obsah proměnné result.
# Dáme ti malou radu. Rozděl si celou úlohu na jednotlivé kroky. Jak uvidíš, naše řešení má 4 kroky. 
# Pokud si opravdu nevíš rady, podívej se níže, kde je více nápovědy. Určitě to zvládneš :)

# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu (vse malymi pismeny!)
tyden = ['pondeli', 'utery', 'streda', 'ctvrtek', 'patek', 'sobota', 'nedele']

# Ziskej tip uzivatele
tip_uzivatele = input('Jakým písmenem začíná jméno pátého dne v týdnu?: ')

# Ziskej prvni pismeno z 'pátek' 3
patek_pismeno = tyden[4][0]

# Vysledek porovnani uloz do promenne 'vysledek'
vysledek = tip_uzivatele == patek_pismeno

# Vytiskni vysledek porovnani promennych
print(vysledek)