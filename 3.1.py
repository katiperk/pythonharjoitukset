kuha = float(input("Anna kuhan pituus senttimetreinä: "))

if kuha < 37.0:
    puuttuva = 37.0 - kuha
    print(f"Kuha on alamittainen: alimmasta sallitusta pyyntimitasta jää puuttumaan {puuttuva:.2f} senttimetriä. Laske kuha takaisin järveen.")