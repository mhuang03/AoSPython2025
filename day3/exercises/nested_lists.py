nested = [[5, 6, 7], [2, 3], [10, 11, 12], [5]]
flattened = []

for inner_list in nested:
    # for element in inner_list:
    #     flattened.append(element)
    flattened += inner_list

print(flattened)
#   [ 5, 6, 7, 2, 3, 10, 11, 12, 5 ]
