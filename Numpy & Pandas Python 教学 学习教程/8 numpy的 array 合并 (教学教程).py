import numpy as np

A = np.array([1, 1, 1]);
B = np.array([2, 2, 2]);

print(np.vstack((A, B)))  # 上下合并
C = np.vstack((A, B))

print(A.shape, C.shape)

D = np.hstack((A, B))  # 左右合并
print(D)

# 改变纬度,增加一个纬度
G = A[:, np.newaxis];
print(G)
print(G.shape)

# 改变纬度,增加一个纬度
F = B[:, np.newaxis];
print(F)
print(F.shape)

print(np.hstack((G, F)))

# 多个array合并，axis=0 纵向合并，axis=1 横向合并
X = np.concatenate((G, F, F, G),axis=1);
print(X)


# 多个array合并，axis=0 纵向合并，axis=1 横向合并
Y = np.concatenate((G, F, F, G),axis=0);
print(Y)
