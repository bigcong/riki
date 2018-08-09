import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.collections import PathCollection

fig, ax = plt.subplots()

x = np.random.rand(100)
y = 0.3 * x + 0.1

Weight = tf.Variable(tf.random_uniform([1], -100, 100))
Baise = tf.Variable(tf.random_uniform([1], -100, 100))

y_target = x * Weight + Baise




loss = tf.reduce_mean(tf.square(y - y_target))

# 0.5 是学习效率，通过梯度下降法，是loss 越来越小
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

plt.figure()
line, = plt.plot(x, y)

with tf.Session() as sess:
    sess.run(init)  # 初始化变量
    for step in range(200):
        sess.run(train)
        w = sess.run(Weight);
        b = sess.run(Baise)
        print(w,b)
