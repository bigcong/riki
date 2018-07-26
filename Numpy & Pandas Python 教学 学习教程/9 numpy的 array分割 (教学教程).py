import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)

# 分割 2 块，纵向分割 axis=1 ,相等分割
C = np.split(A, 2, axis=1)
print(C)

# 分成3块，不,相等分割
d = np.array_split(A, 3, axis=1)
print(d)



# 纵向分割

E = np.vsplit(A,3)
print(E)


# 横向分割

F= np.hsplit(A,2)
print(F)




