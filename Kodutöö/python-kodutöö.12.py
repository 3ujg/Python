EEK = float(15.64)
EUR = 1
valik = int(input("Millisest rahaühikust soovid kalkuleerida: \n1.EUR -> EEK\n2.EEK -> EUR\n1,2: "))
if valik==1:
    EEKN = int(input("EUR: "))
    eru = round(EEK * EEKN)
    print(f"{EEKN} eurot on {eru} eesti krooni")
elif valik==2:
    EURN = int(input("EEK: "))
    eku = float(EURN * 0.06)
    print(f"{EURN} eesti krooni on {round(eku)} eurot")
else:
    "Vale vastus!"
