# Seven segment search part 2
from enum import Enum, auto

TEST_INPUT = 'puzzle_input.txt'

def calc_multi_set_intersection(set_list):
    return set.intersection(*set_list)

def calc_multi_set_difference(set_list):
    return set.difference(*set_list)

class SegmentEnum(Enum):
    TOP = auto()
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    MIDDLE = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_RIGHT = auto()
    BOTTOM = auto()

DIGIT_SEGMENT_DICT = {
    0: {SegmentEnum.TOP, SegmentEnum.TOP_LEFT, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM, SegmentEnum.BOTTOM_LEFT, SegmentEnum.TOP_RIGHT},
    1: {SegmentEnum.TOP_RIGHT, SegmentEnum.BOTTOM_RIGHT},
    2: {SegmentEnum.TOP, SegmentEnum.TOP_RIGHT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_LEFT, SegmentEnum.BOTTOM},
    3: {SegmentEnum.TOP, SegmentEnum.TOP_RIGHT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM},
    4: {SegmentEnum.TOP_RIGHT, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.MIDDLE, SegmentEnum.TOP_LEFT},
    5: {SegmentEnum.TOP, SegmentEnum.TOP_LEFT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM},
    6: {SegmentEnum.TOP, SegmentEnum.TOP_LEFT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM, SegmentEnum.BOTTOM_LEFT},
    7: {SegmentEnum.TOP_RIGHT, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.TOP},
    8: {SegmentEnum.TOP, SegmentEnum.TOP_LEFT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM, SegmentEnum.BOTTOM_LEFT, SegmentEnum.TOP_RIGHT},
    9: {SegmentEnum.TOP, SegmentEnum.TOP_LEFT, SegmentEnum.MIDDLE, SegmentEnum.BOTTOM_RIGHT, SegmentEnum.BOTTOM, SegmentEnum.TOP_RIGHT}
}

def calculate_output_sum(char_set_list, segment_dict):
    sum = ''
    inverted_segment_dict = {}

    for key in segment_dict:
        value = segment_dict[key]
        inverted_segment_dict[value] = key

    for char_set in char_set_list:
        digit_segment_set = set()
        for character in char_set:
            digit_segment_set.add(inverted_segment_dict[character])
        
        for digit in DIGIT_SEGMENT_DICT:
            if DIGIT_SEGMENT_DICT[digit] == digit_segment_set:
                sum += str(digit)

    return int(sum)

def sum_difference(a, b):
    return a + b, a - b

def parse_input_line(line):
    """
        Returns pair of input_list, output_list
        input_list: a list of set of characters sorted by length
        output_list:  a list of set of characters
    """
    unstripped_input_values, unstripped_output_values = line.split('|')
    input_values = unstripped_input_values.strip()
    output_values = unstripped_output_values.strip()

    sorted_inputs = sorted(input_values.split(' '), key=len)
    outputs = output_values.split(' ')

    input_list = [set(input) for input in sorted_inputs]
    output_list = [set(output) for output in outputs]
    return input_list, output_list

def map_unique_length_digits(input_list, mapping_dict):
    mapping_dict[1] = input_list[0] # --> 1
    mapping_dict[7] = input_list[1]  # --> 7
    mapping_dict[4] = input_list[2] # --> 4
    mapping_dict[8] = input_list[-1] # --> 8

def run(test_input):
    with open(test_input) as file:
        total_sum = 0
        for line in file:
            input_list, output_list = parse_input_line(line)

            mapping_dict = {} # Maps key (number) to value (character config)
            segment_dict = {}
            # 1, 4, 7, 8 where 8 is unused

            # Assign digits with unique number of segments as keys and the corresponding set from the input_list as the value to mapping_dict
            map_unique_length_digits(mapping_dict, input_list)
            
            top_segment = mapping_dict[7] - mapping_dict[1]
            segment_dict[SegmentEnum.TOP] = top_segment.pop()

            five_digit_list = [input_list[3], input_list[4], input_list[5]]
            # Three possible combinations
            first_pair_length = len(five_digit_list[0] & five_digit_list[1])
            second_pair_length = len(five_digit_list[0] & five_digit_list[2])
            third_pair_length = len(five_digit_list[1] & five_digit_list[2])

            # Only one of these will have intersection of length 3
            if first_pair_length == 3:
                mapping_dict[3] = five_digit_list[2]
                if len(five_digit_list[0] & mapping_dict[4]) == 2: # One of the two sets being compared -- compare against and if length is 2, it's 2
                    mapping_dict[2] = five_digit_list[0]
                    mapping_dict[5] = five_digit_list[1]
                else:
                    mapping_dict[2] = five_digit_list[1]
                    mapping_dict[5] = five_digit_list[0]
                    
            if second_pair_length == 3:
                mapping_dict[3] = five_digit_list[1]
                if len(five_digit_list[0] & mapping_dict[4]) == 2:
                    mapping_dict[2] = five_digit_list[0]
                    mapping_dict[5] = five_digit_list[2]
                else:
                    mapping_dict[2] = five_digit_list[2]
                    mapping_dict[5] = five_digit_list[0]

            if third_pair_length == 3:
                mapping_dict[3] = five_digit_list[0]
                if len(five_digit_list[1] & mapping_dict[4]) == 2:
                    mapping_dict[2] = five_digit_list[1]
                    mapping_dict[5] = five_digit_list[2]
                else:
                    mapping_dict[2] = five_digit_list[2]
                    mapping_dict[5] = five_digit_list[1]

            top_right_segment = calc_multi_set_intersection([mapping_dict[2], mapping_dict[1]])
            segment_dict[SegmentEnum.TOP_RIGHT] = top_right_segment.pop()
            
            bottom_right_segment = calc_multi_set_intersection([mapping_dict[5], mapping_dict[1]])
            segment_dict[SegmentEnum.BOTTOM_RIGHT] = bottom_right_segment.pop()

            middle_segment = calc_multi_set_intersection([mapping_dict[5], mapping_dict[4], mapping_dict[2]])
            segment_dict[SegmentEnum.MIDDLE] = middle_segment.pop()

            bottom_segment = calc_multi_set_difference([mapping_dict[5], mapping_dict[4], segment_dict[SegmentEnum.TOP]])
            segment_dict[SegmentEnum.BOTTOM] = bottom_segment.pop()

            top_left_segment = calc_multi_set_difference([mapping_dict[4], mapping_dict[3]])
            segment_dict[SegmentEnum.TOP_LEFT] = top_left_segment.pop()

            bottom_left_segment = calc_multi_set_difference([mapping_dict[8], segment_dict[SegmentEnum.TOP], segment_dict[SegmentEnum.TOP_RIGHT], segment_dict[SegmentEnum.BOTTOM_RIGHT], segment_dict[SegmentEnum.MIDDLE], segment_dict[SegmentEnum.BOTTOM], segment_dict[SegmentEnum.TOP_LEFT]])
            segment_dict[SegmentEnum.BOTTOM_LEFT] = bottom_left_segment.pop()

            total_sum += calculate_output_sum(output_list, segment_dict)

    return total_sum

print(run(TEST_INPUT))
#1070957
