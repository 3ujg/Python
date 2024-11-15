


def sarnased_esitahed(nimi):
    tykk = nimi.split(" ")
    if tykk[0][0] == tykk[0][0]:
        return True
    else:
        return False

    return tykk[1][0]




print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False