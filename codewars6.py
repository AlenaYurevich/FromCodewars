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

# function that will return true if this walk the app gives you will
# take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your
# starting point. Return false otherwise.
# def is_valid_walk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')
#
#
# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


# You are going to be given a word. Your job is to return the middle character of the word. If the word's length
# is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# def get_middle(s):
#     ind = int(len(s) / 2)
#     if len(s) % 2 == 0:
#         return s[ind - 1] + s[ind]
#     else:
#         return s[ind]
#
#
# print(get_middle("ah"))

# Your task is to write a function which returns the sum of a sequence of integers.
# def sequence_sum(begin_number, end_number, step):
#     return sum(range(begin_number, end_number + 1, step))
#
#
# print(sequence_sum(16, 15, 3))


# As a part of this Kata, you need to create a function that when provided with a
# triplet, returns the index of the numerical element that lies between the other
# two elements.
# def gimme(input_array):
#     res = sorted(input_array)[1]
#     return input_array.index(sorted(input_array)[1])
#
#
# print(gimme([-0.410, -23, 4]))

# to make two functions ( max and min, that receive a list of integers as input,
# and return the largest and lowest number in that list, respectively
# def minimum(arr):
#     return min(arr)
#
#
# def maximum(arr):
#     return max(arr)
#
#
# print(minimum([-52, 56, 30, 29, -54, 0, -110]))
# print(maximum([-52]))


# Given an array of integers, find the one that appears an odd number of times.
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# print(find_it([20, 1, -1,  2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be
# case-insensitive. The string can contain any char.
def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")


# print(xo("ooxXm"))

# Write a program that finds the summation of every number from 1 to num. The number will always
# be a positive integer greater than 0.
def summation(num):
    return sum(range(num + 1))


# print(summation(22))


# Write a 'welcome' function that takes a parameter 'language'
# (always a string), and returns a greeting - if you have it
# in your database. It should default to English if the language is not in the database,
# or in the event of an invalid input.
database = {'english': 'Welcome',
            'czech': 'Vitejte',
            'danish': 'Velkomst',
            'dutch': 'Welkom',
            'estonian': 'Tere tulemast',
            'finnish': 'Tervetuloa',
            'flemish': 'Welgekomen',
            'french': 'Bienvenue',
            'german': 'Willkommen',
            'irish': 'Failte',
            'italian': 'Benvenuto',
            'latvian': 'Gaidits',
            'lithuanian': 'Laukiamas',
            'polish': 'Witamy',
            'spanish': 'Bienvenido',
            'swedish': 'Valkommen',
            'welsh': 'Croeso'}


def greet(language):
    return database.get(language, "Welcome")


# print(greet('kmlknmklnm'))

# Write a function that takes an array of numbers (integers for the tests)
# and a target number. It should find two different items in the array
# that, when added together, give the target value. The indices of these
# items should then be returned in a tuple / list


def two_sum(numbers, target):
    for i in numbers:
        if target - i in numbers:
            return numbers.index(i)



print(two_sum([2, 2, 3], 4))
