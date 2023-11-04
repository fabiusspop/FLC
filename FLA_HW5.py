# In HW5Ex1.html:

import re

html = open("HW5Ex1.html", "r").read()

# a) Find and display the links (https://www.google.com/)

links = re.findall(r'href="(.+?)"', html)

print("Ex a) - Links:")
for link in links:
    print(link)


# b) Find and display the labels of the form (Last name, First name)

pattern = re.compile(r'<label for="(?:fname|lname)">([^<]+)</label>')

labels = pattern.findall(html)

print("Ex b) - Labels:")
for label in labels:
    print(label.strip())

# c) Find and display the types of the attributes in the form (text, number, email)

types_pattern = re.compile(r'<input type="(.*?)"')

types = types_pattern.findall(html)

print("Ex c) - Attributes:")
for t in types:
    print(t)

# d) Find and display the values of the options in the form (PhD Student, Professor)

options_pattern = re.compile(r'<option value="(.+?)">(.+?)</option>')

options = options_pattern.findall(html)

print("Ex d) - Values of options:")
for value, text in options:
    if text in ["PhD Student", "Professor"]:
        print(value)

# e) Find and display all the ids in the form (lname, fname)

ids_pattern = re.compile(r'<input .+? id="(.*?)"')

ids = ids_pattern.findall(html)

print("Ex e) - Ids:")
for id in ids:
    print(id)
     

