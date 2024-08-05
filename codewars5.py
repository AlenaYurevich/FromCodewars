"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling
faces.
Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose, but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.
Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
"""

import re


def count_smileys(arr):
    return len(list(re.findall(r"[:;][-~]?[)D]", " ".join(arr))))


result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.start())
print(result.end())

result = re.search(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)

result = re.split(r'y', 'Analytics')
print(result)

result = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
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
