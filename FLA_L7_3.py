import matplotlib.pyplot as plt
import numpy as np

y = np.array([1, 2, 3, 4, 5])
mylabels = ["A", "B", "C", "D", "E"]
mycolors = ["magenta", "cyan", "black", "red", "blue"]

plt.pie(y, labels = mylabels, colors = mycolors, shadow = True)
plt.show()