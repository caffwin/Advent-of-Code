# Lanternfish

initial_state = []

with open('test_input.txt') as file:
    unprocessed_input = file.readlines()
    string_list = unprocessed_input[0].strip().split(',')
    int_list_map_obj = map(int, string_list)
    initial_state = list(int_list_map_obj)


def calc_lanternfish_growth(initial_state, num_days):
    """
    Takes in an initial state of lanternfish, and returns the total number of lanterfish calculated after num_days
    """
    num_lanternfish = 0
    total_fish = len(initial_state)

    initial_state_length = len(initial_state)

    for day in range(num_days):
        for i in range(total_fish): # i --> index from initial state
            internal_timer = initial_state[i] # value of internal time for each fish
            
            if internal_timer == 0:
                initial_state.append(8) # Longer initial reproduction cycle
                total_fish += 1
                initial_state[i] = 6 # Reset internal timer value
                
            if internal_timer > 0:
                initial_state[i] -= 1

    return total_fish

print('calc_lanternfish_growth: ', calc_lanternfish_growth(initial_state, 80))
