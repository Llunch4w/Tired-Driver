import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(10,16).reshape(2,3)

print(a)
print("a<3",a<3) # 放回一个bool二维数组，表示每个元素是否满足约束条件

c = 10*np.sin(a) # 对a中每个元素都做sin变化
print("sin(a):",c)

print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b) # 元素对应相乘
print("a.dot(b):",a.dot(b.reshape(3,2))) # 矩阵相乘

print("aMax:",np.max(a)) # a所有元素中的最大值
print("aMax_arg:",np.argmax(a)) # a中最大值所在下标
print("aMin:",np.min(a))
print("aMin_arg:",np.argmin(a))
print("aSum:",np.sum(a))
print("aMean:",np.mean(a)) # 求均值
print(a.shape)
print("aMean_col",np.mean(a,axis=0)) # 逐列求均值
print("aMean_row",np.mean(a,axis=1)) # 逐列求均值
print("aMid:",np.median(a)) # 求中位数
print("逐步累加:",np.cumsum(a)) # 逐步累积
print("逐步累减:",np.diff(a)) # 每行逐步累减

print("行列下标：",np.nonzero(a)) # 返回两个数组，一个是所有元素的行下标，一个是所有元素列下标

d = np.arange(14,2,-2).reshape(3,2)
print("未排序：",d)
print("排序后：",np.sort(d)) # 对于每一行来说是有序的

print("矩阵的转置：",a.T)

c = np.arange(4,12)
print(np.clip(c,5,9)) #a中小于5的都为5，大于9的都为9，5和9之间的保持不变