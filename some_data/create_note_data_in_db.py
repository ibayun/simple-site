import csv
from users.models import User
from notes.models import Note
import random


u = User.objects.values_list("id", flat=True)
with open("some_data/sw_data_new.csv") as f:
    readers = csv.reader(f)
    for row in readers:
        title, text = row
        note = Note.objects.create(title=title, body=text, created_by=User.objects.get(id=random.choice(u)))


#
# test_title = "Hello again"
# test_body = "I like this place"
# note = Note.objects.create(title=test_title, body=test_body, created_by=User.objects.get(id=random.choice(u)))
