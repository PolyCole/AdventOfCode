import os

# Author: Cole Polyak
# 13 December 2021
# Advent of Code: Day 13

class Grid:
    def __init__(self):
        self.grid = []

    def build_grid(self, points):
        maxx = 0
        maxy = 0

        for x,y in points:
            maxx = max(maxx, x)
            maxy = max(maxy, y)

        for i in range(0, maxy + 1):
            row = []
            for j in range(0, maxx + 1):
                row.append(False)
            self.grid.append(row)

    def mark_point(self, x, y):
        self.grid[y][x] = True

    def output_grid(self):
        for i in range(len(self.grid)):
            row = ""
            for j in range(len(self.grid[i])):
                value = "#" if self.grid[i][j] else "."
                row += f"{value} "
            print(row)

    def fold(self, direction, line):
        if direction == "x":
            self.fold_x(line)
        else:
            self.fold_y(line)

    def fold_x(self, line):
        mirror = self.get_mirror(False)

        for i in range(len(mirror)):
            for j in range(len(mirror[i])):
                if j > line:
                    self.grid[i][j] = False
                    continue
                else:
                    if mirror[i][j]:
                        self.grid[i][j] = True

        new_grid = []
        for row in self.grid:
            new_grid.append(row[0:line])
        self.grid = new_grid

    def fold_y(self, line):
        mirror = self.get_mirror(True)

        for i in range(len(mirror)):
            for j in range(len(mirror[i])):
                if i > line:
                    self.grid[i][j] = False
                    continue
                else:
                    if mirror[i][j]:
                        self.grid[i][j] = True

        new_grid = []
        for row in range(len(self.grid)):
            if row < line:
                new_grid.append(self.grid[row])
        self.grid = new_grid

    def get_mirror(self, is_y):
        if is_y:
            rotated90 = list(zip(*self.grid.copy()[::-1]))
            start = list(zip(*rotated90[::-1]))
        else:
            start = self.grid.copy()

        mirror = []
        for row in start:
            mirror.append(list(row[::-1]))
        return mirror

    def count_lit_points(self):
        count = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j]:
                    count += 1
        return count


def main():
    points, instructions = parse_input("day13.txt")
    grid = Grid()
    grid.build_grid(points)

    for x,y in points:
        grid.mark_point(x, y)

    for axis, line in instructions:
        print(f"Folding {axis} -- {line}")
        grid.fold(axis, line)

    grid.output_grid()
    print(f"{grid.count_lit_points()}")

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    points = []
    instructions = []

    flag = False

    for line in file:
        if flag == False and line.strip() == '':
            flag = True
            continue

        if "fold along" not in line.strip():
            points.append(tuple(map(lambda x: int(x), line.strip().split(","))))
        else:
            processed = line.split("=")
            instructions.append((processed[0][-1], int(processed[1])))

    return (points, instructions)

if __name__ == '__main__':
    main()
