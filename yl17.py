# fail = open("Pangakonto.txt")
# loend = fail.readlines()

#print(f"Tehingud kokku{(len(loend))}")

#or i in loend:
#    if 1>0:
#        +i
#    append.float
#    print(i)
mpalgad = []
npalgad = []

fail = open("palgad.txt")
loend = fail.readlines()
for txt in loend:
    x = txt.split(",")[3]
    y = txt.split(",")[6]
    if x == "Mees":
        mpalgad.append(float(y))
    else:
        npalgad.append(float(y))
print(mpalgad)