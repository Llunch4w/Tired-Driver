import matplotlib.pyplot as plt
import numpy as np

plt.figure("first")
x = np.linspace(0,20,50) # 将[0,20]分成50份
y1 = 2*x + 1
y2 = x**2 + 1
plt.plot(x,y1)
plt.plot(x,y2,color='#ff4400',linewidth=1,linestyle='--')

plt.figure("second")
plt.scatter(x,y1)

plt.show()