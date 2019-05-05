import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(0,1,n) # 产生n个随机数，范围均在[0,1]
y = np.random.normal(0,1,n)
T = np.arctan2(y,x) # for color

plt.scatter(x,y,s=75,c=T,alpha=0.5)#最后三个参数是大小，颜色，透明度

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(()) #去除x轴刻度
plt.yticks(())

plt.show()
