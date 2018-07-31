import matplotlib.pyplot as plt
import numpy as np

plt.figure()
n = 12
X = np.arange(n)
# 非正式均匀分布
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1)
plt.bar(X, -Y2)

plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)
# 去掉x,y 轴
plt.xticks(())
plt.yticks(())

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.1, -y - 0.05, '%.2f' % y, ha='center', va='top')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    # x + 0.1, y+0.15指的x,y 的位置，'%.2f' 是保留两位小数
    plt.text(x + 0.1, y + 0.15, '%.2f' % y, ha='center', va='top')
plt.show()
