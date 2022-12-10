TEST_FILE_INPUT = "test_input.txt"
MAX_DIR_SIZE = 100000

class Node():
    def __init__(self, name, file_type=None, file_size=0, children=None, parent=None, total_size=0) -> str:
        self.name = name
        self.file_type = file_type
        self.file_size = file_size 
        self.children = children # By default, no children unless directory -- then pass in list of additional nodes?
        self.parent = parent
        self.total_size = total_size

    def add_children(self, child_node):
        self.children[child_node.name] = child_node

    def show_children(self):
        print(self.children)

    def print_name(self):
        print(self.name)

def p1_solution():
    root_node_placeholder = None
    current_node = None

    # Populate tree as listing out files/dirs
    with open(TEST_FILE_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            # if current_node:
            #     print("current node is: ", current_node.name)
            if stripped_line[0] == "$": # Command
                output = stripped_line[2:] # can be "cd" or "ls", do nothing for "ls"
                if output[:2] == "cd": # Ex: "cd a" or "cd .." -- traversing down one level, or up one level
                    cd_cmd, file_name = output.split(" ") # cd_cmd not used
                    if file_name == "/": # Root directory, only applicable to line 1
                        print("** This the root directory! Creating a root node", )
                        root_node = Node("/", children={})
                        current_node = root_node
                        root_node_placeholder = root_node
                    
                    # Test input never tries to cds into a file.
                    elif file_name == "..": # Traverse up one level
                        # print("** This is a cd command -- going up one level to: ", current_node.parent.name)
                        current_node = current_node.parent
                    else: # down one level, # Node always exists.
                        # print("** This is a cd command -- checking.. ", file_name)
                        current_node = current_node.children[file_name]
            else: # Listing either file or dir
                # A directory and a file can't share the same name.
                file_type, file_name = stripped_line.split(" ")
                if file_type == "dir": # A directory - probably find better var since "dir" is a type and not size
                    # print("** The file is a directory: ", file_name)
                    # If it's a directory, only add if it's not a child
                    if file_name not in current_node.children:
                        # print("**** This is a directory and does not exist in the current node's children, adding new node with name: ", file_name, "to", current_node.name)
                        new_child_node = Node(file_name, file_type="dir", children={}, parent=current_node) # add children dict because dir
                        current_node.file_size += new_child_node.file_size
                        current_node.add_children(new_child_node)

                else: # A file (it'll be a file starting with a numeric value indicating file_size)
                    file_size, file_name = stripped_line.split(" ")
                    # Not a directory -- add the node's file size here to the parent! Only upon instantiation.
                    if file_name not in current_node.children: # Check if already a child
                        new_child_node = Node(file_name, file_type="file", file_size=int(file_size), parent=current_node) # no children
                        current_node.file_size += new_child_node.file_size
                        # print("** The file is not a directory, it has name: ", file_name, "and size: ", file_size, " adding ", file_name, "to", current_node.name)
                        current_node.add_children(new_child_node)

    sum = sum_dir_sizes_under_10k(root_node_placeholder)
    return sum

def sum_dir_sizes_under_10k(root_node):
    # Try DFS, only regarding directories.
    fringe_stack = [root_node] 
    sum_dir_sizes_under_10k = 0
    dir_size_list = []
    visited_list = []
    # Can store a tuple of (name, size)
    current_node = None
    while len(fringe_stack) > 0:
        current_node = fringe_stack.pop(0)
        print('current node name: ', current_node.name)
        print('current node: ', current_node.show_children())
        # total_size_current_node = current_node.file_size
        # print('file size of node: ', total_size_current_node)
        for child in current_node.children: # child is a string
            child_node = current_node.children[child]
            if child_node.file_type == "dir" and child_node.name not in visited_list: # current_node.children[child] returns the value, which is the node
                # itzOnlyDirectoriez
                # total_size_current_node += child_node.file_size
                fringe_stack.append(child_node)
                # If it's a directory, not in visited list, then add sum
                dir_tuple = (child_node.name, child_node.file_size)
                dir_size_list.append(dir_tuple)
                print('Directory child node found! dir name: ', child_node.name, " and size: ", str(child_node.file_size))
                # dir_tuple = (child_node.name, child_node.file_size)
                # dir_size_list.append(dir_tuple)
                # add child node to parent node's size


    for dir_size_pair in dir_size_list:
        if dir_size_pair[1] <= MAX_DIR_SIZE:
            sum_dir_sizes_under_10k += dir_size_pair[1]
    # Loop through and sum sizes, then return sum_dir_sizes_under_10k
    # Traverse through entire `tree`
    print("dir_size_list: ", dir_size_list)
    return sum_dir_sizes_under_10k

# Determine sizes at a directory level!
# Find directories with total size less than or equal to 100000 and sum those. What is the answer?

def run():
    print('henlo')
    part_one_solution = p1_solution()
    print("p1 solution: ", part_one_solution)

if __name__ == "__main__":
    run()