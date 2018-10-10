import pandas as pd
import numpy as np
import re
data = pd.read_csv("result.csv")
data = data.fillna(0)
data = data.drop(columns=['Unnamed: 0'])
time=[]
for i in range(len(data)):
    timestr=data.loc[i].date
    time.append(re.findall(r"\d+\.?\d*",timestr))
