# Day 9 - Smoke Basin

INPUT_FILENAME = 'puzzle_input.txt'

class HeightMapAnalyzer():
    """
    Finds low points in heightmap, and uses them to:
    CalcPartOneSolution - calculate risk level using sum of each low point + 1
    CalcPartTwoSolution - recursively calculate basin size
    
    Additional helper functions calculate risk level and basin size to find the solution for parts 1 and 2.

    Class member variables:
    input_file (str)
    heightmap (list of list of ints)
    low_points (list of tuples (row, column))
    """

    def __init__(self, file_name):
        self.heightmap = self.CalcHeightmap(file_name)
        self.low_points = self.CalcLowPoints()

    def CalcHeightmap(self, file_name):
        heightmap = []

        with open(file_name) as file:
            for row in file:
                stripped_row = row.strip()
                row_lst = []
                for column_value in stripped_row:
                    row_lst.append(int(column_value))
                heightmap.append(row_lst)

        return heightmap

    # Public functions:        
    def CalcLowPoints(self):
        """
        Returns a list of coordinates of low points (tuples) from a heightmap matrix.
        """
        low_points = []
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
                    low_points.append((r, c))

        return low_points

    def CalcPartOneSolution(self):
        """
        Risk level is the sum of each (low point + 1).
        """
        risk_level_sum = 0

        for low_point in self.low_points:
            risk_level_sum += self.heightmap[low_point[0]][low_point[1]] + 1

        return risk_level_sum

    def CalcBasinSize(self, current_coord, visited_set=set()):
        """
        Starts with single pair (low point coords) as input, finding valid adjacent value coordinates based on recursive case criteria and returns basin size.
        Recursive case: valid adjacent value, within indexes of matrix, --> increments basin_size by one.
        Base case: adjacent value is a 9, or coordinate exists in basin_coords set.
        """

        valid_adjacent_coords = []
        visited_set.add(current_coord)
        basin_sum = 1

        coord_row, coord_col = current_coord
        adjacent_coordinates = [(coord_row-1, coord_col), (coord_row+1, coord_col), (coord_row, coord_col-1), (coord_row, coord_col+1)]
        row_length = self.heightmap[0]

        for coord_pair in adjacent_coordinates:
            if (0 <= coord_pair[0] < len(self.heightmap)
                    and 0 <= coord_pair[1] < len(row_length)
                    and self.heightmap[coord_pair[0]][coord_pair[1]] != 9): # Recursive case
                valid_adjacent_coords.append(coord_pair)

        for adj_coord in valid_adjacent_coords:
            if adj_coord not in visited_set:
                basin_sum += self.CalcBasinSize(adj_coord, visited_set)

        return basin_sum

    def CalcPartTwoSolution(self):
        """
        Calculates product of three largest basins (assumes there are at least 3 basins). 
        """
        visited_set = set()
        basin_size_list = []
        
        for low_point_coord in self.low_points:
            basin_size_list.append(self.CalcBasinSize(low_point_coord, visited_set))

        sorted_basin_size_list = sorted(basin_size_list)
        product_top_3_basin_sizes = sorted_basin_size_list[-3] * sorted_basin_size_list[-2] * sorted_basin_size_list[-1]

        return product_top_3_basin_sizes

def main():
    height_map_analyzer = HeightMapAnalyzer(INPUT_FILENAME)

    # # Part 1
    part_one_solution = height_map_analyzer.CalcPartOneSolution()
    print(f'Part 1 Solution: {part_one_solution}')

    # # Part 2
    part_two_solution = height_map_analyzer.CalcPartTwoSolution()
    print(f'Part 2 Solution: {part_two_solution}')
    
if __name__ == '__main__':
    main()
