import pandas as pd

date = pd.read_csv('/Users/cong/Downloads/1.csv')

# print(date)

for i,d in enumerate(date.columns.values):
    date.columns.values[i]=d.strip();


#### 保存到中文乱吗问题

date.to_csv(path_or_buf='/Users/cong/Downloads/2.csv',index=False,encoding='utf_8_sig')

date.to_sql(path_or_buf='/Users/cong/Downloads/2.sql',index=False,encoding='utf_8_sig')
