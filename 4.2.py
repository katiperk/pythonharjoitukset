while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat >= 0:
        senttimetrit = tuumat * 2.51
        print(f"Senttimetreinä: {senttimetrit:.2f}")
    else:
        break