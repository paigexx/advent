with open("./input.txt") as input:
    lines = input.read().splitlines()


# get sum 
sum_count = 0
length = len(lines)
for i, line in enumerate(lines):
    if i < length-3:
        d1 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        d2 = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
        if d2 > d1: 
            sum_count += 1
print(sum_count)