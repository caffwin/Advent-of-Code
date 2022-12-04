TEST_INPUT_FILE = 'test_input.txt'
ASSIGNMENT_PAIR_LIST = []

def run():
    overlapping_pairs = 0
    with open(TEST_INPUT_FILE) as file:
        for line in file:
            stripped_line = line.strip()
            first_pair, second_pair = stripped_line.split(',')

            first_pair_tuple = tuple(first_pair.split('-'))
            first_pair_start, first_pair_end = first_pair.split('-')
            second_pair_tuple = tuple(second_pair.split('-'))
            second_pair_start, second_pair_end = second_pair.split('-')

            if (first_pair_start >= second_pair_start and first_pair_end <= second_pair_end) or (second_pair_start >= first_pair_start and second_pair_end <= first_pair_end):
                overlapping_pairs += 1
                lst = [first_pair_tuple, second_pair_tuple]
                ASSIGNMENT_PAIR_LIST.append(lst)

    print('ASSIGNMENT PAIR LIST: ', ASSIGNMENT_PAIR_LIST) # for debugging purposes
    print(overlapping_pairs)
    return overlapping_pairs

if __name__ == "__main__":
    run()