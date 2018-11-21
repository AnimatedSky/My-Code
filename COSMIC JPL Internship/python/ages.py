import matplotlib.pyplot as plt
import numpy as np

population_ages = (22,56,13,79,56,34,13,46,35,26,79,24,56,31,18)

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nLOOK AT IT')
plt.legend()

plt.show()

