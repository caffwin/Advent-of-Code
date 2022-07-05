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

    def return_value(self):
        return self.value

    def return_neighbors(self):
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

def dfs_paths_iterative(root_node):
    """
    Use Node class
    Add node to current_path list
    Check neighbors and set to variable


    Keep checking until letter .isupper(), that's the end node
    Could record end nodes in a list to ignore those neighbours? But seems dumb because xXxtra storage & too contextual

    If length of unvisited neighbours is 0, we've reached 
    Unvisited neighbors is current node's neighbours minus visited nodes

    Add neighbors to current path
    """
    total_paths = 0
    stack = [root_node]
    current_path = []
    visited_nodes = set()
    
    while len(stack) > 0:

        current_node = stack.pop()
        current_path.append(current_node)
        visited_nodes.add(current_node)
        unvisited_neighbors = set(current_node.neighbors) - visited_nodes # a set
        
        # if current_node.return_value() != 'end': # and current_node.return_value().islower():
            # visited_nodes.add(current_node)

        if current_node.return_value() == 'end': # Behaviour only for end node
            total_paths += 1
            current_path.pop() # Remove the end node to make room for other paths

        else: # If not end node, add visitors
            for neighbor in current_node.neighbors:
                if neighbor in unvisited_neighbors:
                    stack.append(neighbor)
                else:
                    print('neighbor has been visited: ', neighbor.return_value())

    return total_paths


def main():
    edges = parse_edges_from_input(TEST_FILE_NAME)
    graph_adjacent_pairs = edges # [('start', 'A'), ('start', 'b'), ('A', 'b'), ('b', 'c'), ('A', 'c'), ('c', 'end')]

    node_dict = GenerateGraph(graph_adjacent_pairs)
    root_node = node_dict['start']

    print(dfs_paths_iterative(root_node))

    return


if __name__ == "__main__":
    main()
