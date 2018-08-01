import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)
# 8 分成8分 #plt.cm.hot 热图 #plt.cm.hot  冷图
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# 等高线

C = plt.contour(X, Y, f(X, Y), 8, colors='black')
#inline控制是否将Label画在线里面，字体大小为10
plt.clabel(C, inline=True, fontsize=12)

plt.show()
