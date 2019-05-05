import tensorflow as tf

# 生成矩阵常量
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                        [2]])

# 矩阵相乘
product = tf.matmul(matrix1,matrix2)

# method1
sess = tf.Session()
result = sess.run(product) #每次run的时候才会执行以下上述结构
print(result)
sess.close()

# method2
# with块可以自动closr Session
with tf.Session as sess:
    result2 = sess.run(product)
    print(result2)
