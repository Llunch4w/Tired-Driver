import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
plt.plot(x,y1)
plt.plot(x,y2,color='#ff4400',linewidth=1,linestyle='--')

plt.xlim((-1,2)) # x轴取值范围
plt.ylim((-2,3)) # y轴范围
plt.xlabel('I am X')
plt.ylabel('I am Y')

new_ticks = np.linspace(-3,3,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,0,1,2,3],
        [r'$very\ bad$',r'$bad$',r'$just\ soso$',r'$normal$',r'$good$',r'$perfect$'])

plt.show()