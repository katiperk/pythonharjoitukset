sukupuoli = input("Mikä on biologinen sukupuolesi?: ")
hemoglobiini = float(input("Mikä on hemoglobiiniarvosi (g/l)?: "))

if (sukupuoli == 'nainen' or sukupuoli == 'Nainen')  and 117 <= hemoglobiini <= 175:
    print("Hemoglobiiniarvosi on normaali.")
elif (sukupuoli == 'nainen' or sukupuoli == 'Nainen') and hemoglobiini < 117:
    print("Hemoglobiiniarvosi on alhainen.")
elif (sukupuoli == 'nainen' or sukupuoli == 'Nainen') and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on korkea.")
elif (sukupuoli == 'mies' or sukupuoli == 'Mies') and 134 <= hemoglobiini <= 195:
    print("Hemoglobiiniarvosi on normaali.")
elif (sukupuoli == 'mies' or sukupuoli == 'Mies') and hemoglobiini < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif (sukupuoli == 'mies' or sukupuoli == 'Mies') and hemoglobiini > 195:
    print("Hemoglobiiniarvosi on korkea.")