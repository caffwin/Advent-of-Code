TEST_INPUT = "test_input.txt"

DIRECTION_DICT = {
    "L": ,
    "D": ,
    "U": ,
    "R":
}
def parse_input():
    with open(TEST_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            print('stripped line: ', stripped_line)

# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2

def p1_solution():
    # Starts at (0,0)
    # Don't even need to build a matrix, just increment/decrement coords 

    # Whenever the tail changes coordinates, advance the counter 
    num_spaces_moved_tail = 0

    start_coord_head = (0, 0) # tuple of ints
    start_coord_tail = (0, 0) # Same starting position

    return

def run():

    result = parse_input()
    print(result)

    return

if __name__ == "__main__":
    run()