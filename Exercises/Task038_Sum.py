# Definice funkce sum
def my_sum(data):
    mysum = 0
    for num in data:
        mysum += num
    return mysum

# Data k secteni
data = [32,43,54,54,76,21,62,83,52,58]

# Pouziti a funkce sum na data a tisk vysledku
print(my_sum(data))