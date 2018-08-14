import numpy as np
import tensorflow as tf


class DeepQNetwork:
    def __init__(
            self,
            e_greedy_increment=None):
        self.n_actions = 4  # 有多少决策行为
        self.n_features = 2  #
        self.lr = 0.01  # 学习效率
        self.gamma = 0.9  # 奖励衰减效率
        self.epsilon_max = 0.9  # 学习贪婪度
        self.replace_target_iter = 300
        self.memory_size = 500  # 存储记忆大小
        self.batch_size = 32  # 训练批次
        self.epsilon_increment = e_greedy_increment  # 学习贪婪度增加效率
        self.epsilon = 0 if e_greedy_increment is not None else self.epsilon_max

        # total learning step
        self.learn_step_counter = 0  # 学习步数，计步器

        # initialize zero memory [s, a, r, s_]
        self.memory = np.zeros((self.memory_size, 6))

        # consist of [target_net, evaluate_net]
        self._build_net()

        t_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='target_net')
        e_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='eval_net')

        with tf.variable_scope('soft_replacement'):
            self.target_replace_op = [tf.assign(t, e) for t, e in zip(t_params, e_params)]

        self.sess = tf.Session()

        self.sess.run(tf.global_variables_initializer())

        # 记录每一步的误差
        self.cost_his = []

    def _build_net(self):
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # 当前坐标
        self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')  # 下一个坐标
        self.r = tf.placeholder(tf.float32, [None, ], name='r')  # 奖励
        self.a = tf.placeholder(tf.int32, [None, ], name='a')  # 行为
        # 权重 和偏执
        w_initializer, b_initializer = tf.random_normal_initializer(0., 0.3), tf.constant_initializer(0.1)

        # ----------对预测值的处理--------

        """"
        inputs: 该层的输入
        units: 输出的大小（维数），整数或long
        activation: 使用什么激活函数（神经网络的非线性层），默认为None，不使用激活函数
        use_bias: 使用bias为True（默认使用），不用bias改成False即可
        """
        # 相当于添加一个层，即初学的add_layer()函数
        e1 = tf.layers.dense(self.s, 20, tf.nn.relu, kernel_initializer=w_initializer,
                             bias_initializer=b_initializer, name='e1')
        # 添加一个输出层，没有使用激励函数,输出为n_actions 类型的数据
        # 预测值 　
        self.q_eval = tf.layers.dense(e1, self.n_actions, kernel_initializer=w_initializer,
                                      bias_initializer=b_initializer, name='q_eval')

        # ----------对实际值处理--------
        t1 = tf.layers.dense(self.s_, 20, tf.nn.relu, ernel_initializer=w_initializer,
                             bias_initializer=b_initializer, name='t1')

        self.q_next = tf.layers.dense(t1, self.n_actions, kernel_initializer=w_initializer,
                                      bias_initializer=b_initializer, name='t2')

        # 奖励+衰减值*（下一个状态这一行的对应的q值最大一个）
        q_target = self.r + self.gamma * tf.reduce_max(self.q_next, axis=1, name='q_max')  # shape=(None, )

        self.q_target = tf.stop_gradient(q_target)

    # 存储tran
    def store_transition(self, s, a, r, s_):
        # s 当前状态  a 动作  r 奖励  s_ 下个状态
        # 判断一个对象是否包含某个属性
        if not hasattr(self, 'memory_counter'):
            self.memory_counter = 0

        transition = np.hstack((s, [a, r], s_))
        # replace the old memory with new memory

        # 一直在更新替换这500个数
        index = self.memory_counter % 500
        self.memory[index, :] = transition
        # 计数器增加1
        self.memory_counter += 1

    def choose_action(self, observation):
        # to have batch dimension when feed into tf placeholder
        observation = observation[np.newaxis, :]  # 变成了2维数组

        if np.random.uniform() < self.epsilon:
            # forward feed the observation and get q value for every actions
            actions_value = self.sess.run(self.q_eval, feed_dict={self.s: observation})
            action = np.argmax(actions_value)
        else:
            action = np.random.randint(0, self.n_actions)
        return action


if __name__ == '__main__':
    observation = np.random.randn(4)
    s = observation[np.newaxis, :]
    print(s.shape)
