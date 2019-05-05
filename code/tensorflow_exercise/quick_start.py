import tensorflow as tf
import numpy as np

# 生成100个0-1范围内数据类型为32位浮点数的数组
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

# ------开始创建tensorflow结构-------

# 生成权重Weights和截距biases
# tf.random_uniform([维度],lower_bound,upper_bound)
# 随机生成[lower_bound,upper_bound]之间数值的变量
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases # 预测函数
loss = tf.reduce_mean(tf.square(y-y_data)) # 损失
optimizer = tf.train.GradientDescentOptimizer(0.5) # 优化器，0.5是学习效率（一般小于1）
train = optimizer.minimize(loss) # 使用优化器不断减小误差

init = tf.global_variables_initializer() # 初始化变量

# ----激活------
sess = tf.Session() # 会话控制，tf.Session()返回值类似于指针
sess.run(init)   # !important
# sess.run(xxx)使当前指针指向这个变量

# ----开始训练-----
steps = 200
for step in range(steps):
    sess.run(train)
    if step%20 == 0:
        print(step,sess.run(Weights),sess.run(biases))