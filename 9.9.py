import random

tehted = ["+","-","*","/"]
punktid = 0
for _ in range(6):
    j = random.randint(1,10)
    k = random.randint(1,10)
    tehe = random.choice(tehted)
    if tehe=="+":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j+k:
            print ("ÕIGE")
            punktid+=1
        else:
            print("vale!")
    elif tehe=="-":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j-k:
            print ("ÕIGE")
            punktid+=1
        else:
            print("vale!")
    if tehe=="*":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j*k:
            print ("ÕIGE")
            punktid+=1
        else:
            print("vale!")
    else:
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j/k:
            print ("ÕIGE")
            punktid+=1
        else:
            print("vale!")


print(punktid)
