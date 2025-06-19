
summa = int(input("Omonat summasini kiriting (so'mda): "))

if summa < 100000:
    print("Foiz: 5%")
else:
    if summa <= 500000:
        print("Foiz: 7%")
    else:
        print("Foiz: 10%")
