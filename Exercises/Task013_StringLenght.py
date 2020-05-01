# Vytvoř skript, který:

# přijme jakékoli slovo od uživatele,
# zjistí a vytiskne délku zadaného slova,
# pokud je délka slova větší než 4, vytiskne větu 'slovo' obsahuje 5 znaků',
# pokud je delka_slova menší než 5, vytiskne 'slovo' obsahuje 3 znaky. Rozdíl je v jednotném a množném čísle slova znaků/y. 

# Zadani slova
slovo = str(input("Yadejte slovo: "))

# Zjisteni delky
delka_slova = len(slovo)

# Podminka a tisk delky slova
if delka_slova > 4:
    print('slovo', slovo, 'obsahuje vie nez', delka_slova + 1, 'znaku.')
else:
    print('slovo', slovo, 'obsahuje mene nez', delka_slova + 1, 'znaky.')