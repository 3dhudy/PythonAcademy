# Tvým úkolem je vytvořit funkci, která bude imitovat built-in funkci reversed(). 
# Funkce vezme jakoukoli sekvenci jako vstup a vrátí list prvků v opačném pořadí.

seq01 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
seq02 = (['New', 'Years', 'Eve'])
seq03 = ('Hello World')

def my_reversed(sequence):
    return print(list(sequence[::-1]))

my_reversed(seq02)