import re


# Ex 1 - Write a function that checks if a string contains only lowercase letters, digits and *. Provide at least two examples (one right and one wrong).
"""

def stringCheck(s):
    reg = re.compile(r'^[a-z0-9*]+$')
    return bool(reg.match(s))

print(stringCheck("rightexample1*"))  
print(stringCheck("Badexample1*"))  

"""

# Ex 2 - Write a function that checks if a string has the following pattern: word containing only uppercase letters _ word containing only lowercase letters (e.g., FILS_student). Provide at least two examples (one right and one wrong). 

"""

def stringCheck(s):
    reg = re.compile(r'^[A-Z]+_[a-z]+$')
    return bool(reg.match(s))

print(stringCheck("FILS_student"))  
print(stringCheck("FiLS_student"))   

"""  

# Ex 3 - hw4=“rectangle square sphere triangle cone cube cylinder”. Print all the words ending in “le” or “re”.

"""

hw4 = "rectangle square sphere triangle cone cube cylinder"
reg = re.compile(r'\b\w+(?:le|re)\b')
matches = reg.finditer(hw4)

print("Words ending in le or re:")

for match in matches:
    print(match.group())
    
"""  

# Ex 5 - Create a program that changes the format of a date from YY-MM-DD to DD-MM-YY and changes the month from a number to its name. (e.g., 21-12-01 will be 01-December-21). Provide at least one example.

"""

def dateFormat(date):
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    reg = re.compile(r'(\d{2})-(\d{2})-(\d{2})')
    
    day, month, year = reg.match(date).groups()
    
    return f"{day}-{months[int(month)-1]}-{year}"

d = "02-07-24"
print(dateFormat(d)) 

""" 

# Ex 6 - Write a function that matches only text that starts with m, ends with n and have exactly 3 characters between them. Provide at least two examples when calling the function (1 right and 1 wrong)

"""

def itsaMatch(s):
    reg = re.compile(r'^m.{3}n$')
    return bool(reg.match(s))

print(itsaMatch("mabcn"))
print(itsaMatch("mabcdn"))

"""  

# Ex 7 - Write a function that matches only text that starts with h and is followed by exactly 2 or 3 i. Provide at least two examples when calling the function (1 right and 1 wrong)

"""

def itsaMatch(s):
    reg = re.compile(r'^hi{2,3}$')
    return bool(reg.match(s))

print(itsaMatch("hiii"))
print(itsaMatch("hiiii"))

"""  

# Ex 8 - Write a function that matches words containing q, but not in the beginning or at the end of a word. Provide at least two examples when calling the function (1 right and 1 wrong)

"""

def itsaMatch(s):
    reg = re.compile(r'\wq\w')
    return bool(reg.match(s))


print(itsaMatch("RightqExample")) 
print(itsaMatch("qBadExample")) 

""" 

# Ex 9 - Write a function that replaces all a in a string with u and all i with e.

def replaceChar(s):
    return s.replace("a", "u").replace("i", "e")

print(replaceChar("aiaiaiaiaiPuertoRico"))

