
# Smoke Basin

HEIGHTMAP = []

with open('puzzle_input.txt') as file:
    for row in file:
        # print('**' + row + '**')
        stripped_row = row.strip()
        row_lst = []
        for column_value in stripped_row:
            row_lst.append(column_value)
        HEIGHTMAP.append(row_lst)


def calc_risk_level(low_point_list):
    """
    Risk level is the sum of each low points + 1
    """
    risk_level_sum = len(low_point_list)

    for low_point in low_point_list:
        risk_level_sum += low_point

    return risk_level_sum


def pp_matrix(heightmap):
    'pretty printing HEIGHTMAP: \n'

    for row in heightmap:
        print(str(row) + '\n')
    
print(pp_matrix(HEIGHTMAP))

# Main run function: takes in a list of lists (matrix of heightmap) 
# Iterate through each element in each row and check if adjacent coordinates are within bounds of grid
# If coordinate is "valid", access that element in the heightmap and append it to a list, "lowest_points"

def calc_sum_risk_level(heightmap_matrix):
    low_point_value_list = []

    for r in range(len(heightmap_matrix)):
        row = heightmap_matrix[r]

        for c in range(len(row)):
            col_value = row[c]
            adjacent_coordinate_values = []
            adjacent_coordinates = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            
            valid_adjacent_coords = []

            for coord_pair in adjacent_coordinates:
                if 0 <= coord_pair[0] < len(heightmap_matrix) and 0 <= coord_pair[1] < len(row):
                    valid_adjacent_coords.append(coord_pair)
                    adjacent_coordinate_values.append(HEIGHTMAP[coord_pair[0]][coord_pair[1]])
                else:
                    print('coord pair filtered out: ', coord_pair)
                  
            num_valid_coords = 0

            for pair in valid_adjacent_coords:
                if col_value < heightmap_matrix[pair[0]][pair[1]]:
                    num_valid_coords += 1

            if num_valid_coords == len(valid_adjacent_coords):
                low_point_value_list.append(int(col_value))

    risk_level = calc_risk_level(low_point_value_list)

    return risk_level

print(calc_sum_risk_level(HEIGHTMAP))


# Expected low points: 1, 0, 5, 5
# Expected nums to sum: 2, 1, 6, 6
# Expected risk level: 15
