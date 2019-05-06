import numpy as np

A = np.arange(12).reshape(4,3)
print("A:",A)

# 等大小分割
print(np.split(A,3,axis=1)) # 把列分成3块
print(np.hsplit(A,3))

print(np.split(A,2,axis=0)) # 把行分成2块
print(np.vsplit(A,2))


# 不等大小分割
print(np.array_split(A,3,axis=0))
