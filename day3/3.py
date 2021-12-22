with open("day3/input_day3.txt") as input: 
    lines = input.read().splitlines()

def con_rate(lines):
    length = len(lines[0])
    gg_rate = [0] * length
    ones = [0] * length
    zeros = [0] * length
   
    for line in lines:
        for i, char in enumerate(line):
            if char == "0":
                zeros[i] += 1
            else:
                ones[i] += 1
    
    for rate in range(len(zeros)):
        if zeros[rate] > ones[rate]:
            gg_rate[rate] = 0
        else:
            gg_rate[rate] = 1
    print (gg_rate)

    def array_to_string(array):
        return "".join(map(str, array))

    def to_decimal(binary_str):
        return int(binary_str, 2)

    def binary_array_inversion(binary_array):
        return [1 if i == 0 else 0 for i in binary_array]

    e_rate = (binary_array_inversion(gg_rate))  
    print(e_rate)
    g_rate_str = array_to_string(gg_rate)
    e_rate_str = array_to_string(e_rate)

    return to_decimal(g_rate_str) * to_decimal(e_rate_str)





con_rate(lines)





