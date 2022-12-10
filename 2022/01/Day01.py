import os

# Author: Cole Polyak
# 01 December 2022
# Advent of Code: Day 01

def main():
    arr = parse_input("day01.txt")
    print("\n\n\n*****************")
    print(f"arr: {arr}")


def parse_input(filename):
    file = open(f"{os.getcwd()}/01/{filename}", "r")

    cur_sum = 0
    sums = []

    for line in file:
        if line.strip() == '':
            sums.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(line.strip())

    sums.append(cur_sum)

    # O(nlog(n)
    sums.sort()
    sums = sums[::-1]
    
    print(f"Part one answer: {sums[0]}")
    print(f"Part two answer: {sum(sums[0:3])}")

if __name__ == '__main__':
    main()
