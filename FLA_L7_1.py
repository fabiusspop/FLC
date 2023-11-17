# Ex 7 - Using matplotlib, create a 3x2 subplot with:

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
y = np.linspace(0, 10, 10)
z = np.random.randint(0, 100, 10)


# 7.1. Line with custom marker color for points
plt.subplot(3, 2, 1)
plt.plot(x, y)  
plt.title('Title 1')

# 7.2. Line with custom style and grid
plt.subplot(3, 2, 2)
plt.plot(x, y, 'g--')  
plt.title('Title 2')
plt.grid(True)

# 7.3. Vertical bars with custom color, width
plt.subplot(3, 2, 3)
plt.bar(x, y, color='#00FFFF', width=0.1)  
plt.title('Title 3')

# 7.4. Scattered points with different colors
z = np.random.randint(0, 100, 10)
plt.subplot(3, 2, 4)
plt.scatter(x, y, c=z, cmap='inferno')  
plt.title('Title 4')

# 7.5. 1 line with custom style, color & 1 line with custom width, color
plt.subplot(3, 2, 5)
plt.plot(x, y, 'b:', color='#00FFFF')  
plt.plot(y, x, color='#00BBBB', linewidth=1)  
plt.title('Title 5')

# 7.6. Horizontal bars with custom color, height
plt.subplot(3, 2, 6)
plt.barh(x, y, color='#00FFFF', height=0.2)  
plt.title('Title 6')

plt.show()
