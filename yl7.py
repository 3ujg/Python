# 22.10 Tammes
# ülesanne 7 loendid

import datetime

x = datetime.datetime.now()
tana 0 int(x.strftime("%m")) - 1

# 12 kuud

# ülesanne
print(kuud[tana[0]])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana])
    print(kuud[tana][i+1], end=", ")
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(f"-20 esineb {ajutine.count(-20)} korda")
ajutine.pop(5)
print(ajutine)


"""
# Jukebox
muusika = ['ALIKA – “Bridges”',
           'Anett x Fredi – “Read Between The Lines”',
           'villemdrillem – “leekiv armastus”',
           'Clicherik & Mäx – “PAKSUD”',
           'nublu – “ära ärata”',
           'NOËP – “Move Your Feet”',
           'Trad.Attack! – “Bring It On”',
           'Bedwetters – “It Is What It Is”',
           'Reket – “Panama paberid”',
           'Grete Paia – “Võluväel”']

for i in range(len(muusika)):
    print(str(i+1)+". "+muusika[i])

try:
    valik = int(input("Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagi läks valesti. Teavita adminni")


