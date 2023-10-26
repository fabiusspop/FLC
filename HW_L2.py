#ex 1 - fibo series
"""def fibo(n):
    l = []
    a = 0
    b = 1  

    for _ in range(n):
        l.append(a) 
        a = b 
        b = a + b 

    return l

n = int(input("Number: "))
print(fibo(n))"""

#ex 2 - GCD
"""def gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x 

a = int(input("x: "))
b = int(input("y: "))
print(f"GCD is:", gcd(a,b))"""

#ex 3 - LCM
"""def lcm(x, y):
    def gcd(x, y):
        while y: 
            x, y = y, x % y
        return x
    
    val = abs(x * y) // gcd(x, y)
    return val
    
a = int(input("a: "))
b = int(input("b: "))
print(f"LCM is:", lcm(a, b))"""

#ex 4 - Even/Odd list
"""def splitList(l):
    even = [i for i in l if i % 2 == 0] #list comprehension ;) 
    odd = [i for i in l if i % 2 != 0]
    
    return even, odd

lst = [int (i) for i in input("Enter list: ").split()]
even, odd = splitList(lst)
print(f"Even list: ", even)
print(f"Odd list: ", odd)"""

#ex 5 - Cube
"""class Cube:
    def __init__(self, side_length):
        self.side = side_length

    def area_of_one_surface(self):
        return self.side ** 2

    def area_of_all_surfaces(self):
        return 6 * self.area_of_one_surface()

    def volume(self):
        return self.side ** 3


side_length = int(input("Enter side length: "))
c = Cube(side_length)

print(f"One Surface Area: {c.area_of_one_surface()}")
print(f"Total Surface Area: {c.area_of_all_surfaces()}")
print(f"Volume: {c.volume()}")"""

#ex 6 - Lambda Program
exp = lambda x, y: x ** y

x = float(input("x: "))
y = float(input("y: "))
print(f"x ^ y: ", exp(x, y))
