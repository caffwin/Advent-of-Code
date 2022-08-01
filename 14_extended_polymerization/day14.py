# Day 14 Extended Polymerization
import math

INPUT_FILE = 'puzzle_input.txt'
NUM_STEPS = 40

def parse_input(file_name):

    with open(file_name) as file:
        template_flag = False
        template = None
        insertion_rules = {}

        for line in file:
            stripped_line = line.strip()

            if template_flag == False:
                template = stripped_line
                template_flag = True
            else:
                if line != '\n':
                    result = stripped_line.split('->')
                    pair = result[0].strip()
                    result = result[1].strip()
                    insertion_rules[pair] = result

    return template, insertion_rules

def calc_most_and_least_common_elements(polymer):
    str_dict = {}
    # Populate str_dict to calculate number of occurrences
    for char in polymer:
        if char not in str_dict:
            str_dict[char] = 1
        else:
            str_dict[char] += 1
    most_frequent_element = max(str_dict.values())
    least_frequent_element = min(str_dict.values())

    p1_answer = most_frequent_element - least_frequent_element
    return p1_answer

def perform_pair_insertion(template, insertion_rules):
    iterations = len(template) - 1
    new_str = ''
    first_sequence = True

    for i in range(iterations):
        modified_polymer = ''
        element_pair = str(template[i] + template[i + 1])

        if first_sequence == True:
            modified_polymer = template[i] + insertion_rules[element_pair] + template[i + 1]
            first_sequence = False
        else: # Not first sequence - only add last two characters
            modified_polymer = insertion_rules[element_pair] + template[i + 1]        
        new_str += modified_polymer
    return new_str


def part_one_solution(template, insertion_rules, steps):
    new_polymer_placeholder = None

    for i in range(steps):
        if new_polymer_placeholder == None:
            new_polymer = perform_pair_insertion(template, insertion_rules)
            new_polymer_placeholder = new_polymer
        else:
            new_polymer = perform_pair_insertion(new_polymer_placeholder, insertion_rules)
            new_polymer_placeholder = new_polymer

    p1_answer = calc_most_and_least_common_elements(new_polymer)
    return p1_answer


########################## P2 ############################

def calc_most_and_least_common_elements_p2(polymer_dict):
    most_frequent_element = max(polymer_dict.values())
    least_frequent_element = min(polymer_dict.values())
    p2_answer = most_frequent_element - least_frequent_element
    return p2_answer

def create_polymer_dict(insertion_rules):
    pair_dict = {}
    for key in insertion_rules.keys():
        pair_dict[key] = 0
    return pair_dict

def populate_polymer_dict(polymer, polymer_dict):
    total_pairs = len(polymer) - 1
    for i in range(total_pairs):
        element_pair = str(polymer[i] + polymer[i + 1])
        polymer_dict[element_pair] += 1
    return polymer_dict

def calc_polymer_state(polymer_state_dict, insertion_rules):
    # Takes in a polymer and returns a polymer dict containing the pairs of elements that will be
    # go through pair insertion process via set of rules defined through polymer_dict
    
    blank_dict = create_polymer_dict(insertion_rules)
    new_state_dict = blank_dict # blank dict is passed in, maybe not optimal

    # Process pairs and return the next state dict with new pairs
    for pair, count in polymer_state_dict.items():
        first_pair = str(pair[0]) + str(insertion_rules[pair])
        second_pair = str(insertion_rules[pair]) + str(pair[1])
        new_state_dict[first_pair] += count
        new_state_dict[second_pair] += count

    return new_state_dict

def create_occurence_dict(polymer_dict):
    """
        Takes in a polymer_dict containing element pairs (str, key) and number of occurrences (int, value)
        Returns a dict representing the number of occurrences (int) of each unique letter (str, single character).
    """
    template_dict = {}

    for key, count in polymer_dict.items():
        if count > 0:
            for char in key:
                if char not in template_dict:
                    template_dict[char] = 0.5 * count
                else:
                    template_dict[char] += 0.5 * count

    # Rounding, after values are all populated
    for key in template_dict:
        rounded_value = math.ceil(template_dict[key])
        template_dict[key] = rounded_value
    return template_dict

def part_two_solution(template, insertion_rules, steps):
    # Represent the current state, then transition to the next state based on a set of rules
    polymer_dict = create_polymer_dict(insertion_rules)
    initial_state = populate_polymer_dict(template, polymer_dict)
    initial_state_flag = True

    for i in range(steps):
        if initial_state_flag == True:
            current_state = calc_polymer_state(initial_state, insertion_rules)
            initial_state_flag = False
        else:
            new_state = calc_polymer_state(current_state, insertion_rules)
            current_state = new_state

    occurence_dict = create_occurence_dict(current_state)
    p2_answer = calc_most_and_least_common_elements_p2(occurence_dict)
    return p2_answer

def main():
    template, insertion_rules = parse_input(INPUT_FILE)
    # p1_answer = part_one_solution(template, insertion_rules, NUM_STEPS)
    # print('Most common element subtracted by least common element is: ', str(p1_answer))

    p2_answer = part_two_solution(template, insertion_rules, NUM_STEPS)
    print("p2_answer: ", p2_answer)

if __name__ == '__main__':
    main()
