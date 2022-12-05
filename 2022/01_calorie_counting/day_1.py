TEST_INPUT_FILE = 'test_input.txt'

def parse_elf_calories_into_dict(TEST_INPUT_FILE):
    """
        Takes in input file and parses into output dict containing elf number (int) as the key and total calories consumed (int) as the value.
    """
    elf_calorie_dict = {}
    with open(TEST_INPUT_FILE) as file:
        elf_num = 1
        for line in file:
            if line == '\n':
                elf_num += 1
            else:
                calories = int(line)
                if elf_num not in elf_calorie_dict.keys():
                    elf_calorie_dict[elf_num] = calories
                else:
                    elf_calorie_dict[elf_num] += calories

    return elf_calorie_dict

def calc_most_calories_consumed(elf_calorie_dict):
    """
    Takes in elf_calorie_dict (dictionary of elf number (int) to calorie (int) mapping) and iterates through keys, 
    returning the highest value in the dict. Returns the highest number of calories consumed (value).
    """
    most_calories_consumed = 0

    for key in elf_calorie_dict:
        if elf_calorie_dict[key] > most_calories_consumed:
            most_calories_consumed = elf_calorie_dict[key]

    return most_calories_consumed

def calc_sum_top_three_calories_consumed(elf_calorie_dict):
    dict_to_list = list(elf_calorie_dict.values())
    dict_to_list.sort(reverse=True)
    top_three_results = dict_to_list[:3]

    return sum(top_three_results)

def run():
    elf_calorie_dict = parse_elf_calories_into_dict(TEST_INPUT_FILE)
    most_calories_consumed = calc_most_calories_consumed(elf_calorie_dict)
    print('part one solution: ', most_calories_consumed)

    part_2_solution = calc_sum_top_three_calories_consumed(elf_calorie_dict)
    print('part two solution: ', part_2_solution)

if __name__ == "__main__":
    run()
