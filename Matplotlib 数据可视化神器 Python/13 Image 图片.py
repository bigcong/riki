import numpy as np;
import matplotlib.pyplot as plt;

print(np.random.uniform(0, 1, 9).reshape(3, 3))

a = np.sort(np.random.uniform(0, 1, 625)).reshape(25, 25);

# interpolation 生成方式，cmap=hot 热土
plt.imshow(a, interpolation='nearest', cmap='hot', origin='upper')
# shrink=.92 高度压缩92%
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()
