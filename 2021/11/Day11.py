import os
import sys

# Author: Cole Polyak
# 11 December 2021
# Advent of Code: Day 11

class Octopus:
    def __init__(self, energy):
        self.energy = energy

    def increment(self):
        self.energy += 1
        if self.energy >= 9:
            return True
        else:
            return False


def main():
    arr = parse_input("day11.txt")

    flash_count = 0
    step_flash_count = 0

    # for x in range(0, 100):
    step_count = 0
    while(True):
        # Iterate through entire array, increment every value. If value > 10, push into a queue.
        flash_queue = []

        print(f"{flash_count} -- {step_flash_count}")

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] += 1
                if arr[i][j] >= 10:
                    flash_queue.append((i, j))

        # Begin processing the queue, by "flashing" the octopus -- method iterating in a square around value, adding fully-charged octopus to queue.
        exclude_octopus = set()
        while(len(flash_queue) != 0):
            octo_i, octo_j = flash_queue.pop()

            if (octo_i, octo_j) in exclude_octopus:
                continue

            flash_queue = flash(octo_i, octo_j, arr, flash_queue, exclude_octopus)
            step_flash_count += 1
            exclude_octopus.add((octo_i, octo_j))

        flash_count += step_flash_count

        if step_flash_count == 100:
            print(f"All octopus flashed !!! Step: {step_count + 1}")
            sys.exit(0)
        step_flash_count = 0
        step_count += 1

        # print(f"I think {flash_count} octopus flashed")

def flash(i, j, arr, flash_queue, exclude_octopus):
    for r in range(i - 1, i + 2):
        row = ""
        for c in range(j - 1, j + 2):
            # If we're out of bounds, or at the center, we want to continue.
            if (r < 0) or (c < 0) or (r == i and c == j):
                continue

            if (r, c) in exclude_octopus:
                continue

            try:
                arr[r][c] += 1

                if arr[r][c] >= 10:
                    flash_queue.append((r, c))
            except IndexError:
                continue


    arr[i][j] = 0
    return flash_queue

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        arr.append(list(map(lambda x: int(x), [char for char in line.strip()])))

    return arr

if __name__ == '__main__':
    main()
