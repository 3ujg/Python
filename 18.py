import csv
import pandas
faili_nimi = 'est.csv'

with open(faili_nimi, mode='r', encoding='utf-8') as fail:

    dict_reader = csv.reader(fail)
    print(dict_reader)
    for rida in dict_reader:
        len(df.index)
        print(rida)