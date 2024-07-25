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
