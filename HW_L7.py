import argparse

# Ex 1 - Create a parser that takes as args two numbers and computes their sum, difference, multiplication, division and mean

"""

parser = argparse.ArgumentParser()

parser.add_argument('x', type = int, help  = 'x')
parser.add_argument('y', type = int, help = 'y')

args = parser.parse_args()

sum = args.x + args.y
dif = args.x - args.y
mul = args.x * args.y
div = args.x / args.y
mean = (args.x + args.y) / 2

print("Sum= ", sum)
print("Dif= ", dif)
print("Mul= ", mul)
print("Div= ", div)
print("Mean= ", mean)

"""

# Ex 2 - Create a parser that takes as args 2 nbs and a string (math symbol) and depending on the symbol the program computes their sum, diff, multip, div, or mean

"""

parser = argparse.ArgumentParser()

parser.add_argument('a', type = int, help = 'a')
parser.add_argument('b', type = int, help = 'b')
parser.add_argument('sign', type = str, help = 'sign')

args = parser.parse_args()

def operationSymbol(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        return a / b
    elif sign == 'mean':
        return (a + b) / 2
    else:
        return "Invalid input"

result = operationSymbol(args.a, args.b, args.sign)
print(result)
        
"""

# Ex 3 - Write a program in Python which creates an HTML file with an ordered list with and an unordered list having items of any color         

import csv
import html

"""

parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r'))

args = parser.parse_args()

emails = []
first_names = []

with args.file as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        emails.append(html.escape(row['Email']))
        first_names.append(html.escape(row['FirstName']))

"""
#html_content = f"""<!DOCTYPE html>
#<html lang="en">
#<head>
#   <title>Emails and Names List</title>
#    <style>
#        body {{
#            background-color: #FF5733;  
#            color: #33FF93;            
#        }}
#        ul, ol {{
#            background-color: #A6B0AB;  
#        }}
#    </style>
#</head>
#<body>
#    <h2>Email</h2>
#    <ul>
#        {''.join(f'<li>{email}</li>' for email in emails)}
#    </ul>
#    <h2>FirstName</h2>
#    <ol>
#        {''.join(f'<li>{name}</li>' for name in first_names)}
#    </ol>
#</body>
#</html>

"""
outputHTML = 'output.html'

with open(outputHTML, 'w', encoding = 'utf-8') as htmlfile:
    htmlfile.write(html_content)
    
""" 
    
# Ex 4 - Write a program in python which creates an HTML file with a table with the columns “Name” and “Age” and populate it with the values from the following lists:

names = ["Alex", "Emma", "Kate", "Ryan", "Lily"]
ages = [21, 25, 36, 31, 27]

html_file_name = "names_ages_table.html"

with open(html_file_name, "w") as file:
    
    file.write("<html>\n")
    file.write("<head>\n<title>Table</title>\n</head>\n")
    file.write("<body>\n")
    file.write("<h1>NameAndAge</h1>\n")
    
    file.write("<table>\n")
    file.write("<tr><th>Name</th><th>Age</th></tr>\n")
    
    for name, age in zip(names, ages):
        file.write(f"<tr><td>{name}</td><td?{age}</td></tr>\n")
        
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("</html>\n")
    
print("Creating your html file...")

import time
for i in range(0,4):
    print(i)
    time.sleep(1)

print("File created successfully!")    
    