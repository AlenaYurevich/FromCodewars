"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling
faces.
Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose, but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ')' or D
No additional characters are allowed except for those mentioned.
Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
"""

import re


def count_smileys(arr):
    return len(list(re.findall(r"[:;][-~]?[)D]", " ".join(arr))))


result = re.match(r'AV', 'AV Analytics AV')
print(result.start())
print(result.end())

result = re.search(r'AV', 'AV Analytics AV')
print(result.group(0))

result = re.findall(r'AV', 'AV Analytics AV')
print(result)

result = re.split(r'y', 'Analytics')
print(result)

result = re.split(r'i', 'Analytics', maxsplit=1)
print(result)

result = re.sub(r'India', 'World', 'AV is largest Analytics community of India')
print(result)

result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)
"""
* означает «ноль или более символов»
Теперь вытащим первое слово, используя ^
Если мы используем $ вместо ^, то мы получим последнее слово, а не первое
Еще есть офигенный сайт - ihateregex.io, там удобно на базе абзаца писать регулярки, и вспомогательная диаграмма
 удобно рядом строится:
"""

result = re.findall(r'^\w+', 'AV is largest Analytics community of India')
print(result)

"""
Вернуть домены из списка адресов
[] содержит символы для поиска значений
() группирует символы внутри
. Любой символ кроме новой строки \n
"""
result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

result = re.findall(r'[Т,т]ариф.+', 'Сумма, Тариф и тарифы изменяются по тарифной политике')
print(result)

"""
Create a function which translates a given DNA string into RNA.
For example:
"GCAT"  =>  "GCAU"
"""


def dna_to_rna(dna):
    return dna.replace("T", "U")


"""
Count the number of divisors of a positive integer n.
"""


def divisors(n):
    return sum([1 for i in range(1, int(n/2) + 1) if n % i == 0]) + 1


"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""


def number(lines):
    return [f'{count}: {value}' for count, value in enumerate(lines, 1)]


"""
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
"""


def diamond(n):
    if n < 1 or n % 2 == 0:
        return None  # validate input
    res = ""         # initialize result string
    space = n // 2
    for i in range(1, n, 2):
        res += " " * space
        res += '*' * i
        res += '\n'
        space -= 1
    for i in range(n, 0, -2):
        res += " " * space
        res += '*' * i
        res += '\n'
        space += 1
    return res


print(diamond(5))


"""
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet 
should be shifted, like in the original Rot13 "implementation".
"""


def rot13(message):
    res = ''
    for c in message:
        if c.isalpha():
            if ord(c) <= 77:
                c = chr(ord(c) + 13)
                res += c
            elif ord(c) <= 90:
                c = chr(ord(c) - 13)
                res += c
            elif ord(c) <= 109:
                c = chr(ord(c) + 13)
                res += c
            else:
                c = chr(ord(c) - 13)
                res += c
        else:
            res += c
    return res


# def rot13(message):
#     abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     cba = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
#     mytable = message.maketrans(abc, cba)
#     return message.translate(mytable)


print(rot13("aA bB zZ 1234 *!?%"))


"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"""


def alphabet_position(text):
    # alfabet = "-abcdefghijklmnopqrstuvwxyz"
    # res = []
    # for i in text:
    #     if i.lower() in alfabet:
    #         i = alfabet.index(i.lower())
    #         res.append(str(i))
    # return ' '.join(res)
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at "))


"""
Messi is a soccer player with goals in three leagues:
LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.
Note: the input will always be valid.
For example: 5, 10, 2  -->  17
"""


# def goals(laLiga, copaDelRey, championsLeague):
#     return sum([laLiga, copaDelRey, championsLeague])


def goals(*args):
    return sum(args)


"""
Numbers ending with zeros are boring. They might be fun in your world, but not here.
Get rid of them. Only the ending ones.
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway
"""


def no_boring_zeros(n):
    try:
        return int(str(n).rstrip("0"))
    except ValueError:
        return n


print(no_boring_zeros(9606000))


"""
Complete function sale_hotdogs, function accepts 1 parameter: n, n is the number of hotdogs a customer will buy,
different numbers have different prices (refer to the following table), return how much money will the customer spend
to buy that number of hotdogs.
"""


def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)


# print(sale_hotdogs(100))


"""
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each
of the following phrases each time a petal was torn:
"""


def how_much_i_love_you(nb_petals):
    di = {1: "I love you",
          2: "a little",
          3: "a lot",
          4: "passionately",
          5: "madly",
          0: "not at all"}
    return di[nb_petals % 6]


"""
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month
11 (November), is part of the fourth quarter.
"""


# def quarter_of(month):
#     li = ["", "1 2 3", "4 5 6", "7 8 9", "10 11 12"]
#     for mo in li:
#         if str(month) in mo:
#             return li.index(mo)


def quarter_of(month):
    return 1 if month <= 3 else 2 if month <= 6 else 3 if month <= 9 else 4


"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and
lowercase) and numeric digits.
"""


def duplicate_count(text):
    t = text.lower()
    return len([i for i in set(t) if t.count(i) > 1])


# print(duplicate_count("Indivisibilities"))


"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is
known.He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height
(a bounce of 0.66). His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?
"""


def bouncing_ball(h, bounce, window):
    counter = -1
    if 0 < bounce < 1:
        while h > window:
            print(h * bounce)
            counter += 2
            h *= bounce
    return counter

#
# print(bouncing_ball(2, 0.5, 1))
# print(bouncing_ball(3, 0.66, 1.5))
# print(bouncing_ball(30, 0.66, 1.5))


"""
You will be given an array and a limit value. You must check that all values in the array are below or equal to the 
limit value. If they are, return true. Else, return false.
You can assume all values in the array are numbers.
"""


# def small_enough(array, limit):
#     return len(array) == len([i for i in array if i <= limit])


def small_enough(array, limit):
    return max(array) <= limit


print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))


"""
Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements 
but with the 'geese' removed.
"""
    

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]


# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))


"""
Given a string str, reverse it and omit all non-alphabetic characters.
"""


def reverse_letter(st):
    return "".join(i for i in st[::-1] if i.isalpha())


print(reverse_letter("ultr53o?n"))
