import pandas as pd
import numpy as np
import re
data = pd.read_csv("result.csv")
data = data.fillna(0)
data = data.drop(columns=['Unnamed: 0'])
time,time_rusult=[],[]
for i in range(len(data)):
    timestr=data.loc[i].date
    time_num=re.findall(r"\d+\.?\d*",timestr)
    try:
         num1=int(time_num[0])
         num2=int(time_num[1])
         if 'a' in timestr:
             if num1==12:
                 time=num2
             else:
                 time=num1*60+num2
  #       elif timestr[7:9]=='pm':
         elif 'p' in timestr:
            time=(num1+12)*60+num2
    except:
        print('异常')
    time_rusult.append(time)
time_rusult.to_csv("timeresult.csv",encoding="utf_8_sig")
