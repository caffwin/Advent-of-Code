

# Iterate through each line
# Discard "corrupted" lines  -- where a chunk closes with the wrong character

# Find corrupted lines first
# 

PUZZLE_INPUT = 'puzzle_input.txt'

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

    def return_items(self):
        return self.items

    def print_items(self):
        print(self.items) 


def identify_incomplete_line(line):
    """
    Returns empty string for incomplete line, and character for corrupt line
    """
    stack = Stack()

    # opening char is key, closing char is value
    char_dict = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }

    for char in line:
        stripped_char = char.strip()
        if stripped_char in char_dict: # If it's one of the keys (opening brackets), add it to the stack
            stack.push(stripped_char)
        else: # If it's a closing char:
            if stack.size() > 0 and stripped_char == char_dict[stack.peek()]: # If the stack has items and last char in the stack matches
                stack.pop()
            else:
                # print('first illegal character -- returning on: ', stripped_char)
                # The behaviour: returns on a character if illegal, otherwise returns empty string.
                # The empty strings we identify to be NOT corrupted -- incomplete. If it doesn't return a character, it's incomplete.
                # If it returns a character, it's corrupted.
                return stripped_char

# def calculate_error_score(corrupted_values):
    # ): 1 point.
    # ]: 2 points.
    # }: 3 points.
    # >: 4 points.
#     sum_values = 0

#     symbol_point_mapping_dict = {
#         ')': 1,
#         ']': 2,
#         '}': 3,
#         '>': 4
#     }

#     for value in corrupted_values:
#         if value in symbol_point_mapping_dict:
#             print('value: ', value)
#             sum_values += symbol_point_mapping_dict[value]

#     return sum_values

def find_closing_parens(line):
    """
        Takes in a line as a string and returns a list of missing closing parens as a string
    """
    stack = Stack()

    char_dict = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }

    for char in line:
        # print('char: ', char)
        stripped_char = char.strip()
        if stripped_char in char_dict: # If it's one of the keys (opening brackets), add it to the stack
            stack.push(stripped_char)
        else: # If it's a closing char:
            if stack.size() > 0 and stripped_char == char_dict[stack.peek()]: # Check to see if it's it's a matching paren to the last char in the stack, if yes, delete it:
                stack.pop()

    reversed_list = list(reversed(stack.return_items()))
    closing_parens = ''.join([char_dict[bracket] for bracket in reversed_list])
    # bracket_list = ''.join(list(reversed(stack.return_items())))
    
    return closing_parens # closing_parens_list #closing_parens #   

def find_incomplete_lines():
    incomplete_lines = []
    with open(PUZZLE_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            # print('line: ', stripped_line)

            if identify_incomplete_line(line) == '': # not corrupted = incomplete
                # print('return_if_corrupted(line) has value.. ', return_if_corrupted(line))
                incomplete_lines.append(line.strip())

    return incomplete_lines

def calculate_score(parens):
    """
        ): 1 point.
        ]: 2 points.
        }: 3 points.
        >: 4 points.
    """
    middle_score = 0
    # print('parens: ', parens)
    paren_point_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    # print('parenS: ', parens)
    for paren in parens:
        middle_score = middle_score * 5 + paren_point_dict[paren]

    return middle_score

# Are incomplete lines only missing ending parens? Seems like it
def calc_syntax_score():
    all_scores = []
    incomplete_lines = find_incomplete_lines()
    # print("incomplete lines: ", incomplete_lines)
    for line in incomplete_lines:
        closing_parens = find_closing_parens(line)
        score = calculate_score(closing_parens)
        # print('score: ', score)
        all_scores.append(calculate_score(closing_parens))
        # print('closing parens: ', closing_parens)
    # print('all scores: ', all_scores)

    all_scores.sort()
    # print('sorted_scores; ', all_scores)
    # middle_score =  # Median??
    middle_idx = int(len(all_scores)/2)
    return all_scores[middle_idx]

print(calc_syntax_score())

# 306241117217
# your answer is too high