tah = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","Z"]
num = ["1","2","3","4","5","6","7","8","9","0"]

numbrimark = input("Numbrimärgi kontroll: ")
if len(numbrimark) > 6 or len(numbrimark) < 6:
    print("Ei sobi")
if numbrimark[0] and numbrimark[1] and numbrimark[2] in tah:
        if numbrimark[3]and numbrimark[4]and numbrimark[5] in num:
            print("Sobib")
        else:
            print("ei Sobi")

    