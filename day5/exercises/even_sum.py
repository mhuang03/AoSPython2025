pairs = [(x, y) for x in range(11) for y in range(11) if (x+y) % 2 == 0]
#                                                     ^^^^^^^^^^^^^^^^^ include only pairs whose sum is even
#                                  ^^^^^^^^^^^^^^^^^^ loop y from 0 to 10
#               ^^^^^^^^^^^^^^^^^^ loop through all x from 0 - 10
print(pairs)