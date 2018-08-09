import tensorflow as tf

m1 = tf.constant([[3, 3]])

m2 = tf.constant([[2],[2]])

# 点乘 =np.dot(m1,m2)
product = tf.matmul(m1, m2)

with tf.Session() as sess:
    rest = sess.run(product)
    print(rest)
