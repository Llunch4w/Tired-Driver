import pandas as pd
import numpy as np

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                        'C':['C0','C1','C2','C3'],
                        'D':['D0','D1','D2','D3']})

print(left)
print(right)
res = pd.merge(left,right,on='key')
print(res)


print("-------------------------")
left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                    'key2':['K0','K1','K0','K1'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K3'],
                        'key2':['K0','K0','K0','K0'],
                        'C':['C0','C1','C2','C3'],
                        'D':['D0','D1','D2','D3']})

print(left)
print(right)
res = pd.merge(left,right,on=['key1','key2'])# 拥有相同key1、key2的合并
print(res)

print("-------------------")
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K1','K2'],'age':[4,5,6]})
res = pd.merge(boys,girls,on='k')
print(res)

print("-------------------")
res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)
