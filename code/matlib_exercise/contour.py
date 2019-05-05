import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y) #把x,y绑定成网格值

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)#8+2份，alpha为透明度，cmap为图色标

C = plt.contour(X,Y,f(X,Y),8,colors='black') # 画线,与上面函数有f的区别
plt.clabel(C,inline='True',fontsize=10) #inline表示是否穿过线

plt.show()