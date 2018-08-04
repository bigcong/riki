import time

import numpy as np

import pandas as pd

q_table = pd.DataFrame(np.random.rand(24).reshape(8, 3), columns=['left', 'right', 'stay'])
print(q_table)


# 随机选择一个动作，90% 几率选择Q_table 这一行的最大值
def choose_action(index):
    actions = q_table.iloc[index]  # 获取这一行的数据
    rd = np.random.uniform()  # 随机数
    if rd > 0.1:
        return actions.idxmax()
    else:
        return np.random.choice(q_table.columns)


def get_env_feedback(index, aciton):
    if aciton == 'right':
        if index >= len(q_table.index) - 2:  # 到最后一行了
            return 'end', 1
        else:
            return index + 1, 1

    elif aciton == 'left':
        if index == 0:  # 到达第一行了
            return index, -1
        else:
            return index - 1, -1
    else:
        return index, 0;


def update_env(next, index):
    # This is how environment be updated
    env_list = ['-'] * (len(q_table.index) - 1) + ['T']  # '---------T' our environment
    if next == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[index] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(0.3)


if __name__ == '__main__':

    for episode in range(8):

        print("------------第" + str(episode) + "回合-----------")
        is_end = False;  # 是否结束本回合
        now = 0;  # 当前位置
        step_counter = 0;  # 这个回合已经走了多少步
        while not is_end:
            A = choose_action(now)
            next, r = get_env_feedback(now, A)  # 获取环境的反馈
            env_list = ['_'] * (len(q_table.index) - 1) + ['🏁']

            env_list[now] = '狗'
            interaction = ''.join(env_list)
            print('\r{}'.format(interaction), end='')
            time.sleep(0.1)

            q_pridict = q_table.loc[now, A]  # 获取表中的数据，预测值

            q_actal = 0;
            if next != 'end':
                q_actal = q_table.loc[next].max() * 0.8 + r  # 获取下一步此行中最大的值(0.9 是衰减值)+（当前的奖励，可能为0，1）
            else:  # 回合结束了
                is_end = True;  # 死循环结束
                q_actal = r  # 不存在下一个了， 实际得到值只有r

            q_table.loc[now, A] = 0.1 * (q_actal - q_pridict)  # 0.1 是学习效率，
            now = next;  # 当前位置改变
            step_counter = step_counter + 1
        print("\r花费步数:" + str(step_counter))

    print(q_table)
