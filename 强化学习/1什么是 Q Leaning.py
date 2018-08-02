import numpy as np
import pandas as pd

q_table = pd.DataFrame(data=np.random.rand(10).reshape((5, 2)), columns=['left', 'right'])

print(q_table)


# 选择动作


def choose_action(status):
    rand = np.random.uniform()
    actions = q_table.iloc[status, :]
    if rand < 0.1:  # 随机选择一个
        return np.random.choice(q_table.columns)
    else:
        # 返回最大数的索引
        return actions.idxmax()


