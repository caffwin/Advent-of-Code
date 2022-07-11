import day12

TEST_FILE_1_PATH = 'test1.txt'
TEST_FILE_2_PATH = 'test2.txt'
TEST_FILE_3_PATH = 'test3.txt'


def test_start_end():
    result = day12.main(TEST_FILE_1_PATH)
    expected_result = 1
    print('result: ', result)

    if result == expected_result:
        print("success test 1")
    else:
        print("failure test 1")

def test_all_lower():
    result = day12.main(TEST_FILE_2_PATH)
    expected_result = 2
    print('result: ', result)

    if result == expected_result:
        return "success test 2"
    else:
        return "failure test 2"

def test_casing():
    result = day12.main(TEST_FILE_3_PATH)
    expected_result = 5
    print('result: ', result)

    if result == expected_result:
        return "success test 3"
    else:
        return "failure test 3"

def main():
    test_start_end()
    test_all_lower()
    test_casing()
    print('All tests passed!')

if (__name__ == '__main__'):
    main()