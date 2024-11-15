import turtle
import random


def viisnurk(k):
    print("Joonistan viisnurga")
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,360))
        for i in range(5):
            turtle.fd(100)
            turtle.lt(144)
    

def ring(k):
    print("Joonistan ringi")
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,360))
        turtle.circle(50)
def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)

def suvaline(k):
    for i in range(k):
        my_list = [viisnurk, ring, ruut]
        random.choice(my_list)(1)


print("-----------------Fancy Program------------------")


loop = 1

while loop == 1:
    try:
        valik = int(input("1 -viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nLisa valik (1-4): "))
        kujunditeArv = int(input("Mitu kujundit soovid joonistada: "))
    except:
        print("game over")
        loop = 0
        break
    if valik =="" or kujunditeArv =="":
        loop = 0
        break

    if valik == 1:
        viisnurk(kujunditeArv)
    elif valik == 2:
        ring(kujunditeArv)
    elif valik == 3:
        ruut(kujunditeArv)
    else:
        suvaline(kujunditeArv)