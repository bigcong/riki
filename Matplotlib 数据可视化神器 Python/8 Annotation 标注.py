import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100);
y = x * 2 + 1;
plt.figure(num=3, figsize=(8, 5))

plt.plot(x, y)

# 然后我们挪动坐标轴的位置

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')

ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 定义一个点注解
x0 = 1;
y0 = x0 * 2 + 1

# 颜色为蓝色，s=50 大小为50
plt.scatter(x0, y0, s=50, color='b')
# 虚线，宽度为2.5虚线
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)
#xytext 弧度的长度，
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
plt.show()
