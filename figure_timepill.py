import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
data = pd.read_csv("result.csv")
data = data.fillna(0)
data = data.drop(columns=['Unnamed: 0'])
time,time_rusult=[],[]
timetemp=10000000
for i in range(len(data)):
    timestr=data.loc[i].date
    time_num=re.findall(r"\d+\.?\d*",timestr)
    try:
         num1=int(time_num[0])
         num2=int(time_num[1])

         num3=num2
         if 'a' in timestr:
             if num1==12:
                 time=num2
             else:
                 time=num1*60+num2
  #       elif timestr[7:9]=='pm':
         elif 'p' in timestr:
             if num1==12:
                 time=num1*60+num2
             else:
                 time=(num1+12)*60+num2

         if time<=timetemp and time<2000:
            timetemp=time
         else:
             continue
    except:
        print('异常')
    time_rusult.append(time)

hour=[]
for ix in range(24):
    h1=0
    for ii in  time_rusult:
        if (ix*60+1)<ii and ii<=(ix*60+61):
            h1=h1+1
    hour.append(h1)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] =False
plt.plot(hour,color='k')
plt.grid(b=True, which='major', axis='y')
plt.ylabel(u"频数")
plt.xlabel(u"时间/h")
plt.title(u"胶囊发帖量统计")
plt.show()
