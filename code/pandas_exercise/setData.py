import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df)
print("-------------")

df.iloc[2,2] = 111 #通过坐标索引
print(df)
print("-------------")

df.loc['20130101','B'] = 2222 #通过label
print(df)
print("-------------")

df2 = df.copy()

df.A[df.A > 10] = 0 # 只有A列中满足条件的元素置0
print(df)
print("-------------")

df2[df2.A > 10] = 0 #A列满足条件的元素所在的行全置0
print(df2)
print("-------------")

df['F'] = np.nan
print(df)
print("-------------")

df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print(df)
print("-------------")
