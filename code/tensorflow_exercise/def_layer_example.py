import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 增加一层神经层
# 输入，输入层神经元个数，该层神经元个数，激励函数（若无激励函数则为线性函数关系）
def add_layer(inputs,in_size,out_size,n_layer,activation_function=None):
    layer_name = 'layer%s'%n_layer
    # 生成一个in_size行，out_size列的随机矩阵
    with tf.name_scope('layer'): # 为输出log文件作准备
        with tf.name_scope('weight'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
            tf.summary.histogram(layer_name+'/weights',Weights) #观看学习过程中W的变化
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size])+0.1)
            tf.summary.histogram(layer_name+'/biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs,Weights)+biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs',outputs)
        return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis] # -1,1等分成300份，且返回为列向量
noise = np.random.normal(0,0.05,x_data.shape) # 噪声，参数列表（均值，方差，大小）
y_data = np.square(x_data)-0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input') 
    #1表示输入只有一个
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

l1 = add_layer(xs,1,10,n_layer=1,activation_function=tf.nn.relu) # 输出层到隐藏层
prediction = add_layer(l1,10,1,n_layer=2,activation_function=None) # 隐藏层到输出层

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.square(ys-prediction))
    tf.summary.scalar('loss',loss) # 观看loss和观察别的变量有些不一样

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

sess = tf.Session()
merged = tf.summary.merge_all() # summary合并
writer = tf.summary.FileWriter("logs/",sess.graph)
# 运行 tensorboard --logdir=logs/
# 然后浏览器访问localhost:6006

sess.run(tf.global_variables_initializer())

# 可视化操作
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion() # 程序在show了之后不暂停继续进行
plt.show()

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50 == 0:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result,i)
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        prediction_value = sess.run(prediction,feed_dict={xs:x_data})
        try:
            ax.lines.remove(lines[0]) # 去除lines的第一个
        except Exception:
            pass
        # 可视化操作
        lines = ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(0.2)