import os

# Author: Cole Polyak
# 8 December 2021
# Advent of Code: Day 8

def main():
    arr = parse_input("day8.txt")
    # arr2 = parse_input("day8-test3.txt")

    sum = 0
    for left, right in arr:
        sum += solve(left, right)

    print(f"Sum: {sum}")


def solve(left, right):
    # immediately, we can narrow down a bunch of possibilities.
    # (length of string, possible values)
    multiple_possibility_constants = {5: [2, 3, 5], 6: [0, 6, 9]}
    single_possibility_constants = {2: 1, 3: 7, 4: 4, 7: 8}

    # print(f"---------------------------------------")
    solved = [
        list(map(lambda x: "".join(sorted(x)), right.split(" "))),
        ["", "", "", ""]
    ]

    data = left.split(" ")
    known_values, possibilities = get_constants(data, multiple_possibility_constants, single_possibility_constants)

    while(not_solved(solved[1])):
        # print(f"{known_values}")

        solved = solve_knowns(solved, possibilities)

        for string, possible_values in possibilities.items():
            # print(f"{string} -- {possible_values}")
            if len(possible_values) == 1:
                continue

            # THREE CHECK
            if sorted(possible_values) == [2, 3, 5]:
                if 1 in known_values:
                    one = known_values[1]
                    # If we have a one for a base, and three extra characters, the only thing it can be is a 3.
                    if (one[0] in string) and (one[1] in string):
                        known_values[3] = string
                        possibilities[string] = [3]
                    else:
                        possibilities[string] = [2,5]

            # Nine Check
            if sorted(possible_values) == [0, 6, 9]:
                if 3 in known_values:
                    three = known_values[3]
                    # If we have a three for a base, and one extra character, the only thing it can be is a 9.
                    flag = True
                    for char in three:
                        flag = flag and (char in string)

                    if flag and len(string) == 6:
                        known_values[9] = string
                        possibilities[string] = [9]
                    else:
                        possibilities[string] = [0, 6]

            if sorted(possible_values) == [0, 6]:
                if 7 in known_values:
                    seven = known_values[7]

                    flag = True
                    for char in seven:
                        flag = flag and (char in string)

                    if flag:
                        possibilities[string] = [0]
                    else:
                        possibilities[string] = [6]

            if sorted(possible_values) == [2, 5]:
                if 9 in known_values:
                    nine = known_values[9]

                    diff = 0
                    for char in nine:
                        if char not in string:
                            diff += 1

                    if diff == 1:
                        possibilities[string] = [5]
                    else:
                        possibilities[string] = [2]
                elif 6 in known_values:
                    six = known_values[6]

                    diff = 0
                    for char in six:
                        if char not in string:
                            diff += 1

                    if diff == 1:
                        possibilities[string] = [5]
                    else:
                        possibilities[string] = [2]
                elif 4 in known_values:
                    four = known_values[4]

                    diff = 0
                    for char in four:
                        if char not in string:
                            diff += 1

                    if diff == 2:
                        possibilities[string] = [2]
                    else:
                        possibilities[string] = [5]

            possible_values = check_if_known(string, possible_values, known_values)

    output = "".join(list(map(lambda x: str(x),solved[1])))
    print(f"{left} ||| {right}: {output}")
    return int(output)

def get_constants(data, multiple_possibility_constants, single_possibility_constants):
    possibilities = {}
    known_values = {}

    # Check for constants.
    for option in data:
        option = "".join(sorted(option))
        if len(option) in single_possibility_constants:
            value = single_possibility_constants[len(option)]
            known_values[value] = option
            possibilities[option] = [value]
        else:
            possibilities[option] = multiple_possibility_constants[len(option)]

    return (known_values, possibilities)

def solve_knowns(solved, possibilities):
    for i in range(0, len(solved[0])):
        entry = possibilities[solved[0][i]]
        # We have a solved value.
        if len(entry) == 1:
            solved[1][i] = entry[0]
    return solved

def check_if_known(string, possible_values, known_values):
    # Now let's try to eliminate some values we may have already checked for.
    for value, characters in known_values.items():
        if value in possible_values:
            possible_values.remove(value)

    return possible_values


def not_solved(answers):
    flag = False
    for answer in answers:
        flag = flag or (answer == "")
    return flag


def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        split = line.strip().split("|")
        arr.append((split[0].strip(), split[1].strip()))

    return arr

if __name__ == '__main__':
    main()
