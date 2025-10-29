import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, np.pi * 2, 100)

plt.plot(x, np.sin(x), 'r-')
plt.plot(x, np.cos(x), 'b:')
plt.show()