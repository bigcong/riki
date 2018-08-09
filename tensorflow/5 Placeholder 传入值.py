import numpy as np
import tensorflow as tf

# 定义数据类型和结构
input1 = tf.placeholder(tf.float32, [2, 2]);
# 定义数据类型和结构
input2 = tf.placeholder(tf.float32, [2, 2]);

out = tf.multiply(input1, input2)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    a = sess.run(out, feed_dict={input2: np.random.rand(4).reshape(2,2), input1:  np.random.rand(4).reshape(2,2)})
    print(a)
