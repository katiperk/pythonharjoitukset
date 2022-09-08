from random import randint

nopat = int(input("Montako noppaa heitetään? "))
nopatYhteensa = 0
for nopat in range(nopat):
    x = randint(1, 6)
    nopatYhteensa += x

print(f"Noppien silmälukujen summa on: {nopatYhteensa}")