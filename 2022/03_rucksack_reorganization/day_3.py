TEST_INPUT_FILE = 'test_input.txt'

def part_one_solution():
    priority_sum = 0
    with open(TEST_INPUT_FILE) as file:
        
        for line in file:
            shared_char = None
            stripped_line = line.strip()
            compartment_one = set(stripped_line[0:int(len(stripped_line)/2)])
            compartment_two = set(stripped_line[int(len(stripped_line)/2):])

            shared_char = ''.join(compartment_one.intersection(compartment_two))
            unicode_char = ord(shared_char)

            if shared_char.islower():
                priority_index = ord(shared_char) - 96
            else: # upper case
                priority_index = ord(shared_char) - 38

            priority_sum += priority_index

    return priority_sum


def run():
    print('part one solution: ', part_one_solution())

if __name__ == "__main__":
    run()