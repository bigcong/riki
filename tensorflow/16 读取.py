import numpy as np
import tensorflow as tf

W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")

saver = tf.train.Saver()
with tf.Session() as sess:
    # 提取变量

    saver.restore(sess, "logs/save_net.ckpt")
    print("weights:", sess.run(W))
    print("biases:", sess.run(b))
