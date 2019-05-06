import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df)
print("-------------------")

print(df['A'])
print(df[0:3],df['20130103':'20130104'])
print("-------------------")

print(df.loc['20130102'])
print(df.loc['20130102',['A','B']])
print("-------------------")

print(df.iloc[3]) # 第三行
print(df.iloc[3,1]) #第三行第一列
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3]) #不连续的筛选
print("-------------------")

print(df.ix[:3,['A','C']])
print("-------------------")

print(df[df.A>8])
print("-------------------")