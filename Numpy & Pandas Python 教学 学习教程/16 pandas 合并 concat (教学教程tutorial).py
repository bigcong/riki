import numpy as np
import pandas as pd

c = ['a', 'b', 'c', 'd']
df1 = pd.DataFrame(data=np.ones((3, 4)) * 0, columns=c)
df2 = pd.DataFrame(data=np.ones((3, 4)) * 1, columns=c)

df3 = pd.DataFrame(data=np.ones((3, 4)) * 2, columns=c)

print(df1)
print(df2)
print(df3)
# 三个竖向合并,ignore_index =True,重新排序


df4 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(df4)

# join ，['inner','outer']


df5 = pd.DataFrame(data=np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df6 = pd.DataFrame(data=np.ones((3, 4)) * 1, columns=['x', 'b', 'c', 'd'], index=[2, 3, 4])

# 默认合并为outer
df7 = pd.concat([df5, df6], join='inner', ignore_index=True)
print(df7)

# join_axes 合并时候只考虑某个index
df8 = pd.concat([df5, df6], axis=1, join_axes=[df5.index])
print(df8)

# append  Series

df9 = df1.append(df2, ignore_index=True)
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(s1)
print(df5)
res = df1.append(s1, ignore_index=True)
print(res)
