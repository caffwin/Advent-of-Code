# Day 12 Passage Pathing

TEST_FILE_NAME = 'test_input.txt'
PUZZLE_INPUT_FILE = 'puzzle_input.txt'

def parse_edges_from_input(file_name):
    """
    Takes in puzzle input, parses through lines containing graph vertices and returns:
    edges: a set of tuples, unique collection (ordered pairs) or vertices that are adjacent to one another
    vertices: a unique list of strings containing all vertices present in the graph
    """

    vertices = []
    edges = set()

    with open(file_name) as file:
        for line in file:
            stripped_line = line.strip()
            vertex_one, vertex_two = stripped_line.split('-')

            if vertex_one not in vertices:
                vertices.append(vertex_one)
            if vertex_two not in vertices:
                vertices.append(vertex_two)

            edges.add((vertex_one, vertex_two))

    return vertices, edges

def create_vertex_dict(vertices):
    """
    Vertex dict that describes mapping from indices to vertex names.
    """
    vertex_dict = {}
    for i, vertex in enumerate(vertices):
        vertex_dict[vertex] = i

    return vertex_dict

def initialize_adj_dict(vertices):
    adj_dict = {}
    for vertex in vertices:
        adj_dict[vertex] = []
    return adj_dict


def create_adjacency_dict(vertices, edges):
    adj_dict = initialize_adj_dict(vertices) # A dict containing vertices as keys and empty lists as values
    # Populate adj_dict:
    for edge in edges:
        adj_dict[edge[0]].append(edge[1])
        adj_dict[edge[1]].append(edge[0])

    return adj_dict

# def create_adjacency_matrix(vertex_dict, edge_set):
#     """
#     Creates an adjacency matrix using 
#     Takes in edges (a set of tuples) and dict of indexed vertices

#     Row (r) and column (c) values represent 
#     # Checks through 
#     """
    
#     dict_length = len(vertex_dict)
#     adj_matrix = []

#     # Create matrix with length and width equal to number of vertices 
#     for num_r in range(dict_length):
#         row = []
#         for num_c in range(dict_length):
#             row.append(0)
#         adj_matrix.append(row)

#     # Mark coordinates for adjacent pairs in matrix
#     for edge_pair in edge_set:
#         r = vertex_dict[edge_pair[0]]
#         c = vertex_dict[edge_pair[1]]
#         adj_matrix[r][c] = 1
#         adj_matrix[c][r] = 1

#     return adj_matrix


def check_if_adjacent():
    # if r, c in adj_dict or c, r in adj_dict then ...
    return True
    # else, return False

def part_one_solution(adj_dict, start_node):
    """
    Takes in a unique list of vertices and edges (set of tuples) and performs graph traversal (DFS? expand later) to find the total number of
    possible paths through the cave system (graph). 
    Lower-case letters represent small caves and can only be traversed through once.
    Upper-case letters represent large caves that can be traversed through any number of times.
    Paths must start at start, and end at end.
    """

    invalid_vertices = [] # Includes small caves that have been traversed through already and start vertex
    unique_sequences = set()

    
    # islower() and isupper()


    # Chceck which other vertices are adjacent, and if it's not in traversed_small_caves, continue searching through matrix?
    # Mark off small caves that have already been traversed through, only nodes that are not in here can be traversed

    # Challenges: 
    # Recording all of the valid route sequences, excluding routes that don't end on "end"
    # Making sure start node is not traversed through after first move
    # Potential for recomputation if there's no way to validate the path until it's complete and added to the sequence

    # unique_paths = len(set_paths)
    return # unique_paths


def main():
    vertices, edges = parse_edges_from_input(TEST_FILE_NAME)
    adj_dict = create_adjacency_dict(vertices, edges)
    # Create edges...  
    start_node = 'start' # always starts here

    print('part one solution: ', part_one_solution(adj_dict, 'start'))

    return


if __name__ == "__main__":
    main()