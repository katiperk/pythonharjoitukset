import random

def noppa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

tahkojenMaara = int(input("Kuinka monta tahkoa? "))
while True:
    nopanLuku = noppa(tahkojenMaara)
    print(nopanLuku)
    if nopanLuku == tahkojenMaara:
        break