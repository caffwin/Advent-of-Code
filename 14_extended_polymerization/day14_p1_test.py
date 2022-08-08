# Day 14 tests
import day14

TEST_FILE_1_PATH = 'dummy_input.txt'


def test_parse_input(file_name):
    result = day14.parse_input(file_name)
    expected_template = 'ABC'
    expected_dict =  {'AB': 'B', 'BC': 'A', 'CA': 'C', 'AC': 'C', 'BA': 'A', 'CC': 'A', 'BB': 'C', 'AA': 'B'}
    expected_result = expected_template, expected_dict

    if result == expected_result:
        print("success test 1")
    else:
        print("failure test 1")

def test_pair_insertion():
    # Tests pair insertion logic for a single step
    # Where the bulk of the logic lives
    
    template = 'ABC'
    insertion_rules = {'AB': 'B', 'BC': 'A', 'CA': 'C', 'AC': 'C', 'BA': 'A', 'CC': 'A', 'BB': 'C', 'AA': 'B'}

    # Returns the string of the next polymer template after elements have been inserted based on insertion_rules
    result = day14.perform_pair_insertion(template, insertion_rules)
    expected_result = 'ABBAC'

    insertion_rules2 = {'AB': 'C', 'BC': 'C', 'CA': 'C', 'AC': 'C', 'BA': 'A', 'CC': 'A', 'BB': 'C', 'AA': 'B'}
    result2 = day14.perform_pair_insertion(template, insertion_rules2)
    expected_result2 = 'ACBCC'

    if result == expected_result and result2 == expected_result2:
        print("success test 2")
    else:
        print("failure test 2")
    return

def test_calc_p1_solution():
    result1 = day14.calc_p1_solution('ABCD')
    result2 = day14.calc_p1_solution('NNBCNHDNNNHHNNNCN')
    # result3 = day14.calc_p1_solution('') # --> expect 0 also, but would get ValueError
    
    expected_result1 = 0
    expected_result2 = 9
    # expected_result3 = 0

    if result1 == expected_result1 and result2 == expected_result2:
        print("success test 3")
    else:
        print("failure test 3")

def main():
    test_parse_input(TEST_FILE_1_PATH)
    test_pair_insertion()
    test_calc_p1_solution()

if __name__ == '__main__':
    main()