

# Iterate through each line
# Discard "corrupted" lines  -- where a chunk closes with the wrong character

# Find corrupted lines first
# 

PUZZLE_INPUT = 'test_input.txt'

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def print_items(self):
        print('self.items: ', self.items)

chunk_list = []
with open(PUZZLE_INPUT) as file:
    for line in file:
        stripped_line = line.strip()
        # print('line: ', stripped_line)
        chunk_list.append(stripped_line)

def filter_corrupted_lines(line):
    """
    
    """
    char_dict = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }
    uncorrupted_lines = []
    for char in line:
        # print('current char: ', char)
        if char in char_dict: # If it's one of the keys (opening brackets), add it to the stack
            if line[-1] == char_dict[char]:
                uncorrupted_lines.append(line)

    return uncorrupted_lines



def has_illegal_char(line):
    """
    Takes in puzzle input, finds "good" lines that are not corrupted, finds first illegal character in each line, 
    sums illegal letter scores as total syntax error score and returns as an int.
    ## This is for the solution function

    ## For this function:
    Determines if the line is corrupted - a corrupted line is when a chunk closes with the wrong character
    
    Returns '' if there is an illegal character, otherwise returns None

    """

    stack = Stack()
    # opening_chars = "[({<"
    # closing_chars = "])}>"

    # opening char is key, closing char is value
    char_dict = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }
    # stack.print_items()

    # corrupted_lines = []
    # remaining_lines = []

    # good_lines = filter_corrupted_lines(line)

    for char in line:
        # print('current char: ', char)
        if char in char_dict: # If it's one of the keys (opening brackets), add it to the stack
            stack.push(char)
            # print('after adding char... ')
            # stack.print_items()
        else: # If it's a closing char:
            # print("closing char detected.. ")
            if stack.size() > 0 and char == char_dict[stack.peek()]: # If the stack has items and most recent char in the stack matches the top of the stack
                # print('Matching char and char_dict[stack.peek()]!')
                # print('char: ', char)
                # print('removing char.. char_dict[stack.peek()]: ', char_dict[stack.peek()]) # ]
                stack.pop() # Remove the starting bracket -- match found, so the pair is "compeleted"

            else: # The character is a closing character AND does not match the most recent character in the stack, illegal char found.
                # print('first illegal character: ', char)
                return char
                # stack.push(char)

    # Stop at the first incorrect character

    # We only want to add a charcter that is opening bracket
    # We only want to delete a character that matches the most recently added stack item

    # print('Following all processing... ')
    stack.print_items()

    if stack.size() > 0:
        # print('stack size is greater than 0, corrupted line')
        # return line
        return None # Placeholder for part1
    # else:
    #     return None

def calculate_error_score(corrupted_values):
    """
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
    """
    sum_values = 0

    symbol_point_mapping_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    for value in corrupted_values:
        if value in symbol_point_mapping_dict:
            print('value: ', value)
            sum_values += symbol_point_mapping_dict[value]

    return sum_values

# Find corrupteds
# Find first illegal char
# 
def calc_syntax_score():

    corrupted_values = ''
    with open(PUZZLE_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            print('line: ', stripped_line)

            # For each line, we'll check to see if it has an illegal character -- 
            # Doesn't just check if it has the char, but returns if so, and returns false if not (will not be caught by loop)
            if has_illegal_char(line): # Checks if there is an illegal character
                print('has_illegal_char(line) has value.. ', has_illegal_char(line))
                corrupted_values += has_illegal_char(line)

    return calculate_error_score(corrupted_values.strip())


print(calc_syntax_score())

# print(calc_solution(PUZZLE_INPUT))