# 3 Binary Diagnostic

gamma_rate_lst = []

with open('puzzle_input.txt') as file:
    lines = file.readlines()    
    for line in lines:
        gamma_rate_lst.append(line.strip())


def find_gamma_rate(lst):
    """
    Takes in a list of binary numbers as strings of the same length and outputs a 
    binary number as a string containing the most common bit in each column
    """
    
    output_num = ""
    binary_length = len(lst[0])

    for i in range(binary_length):
        num_zeroes = 0
        num_ones = 0
        for binary_num in lst:
            if binary_num[i] == "0":
                num_zeroes += 1
            else:
                num_ones += 1

        output_num += "0" if num_zeroes > num_ones else "1"

    return output_num

# 
def find_epsilon_rate(gamma_rate):
    print('gamma rate input from find_epsilon_rate: ', gamma_rate)
    epsilon_rate = ""
    for bit in gamma_rate:
        epsilon_rate += "0" if bit == "1" else "1"

    return epsilon_rate

def change_rate_to_decimal(rate):
    return int(rate, 2)

gamma_rate = find_gamma_rate(gamma_rate_lst)

epsilon_rate = find_epsilon_rate(gamma_rate) 
print('epsilon_rate: ', epsilon_rate)

print('gamma_rate decimal: ', change_rate_to_decimal(gamma_rate))
print('epsilon_rate decimal: ', change_rate_to_decimal(epsilon_rate))
power_consumption = change_rate_to_decimal(epsilon_rate) * change_rate_to_decimal(gamma_rate)

print('power consumption: ', str(power_consumption))
