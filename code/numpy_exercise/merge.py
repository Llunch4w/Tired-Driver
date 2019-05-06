import numpy as np

A = np.ones((1,3))
B = 2*np.ones((1,3))

print("A:",A)
print("B:",B)
print("AB上下合并:",np.vstack((A,B)))
print("AB左右合并:",np.hstack((A,B)))

C = np.arange(4)
print("C:",C)
print("add a demension and trans:")
print(C[np.newaxis,:].T)
print(C[:,np.newaxis]) # 与上面语句生成结果相同

D = np.concatenate((A,B,B,A),axis = 0) # 多个array合并
print("D:",D)