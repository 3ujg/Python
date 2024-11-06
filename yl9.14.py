import turtle





#6
#a = 100
#for i in range(4):
#    turtle.fd(a)
#    turtle.lt(90)
#    turtle.fd(a/3)
#    turtle.lt(90)
#    turtle.fd(a)
#    turtle.lt(90)
#    turtle.fd(a/3)


#13
#d = 100
#turtle.speed(0)

#k = 5
#for i in range(5):
#    turtle.fd(d/2)
#    turtle.lt(120)
#    for i in range(2):
#        turtle.fd(d)
#        turtle.lt(120)    
#    turtle.fd(d/2)
#    turtle.lt(360/k) #ei teadnud, et 360 kraadi pidi mõttesse võtma

#14
d = 100
turtle.speed(0)

k = 20
for i in range(20):
    turtle.left(360/k)
    turtle.penup()
    turtle.fd(d/2)
    turtle.pendown()
    turtle.lt(90)
    turtle.fd(d/2)
    turtle.lt(90)
    for i in range(3):
        turtle.fd(d)
        turtle.lt(90)
    turtle.fd(d/2)
    turtle.lt(90)
    turtle.penup()
    turtle.fd(d/2)
    turtle.pendown()
    turtle.lt(90)

turtle.done()
