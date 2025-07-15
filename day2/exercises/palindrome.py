text = input("Type something: ")

#  a  b  c  d  e  f
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

for i in range(len(text)//2):  # i = 0, i = 1, ..., i = half the length
    if text[i] != text[-(i+1)]:
        print("Not a palindrome!")
        break
else:  # else block on a for loop runs only if no break statement happened.
    print("Palindrome!")
