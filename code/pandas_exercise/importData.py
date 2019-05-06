import pandas as pd
import numpy as np

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')