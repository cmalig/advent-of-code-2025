from util.input_management import ingest_input

def initialise_input(test=True):
    input = ingest_input("05", test, "\n")
    blank_index = input.index("")
    fresh_ids, available_ids = input[:blank_index], list(map(int,input[blank_index+1:]))
    fresh_ids = [list(map(int,id.split("-"))) for id in fresh_ids]
    return fresh_ids, available_ids

def get_min(id):
    return id[0]

def find_diffs(ids):
    ans = 0
    for id in ids:
        ans += id[1]-id[0]+1
    return ans

def solution_1(fresh_ids, available_ids):
    available_fresh = 0 
    for available_id in available_ids:
        for fresh_id in fresh_ids:
            if fresh_id[0] <= available_id <= fresh_id[1]:
                available_fresh += 1
                break
    return available_fresh

def solution_2(fresh_ids):
    fresh_ids.sort(key=get_min)
    new_ids = []
    i = 0
    id_len = len(fresh_ids)
    while i < id_len:
        j = i + 1
        check_max = fresh_ids[i][1]
        while j < id_len and check_max >= fresh_ids[j][0]:
            check_max = max(check_max, fresh_ids[j][1])
            j += 1
        new_range = [fresh_ids[i][0],check_max]
        new_ids.append(new_range)
        i = j
    return find_diffs(new_ids)

fresh_ids, available_ids = initialise_input(False)

print(solution_1(fresh_ids,available_ids))
print(solution_2(fresh_ids))
