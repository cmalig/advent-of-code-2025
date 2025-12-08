from util.input_management import ingest_input
import math

def initialise_input(test=True):
    input = ingest_input("06", test, "\n")
    return input

def chunkify_list(input):
    result = []
    sublist = []
    for i in input:
        if i == '':
            if sublist:
                result.append(list(map(int,sublist)))
                sublist = []
        else:
            sublist.append(i)
    if sublist:
        result.append(list(map(int,sublist)))
    return result

def solution_1(input,debug=False):
    ans = 0
    input = [" ".join(i.split()).split() for i in input]
    input = list(zip(*input[::-1]))
    if debug: print(input)
    for i in input:
        if i[0] == "+":
            ans += sum(list(map(int,i[1:])))
        if i[0] == "*":
            ans += math.prod(list(map(int,i[1:])))
    return ans

def solution_2(input,debug=False):
    input = [list(i) for i in input]
    signs = [i for i in input[-1:][0] if i != " "]
    values = input[:-1]
    if debug: print(values)
    values = list(zip(*values[::-1]))
    if debug: print(values)
    values = ["".join(i[::-1]).strip() for i in values]
    if debug: print(values)
    values = chunkify_list(values)
    
    if debug: print(values)
    if debug: print(signs)
    
    ans = 0
    i = 0
    while i < len(signs):
        if signs[i] == "+":
            ans += sum(values[i])
        if signs[i] == "*":
            ans += math.prod(values[i])
        i += 1
    return(ans)

input = initialise_input(True)

print(solution_1(input))
print(solution_2(input, True))
