# Alar Tammes 09.05.2025
# Ülesanne 14

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
mkpalgad = sum(mpalgad) / len(mpalgad)
nkpalgad = sum(npalgad) / len(npalgad)
print(f"Meeste keskmine palk{mkpalgad}")
print(f"Naiste keskmine palk {nkpalgad}")
if mkpalgad > nkpalgad:
    print("Meeste keskmine palk on suurem.")
elif mkpalgad < nkpalgad:
    print("Naiste keskmine palk on suurem.")
else:
    print("Maailmas on rahu.")
fail.close()
