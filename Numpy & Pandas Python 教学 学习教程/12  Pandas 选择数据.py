import pandas as pd
import numpy as np

date = pd.date_range(start='20180101', periods=3)

df = pd.DataFrame(data=np.arange(12).reshape((3, 4)), index=date, columns=['a', 'b', 'c', 'd'])

print(df)
print("-----------")
print(df['a'], df.b)

print("*********")

# 切片选择
print(df[0:2])
print(df['20180101':'20180102'])

# 根据标签选择
print("******************************************************")

print(df.loc['20180101'])

print("******************************************************")

print(df.loc['20180101', ['a', 'b']])

# 通过位置选择
print(df.iloc[0, 0])
print(df.iloc[[0, 1], [0, 1]])
print("******************************************************")

# 混合筛选
print(df.ix[:3, ['a', 'b']])
print("******************************************************")

# 通过条件筛选
print(df[df.a <2])
