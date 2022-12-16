TEST_INPUT_FILE = "test_input.txt"
CYCLE_VALUE_LIST = []
SIGNAL_STRENGTH_CYCLES = [20, 60, 100, 140, 180, 220]

def p1_solution():
    sum_signal_strengths = 0
    with open(TEST_INPUT_FILE) as file:
        curr_value = 1
        CYCLE_VALUE_LIST.append(curr_value) # Add 1 for first cycle
        for line in(file):
            stripped_line = line.strip()
            if len(stripped_line) == 4: # noop
                CYCLE_VALUE_LIST.append(curr_value)
            else:
                CYCLE_VALUE_LIST.append(curr_value)
                addx, value = stripped_line.split(" ")
                curr_value += int(value)
                CYCLE_VALUE_LIST.append(curr_value) # Add value at the end of second cycle

    for cycle in SIGNAL_STRENGTH_CYCLES:
        sum_signal_strengths += (cycle * CYCLE_VALUE_LIST[cycle-1])

    return sum_signal_strengths

def run():
    print("Part one solution: ", p1_solution())
    return

if __name__ == "__main__":
    run()