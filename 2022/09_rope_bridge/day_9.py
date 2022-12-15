from locale import currency


TEST_INPUT = "test_input.txt"
INSTRUCTION_LIST = []

# (x, y)
DIRECTION_DICT = {
    "L": (-1, 0), # -x
    "D": (0, -1), # -y
    "U": (0, 1), # +y
    "R": (1, 0) # +x
}

def parse_input():
    with open(TEST_INPUT) as file:
        for line in file:
            stripped_line = line.strip()
            print('stripped line: ', stripped_line)
            direction, value = stripped_line.split(" ")
            INSTRUCTION_LIST.append((direction, int(value)))

def p1_solution():
    num_spaces_moved_tail = 0
    unique_coords_tail = set()

    start_coord_head = (0, 0) # tuple of ints
    start_coord_tail = (0, 0) # Same starting position
    curr_head_coord = start_coord_head # (0, 0) # (x, y)
    prev_head_coord = None
    curr_tail_coord = start_coord_tail
    print("Current coord starts at: ", curr_head_coord)
    for instruction in INSTRUCTION_LIST: #('R', 4)
        print("**** New instruction is: ", instruction)
        for i in range(instruction[1]): # 4 times for above example
            ###### Head ######
            transformed_coord = tuple([sum(tup) for tup in zip(curr_head_coord, DIRECTION_DICT[instruction[0]])]) # instruction[0] is a single character string indicating the direction
            prev_head_coord = curr_head_coord
            curr_head_coord = transformed_coord
            print("Head coord moving to ---->: ", transformed_coord)

            ###### Tail ######
            print("**** Tails' turn!")
            print("current tail coord: ", curr_tail_coord)

            diff_x = (abs(curr_tail_coord[0] - curr_head_coord[0]))
            diff_y = (abs(curr_tail_coord[1] - curr_head_coord[1]))


            if diff_x == 1 and diff_y > 1 or diff_x > 1 and diff_y == 1:
                print("/////////Need to move the snake diagonally")
                print("previous head coord is (tail should be moving here): ", prev_head_coord)
                curr_tail_coord = prev_head_coord
                unique_coords_tail.add(curr_tail_coord)
                num_spaces_moved_tail += 1

            if diff_x > 1:
                print("x value differs by ", str(diff_x))
                for i in range(diff_x-1):
                    if max(curr_head_coord[0], curr_tail_coord[0]) == curr_tail_coord[0]: # Tail is larger, move tail to the left
                        # Move the tail left
                        print("Tail x value is greater than head x value, moving to the left of: ", curr_tail_coord)
                        curr_tail_coord = tuple([sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["L"])]) # increment on x axis, so left
                        print("New tail value -- moving to ---->: ", curr_tail_coord)
                        num_spaces_moved_tail += 1
                        unique_coords_tail.add(curr_tail_coord)
                        
                    else: # Head is larger, move tail to the right
                        # Move the tail right
                        print("Tail x value is less than head x value, moving to the right of: ", curr_tail_coord)
                        curr_tail_coord = tuple([sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["R"])])
                        print("New tail value -- moving to ---->: ", curr_tail_coord)
                        num_spaces_moved_tail += 1
                        unique_coords_tail.add(curr_tail_coord)
                        # curr_tail_coord[0] += 1
            if diff_y > 1:
                print("y value differs by ", str(diff_y))
                for i in range(diff_y-1):
                    if max(curr_head_coord[1], curr_tail_coord[1]) == curr_tail_coord[1]:
                        print("Tail y value is greater than head y value, moving down from: ", curr_tail_coord)
                        curr_tail_coord = tuple([sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["D"])])
                        print("New tail value -- moving to ---->", curr_tail_coord)
                        num_spaces_moved_tail += 1
                        unique_coords_tail.add(curr_tail_coord)
                        # curr_tail_coord[1] -= 1 # increment the tail
                    else:
                        print("Tail y value is greater than head y value, moving up from: ", curr_tail_coord)
                        curr_tail_coord = tuple([sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["U"])])
                        print("New tail value -- moving to ---->", curr_tail_coord)
                        num_spaces_moved_tail += 1
                        unique_coords_tail.add(curr_tail_coord)

    print("unique_coords_tail: ", unique_coords_tail)
    return num_spaces_moved_tail

def run():
    result = parse_input()
    print(INSTRUCTION_LIST)
    print(result)
    part_one_solution = p1_solution()
    print("part one solution: ", part_one_solution)
    return

if __name__ == "__main__":
    run()

# 9307 Too high