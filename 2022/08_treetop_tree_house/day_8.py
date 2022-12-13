TEST_INPUT = "test_input.txt"
TREE_HEIGHTMAP = [] # 0 shortest, 9 tallest

with open(TEST_INPUT) as file:
    for line in file:
        tree_height = []
        stripped_line = line.strip()
        for num in stripped_line:
            tree_height.append(int(num))
        TREE_HEIGHTMAP.append(tree_height)


def determine_directional_visibility(lst_surrounding_coords, curr_tree_coords):
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


########################### P2 ###########################

def determine_directional_scenic_score(lst_surrounding_coords, curr_tree_coords, direction):
    """
        Totals the number of trees shorter than the tree from the heightmap at coordinate (row, col) for a given direction (str), 
        and returns a scenic score.
    """
    # print("***** coords are: ", curr_tree_coords)
    scenic_score = 0
    sorted_list = sorted(lst_surrounding_coords , key=lambda k: [k[1], k[0]])
    # print('lst surrounding coords: ', sorted_list)
    for tree_coord in sorted_list: # Checking through each tree
        # print('checking coord: ', str(tree_coord))
        if TREE_HEIGHTMAP[tree_coord[0]][tree_coord[1]] >= TREE_HEIGHTMAP[curr_tree_coords[0]][curr_tree_coords[1]]: # If the tree in the ordered list is taller
            # Calculate the number of spaces away it is
            # Find which coord is the 
            if tree_coord[0] == curr_tree_coords[0]:
                diff_spaces = abs(tree_coord[1] - curr_tree_coords[1])
                # print("Taller tree found at a difference of: ", diff_spaces, "in the ", direction, "direction!")
                return diff_spaces
            else:
                diff_spaces = abs(tree_coord[0] - curr_tree_coords[0])
                # print("Taller tree found at a difference of: ", diff_spaces, "in the ", direction, "direction!")
                return diff_spaces
        # else:
        #     print("The tree at coords: ", str(tree_coord), " is shorter than the current tree, keep looping")
    if scenic_score == 0: # If it's still 0 after checking (fully visible in a given direction), return the length of the list (all trees in that direction)
        # Empty list
        # print("No trees blocking!! Number of trees we are seeing over: ", str(len(lst_surrounding_coords)))
        return len(lst_surrounding_coords)
    return scenic_score


def calc_tree_scenic_score(row, col):
    """
        Takes in a row (int) and column (int) value and checks all trees east, west, north and south of that coordinate in the heightmap.

        For each direction,  multiplies those to return a tree_scenic_score (int) for a given tree.
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

    east_scenic_score = determine_directional_scenic_score(east_coords, curr_coord, "east")
    west_scenic_score = determine_directional_scenic_score(west_coords, curr_coord, "west")
    north_scenic_score = determine_directional_scenic_score(north_coords, curr_coord, "north")
    south_scenic_score = determine_directional_scenic_score(south_coords, curr_coord, "south")

    # print("east_scenic_score: ", east_scenic_score)
    # print("west_scenic_score: ", west_scenic_score)
    # print("north_scenic_score: ", north_scenic_score)
    # print("south_scenic_score: ", south_scenic_score)

    return int(east_scenic_score * west_scenic_score * north_scenic_score * south_scenic_score)

def calc_total_visible_trees(heightmap):
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


def calc_heightmap_scenic_score(heightmap):
    # Calculate a tree's scenic score by multiplying the number of trees in each NSWE directions that are shorter than that tree
    highest_scenic_score = 0
    heightmap_height = len(heightmap)
    heightmap_width = len(heightmap[0])
    for r in range(heightmap_height):
        # row = heightmap[r]
        for c in range(heightmap_width):
            scenic_score = calc_tree_scenic_score(r, c)
            # print("scenic score for: ", r, ",", c, "is: ", str(scenic_score))
            if scenic_score > highest_scenic_score:
                # print("Current scenic score ", str(scenic_score), "is higher than current record holder: ", str(highest_scenic_score))
                highest_scenic_score = scenic_score
    return highest_scenic_score

def run():
    p1_solution = calc_total_visible_trees(TREE_HEIGHTMAP)
    print("part one solution: ", p1_solution)

    p2_solution = calc_heightmap_scenic_score(TREE_HEIGHTMAP)
    print("part two solution: ", p2_solution)
    return

if __name__ == "__main__":
    run()

# 5025102114 too high
# 2867088 too high!
# 2565 too low!