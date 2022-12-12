TEST_INPUT = "test_input.txt"
TREE_HEIGHTMAP = [] # 0 shortest, 9 tallest

with open(TEST_INPUT) as file:
    for line in file:
        tree_height = []
        stripped_line = line.strip()
        for num in stripped_line:
            tree_height.append(int(num))
        TREE_HEIGHTMAP.append(tree_height)


def determine_directional_visibility(lst_surrounding_coords, curr_tree_coords, direction):
    """
        Checks a single surrounding coord, either in the north, west, east or south direction.
        Returns False if the tree in that direction is taller than the current tree, else True.
    """
    is_visible = True

    for tree_coord in lst_surrounding_coords:
        if TREE_HEIGHTMAP[tree_coord[0]][tree_coord[1]] >= TREE_HEIGHTMAP[curr_tree_coords[0]][curr_tree_coords[1]]:
            is_visible = False

    return is_visible

def determine_tree_visibility(row, col):
    """
        Takes in a row and column value and checks all coordinates east, west, north and south of those in the heightmap.

        Returns True if either of those flags are True, else False.
    """
    
    heightmap_height = len(TREE_HEIGHTMAP)
    heightmap_width = len(TREE_HEIGHTMAP[0])
    curr_coord = (row, col)
    
    east_coords = []
    west_coords = []
    north_coords = []
    south_coords = []

    # Populate valid east coords
    for i in range(heightmap_width - (col + 1)):
        coord = (row, heightmap_width - i - 1)
        east_coords.append(coord)

    # Populate valid west coords
    for i in range(col):
        coord = (row, i)
        west_coords.append(coord)

    # Populate valid north coords
    for i in range(row):
        coord = (i, col)
        north_coords.append(coord)    

    # Populate valid south coords
    for i in range(heightmap_height - (row + 1)):
        coord = (heightmap_height - i - 1, col)
        south_coords.append(coord)

    if determine_directional_visibility(east_coords, curr_coord) or determine_directional_visibility(west_coords, curr_coord) or determine_directional_visibility(north_coords, curr_coord) or determine_directional_visibility(south_coords, curr_coord):
        return True

    else:
        return False

def p1_solution(heightmap):
    total_visible_trees = 0
    heightmap_height = len(heightmap)
    heightmap_width = len(heightmap[0])
    for r in range(heightmap_height):
        row = heightmap[r]
        for c in range(heightmap_width):
            is_visible_tree = determine_tree_visibility(r, c)
            if is_visible_tree:
                total_visible_trees += 1

    return total_visible_trees


def run():
    p1_solution = p1_solution(TREE_HEIGHTMAP)
    print('part one solution: ', p1_solution)
    return

if __name__ == "__main__":
    run()