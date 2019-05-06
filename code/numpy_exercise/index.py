import numpy as np

A = np.arange(3,15).reshape((3,4))
print("A:",A)
print("A[2]:",A[2]) # 输出index=2的那一行
print("A[2,:]",A[2,:]) # 第二行的所有数
print("A[2][1]",A[2][1]) # 输出A(2,1)
print("A[2,1]",A[2,1]) # 输出A(2,1)

print("打印每一行")
for row in A:
    print(row)

print("打印每一列")
for col in A.T:
    print(col)

print("迭代每一个")
for item in A.flat:
    print(item,end=' ')