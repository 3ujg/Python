import os
import datetime

nimi = os.getlogin()

print (f"tere {nimi}")

print(f"Sa oled: {os.getcwd()}")

kokku = 3
x = datetime.datetime.now().strftime('%Y%m%d')
try:
    for i in range(kokku):
        os.mkdir(x+"_"+str(i+1))
except:
    print("Sul on juba need kataloogid")