import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 两行两列

plt.subplot(2, 2, 1)

x1 = np.random.randint(-10, 10, 4).reshape(2, 2)

plt.plot(x1[0], x1[1])




plt.subplot(2, 2, 2)

x2 = np.random.randint(-10, 10, 4).reshape(2, 2)

plt.plot(x2[0], x2[1])




plt.subplot(2, 2, 3)

x3 = np.random.randint(-10, 10, 4).reshape(2, 2)

plt.plot(x3[0], x3[1])



plt.subplot(2, 2, 4)

x4 = np.random.randint(-10, 10, 4).reshape(2, 2)

plt.plot(x4[0], x4[1])


plt.show()
