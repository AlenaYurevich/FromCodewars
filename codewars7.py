#  To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
#  In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
# def open_or_senior(data):
#     print(["Senior" if age > 54 and handicap > 7 else "Open" for (age, handicap) in data])
#
#
# open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6]])


# Simple, given a string of words, return the length of the shortest word(s).
# def find_short(s):
#     # your code here
#     print(min((len(word)) for word in s.split()))
#
#
# find_short("sdf ckckck")


# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings,
# ordered from shortest to longest.
def sort_by_length(arr):
    arr.sort(key=len)
    print(arr)


sort_by_length(["iiiii", "to", "beg", "life"])


