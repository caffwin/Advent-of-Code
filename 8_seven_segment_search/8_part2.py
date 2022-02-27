# Seven segment search part 2

# Seven Segment Search

import numbers

all_outputs = []

# with open('puzzle_input.txt') as file:
with open('test_input.txt') as file:
    for line in file:
        # print('line: ', line)
        unstripped_input_values, unstripped_output_values = line.split('|')

        input_values = unstripped_input_values.strip()
        output_values = unstripped_output_values.strip()

        input_lst = input_values.split(' ')
        output_lst = output_values.split(' ')

        # all_outputs.extend(output_lst)
        all_outputs.append(output_lst)

# print('all_outputs: ', all_outputs)

# New config
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

digit_mapping_dict = {
    "0": "cagedb",
    "1": "ab", # ** 2
    "2": "gcdfa",
    "3": "fbcad", # cefdb
    "4": "eafb", # ** 4
    "5": "cdfbe",
    "6": "cdfgeb",
    "7": "dab", # ** 3
    "8": "acedgfb", # ** 7
    "9": "cefabd"
}

def check_anagram(string_1, string_2):
    if(sorted(string_1)== sorted(string_2)):
        return True
    else:
        return False
         

def count_unique_displays(outputs):
    """
        Updated display configuration
    """
    unique_nums = '1478'
    segment_list_lengths = []
    total_unique = 0

    # Number of chars -- ex. 5, 2, and 3 all have 5 chars
    # Clump to digit mappings
    char_length_dict = {
        '5': '523',
        '6': '690',
        '2': '1',
        '4': '4',
        '7': '8',
        '3': '7'
    }

    total_sum = 0
    output_nums = []

    for output_list in outputs:
        char_total = ''
        for char_clump in output_list:
            # Should be: 8394
            # Getting: 8564            
            # Why does "cefdb" resolve to 3, and not 5?
            length_clump_str = str(len(char_clump)) # fdgacbe --> '7'
            numbers_matching_clump_length = char_length_dict[length_clump_str] # could be 523, 1, 690, 4 --> values of dict depending on length of clump
            if len(numbers_matching_clump_length) == 1: # This means there's only 1 value that exists
                print("numbers_matching_clump_length -- adding this to char total: ", str(numbers_matching_clump_length))
                char_total += numbers_matching_clump_length # Find the only number that matches

            else: # There are numerous characters that have this same clump length
                potential_nums = char_length_dict[length_clump_str]
                print(f"there is more than one letter that shares the same length of characters as this. Potential nums: {potential_nums}")
                for num in potential_nums:
                    print('checking num: ', num)
                    if check_anagram(char_clump, digit_mapping_dict[num]):
                        print(f'{char_clump} is an anagram of {digit_mapping_dict[num]}!')
                        char_total += num # should be str but check
                        
        print('char_total: ', char_total)
        output_nums.append(char_total)

    for num in output_nums:
        total_sum += int(num)
        
    return "Clumps"

print("Number of unique segments in output:", count_unique_displays(all_outputs))
