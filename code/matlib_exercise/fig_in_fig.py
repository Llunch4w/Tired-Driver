import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.arange(1,8)
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_title('figure1')

left,bottom,width,height = 0.2,0.5,0.3,0.3
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b')
ax2.set_title('figure2')

left,bottom,width,height = 0.6,0.2,0.2,0.2
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y[::-1],x,'g') # y值逆序
ax2.set_title('figure3')

plt.show()