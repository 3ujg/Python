# Alar Tammes 09.05.2025
# Ülesanne 12

EEK = float(15.64)
EUR = 1
while True:
    valik = int(input("Millisest rahaühikust soovid kalkuleerida: \n1.EUR -> EEK\n2.EEK -> EUR\n3. Lõpeta tegum\n1,2,3: "))
    if valik==1:
        EEKN = int(input("EUR: "))
        eru = round(EEK * EEKN)
        print(f"{EEKN} eurot on {eru} eesti krooni")
    elif valik==2:
        EURN = int(input("EEK: "))
        eku = float(EURN * 0.06)
        print(f"{EURN} eesti krooni on {round(eku)} eurot")
    elif valik==3:
        break
    else:
        print("Midagi läks valesti, proovi uuesti.")