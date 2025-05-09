# Alar Tammes 09.05.2025

import random

oiged = 0
valed = 0
for _ in range(10):
    j = random.randint(1,10)
    k = random.randint(1,10)
    tehe = "*"
    
    print(f"{j} {tehe} {k} = ")
    vastus = int(input("Vastus: "))
    if vastus == j*k:
        print ("ÕIGE")
        oiged+=1
    else:
        print("vale!")
        valed+=1
print(f"{oiged} õiget vastust ja {valed} valet vastust")
