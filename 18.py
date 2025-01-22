import csv
faili_nimi = 'est.csv'

with open(faili_nimi, mode='r', encoding='utf-8') as fail:

    dict_reader = csv.reader(fail)
    print(dict_reader)
    for rida in dict_reader:
        print(rida)
fass = open(faili_nimi)
tiimide_arv = fass.readlines(1)
fass.close()
print(tiimide_arv)