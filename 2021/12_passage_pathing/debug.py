# Expected:


expected_result_list = []
with open('p2_expected_results.py') as file:
    for line in file:
        split_line = line.strip().split(',')
        # print(split_line)
        expected_result_list.append(split_line)


    
# Actual:
actual_results = [
['start', 'b', 'end'],
['start', 'b', 'd', 'b', 'end'],
['start', 'b', 'd', 'b', 'A', 'end'],
['start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
['start', 'b', 'd', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'end'],
['start', 'b', 'A', 'b', 'end'],
['start', 'b', 'A', 'b', 'A', 'end'],
['start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'c', 'A', 'b', 'end'],
['start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'b', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
['start', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'end'],
['start', 'A', 'b', 'end'],
['start', 'A', 'b', 'd', 'b', 'end'],
['start', 'A', 'b', 'd', 'b', 'A', 'end'],
['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'end'],
['start', 'A', 'b', 'A', 'b', 'end'],
['start', 'A', 'b', 'A', 'b', 'A', 'end'],
['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'end'],
['start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'],
['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'b', 'end'],
['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'd', 'b', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'b', 'end'],
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'],
]

extra_paths = []
for list in actual_results:
    if list not in expected_result_list:
        extra_paths.append(list)

print('investigate extra paths:')

for path in extra_paths:
    print(str(path))

# investigate extra paths:
['start', 'b', 'd', 'b', 'A', 'c', 'A', 'c', 'A', 'end']
['start', 'b', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end']
['start', 'b', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end']
['start', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'end']
['start', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end']
['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'c', 'A', 'end']
['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end']
['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end']
['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'end']
['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end']
['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end']
['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end']
['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'b', 'end']
['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end']
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'd', 'b', 'end']
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end']
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'b', 'end']
['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end']