TEST_INPUT_FILE = 'test_input.txt'

# Debug
ASSIGNMENT_PAIR_LIST = [] # Part 1
NO_OVERLAP_PAIRS_LIST = [] # Part 2

def parse_input():
    fully_contained_pairs = 0
    not_overlapping_pairs = 0
    total_lines = 0
    with open(TEST_INPUT_FILE) as file:
        for line in file:
            total_lines += 1
            stripped_line = line.strip()
            first_pair, second_pair = stripped_line.split(',')
            first_pair_start, first_pair_end = first_pair.split('-')
            second_pair_start, second_pair_end = second_pair.split('-')

            # Part 1 solution
            if (int(first_pair_start) >= int(second_pair_start) and int(first_pair_end) <= int(second_pair_end)) or (int(second_pair_start) >= int(first_pair_start) and int(second_pair_end) <= int(first_pair_end)):
                fully_contained_pairs += 1

            # Part 2 solution
            if (int(second_pair_start) > int(first_pair_end)) or (int(first_pair_start) > int(second_pair_end)):
                not_overlapping_pairs += 1            

    return fully_contained_pairs, not_overlapping_pairs, total_lines

def run():
    p1_solution, p2_excluded_pairs, total_lines = parse_input()
    p2_solution = total_lines - p2_excluded_pairs
    print('part one answer: ', p1_solution)
    print('part two answer: ', p2_solution)
    return

if __name__ == "__main__":
    run()