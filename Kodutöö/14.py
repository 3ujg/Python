# Alar Tammes 09.05.2025
# Ülesanne 14

mpalgad = [] #meeste palgad
npalgad = [] #naiste palgad

fail = open("palk.txt", "r") # Avab faili
loend = fail.readlines() # Loeb joon kaupa
for txt in loend:
    nimi, perenimi, soo, palk = txt.split() # Jagab andmed stringideks
    palk = int(palk)
    if soo == "m":
        mpalgad.append(palk)
    else:
        npalgad.append(palk)
mkpalgad = sum(mpalgad)/len(mpalgad)
nkpalgad = sum(npalgad)/len(npalgad)
print(f"Meeste keskmine palk{mkpalgad}")
print(f"Naiste keskmine palk {nkpalgad}")
if mkpalgad > nkpalgad:
    print("Mehed saavad rohkem palka.")
elif mkpalgad < nkpalgad:
    print("Naised saavad rohkem palka.")
else:
    print("Maailmas on rahu.")
fail.close()
