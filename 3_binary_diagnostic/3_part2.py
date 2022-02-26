# Binary Diagnostic part 2

full_bin_list = []

with open('puzzle_input.txt') as file:
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
        Takes in a list of binary numbers as strings of the same length, performs processing based on
        most common bit criteria and outputs a decimal number representation of the last standing number
        as an int.
    """
    
    list_length = len(lst[0])
    updated_list = lst
    oxy_rating_bin = None

    for i in range(list_length):
        lst_zeroes = []
        lst_ones = []

        for binary_num in updated_list:
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

        if len(updated_list) == 1:
            oxy_rating_bin = updated_list[0]

    oxy_decimal = convert_bin_to_decimal(oxy_rating_bin)
    return oxy_decimal


def find_co2_rate(lst):
    """
        Takes in a list of binary numbers as strings of the same length, performs processing based on
        most common bit criteria and outputs a decimal number representation of the last standing number
        as an int.
    """
    
    list_length = len(lst[0])
    updated_list = lst
    co2_rating_bin = None

    for i in range(list_length):
        lst_zeroes = []
        lst_ones = []

        for binary_num in updated_list:
            if binary_num[i] == "0":
                lst_zeroes.append(binary_num)
            else:
                lst_ones.append(binary_num)

        if len(lst_zeroes) == len(lst_ones):
            updated_list = lst_zeroes # Keep list with zero for co2 rating
        else:
            if len(lst_zeroes) > len(lst_ones):
                updated_list = lst_ones
            else:
                updated_list = lst_zeroes

        if len(updated_list) == 1:
            co2_rating_bin = updated_list[0]

    co2_decimal = convert_bin_to_decimal(co2_rating_bin)
    return co2_decimal

oxy_rate = find_oxy_rate(full_bin_list)
co2_rate = find_co2_rate(full_bin_list)

life_support_rating = oxy_rate * co2_rate
print('life support rating: ', life_support_rating)
