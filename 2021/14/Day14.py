import os

# Author: Cole Polyak
# 14 December 2021
# Advent of Code: Day 14

def main():
    seed, instructions = parse_input("day14-test.txt")

    instruction_set = {}
    for lookup, mutation in instructions:
        instruction_set[lookup] = mutation
    print(f"Part1: {part1(seed, instruction_set)}")
    print(f"Part2: {part2(seed, instruction_set)}")


def part1(polymer, instruction_set):
    for x in range(10):
        polymer_split = [char for char in polymer]
        transformed_polymer = []
        for i in range(len(polymer_split) - 1):
            cur_segment = f"{polymer_split[i]}{polymer_split[i + 1]}"

            transformed_polymer.append(polymer_split[i])
            if cur_segment in instruction_set:
                transformed_polymer.append(instruction_set[cur_segment])

        transformed_polymer.append(polymer_split[-1])
        together = "".join(transformed_polymer)
        polymer = together

    polymer = [char for char in polymer]
    frequency = {}

    for char in polymer:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max = float('-inf')
    min = float('inf')
    for char, freq in frequency.items():
        if freq > max:
            max = freq

        if freq < min:
            min = freq
    return max - min

def part2(polymer, instruction_set):
    queue = [char for char in polymer]

    for x in range(40):
        print(f"Step: {x}")
        new_queue = []
        while(len(queue) > 1):
            left = queue.pop(0)
            right = queue[0]
            cur = f"{left}{right}"

            new_queue.append(left)
            if cur in instruction_set:
                new_queue.append(instruction_set[cur])
            new_queue.append(right)
        new_queue.append(queue.pop(0))
        queue = new_queue


    frequency = {}

    for char in queue:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max = float('-inf')
    min = float('inf')
    for char, freq in frequency.items():
        if freq > max:
            max = freq

        if freq < min:
            min = freq
    return max - min

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    instructions = []
    seed = file.readline().strip()
    file.readline()

    for line in file:
        p = line.split(" -> ")
        instructions.append((p[0].strip(), p[1].strip()))

    return (seed, instructions)

if __name__ == '__main__':
    main()
