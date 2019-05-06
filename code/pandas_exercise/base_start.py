import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1]) # 生成一个有索引的序列
print(s)

dates = pd.date_range('20160101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
# np.random.rand(6,4)随机产生一个6行4列的矩阵，index为行索引名称,column为列索引名称
print(df)

df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print("df2:",df2)
print("df2.dtypes:",df2.dtypes)
print("df2.index:",df2.index)
print("df2.columns:",df2.columns)
print("df2.values:",df2.values)

print(df2.describe())  # 输出mean、max、min等信息,只对数字列有效

print(df2.T) # 转置输出

print(df2.sort_index(axis=1,ascending=False))

print(df2.sort_values(by='E')) # 根据'E'列的值进行排序