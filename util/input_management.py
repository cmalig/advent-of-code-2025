def ingest_input(day,test,split_char):
    path = "day" + day + "/"
    if test == True:
        path = path + 'test_input.txt'
    else:
        path = path + 'input.txt'
    myfile = open(path,"r")
    data = myfile.read()
    myfile.close()
    return data.split(split_char)
