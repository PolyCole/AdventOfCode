import os

# Author: Cole Polyak
# 07 December 2022
# Advent of Code: Day 07

class Directory:
    def __init__(self, name):
        self.directories = {}
        self.files = []
        self.sum = -1
        self.name = name
    
    def get_sum(self):
        if self.sum != -1:
            return self.sum
        
        if len(self.files) == 0 and len(self.directories) == 0:
            self.size = 0
            return 0

        sum = 0
        for directory in self.directories:
            sum += self.directories[directory].get_sum()

        for file in self.files:
            sum += file

        self.sum = sum
        return self.sum 
    
    def add_file(self, file):
        self.files.append(int(file))
    
    def add_directory(self, name):
        self.directories[name] = Directory(name)

    def __str__(self):
        one = f"DIRS: {list(self.directories.keys())}\n"
        two = f"FILES: {self.files}"
        return one + two


def main():
    arr = parse_input("day07.txt")

    root = Directory("root")
    history = [root]
    cur_dir = root

    # Constructing tree.
    for command in arr:
        if command == "$ cd /":
            continue
            
        command_parsed = command.split(" ")
        
        # Dealing with a command
        if command_parsed[0] == "$":
            if command_parsed[1] == "cd":
                if command_parsed[2] == "..":
                    cur_dir = history.pop()
                    continue
                
                history.append(cur_dir)
                cur_dir = cur_dir.directories[command_parsed[2]]
            elif command_parsed[1] == "ls":
                continue
        # Dealing with output
        else:
            if command_parsed[0] == "dir":
                cur_dir.add_directory(command_parsed[1])
            else:
                cur_dir.add_file(command_parsed[0])
    
    # Summing
    root_sum = root.get_sum()
    list_of_sizes = [root_sum]
    for dir in root.directories:
        get_list_of_sizes(list_of_sizes, root.directories[dir])

    sum = 0
    for size in list_of_sizes:
        if size <= 100000:
            sum += size

    print(f"ANSWER PART 1::: {sum}")

    total_disk_space = 70000000
    required = 30000000
    unused_space = total_disk_space - root_sum

    smol = root_sum

    for size in list_of_sizes:
        if size + unused_space >= required:
            smol = min(size, smol)

    print(f"part 2::{smol}")

def get_list_of_sizes(sizes, dir):
    sizes.append(dir.get_sum())

    if len(dir.directories) == 0:
        return sizes
    else:
        for directory in dir.directories:
            get_list_of_sizes(sizes, dir.directories[directory])
        
        return sizes


def parse_input(filename):
    file = open(f"{os.getcwd()}/07/{filename}", "r")
    arr = []

    for line in file:
        arr.append(line.strip())

    file.close()
    return arr

if __name__ == '__main__':
    main()
