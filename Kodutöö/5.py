# Alar Tammes 15.05.2025
# Ülesanne 5
loop = 1
List = []
while loop == 1:
    Shop = input("Mida ostame: ")
    List.append(Shop)
    if Shop == "":
        break
print("Ostukorv: ")
for item in List:
    print(item)