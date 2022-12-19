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
            direction, value = stripped_line.split(" ")
            INSTRUCTION_LIST.append((direction, int(value)))

def p1_solution():
    num_spaces_moved_tail = 0
    start_coord_head = (0, 0)
    start_coord_tail = (0, 0)
    curr_head_coord = start_coord_head
    prev_head_coord = None
    curr_tail_coord = start_coord_tail
    unique_coords_tail = set()
    unique_coords_tail.add(start_coord_tail)
    for instruction in INSTRUCTION_LIST:
        for i in range(instruction[1]):
            transformed_coord = tuple([sum(tup) for tup in zip(curr_head_coord, DIRECTION_DICT[instruction[0]])]) # instruction[0] is a single character string indicating the direction
            prev_head_coord = curr_head_coord
            curr_head_coord = transformed_coord

            diff_x = (abs(curr_tail_coord[0] - curr_head_coord[0]))
            diff_y = (abs(curr_tail_coord[1] - curr_head_coord[1]))

            if diff_x > 1 or diff_y > 1:
                curr_tail_coord = prev_head_coord
                unique_coords_tail.add(curr_tail_coord)
                num_spaces_moved_tail += 1

    return len(unique_coords_tail)

def run():
    parse_input()
    part_one_solution = p1_solution()
    print("part one solution: ", part_one_solution)
    return

if __name__ == "__main__":
    run()
