#Ex 1 : Current Time
"""
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y %B %d %H:%M:%S"))
"""

#Ex 2 : Radius of a Circle
"""
import math

radius = float(input("R: "))
print(f"Area is {math.pi * radius**2}")
"""

#Ex 3 : Selecting Random Nb. from a List
"""
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Random nb selected is:", random.choice(l))
"""

#Ex 4: Shuffle Elem. from a List
"""
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(l)
print(f"Random number shuffled is: ", numbers)
"""

#Ex 5: LCM and GCD with Math Module
"""
import math

a = int(input("a: "))
b = int(input("b: "))

print(f"GCD:", math.gcd(a, b))
print(f"LCM:", abs(a*b) // math.gcd(a, b))
"""

#Ex 6: Factorial Nb. with Math Module
"""
import math

x = int(input("X: "))
print(f"X!:", math.factorial(x))
"""

#Ex 7: Week nb. of a date using isocalendar()
"""
from datetime import datetime

now = datetime.now()
print(f"Week nb:", now.isocalendar()[1])
"""

#Ex 8: Distance btwn. 2 points
import math

x1, y1 = map(float, input("A(x1,y1): ").split())
x2, y2 = map(float, input("B(x2,y2): ").split())
print(f"|A,B|:", math.sqrt((x2 - x1)**2 + (y2 - y1)**2))







