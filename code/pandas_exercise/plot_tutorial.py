import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data = data.cumsum()
print(data)
data.plot()
plt.show()

ax = data.plot.scatter(x='A',y='B',color='yellow',label='Class 1')
data.plot.scatter(x='A',y='C',color='green',label='Class 2',ax=ax) #ax=ax使两图在同一坐标轴上显示
plt.show()
