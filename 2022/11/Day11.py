import os

# Author: Cole Polyak
# 11 December 2022
# Advent of Code: Day 11


# Monkey Class
    # Has to track number of times it inspects something
    # Has an inventory list (because new items are added on the end)
    # Has a Test function
        # we need to read in the number on the line, and then use that
        # in our Test Function.
        # We also need Monkey directions. If True, If False.
    # Operation
        # Need to read in the symbol and the value. Then do math based on that.

class Monkey:
    def __init__(self):
        self.inventory = []
        self.inspected = 0

        self.test = None
        self.operation = None
    
    def inspect(self, index):
        val = self.inventory[index]
        val = self.operation(val)
        # val = val // 3 # relief operation.
        self.inspected += 1
        self.inventory[index] = val
    
    def throw_item(self):
        destination = self.test(self.inventory[0])
        item = self.inventory.pop(0)
        return (destination, item)

    def set_operation(self, symbol, value):
        if symbol == "+":
            self.operation = lambda x: x + int(value)
        else:
            if value == "old":
                self.operation = lambda x: x * x
            else:
                self.operation = lambda x: x * int(value)
    
    def set_test(self, val, true_monkey, false_monkey):
        self.test = lambda x: int(true_monkey) if x % val == 0 else int(false_monkey)
    
    def __str__(self):
        to_return = "Monkey:\n"
        to_return += f"{self.inventory}\n"
        to_return += f"{self.inspected}\n"
        return to_return

# General flow
    # Initialize monkeys.
    # Loop 20 times (rounds)
    #   Loop over monkeys (Turns)
    #       Each monkey starts turn by calculating Worry level
    #       Then monkey evaluates test and throws.

def main():
    print("\n\n")
    monkeys, magic_number = parse_input("day11.txt")

    for i in range(0, 10000):
        if i % 100 == 0:
            print(f"on round: {i}")
        for monkey in monkeys:
            for j in range(0, len(monkey.inventory)):
                monkey.inspect(j)
                monkey.inventory[j] %= magic_number
            
            while len(monkey.inventory) != 0:
                dest, item = monkey.throw_item()
                monkeys[dest].inventory.append(item)
    
    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspected)
    
    inspect_counts.sort(reverse = True)

    print(f"ANSWER: {inspect_counts[0] * inspect_counts[1]}")


def parse_input(filename):
    file = open(f"{os.getcwd()}/11/{filename}", "r")
    arr = []
    magic_number = 1

    while True:
        monkey = Monkey()
        try:
            file.readline().strip() # monkey
            items = get_items(file.readline().strip())
            op_symb, op_val = get_operation(file.readline().strip())
            test_val = get_test_val(file.readline().strip())
            test_true = get_test_true(file.readline().strip())
            test_false = get_test_false(file.readline().strip())
            file.readline() # blank

            monkey.inventory = items
            monkey.set_operation(op_symb, op_val)
            monkey.set_test(test_val, test_true, test_false)
            arr.append(monkey)
            magic_number *= test_val

        except ValueError as e:
            file.close()
            return (arr, magic_number)

def get_items(line):
    items = line.replace("Starting items: ", "").strip().split(",")
    items = list(map(lambda x: int(x), items))
    return items

# Return (symbol, value)
def get_operation(line):
    op = line.replace("Operation: new = old ", "").split(" ")
    return (op[0], op[1])

def get_test_val(line):
    return int(line.replace("Test: divisible by ", "").strip())

def get_test_true(line):
    return int(line.replace("If true: throw to monkey ", "").strip())

def get_test_false(line):
    return int(line.replace("If false: throw to monkey ", "").strip())
    

if __name__ == '__main__':
    main()
