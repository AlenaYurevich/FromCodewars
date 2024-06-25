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


# print(two_sum([2, 2, 3], 4))


# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
def remove_url_anchor(url):
    return url.split("#")[0]


# print(remove_url_anchor("www.codewars.com#about"))
# print(remove_url_anchor("www.codewars.com?page=1"))

# Complete the solution so that it returns true if the first argument(string) passed in ends
# with the 2nd argument (also a string).

def solution(text, ending):
    return text.endswith(ending)

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple
# elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty
# array/list. Don't change the order of the elements that are left.Given an array of integers, remove the smallest value
# Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the
# lowest index. If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.


def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


# In this little assignment you are given a string of space separated numbers, and have to return the highest and
# lowest number.
def high_and_low(numbers):
    res = [int(num) for num in numbers.split(" ")]
    return f"{max(res)} {min(res)}"


# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:


def grow(arr):
    res = 1
    for num in arr:
        res *= num
    return res


# Write a function that always returns 5#
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/


def unusual_five():
    s = "eeeee"
    return s.count("e")


# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend
# to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the
# queue which is at the end of the array:


def warn_the_sheep(queue):
    queue.reverse()
    c = queue.index("wolf")
    if c == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return f"Oi! Sheep number {queue.index('wolf')}! You are about to be eaten by a wolf!"


# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. Itmustreturn the display
# text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'
