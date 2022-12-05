TEST_INPUT_FILE = 'test_input.txt'

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def return_items(self):
        return self.items

    def print_items(self):
        print(self.items) 

    def reverse_item_order(self):
        return self.items.reverse()

# Determine number of crates:
TOTAL_CHARS_IN_CRATE = 3
test_file = open(TEST_INPUT_FILE)
content = test_file.readlines() # hashtag content
TOTAL_CRATES = round(len(content[0])/(TOTAL_CHARS_IN_CRATE + 1)) # accounts for length of crate (3 chars) and space

# Extract crate data and instructions from input
def parse_input(TEST_INPUT_FILE):
    crate_matrix = [] # a list of list of stacks
    new_line_flag = False
    instructions = []
    with open(TEST_INPUT_FILE) as file:
        for line in file:
            # print('line: ', line)
            if line == '\n':
                new_line_flag = True
            
            # Parse crate contents until new line is reached
            if new_line_flag == False:
                crate_contents = list(line[1::4]) # crate contents, every 4th character starting from index 1
                crate_matrix.append(crate_contents)
            
            else:
                if line == '\n':
                    print('new line detected, proceeding with parsing instructions')
                # Parse instructions
                else:
                    stripped_line = line.strip()
                    junk, num_crates, junk2, origin, junk3, destination = stripped_line.split(' ')
                    instruction_list = [int(num_crates), int(origin), int(destination)]
                    instructions.append(instruction_list)

    return crate_matrix[:-1], instructions

def create_stacks_from_crate_matrix(crate_matrix):
    stacks = []
    for i in range(len(crate_matrix) + 1):
        stacks.append(Stack())
        
    for crate_list in crate_matrix:
        for i, item in enumerate(crate_list):
            if item != ' ':
                stacks[i].push(item) # list index out of range
    for stack in stacks:
        stack.reverse_item_order()

    return stacks

def perform_stack_calculations(stacks, instructions):
    """
        Takes in a list of stacks and performs calculations based on list of instructions.
        Each instruction is a list of three ints:
        1) number of crates to move 
        2) origin stack
        3) destination stack

        Returns new stacks after all instructions have been carried out and crates moved
    """

    for instruction in instructions:
        num_crates_to_move = instruction[0]
        origin_stack_index = instruction[1] - 1
        destination_stack_index = instruction[2] - 1
        
        temp_stack = Stack()
        for i in range(num_crates_to_move):
            temp_stack.push(stacks[origin_stack_index].pop())

        for i in range(num_crates_to_move):
            stacks[destination_stack_index].push(temp_stack.pop())

    return stacks

def find_top_crates(stacks):
    lst_top_crates = []
    for stack in stacks:
        lst_top_crates.append(stack.pop())

    return lst_top_crates


def pp_matrix(matrix):
    for row in matrix:
        prettier_row = ' '.join(map(str, row))
        print(prettier_row)


def run():
    crate_matrix, instructions = parse_input(TEST_INPUT_FILE) # return crate matrix
    stacks = create_stacks_from_crate_matrix(crate_matrix)
    modified_stacks = perform_stack_calculations(stacks, instructions)
    top_crates = find_top_crates(modified_stacks)
    print('part two solution: :', ''.join(top_crates))
    return

if __name__ == "__main__":
    run()