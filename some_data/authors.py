# nickname, email, password, first_name, last_name
import csv


def read_file(name_file):
    with open(f"{name_file}") as file:
        contain = [line.rstrip().strip(" ") for line in file.readlines()]
        return contain


first_name = read_file("first_name.txt")
last_name = read_file("last_name.txt")
email = read_file("emails.txt")
nickname = read_file("nickname.txt")
passwords = read_file("passwords.txt")
res = list(zip(first_name, last_name, email, nickname, passwords))

with open("all_authors.csv", "w") as f:
    writer = csv.writer(f)
    for row in res:
        writer.writerow(row)
