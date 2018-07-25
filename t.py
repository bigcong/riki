import numpy as np
from numpy.random import random

q = np.zeros((6, 2))
rewards = np.zeros((6, 2));

rewards[:, 1] = 1
rewards[:, 0] = -1
print(q)
print(rewards)

def action(index=1):
    np.random(1)

