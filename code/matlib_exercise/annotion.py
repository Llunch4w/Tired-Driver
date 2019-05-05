import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-1,2,50)
y = 2*x + 1
plt.plot(x,y)

x0 = 1
y0 = 2*x0 + 1
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
plt.scatter(x0,y0,color='blue')
plt.plot([x0,x0],[y0,0],lw=2.5,linestyle='--') #绘制(x0,y0)到(x0,0)的直线

# method1
###############
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
        fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
# xy=(x0,y0)是基准，xytext是相对于基准移动的距离


#method2
########################
plt.text(-1,2,r'$this\ is\ \alpha$',fontdict={'size':16,'color':'r'})
# 前两个参数表示字符串起点坐标为(-1,2)
plt.show()
