# Vytvoř funkci, která zjišťuje počet výskytů daného prvku. 
# Jako vstup bere prvek, který hledáme a sekvenci, ve které ho chceme najít.
from pprint import pprint as pp

# Definice funkce count
def my_count(sequence):
    vyskyt_slov = {}
    for slovo in sequence:
        vyskyt_slov[slovo] = vyskyt_slov.setdefault(slovo, 0) +1
    pp(f"{vyskyt_slov}")

# Nase data
names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark',
'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim',
'Mark', 'Mark', 'Bob', 'Mark']

# Pouziti funkce count a tisk vysledku
my_count(names)