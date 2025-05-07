import codecs

false = "True"
while false == "True":
    x = input("1. Uus sõna.\n2. Teisenda tagasi\n:")
    if x == "1":
        v = input("Kirjuta: ")
        y = codecs.encode(v, 'rot13') #Muudab sõna rot13 peale
        print(y)
    elif x == "2":
        x = input("Transleeri: ")   
        z = codecs.decode(x, 'rot13')
        print(z)
    elif x == "3":
        break
    else:
        print("Midagi läks valesti proovi uuesti.")