def ingest_input(day,test,split_char):
    path = "day" + day + "/"
    if test:
        path = path + 'test_input.txt'
    else:
        path = path + 'input.txt'
    with open(path, "r") as myfile:
        data = myfile.read()
    return data.split(split_char)
