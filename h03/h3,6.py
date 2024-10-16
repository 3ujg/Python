#16.10.24 Allu
#Ülesanne 03
import turtle
#Ülesanne 3.5: Unistuste auto
mark, mudel = "bmw", "118"
auto = mark+" "+ mudel
aasta = 1997
hind = 381.60

print("Minu unistuste auto on",auto,"aastast",aasta,", mille hind on",hind,"eurot")


"""
#Ülesanne 3.6: Python Turtle kolmnurk
kylje_pikkus = 100
nurk = 120
kujundi_varv = "purple"

turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.forward(kylje_pikkus)
        turtle.left(nurk)

    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()


turtle.done()

