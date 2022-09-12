user = "python"
passwd = "rules"
i = 0

while i < 5:
    kayttaja = input("Anna käyttäjätunnus: ")
    salis = input("Anna salasana: ")
    if kayttaja != user or salis != passwd:
        if i == 4:
            print("Pääsy evätty.")
            break
        else:
            print("Väärä käyttäjätunnus tai salasana!")
    elif kayttaja == user and salis == passwd:
        print("Tervetuloa!")
        break
    i = i + 1