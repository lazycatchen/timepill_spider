import csv
import pandas as pd
time = []
nickName = []
gender = []
cityName = []
userLevel = []
score = []
content = []

# 读数据
def read_csv():
	data = pd.read_csv("result_1.csv")
	data = data.fillna(0)
	data = data.drop(columns=['Unnamed: 0'])
	for i in range(len(data)):
		contentstr=data.loc[i].book
		content.append(contentstr)
	return content

import re, jieba
#词云生成工具
from wordcloud import WordCloud
#需要对中文进行处理
import matplotlib.font_manager as fm
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from os import path

d=path.dirname(__file__)

#stopwords_path = d + '/static/stopwords.txt'
stopwords_path = d+ '/static/stopwords.txt'
# 评论词云分析
def jiebaclearText(text):
    #定义一个空的列表，将去除的停用词的分词保存
    mywordList=[]
    re.sub('[！，em。.…《》#—“”‘’ ？\r\n]', '', text)
    #进行分词
    seg_list=jieba.cut(text,cut_all=False)
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
	bg = plt.imread(d + r"/static/znn1.jpg")
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
	wc.to_file(d+r"/picture/word_cloud.png")
content = read_csv()
jiebaclearText(content)
make_wordcloud(content)
#word_cloud(content)