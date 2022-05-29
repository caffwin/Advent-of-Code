# Day 11 - Dumbo Octopus



# "Flash" occurs when value is 0

CAVE_MATRIX = []
with open('puzzle_input.txt') as file:
    for row in file:
        stripped_row = row.strip()
        row_lst = []
        for column_value in stripped_row:
            row_lst.append(int(column_value))
        CAVE_MATRIX.append(row_lst)

def pretty_print_matrix(matrix):
    print('\npretty printing rows in matrix')
    for row in matrix:
        print(row)
    return ''

# print(pretty_print_matrix(CAVE_MATRIX))
# Class implementation takes in file name and outputs two solutions

def part_one_solution(cave_matrix, step_count):
    # Heightmap: a list of list of ints
    # step_count: an int

    cave_width = len(cave_matrix[0])
    cave_height = len(cave_matrix)
    total_flashes = 0
    # tmp_matrix = cave_matrix
    temp_matrix = cave_matrix
 
    # Each step:
    # Ensure we're within the confines of the matrix row & column constraints

    # Increase octopus increases by 1
    # If energy level is 9, increase all surrounding values, capping at 0 "max"
    # If energy level becomes 0 for whatever reason, 
    # An octopus can flash once per step max

    for i in range(step_count):
        print('\n \nstarting run through: ', str(i + 1))
        # A list of tuples, the coordinates of 0s that have been incremented from 9 -> 0 within this run through
        will_flash_coords = set() # A list of coordinates of zero values that still need to execute flash logic during this step
        has_flashed_coords = set()
        # Problem: values are incrementing but not being updated..
        # Next row is still working with original values of previous row
        for r in range(cave_height):
            # print('r value: ', cave_width)
            # print('row: ', str(r))
            # print('starting row: ', str(cave_matrix[r]))
            for c in range(cave_width):
                # print('\ncurrent coord: ', str(r) + ',' + str(c))
                # pretty_print_matrix(cave_matrix)
                # pretty_print_matrix(temp_matrix)
                energy_level = cave_matrix[r][c]
                # if energy_level > 0 and energy_level < 9:
                #     print('number is not 9 or 0 -- it is:', energy_level)
                #     energy_level += 1
                if energy_level == 9:
                    energy_level = 0
                    # print('Energy level is 9 and has been reset to 0 -- executing flash behavior')
                    has_flashed_coords.add((r, c))
                    total_flashes += 1 # Increment when 9 -> 0 on its own
                    
                    surrounding_coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
                    increment_coords = []
                    # print('test: ', str(cave_matrix[r-1][c]))
                    for coord_pair in surrounding_coords:
                        if 0 <= coord_pair[0] < len(cave_matrix) and 0 <= coord_pair[1] < cave_width:
                        # Filter coords to be within matrix dimensions
                            increment_coords.append(coord_pair)
                    # print('#($&*@#(*&$increment_coords: ', increment_coords)
                    # print('surrounding coords: ')
                    for coord in increment_coords:
                        print(cave_matrix)
                        # print('*******errors out here... this is the row: ', cave_matrix[r])
                        
                        if cave_matrix[coord[0]][coord[1]] == 9:
                            
                            cave_matrix[coord[0]][coord[1]] = 0
                            # total_flashes += 1
                            # print('*************flashing at coord after turning from 9 -> 0 at coord: ', str(coord), '... incrementing flash count')
                            # Increment when value increases from 9 -> 0 after incremented through a neighbouring flash
                            # print('this coordinate has been capped at 0 -- adding to will_flash_coords: ', coord)
                            will_flash_coords.add(coord)
                        # Included behaviour to only flash 0s that should still be incremented
                        elif cave_matrix[coord[0]][coord[1]] == 0 and coord not in will_flash_coords:
                            cave_matrix[coord[0]][coord[1]] += 1
                        elif cave_matrix[coord[0]][coord[1]] > 0: #
                            # print('^incrementing surrounding coord from flash - ', coord)
                            # print('^value before: ', str(cave_matrix[coord[0]][coord[1]]), ' value after: ', str(cave_matrix[coord[0]][coord[1]] + 1))
                            cave_matrix[coord[0]][coord[1]] += 1
                        # elif cave_matrix[coord[0]][coord[1]] == 9: #
                        #     print('^incrementing surrounding coord from flash - ', coord)
                        #     print('^value before: ', str(cave_matrix[coord[0]][coord[1]]), ' value after: ', str(cave_matrix[coord[0]][coord[1]] + 1))
                        #     cave_matrix[coord[0]][coord[1]] += 1
                        #     total_flashes =+ 1
                        else:
                            print('^Trying to increment a 0, but capped -- coord is: ', coord)
                    # temp_matrix[r] = cave_matrix[r]


                # Account for case where a number is turned from 9 -> 0 from a flash after it has already incremented itself



                # Duplicate coords added to will_flash_coords but it's ok since it's a set

                # How do you know if a 0 needs to be incremented or was just capped?
                # Keep track of 

                # The problem is when the next value == 0 with no way of knowing if it should increment on its own (0 at start of step)
                # or if it should execute flash behaviour from being incremented through neighboring flash

                # Not sure if the 1 in the middle is being incremented

                # 9 in (2, 1) is being incremented when it should not be
                # Check behaviour in has_flashed list...

                # Logic for coords that have become a 0 from 
                # Ignores self-increment as values cap at 0
                elif energy_level == 0 and (r, c) in will_flash_coords:
                    # print('\n')
                    # print('value is 0 and in the will_flash_coords, flashing')
                    total_flashes += 1 # Increment when 9 -> 0 on its own
                    surrounding_coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
                    increment_coords = []
                    
                    for coord_pair in surrounding_coords:
                        if 0 <= coord_pair[0] < len(cave_matrix) and 0 <= coord_pair[1] < cave_width:
                        # Filter coords to be within matrix dimensions
                            increment_coords.append(coord_pair)
                    # print('increment_coords: ', increment_coords)

                    for coord in increment_coords:
                        if cave_matrix[coord[0]][coord[1]] == 9:
                            cave_matrix[coord[0]][coord[1]] = 0
                            # total_flashes += 1
                            # Increment when value increases from 9 -> 0 after incremented through a neighbouring flash
                            print('this coordinate has been capped at 0 -- adding to will_flash_coords: ', coord)
                            will_flash_coords.add(coord)
                        # Included behaviour to only flash 0s that should still be incremented
                        elif cave_matrix[coord[0]][coord[1]] == 0 and coord not in will_flash_coords:
                            cave_matrix[coord[0]][coord[1]] += 1
                        elif cave_matrix[coord[0]][coord[1]] > 0:
                            # print('*incrementing surrounding coord from flash - ', coord)
                            # print('*value before: ', str(cave_matrix[coord[0]][coord[1]]), ' value after: ', str(cave_matrix[coord[0]][coord[1]] + 1))
                            cave_matrix[coord[0]][coord[1]] += 1
                        else:
                            print('*Trying to increment a 0, but capped -- coord is: ', coord)
                    # temp_matrix[r] = cave_matrix[r]

                else: # 
                    # print('number is not 9 or 0 -- it is:', energy_level)
                    cave_matrix[r][c] += 1
                    # print('incrementing -- now a', energy_level)

                # print('&&&&finishing after step: ', str(cave_matrix[r]))
            if len(will_flash_coords) > 0:
                print('**** the following coordinates have flashed: ', will_flash_coords)

        
            # print('finishing row: ', str(cave_matrix[r]))
            # temp_matrix.append(cave_matrix[r])
            # print('*** total flashes inside loop: ', total_flashes)
            pp_matrix = pretty_print_matrix(temp_matrix) # prints a bunch of lines but returns empty str
            # # print('pp matrix: ', pp_matrix)
            # 
        total_flashes += len(has_flashed_coords)
        print('*** total flashes: ', total_flashes)
    return ''


# print(part_one_solution(CAVE_MATRIX, 1))
# print(part_one_solution(CAVE_MATRIX, 100))


print(part_one_solution(CAVE_MATRIX, 10))

# print(part_one_solution(CAVE_MATRIX, 100))
# 2880 --> too high


# [[0, 0, 6, 0, 0, 0, 0, 0, 3, 7], 
# [7, 5, 6, 0, 0, 0, 0, 5, 6, 9], 
# [9, 2, 0, 5, 0, 9, 5, 0, 7, 3], 
# [5, 7, 6, 6, 4, 8, 2, 5, 9, 4], 
# [4, 9, 7, 5, 6, 6, 2, 4, 7, 6], 
# [2, 9, 8, 9, 3, 6, 4, 6, 9, 2], 
# [9, 4, 2, 8, 5, 3, 3, 5, 4, 8], 
# [2, 6, 2, 8, 3, 6, 5, 3, 7, 7], 
# [3, 7, 3, 2, 2, 3, 5, 8, 7, 2], 
# [4, 5, 8, 4, 4, 4, 2, 6, 2, 5]]