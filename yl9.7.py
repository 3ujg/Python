#ülesanne 9

ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
meeles = []


for opilane in ryhma_hinded:
    meeles.append(float(opilane.split(" ")[1]))
print(f"parim tulemus {max(meeles)}")
print(f"parim tulemus {min(meeles)}")
print(f"parim tulemus {round(sum(meeles)/len(meeles),2)}")