# Advent of Code day 4

bingo_input = []
all_boards = []

BOARD_SIZE = 5

with open('test_input.txt') as input_file:
# with open('test_input.txt') as input_file:
    first_line = True
    
    for line in input_file:
        stripped_line = line.strip()

        if first_line:
            bingo_input = stripped_line.split(',')
            first_line = False

        else: # all other lines
            if stripped_line == "":
                all_boards.append([])

            else: # bingo board 
                bingo_row = stripped_line.split(' ')
                cleaned_bingo_row = [el for el in bingo_row if el != ""]
                all_boards[-1].append(cleaned_bingo_row) # last board      
                # Process entire line as list to the most recent board

# def play_bingo_single(board, input):
#     """ Checks through a bingo board (list of lists) for all elements in 
#     input and returns True if board wins"""

#     is_winner = False
#     # A list of coordinates for positions that match input
#     coord_list = [] # Ordered by index of row, then index in row 

#     # Bingo occurrs when:
#     # Rows: same five of first element in list: [0, 0], [0, 1], [0, 2], [0, 3], [0, 4]
#     # Columns: same five of second element in list: [0, 0], [1, 0], [2, 0], [3, 0], [4, 0]

#     # while is_winner = False:
#     for num in input:
#         # Each row in board
#         for i in range(len(board)): 
#             # Each item in row
#             for j in range(len(board[i])):
#             # for item in board[i]:
#                 print('row: ', str(i), ', index: ', str(j))
#                 # str(board[i][j]) --> value of index
#                 # str(i) --> index of row

#                 if str(num) == board[i][j]:
#                     coord_list.append([str(i), str(j)])


#     # print('coord_list: ', coord_list)

#     row_dict = {} # A dictionary of all row values and number of occurrences
#     col_dict = {}
#     # If any reach 5, bingo

#     coord_list = [[0, 1], [0, 2], [0, 3]]
#     for coord in coord_list:
#         # if coord_list[0] or coord_list[1] have same value 5 times
#         # print('coord[0]: ', coord[0])
#         if coord[0] not in row_dict: # 
#             row_dict[coord[0]] = 1
#         else:
#             row_dict[coord[0]] += 1

#         if coord[1] not in col_dict: # 
#             col_dict[coord[1]] = 1
#         else:
#             col_dict[coord[1]] += 1

#     # print('row_dict: ', row_dict)
#     # print('col_dict: ', col_dict)

#     for item in row_dict:
#         print('item in row dict: ', item)
#         print('value of item in row dict: ', row_dict[item])
#         if row_dict[item] >= BOARD_SIZE:
#             print("Bingo!")

#     for item in col_dict:
#         if col_dict[item] >= BOARD_SIZE:
#             print("Bingo!")

#     return

def calculate_final_score(unmatched_num_list, last_num):
    # Product of unmatching #s and last number called for bingo to occur
    return

def calculate_unmarked_nums(board, excluded_coords):
    """
    Takes in single winning board and calculates a sum of all unmarked input numbers.
    """
    sum_unmarked_nums = 0

    for i in range(len(board)):
        row = board[i]

        for j in range(len(row)):
            col = row[j]

            element = row[j]
            x_value = i
            y_value = str(j)

            current_coord = [str(x_value), str(y_value)]
            # print('current coord: ', current_coord)
            # Iterate through 2D array, only adding to sum if coords are not in excluded list
            if current_coord not in excluded_coords:
                # print('adding element: ', str(element))
                sum_unmarked_nums += int(element) # check if cast needed

    return sum_unmarked_nums
    

# Iterate through board, if index in match_coords, skip
# Else, add value to current value list

# Returns sum of unmatched nums
# print(calculate_unmatched_nums(all_boards))

def initiate_coord_boards(boards):
    coord_list = []
    for board in boards:
        coord_list.append([])
    return coord_list

# print(initiate_coord_boards(all_boards))

def play_bingo(boards, input):
    """Takes in a list of boards (5 x 5 2D array) and returns final score --
    a product of the sum of all unmarked numbers on the winning board and the
    number called for bingo to occur. """

    is_winner = False
    coords_list = initiate_coord_boards(boards)
    last_called_number = None
    winning_board_idx = None
    last_winning_board_idx = None
    winning_boards_list = []


    for board in boards:
        winning_boards_list.append(False)

    for num in input:
        # if is_winner == True:
        #     break
        
        last_called_number = num

        for i in range(len(boards)):
            board = boards[i]
            # Can't initialize empty board list here because it'll happen for each number in input, not number of boards
        # for board in boards:
            # Each item in board
            current_board_index = i
            # print('board at index i: ', str(boards[i]))
            for row_i in range(len(board)):
                # row_i is index of row
                row = boards[i][row_i]
                # print('row: ', row)
                # for element in range(boards[i][row_i]):
                for el_i in range(len(row)):
                    element = row[el_i] # --> value of each index
                    if str(num) == str(element): # If match
                        # print('match!')
                        # print('adding coords: ', str(row_i), 'and', str(el_i))
                        coords_list[i].append([str(row_i), str(el_i)]) 

        # Iterate list of coordinates from coords_list, each corresponding to a board
        # For each item in the complete coordinates list, 
        # print('coords_list: ', coords_list)
        for i in range(len(coords_list)):
            board_coord_list = coords_list[i] # a list containing coords for a single board
            row_dict = {}
            col_dict = {}

            for coord in board_coord_list:
                if coord[0] in row_dict:
                    row_dict[coord[0]] += 1
                else:
                    row_dict[coord[0]] = 1

                if coord[1] in col_dict:
                    col_dict[coord[1]] += 1
                else:
                    col_dict[coord[1]] = 1

            for item in row_dict:
                if row_dict[item] >= BOARD_SIZE:
                    winning_board_idx = i
                    winning_boards_list[i] = True # Mark off board in that position as True when board wins
                    if sum(winning_boards_list) == len(winning_boards_list):
                        last_winning_board_idx = i
                        # print('all boards have won, last winning board index: ', last_winning_board_idx)
                        sum_unmarked_nums = calculate_unmarked_nums(all_boards[last_winning_board_idx], coords_list[last_winning_board_idx])
                        # print('sum_unmarked_nums: ', sum_unmarked_nums)
                        # print('last_called_number: ', last_called_number)
                        final_score = sum_unmarked_nums * int(last_called_number)
                        return final_score

                    # Check to see if number of Trues is equal to length of list
                    # If so, then declare last winning board
                    # is_winner = True

            for item in col_dict:
                if col_dict[item] >= BOARD_SIZE:
                    # print("Bingo! On board index: ", str(i))
                    winning_board_idx = i
                    # print('winning_board_idx: ', winning_board_idx)
                    winning_boards_list[i] = True
                    # # is_winner = True
                    # print('winning_boards_list: ', winning_boards_list)
                    if sum(winning_boards_list) == len(winning_boards_list):
                        last_winning_board_idx = i
                        # print('all boards have won, last winning board index: ', last_winning_board_idx)
                        sum_unmarked_nums = calculate_unmarked_nums(all_boards[last_winning_board_idx], coords_list[last_winning_board_idx])
                        # print('sum_unmarked_nums: ', sum_unmarked_nums)
                        # print('last_called_number: ', last_called_number)
                        final_score = sum_unmarked_nums * int(last_called_number)
                        return final_score

    # print('last_winning_board_idx: ', last_winning_board_idx)
    # winning_board = all_boards[winning_board_idx]
    # excluded_coords = coords_list[winning_board_idx]
    # sum_unmarked_nums = calculate_unmarked_nums(winning_board, excluded_coords)

    # calculate_unmarked_nums # Call this on last_winning_board
    # final_score = sum_unmarked_nums * int(last_called_number)
    # print("final score: ", final_score)
    # return final_score
    return

# test_input = ['1', '6', '3', '9', '5']
# test_board = [['1', '2', '0'], ['7', '9', '8'], ['6', '5', '3']]
# print(parse_bingo_board(test_board, test_input))

# print('all boards: ', all_boards)

print(play_bingo(all_boards, bingo_input))