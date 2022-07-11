# 12 Passage Pathing
from typing import Dict, List, Tuple

TEST_FILE_NAME = 'test_input.txt'
PUZZLE_INPUT_FILE = 'puzzle_input.txt'

class Node:
    '''
    Member variables:
     - self.value: str
     - self.neighbors: List[Node]
    '''
    def __init__(self, value: str):
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

def ConnectNodes(node, other_node):
    node.neighbors.append(other_node)
    other_node.neighbors.append(node)

def GenerateGraph(adjacent_pairs: List[Tuple[str, str]]) -> Dict[str, Node]:
    node_dict = {}
    for left_value, right_value in adjacent_pairs:
        # Create nodes if missing
        for value in left_value, right_value:
            if (value not in node_dict):
                node_dict[value] = Node(value)
        # Add connection
        ConnectNodes(node_dict[left_value], node_dict[right_value])
    return node_dict


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

    return edges

def dfs_paths_iterative_basic(root_node):
    '''
    Takes in a root node and prints out all possible paths using iterative depth-first search to the end node
    
    Fringe stack contains a tuple, pair of node and the path traversed to get to that node:
    node (instance of Node class), current_path (list))
    '''
    total_paths = 0
    fringe_stack = [(root_node, [])]
    current_path = []
    visited_nodes = set()
    
    while len(fringe_stack) > 0:
        current_node, current_path = fringe_stack.pop()
        visited_nodes = current_path
        visited_nodes.append(current_node)

        unvisited_neighbors = set(current_node.neighbors) - set(visited_nodes)

        if current_node.get_value() == 'end':
            print('*** Reached end, current path: ', [repr(node) for node in current_path])
            total_paths += 1

        else:
            if len(unvisited_neighbors) == 0:
                print("No neighbours left..", [repr(node) for node in current_path])
                current_path.pop()
            else:
                for neighbor in current_node.neighbors:
                    if neighbor in unvisited_neighbors or neighbor.get_value().isupper(): # Covers start-A-b-A-end
                        print('neighbor in unvisited nodes, adding to stack: ', neighbor.get_value())
                        fringe_stack.append((neighbor, list(current_path)))
                    else:
                        print('neighbour has already been visited, not adding: ', neighbor.get_value())

    return total_paths


def main():
    edges = parse_edges_from_input(TEST_FILE_NAME)
    graph_adjacent_pairs = edges # [('start', 'A'), ('start', 'b'), ('A', 'b'), ('b', 'c'), ('A', 'c'), ('c', 'end')]
    node_dict = GenerateGraph(graph_adjacent_pairs)
    root_node = node_dict['start']
    print('basic ver: ', dfs_paths_iterative_basic(root_node))
    return

if __name__ == '__main__':
    main()
