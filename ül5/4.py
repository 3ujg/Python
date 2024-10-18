# 18.10.24 Tammes
# Ülesanne 5
import random
import turtle

# 4. Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
suv = random.randint(0,1)
kasutaja_valik = input("Kull või kiri: ")

if suv==1 and kasutaja_valik=="kull" or (suv==1 and kasutaja_valik=="kiri"):
    varv = "green"
else:
    varv = "red"

print(suv)
turtle.color(varv)
turtle.circle(50,360)
turtle.done