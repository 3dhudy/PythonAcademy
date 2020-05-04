# Vytvořte program, který vytiskne každý pár klíč-hodnota ve formátu: "Klíč: <key> | Hodnota: <value>"

film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump is
                    the same house used in The Patriot
                    (2000). Some paneling was changed
                    for interior shots  in the latter
                    film.'''}
                    
while film:
    info = film.popitem()
    print('Klíč:', str(info[0]), '|', 'Hodnota:', str(info[1]))

# Reseni
# Během každého opakování uvnitř smyčky chceme ze slovníku film extrahovat klíč i hodnotu.
# K tomu nám může pomoci metoda dict.popitem()
# Opakovaným prováděním dojde k vymazání celého slovníku, tudíž můžeme v hlavičce smyčky použít podmínku while film.
# Až bude slovník prázdný, kód ve smyčce nebude dále prováděn