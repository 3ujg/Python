domeen = input("Palun sisesta aadress: ")

s = domeen.split(".")

if s[2] == "ee":
    print("Eesti domeen")
else:
    print("Valesti")