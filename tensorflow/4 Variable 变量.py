import numpy as np
import tensorflow as tf

a = tf.Variable(0, name='counter')
one = tf.constant(1)

b = np.add(a, one)

update = tf.assign(a, b)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(10):
        sess.run(update)
        print(sess.run(a))
