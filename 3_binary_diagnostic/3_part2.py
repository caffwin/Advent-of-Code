# Binary Diagnostic part 2

full_bin_list = []

# with open('puzzle_input.txt') as file:
with open('test_file.txt') as file:
    lines = file.readlines()    
    for line in lines:
        full_bin_list.append(line.strip())

def convert_bin_to_decimal(binary_str):
    """
        Takes in a binary number as a string and converts to decimal (int) with base 2
    """
    decimal_num = int(binary_str, 2)
    return decimal_num

def find_oxy_rate(lst):
    """
        Takes in a list of binary numbers as strings of the same length and outputs a 
        binary number as the last standing number
    """
    
    output_num = ""
    list_length = len(lst[0])
    print('lst: ', lst)

    updated_list = lst

    for i in range(list_length):
        lst_zeroes = []
        lst_ones = []

        for binary_num in updated_list: # 00100
            if binary_num[i] == "0":
                lst_zeroes.append(binary_num)
            else:
                lst_ones.append(binary_num)

        if len(lst_zeroes) == len(lst_ones):
            updated_list = lst_ones # Keep list with one for oxy rating
        else:
            if len(lst_zeroes) > len(lst_ones):
                updated_list = lst_zeroes
            else:
                updated_list = lst_ones

        print(f'For index (run) {i} the updated list is: ', updated_list)
        print('updated list.... ', updated_list)

    oxy_decimal = updated_list[0]
    return convert_bin_to_decimal(oxy_decimal)


oxy_rate = find_oxy_rate(full_bin_list)
# co2_rate = find_co2_rate(full_bin_list)

print('original function: ', find_oxy_rate(full_bin_list))


# First run through, keep:
# 11110, 10110, 10111, 10101, 11100, 10000, and 11001.

# Second run through, keep numbers with 0 in 2nd:
# 10110, 10111, 10101, and 10000
