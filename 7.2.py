nimet = set()
while True:
    nimi = input("Anna nimi: ")
    if len(nimi) == 0:
        print(nimet)
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimet.add(nimi)
    elif nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)