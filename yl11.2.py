def kolm_pikimat_sona(a):
    sonastik = {}
    for i in a:
        sonastik[i] = len(i)
    sorteeritud = sorted(sonastik.items(), key = lambda x:x[1], reverse = True)
    for j in range(3):
        print(sorteeritud[j][0])
    

sonad = ("üks", "kaks", "viis", "kolmsada", "mustmiljon")

kolm_pikimat_sona(sonad)