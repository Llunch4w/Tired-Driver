import tensorflow as tf

# tensorflow中变量必须按如下述这样显示声明（name不必要）
state = tf.Variable(0,name='counter') 
one = tf.constant(1) # 声明常量


new_value = tf.add(state,one)
# 把new_value的值加载到state上
update = tf.assign(state,new_value)
init = tf.global_variables_initializer() # must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))