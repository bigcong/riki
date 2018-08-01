import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
# 3行3列，起点0,0 跨度：3
ax1 = plt.subplot2grid((3, 3), (0, 1), colspan=3)
ax1.plot([1, 2], [1, 2])  # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=1)
ax1.plot([1, 2], [1, 2])  # 画小图
ax1.set_title('ax1_title2')  # 设置小图的标题

ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)


plt.figure()
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])


f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

plt.tight_layout()
plt.show()
