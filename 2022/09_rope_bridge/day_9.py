TEST_INPUT = "test_input.txt"
INSTRUCTION_LIST = []

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
            direction, value = stripped_line.split(" ")
            INSTRUCTION_LIST.append((direction, int(value)))

def p1_solution():
    num_spaces_moved_tail = 0
    start_coord_head = (0, 0) # tuple of ints
    start_coord_tail = (0, 0) # Same starting position
    curr_head_coord = start_coord_head # (0, 0) # (x, y)
    curr_tail_coord = start_coord_tail

    for instruction in INSTRUCTION_LIST:
        for i in range(instruction[1]):
            transformed_coord = [sum(tup) for tup in zip(curr_head_coord, DIRECTION_DICT[instruction[0]])] # instruction[0] is a single character string indicating the direction
            curr_head_coord = transformed_coord

            diff_x = (abs(curr_tail_coord[0] - curr_head_coord[0]))
            diff_y = (abs(curr_tail_coord[1] - curr_head_coord[1]))

            if diff_x <=1 and diff_y <= 1: # Debug
                print("Both x and y coords for tail is within 1 of heads")
            if diff_x > 1:
                for i in range(diff_x-1):
                    if max(curr_head_coord[0], curr_tail_coord[0]) == curr_tail_coord[0]: # Tail is larger, move tail to the left
                        # Move the tail left
                        curr_tail_coord = [sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["L"])] # increment on x axis, so left
                        
                    else: # Head is larger, move tail to the right
                        curr_tail_coord = [sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["R"])]
            if diff_y > 1:
                for i in range(diff_y-1):
                    if max(curr_head_coord[1], curr_tail_coord[1]) == curr_tail_coord[1]:
                        curr_tail_coord = [sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["D"])]
                    else:
                        curr_tail_coord = [sum(tup) for tup in zip(curr_tail_coord, DIRECTION_DICT["U"])]
    return

def run():
    p1_solution()

    return

if __name__ == "__main__":
    run()