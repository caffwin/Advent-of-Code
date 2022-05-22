# Day 11 - Dumbo Octopus



# "Flash" occurs when value is 0

CAVE_MATRIX = []
with open('test_input.txt') as file:
    for row in file:
        stripped_row = row.strip()
        row_lst = []
        for column_value in stripped_row:
            row_lst.append(int(column_value))
        CAVE_MATRIX.append(row_lst)

# print(HEIGHTMAP)

def pretty_print_heightmap(heightmap):
    for row in heightmap:
        print(row)

print(pretty_print_heightmap(CAVE_MATRIX))

# Class implementation takes in file name and outputs two solutions

def part_one_solution(cave_matrix, step_count):
    # Heightmap: a list of list of ints
    # step_count: an int

    cave_width = len(cave_matrix[0])
    cave_height = len(cave_matrix)

    # Each step:
    # Ensure we're within the confines of the matrix row & column constraints

    # Increase octopus increases by 1
    # If energy level is 9, increase all surrounding values, capping at 0 "max"
    # If energy level is 0, 
    # An octopus can flash once per step max
    # for i in range(step_count):
    for r in range(cave_height):
        for c in range(cave_width):
            if cave_matrix[r][c] == 9 or cave_matrix[r][c] == 0:
                cave_matrix[r][c] = 0
                surrounding_coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
                increment_coords = []

                for coord_pair in surrounding_coords:
                    if 0 <= coord_pair[0] < len(cave_matrix) and 0 <= coord_pair[1] < len(row):
                    # Filter coords to be within matrix dimensions
                        increment_coords.append(coord_pair)
                print('increment_coords: ', increment_coords)

                for coord in increment_coords:
                    if cave_matrix[coord[0]][coord[1]] == 9:
                        cave_matrix[coord[0]][coord[1]] = 0
                    elif cave_matrix[coord[0]][coord[1]] > 0:
                        cave_matrix[coord[0]][coord[1]] += 1
                    else:               
                        print('zZzz')

            else:
                if cave_matrix[r][c] == 9:
                    cave_matrix[r][c] = 0
                else:
                    cave_matrix[r][c] += 1
            # if 

        print(cave_matrix[r])

    return

print(part_one_solution(CAVE_MATRIX, 1))


# 11111
# 19991
# 19191
# 19991
# 11111