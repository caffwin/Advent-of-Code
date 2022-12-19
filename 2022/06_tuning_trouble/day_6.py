TEST_FILE_NAME = "test_input.txt"
DATASTREAM_BUFFER = None
DISTINCT_NUM_CHARS_P1 = 4
DISTINCT_NUM_CHARS_P2 = 14

with open(TEST_FILE_NAME) as file:
    for line in file:
        stripped_line = line.strip()
        DATASTREAM_BUFFER = stripped_line

def p1_solution():
    """
        Given a puzzle input, finds the first group of 4 sequential unique chars and returns the starting index where this occurs. 
    """
    index_flag = False
    packet_marker_index = None
    for i in range(0, len(DATASTREAM_BUFFER) - DISTINCT_NUM_CHARS_P1):
        packet_string = DATASTREAM_BUFFER[i] + DATASTREAM_BUFFER[i+1] + DATASTREAM_BUFFER[i+2] + DATASTREAM_BUFFER[i + 3]
        set_chars = set(packet_string)

        if len(set_chars) == DISTINCT_NUM_CHARS_P1:
            if not index_flag:
                packet_marker_index = int(i + 3) + 1
                index_flag = True

    return packet_marker_index

def p2_solution():
    # 14 distinct characters instead of 4
    index_flag = False
    packet_marker_index = None
    for i in range(0, len(DATASTREAM_BUFFER) - DISTINCT_NUM_CHARS_P2):
        packet_string = ""
        for j in range(i, i + DISTINCT_NUM_CHARS_P2):
            packet_string += DATASTREAM_BUFFER[j]
            set_chars = set(packet_string)
            
            if len(set_chars) == DISTINCT_NUM_CHARS_P2:
                if not index_flag:
                    packet_marker_index = j + 1
                    return packet_marker_index

    return

def run():
    part_one_solution = p1_solution()
    part_two_solution =  p2_solution()
    print("part one solution: ", part_one_solution)
    print("part two solution: ", part_two_solution)
    return

if __name__ == "__main__":
    run()