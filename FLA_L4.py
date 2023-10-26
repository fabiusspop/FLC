
# Ex 1 - a=“rectangle”, b=“square”, c=“sphere”, d=“triangle”, e=“cone”, f=“cube”, g=“cylinder”. Using compile(), print only the strings that start with either c or s and end with e.
"""
import re

l = ["rectangle", "square", "sphere", "triangle", "cone", "cube", "cylinder"]
reg = re.compile(r'^(c|s).*e$')

print("Strings that start with S or C:")

for s in l:
    if reg.match(s):
        print(s)
"""

# Ex 2 - words=“car, cat, dog, pool, bath, cone, cube, ring, int”. Write a regex that prints only the words that have exactly 4 letters.
"""
import re

words = "car, cat, dog, pool, bath, cone, cube, ring, int"

reg = re.compile(r'\b\w{4}\b')
matches = reg.findall(words)

print("Words of 4 letters: ")

for match in matches:
    print(match)

"""

# Ex 3 - list=[“square”,”triangle”,”cube”,”sphere”,”circle”,”pentagon”, “hexagon”, “rectangle”,”parallelogram”,”trapezoid”]. Loop thourgh the list and match only the words ending in “re”.

"""
import re

list = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", "rectangle", "parallelogram", "trapezoid"]
reg = re.compile(r're$')

print("Words ending in re:")

for i in list:
    if reg.search(i):
        print(i)
        
""" 

# Ex 4 - Take the list from the previous exercise and search for the words in it in the string: geo=“A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a
# triangle can have 0, 2 or 3 equal sides.”. Extract from geo the digits and the non-digits characters.

"""
import re 

geo = "A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."

d = re.findall(r'\d+', geo)
print("d:", d)

nd = re.sub(r'\d+', '', geo)
print("Nd:", nd)

"""

# Ex 5 - link=“https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias”. Extract the year, month and date

"""
import re

link = "https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias"
date = re.compile(r'(\d{4})/(\d{2})/(\d{2})')

match = date.search(link)

if match:
    print("Date extracted: ")
    year, month, day = match.groups()
    print(year, month, day)

"""

# Ex 6 - date = "2021-11-02“. Change the date format to DD-MM-YYYY.

"""
from datetime import datetime

d = "2021-11-02"

date = datetime.strptime(d, '%Y-%m-%d')
print("Date format: ", date)

reversedDate= date.strftime('%d-%m-%Y')
print("Reversed date format: ", reversedDate)

"""

# Ex 7 - Write a function to check if a string starts with a digit. Provide at least two examples (one right and one wrong).

"""
import re

def digitCheck(x):
    return bool(re.match(r'^\d', x))

print(digitCheck("1GoodExample"))  
print(digitCheck("BadExample")) 
"""

# Ex 8 - Write a function to check if a string ends with a digit. Provide at least two examples when calling the function (one right and one wrong). 
"""

import re

def digitCheck(s):
    return bool(re.search(r'\d$', s))

print(digitCheck("GoodExample1"))  
print(digitCheck("BadExample")) 
"""

# Ex 9 - Write a function to check if a string contains a digit. Provide at least two examples (one right and one wrong). 

import re 

def digitCheck(s):
    return bool(re.search(r'\d', s))

print(digitCheck("Good1Example"))
print(digitCheck("BadExample"))

