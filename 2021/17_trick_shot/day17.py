# target area: x=5..7, y=-3..-6
# target area: x=20..30, y=-10..-5

TEST_INPUT_FILE = 'test_input.txt'

def parse_input(file_name):
    # Returns target area coords, x and y
    # (5, 7), (-3,-6)
    x_area = tuple()
    y_area = tuple()
    with open(file_name) as file:
        x_bounds, y_bounds = file.readline()[13:].split(',')
        x_min, x_max = x_bounds.strip()[2:].split('..')
        y_min, y_max = y_bounds.strip()[2:].split('..')
        x_area += (int(x_min), int(x_max))
        y_area += (int(y_min), int(y_max))

    return x_area, y_area

def perform_step_transformations(velocity_pair):
    # Takes in pair of velocity pairs, a tuple? (x, y)

    # For each step, increase x and y by initial velocity values
    # x increments/decrements 1 towards 0, y decrements by 1

    # x += x_initial_velocity + 1 #  if any negative values are in x_target, else -1
    # y += y_initial_velocity - 1
    return

def create_matrix(x_area, y_area):
    # Based on target area upper/lower bounds, create matrix from 0,0 start coord to include that area
    # Matrix widest = 

    if y_area[0] and y_area[0] > 0:
        y_max = y_area[1] + 1
    else:
        y_max = y_area[1] + 1
        # y area values negative

    if x_area[0] and x_area[0] > 0:
        x_max = x_area[1] + 1
    else:
        x_max = x_area[1] + 1
        # Matrix highest/lowest = 
        
    x_min = x_area[0]
    y_min = y_area[0]

    matrix = []
    # How much vertical space is needed?
    print(abs(y_max)) # 5 --> indexes 0 to 4
    # Behaviour for negatives:

# S . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . T T T
# . . . . . T T T
# . . . . . T T T
# . . . . . T T T

# . . . . . . . S
# . . . . . . . .
# . . . . . . . .
# T T T . . . . .
# T T T . . . . .
# T T T . . . . .
# T T T . . . . .

    for r in range(abs(y_max)):
        print('r: ', r)
        row = []
        for c in range(abs(x_max)):
            if r >= y_min and r <= y_max and c >= x_min and c <= x_max:
                # Target area
                row.append('T')
            elif r > 0 and c > 0 and r == 0 and c == 0:
                row.append('S')

            # Account for case where y is positive:
            else:
                row.append('.')
        matrix.append(row)


    return matrix

def print_matrix(file_name):
    # Matrix's leftmost column will have the probe start coord (0,0) if starting velocity x is positive
    # Negative x starting velocity means matrix's rightmost column will contain probe start coord somewhere




    return

def pp_matrix(matrix):
    for row in matrix:
        prettier_row = ' '.join(map(str, row))
        print(prettier_row)


def main():
    print('henlo')
    x_target_area, y_target_area = parse_input(TEST_INPUT_FILE)
    print('x_target_area, y_target_area: ', x_target_area, y_target_area)
    matrix = create_matrix(x_target_area, y_target_area)
    pp_matrix(matrix)
    return

if __name__ == '__main__':
    main()
