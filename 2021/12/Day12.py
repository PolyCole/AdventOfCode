import os

# Author: Cole Polyak
# X December 2021
# Advent of Code: Day X

# Python program to print all paths from a source to destination.

from collections import defaultdict

class Part1Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_list = [[]]

    def add_edge(self, origin, terminus):
        self.graph[origin].append(terminus)

    def depth_first_search(self, cur_node, visited):
        visited.append(cur_node)

        if cur_node == "end":
            self.visited_list.append(visited)
            return

        for node in self.graph[cur_node]:
            if node.isupper():
                self.depth_first_search(node, visited.copy())
            else:
                if node not in visited:
                    self.depth_first_search(node, visited.copy())

        self.visited_list.append(visited)

    def perform_dfs(self):
        visited_list = [[]]
        self.depth_first_search("start", [])

class Part2Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_list = [[]]
        self.visited_small_cave = False

    def add_edge(self, origin, terminus):
        self.graph[origin].append(terminus)

    def depth_first_search(self, cur_node, visited, can_visit_small_cave):
        visited.append(cur_node)

        if cur_node == "end":
            self.visited_list.append(visited)
            return

        for node in self.graph[cur_node]:
            if node == "start":
                continue

            if node.isupper():
                self.depth_first_search(node, visited.copy(), can_visit_small_cave)
            else:
                if can_visit_small_cave and node in visited:
                    self.depth_first_search(node, visited.copy(), False)
                else:
                    if node not in visited:
                        self.depth_first_search(node, visited.copy(), can_visit_small_cave)

        self.visited_list.append(visited)

    def perform_dfs(self):
        visited_list = [[]]
        self.depth_first_search("start", [], True)


def main():
    arr = parse_input("day12.txt")
    g = Part1Graph()
    g2 = Part2Graph()

    for origin, terminus in arr:
        g.add_edge(origin, terminus)
        g.add_edge(terminus, origin)

        g2.add_edge(origin, terminus)
        g2.add_edge(terminus, origin)

    output_dfs(g, "for Part 1")
    output_dfs(g2, "for Part 2")


def output_dfs(g, fluff):
    g.perform_dfs()

    kept_paths = []
    for path in g.visited_list:
        if "start" not in path:
            continue

        if "end" not in path:
            continue

        kept_paths.append(path)

    print(f"There are {len(kept_paths)} unique paths {fluff}.")

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        processed = line.strip().split("-")
        arr.append((processed[0], processed[1]))

    return arr

if __name__ == '__main__':
    main()
