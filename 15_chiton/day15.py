# Chiton

TEST_INPUT = 'test_input.txt'

def parse_input_to_matrix(file_path):
    '''
    Parses puzzle input and returns:
    
    matrix: 2D array - list of lists of risk levels (int)
    '''
    matrix = []
    with open(file_path) as file:
        for line in file:
            stripped_line = line.strip()
            row = [int(risk_level) for risk_level in stripped_line]
            matrix.append(row)
    return matrix

class Node():
    def __init__(self, value: str, coordinates=None):
        self.value = value
        self.neighbors = [] # List of nodes
        self.coordinates = coordinates
        self.path_to_self = []

    def __repr__(self):
        return 'Node: ' + str(self.value)
    
    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def get_current_path(self):
        return self.path_to_self


def find_adjacent_pairs(r, c, matrix):
    num_rows = len(matrix)
    adj_coords = [(r-1, c), (r+1, c), (r, c -1), (r, c+1)]
    valid_adj_nodes = []

    for coord in adj_coords:
        if 0 <= coord[0] < num_rows and 0 <= coord[1] < num_rows:
            value = matrix[coord[0]][coord[1]]
            neighbor_node = matrix[coord[0]][coord[1]]
            valid_adj_nodes.append(neighbor_node)

    return valid_adj_nodes


def create_node_matrix(matrix):
    node_matrix = []
    matrix_idx_length = len(matrix) - 1
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix)):
            current_coord = (r, c)
            value = matrix[r][c]
            node = Node(value, current_coord)
            row.append(node)
            if r == 0 and c == 0:
                start_node = node

            if r == matrix_idx_length and c == matrix_idx_length:
                end_node = node
        node_matrix.append(row)

    print(node_matrix)
    return node_matrix, node_matrix[0][0], node_matrix[matrix_idx_length][matrix_idx_length] # should be start node

def create_connections(node_matrix):

    for r in range(len(node_matrix)):
        for c in range(len(node_matrix)):
            current_node = node_matrix[r][c]
            adj_nodes = find_adjacent_pairs(r, c, node_matrix)
            current_node.neighbors = adj_nodes
    return

def main():
    matrix = parse_input_to_matrix(TEST_INPUT)
    node_matrix, start_node, end_node = create_node_matrix(matrix)
    create_connections(node_matrix)

if __name__ == '__main__':
    main()
