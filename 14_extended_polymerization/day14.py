# Day 14 Extended Polymerization

INPUT_FILE = 'puzzle_input.txt'
NUM_STEPS = 10

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

def main():
    template, insertion_rules = parse_input(INPUT_FILE)
    p1_answer = part_one_solution(template, insertion_rules, NUM_STEPS)
    print('Most common element subtracted by least common element is: ', str(p1_answer))

if __name__ == '__main__':
    main()
