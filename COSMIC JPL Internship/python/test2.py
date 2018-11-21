import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot (x,y, label='First line')
plt.plot (x2,y2, label='second line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting graph\nLOOK AT IT')
plt.legend()

plt.show()

