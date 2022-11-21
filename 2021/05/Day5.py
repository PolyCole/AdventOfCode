import os
import math

# Author: Cole Polyak
# 5 December 2021
# Advent of Code: Day 5

class Grid:
    def __init__(self, maxes):
        self.grid = self.init_grid(maxes)

    def init_grid(self, maxes):
        x, y = maxes
        grid = []
        for i in range(0, (y + 1)):
            row = []
            for j in range(0, (x + 1)):
                row.append(0)
            grid.append(row)
        return grid

    def draw_horiz_line(self, start, stop, y):
        for i in range(start, stop + 1):
            self.grid[y][i] += 1

    def draw_vert_line(self, start, stop, x):
        for i in range(start, stop + 1):
            self.grid[i][x] += 1

    def draw_diagonal_line_pos(self, start, stop):
        cur_x, cur_y = start
        goal_x, goal_y = stop

        while((cur_x != goal_x + 1) and (cur_y != goal_y + 1)):
            self.grid[cur_y][cur_x] += 1
            cur_x += 1
            cur_y += 1

    def draw_diagonal_line_neg(self, start, stop):
        if start[0] > stop[0]:
            hold = start
            start = stop
            stop = hold
        
        cur_x, cur_y = start
        goal_x, goal_y = stop

        while((cur_x != goal_x + 1) and (cur_y != goal_y - 1)):
            self.grid[cur_y][cur_x] += 1
            cur_x += 1
            cur_y -= 1


    def count_overlapping_vents(self):
        overlap = 0
        for row in self.grid:
            for num in row:
                if num > 1:
                    overlap += 1
        return overlap

    def __str__(self):
        output = ""

        for row in self.grid:
            output += "\n"
            for num in row:
                if num < 10:
                    output += " "

                num_out = num if num != 0 else "."
                output += f"{num_out}"

        return output




def main():
    lines, maxes = parse_input("day5.txt")
    grid = Grid(maxes)

    for line in lines:
        start, stop = line

        print(f"Drawing {start}, {stop}")

        # X coordinate matches, it's vertical.
        if start[0] == stop[0]:
            grid.draw_vert_line(start[1], stop[1], start[0])
        # Y coordinate matches, it's horizontal.
        elif start[1] == stop[1]:
            grid.draw_horiz_line(start[0], stop[0], start[1])
        # It's a diagonal line. This'll be part 2.
        else:
            if slope(start, stop) > 0:
                grid.draw_diagonal_line_pos(start, stop)
            else:
                grid.draw_diagonal_line_neg(start, stop)

    # print(f"{grid}")
    print(f"Overlap: {grid.count_overlapping_vents()}")

def slope(start, stop):
    m = (stop[1] - start[1]) / (stop[0] - start[0])
    return m

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")

    max_x = 0
    max_y = 0

    lines = []

    for line in file:
        split_points = line.split(" -> ")

        left_points, left_dist = extract_coords(split_points[0].strip())
        right_points, right_dist = extract_coords(split_points[1].strip())

        max_x = left_points[0] if left_points[0] > max_x else max_x
        max_x = right_points[0] if right_points[0] > max_x else max_x
        max_y = left_points[1] if left_points[1] > max_y else max_y
        max_y = right_points[1] if right_points[1] > max_y else max_y

        if left_dist > right_dist:
            lines.append((right_points, left_points))
        elif right_dist > left_dist:
            lines.append((left_points, right_points))
        # They're equal, let's paint a diag.
        else:
            if left_points[0] < right_points [0]:
                lines.append((left_points, right_points))
            else:
                lines.append((right_points, left_points))


    return (lines, (max_x, max_y))

def extract_coords(coords):
    vals = coords.split(",")
    x = int(vals[0])
    y = int(vals[1])

    point = (x , y)

    return (point, math.dist((0,0), point))


if __name__ == '__main__':
    main()
