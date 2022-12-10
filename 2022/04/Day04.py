import os

# Author: Cole Polyak
# 04 December 2022
# Advent of Code: Day 04

def main():
    arr = parse_input("day04.txt")

    pt1_count = 0
    pt2_count = 0

    for one, two in arr:
        start1, end1 = one
        start2, end2 = two

        # Basically, the first point's start is less than the second's
        # and the first point's end is greater than the second's.
        # start1 --- start 2 --- end 2 --- end 1
        if (start1 <= start2) and  (end1 >= end2):
            pt1_count += 1
            pt2_count += 1
        # The second point's start is less than the first's
        # and the second point's end is greater than the first's
        # start2 --- start1 --- end1 --- end 2
        elif (start2 <= start1) and (end2 >= end1):
            pt1_count += 1
            pt2_count += 1
        # This one is tricky. Basically, the first point's end is greater
        # than the second point's start ~~AND~~ the first point's start is
        # less than the second point's end. 
        # start1 --- start2 --- end1 --- end2
        elif (end1 >= start2) and (start1 <= end2):
            pt2_count += 1

    print(f"Part 1 count: {pt1_count}\nPart 2 count: {pt2_count}")

def parse_input(filename):
    file = open(f"{os.getcwd()}/04/{filename}", "r")
    arr = []

    convert_to_int = lambda r: (int(r[0]), int(r[1])) 

    for line in file:
        # ["2-3", "3-4"]
        pair = line.strip().split(",")
        arr.append(
            (
                # ["2", "3"] -> (2,3)
                convert_to_int(pair[0].split("-")), 
                # ["3", "4"] -> (3,4)
                convert_to_int(pair[1].split("-"))
            ) # -> ((2,3), (3,4))
        )

    file.close()
    return arr

if __name__ == '__main__':
    main()
