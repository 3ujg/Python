# Alar Tammes 07.05.2025
mpalgad = []
npalgad = []

fail = open("palk.txt", "r")
loend = fail.readlines()
for txt in loend:
    nimi, perenimi, soo, palk = txt.split()
    palk = int(palk)
    if soo == "m":
        mpalgad.append(palk)
    else:
        npalgad.append(palk)
print(mpalgad)