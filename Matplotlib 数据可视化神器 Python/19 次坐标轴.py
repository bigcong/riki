import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1);

y = x ** 2 + 1
y2 = -y

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y)
ax2.plot(x, y2)
plt.show()
