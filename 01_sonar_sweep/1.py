measurement_list = [] # For part 1
sliding_window_list = [] # For part 2

# Part 1 - final test file
with open('puzzle_input.txt') as file:
    lines = file.readlines()    
    for line in lines:
        measurement_list.append(int(line.rstrip("\n"))) # line.strip()

# Part 2 - sample test case
with open('test_file.txt') as file:
    lines = file.readlines()    
    for line in lines:
        sliding_window_list.append(int(line.rstrip("\n")))

def calculate_depth_increases(report):
    """
    Takes in an array of depth measurements (int) and returns the number of times
    a depth measurement increases from the previous measurement
    """
    num_increases = 0

    for i in range(1, len(report)):
        if report[i] > report[i-1]:
            num_increases += 1

    return  str(num_increases) + " increases out of " + str(len(report)) + " lines."

# print(calculate_depth_increases(measurement_list)) # Test part 1


# Part 2:
def calculate_increases_sliding_window(report, window_length):
    num_increases = 0
    temp_sum = 0

    # # naive approach with O(n^2) time complexity:
    # O(nw)
    # Suppose w = n/10
    # O(n * n/10) = O(n^2)
    # for i in range(0, len(report) - (window_length - 1)): # 9 rows, window 3 -> compare 7 sums
    #     current_sum = 0
    #     for j in range(i, i + window_length):
    #         print('current index: ', str(i) + '-' + str(j) + ' and current value: ', str(report[j]))
    #         current_sum += report[j]
    #     print('current_sum: ', current_sum)
    #     if current_sum > temp_sum and temp_sum > 0:
    #         num_increases += 1
    #         print('current sum is greater than temp sum, increasing...')

    #     temp_sum = current_sum
    #     print('')

    # Alternate solution O(n)
    # Calculate initial sum
    for i in range(0, window_length):
        temp_sum += report[i]
        
    subtract_value = report[0]

    for i in range(1, len(report) - (window_length - 1)):
        add_value = report[i + (window_length - 1)]
        current_sum = temp_sum + add_value - subtract_value

        if current_sum > temp_sum:
            num_increases += 1

        temp_sum = current_sum
        subtract_value = report[i]
    
    return 'Total increases: ' + str(num_increases)

# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H
#    
# A: 607 (N/A - no previous sum)
# B: 618 (increased)
# C: 618 (no change)
# D: 617 (decreased)
# E: 647 (increased)
# F: 716 (increased)
# G: 769 (increased)
# H: 792 (increased)
    
# 10 total rows, 8 total windows

print(calculate_increases_sliding_window(measurement_list, 3))