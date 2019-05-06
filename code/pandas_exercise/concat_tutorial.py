import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print("df1:",df1)
print("df2:",df2)
print("df3:",df3)

res = pd.concat([df1,df2,df3],axis = 0)
print("res:",res)

print("-----------------")
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print("df1:",df1)
print("df2:",df2)

res = pd.concat([df1,df2],join='outer',ignore_index=True) #不同的列用NAN填充
print("res:",res)

print("----------------------")
res = pd.concat([df1,df2],join='inner') #不同的列去掉
print("res:",res)

print("----------------------")
res = pd.concat([df1,df2],axis = 1,join_axes=[df1.index])
print("res:",res)

print("----------------------")
res = df1.append(df2)
print(res)

print("----------------------")
res = df1.append([df2,df3])
print(res)



