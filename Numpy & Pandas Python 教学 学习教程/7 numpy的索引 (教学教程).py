import numpy as np

A = np.arange(3, 15)  # 默认步长为1
print(A)

A = np.arange(3, 15).reshape(3, 4)
print(A)
print(A[2][1])
print(A[2, 1])
print(A[2, :])  # 第二行所有数
print(A[2, 1:3])  # 第二行所有数,第从什么到什么


for column in A:
    print(column)





for column in A.flat: #3行4列，压缩到一行
    print(column)