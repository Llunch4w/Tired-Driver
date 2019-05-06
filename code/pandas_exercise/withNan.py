import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[0,1] = np.nan #iloc->index location
df.iloc[1,2] = np.nan
print(df)
print("----------------")

df2 = df.copy()
print(df2.dropna(axis=0,how='any')) #如果某一行有任意一个nan，就把这一行都扔掉,how还可取'all'
print("----------------")

df2 = df.copy()
print(df2.fillna(value=0)) #将nan替换成value
print("----------------")

df2 = df.copy()
print(df.isnull()) #每个元素是否丢失bool值
print("----------------")

df2 = df.copy()
print(np.any(df2.isnull()) == True) #df2中是否有非null值
print("----------------")