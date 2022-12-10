TEST_INPUT = "test_input.txt"
TREE_HEIGHTMAP = [] # 0 shortest, 9 tallest.

with open(TEST_INPUT) as file:
    for line in file:
        tree_height = []
        stripped_line = line.strip()
        for num in stripped_line:
            tree_height.append(int(num))
        TREE_HEIGHTMAP.append(tree_height
)

def calc_valid_coords(row, col):
    heightmap_height = len(TREE_HEIGHTMAP)
    heightmap_width = len(TREE_HEIGHTMAP[0])

    coord = (row, col) # tuple of current coord, ex. (3, 2)

    east_coords = []
    west_coords = []
    north_coords = []
    south_coords = []

    # Populate valid east coords
    for i in range(heightmap_width - (col + 1)): # 11 - 8 = 3, producing i as: 0, 1, 2
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

    return 

def p1_solution(heightmap):
    heightmap_height = len(heightmap)
    heightmap_width = len(heightmap[0])
    for r in range(heightmap_height):
        row = heightmap[r]
        for c in range(heightmap_width):
            # tree_height = row[c]
            col_value = int(row[c])
            print('current coord is ************* : ', col_value)
            print('passing coords into function: ', r, c)
            calc_valid_coords(r, c)

    return


def run():
    print(TREE_HEIGHTMAP)
    result = p1_solution(TREE_HEIGHTMAP)
    print('result: ', result)
    return

if __name__ == "__main__":
    run()