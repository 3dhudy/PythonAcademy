# Tvým úkolem je vytvořit dvě funkce:

# Funkce my_min(), která imituje built-in funkci min(). 
# Funkce by měla přijmout jakoukoli sekvenci a vrátit položku s nejmenší hodnotou.

seq = [43,45,87,21,23]

def main(sequence):
    my_max(seq)
    my_min(seq)

def my_min(sequence):
    minimum = seq[0]
    for num in seq[1:]:
        if num < minimum:
            minimum = num
    return print(f"Minimum number is {minimum}")

def my_max(sequence):
    maximum = seq[0]
    for num in seq[1:]:
        if num > maximum:
            maximum = num
    return print(f"Maximum number is {maximum}")

main(seq)