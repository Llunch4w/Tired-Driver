import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x)) #末尾的,很重要

def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line

def init():
    line.set_ydata(np.sin(x))
    return line

ani = animation.FuncAnimation(fig=fig,func=animate,frames=1000,init_func=init,interval=20,blit=False)
# func变化函数，init_func初始状态，interval频率，frame一次循环帧数,blit是否只更新变化了的点
plt.show()