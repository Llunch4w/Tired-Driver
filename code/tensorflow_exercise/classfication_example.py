import tensorflow as tf
from tensorflow.example.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)

# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data',one_hot = True)

def add_layer(inputs,in_size,out_size,activation_function=None):
        Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
        biases = tf.Variable(tf.zeros([1,out_size])+0.1)
        Wx_plus_b = tf.matmul(inputs,Weights)+biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result

# define placeholder for inputs to network
xs = tf.placeholder(tf.float32,[None,784])# 不规定有多少个sample，但规定每个sample的大小
ys = tf.placeholder(tf.float32,[None,10])

# add output layer
# tf.nn.softmax适合做分类
prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax)

# the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reducr_sum(ys*tf.log(prediction),
                            reduction_indices=[1])) #loss
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100) # 先学习一部分（前100个）
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_xs})
    if i%50 == 0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))

