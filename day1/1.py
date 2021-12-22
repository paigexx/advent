with open("./input.txt") as input:
    lines = input.read().splitlines()

# get count
count = 0
for i, line in enumerate(lines): 
    if i > 0 and int(lines[i]) > int(lines[i-1]):
        count += 1