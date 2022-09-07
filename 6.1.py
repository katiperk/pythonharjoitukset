import random

def noppa():
    luku = random.randint(1, 6)
    return luku

while True:
    nopanLuku = noppa()
    print(nopanLuku)
    if nopanLuku == 6:
        break