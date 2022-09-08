def parittomatPois(luvut):
    for i in luvut:
        if i % 2 != 0:
            luvut.remove(i)
    return luvut

luvut = []

koko = int(input("Anna listan koko: "))

for i in range(0, koko):
    luku = int(input())
    luvut.append(luku)

print(luvut)
paritonLista = parittomatPois(luvut)
print(paritonLista)