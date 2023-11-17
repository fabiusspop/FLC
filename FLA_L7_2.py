import matplotlib.pyplot as plt
import numpy as np

# Ex 8 - Two lines intersecting

x = np.linspace(1, 9, 100)
y1 = x  
y2 = 1 + 0.5 * x  

plt.plot(x, y1, color='cyan')  
plt.plot(x, y2, color='magenta')  

plt.title('Two lines intersecting')

plt.show()
