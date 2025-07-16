# Problem 4: Look and Say
# The look-and-say sequence is a sequence of numbers where each term is generated from the previous term.
# The first term is 1. To generate the next term, read the previous term and count the number of digits in each group of the same digit.
# For example, the first 5 terms are:
# 1, 11, 21, 1211, 111221
# "one", "one one", "two one(s)", "one two, one one", "one one, one two, two one(s)"
# Write a program that asks the user for a number n and prints the first n terms of the look-and-say sequence.
# Hint: It might be more convenient to work with strings instead of numbers for this problem.

n = int(input("How many terms: "))

prev = "1"  # 1211
print(prev)

for _ in range(1, n):
    current = prev[0]  # stores the current digit we see in the sequence
    tally = 1   # stores how many we've seen in a row
    next = ""

    for digit in prev[1:]:
        if digit == current:  # if we see the same digit, increase the tally by 1
            tally += 1
        else:  # if the digit is different, add the info from the previous section of digits, reset the counters
            next += f"{tally}{current}"
            current = digit
            tally = 1
    next += f"{tally}{current}"  # at the end, we add the final section of digits
    print(next)

    prev = next

#   1   1   1   2   2   1
#                       ^digit
#                       ^current
#   tally = 1
#   next = "312211"

