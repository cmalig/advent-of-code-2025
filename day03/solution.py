from util.input_management import ingest_input
import numpy as np

def initialise_input(test=True):
    input = ingest_input("03",test,"\n")
    input = [list(i) for i in input]
    input = [list(map(int,a)) for a in input]
    return input

def part1(banks):
    ans = 0
    for bank in banks:
         ans += max_power(bank)
    print(f"P1 ans: {ans}")

def part2(banks):
    ans = 0
    for bank in banks:
         ans += max_power_12(bank)
    print(f"P2 ans: {ans}")

def convert_to_int(x):
    x = list(map(str,x))
    res = ''.join(x)
    return int(res)

def find_max(l):
    max_idx = np.argmax(l)
    max_val = l[max_idx]
    return max_val, max_idx

def max_power(b):
    elem1, elem1_idx = find_max(b[:-11])
    elem2, elem2_idx = find_max(b[elem1_idx+1:-10])
    return int(str(elem1)+str(elem2))

def max_power_12(b):
    max_arr = []
    elem_idx = 0
    end_pointer = 3
    while len(max_arr) < 12:
        elem, elem_idx = find_max(b[0:end_pointer+1])
        max_arr.append(elem)
        b = b[elem_idx+1:]
        end_pointer = end_pointer-elem_idx
    return convert_to_int(max_arr)

banks = initialise_input(True)
part1(banks)
part2(banks)