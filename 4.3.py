luvut = []

while True:
        luku = (input("Syötä luku: "))
        if luku == '':
            print(f"Pienin syötetty luku on {min(luvut)} ja suurin syötetty luku on {max(luvut)}.")
            break
        try:
            luvut.append(float(luku))
        except ValueError:
            continue