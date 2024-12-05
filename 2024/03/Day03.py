import os
import re

# Author: Cole Polyak
# 03 December 2024
# Advent of Code: Day 03

def main():
    arr = parse_input("day03.txt")
    sum = 0

    count = 0
    
    for line in arr:
        pattern = r"mul\((\d+),(\d+)\)"    

        pattern_do = r"do\(\)"
        pattern_dont = r"don\'t\(\)"

        matches_do = [(match.group(), match.start()) for match in re.finditer(pattern_do, line)]
        matches_dont = [(match.group(), match.start()) for match in re.finditer(pattern_dont, line)]

        dos = assemble_set(matches_do)
        dont = assemble_set(matches_dont)

        matches = [(match.group(1), match.group(2), match.start()) for match in re.finditer(pattern, line)]

        for match in matches:
            x = match[0]
            y = match[1]
            start = match[2]

            flag = True
            for i  in range(0, start):
                if i in dos:
                    flag = True
                
                if i in dont:
                    flag = False

            if flag:
                count += 1
                sum += int(x) * int(y)
            print("\n")
        

    print(sum)

def assemble_set(matches): 
    result = set()

    for match in matches:
        result.add(int(match[1]))

    return result

def parse_input(filename):
    file = open(f"{os.getcwd()}/03/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
