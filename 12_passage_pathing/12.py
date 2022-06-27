# 12 Passage Pathing

TEST_FILE_NAME = 'test_input.txt'
PUZZLE_INPUT_FILE = 'puzzle_input.txt'


class Node():
    def __init__(self, is_big_cave=False, adj_nodes=[]):
        self.is_big_cave = is_big_cave
        self.adj_nodes = adj_nodes

    def return_adj_nodes(self):
        return self.adj_nodes

def parse_edges_from_input(file_name):
    """
    Takes in puzzle input, parses through lines containing graph vertices and returns:
    edges: a set of tuples, unique collection (ordered pairs) or vertices that are adjacent to one another
    vertices: a unique list of strings containing all vertices present in the graph
    """

    vertices = []
    edges = []

    with open(file_name) as file:
        for line in file:
            stripped_line = line.strip()
            vertex_one, vertex_two = stripped_line.split('-')

            if vertex_one not in vertices:
                vertices.append(vertex_one)
            if vertex_two not in vertices:
                vertices.append(vertex_two)

            edges.append((vertex_one, vertex_two))

    return vertices, edges

def initialize_adj_dict(vertices):
    adj_dict = {}
    for vertex in vertices:
        adj_dict[vertex] = []
    return adj_dict

def create_adjacency_dict(vertices, edges):
    adj_dict = initialize_adj_dict(vertices) # A dict containing vertices as keys and empty lists as values
    for edge in edges:
        adj_dict[edge[0]].append(edge[1])
        adj_dict[edge[1]].append(edge[0])

    return adj_dict

def part_one_solution(adj_dict, start_node):
    """
    Takes in a unique list of vertices and edges (set of tuples) and performs graph traversal (DFS? expand later) to find the total number of
    possible paths through the cave system (graph). 
    Lower-case letters represent small caves and can only be traversed through once.
    Upper-case letters represent large caves that can be traversed through any number of times.
    Paths must start at start, and end at end.
    """

    stack = [start_node] # always initialize to start node
    invalid_vertices = [] # Includes small caves that have been traversed through already and start vertex
    num_unique_sequences = 0

    while len(stack) > 0:

        current_node = stack.pop() # 'start'
        print('current node: ', current_node)
        adj_nodes = adj_dict[current_node]
        print('adj_nodes: ', adj_dict[current_node])
        if current_node.islower() and current_node != 'end': # Can this even happen if "end" nodes never make it in the stack?  
            print('adding to invalid_vertices: ', current_node)
            invalid_vertices.append(current_node)
        else:
            print(current_node, 'is a big cave')

        for adj_node in adj_nodes:
            print('Checking adj nodes and entering for loop.... adj_node is: ', adj_node)
            if adj_node not in invalid_vertices and adj_node != 'end': # Add node if not invalid
                print('adding node: ', adj_node)
                stack.append(adj_node)

            if adj_node == 'end':
                num_unique_sequences += 1
                print('adding one to unique sequences')

        print('invalid vertices: ', invalid_vertices)
        print('current stack: ', stack)

    return num_unique_sequences


def main():
    vertices, edges = parse_edges_from_input(TEST_FILE_NAME)
    adj_dict = create_adjacency_dict(vertices, edges)

    # test_adj_dict = {
    #     'a': ['b', 'c'],
    #     'b': ['d'],
    #     'c': ['e'],
    #     'd': ['f'],
    #     'e': [],
    #     'f': []
    # }
    start_node = 'start' # always starts here
    print('*** adj_dict: ', adj_dict)
    print('part one solution: ', part_one_solution(adj_dict, 'start'))

    return


if __name__ == "__main__":
    main()


# *** adj_dict:  {'start': ['b', 'A'], 'A': ['b', 'end', 'start', 'c'], 'b': ['start', 'A', 'end', 'd'], 'c': ['A'], 'd': ['b'], 'end': ['b', 'A']}
# *** adj_dict:  {'start': ['b', 'A'], 'A': ['c', 'start', 'b', 'end'], 'b': ['d', 'start', 'end', 'A'], 'c': ['A'], 'd': ['b'], 'end': ['b', 'A']}
# *** adj_dict:  {'start': ['A', 'b'], 'A': ['b', 'start', 'c', 'end'], 'b': ['A', 'd', 'end', 'start'], 'c': ['A'], 'd': ['b'], 'end': ['b', 'A']} # 5
# *** adj_dict:  {'start': ['A', 'b'], 'A': ['start', 'b', 'c', 'end'], 'b': ['end', 'd', 'A', 'start'], 'c': ['A'], 'd': ['b'], 'end': ['b', 'A']} # 7
# *** adj_dict:  {'start': ['b', 'A'], 'A': ['c', 'start', 'end', 'b'], 'b': ['start', 'end', 'd', 'A'], 'c': ['A'], 'd': ['b'], 'end': ['b', 'A']} # 11