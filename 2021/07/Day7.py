import os

# Author: Cole Polyak
# 7 December 2021
# Advent of Code: Day 7

# For part 2 we need to essentially get the value of:
# SUM(range(1, num_steps + 1))
# That's an annoying calculation, but we only want to do it once. So let's
# put it into a map. (steps, fuel_cost)
crab_movement_costs = {}

def main():
    arr = parse_input("day7.txt")

    density_list = [0]

    for num in arr:
        num = int(num)
        while(len(density_list) <= num):
            density_list.append(0)
        density_list[num] += 1

    min_fuel_cost = -1
    for position in range(0, len(density_list)):
        cur_fuel_cost = 0

        for crabs_to_move in range(0, len(density_list)):
            if crabs_to_move == position:
                continue

            movement_cost= get_movement_cost(abs((crabs_to_move - position)))

            cur_fuel_cost += density_list[crabs_to_move] * movement_cost

        if min_fuel_cost == -1 or min_fuel_cost > cur_fuel_cost:
            min_fuel_cost = cur_fuel_cost

    print(f"I think it'd cost {min_fuel_cost}")

def get_movement_cost(spaces):
    if spaces in crab_movement_costs:
        return crab_movement_costs[spaces]
    else:
        cost = sum(range(1, spaces + 1))
        crab_movement_costs[spaces] = cost
        return cost


def parse_input(filename):
    file = open(f"{os.getcwd()}/{filename}", "r")
    return file.readline().strip().split(",")

if __name__ == '__main__':
    main()
