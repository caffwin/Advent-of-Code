TEST_INPUT = "test_input.txt"
MONKEY_DICT = {}
MODULUS = 1

def parse_input():
    global MODULUS
    MODULUS = 1
    with open(TEST_INPUT) as file:
        monkey_num = None
        for line in file:
            stripped_line = line.strip()

            if stripped_line.startswith("Monkey"):
                monkey_num = str(stripped_line[7:-1])
                MONKEY_DICT[monkey_num] = []

            if stripped_line.startswith("Starting"):
                worry_level_values = stripped_line[16:].split(",")
                starting_worry_level_list = list(map(int, worry_level_values))
                MONKEY_DICT[monkey_num].append(starting_worry_level_list)

            if stripped_line.startswith("Operation"):
                operation = stripped_line[21:].split(" ")
                MONKEY_DICT[monkey_num].append(operation)

            if stripped_line.startswith("Test"): # Always "divisible by"
                divisible_by = stripped_line[19:]
                MODULUS *= int(divisible_by)
                MONKEY_DICT[monkey_num].append(divisible_by)

            if stripped_line.startswith("If true"):
                true_action_lst = stripped_line[9:].split(" ")
                true_action_pass_to_monkey = true_action_lst[-1]
                MONKEY_DICT[monkey_num].append(true_action_pass_to_monkey)

            if stripped_line.startswith("If false"):
                false_action_lst = stripped_line[10:].split(" ")
                false_action_pass_to_monkey = false_action_lst[-1]
                MONKEY_DICT[monkey_num].append(false_action_pass_to_monkey)

        for key in MONKEY_DICT:
            MONKEY_DICT[key].append(0) # For holding total number of items inspected, part one solution

def run(num_rounds, use_modulus):
    # Monkey is a list containing:
        # Lists -- starting items
        # Operation
        # Rule
        # True outcome
        # False outcome
    for i in range(num_rounds):
        for monkey_num in MONKEY_DICT:
            monkey_attributes = MONKEY_DICT[monkey_num]
            item_worry_level_list = monkey_attributes[0]
            full_operation = monkey_attributes[1] # Ex: ["*", "old"]
            divisible_by_num = int(monkey_attributes[2])
            true_condition_monkey = monkey_attributes[3]
            false_condition_monkey = monkey_attributes[4]

            num_items_inspected = 0 # For part one solution

            while item_worry_level_list:
                # Operator
                item_worry_level = item_worry_level_list.pop(0)
                num_items_inspected += 1
                operator = full_operation[0] 
                second_operand = full_operation[1]
                if operator == "+":
                    if second_operand == "old": # old + old
                        item_worry_level += item_worry_level
                    else: # old + 5
                        item_worry_level += int(second_operand)

                else: # Assume it must be *
                    if second_operand == "old": # old * old
                        item_worry_level *= item_worry_level
                    else: # must be an int -- old * 5
                        item_worry_level *= int(second_operand)

                if use_modulus:
                    item_worry_level %= MODULUS # Part two solution
                else:
                    item_worry_level //= 3 # Part one solution, divide by 3

                # Check "divisible by" rule
                if item_worry_level % divisible_by_num == 0:
                    new_item = item_worry_level
                    MONKEY_DICT[true_condition_monkey][0].append(new_item)
                else:
                    new_item = item_worry_level
                    MONKEY_DICT[false_condition_monkey][0].append(new_item)

            MONKEY_DICT[monkey_num][5] += num_items_inspected

    return MONKEY_DICT

# Debug
def print_monkey_dict_worry_list(MONKEY_DICT):
    for key in MONKEY_DICT:
        print("Monkey ", str(key), ": " + str(MONKEY_DICT[key][0]))

def calc_product_top_two_inspected_items(monkey_dict):
    list_desc_inspected_item_count = []
    for key in monkey_dict:
        list_desc_inspected_item_count.append(monkey_dict[key][5])

    list_desc_inspected_item_count.sort(reverse=True)
    product_top_two_inspected_items = list_desc_inspected_item_count[0] * list_desc_inspected_item_count[1]
    return product_top_two_inspected_items

def main():
    parse_input()
    print("part one solution: ", calc_product_top_two_inspected_items(run(20, False)))

    parse_input()
    print("part two solution: ", calc_product_top_two_inspected_items(run(10000, True)))
    return

if __name__ == "__main__":
    main()
