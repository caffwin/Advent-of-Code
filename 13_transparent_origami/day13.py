# Transparent origami
 
TEST_FILE_PATH = 'puzzle_input.txt'
 
def parse_input(file_path):
    """
    Populates matrix row/col values using max x and y coord values
    Returns...

    max_cols, max_rows
    first_fold_instruction
    all_coords
    """
    fold_flag = False
    all_coords = []

    with open(file_path) as file:
        x_crease_values = []
        y_crease_values = []
        max_cols = 0 # x coord max
        max_rows = 0 # y coord max

        first_fold_instruction = {}
        first_fold_flag = False

        for line in file:
            stripped_line = line.strip()
    
            if line == '\n':
                fold_flag = True
    
            if fold_flag == False:
                x_coord, y_coord = stripped_line.split(',')
                all_coords.append((int(x_coord), int(y_coord)))
    
                if int(x_coord) > max_cols:
                    max_cols = int(x_coord)
                if int(y_coord) > max_rows:
                    max_rows = int(y_coord)
    
            else: # fold_flag == True
                if line != '\n' and first_fold_flag == False:
                        axis_phrase, value = stripped_line.split('=')
                        axis = axis_phrase[-1]
                        first_fold_instruction[axis] = int(value)
                        first_fold_flag = True # First row only for part 1 solution

                    # For x and y values
                    #    if direction[-1] == 'x':
                    #        x_crease_values.append(int(value))
                    #    if direction[-1] == 'y': # direction is y
                    #        y_crease_values.append(int(value))
 
 
        # print('VERTICAL_CREASE_LIST: ', y_crease_values)
        # print('HORIZONTAL_CREASE_LIST: ', x_crease_values)

    return max_cols, max_rows, first_fold_instruction, all_coords
#    return max_cols, max_rows, y_crease_values, x_crease_values, all_coords
 
def pp_matrix(matrix):
    for row in matrix:
        string_row = ''.join(row)
        print(string_row)
    return

# Old working function
# def build_matrix(rows, cols, coord_list):
#     matrix = []
#     # num_marks = 0
    
#     # test_y_fold = 7
#     # test_x_fold = 5
#     for r in range(rows + 1):
#         row = []
#         for c in range(cols + 1):
#             # For debugging purposes
#             # if c == test_x_fold or r == test_y_fold:
#             #     # print("c matches test x fold")
#             #     row.append('-')
#             #     # Under this condition, can start to modify coordinates
#             # elif (c, r) in coord_list:
#             if (c, r) in coord_list:
#                 row.append('#')
#                 # num_marks += 1 # Also debugging
#             else:
#                 row.append('.')
#         matrix.append(row)   
#     return matrix
 

def build_matrix(rows, cols, coord_list):
    matrix = []

    test_x_fold = None
    test_y_fold = 7
    for r in range(rows + 1):
        row = []
        for c in range(cols + 1):
            # For debugging purposes
            if c == test_x_fold or r == test_y_fold:
                row.append('-')
            elif (c, r) in coord_list:
                row.append('#')
            else:
                row.append('.')
        matrix.append(row)
    
    return matrix
 
def part_one_solution(matrix, all_coords, first_fold_instruction):
    """
        Calculates dot count after the first fold instruction.
        Takes in a marked matrix (list of lists), the first fold instruction (dict), and returns
        the number of dots after the transformation is applied.

        Y folds always take dots below and transform above the line
        Y folds always take dots from the right and transform to left of line

        [Make sure to account for overlapping dots ('#')! The dots count should be less than the total number of coordinates]
    """

    new_coords_list = []
    modified_matrix = []
    dot_count = 0

    fold_value = first_fold_instruction['x'] # 7
    # fold_value = first_fold_instruction['y']

    # Eliminate matrix rows after the fold row:
    if 'y' in first_fold_instruction:
        transform_coords_list = [coord for coord in all_coords if coord[1] > first_fold_instruction['y']]

        # Process coordinates -- check distance for column value (coord[0])
        for coord in transform_coords_list:
            difference = coord[1] - fold_value
            shifted_value = fold_value - difference
            transformed_coord = (coord[0], shifted_value)
            new_coords_list.append(transformed_coord)

        for r in range(fold_value): # 0 to 6 -- excludes 7, the fold row
            modified_matrix.append(matrix[r])

    elif 'x' in first_fold_instruction:
        transform_coords_list = [coord for coord in all_coords if coord[0] > first_fold_instruction['x']] # Take all coords right of line

        # Process coords
        for coord in transform_coords_list:
            difference = coord[0] - fold_value
            shifted_value = fold_value - difference
            transformed_coord = (shifted_value, coord[1])
            new_coords_list.append(transformed_coord)

        for r in range(len(matrix)):
            slice_end_index = first_fold_instruction['x'] - len(matrix[0]) + 1 # find slice end index
            modified_matrix.append((matrix[r])[:slice_end_index])

    else: 
        print('no fold instructions for x or y')

    # Set new dots
    for coord in new_coords_list:
        modified_matrix[coord[1]][coord[0]] = '#'

    modified_matrix_rows = len(modified_matrix)
    modified_matrix_cols = len(modified_matrix[0])

    # Sum dots
    for r in range(modified_matrix_rows):
        for c in range(modified_matrix_cols):
            if modified_matrix[r][c] == '#':
                dot_count += 1

    return dot_count

 
def main():
    # max_cols, max_rows, y_crease_values, x_crease_values, coord_list = parse_input(TEST_FILE_PATH) # Populates matrix x/y values
    max_cols, max_rows, first_fold_instruction, coord_list = parse_input(TEST_FILE_PATH) 
    marked_matrix = build_matrix(max_rows, max_cols, coord_list)
    print(pp_matrix(marked_matrix))
    # part_one_solution(marked_matrix, x_crease_values, y_crease_values)
    print(part_one_solution(marked_matrix, coord_list, first_fold_instruction))
 
if __name__ == '__main__':
   main()

