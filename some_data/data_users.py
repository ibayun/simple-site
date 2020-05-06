from some_data.readeble import notes_authors


a = notes_authors()
while True:
    try:
        data = next(a)
        title, text, name = data
        print(title, text, name)
    except StopIteration:
        print("done!")
        break
