import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(-10.0, 10.0, 0.01)
y = x**2 + 2*x + 3

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y',
       title='x**2+2x+3')
ax.grid()

# fig.savefig("test.png")
plt.show()