
## Tensorboard 使用小结

### 介绍

为了方便调试参数以及调整网络结构，我们需要将计算图可视化出来，以便能够更好的进行下一步的决策。Tensorflow提供了一个TensorBoard工具，可以满足上面的需求。TensorBoard是一个可视化工具，能够有效地展示Tensorflow在运行过程中的计算图、各种指标随着时间的变化趋势以及训练中使用到的数据信息。可以查看TensorBoard Github ReadMe 详细阅读适应方法。

### 使用方法

为了观察所建立的计算图，我们可以简单的在前面的代码中加入一句：

```python

train_writer = tf.summary.FileWriter("logdir", sess.graph)
```



sess.graph就是我们所描绘的计算图，“logdir”是log的存储的文件夹。在shell中运行TensorBoard，日志目录就是刚才我们所保存的目录，就可以直接用浏览器访问了(由于TensorFlow问题，这里网址应该是localhost)：
使用方法：先在终端中运行python文件，然后在运行如下命令：
**在浏览器中显示运行命令：tensorboard --logdir /tmp/tensorflow***

### 例子

**矩阵相乘**

```python
tfboard1.pyimport tensorflow as tf
with tf.name_scope('graph') as scope:
    matrix1 = tf.constant([[3., 3.]], name = 'matrix')   # 一行两列
    matrix2 = tf.constant([[2.], [2.]], name = 'matrix2') # 两行一列
    product = tf.matmul(matrix1, matrix2, name = 'product')

sess = tf.Session()

writer = tf.summary.FileWriter("logs1/", sess.graph)

init = tf.global_variables_initializer()

sess.run(init)
```

****

tf.name_scope函数是作用域名，上述代码斯即在graph作用域op下，又有三个op（分别是matrix1，matrix2，product),用tf函数内部的name参数命名，这样会在tensorboard中显示。运行上述代码后，在项目所在目录会生成"logs1"目录（可以自定义名字），然后在命令行运行：
***tensorboard --logdir logs1***
即可在本机6006端口调用TensorBoard。可以通过浏览器打开使用。

### 可视化内容
可视化内容包括：

Event：训练过程中的统计数据，主要包括 Loss、Accuracy等

Image：记录的图像数据

Graphs：网络结构图

Audio：记录的音频数据

Histogram：直方图描述的统计结果




