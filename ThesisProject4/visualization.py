# -*- coding=utf-8 -*-
import io
import re
import sys
from collections import Counter
import jieba
import pandas as pd
from matplotlib import pyplot as plt
import wordcloud
import warnings
# from scipy.misc import imread
from importlib import reload



def mycut(str1):
	str1 = ' '.join(jieba.cut(str1))  # 已经关闭了新词发现
	return str1
# mycut = lambda s:' '.join(jieba.cut(s))

# 4SnowNLP模块做正负情感分析/或者使用ROSTCM6代替生成
filepath1 = 'temp_after_filter3_utf8_正面情感结果.txt'
filepath2 = 'temp_after_filter3_utf8_负面情感结果.txt'
df1 = pd.read_csv(filepath1, encoding='utf-8', header=0)
df2 = pd.read_csv(filepath2, encoding='utf-8', header=0)
print(df1.head())
print(df2.head())
df11 = df1['comments'].map(lambda x: re.sub(r'\d*\s\s', '', x))
df22 = df2['comments'].map(lambda x: re.sub(r'[-]\d*\s\s', '', x))
print('去除评分前缀后正面：\n')
print(df11.head())
print('去除评分前缀后负面：\n')
print(df22.head())
# 输出去除前缀后的内容 用于ROSTCM6生成正负语义网络
df11.to_csv('正面情感评论_无前缀.txt', index=False, header=False, encoding='utf-8')
df22.to_csv('负面情感评论_无前缀.txt', index=False, header=False, encoding='utf-8')

'''以下是用snownlp自行分类的代码
coms=[]
coms=comments.apply(lambda x: SnowNLP(x).sentiments)
 # 情感分析，coms在0~1之间，以0.5分界，大于0.5，则为正面情感
pos_data=comments[coms>0.6] # 此处取0.6是为了使的词的情感更强烈点
neg_data=comments[coms<0.4] # 负面情感数据集
neutral_data = comments[coms>=0.4 and coms<=0.6]
pos_data[:5]
neg_data[:5]
neutral_data[:5]
'''

# 5jieba模块做中文分词处理，采用apply()广播形式加快分词速度
df1 = df1.iloc[:, 0].apply(mycut)
df11 = pd.DataFrame(df11.apply(mycut))
df2 = df2.iloc[:, 0].apply(mycut)
df22 = pd.DataFrame(df22.apply(mycut))
print('分词处理后正面：\n')
print(df11.head())
print('分词处理后负面：\n')
print(df22.head())
# df1 = mycut(str(df1))这种方法也可以
# df11 = pd.DataFrame(df1)

# 6去除停用词
stopfilepath = './stoplist_utf8.txt'
stop = pd.read_csv(stopfilepath, encoding='utf-8', header=None, sep='dingbangchu',
                   engine='python')  # 这里sep分割符 非停用词符均可，这里选的是竞赛站名
# sep设置分割词，csv默认以半角逗号分割，该词恰好在停用词表中导致读取出错，因此手动设置一个不存在的分割词，如dingbangchu
stop = [' ', ''] + list(stop[0])  # Pandas自动过滤了空格符，这里手动添加，此时stop由df类型转为list类型
pos = pd.DataFrame(df11.copy())
neg = pd.DataFrame(df22.copy())
pos = pos['comments'].apply(lambda s: s.split(' '))  # 定义一个分割函数，然后用apply广播，每行按空格分隔,每行由str转变为list
pos = pos.apply(lambda x: [i for i in x if i not in stop])  # 逐词判断是否停用词，思路同上
neg = neg['comments'].apply(lambda s: s.split(' '))
neg = neg.apply(lambda x: [i for i in x if i not in stop])
print('去除停用词后正面：\n')
print(pos.head())
print('去除停用词后负面：\n')
print(neg.head())
# 输出去除停用词后已分词的内容 用于生成词云以及后续LDA主题分析
pos.to_csv('正面情感分词有效版.txt', index=False, header=False, encoding='utf-8')
neg.to_csv('负面情感分词有效版.txt', index=False, header=False, encoding='utf-8')

# pos = pd.DataFrame(pos.copy())
# neg = pd.DataFrame(neg.copy())
# pos = pos[pos.iloc[:, 0].apply(len) >= 1]
# print(pos[:5])
# neg = neg[neg.iloc[:, 0].apply(len) >= 1]
# print(neg[:5])

# 7词频统计
# 正面
all_words = []
for n in range(0, len(pos)):
	for i in pos[n]:
		all_words.append(i)
word_count = pd.Series(all_words)
top_10 = word_count.value_counts(sort=True, ascending=False, dropna=True)
print('正面词频统计TOP10关键词：')
print(top_10[:10])
counts_result = dict(Counter(all_words))
# get to k most frequently occuring words
# counts_result = Counter(all_words).most_common(10)
# print('正面词频统计字典如下：')
# print(counts_result)
with open('正面词频统计.txt', 'w', errors='ignore') as f:
	[f.write(str('{0},{1}\n'.format(key, value))) for key, value in counts_result.items()]
# 负面
all_words = []
for n in range(0, len(neg)):
	for i in neg[n]:
		all_words.append(i)
word_count = pd.Series(all_words)
top_10 = word_count.value_counts(sort=True, ascending=False, dropna=True)
print('负面词频统计TOP10关键词：')
print(top_10[:10])
counts_result = dict(Counter(all_words))
# print('负面词频统计字典如下：')
# print(counts_result)
with open('负面词频统计.txt', 'w', errors='ignore') as f:
	[f.write(str('{0},{1}\n'.format(key, value))) for key, value in counts_result.items()]
# temp_df = pd.DataFrame(counts_result)
# temp_df.to_csv('词频统计.txt', index=False, header=False, encoding='utf-8')
# print(type(pos)) <class 'pandas.core.series.Series'>
# print(pos[0])
# print(type(pos[0])) list
# print(all_words)
# print(type(all_words))


# 8词云图绘制
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
warnings.filterwarnings("ignore")
# (1)读取背景图片
# back_picture = imread(r"")
# usa_mask = np.array(Image.open('flower.png'))
# (2)设置词云参数（源文件应该是分词后并去除停用词的内容，而不是词频表）
# 从文件导入数据：
f = open('负面情感分词有效版.txt', encoding='utf-8').read()
font = r'C:\Windows\Fonts\msyh.ttc'
# pic = imread('')  +mask='pic',
wc = wordcloud.WordCloud(
	background_color="white",
	height=800,
	width=1000,
	font_path=font,
    prefer_horizontal=0.2,
	max_words=2000,
	relative_scaling=0.3,
	max_font_size=200).generate(f)
# wc1 = wc.fit_words(counts_result)
# .generate_from_text(comments)
# 从DataFrame/pos/neg生成词云
# 从词频统计文件生成词云
# (3)绘制词云图
plt.imshow(wc, interpolation="nearest")
plt.axis("off")
# plt.figure(figsize=(8, 8))
# plt.savefig('ciyun_test.jpg', dpi=1000, bbox_inches='tight', quality=95)
plt.show()
# (4)保存到本地
wc.to_file("ciyun2.png")
print('词云图已生成！')
# plt.savefig('图6.jpg', dpi=600, bbox_inches='tight', quality=95)
# plt.show()


'''以下是某网站的词云全过程前半部分代码
# 利用jieba进行分析操作
df["评论"] = df["评论"].apply(jieba.lcut)
df.head()
# 去除停用词操作
with open("stopword.txt", "r", encoding="gbk") as f:
	stop = f.read()  # 返回的是一个字符串
stop = stop.split()  # 这里得到的是一个列表.split()会将空格，\n，\t进行切分，因此我们可以将这些加到停用词当中
stop = stop + [" ", "\n", "\t"]
df_after = df["评论"].apply(lambda x: [i for i in x if i not in stop])
df_after.head()
'''

'''以下是所有为了去除前缀所做的尝试
课本中的“data1 = pd.DataFrame(data1[0].str.replace(r'.*?\d+?\\t ', ''))”方法不行，会显示df无str（）方法
df1 = df1.apply(lambda s: s.str.split(r'\s'))
df2 = df2.apply(lambda s: s.str.split(r'\s'))
print(df1.values)
print(df1.shape[1])
df1 = df1.apply(lambda s: s.str.strip([0, 2]))  # s.str.strip('@')
ndarray = df1['comments'].astype(str).values
for i in ndarray:
	i = i.split('    ')
print(df1.shape[1])
用正则表达式非贪婪模式修改数据:(*?)表示0个或多个非\n字符  (+?)表示1个或多个数字，此操作是为了删除ROSTCM6软件给出的评分正负前缀
df3 = pd.DataFrame(df1.astype(str).replace(r'\d*\s\s', 'a'))
Python 3将字符串文字解释为Unicode字符串，因此 \d 被视为转义的Unicode字符
df4 = pd.DataFrame(df2.astype(str).replace(r'([-]\d*\s\s).*?', 'b'))
'''
