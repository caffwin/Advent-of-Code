# Use the given report to generate a "gamma rate" and "epsilon rate" - each a binary number
# The power consumption can be calculated by multiplying these two numbers

# Each digit in a binary number is a bit. The number 1010110 is represented by 7 bits.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position 
#  of all numbers in the diagnostic report. For example, given the following diagnostic report (test_file)

# Test file - 12 rows

gamma_rate_lst = []

# Generates diagnostic report from input file into list
# with open('puzzle_input.txt') as file: # For answer submission 
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
    # Iterate through each element in list
    binary_length = len(lst[0])

    for i in range(binary_length):
        most_common = 0
        num_zeroes = 0
        num_ones = 0
        for binary_num in lst:
            if binary_num[i] == "0":
                num_zeroes += 1
            else:
                num_ones += 1

        # print("num_zeroes: ", num_zeroes)
        # print("num_ones: ", num_ones)

        # if num_zeroes > num_ones:
        #     output_num += "0"
        # else:
        #     output_num += "1"

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

# print('gamma_rate_lst: ', str(len(gamma_rate_lst)))
# print("Gamma rate: ", change_rate_to_decimal(find_gamma_rate(gamma_rate_lst)))

gamma_rate = find_gamma_rate(gamma_rate_lst) # a string

epsilon_rate = find_epsilon_rate(gamma_rate) 
print('epsilon_rate: ', epsilon_rate)

print('gamma_rate decimal: ', change_rate_to_decimal(gamma_rate))
print('epsilon_rate decimal: ', change_rate_to_decimal(epsilon_rate))
power_consumption = change_rate_to_decimal(epsilon_rate) * change_rate_to_decimal(gamma_rate)

print('power consumption: ', str(power_consumption))
