import pandas as pd
from numpy import *





q = zeros((2, 6))
rewards = zeros((6, 6));
rewards[:, 5] = 500
actions = [[4], [3, 5], [3], [1, 2, 4], [0, 3, 5], [1, 4, 5]]


def trial():
    s = random.randint(6)
    while s < 5:
        s1 = a = random.choice(actions[s])
        q[s, a] = rewards[s, a] + 0.8 * q[s1].max()
        s = s1


for i in range(100):
    trial()


def test(s):
    while s < 5:
        s = q[s].argmax()
        print("->", s)



