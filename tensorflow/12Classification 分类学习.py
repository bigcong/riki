from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt;
import numpy as np
import tensorflow as tf

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# plt.figure()
# 两行两列

# for i in range(10):
# plt.subplot(2, 5, i + 1)
# plt.imshow(mnist.train.images[i].reshape(28, 28))
# plt.show()


input_x = tf.placeholder(tf.float32, [None, 784])
input_y = tf.placeholder(tf.float32, [None, 10])


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


output_y = add_layer(input_x, 784, 10, activation_function=tf.nn.softmax)

##  reduction_indices = [1] 横向压扁数组求和， reduction_indices =[0] 竖向压扁数组求和
# 选用交叉熵函数。交叉熵用来衡量预测值和真实值的相似程度，如果完全相同，它们的交叉熵等于零
# reduce_sum 求和，# reduce_mean 求平均值

cross_entropy = tf.reduce_mean(-tf.reduce_sum(input_y * tf.log(output_y), reduction_indices=[1]))

with tf.name_scope('loss'):
    loss = cross_entropy
    tf.summary.scalar('loss', loss)

train_setp = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy);

init = tf.global_variables_initializer()

merged = tf.summary.merge_all()

with  tf.Session() as sess:
    writer = tf.summary.FileWriter("logs/", sess.graph)

    sess.run(init)

    right_counter = 0
    for i in range(1000):
        batch_x, batch_y = mnist.train.next_batch(100)

        p = sess.run(train_setp, feed_dict={input_x: batch_x, input_y: batch_y})

        p_y = sess.run(output_y, feed_dict={input_x: batch_x, input_y: batch_y})

        equals = np.equal(np.argmax(p_y, 1), np.argmax(batch_y, 1));

        right_counter = right_counter + np.sum(equals == True)
        print(right_counter / (100 * (i + 1)))

        if i % 50 == 0:
            rs = sess.run(merged, feed_dict={input_x: batch_x, input_y: batch_y})
            writer.add_summary(rs, i)
