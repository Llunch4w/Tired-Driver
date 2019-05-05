import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-1,2,50)
y1 = 2*x + 1
y2 = x**2 + 1

l1, = plt.plot(x,y1,color='blue',label='up')
l2, = plt.plot(x,y2,color='red',label='down')

plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')
# loc='best'会自动寻找数据比较少的地方放置legend

plt.show()