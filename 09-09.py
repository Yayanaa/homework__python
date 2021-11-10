import random
number1=['3', '2', '6', '8']
number2=['4', '7', '0', '4']
number3=['1', '5', '2', '1']
def generator(num):
    i = 0
    while i < num:
        yield random.choice(number1)+ random.choice(number2) + random.choice(number3)
        i += 1

gen = generator(3)
for x in gen:
    print(x)
