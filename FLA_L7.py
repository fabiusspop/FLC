import numpy as np

# Ex 1 - list1=[1.4,5.9,2.6,7.3,8.5,9.3,6.1] -> Convert it into an array using numpy

print("Ex 1: ")

list1 = [1.4, 5.9, 2.6, 7.3, 8.5, 9.3, 6.1]

array1 = np.array(list1)

print(array1)
print("\n")

# Ex 2 - Write a program that creates a 1D array of even numbers between 70 and 91. (Hint: use arrange() from numpy)

print("Ex 2: ")

def evenNumbers(min, max):
    evenArray=np.arange(min, max, 2)
    
    return evenArray

print(evenNumbers(70,91))
print("\n")

# Ex 3 - Write a program that creates a 3x3 matrix populated by 0s and having the numbers 3,7,11 on the main diagonal. (Hint: use diag() from numpy)

print("Ex 3: ")

mx = np.diag([3,7,11])

print(mx)
print("\n")

# Ex 4 - Write a program that creates a 2x3 array of numbers between 10 and 16. (Hint: use arrange() and reshape() from numpy).

print("Ex 4: ")

arr1 = np.arange(10,16).reshape(2,3)

print(arr1)
print("\n")

# Ex 5 - ex5=np.array([[10,50,70,20,40],[5,45,95,35,65]]) ; Print all the numbers below and above 43 inside ex4 array.

print("Ex 5: ")

ex5 = np.array([[10, 50, 70, 20, 40], [5, 45, 95, 35, 65]])

ex4_1 = ex5[ex5 < 43]
ex4_2 = ex5[ex5 > 43]

print("Less than 43: ", ex4_1)
print("Greater than 43: ", ex4_2)
print("\n")

# Ex 6 - Use ex5 array. Write a program that saves the array in a text file, then load the content of it.

print("Ex 6: ")

np.savetxt('ex5.txt', ex5)

loadEx5 = np.loadtxt('ex5.txt')

print(loadEx5)
print("\n")

