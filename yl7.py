# 22.10 Tammes
# ülesanne 7 loendid

%m




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


