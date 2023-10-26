#ex1
"""for num in range(40, 71):
    if num % 3 == 0:
        print(num)
        
print("-----")"""
        
#ex2
"""first_name = input("First name: ")
last_name = input("Last name: ")
print(last_name + " " + first_name)
print("------")"""

#ex3
"""n = int(input("Enter a number: "))
total = sum(range(1, n+1))
print(total)
print("-------")"""

#ex4
"""for i in range(5, 15):
    print("Success! ^_^")
print("------")"""

#ex5
"""s = "Welcome to the lab!"
i = ["m", "l", "c", "a", "e"]
for i in s:
    print(f"{i}: {s.count(i)}")
print("------")"""

#ex6
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
    
n = int(input("Number: "))
print(factorial(n))"""

#ex7
"""n = int(input("Enter nb: "))
if n > 100:
    n = n / 2 + 20
else:
    n = n * 3 - 200
print(n)"""

#ex8
"""n = input("Enter nbs sep by comma: ")
n_list = n.split(',')
n_tuple = tuple(n_list)
print("List:", n_list)
print("Tuple:", n_tuple)"""

#ex9
"""n = int(input("Nb: "))
for i in range(1, n + 1):
    print(i**2)"""