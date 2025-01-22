import codecs
x = input("1. Uus sõna.\n2. Teisenda tagasi\n:")
false = "True"
while false == "True":
    if x == "1":
        v = input("Kirjuta: ")
        y = codecs.encode(v, 'rot13') #Muudab sõna rot13 peale
        print(y)
    elif x == "2":
        y = input("Transleeri: ")   
        codecs.decode(y, 'rot13')

    else:
        print("Midagi läks valesti proovi uuesti.")

    print(y)
    smth = input("1. Originaalne sõna.\n2. Uus sõna/vale")
    if smth == "1":
        print(v)
