import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 100);
y = x * 2

plt.figure(num=3, figsize=(5, 8))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.ylim([-1000, 1000])
plt.plot(x, y, lw=10, zorder=1)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 调节字体大小
    label.set_fontsize(10)
    # facecolor调节 box 前景色，edgecolor 设置边框， 本处设置边框为无，alpha设置透明
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))

plt.show()
