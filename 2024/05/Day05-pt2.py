import os

# Author: Cole Polyak
# 05 December 2024
# Advent of Code: Day 05

def main():
    arr = parse_input("day05.txt")

    rules = arr[0:arr.index("")]
    manuals = arr[arr.index("")+1:]
    rule_dict = build_rules(rules)

    total = 0

    for manual in manuals:
        pages = manual.split(",")
        pointer = len(pages) - 1

        if is_valid(pages, rule_dict):
            continue

        # Basically, we're establishing a "known good" section at the end of the list.
        # We'll walk the pointer backwards, swapping elements into place
        # When swapping, we'll move the pointer back to the place we just swapped to
        while(not is_valid(pages, rule_dict)):
            seen = get_seen(pages, pointer)
            all_good = True
            if pages[pointer] in rule_dict:
                before = rule_dict[pages[pointer]]
                for b in before:
                    if b in seen:
                        target_index = seen[b]
                        pages = swap_indices(pages, pointer, target_index)
                        pointer = max(pointer, target_index)
                        all_good = False
            if all_good:
                pointer -= 1
        
        total += int(pages[len(pages) // 2])

    print(f"TOTAL: {total}")

def get_seen(pages, index):
    seen = {}
    for i in range(0, index):
        seen[pages[i]] = i

    return seen

def is_valid(pages, rule_dict):
    seen = set()
    for page in pages:
            seen.add(page)
            if page in rule_dict:
                before = rule_dict[page]
                for b in before:
                    if b in seen:
                        return False
    
    return True

def swap_indices(pages, i, j):
    temp = pages[i]
    pages[i] = pages[j]
    pages[j] = temp

    return pages

# The rule dict is a dictionary where the key is the page
# and the value is a list of pages that must come before it.
def build_rules(rules):
    rule_dict = {}

    for rule in rules:
        rule = rule.split("|")
        if rule[0] in rule_dict:
            rule_dict[rule[0]].append(rule[1])
        else:
            rule_dict[rule[0]] = [rule[1]]

    return rule_dict


def parse_input(filename):
    file = open(f"{os.getcwd()}/05/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
