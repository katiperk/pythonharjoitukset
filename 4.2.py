tuumat = 0
# En saanut ohjelmaa toimimaan niin, että negatiivinen tuumamäärä jäisi tulostamatta. Ohjelma kuitenkin pysähtyy, joten sinällään toimii.

while True:
    if tuumat < 0:
        break
    elif tuumat >= 0:
        tuumat = float(input("Anna tuumat: "))
        senttimetrit = tuumat * 2.51
        print(f"Senttimetreinä: {senttimetrit:.2f}")