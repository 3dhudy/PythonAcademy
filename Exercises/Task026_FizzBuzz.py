# Napiš program, který tiskne celá čísla od 1 do 100 (včetně).
# 
# Ale:
# 
# pro násobky 3 vytiskni Fizz (místo čísla)
# pro násobky 5 vytiskni Buzz (místo čísla)
# pro násobky 3 a 5 zároveň vytiskni FizzBuzz (místo čísla)

for cislo in range(1, 101):
    if cislo % 15 == 0:
        print('FizzBuzz')
    elif cislo % 3 == 0:
        print('Fizz')
    elif cislo % 5 == 0:
        print('Buzz')
    else:
        print(cislo)