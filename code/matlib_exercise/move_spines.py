import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-3,3,50)
y = x**2
plt.plot(x,y)

plt.xlim((-3,3))
plt.ylim((-1,10))

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none') # 右边框消失
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom') # 将x轴和底边框绑定
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1)) # bottom绑定的x轴通过y=-1
ax.spines['left'].set_position(('data',0)) # left绑定的y轴通过x=0

plt.show()