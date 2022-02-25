# Seven Segment Search

all_outputs = []
with open('test_input.txt') as file:
    for line in file:
        print('line: ', line)
        unstripped_input_values, unstripped_output_values = line.split('|')

        input_values = unstripped_input_values.strip()
        output_values = unstripped_output_values.strip()

        input_lst = input_values.split(' ')
        output_lst = output_values.split(' ')

        all_outputs.extend(output_lst)

digit_display_mappings = {
    "0": "abcefg",
    "1": "cf", # ** 2
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf", # ** 4
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf", # ** 3
    "8": "abcdefg", # ** 7
    "9": "abcdfg"
}

def count_unique_displays(output_list):
    """ Given an ouput list of segments corresponding to displayed numbers, calculate how many times
    a digit with a unique number of segments """
    print('output list in function: ', output_list)
    target_nums = ['1', '4', '7', '8']
    # segment_list = [] # Unused
    segment_list_lengths = []
    total_unique = 0

    # Populate list of combinations for unique segments (to calculate for part 1)
    for num in target_nums:
        # segment_list.append(digit_display_mappings[num])
        segment_list_lengths.append(len(digit_display_mappings[num]))

    for item in output_list:
        if len(item) in segment_list_lengths:
            total_unique += 1

    return total_unique

print("Number of unique segments in output:", count_unique_displays(all_outputs))
