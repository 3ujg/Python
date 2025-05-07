# Alar Tammes 07.05.2025
mpalgad = []
npalgad = []

fail = open("palk.txt")
loend = fail.readlines()
for txt in loend:
    x = txt.split(",")[3]
    y = txt.split(",")[6]
    if x == "m":
        mpalgad.append(float(y))
    else:
        npalgad.append(float(y))
print(mpalgad)