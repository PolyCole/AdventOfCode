import os

# Author: Cole Polyak
# 12 December 2022
# Advent of Code: Day 12

MAX = 1000000000000000000
seen = set()

def main():
    grid, start_coords = parse_input("day12-test.txt")
    print(f"GRID:{grid}\nSTARTING:{start_coords}")

    print(f"ANSWER: {perform_bfs(grid, start_coords)}")

def perform_bfs(grid, start_coords):
    queue = [(start_coords, [start_coords])]
    shortest_path = MAX

    while len(queue) != 0:
        cur_node = queue.pop()

        position, path = cur_node
        cur_i, cur_j = position

        if grid[cur_i][cur_j] == "E":
            print(f"FOUND END ---- {len(path)}")
            print(f"{path}")
            shortest_path = min(shortest_path, len(path))
            continue

        seen.add(position)

        # check surrounding, and add to queue.
        left = (cur_i, cur_j - 1)
        if can_traverse(grid, position, left): # left
            # print(f"Can visit left: {left} -- ({grid[left[0]][left[1]]})")
            queue.append((left, [*path, left]))

        right = (cur_i, cur_j + 1)
        if can_traverse(grid, position, (cur_i, cur_j + 1)): # right
            # print(f"Can visit right: {right} -- ({grid[right[0]][right[1]]})")
            queue.append((right, [*path, right]))

        down = (cur_i - 1, cur_j)
        if can_traverse(grid, position, (cur_i - 1, cur_j)): # down
            # print(f"Can visit down: {down} -- ({grid[down[0]][down[1]]})")
            queue.append((down, [*path, down]))

        up = (cur_i + 1, cur_j)
        if can_traverse(grid, position, (cur_i + 1, cur_j)): # up
            # print(f"Can visit up: {up} -- ({grid[up[0]][up[1]]})")
            queue.append((up, [*path, up]))
    
    return shortest_path


def can_traverse(grid, start, end):
    if end in seen:
        return False

    start_i, start_j = start
    end_i, end_j = end

    if end_i < 0 or end_j < 0:
        return False

    try:
        start_val = grid[start_i][start_j]

        if start_val == "S":
            start_val = "`"

        end_val = grid[end_i][end_j]

        print(f"{start_val} - {end_val} == {abs(ord(start_val) - ord(end_val))}")


        if end_val == "E":
            return True

        return abs(ord(start_val) - ord(end_val)) == 1

    except IndexError:
        return False

def parse_input(filename):
    file = open(f"{os.getcwd()}/12/{filename}", "r")
    arr = []

    for line in file:
        if "S" in line:
            start = (len(arr), line.find("S"))

        arr.append([char for char in line.strip()])

    file.close()
    return arr, start

if __name__ == '__main__':
    main()
