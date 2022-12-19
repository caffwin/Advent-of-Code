TEST_INPUT = "test_input.txt"
MONKEY_DICT = {}

# Output should be a monkey dict containing monkeys (key) with a list (value) of worry levels (ints) after the instruction is carried out.
# Function takes in step # and applies that to each monkey
# List of:
# Lists -- starting items
# Operation
# Rule
# True outcome
# False outcome


with open(TEST_INPUT) as file:
    monkey_num = None
    for line in file:
        stripped_line = line.strip()

        if stripped_line.startswith("Monkey"):
            monkey_num = str(stripped_line[7:-1])
            MONKEY_DICT[monkey_num] = []

        # For starting items
        if stripped_line.startswith("Starting"):
            starting_worry_level_list = stripped_line[16:].split(",")
            MONKEY_DICT[monkey_num].append(starting_worry_level_list)

        if stripped_line.startswith("Operation"):
            operation = stripped_line[11:].split(" ")
            MONKEY_DICT[monkey_num].append(operation)

        if stripped_line.startswith("Test"): # The rule
            rule = stripped_line[6:]
            MONKEY_DICT[monkey_num].append(rule)

        if stripped_line.startswith("If true"):
            true_action = stripped_line[9:]
            MONKEY_DICT[monkey_num].append(true_action)

        if stripped_line.startswith("If false"):
            false_action = stripped_line[10:]
            MONKEY_DICT[monkey_num].append(false_action)
 
def run():
    print(MONKEY_DICT)
    return

if __name__ == "__main__":
    run()