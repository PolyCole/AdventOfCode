import os

# Author: Cole Polyak
# 3 December 2021
# Advent of Code: Day 3

def main():
    arr = parse_input("day3.txt")
    part1(arr)
    part_2_solution(arr)


def find_matching_number(nums, want_most_common: bool):
    mcb_list = nums.copy()
    lcb_list = nums.copy()

    print(f"{len(mcb_list)}  {len(lcb_list)}")

    for i in range(0, len(nums[0])):
        most_common_bit = int(find_most_common_bit(nums, i))
        least_common_bit = int(not bool(most_common_bit))

        mcb_list = mcb_list if type(mcb_list) is str else prune_list(mcb_list, most_common_bit, i)
        lcb_list = lcb_list if type(lcb_list) is str else prune_list(lcb_list, least_common_bit, i)

def prune_list(num_list, desired_bit, index):
    if len(num_list) == 1:
        print(f"boop {num_list}")
        return num_list[0]

    ok_list = []
    for num in num_list:
        if int(num[index]) == desired_bit:
            ok_list.append(num)
    return ok_list


def find_most_common_bit(nums, index):
    zeroes = 0
    ones = 0

    for num in nums:
        if int(num[index]) == 0:
            zeroes += 1
        else:
            ones += 1

    return 0 if zeroes > ones else 1


def part_2_solution(arr):
    mcb_match = find_matching_number(arr, True)
    lcb_match = find_matching_number(arr, False)
    print(f"{mcb_match}, {lcb_match}")
    answer = int(mcb_match, 2) * int(lcb_match, 2)

    print(f"I think the answer for Part 2 is {answer}")


def part1(arr):
    gamma_rate = 0
    epsilon_rate = 0

    for i in range(0, len(arr[0])):
        most_common_bit = find_most_common_bit(arr, i)
        least_common_bit = int(not bool(most_common_bit))

        # Originally was building a string (gross), bit shifting is faster.
        # gamma_rate += str(most_common_bit)
        gamma_rate  = int(bin((gamma_rate | most_common_bit) << 1), 2)
        epsilon_rate  = int(bin((epsilon_rate | least_common_bit) << 1), 2)

    # Knocking off extra bit
    gamma_rate = int(bin(gamma_rate >> 1), 2)
    epsilon_rate = int(bin(epsilon_rate >> 1), 2)

    answer = gamma_rate * epsilon_rate
    print(f"I think the answer for Part 1 is: {answer}")

def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())
    file.close()
    return arr

if __name__ == '__main__':
    main()
