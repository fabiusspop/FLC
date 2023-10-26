"""
# Ex 1 - Create your own module

from my_module import greet

name = input("Enter name: ")
print(greet(name))
"""

"""
# Ex 2 - List with 5 random numbers

import random 

l = [random.randint(1, 1000) for _ in range(5)]
print(f"Random numbers generated: ", l)
"""

"""
# Ex 3 - Function that prints 5 random int btwn 40 and 70

import random

def generateRandom():
    return [random.randint(40, 70) for _ in range(5)]

print(f"Random Generated Numbers from [40,70]: ", generateRandom())
"""   

"""
# Ex 4 - Use DateTime Module -> DateTime Obj -> Print Full Name of the Weekday of the Day

import datetime

now = datetime.datetime.now()
print(f"Today is", now.strftime('%A'))
""" 
"""
# Ex 5 - Create a directory. Create txt file inside. Add text to txt file. Read the first 2 lines. Overwrite the text inside de file

import os 

# Creating a Directory
directory_name = "my_directory"
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    
# Creating a.txt file inside it
file_path = os.path.join(directory_name, "a.txt")

# Adding text to a.txt
with open(file_path, 'w') as file:
    file.write("Ana are mere \n")
    file.write("Ana are pere \n")
    file.write("Ana are mere si pere \n")
    
# Reading the first 2 lines
with open(file_path, 'r') as file: 
    l1 = file.readline().strip()
    l2 = file.readline().strip()
    print(f"First line:", l1)
    print(f"Second line:", l2)

# Overwriting the text inside a.txt
with open(file_path, 'w') as file:
    file.write("Overwrited! \n")    

"""  

"""
# Ex 6 - Print name of the OS + files & directories

import os  
 
print("OS_Name:", os.name)
print("Files & Dir:", os.listdir('.'))
"""  

# Ex 7 - Display the date from 10 days ago

import datetime 

today = datetime.date.today()

print(f"Ten days ago was", today - datetime.timedelta(days=10))



