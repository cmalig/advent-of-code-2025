from util.input_management import ingest_input
import textwrap

def initialise_input(test=True):
    input = ingest_input("02",test,",")
    input = [x.split("-") for x in input]
    return input

def solution(input):
    valid_set = []
    for i in input:
        for r in range(int(i[0]),int(i[1])+1):
            valid_subset = set()
            for n in range(1,6):
                if len(str(r))%n==0 and len(str(r)) != n:
                    if invalid_check(chunkify_string(str(r),n)):
                        valid_subset.add(str(r))
            if len(valid_subset)>0:
                valid_set.append(list(valid_subset))
    ans = 0
    for x in valid_set:
        ans += int(x[0])
    print(ans)

def invalid_count(min,max):
    #make min lowest even in range
    if len(min)%2 == 1:
        min = '1' + '0'*len(min)
    elif int(min[:len(min)//2]) < int(min[len(min)//2:]):
        min = str(int(min[:len(min)//2])+1)*2
    #make max highest even in range
    if len(max)%2 == 1:
        max = '9'*(len(max)-1)
    elif int(max[:len(max)//2]) > int(max[len(max)//2:]):
        max = str(int(max[:len(max)//2])-1)*2
    #check range still makes sense
    if int(max) < int(min): 
        return 0
    #return 1 if range only has one value THIS HAS AN ISSUE TO FIX... 68 - 68 should be 0
    elif min == max and min[:len(min)//2] == min[len(min)//2:]:
        return min
    elif min == max:
        return 0
    # This returns the amount of invalids, i need the actual invalids
    # return int(max[:len(max)//2]) - int(min[:len(min)//2]) + 1
    invalids = list(range(int(min[:len(min)//2]),int(max[:len(max)//2])+1))
    count = 0
    for invalid in invalids:
        count += int(str(invalid)*2)
    return count

def chunkify_string(x,chunk_size):
    if len(x)%chunk_size != 0: print("ERROR, can't chunk")
    return textwrap.wrap(x, chunk_size)

def invalid_check(x):
    set_x = set(x)
    if len(set_x) == 1: return True
    else: return False

input = initialise_input(True)
solution(input)