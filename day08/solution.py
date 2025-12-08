from util.input_management import ingest_input
import math
import itertools

def initialise_input(test=True):
    input = ingest_input("08", test, "\n")
    input = [tuple(map(int,i.split(","))) for i in input]
    return input

def sort_func(l):
    return l[1]

def solution_1(input,depth,debug=False):
    combinations = list(itertools.combinations(input,2))
    combo_distance = []
    for combo in combinations:
        combo_distance.append((combo,math.dist(combo[0],combo[1])))
    combo_distance.sort(key = sort_func)
    combo_distance = combo_distance[0:depth]
    circuit_dict = {}
    circuit = 1
    for dist in combo_distance:
        a = circuit_dict.get(dist[0][0])
        b = circuit_dict.get(dist[0][1])
        #print(f"processing {dist} a:{a},b:{b}")
        if a == None and b == None:
            circuit_dict[dist[0][0]] = circuit
            circuit_dict[dist[0][1]] = circuit
            if debug: print(f"circuit {circuit} created, adding {dist[0][0]} and {dist[0][1]}")
            circuit += 1
        elif a == None:
            print(f"{dist[0][1]} is a match, adding {dist[0][0]} to circuit {b}")
            circuit_dict[dist[0][0]] = b
        elif b == None:
            print(f"{dist[0][0]} is a match, adding {dist[0][1]} to circuit {a}")
            circuit_dict[dist[0][1]] = a
        elif b == a:
            pass
        else:
            print(f"processing {dist} a:{a},b:{b} {dist[0][0][0] * dist[0][1][0]}")
            print(f"make circuit {b} into circuit {a}")
            if debug: print(circuit_dict)
            for i in circuit_dict.keys():
                if circuit_dict[i] == b:
                    circuit_dict.update({i:a})
                if debug: print(i, circuit_dict[i])
    circuit_list = list(circuit_dict.values())
    count_list = dict.fromkeys(circuit_list,0)
    for x in count_list.keys():
        count_list[x] = circuit_list.count(x)
    count_list_values = list(count_list.values())
    count_list_values.sort(reverse = True)
    count_list_values_top = count_list_values[0:3]
    if debug: print(count_list_values_top)
    print(math.prod(count_list_values_top))


input = initialise_input(False)
#solution_1(input,1000)
solution_1(input,10000000000,False)