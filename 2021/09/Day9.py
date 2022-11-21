import os

# Author: Cole Polyak
# 9 December 2021
# Advent of Code: Day 9

# These are points we've already attributed to another basin, and can skip.
processed_points = set()

def main():
    arr = parse_input("day9.txt")

    part1(arr)

    # k, v
    # size of basin, the points in the basin.
    basin_sizes = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i, j) in processed_points:
                continue

            possibilities = [
                check_point(i, (j + 1), arr),
                check_point(i, (j - 1), arr),
                check_point((i + 1), j, arr),
                check_point((i - 1), j, arr)
            ]

            if arr[i][j] < min(possibilities):
                basin_sizes.append(perform_bfs(i, j, arr))


    sizes_sorted = sorted(basin_sizes)
    one = sizes_sorted.pop()
    two = sizes_sorted.pop()
    three = sizes_sorted.pop()
    print(f"outputting: {one} -- {two} -- {three}")
    print(f"product -- {one[0] * two[0] * three[0]}")

def part1(arr):
    low_points = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            possibilities = [
                check_point(i, (j + 1), arr),
                check_point(i, (j - 1), arr),
                check_point((i + 1), j, arr),
                check_point((i - 1), j, arr)
            ]

            if arr[i][j] < min(possibilities):
                low_points += (1 + arr[i][j])
    print(f"low points --- {low_points}")

def perform_bfs(i, j, arr):
    visited = set()
    queue = [(i, j)]

    while(len(queue) != 0):
        point = queue.pop()

        if point in visited:
            continue

        visited.add(point)
        processed_points.add(point)
        queue = queue + visit_point(point, visited, arr)

    print(f"Finished BFS, returning {len(visited)}")
    return (len(visited), visited)


def visit_point(point, visited, arr):
    to_visit = []
    i, j = point

    if check_point(i, j + 1, arr) <= 8:
        to_visit.append((i, j + 1))

    if check_point(i, j - 1, arr) <= 8:
        to_visit.append((i, j - 1))

    if check_point(i + 1, j, arr) <= 8:
        to_visit.append((i + 1, j))

    if check_point(i - 1, j, arr) <= 8:
        to_visit.append((i - 1, j))

    return to_visit


def check_point(i, j, arr):
    # PYTHON LISTS CAN HAVE NEGATIVE INDEXES.
    if i < 0 or j < 0:
        return 10

    try:
        return arr[i][j]
    except IndexError:
        # Returning the the highest possible value in this single-digit space.
        return 10

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        row = [char for char in line.strip()]
        arr.append(list(map(lambda x: int(x), row)))

    return arr

if __name__ == '__main__':
    main()
