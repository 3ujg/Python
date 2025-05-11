# Alar Tammes 09.05.2025
import codecs

false = "True"
while false == "True":
    x = input("1. Uus sõna.\n2. Teisenda tagasi\n3. Lõpeta tegum.\n:")
    if x == "1":
        v = input("Kirjuta: ")
        y = codecs.encode(v, 'rot13') #Muudab sõna rot13 peale
        print(f'Krüpteeritud sõna: {y}')
    elif x == "2":
        x = input("Transleeri: ")   
        z = codecs.decode(x, 'rot13') #V6ttab s2na rot13 ja muudab tagasi
        print(f'Dekrüpteeritud sõna: {z}')
    elif x == "3":
        break
    else:
        print("Midagi läks valesti proovi uuesti.")