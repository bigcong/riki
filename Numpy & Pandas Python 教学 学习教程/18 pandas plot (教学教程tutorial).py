import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt


data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum();
print(data)






#  np.random.randn(1000,4) 生成4*1000的数据 线
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('abcd'))
data=data.cumsum()
data.plot()
plt.show()




# 点

ax=data.plot.scatter(x='a',y='b',color='red',label='ab')

data.plot.scatter(x='c',y='d',color='blue',label='cd',ax=ax)
plt.show()




