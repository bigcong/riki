import matplotlib.pyplot as plt
import numpy as np

# -*- coding: utf-8 -*-

# 生成-3，到3 50个数的等差数列
x = np.linspace(-3, 3, 100);
y1 = 2 * x + 2;
y2 = x * x + 2 * x + 1;

# 设置编号和大小
plt.figure(num=3, figsize=(8, 5))

plt.plot(x, y1, color='red', linewidth=1, linestyle='--')

plt.plot(x, y2, color='green', linewidth=1.0)

# x,y的取值范围
plt.ylim((-2, 3))
plt.xlim((-1, 2))

# 设置x,y的名字
plt.ylabel("y")
plt.xlabel("x")
# 设置x轴上的标尺
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)

plt.xticks(new_ticks)

plt.yticks([-2, -1.8, -1, 1.22, 3], ['$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# GCA=get current axis
ax = plt.gca();

ax.spines['right'].set_color('none')  # 去掉右边的线
ax.spines['top'].set_color('none')  # 去掉上边的线
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 调整原点
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
