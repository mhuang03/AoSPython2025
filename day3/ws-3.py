# Problem 3: Anagrams
# Design a function that accepts two strings and returns True if the strings are anagrams,
# and False otherwise. Anagrams are words or phrases that are formed by rearranging the
# letters of another word or phrase, using all the original letters exactly once.
# For example, "listen" and "silent" are anagrams.
# Hint: You could: 1) use a dictionary to store the counts of each letter in each string.
#               or 2) sort the letters in each string and compare the sorted strings.

def anagrams(word1, word2):
    # counts1 = {}
    # for char in word1:
    #     if char not in counts1:
    #         counts1[char] = 1
    #     else:
    #         counts1[char] += 1
    #
    # counts2 = {}
    # for char in word2:
    #     if char not in counts2:
    #         counts2[char] = 1
    #     else:
    #         counts2[char] += 1
    #
    # if len(counts1) != len(counts2):
    #     return False
    #
    # for key1 in counts1:
    #     if key1 not in counts2:
    #         return False
    #     if counts1[key1] != counts2[key1]:
    #         return False
    # return True

    if sorted(word1) == sorted(word2):
        return True
    return False


print(anagrams("anagram", "nagaram"))
