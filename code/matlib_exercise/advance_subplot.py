import matplotlib.pyplot as plt
import numpy as np

plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1) 
# (3,3)网格布局，从0行0列开始，列跨度为3，行跨度为1
ax1.plot([1,2],[1,2])
ax1.set_title('1')


ax1 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1) 
ax1.plot([1,2],[1,2])
ax1.set_title('2')

ax1 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2) 
ax1.plot([1,2],[1,2])
ax1.set_title('3')

ax1 = plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1) 
ax1.plot([1,2],[1,2])
ax1.set_title('4')

ax1 = plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1) 
ax1.plot([1,2],[1,2])
ax1.set_title('5')

plt.show()