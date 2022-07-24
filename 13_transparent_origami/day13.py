# Transparent origami
 
TEST_FILE_PATH = 'puzzle_input.txt'

# Final matrix size:
CODE_MATRIX_COL_COUNT = 38
CODE_MATRIX_ROW_COUNT = 5

 
def parse_input(file_path):
    """
    Parses puzzle input and calculates matrix row and column values. 
    Creates a list of fold instructions and a list of coordinates that represent where dots are marked.
    
    Args:
    file_path (str): Path to puzzle input file

    Returns:
    fold_instructions (list of tuples)
    all_coords (set of tuples)
    """
    fold_flag = False
    all_coords = set()

    with open(file_path) as file:
        max_cols = 0 # x coord max
        max_rows = 0 # y coord max
        fold_instructions = []

        for line in file:
            stripped_line = line.strip()
    
            if line == '\n':
                fold_flag = True
    
            if fold_flag == False:
                x_coord, y_coord = stripped_line.split(',')
                all_coords.add((int(x_coord), int(y_coord)))
    
                if int(x_coord) > max_cols:
                    max_cols = int(x_coord)
                if int(y_coord) > max_rows:
                    max_rows = int(y_coord)
    
            else: # fold_flag == True
                if line != '\n':
                    direction, value = stripped_line.split('=')
                    if direction[-1] == 'x':
                        fold_instructions.append(('x', int(value)))
                    if direction[-1] == 'y': # axis is y
                        fold_instructions.append(('y', int(value)))

    return fold_instructions, all_coords


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
    fold_value = 7 # Hard coding for test

    if 'y' in first_fold_instruction:
        transform_coords_list = [coord for coord in all_coords if coord[1] > fold_value]

        # Process coordinates -- check distance for column value (coord[0])
        for coord in transform_coords_list:
            difference = coord[1] - fold_value
            shifted_value = fold_value - difference
            transformed_coord = (coord[0], shifted_value)
            new_coords_list.append(transformed_coord)

        for r in range(fold_value): # 0 to 6 -- excludes 7, the fold row
            modified_matrix.append(matrix[r])

    elif 'x' in first_fold_instruction:
        transform_coords_list = [coord for coord in all_coords if coord[0] > fold_value] # first_fold_instruction['x']] # Take all coords right of line

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

def apply_fold_transformation(all_coords, fold_instruction):
    transformed_coords_set = set()
    fold_axis = fold_instruction[0]
    fold_value = fold_instruction[1]

    if fold_axis == 'y':
        transform_coords_set = set(coord for coord in all_coords if coord[1] > fold_value)
        remaining_coords = all_coords - transform_coords_set

        for coord in transform_coords_set:
            difference = coord[1] - fold_value
            shifted_value = fold_value - difference
            transformed_coord = (coord[0], shifted_value)
            transformed_coords_set.add(transformed_coord)
            
    else:
        transform_coords_set = set(coord for coord in all_coords if coord[0] > fold_value)
        remaining_coords = all_coords - transform_coords_set
        for coord in transform_coords_set:
            difference = coord[0] - fold_value
            shifted_value = fold_value - difference
            transformed_coord = (shifted_value, coord[1])
            transformed_coords_set.add(transformed_coord)

    new_coords_set = transformed_coords_set | remaining_coords
    return new_coords_set

def part_two_solution(all_coords, fold_instructions):
    """
        Takes in a set of initial coordinates where dot appear from puzzle input and a list of fold instructions.
        Returns a list of coordinates representing the final state that reflect the remaining coordinates after all 
        fold instructions have been applied. The state is modified each time fold transformation logic is executed. 
        Each state represents the current list of coordinates up to the current set of fold instructions.

        Y folds always take dots below and transform above the fold
        X folds always take dots from the right of the fold and transform them to the left side

        Args:
        all_coords (set of tuples): A set of coordinates (row, column) that mark where first set of dots appear
        fold_instructions (list of tuples): Each tuple contains the axis (str) and value (int). Ex. ('y', 7)

        Returns:
        state (set): A set of coordinates that represents the final state after all fold transformations have been made.
    """
    state = all_coords

    for fold_instruction in fold_instructions:
        state = apply_fold_transformation(state, fold_instruction)

    return state

def plot_coords(coords):    
    modified_matrix = []
    for r in range(CODE_MATRIX_ROW_COUNT + 1):
        row = []
        for c in range(CODE_MATRIX_COL_COUNT + 1):
            if (c, r) in coords:
                row.append('#')
            else:
                row.append('.')
        modified_matrix.append(row)

    return modified_matrix
 
def main():
    fold_instructions, coord_list = parse_input(TEST_FILE_PATH)
    final_state = part_two_solution(coord_list, fold_instructions) # returns all coords from final state
    final_state_matrix = plot_coords(final_state)
    pp_matrix(final_state_matrix) # PGHZBFJC
 
if __name__ == '__main__':
   main()
