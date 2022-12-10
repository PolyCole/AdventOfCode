import os

# Author: Cole Polyak
# 08 December 2022
# Advent of Code: Day 08

class Grid:
    def __init__(self):
        self.forest = []
    
    def add_row(self, row):
        self.forest.append(row)
    
    def index_is_visible(self, x, y):
        right = self.check_right(x, y)
        left = self.check_left(x, y)
        up = self.check_up(x, y)
        down = self.check_down(x, y)

        return left or right or up or down
    
    def index_score(self, x, y):
        right = self.check_right(x, y)
        left = self.check_left(x, y)
        up = self.check_up(x, y)
        down = self.check_down(x, y)

        if right * left * up * down == 720000:
            print(f"({self.forest[x][y]}), {x}, {y}")
            print(f"UP {up} DOWN {down} LEFT {left} RIGHT {right}")


        return right * left * up * down
    
    def check_up(self, x, y):
        if x == 0:
            # return True
            return 1

        trees = 0
        for cur in range(x - 1, -1, -1):
            trees += 1
            if self.forest[cur][y] >= self.forest[x][y]:
                return trees
        
        # return True
        return trees

    def check_down(self, x, y):
        try:
            self.forest[x + 1][y]
        except IndexError:
            # return True
            return 1
        
        trees = 0
        for cur in range(x + 1, len(self.forest)):
            trees += 1
            if self.forest[cur][y] >= self.forest[x][y]:
                # return False
                return trees
        
        # return True
        return trees
    
    def check_left(self, x, y):
        try:
            self.forest[x][y + 1]
        except IndexError:
            # return True
            return 1

        trees = 0
        for cur in range(y - 1, -1, -1):
            trees += 1
            if self.forest[x][cur] >= self.forest[x][y]:
                # return False
                return trees
        
        # return True
        return trees

    def check_right(self, x, y):
        if y == 0:
            # return True
            return 1
        
        trees = 0
        for cur in range(y + 1, len(self.forest[x])):
            trees += 1
            if self.forest[x][cur] >= self.forest[x][y]:
                # return False
                return trees 
        
        # return True
        return trees

    def __str__(self):
        return str(self.forest)


def main():
    grid = parse_input("day08.txt")

    # count = 0
    # success = []
    
    # for x in range(0, len(grid.forest)):
    #     for y in range(0, len(grid.forest[x])):
    #         if grid.index_is_visible(x, y):
    #             count += 1
    #             success.append(grid.forest[x][y])

    scenic = -1
    for x in range(0, len(grid.forest)):
        for y in range(0, len(grid.forest[x])):
            scenic = max(grid.index_score(x, y), scenic)
    
    print(f"Answer:::: {scenic}")

def parse_input(filename):
    grid = Grid()

    file = open(f"{os.getcwd()}/08/{filename}", "r")
    arr = []

    for line in file:
        grid.add_row(list(map(lambda x: int(x), list(line.strip()))))

    file.close()
    return grid

if __name__ == '__main__':
    main()
