import numpy as np
import pandas as pd


class q_table():
    def __init__(self):
        self.table = pd.DataFrame(columns=['up', 'down', 'lef', 'right'], dtype=np.float64)

    def choose_action(self, state):
        actions = q_table.loc[state]
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

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.table = self.table.append(
                pd.Series(np.random.rand(len(self.table.columns)), index=self.table.columns, name=state))
