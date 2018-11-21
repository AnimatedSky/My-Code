import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8,10]
y = [6,7,8,2,4]


x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label='Bars 1', color='blue')
plt.bar(x2, y2, label='Bars 2', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nLOOK AT IT')
plt.legend()

plt.show()

