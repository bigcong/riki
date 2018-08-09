import tensorflow as tf
hello = tf.constant('我日擦!')
sess = tf.Session()
print(sess.run(hello))