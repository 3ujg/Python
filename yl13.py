
import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()


# Küsi kasutajalt numbrilist sisendit
#vanus = screen.numinput("Vanuse sisestamine", "Nis on sinu vanus?", default=20, minival=0, maxval=100)
nr = 10
for i in range(nr*10):
    t.lt(90)
    t.fd(3)
    t.lt(180)
    t.fd(3)
    t.lt(90)
    t.fd(4)
t.goto(0,0)


for i in range(nr+1):
    t.lt(90)
    t.fd(5)
    t.write(i, font=("Arial", 10, "normal"))
    t.lt(180)
    t.fd(5)
    t.lt(90)
    t.fd(9*4)


turtle.done()