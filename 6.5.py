def parittomatPois(luvut):
    if (koko == 0):
        return 0
    else:
        return luvut[koko - 1] + summaus(luvut, koko - 1)

luvut = []

koko = int(input("Anna listan koko: "))

for i in range(0, koko):
    luku = int(input())
    luvut.append(luku)

summa = summaus(luvut, koko)
print(f"Listan lukujen summa: {summa}")