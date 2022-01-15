import random as rnd
import os

clear = lambda: os.system('cls')
znacky = tuple(('BMW', 'Audi', 'Renault', 'Nissan', 'Toyota', 'Ford'))

print(*znacky)
input('Press enter to continue.')
clear()

try:
    pokus = int(input("Pocet pokusu: "))
    actual = rnd.choice(znacky)
    
    while(pokus != 0):
        guess = str(input('Znacka: '))
        if actual.casefold() == guess.casefold():
            print('Vyhral jsi!')
            input('Press enter to exit.')
            exit()
        else:
            print('Vedle jak ta jedle.')
            pokus -= 1

    print('Prohral jsi. (Nedostatek pokusu)')
    input('Press enter to exit.')
    exit()

except ValueError:
    print('Spatny input')