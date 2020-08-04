# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
# Implementation explained https://www.redblobgames.com/pathfinding/a-star/implementation.html#python
# Explained graphs: https://www.redblobgames.com/pathfinding/grids/graphs.html
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

import collections


class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


example_graph = SimpleGraph()
example_graph.edges = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["A"],
    "D": ["E", "A"],
    "E": ["B"],
}

# a wrapper for the built-in collections.deque
class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search_1(graph, start):

    # initialize Queue class with its properties
    frontier = Queue()
    # append start position
    frontier.put(start)
    reached = {}
    # set value for first key to True, adds key automatically as well
    reached[start] = True

    # start loop queue.empty = len(elements) == 0 until every elements value is filled
    while not frontier.empty():
        print(frontier.empty())
        # takes id[0], assigns it to current and then removes it
        current = frontier.get()
        print("Visiting %r" % current)
        # starts loop, iterating over the values of the "current" key-value pair
        for i in graph.neighbors(current):
            print("i: %r" % i)
            # if the value is not in the reached dict yet, append it as key
            # for the last element "E" i = "B", which is already in reached["B"] = True
            # All elements values are filled and the while loop stops
            if i not in reached:
                frontier.put(i)
                print("Element of frontier: %r" % frontier.elements)
                # sets the value of the respective key to true
                reached[i] = True
    print(reached)


breadth_first_search_1(example_graph, "A")


# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)


def draw_tile(graph, id, style, width):
    r = "."
    if "number" in style and id in style["number"]:
        r = "%d" % style["number"][id]
    if "point_to" in style and style["point_to"].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style["point_to"][id]
        if x2 == x1 + 1:
            r = ">"
        if x2 == x1 - 1:
            r = "<"
        if y2 == y1 + 1:
            r = "v"
        if y2 == y1 - 1:
            r = "^"
    if "start" in style and id == style["start"]:
        r = "A"
    if "goal" in style and id == style["goal"]:
        r = "Z"
    if "path" in style and id in style["path"]:
        r = "@"
    if id in graph.walls:
        r = "#" * width
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


# data from main article
DIAGRAM1_WALLS = [
    from_id_width(id, width=30)
    for id in [
        21,
        22,
        51,
        52,
        81,
        82,
        93,
        94,
        111,
        112,
        123,
        124,
        133,
        134,
        141,
        142,
        153,
        154,
        163,
        164,
        171,
        172,
        173,
        174,
        175,
        183,
        184,
        193,
        194,
        201,
        202,
        203,
        204,
        205,
        213,
        214,
        223,
        224,
        243,
        244,
        253,
        254,
        273,
        274,
        283,
        284,
        303,
        304,
        313,
        314,
        333,
        334,
        343,
        344,
        373,
        374,
        403,
        404,
        433,
        434,
    ]
]


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


def breadth_first_search_2(graph, start, goal):
    # return "came_from"
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):

            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    print("came_from: %s" % came_from)
    return came_from


g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

parents = breadth_first_search_2(g, (8, 7), (17, 2))
draw_grid(g, width=2, point_to=parents, start=(8, 7), goal=(17, 2))
