# Chiton

TEST_INPUT = 'puzzle_input.txt'
MATRIX_MULTIPLIER = 5

class Node():
    def __init__(self, value: int):
        self.value = value
        self.neighbors = [] # List of nodes
        self.shortest_path_to_self = 999999999999999999999999

    def __repr__(self):
        return 'Node: ' + str(self.value)
    
    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def get_shortest_path_cost(self):
        return self.shortest_path_to_self


def parse_input_to_matrix(file_path):
    '''
    Args: file_path
    Parses puzzle input and returns:
    
    matrix: 2D array - list of lists of risk level values (int)
    '''
    matrix = []
    with open(file_path) as file:
        for line in file:
            stripped_line = line.strip()
            row = [int(risk_level) for risk_level in stripped_line]
            matrix.append(row)
    return matrix


def find_adjacent_pairs(r, c, matrix):
    '''
    Args: row value (int), column value (int), matrix (2D array, list of lists)

    For improved performance, east and south directions are prioritized over north and west

    Returns: valid_adj_nodes (list of Nodes) - Nodes surrounding the current Node in the 
    cardinal directions that are also within the bounds of the matrix
    '''
    num_rows = len(matrix)
    adj_coords = [(r+1, c), (r, c+1), (r-1, c), (r, c -1)]
    valid_adj_nodes = []

    for coord in adj_coords:
        if 0 <= coord[0] < num_rows and 0 <= coord[1] < num_rows:
            value = matrix[coord[0]][coord[1]]
            neighbor_node = matrix[coord[0]][coord[1]]
            valid_adj_nodes.append(neighbor_node)

    return valid_adj_nodes

    
def create_node_matrix(risk_level_matrix):
    '''
    Converts 2D array of risk levels into 2D array of Nodes.
    '''
    node_matrix = []

    for r in range(len(risk_level_matrix)):
        row = []
        for c in range(len(risk_level_matrix)):
            value = risk_level_matrix[r][c]
            node = Node(value)
            row.append(node)
        node_matrix.append(row)

    return node_matrix, node_matrix[0][0], node_matrix[-1][-1]


def create_connections(node_matrix):
    '''
    Takes in a Node matrix and populates neighbors for each node.
    '''
    matrix_row_count = len(node_matrix)
    matrix_col_count = len(node_matrix[0])
    
    for r in range(matrix_row_count):
        for c in range(matrix_col_count):
            current_node = node_matrix[r][c]
            adj_nodes = find_adjacent_pairs(r, c, node_matrix)
            current_node.neighbors = adj_nodes
    return


def find_lowest_risk_path_value(matrix, start_node, end_node):
    '''
    Explores edges between Nodes to determine the value of the path with the lowest risk cost.
    Starts at the top left Node in the matrix and ends with the bottom right Node. 
    '''
    start_node.shortest_path_to_self = matrix[0][0]
    fringe_stack = [start_node] # Initialize with start node

    while len(fringe_stack) > 0:
        current_node = fringe_stack.pop(0)
        for neighbor in current_node.neighbors:
            check_value = current_node.shortest_path_to_self + neighbor.get_value() 
            if check_value < neighbor.shortest_path_to_self:
                neighbor.shortest_path_to_self = check_value
                fringe_stack.append(neighbor)

    lowest_risk_level_cost = end_node.get_shortest_path_cost() - start_node.get_value()
    # Start node's risk level is not counted - subtract start_node's value from total risk score
    return lowest_risk_level_cost


def increment_matrix_values(matrix):
    '''
    Handles incrementing each value of expanded matrices for part 2. 
    Any value of 9 rolls back down to a 1 when incremented.
    '''

    incremented_matrix = []
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix[0])):
            if matrix[r][c] == 9:
                row.append(1)
            else:
                row.append(matrix[r][c] + 1)
        incremented_matrix.append(row)

    return incremented_matrix

def expand_matrix(matrix, multiplier):
    '''
    Args: matrix (2D array), multiplier (int)
    Expands matrix N-fold where N is the value of the multiplier.
    Ex. a multiplier of 5 will scale the columns and rows 5x the current number,
    making the map 5x larger.
    
    Returns the expanded matrix. 
    '''
    placeholder_matrix = []
    row_count = len(matrix)

    for r in range(row_count):
        row = matrix[r]
        for c in range((multiplier * row_count) - row_count): # number of columns to expand by
            if matrix[r][c] == 9:
                row.append(1)
            else:
                row.append(matrix[r][c] + 1)
        placeholder_matrix.append(row)

    for r in range((multiplier * row_count) - row_count):
        new_row = [x+1 if x < 9 else 1 for x in placeholder_matrix[r]]
        placeholder_matrix.append(new_row)

    return placeholder_matrix


def main():
    # Part 1
    matrix = parse_input_to_matrix(TEST_INPUT)
    node_matrix, start_node, end_node = create_node_matrix(matrix)
    create_connections(node_matrix)
    p1_solution = find_lowest_risk_path_value(matrix, start_node, end_node)
    print('p1 solution: ', p1_solution)

    # Part 2
    expanded_matrix = expand_matrix(matrix, MATRIX_MULTIPLIER) # five-fold matrix
    node_matrix, start_node, end_node = create_node_matrix(expanded_matrix)
    create_connections(node_matrix)
    p2_solution = find_lowest_risk_path_value(expanded_matrix, start_node, end_node)
    print('p2 solution: ', p2_solution)


if __name__ == '__main__':
    main()
