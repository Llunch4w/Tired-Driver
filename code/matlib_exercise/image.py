import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(0,1,9).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper') #图片本质是矩阵
# interpolation是插值方法
plt.colorbar() #添加colorbar

plt.xticks(())
plt.yticks(())
plt.show()