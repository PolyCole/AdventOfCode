import os

# Author: Cole Polyak
# 09 December 2022
# Advent of Code: Day 09

transformation = {
                "R": lambda i, j: (i, j-1),
                "L": lambda i, j: (i, j+1),
                "U": lambda i, j: (i-1, j),
                "D": lambda i, j: (i+1, j)
            }

class Grid:
    def __init__(self):
        self.grid = []
        self.tails = []

        cur = []
        for i in range(0, 21):
            for j in range(0, 26):
                cur.append(0)
            self.grid.append(cur)
            cur = []
        
        # Head is 2, Tail is 1.
        center_i = len(self.grid) // 2
        center_j = len(self.grid[0]) // 2

        for x in range(0, 9):
            self.tails.append((center_i, center_j))

        self.grid[center_i][center_j] = 3
        self.head_i = center_i
        self.head_j = center_j

        self.tail_i = center_i
        self.tail_j = center_j

        self.last_movement = ""


    
    def move_head_right(self):
        self.grid[self.head_i][self.head_j + 1] += 2
        self.remove_head()
        self.head_j += 1
        self.update_movement("R")
    
    def move_head_left(self):
        self.grid[self.head_i][self.head_j - 1] += 2
        self.remove_head()
        self.head_j -= 1
        self.update_movement("L")

    def move_head_up(self):
        self.grid[self.head_i + 1][self.head_j] += 2
        self.remove_head()
        self.head_i += 1
        self.update_movement("U")

    def move_head_down(self):
        self.grid[self.head_i - 1][self.head_j] += 2
        self.remove_head()
        self.head_i -= 1
        self.update_movement("D")

    def update_movement(self, move):
        self.last_movement = move
        self.move_tails()
    
    def remove_head(self):
        self.grid[self.head_i][self.head_j] -= 2

    def remove_tail(self):
        self.grid[self.tail_i][self.tail_j] -= 1
    
    def replace_tail(self):
        self.grid[self.tail_i][self.tail_j] += 1
    
    def move_tails(self):
        prev = (self.head_i, self.head_j)
        for tail in range(0, len(self.tails)):
            cur = self.tails[tail]
            self.tails[tail] = self.move_tail(prev, cur)
        
    def move_tail(self, prev, cur):
        prev_i, prev_j = prev
        cur_i, cur_j = cur

        far_laterally = abs(prev_i - prev_j) >= 2
        far_horizontally = abs(self.tail_j - self.head_j) >= 2

        # We're offset or too far on the grid, need to correct tail.
        if far_laterally or far_horizontally:
            self.remove_tail()
            self.tail_i, self.tail_j = transformation[self.last_movement](self.head_i, self.head_j)
            self.replace_tail()

    def __str__(self):
        out = ""

        for i in range(0, len(self.grid)):
            row_str = ""
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j] >= 2:
                    cell_val = "H"
                elif self.grid[i][j] == 1:
                    cell_val = "T"
                else:
                    cell_val = "."

                row_str += f"{cell_val} "
            out  = f"{row_str}\n{out}"
        
        return out
    



def main():
    # represented as ["direction", "quant"]
    instructions = parse_input("day09-test2.txt")

    grid = Grid()
    tail_places = set()

    methods = {
        "U": grid.move_head_up,
        "D": grid.move_head_down,
        "L": grid.move_head_left,
        "R": grid.move_head_right
    }

    for direction, quant in instructions:
        for x in range(0, int(quant)):
            methods[direction]()
            tail_places.add((grid.tail_i, grid.tail_j))
            print(f"{grid}\n")
    
    print(f"Total tail places: {len(tail_places)}")

    # We need a 2d grid. 
    # Methods for move head left, right, up, down.
    # complex case is when tail is off-set from head and we do the "jerk" motion to get it in place.
    # We'll also need a set of tuples representing (i, j) points where the tail has visited. 

    # So basically, hard case is when tail shares no i, j values with head.
    # In that case, we'll need to put the tail to the opposite direction of movement alongside the head.

def parse_input(filename):
    file = open(f"{os.getcwd()}/09/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip().split(" "))

    file.close()
    return arr

if __name__ == '__main__':
    main()
