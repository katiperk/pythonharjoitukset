def bensanMaara(gallonat):
    litrat = gallonat * 3.78541178
    return litrat


while True:
    gallonat = float(input("Kuinka monta gallonaa? "))
    if gallonat >= 0:
        litrat = bensanMaara(gallonat)
        print(f"Gallonat litroina: {litrat:.2f}")
    else:
        break

