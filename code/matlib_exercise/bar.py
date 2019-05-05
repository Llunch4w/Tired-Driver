import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n) #生成[0,n-1]
# np.arange(a,b,step)生成[a,b)按步长step增加的序列
y1 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)#uniform表示均匀分布
y2 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(x,y1,facecolor='#9999ff',edgecolor='white')
plt.bar(x,-y2,facecolor='#ff9999',edgecolor='white')

for i,j in zip(x,y1):
    plt.text(i,j+0.05,'%.2f'%j,ha='center',va='bottom')# 后面两个参数为水平对齐方式和垂直对齐方式

for i,j in zip(x,y2):
    plt.text(i,-j-0.1,'%.2f'%j,ha='center',va='bottom')

plt.show()