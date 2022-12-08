TEST_FILE_INPUT = "test_input.txt"
INSTRUCTION_LIST = []
NODE_LIST = set() # Keep track of all nodes

class Node():
    def __repr__(self, file_type, children=None) -> str:
        self.file_type = None
        self.children = None # By default, no children unless directory -- then pass in list of additional nodes? Maybe.
        pass

    def add_children(self, children):
        self.children.append()

    def show_children(self):
        return self.children


def execute_instruction(current_node, instruction):

    if len(instruction) == 2: # this is an ls -- this helps BUILD the tree
        print('listing out instructions')

    # Else, it's a cd command -- meaning we traverse in some way
    else:
        cd_cmd, move_to = instruction.split(" ")
        print('moving to file... ', move_to)
        if move_to == "..": # go up one level
            print("go up")
        else:
            # check neighbours to see if node exists, if not, then 
            new_node = Node() # pass in parent -- needs to have knowledge of current node
            NODE_LIST.add(move_to)

def parse_input():
    with open(TEST_FILE_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line[0] == "$": # Command
                command = stripped_line[2:]
                INSTRUCTION_LIST.append(command)
            else: # Listing directory -- get file size and name
                file_size, file_name = stripped_line.split(" ")
                # print('file size and name: ', file_size, file_name) # Debug

def p1_solution():
    # At this point, have a list of instructions!
    sum_dir_sizes_under_10k = 0

    # Iterate through each line
    # First node is always '/', root
    # Create node, set current_node to that 
    # ls -- this means populate children, if they don't already exist
    # Check for children

    # if it's a dir file size, then it can have an array of children
    # if not dir, call it a "file" and print the size

    # takes in root node (which we already know as '/')






    return sum_dir_sizes_under_10k

# Determine sizes at a directory level!
# Find directories with total size less than or equal to 100000 and sum those. What is the answer?

def run():
    parse_input()
    # print('instruction list: ', INSTRUCTION_LIST)
    # for instruction in INSTRUCTION_LIST:
    #     execute_instruction(instruction)
    # return

if __name__ == "__main__":
    run()