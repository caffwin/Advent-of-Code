TEST_INPUT_FILE = 'test_input.txt'

def parse_elf_calories_into_dict(TEST_INPUT_FILE):
    """
        Takes in input file and parses into output dict containing elf (key) and total calories consumed (value).
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


def find_fattest_elf(elf_calorie_dict):
    """
    Takes in a dictionary and iterates through keys, returns the highest value in the dict (representing number of calories consumed).
    """
    fattest_elf = None
    most_calories_consumed = 0

    for key in elf_calorie_dict:
        if elf_calorie_dict[key] > most_calories_consumed:
            most_calories_consumed = elf_calorie_dict[key]
            fattest_elf = key

    return most_calories_consumed


def run():
    elf_calorie_dict = parse_elf_calories_into_dict(TEST_INPUT_FILE)
    most_calories_consumed = find_fattest_elf(elf_calorie_dict)
    print('Part 1 answer: ', most_calories_consumed)

if __name__ == "__main__":
    run()

# 130 answer is too low