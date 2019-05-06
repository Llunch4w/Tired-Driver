import numpy as np

# 浅拷贝
a = np.arange(4)
b = a # b实际上就是a
print("a1:",a)
b[0] = 10
print("a1:",a)

# 深拷贝
b = a.copy()
print("a2:",a)
b[2] = 8
print("a2:",a)
print("b:",b)