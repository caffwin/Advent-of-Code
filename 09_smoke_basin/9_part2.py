# Smoke Basin Part 2

TEST_INPUT_FILE = 'puzzle_input.txt'

class Parser():
    """
        Parses input into a heightmap
        Class attributes:
        input_file (str)
        heightmap (list of lists)
    """

    def __init__(self, input_file, heightmap=None):
        self.input_file = input_file
        self.heightmap = heightmap

    def heightmap(self):
        return self.heightmap

    """
        Helper functions:
    """

    def parse_input_file(self):
        """
        Takes in an input file as a string and produces a heightmap matrix (list of lists) and
        assigns to self.heightmap
        """

        self.heightmap = []
        with open(self.input_file) as file:
            for row in file:
                stripped_row = row.strip()
                row_lst = []
                for column_value in stripped_row:
                    row_lst.append(int(column_value))
                self.heightmap.append(row_lst)

        
    def find_low_point_coords(self):
        """
        Returns a list of coordinates of low points (tuples) from a heightmap matrix.
        """
        low_point_coords = []

        for r in range(len(self.heightmap)):
            row = self.heightmap[r]
            for c in range(len(row)):
                col_value = row[c]
                adjacent_coordinate_values = []
                adjacent_coordinates = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                
                valid_adjacent_coords = []

                for coord_pair in adjacent_coordinates:
                    if 0 <= coord_pair[0] < len(self.heightmap) and 0 <= coord_pair[1] < len(row):
                        valid_adjacent_coords.append(coord_pair)
                        adjacent_coordinate_values.append(self.heightmap[coord_pair[0]][coord_pair[1]])
                    
                num_valid_coords = 0

                for pair in valid_adjacent_coords:
                    if col_value < self.heightmap[pair[0]][pair[1]]:
                        num_valid_coords += 1

                if num_valid_coords == len(valid_adjacent_coords):
                    low_point_coords.append((r, c))
            
        return low_point_coords


def calc_basin_size_recursive(heightmap_matrix, current_coord, visited_set):
    # Starts with single pair (low point coords) as input and returns [sum of basin size]
    # Finds valid adjacent value coordinates
     
    # Recursive case: valid adjacent value, within indexes of matrix, --> increments basin_size by one
    # Base case: adjacent value is a 9, or coordinate exists in basin_coords set

    valid_adjacent_coords = []
    print()
    visited_set.add(current_coord)
    basin_sum = 1

    coord_row, coord_col = current_coord
    adjacent_coordinates = [(coord_row-1, coord_col), (coord_row+1, coord_col), (coord_row, coord_col-1), (coord_row, coord_col+1)]
    row_length = heightmap_matrix[0]

    for coord_pair in adjacent_coordinates:
        if (0 <= coord_pair[0] < len(heightmap_matrix)
                and 0 <= coord_pair[1] < len(row_length)
                and heightmap_matrix[coord_pair[0]][coord_pair[1]] != 9): # Recursive case
            valid_adjacent_coords.append(coord_pair)

    for adj_coord in valid_adjacent_coords:
        if adj_coord not in visited_set:
            basin_sum += calc_basin_size_recursive(heightmap_matrix, adj_coord, visited_set)

    return basin_sum

def calc_product_basin_size():
    visited_set = set()
    parser = Parser(TEST_INPUT_FILE)
    parser.parse_input_file()
    low_point_coords = parser.find_low_point_coords()

    basin_size_list = []

    for low_point_coord in low_point_coords:
        basin_size_list.append(calc_basin_size_recursive(parser.heightmap, low_point_coord, visited_set))

    sorted_basin_size_list = sorted(basin_size_list)
    sum_basin_sizes = sorted_basin_size_list[-1] * sorted_basin_size_list[-2] * sorted_basin_size_list[-3]

    return sum_basin_sizes

def main():
    print(calc_product_basin_size())

if __name__ == "__main__":
    main()
