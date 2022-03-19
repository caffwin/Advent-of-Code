# Lanternfish day 2 - Calculate exponential growth after 256 days

initial_state = []
NUM_DAYS = 256

with open('test_input.txt') as file:
    unprocessed_input = file.readlines()
    string_list = unprocessed_input[0].strip().split(',')
    int_list_map_obj = map(int, string_list) 
    initial_state = list(int_list_map_obj)

def create_initial_state_list(initial_state):
    """
    Takes in parsed initial state list of ints and populates an internal timer count list where the index corresponds to 
    the internal timer value and the value corresponds to the number of fish with that internal timer value.
    """

    state_list = [0] * 9
    for num in initial_state:
        state_list[num] += 1
    
    return state_list

lanternfish_state_list_initial = create_initial_state_list(initial_state)

def count_lanternfish(lanternfish_list):
    count = 0
    for value in lanternfish_list:
        count += value
    return count

def calc_lanternfish_growth(initial_state_list, num_days):
    """
    Takes in an initial state list of lanternfish, and returns the total number of lanterfish calculated after num_days
    """

    for day in range(num_days):
        num_fish_spawned = 0
        for i in range(len(initial_state_list)):
            current_internal_timer_value = initial_state_list[i]
            if i == 0 and initial_state_list[i] > 0:
                initial_state_list[6] += initial_state_list[i] # Add value of 0th index to timer with 6 count (index) 
                initial_state_list[8] += initial_state_list[i] # Spawn same number of fish with new timers, with count of 8
                num_fish_spawned += initial_state_list[i]
                initial_state_list[i] = 0 # reset 0th index to 0

            if i > 0 and current_internal_timer_value > 0:
                if i == 6 or i == 8: # When new fish spawn or existing fish resets, leave 'em alone
                    initial_state_list[i-1] += initial_state_list[i] - num_fish_spawned
                    initial_state_list[i] = num_fish_spawned
                else:
                    initial_state_list[i-1] += current_internal_timer_value
                    initial_state_list[i] = 0

    return "Lantern fish count: " + str(count_lanternfish(initial_state_list))

print('calc_lanternfish_growth after 1 days: ', calc_lanternfish_growth(lanternfish_state_list_initial, NUM_DAYS))
