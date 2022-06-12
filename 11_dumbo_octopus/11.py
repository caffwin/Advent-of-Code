# Day 11 - Dumbo Octopus

INPUT_FILE = 'puzzle_input.txt'
NUM_STEPS = 100
# NUM_STEPS_SYNC = 999 # For part 2 solution

def build_cave_matrix(input_file):
    cave_matrix = []
    with open(input_file) as file:
        for row in file:
            stripped_row = row.strip()
            row_lst = []
            for column_value in stripped_row:
                row_lst.append(int(column_value))
            cave_matrix.append(row_lst)

    return cave_matrix

def part_one_solution(cave_matrix, step_count):
    total_flashes = 0
    cave_width = len(cave_matrix[0])
    cave_height = len(cave_matrix)
    temp_matrix = cave_matrix #
    max_flashes_triggered = False

    for i in range(step_count):
        flash_count_by_step = 0
        will_flash_coords_list = [] # A list of tuples containin coordinates that need to execute flash logic during this step
        rolled_over_coords = [] # A list of coordinates that have already flashed and cannot be incremented (remains at 0 until end of step)
        for r in range(cave_height):
            for c in range(cave_width):
                energy_level = temp_matrix[r][c]
                if energy_level == 9:
                    temp_matrix[r][c] = 0
                    flash_count_by_step += 1
                    coord = (r, c)
                    rolled_over_coords.append(coord)
                    will_flash_coords_list.append(coord)
                else:
                    temp_matrix[r][c] += 1

        while len(will_flash_coords_list) > 0: # Check if this works
            flashing_coord = will_flash_coords_list[-1]
            will_flash_coords_list.pop()
            r = flashing_coord[0]
            c = flashing_coord[1]

            adj_coords = [(r-1, c), (r+1, c), (r, c -1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
            valid_adj_coords = []
            

            for coord in adj_coords:
                if 0 <= coord[0] < cave_height and 0 <= coord[1] < cave_width: # between 0 and 2 for each
                    valid_adj_coords.append(coord)

            for coord in valid_adj_coords:
                if temp_matrix[coord[0]][coord[1]] == 9:
                    temp_matrix[coord[0]][coord[1]] = 0
                    rolled_over_coords.append(coord)
                    will_flash_coords_list.append(coord)
                    flash_count_by_step += 1
                elif coord not in rolled_over_coords: # Any other value that hasn't flashed, increment by 1
                    temp_matrix[coord[0]][coord[1]] += 1
                
        max_flashes = cave_height * cave_width

        if flash_count_by_step == max_flashes and max_flashes_triggered == False:
            max_flashes_triggered = True
            print('Sync happens on step: ', str(i + 1))

        total_flashes += flash_count_by_step

    return total_flashes

def main():
    cave_matrix = build_cave_matrix(INPUT_FILE)
    result = part_one_solution(cave_matrix, NUM_STEPS)
    print('Part 1 solution -- total flashes: ', result)

if __name__ == "__main__":
    main()