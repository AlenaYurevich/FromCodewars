# The goal of this exercise is to convert a string to a new string where
# each character in the new string is "(" if that character appears only
# once in the original string, or ")" if that character appears more than once
# in the original string. Ignore capitalization when determining if a character
# is a duplicate.
# def duplicate_encode(word):
#     word = word.lower()
#     return "".join(("(" if word.count(i) == 1 else ")" for i in word))
#
#
# print(duplicate_encode('WaWt)K uZkcf'))

# function that will return true if the walk the app gives you will
# take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your
# starting point. Return false otherwise.
# def is_valid_walk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')
#
#
# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


# You are going to be given a word. Your job is to return the middle character of the word. If the word's length
# is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(s):
    ind = int(len(s) / 2)
    if len(s) % 2 == 0:
        return s[ind - 1] + s[ind]
    else:
        return s[ind]


print(get_middle("ah"))
