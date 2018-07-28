import numpy as np
import  pandas as pd

dates=pd.date_range(start='20180101',periods=6);

print(dates)


df=pd.DataFrame(data=np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
df.iloc[0,1]=np.nan
df.iloc[1,1]=np.nan
print(df)
# 删除行,存在nan就是删除
print(df.dropna(axis=0,how='any'))#how=all 此行当中都是nan就删除

# nan 替换成0
print(df.fillna(value=0))


# 是不是存在nna
print(df.isnull());


print(np.any(df.isnull()==True));


