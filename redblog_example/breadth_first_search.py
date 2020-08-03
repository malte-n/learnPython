# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
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
