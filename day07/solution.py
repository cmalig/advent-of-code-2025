from util.input_management import ingest_input

def initialise_input(test=True):
    input = ingest_input("07", test, "\n")
    input = [list(i) for i in input]
    del input[1::2] #remove uneeded even rows
    return input

def tree_split(pos):
    return [pos-1,pos+1]

def solution_1(input):
    ans = 0
    check_list = {input[0].index("S")}
    for row in input:
        removes = set()
        adds = set()
        for check in check_list: 
            if row[check] == "^":
                ans += 1
                removes.add(check)
                adds.update(tree_split(check))
        for remove in removes:
            check_list.remove(remove)
        check_list.update(adds)
    return ans

def solution_2(input,debug=False):
    ans_arr = [0]*len(input[0])
    for row in input:
        for i, symbol in enumerate(row):
            if symbol == '.':
                continue
            elif symbol == '^':
                ans_arr[i-1]+=ans_arr[i]
                ans_arr[i+1]+=ans_arr[i]
                ans_arr[i] = 0
            elif symbol == 'S':
                ans_arr[i] += 1
            if debug: print(ans_arr)
    return sum(ans_arr)


input = initialise_input(True)

print(solution_1(input))

print(solution_2(input,True))