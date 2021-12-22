with open("/Users/paigejones/Desktop/funcode/advent/day2/input_day2.txt") as input: 
    map = input.read().splitlines()


def get_directions(map):
    h_position = 0
    depth = 0

    for direction in map: 
        if "forward" in direction:
            h_position += int(direction[-1])
        elif "up" in direction:
            depth -= int(direction[-1])
        elif "down" in direction:
            depth += int(direction[-1])
    return (depth * h_position)

print(get_directions(map))