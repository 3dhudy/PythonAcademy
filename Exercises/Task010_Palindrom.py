# Palindromy jsou taková slova, která se čtou stejně zepředu i pozpátku. Pojďme si napsat program, který je pozná.

# Vytvoř proměnnou slovo, která si od uživatele vyžádá vstup.
# Pokud se jedná o palindrom, vytiskni - Slovo 'slovo' je palindrom!. Pokud ne, vytiskni - Slovo 'slovo' není palindrom.

# Vstup uzivatele
slovo = input("Zadej slovo:")

# Zkontroluj a odpověz, zda se jedná o palindrom
if slovo == slovo[::-1]:
    print("Slovo '" + slovo + "' je palindrom!.")
else:
    print("Slovo '" + slovo + "' není palindrom.")