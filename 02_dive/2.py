#            ^
#        ..  |
#            |
# ..    -----------
#    >(           O ) --->
#     . -----------
#            |
#  .         |
#            v

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

# 2 axis, x and y

# forward = increase x, horizontal pos
# down = increase depth y
# up = decrease depth y

# return product of depth & horizontal pos 



pos_list = []
# Part 1 - sample test case
# with open('test_file.txt') as file:
#     lines = file.readlines()    
#     for line in lines:
#         pos_list.append(line.rstrip("\n"))

# Part 1 - final test file
with open('puzzle_input.txt') as file:
    lines = file.readlines()    
    for line in lines:
        pos_list.append(line.rstrip("\n"))

values_dict = {
    "forward" : 0, # forward
    "depth_dec": 0, # up
    "depth_inc": 0 # down
}

# print('pos list: ', pos_list)
def pos_parser(pos_list):
    for line in pos_list:
        direction, value = line.split(' ')
        print('direction:', direction)
        print('value:', value)

        if direction == "forward":
            values_dict["forward"] += int(value)
        if direction == "up":
            values_dict["depth_dec"] += int(value)
        if direction == "down":
            values_dict["depth_inc"] += int(value)

    return values_dict

# print(pos_parser(pos_list))

def calculate_depth_position():
    return (values_dict["depth_inc"] - values_dict["depth_dec"]) * values_dict["forward"]

# print('final horizontal position * depth is: ', calculate_depth_position())

############################### Part 2 ###############################

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

def populate_pos_values(pos_list):
    forward = 0
    depth_value = 0
    aim_value = 0

    for line in pos_list:
        direction, value_string = line.split(' ') # Ex. forward, 8
        value = int(value_string)
        # print('direction: ', direction, ' value: ', str(value))

        if direction == "forward":
            # print(f'increasing horizontal position by {value} units')
            forward += value # increase horizontal position by X units.
            depth_value += (aim_value * value) # increases your depth by your aim multiplied by X.

        if direction == "up":
            aim_value -= value # decreases your aim by X units.

        if direction == "down":
            aim_value += value # increases your aim by X units.
    
    return forward, depth_value

def calculate_depth_with_aim():
    forward, depth = populate_pos_values(pos_list)
    return forward * depth

print("p2 answer: ", calculate_depth_with_aim())
