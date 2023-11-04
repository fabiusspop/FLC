# Ex 3 - Create an excel file from HW5Ex2.txt (The columns should be LastName, FirstName, HiringDate, Salary)

import pandas as pd

with open('HW5Ex2.txt', 'r') as file:
    lines = file.readlines()

data = [line.strip().split(' , ') for line in lines]

excelFile = pd.DataFrame(data, columns=['LastName', 'FirstName', 'HiringDate', 'Salary'])

excelFile.to_excel('HW5Ex2.xlsx', index=False)

print("File created.")
