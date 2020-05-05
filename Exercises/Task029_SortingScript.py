# Vytvořme program, který nám seřadí abecedně jakýkoli list. Nemůžeme použít funkce jako je sort() nebo sorted(). 
# Toto cvičení slouží jako procvičení práce s for + break + else.

names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

# Vytvoř list, do kterého vložíš jeden prvek z list `names`. 
# Zároveň ho z listu `names` odstraň. 
# Tento krok se ti bude hodit, když budeš chtít přidávat a seřazovat další jméno z listu `names` do listu `sorted_names`
sorted_names = [names.pop(0)]

# Začni vnější for loop, kterým budeš procházet seznam `names` (měl by mít už o jeden prvek méně)
for name in names:
    # Zační vnitřní for loop, kterým budeš procházet seznam `sorted_names` a pomocí podmínkového výrazu, `break` a `else` vlož jméno z `names` buď na pozici, nebo za pozici daného jméno v listu `sorted_names`
    for i,s_name in enumerate(sorted_names):
        if name < s_name:
            sorted_names.insert(i,name)
            break
    else:
        sorted_names.append(name)

# Vytiskni seřazená jména
print(sorted_names)

# Reseni
# V našem řešení porovnáváme jestli je jméno (name) ze starého listu menší než jméno (s_name) z nového listu. Pokud platí, že name < s_name:

# vkládáme pomocí metody .insert() jméno (name) do listu sorted_names. Metoda bere dva vstupy - index (kam má prvek vložit) a daný prvek,
# pomocí break přerušujeme vnitřní smyčku a jdeme na další jméno v names.
# Pokud neplatí, že name < s_name:

# nenarazím na break,
# projedeme celý sorted_names,
# vkládáme pomocí metody .append() jméno (name) do listu sorted_names nakonec.