import matplotlib.pyplot as plt
import numpy as np

# 生成0到-1 ，50个点
x = np.linspace(-1, 1, 50)
# y = 2 * x + 1;
y = x * x
plt.plot(x, y)
plt.show()
