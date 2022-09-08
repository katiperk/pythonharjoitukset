import math

def pizzaPerNelio(halkaisija, hinta):
    ala = halkaisija * math.pi
    neliohinta = hinta / ala
    return neliohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
neliohinta_eka = pizzaPerNelio(halkaisija1, hinta1)

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))
neliohinta_toka = pizzaPerNelio(halkaisija2, hinta2)

if neliohinta_eka > neliohinta_toka:
    print("Pizza numero kaksi antaa parempaa vastinetta rahalle.")
elif neliohinta_eka < neliohinta_toka:
    print("Pizza numero yksi antaa parempaa vastinetta rahalle.")
else:
    print("Pizzat ovat yhtä hyvää vastinetta rahalle.")