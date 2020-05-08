import csv
import random


def notes_authors():
    name = ["Anton", 'Ivan', 'Stepan', "Ernest"]
    with open('sw_data_new.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            title, text = row
            data = title, text, name[random.randint(0, len(name)-1)]
            # print("\t\t{} \n {} \t{}\n\n".format(title, text, name[random.randint(0, len(name)-1)]))
            yield data
