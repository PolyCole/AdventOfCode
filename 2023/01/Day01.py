import os

# Author: Cole Polyak
# 01 December 2022
# Advent of Code: Day 01

def main():
    arr = parse_input("day01.txt")
    sum = 0

    for line in arr:
        # Lmao don't do it like this for part 2
        line=line.replace("one", "o1e")
        line=line.replace("two", "t2o")
        line=line.replace("three", "t3e")
        line=line.replace("four", "f4r")
        line=line.replace("five", "f5e")
        line=line.replace("six", "s6x")
        line=line.replace("seven", "s7n")
        line=line.replace("eight", "e8t")
        line=line.replace("nine", "n9e")

        left = 0
        right = len(line) - 1
        
        while True:
            if not line[left].isdigit():
                left += 1

            if not line[right].isdigit():
                right -= 1

            if line[left].isdigit() and line[right].isdigit():
                break
    
        print(f'selected: {int(line[left] + line[right])}\n')
        sum += int(line[left] + line[right])
        continue

    print(f'Final total: {sum}')


def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
