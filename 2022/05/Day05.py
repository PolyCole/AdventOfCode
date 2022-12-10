import os

# Author: Cole Polyak
# 05 December 2022
# Advent of Code: Day 05

test_stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
    
stacks = [
    ["F", "C", "P", "G", "Q", "R"],
    ["W", "T", "C", "P"],
    ["B", "H", "P", "M", "C"],
    ["L", "T", "Q", "S", "M", "P", "R"],
    ["P", "H", "J", "Z", "V", "G", "N"],
    ["D", "P", "J"],
    ["L", "G", "P", "Z", "F", "J", "T", "R"],
    ["N", "L", "H", "C", "F", "P", "T", "J"],
    ["G", "V", "Z", "Q", "H", "T", "C", "W"]
]

def main():
    arr = parse_input("day05.txt")
    part1(arr)
    part2(arr)
    

def part2(arr):
    for movement in arr:
        quant, origin, destination = movement

        elems = []
        
        for x in range(0, quant):
            elems.append(stacks[origin - 1].pop())

        while len(elems) != 0:
            stacks[destination - 1].append(elems.pop())
        
    result = ""
    for stack in stacks:
        result += stack.pop()
    
    print(f"Result: {result}")



def part1(arr):
    for movement in arr:
        quant, origin, destination = movement

        for x in range(0, quant):
            elem = stacks[origin - 1].pop()
            stacks[destination - 1].append(elem)
        
    result = ""
    for stack in stacks:
        result += stack.pop()
    
    print(f"Result: {result}")

def parse_input(filename):
    file = open(f"{os.getcwd()}/05/{filename}", "r")
    arr = []

    for line in file:
        line = line.strip().split(" ")
        arr.append((int(line[1]), int(line[3]), int(line[5])))
    
    file.close()
    return arr

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

if __name__ == '__main__':
    main()
