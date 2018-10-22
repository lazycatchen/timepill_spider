import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
content = []
import re, jieba
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from os import path
d=path.dirname(__file__)
stopwords_path = d+ '/static/stopwords.txt'
# 读数据


def read_csv():
    data = pd.read_csv("result_1.csv")
    data = data.fillna(0)
    data = data.drop(columns=['Unnamed: 0'])
    timetemp=int(10000)
    time_rusult,content_result=[],[]
#try:
    for i in range(len(data)):
        timestr=data.loc[i].date  #按时间顺序排序，从0到1440分	data = pd.read_csv("result_1.csv")
       #contentstr=data.loc[i].book
        time_num=re.findall(r"\d+\.?\d*",timestr)
        num1=int(time_num[0])
        num2=int(time_num[1])
        num3=num2
        try:
            if 'a' in timestr:
                if num1==12:
                     time=num2
                else:
                    time=num1*60+num2
            elif 'p' in timestr:
                if num1==12:
                    time=num1*60+num2
                else:
                    time=(num1+12)*60+num2

            if time<=timetemp and time<2000:
                timetemp=time
                content_result.append(data.loc[i].book)
            else:
                continue
        except:
            print('异常')
    return content_result
      # except:
         #   print('异常')
    #time_rusult.append(time)
	#for i in range(len(data)):
	#	contentstr=data.loc[i].book
	#	content.append(contentstr)
    #return content


def jiebaclearText(text):
	mywordList=[]
	text_char=' '.join(text)
	text_char=re.sub('[！，em。.…《》#—“”‘’ ？\r\n]', '',text_char)
	seg_list=jieba.cut(text_char,cut_all=False)
	#将一个generator的内容用/连接
	listStr='/'.join(seg_list)
	listStr = listStr.replace("class","")
	listStr = listStr.replace("span", "")
	listStr = listStr.replace("1", "")
	#打开停用词表
	f_stop=open(stopwords_path,encoding="utf8")
	#读取
	try:
         f_stop_text=f_stop.read()
	finally:
	     f_stop.close()#关闭资源
	#将停用词格式化，用\n分开，返回一个列表
	f_stop_seg_list=f_stop_text.split("\n")
	#对默认模式分词的进行遍历，去除停用词
	for myword in listStr.split('/'):
	    #去除停用词
	    if not(myword.split()) in f_stop_seg_list and len(myword.strip())>1:
	        mywordList.append(myword)
	return ' '.join(mywordList)

# 生成词云图
def make_wordcloud(text1):
	text1 = text1.replace("", "")
	bg = plt.imread(d + r"/static/cat1.jpg")
	# 生成
	wc = WordCloud(# FFFAE3
		background_color="white",  # 设置背景为白色，默认为黑色
		width=890,  # 设置图片的宽度
		height=600,  # 设置图片的高度
		mask=bg,
		# margin=10,  # 设置图片的边缘
		max_font_size=150,  # 显示的最大的字体大小
		random_state=50,  # 为每个单词返回一个PIL颜色
		font_path=d+'/static/simkai.ttf'  # 中文处理，用系统自带的字体
	).generate_from_text(text1)
	# 为图片设置字体
	my_font = fm.FontProperties(fname=d+'/static/simkai.ttf')
	# 图片背景
	bg_color = ImageColorGenerator(bg)
	# 开始画图
	plt.imshow(wc.recolor(color_func=bg_color))
	# 为云图去掉坐标轴
	plt.axis("off")
	# 画云图，显示
	# 保存云图
	wc.to_file(d+r"/picture/word_cloud1.png")
content = read_csv()  #读取CSV
x=jiebaclearText(content) #结巴分词
make_wordcloud(x)#词云图
