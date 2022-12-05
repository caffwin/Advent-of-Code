# Day 5 - Hydrothermal Venture

TEST_OCEAN_FLOOR_SIZE = 10
ocean_floor_size_x = 0 # expected x = 9
ocean_floor_size_y = 0 # expected y = 7
coords_list = []

# generate_day5_test_input
with open('test_input.txt') as input_file:
    for line in input_file:
        first_coord, second_coord = line.strip().split(' -> ')
        # print('first_coord: **' + first_coord + '**')
        # print('second_coord: **' + second_coord + '**')
        first_coord_stripped = first_coord.strip()
        second_coord_stripped = second_coord.strip()

        # print('first_coord_stripped: **' + first_coord_stripped + '**')
        # print('second_coord_stripped: **' + second_coord_stripped + '**')
        first_x, first_y = first_coord.split(',')
        second_x, second_y = second_coord.split(',')
        # print('first_x: ***' + first_x + '***')
        # print('first_y: ***', first_y + '***') # extra space
        # print('second_x: ***', second_x + '***') # extra space
        # print('second_y: ***', second_y + '***') # extra space
        
        # Find which set of coords has upper bound
        max_x_value = max(int(first_x), int(second_x))
        max_y_value = max(int(first_y), int(second_y))

        if max_x_value > ocean_floor_size_x:
            ocean_floor_size_x = max_x_value 

        if max_y_value > ocean_floor_size_y:   
           ocean_floor_size_y = max_y_value 

        if first_x == second_x:
            upper_bound = max(first_y, second_y)
            lower_bound = min(first_y, second_y)
            # print('adding to corods list from: ', lower_bound, 'to: ', upper_bound)
            for i in range(int(lower_bound), int(upper_bound)+1):
                coords_list.append([str(i), first_x])

        if first_y == second_y:
            upper_bound = max(first_x, second_x)
            lower_bound = min(first_x, second_x)
            # print('adding to corods list from: ', lower_bound, 'to: ', upper_bound)
            for i in range(int(lower_bound), int(upper_bound)+1):
                coords_list.append([first_y, str(i)])
        

print('ocean_floor_size_x: ', ocean_floor_size_x)
print('ocean_floor_size_y: ', ocean_floor_size_y)

# For initial test case
# def generate_ocean_floor(size):
#     ocean_floor = []
#     for x in range(size):
#        ocean_floor.append('.' * size)

#     return ocean_floor

def generate_custom_ocean_floor(size_y, size_x):
    # y is number rows = 9
    # x is num cols = 7
    length = int(size_x) + 1
    width = int(size_y) + 1
    ocean_floor = []
    for row in range(width):
       ocean_floor.append('.' * length)

    ocean_floor_string = '\n'.join(ocean_floor)
    return ocean_floor

# def pp_grid(ocean_floor):
#     spaced_ocean_floor = []

#     for row in ocean_floor:
#         for el in row:
#             print(el + ' ')

#     return '\n'.join(spaced_ocean_floor)

def replace_char_at_index(string, character, index):
    # takes in string and replaces index with character
    index_int = int(index)
    string_as_list = list(string)
    string_as_list[index_int] = character
    new_str = ''.join(str(el) for el in string_as_list)
    return new_str

def plot_hydro_vents(ocean_floor_grid, coord_list):
    # Takes in grid and coordinates list, and marks horizontal and vertical
    # hydrothermal vent lines. Overlap is when the value of any index reaches 2.

    overlap_count = 0

    for coord in coord_list:
        x_value = int(coord[0])
        y_value = int(coord[1])
        row = ocean_floor_grid[x_value]

        if row[y_value] == '1':
            new_row = replace_char_at_index(row, '2', y_value)
            ocean_floor[x_value] = new_row
            overlap_count += 1

        if row[y_value] == '.':
            new_row = replace_char_at_index(row, '1', y_value)
            ocean_floor[x_value] = new_row

    print('\n'.join(ocean_floor_grid))
    return overlap_count

ocean_floor = generate_custom_ocean_floor(ocean_floor_size_y, ocean_floor_size_x)
print('Plotting hydrothermal vents... ', plot_hydro_vents(ocean_floor, coords_list))
# 5304 too low