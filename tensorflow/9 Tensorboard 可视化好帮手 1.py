import tensorflow as tf
import numpy as np


# input 输入 in_size 输入大小  out_size 输出大小  activation_funciton 激励函数




def add_layer(inputs, in_size, out_size, activation_function=None):
    # 定一个矩阵in_size*out_size
    Weight = tf.Variable(tf.random_uniform([in_size, out_size]))
    # 定一个矩阵1*out_size 都是0.1 的矩阵
    Biase = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    Wx = tf.matmul(inputs, Weight) + Biase
    if activation_function is None:
        # 线性方程
        return Wx
    else:
        return activation_function(Wx)


def add_layer1(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300, dtype=np.float32).reshape(300, 1)
noise = np.random.normal(0, 0.05, x_data.shape)

y_data = x_data ** 2 - 0.5 + noise

# np.square 是平方


# tf.nn.relu  是激励方程

with tf.name_scope('shuru'):
    xs = tf.placeholder(tf.float32, [None, 1])
    ys = tf.placeholder(tf.float32, [None, 1])

ll = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

prediction = add_layer(ll, 10, 1, activation_function=None)

#  reduction_indices = [1] 横向压扁数组求和， reduction_indices =[0] 竖向压扁数组求和
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))

# 0.1 的效率 使loss 慢慢减小
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter("logs/", sess.graph)

    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})

        if i % 50 == 0:
            print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
