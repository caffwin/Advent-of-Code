import day12

TEST_FILE_1_PATH = 'test1.txt'
TEST_FILE_2_PATH = 'test2.txt'
TEST_FILE_3_PATH = 'test3.txt'

# don't worry about ordering, write results in order algorithm puts them in
# Write in order of what algorithm expects
def test_start_end():
    results = day12.main(TEST_FILE_1_PATH)
    expected_lists = [['start', 'end']]

    len_paths = len(results)
    num_matches = 0

    for result in results:
        if result in expected_lists:
            num_matches += 1

    if num_matches == len_paths:
        print("success test 1")
    else:
        print("failure test 1")

def test_all_lower():
    expected_lists = [['start', 'a', 'e', 'end'], ['start', 'a', 'd', 'f', 'e', 'end']]
    results = day12.main(TEST_FILE_2_PATH)

    len_paths = len(results)
    num_matches = 0

    for result in results:
        if result in expected_lists:
            num_matches += 1

    if num_matches == len_paths:
        print("success test 2")
    else:
        print("failure test 2")

def test_casing():
    expected_lists = [['start', 'b', 'end'], ['start', 'b', 'A', 'end'], ['start', 'A', 'end'], ['start', 'A', 'b', 'end'], ['start', 'A', 'b', 'A', 'end']]
    results = day12.main(TEST_FILE_3_PATH)

    len_paths = len(results)
    num_matches = 0

    for result in results:
        if result in expected_lists:
            num_matches += 1

    if num_matches == len_paths:
        print("success test 3")
    else:
        print("failure test 3")

def main():
    test_start_end()
    test_all_lower()
    test_casing()

if (__name__ == '__main__'):
    main()
