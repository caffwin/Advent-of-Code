import numpy as np

TEST_INPUT = "test_input.txt"
HEIGHTMAP_MATRIX = []
ELEVATION_INDEX_DICT = {
    "S": 26,
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "E": 50
}

START_COORD = None
END_COORD = None


def parse_input():
    with open(TEST_INPUT) as file:
        for line in file:
            row = []
            stripped_line_list = line.strip()
            for char in stripped_line_list:
                row.append(ELEVATION_INDEX_DICT[char])
            HEIGHTMAP_MATRIX.append(row)
            # [HEIGHTMAP_MATRIX.append([*string]) for string in stripped_line_list]

def filter_invalid_coords(coord):
    """
        # Takes in a coordinate (set of ints) and returns a list of valid adjacent coords (set of ints)
        Iterates through the HEIGHTMAP_MATRIX and checks value of each coordinate to find valid neighbour coords that are:
            - In a cardinal direction (NWSE) 
            - Within the bounds of the heightmap matrix (including negative coords) 
            - Less than or equal to 1 height value off (+/-) from the current coordinate's elevation value.

        Returns... []
    """
    heightmap_rows = len(HEIGHTMAP_MATRIX)
    heightmap_cols = len(HEIGHTMAP_MATRIX[0])

    adjacent_coordinate_values = []
    adjacent_coordinates = [(coord[0]-1, coord[1]), (coord[0]+1, coord[1]), (coord[0], coord[1]-1), (coord[0], coord[1]+1)]
    valid_adjacent_coords = []    

    for coord_pair in adjacent_coordinates:
        if 0 <= coord_pair[0] < heightmap_rows and 0 <= coord_pair[1] < heightmap_cols: # Within bounds of matrix
            if np.abs(HEIGHTMAP_MATRIX[coord_pair[0]][coord_pair[1]]%26 - HEIGHTMAP_MATRIX[coord[0]][coord[1]]%26) <= 1: # Value within 1
                valid_adjacent_coords.append(coord_pair) # coords
                adjacent_coordinate_values.append(HEIGHTMAP_MATRIX[coord_pair[0]][coord_pair[1]]) # for debug?
        # else:
        #     print('coord pair filtered out: ', coord_pair) # Debug
    print("valid_adjacent_coords: ", valid_adjacent_coords)
    return valid_adjacent_coords

def find_start_end_coords(HEIGHTMAP_MATRIX):
    """
        Check each coordinate in HEIGHTMAP_MATRIX for upper case S (start) and E (end) coordinate and populate global 
        variables START_COORD and END_COORD (tuple of two ints, row followed by col value), returning them in that order. 
    """
    len_matrix_row = len(HEIGHTMAP_MATRIX)
    len_matrix_cols = len(HEIGHTMAP_MATRIX[0])

    for i in range(len_matrix_row):
        row = HEIGHTMAP_MATRIX[i]
        for j in range(len_matrix_cols):
            print("i, j: ", i, j)
            col_value = HEIGHTMAP_MATRIX[i][j]
            if col_value == 26:
                START_COORD = (i, j)
            if col_value == 50:
                END_COORD = (i, j)

    return START_COORD, END_COORD

def part_one_solution(start_coord):
    current_node_coord = None
    len_shortest_path = 0
    fringe_stack = [start_coord] # Initialize with root node value
    visited_nodes = [] # visited node list only grows

    while fringe_stack:
        print("Looping through fringe stack: ", fringe_stack)
        current_node_coord = fringe_stack.pop() # last item
        print('current_node coord is: ', current_node_coord)
        valid_coord_list = filter_invalid_coords(current_node_coord) # Feed in any coord, for start
        print("valid_coord_list: ", valid_coord_list)
        
        len_shortest_path += 1
        for coord in valid_coord_list:
            coord_value = HEIGHTMAP_MATRIX[coord[0]][coord[1]]
            if coord not in visited_nodes:
                print("checking neighbor coord: ", coord, "with value: ", coord_value)
                visited_nodes.append(coord)
                fringe_stack.append(coord)
                if coord_value == 50:
                    print("breaking, found E: ", coord_value, " at: ", coord)
                    len_shortest_path_minus_start_end_nodes = len_shortest_path - 2
                    return len_shortest_path_minus_start_end_nodes

    len_shortest_path_minus_start_end_nodes = len_shortest_path - 2
    # print("len_shortest_path_minus_start_end_nodes: ", len_shortest_path_minus_start_end_nodes)
    return len_shortest_path_minus_start_end_nodes # len_shortest_path_minus_start_end_nodes

# Sabqpo
# accExk
# acctuv


def main():
    parse_input() # Populates HEIGHTMAP_MATRIX
    result = find_start_end_coords(HEIGHTMAP_MATRIX)
    start_coord, end_coord = find_start_end_coords(HEIGHTMAP_MATRIX) # Find start and end coords
    p1_solution = part_one_solution(start_coord)
    print("Part one solution: ", p1_solution)
    
    return

if __name__ == "__main__":
    main()

# 4516 too high