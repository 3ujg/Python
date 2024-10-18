# 16.10.24 Tammes
# Ülesanded 04
import turtle

# Ringi pindala ja Turtle 
try:
    r = int(input("Sisesta ringi raadius: "))
    pi = 3.14
    s = pi*r**2
    p = 2*pi*r
    print(f"Ringi pindala on {s:2f} ja ümbermõõt on {p:2f}")
    turtle.circle(r, 360)
except:
    print("Tegid sisestamisel vea!")

turtle.done