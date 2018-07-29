import matplotlib.pyplot as plt
import numpy as np

# 生成-3，到3 50个数的等差数列
x = np.linspace(-3, 3, 100);
y1 = 2 * x + 2;
y2 = x * x + 2 * x + 1;

# 设置编号和大小
plt.figure(num=3, figsize=(8, 5))

plt.plot(x, y1, color='red', linewidth=1, linestyle='--')

plt.plot(x, y2, color='green', linewidth=1.0)

plt.show()
