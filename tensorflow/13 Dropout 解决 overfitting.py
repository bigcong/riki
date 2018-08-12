import tensorflow as tf
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer

digits = load_digits()
X = digits.data
# 将0 变成 [1 0 0 0 0 0 0 0 0 0]数组
# 1 变成 [ 0 1 0 0 0 0 0 0 0 0]
y = LabelBinarizer().fit_transform(digits.target)

input_x = tf.placeholder(tf.float32, [None, 64])
input_y = tf.placeholder(tf.float32, [None, 10])
# 保持多少数据，防止overfiting
keep_prob = tf.placeholder(tf.float32)


# input 输入 in_size 输入大小  out_size 输出大小  activation_funciton 激励函数
def add_layer(inputs, in_size, out_size, activation_function=None):
    # 定一个矩阵in_size*out_size
    Weight = tf.Variable(tf.random_uniform([in_size, out_size]))
    # 定一个矩阵1*out_size 都是0.1 的矩阵
    Biase = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    Wx = tf.matmul(inputs, Weight) + Biase
    Wx = tf.nn.dropout(Wx, keep_prob)

    if activation_function is None:
        # 线性方程
        output = Wx
    else:
        output = activation_function(Wx)
    tf.summary.histogram('/outputs', output)
    return output


l1 = add_layer(input_x, 64, 50, activation_function=tf.nn.tanh)

output_y = add_layer(l1, 50, 10, activation_function=tf.nn.softmax)

cross_entroy = tf.reduce_mean(-tf.reduce_sum(input_y * tf.log(output_y), reduction_indices=[1]))
tf.summary.scalar('loss', cross_entroy)

train_setp = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entroy)

with tf.Session() as sess:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    merged = tf.summary.merge_all()

    train_writer = tf.summary.FileWriter("logs/train", sess.graph)
    test_writer = tf.summary.FileWriter("logs/test", sess.graph)

    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(500):
        sess.run(train_setp, feed_dict={input_x: X_train, input_y: y_train, keep_prob: 1})
        if i % 50 == 0:
            train_result = sess.run(merged, feed_dict={input_x: X_train, input_y: y_train, keep_prob: 1})
            test_result = sess.run(merged, feed_dict={input_x: X_test, input_y: y_test, keep_prob: 1})
            train_writer.add_summary(train_result, i)
            test_writer.add_summary(test_result, i)
