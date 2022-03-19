# Create a 99 x 99 square and troubleshoot why second test case fails

# test_file = open("test_case_test.txt", "w+")

ocean_floor_size_x = 0 # expected x = 9
ocean_floor_size_y = 0 # expected y = 7
coords_list = []


# Base coordinate for 99 x 99 grid: 0,99 -> 99,99
# def generate_test_input(size):
#     # Start at x,0 -> x,99

#     for x in range(size): # length is x 
#         test_file.writelines(str(x) + ",0 -> " + str(x) + ",99\n")
#     # Horizontal
#     # 0,0 -> 0,99
#     # 1,0 -> 1,99
#     # 2,0 -> 2,99

#     for y in range(size): # width is y
#         test_file.writelines("0," + str(y) + " -> 99," + str(y) + "\n")
    
    # Vertical
    # 0,0 -> 99,0
    # 0,1 -> 99,1
    # 0,2 -> 99,2

# generate_test_input(100)

with open('test_case_test.txt') as input_file:
    for line in input_file:
        first_coord, second_coord = line.strip().split(' -> ')
        first_coord_stripped = first_coord.strip()
        second_coord_stripped = second_coord.strip()

        first_x, first_y = first_coord.split(',')
        second_x, second_y = second_coord.split(',')
        
        max_x_value = max(int(first_x), int(second_x))
        max_y_value = max(int(first_y), int(second_y))

        if max_x_value > ocean_floor_size_x:
            ocean_floor_size_x = max_x_value 

        if max_y_value > ocean_floor_size_y:   
           ocean_floor_size_y = max_y_value 

        if first_x == second_x:
            upper_bound = max(first_y, second_y)
            lower_bound = min(first_y, second_y)
            for i in range(int(lower_bound), int(upper_bound)+1):
                coords_list.append([str(i), first_x])

        if first_y == second_y:
            upper_bound = max(first_x, second_x)
            lower_bound = min(first_x, second_x)
            for i in range(int(lower_bound), int(upper_bound)+1):
                coords_list.append([first_y, str(i)])


def generate_custom_ocean_floor(size_y, size_x):
    length = int(size_x) + 1
    width = int(size_y) + 1
    ocean_floor = []
    ocean_floor_total_units = 0
    for row in range(width):
       ocean_floor.append('.' * length)
       ocean_floor_total_units += length

    ocean_floor_string = '\n'.join(ocean_floor)
    print('total units in ocean floor: ', ocean_floor_total_units)
    return ocean_floor
    # return ocean_floor_string

# print('generate_custom_ocean_floor size: ', generate_custom_ocean_floor(ocean_floor_size_y, ocean_floor_size_x))
ocean_floor = generate_custom_ocean_floor(ocean_floor_size_y, ocean_floor_size_x)

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

# print(coords_list)

print("Plotting vents, overlapping count: ", plot_hydro_vents(ocean_floor, coords_list))


# 0,9 -> 5,9 # y value = number of rows
# 7,0 -> 7,4 # x value = number of columns (chars per row)

# Create a test board 100 x 100

# 0,99 -> 99,99
# 99,0 -> 99,99