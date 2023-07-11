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
# def sort_by_length(arr):
#     arr.sort(key=len)
#     print(arr)
#
#
# sort_by_length(["iiiii", "to", "beg", "life"])


# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# def stray(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             print(i)
#
#
# stray([17, 17, 3, 17, 17, 17, 17])
# stray([1, 1, 2])


# When provided with a number between 0-9, return it in words.

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the
# input parameters, including them.
# def between(a, b):
#     return list(range(a, b + 1))


# print(between(2, 8))


# Your task is to return the number of people who are still on the bus after the last bus stop
# (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might
# still be inside the bus, they are probably sleeping there
# def number(bus_stops):
#     return sum(i[0] - i[1] for i in bus_stops)
#
#
# print(number([[10, 0], [3, 5], [5, 8]]))
#
#
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')


print(correct("L0ND0N"))
print(correct("51NGAP0RE"))
