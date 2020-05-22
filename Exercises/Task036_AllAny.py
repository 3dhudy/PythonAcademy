# Tvým úkolem je vytvořit 2 funkce:

# Funkce my_all(), která imituje built-in funkci all(). 
# Funkce bude brát sekvenci a vrátí True, pokud mají všechny prvky v sekvenci boolean hodnotu True nebo pokud je sekvence prázdná. 
# Jinak fuknce vrací False.

# Funkce my_any(), která imituje built-in funkci any(). 
# Funkce bude brát sekvenci a vrátí True, pokud má aspoň jeden prvek v sekvenci boolean hodnotu True. 
# V opačném případě a také pokud je sekvence prázdná vrací fuknce False.

seq = [1, 2, 3, 4, 5]
def main():
    vsecko = my_all(seq)
    nic = my_any(seq)


def my_all(sequence):
    for item in sequence:
        if not item:
            # return False
            print("False")
    # return True
    print("True")

def my_any(sequence):
    for item in sequence:
        if item:
            # return True
            print("True")
    # return False
    print("False")

main()

# Reseni
# Použijeme podobný princip jako při hledání specifické hodnoty. 
# Pokud najdeme danou hodnotu v sekvenci, můžeme vrátit výstup.
# U naší funkce all() musíme najít aspoň jeden objekt, který má boolean hodnotu False. 
# Použijeme tedy test if not item:, který je totožný s if not bool(item):.
# U funkce any() potřebujeme aspoň jeden objekt, který má boolean hodnotu True. 
# Použijeme tedy test if item:.
# Pokud nebudou výše zmíněné testy nikdy vyhodnoceny jako True, potom by měla funkce vrátit výstup až po for loop.