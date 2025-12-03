from util.input_management import ingest_input

def initialise_input(test=True):
    input = ingest_input("01",test,"\n")
    return input

def solution(input):
    rotations = [convert_dir_to_sign(x) for x in input]
    position = 50
    password = 0

    for rotation in rotations:
        if position == 0 and rotation <0: 
            password -= 1
        position = position + rotation
        while position < 0:
            position += 100
            password += 1
        while position > 99:
            position -= 100
            password += 1
        if rotation < 0 and position == 0:
            password += 1
    print(password)

def convert_dir_to_sign(x):
    if x[0]=='L': 
        return int(x[1:])*-1 
    else: 
        return int(x[1:])

input = initialise_input(False)
solution(input)