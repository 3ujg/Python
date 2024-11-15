#Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
#Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone: deposiit (raha lisamine) ja väljavõte (raha eemaldamine). Tagastage peale igat toimingut konto jääk.
#Funtsiooni parameetrid:

pangakonto = 15

def konto_haldur(saldo, toiming, summa):
    """
    Eriti oluline dokumentatsioon, et kõik aru saaks
    """
    global pangakonto
    if toiming=="deposiit":
        summa = summa + saldo
    else:
        summa = summa + saldo
    
    pangakonto = summa
    return summa

print(konto_haldur(20,"deposiit", pangakonto))
print(konto_haldur(40,"deposiit", pangakonto))