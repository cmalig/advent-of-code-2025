from util.input_management import ingest_input

def initialise_input(test=True):
    input = ingest_input("04", test, "\n")
    input = [list(i) for i in input]
    return input

def get_adjacents(map,row,col):
    adjacents = []
    for a_row, a_col in adjacency:
        c_row, c_col = row + a_row, col + a_col
        if 0 <= c_row < map_size[0] and 0 <= c_col < map_size[1] and map[c_row][c_col] == "@":
            adjacents.append((c_row,c_col))
    return adjacents

def solution_1(map,map_size):
    ans = 0
    for row in range(map_size[0]):
        for col in range(map_size[1]):
            if map[row][col] == "@": 
                if len(get_adjacents(map,row,col)) < 4:
                    ans +=1
    print(ans)

def solution_2(map,map_size):
    found_rolls = set()
    for row in range(map_size[0]):
        for col in range(map_size[1]):
            if map[row][col] == "@": 
                adj = get_adjacents(map,row,col)
                found_rolls.update(adj)
                if len(adj) < 4:
                    map[row][col] = "x"
                    try: 
                        found_rolls.remove((row,col))
                    except: continue
    print(f"found len {len(found_rolls)}: {found_rolls}")
    for row in map:
        print(row)
        
    iterate_check = True
    while iterate_check == True:
        remove_rolls = []
        for roll in found_rolls:
            adj = get_adjacents(map,roll[0],roll[1])
            if len(adj) < 4:
                map[roll[0]][roll[1]] = "x"
                remove_rolls.append(roll)
        print(f"removed len: {remove_rolls}")
        # for row in map:
        #     print(row)
        if len(remove_rolls) == 0:
            iterate_check = False
            break
        for roll in remove_rolls:
            found_rolls.remove(roll)
    count = 0
    for row in map:
        for col in row:
            if col == "x":
                count += 1
    print(count)

map = initialise_input(False)
map_size = (len(map),len(map[0]))
for row in map:
    print(row)
adjacency = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),(0,1),
    (1,-1),(1,0),(1,1)
]

solution_1(map,map_size)
solution_2(map,map_size)

