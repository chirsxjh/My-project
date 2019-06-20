#-*-coding:utf-8-*-
import tensorflow as tf
import numpy as np
import pandas as pd

sess = tf.Session()

data = pd.read_csv('/home/xiang/mygit/学习记录和随笔/AI/james.csv')
#print data['shoot']
# 线性模型 y=bx+a
def model(x, b, a):
    return tf.multiply(x, b) + a


# 归一化函数
def normalize(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    arr_out = []
    for item in arr:
        out = np.divide(np.subtract(item, arr_min), np.subtract(arr_max, arr_min))
        arr_out = np.append(arr_out, np.array(out))
    return arr_out

# 原始数据
trX_i = data['shoot']

trY_i = data['score']
# 数据归一化
# 数据归一化
trX = normalize(trX_i)
trY = normalize(trY_i)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# 设一个权重变量b，和一个偏差变量a
b = tf.Variable(0.0, name="weights")
# create a variable for biases
a = tf.Variable(0.0, name="biases")
y_model = model(X, b, a)

# 损失函数
loss = tf.multiply(tf.square(Y - y_model), 0.5)

# 梯度下降
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init = tf.global_variables_initializer()
sess.run(init)

# 训练数据
for i in range(500):
    for (x, y) in zip(trX, trY):
        output = sess.run(train_op, feed_dict={X: x, Y: y})

print('b:' + str(sess.run(b)) + ' || a:' + str(sess.run(a)))

