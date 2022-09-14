vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))
if 3 <= kuukausi <= 5:
    print(f"{kuukausi}. kuukautta vastaava vuodenaika on {vuodenajat[0]}")
elif 6 <= kuukausi <= 8:
    print(f"{kuukausi}. kuukautta vastaava vuodenaika on {vuodenajat[1]}")
elif 9 <= kuukausi <= 11:
    print(f"{kuukausi}. kuukautta vastaava vuodenaika on {vuodenajat[2]}")
elif kuukausi == 12 or 0 < kuukausi <= 2:
    print(f"{kuukausi}. kuukautta vastaava vuodenaika on {vuodenajat[3]}.")
else:
    print("Virheellinen kuukauden numero.")