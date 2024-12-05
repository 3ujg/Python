#1.1
#import turtle
#
#turtle.write("Tere, maailm!",font=("Arial", 30, "normal"))
#
#turtle.done()

#1.2
#import turtle
#
#aasta = 2020
#liblikas = "teelehe-mosaiikliblikas"
#lause_keskosa = ". aasta liblikas on "
#lause = str(aasta)+""+lause_keskosa+""+liblikas
#
#turtle.write(lause,font=("Arial", 30, "normal"))
#
#turtle.done()

#1.3
#vastus = int(input("Kui kõrgel on pilve alus(km): "))
#if vastus > 6:
#    print("See on ülemine pilv!")
#    print("See on keskmine pilv!")
#else:
#    print("Alumine pilv!")

#1.4
#inimeste_arv = int(input("Mitu inimest on: "))
#kohtade_arv = int(input("Mitu kohta on: "))
#busside_arv = inimeste_arv // kohtade_arv
#viimases_bussis_inimesi = inimeste_arv % kohtade_arv
#if viimases_bussis_inimesi > 0:
#    busside_arv = busside_arv+1
#print(f"Inmeste arv: {inimeste_arv}\nKohtade arv: {kohtade_arv}\nBusse vaja: {busside_arv}\nViimases bussis inimesi: {viimases_bussis_inimesi}")

#2.1
#k = int(input("Sisestage mitu korda äratada: "))
#
#for i in range(k):
#    print("Tõuse ja sära!")

#2.2

#2.3
#import random
#k = int(input("Täringute arv on: "))
#
#for i in range(k):
#    number = random.randint(1,6)
#    print(number)

#2.4
k = int(input("Mitu ruutu on: "))
for i in range(k):
    nisutera = 1
    nisutera = nisutera * 2
print(nisutera)
    


    
