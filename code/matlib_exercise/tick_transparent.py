import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(-1,2,50)
y = 2*x + 1
plt.plot(x,y)

ax = plt.gca()

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='blue',edgecolor='None',alpha=0.7))# alpha是透明度

plt.show()