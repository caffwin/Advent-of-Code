TEST_FILE_INPUT = "test_input.txt"
MAX_DIR_SIZE = 100000
TOTAL_DISK_SPACE_AVAILABLE = 70000000
REQUIRED_DISK_SPACE = 30000000

class Node():
    def __init__(self, name, file_type=None, file_size=0, children=None, parent=None, total_size=0) -> str:
        self.name = name
        self.file_type = file_type
        self.file_size = file_size 
        self.children = children
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
            if stripped_line[0] == "$": # Command
                output = stripped_line[2:] # can be "cd" or "ls", do nothing for "ls"
                if output[:2] == "cd": # Ex: "cd a" or "cd .." -- traversing down one level, or up one level
                    cd_cmd, file_name = output.split(" ") # cd_cmd not used
                    if file_name == "/": # Root directory, only applicable to line 1
                        root_node = Node("/", file_type="dir", children={})
                        current_node = root_node
                        root_node_placeholder = root_node
                    
                    # Test input never tries to cds into a file.
                    elif file_name == "..": # Traverse up one level
                        current_node = current_node.parent
                    else: # down one level, assumption is that Node always exists.
                        current_node = current_node.children[file_name]
            else: # Listing either file or dir
                # A directory and a file can't share the same name.
                file_type, file_name = stripped_line.split(" ")
                if file_type == "dir": # A directory - probably find better var since "dir" is a type and not size
                    if file_name not in current_node.children:
                        new_child_node = Node(file_name, file_type="dir", children={}, parent=current_node) # add children dict because dir
                        current_node.file_size += new_child_node.file_size
                        current_node.add_children(new_child_node)

                else: # A file (it'll be a file starting with a numeric value indicating file_size)
                    file_size, file_name = stripped_line.split(" ")
                    # Not a directory -- add the node's file size here to the parent! Only upon instantiation.
                    if file_name not in current_node.children: # Check if already a child
                        new_child_node = Node(file_name, file_type="file", file_size=int(file_size), parent=current_node) # no children
                        current_node.file_size += new_child_node.file_size
                        current_node.add_children(new_child_node)

    calc_sum_dir_sizes_recursive(root_node_placeholder) # Populate directory sizes
    sum = sum_dir_sizes_under_10k(root_node_placeholder)
    print("Part two solution: ", part_two_solution(root_node_placeholder))
    return sum


# Recursive
def calc_sum_dir_sizes_recursive(node):
    if not node.children or node.children == 0: # Regular file
        return node.file_size
    else: # Directory
        size = 0
        for child in node.children:
            child_node = node.children[child]
            size += calc_sum_dir_sizes_recursive(child_node)

        node.file_size = size
        return size

# Iterate through nodes
def sum_dir_sizes_under_10k(node):
    fringe_stack = [node]
    sum_dirs_under_100k = 0
    while fringe_stack:
        current_node = fringe_stack.pop()
        # print("%s %d %s" % (current_node.name, current_node.file_size, current_node.file_type)) # Debug
        if current_node.file_type == "dir":
            for child in current_node.children:
                child_node = current_node.children[child]
                if child_node.file_type == "dir":
                    fringe_stack.append(child_node)
            if current_node.file_size <= 100000:
                sum_dirs_under_100k += current_node.file_size
    return sum_dirs_under_100k

def part_two_solution(root_node):
    total_tree_file_size = root_node.file_size
    current_unused_space = TOTAL_DISK_SPACE_AVAILABLE - total_tree_file_size
    need_to_free = REQUIRED_DISK_SPACE - current_unused_space
    fringe_stack = [root_node]
    closest_file_size = float('inf')

    while fringe_stack:
        current_node = fringe_stack.pop()
        # print("%s %d %s" % (current_node.name, current_node.file_size, current_node.file_type))
        if current_node.file_type == "dir":
            for child in current_node.children:
                child_node = current_node.children[child]
                if child_node.file_type == "dir":
                    fringe_stack.append(child_node)
            if current_node.file_size >= need_to_free:
                closest_file_size = min(closest_file_size, current_node.file_size)
    return closest_file_size

def run():
    part_one_solution = p1_solution()
    print("Part one solution: ", part_one_solution)

if __name__ == "__main__":
    run()