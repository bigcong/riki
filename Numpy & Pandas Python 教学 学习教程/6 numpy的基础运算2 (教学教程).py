import numpy as np

A = np.arange(2, 14).reshape(3, 4)
print(A)
print(np.mean(A))  # 平均值
print(np.median(A))  # 中位数
print(np.median(A))  # 中位数

print(np.diff(A))  # 累差
print(np.nonzero(A))  # 非零

print(np.sort(A))  # 排序
#print(np.transpose(A))  # 反向=print(A.T)

print((A.T).dot(A))  #乘法


print(np.clip(A,5,9))#小于5，等于5 大于9 等于9

print(np.mean(A,axis=0))#列平均值
print(np.mean(A,axis=1))#行平均值