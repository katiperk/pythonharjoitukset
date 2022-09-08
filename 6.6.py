import math

def pizzaPerNelio(hinta, ala):
    neliohinta = hinta / ala
    return neliohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
ala = halkaisija1 * math.pi
neliohinta_eka = pizzaPerNelio(hinta1, ala)

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))
ala = halkaisija2 * math.pi
neliohinta_toka = pizzaPerNelio(hinta2, ala)

if neliohinta_eka > neliohinta_toka:
    print("Pizza numero kaksi antaa parempaa vastinetta rahalle.")
elif neliohinta_eka < neliohinta_toka:
    print("Pizza numero yksi antaa parempaa vastinetta rahalle.")
else:
    print("Pizzat ovat yhtä hyvää vastinetta rahalle.")