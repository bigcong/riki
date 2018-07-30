import numpy as np
import pandas as pd

date = pd.date_range(start='20180101', periods=6);
print(date)

print('------------------------------------------------------------------------')

pf = pd.DataFrame(data=np.arange(0, 24).reshape(6, 4), index=date, columns=['金', '木', '水', '火'])

print(pf)

pf.iloc[0, 1] = 100;
print('------------------------------------------------------------------------')
print(pf)
#
pf.金[pf.金 > 4] = 4
print('------------------------------------------------------------------------')
print(pf)


# 添加一列，不能用pf.土
pf['土']=pd.Series([0,1,2,3,4,5],index=date)


print('------------------------------------------------------------------------')
print(pf)