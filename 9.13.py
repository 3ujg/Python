ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

labisoit = []
hinnad = []
kolmsada = []

for car in ev_data:
    for i in car:
        print(f"{i:30}", end=" ")
    if car[1] != "range" or car[2] != "price":
        labisoit.append(int(car[1]))
        if int(car[1])>=300:
            kolmsada.append(car[0])
        hinnad.append(int(car[2]))
        print(int(car[2])/int(car[1]))
    else:
        print("ratio")
    
    #for i in car:
    #    print(f"{i:<30}", end=" ")
    print()
print(f"Keskmine läbisõit {sum(labisoit)/len(labisoit)}")
print(f"Keskmine läbisõit {sum(hinnad)/len(hinnad)}€")
print(kolmsada)