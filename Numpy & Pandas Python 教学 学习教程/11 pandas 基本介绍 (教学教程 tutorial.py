import pandas as pd
import numpy as np

s = pd.Series([1, 2, 4, 5, 67, 3, np.nan])

print(s)
# 生成6天的日期数据
date = pd.date_range('20180101', periods=6);
print(date)

# 生成2行4列数据，0-5之间的数据
ar = np.random.randint(5, size=(6, 4))
print(ar)

# 生成有名称的数据，行为为日期，列为abc
df = pd.DataFrame(ar, index=date, columns=['a', 'b', 'c', 'd'])

print(df)

df = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df)
# 字典转为 pandas
d = {'g': 4, 'gg': 12, 'ggg': pd.Categorical(['a', 'b', 'c', 'd'])}

pp = pd.DataFrame(d)
print(pp)

## 打印类型
print(pp.dtypes)

## 打印index
print(pp.index)

## columns
print(pp.columns)

## 打印valeus
print(pp.values)

## 打印描述
print(df.describe())

## 矩阵反转

print(df.T)

# 排序

print(df.sort_index(axis=1,ascending=False))

print(df.sort_index(axis=0,ascending=False))


print(pp.sort_values(by='ggg',ascending=False))

