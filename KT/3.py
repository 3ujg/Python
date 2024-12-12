#4.1
#banner = input("Mis banneriks valisid: ")
#k = int(input("Mitu korda soovid printida: "))
#for i in range (k):
#    print(str.upper(banner))

#4.2
# õunte_kogus = int(input("Mitu õuna on: "))
# mahlapakkide_arv = round(õunte_kogus*0.4/3)
# print(f"Mahla on {mahlapakkide_arv} liitrit")

#4.3
Kutsutud_inimesed = int(input("Kui palju inimesi on kutsutud?: "))
inimesed_tulevad = int(input("Kui palju inimesi tuleb?: "))
maksimaalne_eelarve = Kutsutud_inimesed * 10 + 55
minimaalne_eelarve = inimesed_tulevad * 10 + 55
print(f"{Kutsutud_inimesed} Inimest on kutsutud\n{inimesed_tulevad} Inimest tuleb\n{maksimaalne_eelarve} on maksimaalne eelarve\n{minimaalne_eelarve} on minimaalne eelarve")