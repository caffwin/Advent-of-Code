# Day 14 Extended Polymerization

from concurrent.futures import process


INPUT_FILE = 'test_input.txt'
NUM_STEPS = 3

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


######################################################
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
    # Create initial state
    total_pairs = len(polymer) - 1
    for i in range(total_pairs):
        element_pair = str(polymer[i] + polymer[i + 1])
        polymer_dict[element_pair] += 1
    return polymer_dict

def calc_polymer_state(polymer_state_dict, insertion_rules):
    print("current state dict passed in - should be same as above: ", polymer_state_dict)
    # {'CH': 1, 'HH': 0, 'CB': 0, 'NH': 0, 'HB': 1, 'HC': 0, 'HN': 0, 'NN': 0, 'BH': 0, 'NC': 1, 'NB': 1, 'BN': 0, 'BB': 0, 'BC': 1, 'CC': 0, 'CN': 1}
    # The dict populated as expected
    
    # Isolate keys where the value is greater than 0 into another dict (probably not optimal for storage?):
    process_pair_values = dict((element_pair, occurrences) for element_pair, occurrences in polymer_state_dict.items() if occurrences > 0)
    # {'CH': 1, 'HB': 1, 'NC': 1, 'NB': 1, 'BC': 1, 'CN': 1} --> these are the correct pairs to process, only keys with values over 0 are included
    print('process_pair_values: ', process_pair_values)

    blank_dict = create_polymer_dict(insertion_rules)
    # polymer_dict is a fresh new dict:
    print('blank dict: ', blank_dict)

    new_state_dict = blank_dict # blank dict is passed in

    new_pair_lst = [] # for debug
    # Figure out a way to process pairs, and then return updated dict with new pairs
    for pair in process_pair_values:
        # print('Number of times we need to add new pairs: ', process_pair_values[pair])
        # print('pair that is being checked: ', pair)
        for i in range(process_pair_values[pair]): # For each pair, need to add additional pairs this number of times
        # Each pair maps to 2 additional pairs after insertion rule is executed
            print('checking pair: ', pair)
            first_pair = str(pair[0]) + str(insertion_rules[pair])
            second_pair = str(insertion_rules[pair]) + str(pair[1])
            print('first pair: ', first_pair, 'second pair: ', second_pair)
            new_state_dict[first_pair] += 1
            new_state_dict[second_pair] += 1
            new_pair_lst.append(first_pair)
            new_pair_lst.append(second_pair)
            # print('adding pairs: ', first_pair, second_pair)

    print('total new pairs to be added to new state: ', len(new_pair_lst))
    # print('polymer state dict -- this will be passed to the next state: ', new_state_dict)
    debug_dict = {}
    # print("****Next set of pairs to check: ", new_pair_lst)
    for pair in new_pair_lst:
        if pair not in debug_dict:
            debug_dict[pair] = 1
        else:
            debug_dict[pair] += 1
    print("debug_dict: ", debug_dict)
    print('new state: ', new_state_dict)
    return new_state_dict

def part_two_solution(template, insertion_rules, steps):
    polymer_dict = create_polymer_dict(insertion_rules)
    
    # populate for initial state:
    initial_state = populate_polymer_dict(template, polymer_dict) # Modifies polymer_dict, also need a blank one
    initial_state_flag = True
    # print('polymer dict from first function after initial state, should still be blank: ', polymer_dict)

    # Takes in a state, and returns the new state based on the current state
    for i in range(steps):
        print("Current step: ", str(i+1))
        if initial_state_flag == True:
            current_state = calc_polymer_state(initial_state, insertion_rules)
            initial_state_flag = False
        else:
            print('current state passed in before new state is calculated: ', current_state)
            new_state = calc_polymer_state(current_state, insertion_rules)
            current_state = new_state
    
    # Convert final state pairs into elements/number of occurrences dict using insertion_rules:
    occurence_dict = {}
    for key in current_state:
        if current_state[key] > 0:
            if insertion_rules[key] not in occurence_dict:
                occurence_dict[insertion_rules[key]] = current_state[key] 
            else:
                occurence_dict[insertion_rules[key]] += current_state[key] # int value of number of times pair occurs: ex, 16 ---> 

    p2_solution = calc_most_and_least_common_elements_p2(occurence_dict)
    return p2_solution

def main():
    template, insertion_rules = parse_input(INPUT_FILE)
    # p1_answer = part_one_solution(template, insertion_rules, NUM_STEPS)
    # print('Most common element subtracted by least common element is: ', str(p1_answer))
    p2_answer = part_two_solution(template, insertion_rules, NUM_STEPS)
    print("p2_answer: ", p2_answer)
if __name__ == '__main__':
    main()
