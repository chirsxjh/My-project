#-*-coding:utf-8-*-
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv('/home/xiang/mygit/学习记录和随笔/AI/james.csv')

sho = data['shoot']
sco = data['score']


X_test = sho[0:20].reshape(-1,1)
y_test = sco[0:5]
X_train = sho[20:].reshape(-1,1)
y_train = sco[20:]

x=tf.placeholder(tf.float32,[None,1])
#设置斜率(权重值)W变量
W=tf.Variable(tf.zeros([1,1]))
#设置截距(偏置量)b变量
b=tf.Variable(tf.zeros([1]

y = tf.multiply(x,W)+b

#设置占位符用于输入实际的y值
y_=tf.placeholder(tf.float32,[None,1])

#设置成本函数(最小方差)
cost=tf.reduce_sum(tf.pow((y_-y),2))
#使用梯度下降，以0.000001的学习速率最小化成本函数cost，以获得W和b的值
train_step=tf.train.GradientDescentOptimizer(0.000001).minimize(cost)

#开始训练前对变量进行初始化 
init=tf.global_variables_initializer() 
#创建一个会话(Sess) 
sess=tf.Session() 
#在Sess中启用模型并初始化变量
sess.run(init)

cost_history=[]

#循环训练模型100次 
for i in range(100): 
    feed={x:X_train,y_:y_train} 
    sess.run(train_step,feed_dict=feed) 
    cost_history.append(sess.run(cost,feed_dict=feed)) 
    print("After %d iteration:" %i) 
    print("W: %f" % sess.run(W)) print("b: %f" % sess.run(b))
    print("cost: %f" % sess.run(cost,feed_dict=feed))
    print("W_Value: %f" % sess.run(W),"b_Value: %f" % sess.run(b),"cost_Value: %f" % sess.run(cost,feed_dict=feed))
