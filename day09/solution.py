from util.input_management import ingest_input
import itertools
from shapely.geometry import Polygon, box
import matplotlib.pyplot as plt

def initialise_input(test=True):
    input = ingest_input("09", test, "\n")
    input = [tuple(map(int,i.split(","))) for i in input]
    return input

def rectangle_size(point1, point2):
    return abs(point1[0]-point2[0]+1)*abs(point1[1]-point2[1]+1)

def find_other_corners(point1,point2):
    point3 = (point1[0],point2[1])
    point4 = (point2[0],point1[1])
    return point3, point4

def sort_biggest(square):
    return square[1]

def solution_1(input):
    combinations = list(itertools.combinations(input,2))
    max_size = 0
    rectangles = []
    for combo in combinations:
        size = rectangle_size(combo[0],combo[1])
        rectangles.append((combo,size))
        if size > max_size:
            max_size = size
    rectangles.sort(reverse = True, key=sort_biggest)
    print(max_size)
    return rectangles

def solution_2(input,rectangles):
    input.append(input[0])
    polygon = Polygon(input)
    plt.plot(*polygon.exterior.xy, c='g')
    print(polygon.is_valid)
    print(rectangles[0])
    for rectangle in rectangles:
        point1, point2 = rectangle[0][0], rectangle[0][1]
        x1, y1 = point1
        x2, y2 = point2
        rect_polygon = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if polygon.contains(rect_polygon):
            print(rectangle)
            break
    plt.plot(*rect_polygon.exterior.xy, c='b')
    plt.show()
    pass

input = initialise_input(False)
rectangles = solution_1(input)
solution_2(input,rectangles)