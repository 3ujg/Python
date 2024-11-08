# 1.
# arvud = []
# loop = 1

# while loop == 1:
#     arv = input("Anna mulle number: ")
#     if arv=="":
#         break
#     arvud.append(int(arv)) 

# print(sum(arvud)/len(arvud))
import random
# 2.
arvamused = []
suv = random.randint(1,10)
loop = 1
katsed = 0

while loop==1:
    arva = int(input("Arva arv 1-10: "))
    katsed+=1
    if arva == suv:
        print("Õige")
        print(f"Sul oli {katsed} katseid!")
        arvamused.append(katsed)
        uuesti = input("Tahad uuesti proovida (j/e): ")
        if uuesti=="j":
            suv = random.randint(1,10)
            katsed = 0
        break
    else:
        print("Proovi uuesti!")
print("Game over!")
print(f"Sa tegid {katsed} katseid")