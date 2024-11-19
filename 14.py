import turtle
ekraan = turtle.Screen()

def muuda_varvi_red():
    print("punane")
    turtle.color("red")

def muuda_varvi_green():
    print("roheline")
    turtle.color("green")

def muuda_varvi_blue():
    print("sinine")
    turtle.color("blue")

def ruut(x,y):
    print(x,y)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.fd(50)
        turtle.lt(90)
 
def paremKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
 
def keskmineKlikk(x, y):
    turtle.undo()

def puhasta_ekraan(x,y):
    turtle.clear()
 
ekraan.onscreenclick(ruut, 1) # Vasak klõps
ekraan.onscreenclick(puhasta_ekraan, 3) # Parem klõps
ekraan.onscreenclick(keskmineKlikk, 2) # Keskmine klõps
ekraan.onkey(muuda_varvi_red, "r")
ekraan.onkey(muuda_varvi_green, "g")
ekraan.onkey(muuda_varvi_blue, "b")

ekraan.listen() 
turtle.mainloop()
 