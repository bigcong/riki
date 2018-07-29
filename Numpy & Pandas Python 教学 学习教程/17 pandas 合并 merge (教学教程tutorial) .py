import numpy as np
import pandas as pd

left = pd.DataFrame({
    'key1': ['k1','k2', 'k3', 'k4'],
    'key2': ['k1','k2', 'k3', 'k433'],
    'key3': ['k1','k2', 'k3', 'k4'],
    'key4': ['k1', 'k2', 'k3', 'k334']

})
print(left)

right = pd.DataFrame({
    'key3': ['k1','k2', 'k3', 'k4'],
    'key4': ['k1','k2', 'k3', 'k4'],
    'key5': ['k1','k2', 'k3', 'k4'],
    'key6': ['k331', 'k3332', 'k3', 'k4']

})
print(right)
re = pd.merge(left, right, on='key3')
print(re)



print(right)

### 根据多行合并  how=['left','right','outer','inner']
re = pd.merge(left, right, on=['key3','key4'],how='right')
print(re)


re = pd.merge(left, right, on=['key3','key4'],how='right',indicator=True)

print(re)


# merged by index
re = pd.merge(left, right, on=['key3','key4'],how='right',indicator=True)
