import numpy as np

a = np.zeros((2,3)) # 全0的(2,3)矩阵
print(a)

b = np.ones((3,4),dtype=np.float32) # 全1的（3,4）矩阵，数据类型为float32
print(b)

c = np.arange(6,20,2) # 生成[6,20)步长为2的序列
print(c)

d = np.linspace(1,20,20) # [1,20]等分成20份
print(d)
d = d.reshape((4,5)) #改变维度成(4,5)
print(d)

