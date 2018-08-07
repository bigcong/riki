import tkinter as tk
import numpy as np
import pandas as pd
import time

bb = np.arange(45, 160 - 35, 40)


class CC(tk.Tk, object):
    def __init__(self):
        super(CC, self).__init__()
        self.title('迷宫')
        self.geometry('{0}x{1}'.format(160, 160))
        self._build()

    def _build(self):
        self.canvas = tk.Canvas(self, bg='white', height=160, width=160)
        for c in np.arange(0, 160, 40):
            x0, y0, x1, y1 = c, 0, c, 160
            self.canvas.create_line(x0, y0, x1, y1)

        for c in np.arange(0, 160, 40):
            x0, y0, x1, y1 = 0, c, 160, c
            self.canvas.create_line(x0, y0, x1, y1)

        # 黑色正方形1
        self.blacks = []

        for i in bb:
            x = i
            y = i
            self.canvas.create_rectangle(x, y, x + 30, y + 30, fill='black')
            self.blacks.append([x, y, x + 30, y + 30])

        # self.black_hole4 = self.canvas.create_rectangle(45, 85, 75, 115, fill='black')

        # 黄色圆形
        self.target = self.canvas.create_oval(160 - 35, 160 - 35, 160 - 35 + 30, 160 - 35 + 30, fill='yellow')

        # 移动的红色正方形
        self.red = self.canvas.create_rectangle(5, 5, 35, 35, fill='red')
        self.canvas.pack()

    def get_env_feedback(self, action):
        s = self.canvas.coords(self.red)

        if action == 'right':
            if s[0] < 160 - 40:
                self.canvas.move(self.red, 40, 0)
        elif action == 'left':
            if s[0] - 40 > 0:
                self.canvas.move(self.red, -40, 0)

        elif action == 'up':
            if s[1] > 40:
                self.canvas.move(self.red, 0, -40)
        else:
            if s[1] < 160 - 40:
                self.canvas.move(self.red, 0, 40)

        s_ = self.canvas.coords(self.red);  # 获取移动后的位置

        if s_ == self.canvas.coords(self.target):
            return 1, True, 'end'
        elif s_ in self.blacks:
            return -1, True, 'end'
        elif s_ == s:
            return -1, True, 'end'
        else:
            return 0, False, str(s_)

    def render(self):
        time.sleep(0.1)
        self.update()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.red)
        origin = np.array([20, 20])
        self.red = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        # return observation
        return str(self.canvas.coords(self.red))


def update():
    actions = ['left', 'right', 'up', 'down']
    for t in range(1000):
        print("------------第" + str(t) + "回合-----------")

        s = env.reset()
        RL.check_state_exist(s)

        action = RL.choose_action(s)

        step_counter = 0;
        while True:
            env.render()
            # 选择一个动作

            r, is_end, s_ = env.get_env_feedback(action)
            RL.check_state_exist(s_)

            action_ = RL.choose_action(str(s_))

            RL.learn_sarsa_lamba(s, s_, action, action_, r)
            s = s_
            action = action_
            step_counter = step_counter + 1
            if is_end:
                if r < 0:
                    print("未能找出宝藏")
                    print(RL.table)

                else:
                    print("找出宝藏了")
                break

        print("花费步数:" + str(step_counter))


class q_table():
    def __init__(self):
        self.table = pd.DataFrame(columns=['up', 'down', 'lef', 'right'], dtype=np.float64)
        self.eligibility_trace = self.table.copy()

    def choose_action(self, state):

        actions = self.table.loc[state]
        if np.random.uniform() > 0.1:
            actions = actions.reindex(np.random.permutation(actions.index))
            return actions.idxmax()
        else:
            return np.random.choice(self.table.columns)

    def learn(self, s, s_, action, r):
        q_predict = self.table.loc[s, action]

        if s_ == 'end':
            q_actal = r
        else:
            q_actal = self.table.loc[s_].max() * 0.9 + r

        self.table.loc[s, action] += 0.1 * (q_actal - q_predict)

    def learn_sarsa(self, s, s_, action, action_, r):
        q_predict = self.table.loc[s, action]

        if s_ == 'end':
            q_actal = r
        else:
            q_actal = self.table.loc[s_, action_] * 0.9 + r

        self.table.loc[s, action] += 0.1 * (q_actal - q_predict)

    def learn_sarsa_lamba(self, s, s_, action, action_, r):
        q_predict = self.table.loc[s, action]

        if s_ == 'end':
            q_target = r
        else:
            q_target = self.table.loc[s_, action_] * 0.9 + r

        error = q_target - q_predict

        self.eligibility_trace.loc[s, :] *= 0
        self.eligibility_trace.loc[s, action] = 1

        self.table += 0.1 * error * self.eligibility_trace
        self.eligibility_trace *= 0.9 * 0.9

    def check_state_exist(self, state):

        if state not in self.table.index:
            # append new state to q table
            self.table = self.table.append(
                pd.Series(np.zeros(len(self.table.columns)), index=self.table.columns, name=state))
            self.eligibility_trace = self.eligibility_trace.append(
                pd.Series(np.zeros(len(self.table.columns)), index=self.table.columns, name=state))


if __name__ == '__main__':
    env = CC()
    RL = q_table()
    env.after(100, update)
    env.mainloop()
