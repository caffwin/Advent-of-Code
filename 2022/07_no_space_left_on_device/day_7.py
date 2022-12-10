TEST_FILE_INPUT = "test_input.txt"

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
        return self.children

    def print_name(self):
        print(self.name)

def p1_solution():
    sum_dir_sizes_under_10k = 0
    root_node_flag = False
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
                        root_node_flag == True
                        root_node = Node("/", children={})
                        current_node = root_node
                        # Root node!
                    
                    # Test input never tries to cds into a file.
                    elif file_name == "..": # Traverse up one level
                        print("** This is a cd command -- going up one level to: ", current_node.parent.name)
                        current_node = current_node.parent
                    else: # down one level, # Node always exists.
                        print("** This is a cd command -- checking.. ", file_name)
                        current_node = current_node.children[file_name]
            else: # Listing directory -- get file size and name. Ex: "29116 f"
                # A directory and a file can't share the same name.
                file_type, file_name = stripped_line.split(" ")
                if file_type == "dir": # probably find better var since "dir" is a type and not size
                    # If it's a directory, only add if it's 
                    print("** The file is a directory: ", file_name)
                    # check current node's neighbours 
                    if file_name not in current_node.children:
                        print("**** This is a directory and does not exist in the current node's children, adding new node with name: ", file_name, "to", current_node.name)
                        new_child_node = Node(file_name, file_type="dir", children={}, parent=current_node) # add children dict because dir
                        current_node.add_children(new_child_node)
                    # else: # file, ex "dir e" already exists: do nothing

                # If the size isn't "dir", then it's always a numerical value greater than 0 
                # if int(file_size) > 0:
                else: # Either a directory, or not (it'll be a file starting with a numeric value indicating file_size)
                    file_size, file_name = stripped_line.split(" ")
                    
                    if file_name not in current_node.children: # Check if already a child
                        new_child_node = Node(file_name, file_type="file", file_size=int(file_size), parent=current_node) # no children
                        print("** The file is not a directory, it has name: ", file_name, "and size: ", file_size, " adding ", file_name, "to", current_node.name)
                        current_node.add_children(new_child_node)

def sum_dir_sizes(root_node):
    sum_dir_sizes_under_10k = 0
    list_dir_sizes_under_10k = []
    # Loop through and sum sizes, then return sum_dir_sizes_under_10k
    return sum_dir_sizes_under_10k

# Determine sizes at a directory level!
# Find directories with total size less than or equal to 100000 and sum those. What is the answer?

def run():
    print('henlo')
    part_one_solution = p1_solution()
    print("p1 solution: ", part_one_solution)

if __name__ == "__main__":
    run()