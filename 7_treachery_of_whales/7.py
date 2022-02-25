# Treachery of Whales

crab_position_list = []

with open('test_input.txt') as file:
    unprocessed_input = file.readlines()
    string_list = unprocessed_input[0].strip().split(',')
    int_list_map_obj = map(int, string_list)
    crab_position_list = list(int_list_map_obj)

upper_bound = max(crab_position_list)
lower_bound = min(crab_position_list)

def calculate_fuel_cost(crab_position_list):
    """
    Takes in a horizontal position list (list of ints), calculates the position with the lowest fuel consumption
    (total increment/decrement between all numbers) and returns the cost of fuel total.
    """

    # Best way to find a placeholder value for fuel consumed? Can make this an arbitrarily large # just to start
    least_fuel_consumed = 9999999999999
    most_efficient_position = None
    # Brute force approach - start with min or max, and go down until hitting min
    # Very likely for positions closer to upper/lower bound to be fuel inefficient

    # But.. approach is still the same to calculate:
    # if total fuel consumption for that position is less than total_fuel_consumption, then reassign
    # A "fan out" approach makes sense starting from the median
    # For better efficiency, could create separate list of unique ints, sorted, then take median?

    for i in range(lower_bound, upper_bound + 1): # Testing each position, brute force --> Ex. runs calculations from 1 to 16
        current_position = i
        total_fuel_consumed = 0
        for position in crab_position_list:
            difference = abs(position-i)
            for diff in range(1, difference + 1):
                total_fuel_consumed += diff

        if total_fuel_consumed < least_fuel_consumed:
            least_fuel_consumed = total_fuel_consumed
            most_efficient_position = i
    
    return least_fuel_consumed

print('calculate fuel consumption: ', calculate_fuel_cost(crab_position_list))
