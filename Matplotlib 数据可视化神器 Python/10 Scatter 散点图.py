import numpy as np;
import matplotlib.pyplot as plt

n = 1024;

# 生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1)
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

# 例如 tan(45)=1 , arctan(1)=45
xxyy = np.arctan2(x, y)
# s是大小，c是颜色
plt.scatter(x, y, s=75, c=xxyy, alpha=.5)
plt.ylim(-1.5, 1.5)
plt.xlim(-1.5, 1.5)
plt.xticks(())  #
plt.yticks(())  #忽略x轴 y 轴


plt.show()
