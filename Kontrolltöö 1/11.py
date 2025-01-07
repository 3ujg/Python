import random
tah = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"

kogus = int(input("Mitu numbri märki?: "))
for i in range(kogus):
    tahed = ""
    numbrid = ""
    for i in range(3):
        tahed += random.choice(tah)
    
    for i in range(3):
        numbrid += random.choice(num)

    print("Siin on numbri märk", tahed,numbrid)