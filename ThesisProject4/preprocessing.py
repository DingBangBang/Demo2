# 评论数据的预处理过程：包括文本去重、机械压缩去词、短句过滤及后续的词云图绘制
import pandas as pd


# 高效机械压缩去词函数
# def str_unique(raw_str, reverse=False):
# 	# 比如：我喜欢喜欢喜欢喜欢喜欢喜欢该商品；去掉重复的“喜欢”:param raw_str::param reverse: 是否转置:return:
# 	if reverse:
# 		raw_str = raw_str[::-1]
# 	res_str = ''
# 	for i in raw_str:
# 		if i not in res_str:
# 			res_str += i
# 	if reverse:
# 		res_str = res_str[::-1]
# 	return res_str


# --------------0数据导入----------------
df = pd.read_csv(r'F:\Demo\ComplexDemo\lipstick_result\comments_summary_lipstick.csv', encoding='utf-8', header=0)
# df = pd.read_csv('', encoding='utf-8', header=0)
print('\n========该文档共有%s条评论如下：========' % len(df))
print(df.head())
print(type(df))
# print(df.info)

# ---------------1文本去重---------------
a1 = len(df)
df1 = pd.DataFrame(df.iloc[:, 4].unique())
# df1.to_csv('temp_after_duplicated1.txt', index=False, header=False, encoding='utf-8')
a2 = len(df1)
print('========文本去重共删除了%s条评论如下：=========' % (a1 - a2))
print(df1.head())

# ---------------2【重点】机械压缩去词（不改变评论条数）---------------
'''注释掉是因为没什么意义，去掉了一句中的所有大于1次出现的字
ser1 = df1.iloc[:, 0].apply(str_unique)  # 这时，因为索引了第一列，所以结果成了Series；
print(type(ser1))  # 输出<class 'pandas.core.series.Series'>
df2 = pd.DataFrame(ser1.apply(str_unique, reverse=True))  # 再次生成DataFrame；
print('========机械压缩去词已完成如下：========')
print(df2.head())
'''

# ---------------4清除无意义文本：（1）”此用户没有填写评论“（2）”到货神速，双十一力度太给力了“---------------
df2 = df1.replace('此用户没有填写评论!', '')  # 将默认评论部分替换为空值
df2 = df1.replace('到货神速 双十一力度太给力了', '')
print('========清除无意义文本已完成如下：========')
print(df2.head())  # 查看是否删除成功

# ---------------3短句过滤---------------
c1 = len(df2)
df3 = df2[df2.iloc[:, 0].apply(len) >= 4]
c2 = len(df3)
print('短句过滤共删除了%s条评论如下：' % (c1 - c2))
print(df3[:5])
df3.to_csv('temp_after_filter3_lipstick.txt', index=False, header=True, encoding='utf-8')
print('========预处理完成后还剩%s条评论========' % len(df3))
print('评论预处理过程结束！')

''' 单字、双字、三字去重封装成函数如下：
def func(st):
    for i in range(1,int(len(st)/2)+1):
        for j in range(len(st)):
            if st[j:j+i] == st[j+i:j+2*i]:
                k = j + i
                while st[k:k+i] == st[k+i:k+2*i] and k<len(st):   
                    k = k + i
                st = st[:j] + st[k:]    
return st
'''

'''文本去重处
	显示int()
	参数类型错误，不能是NoValueType
	df = df.dropna(axis=0)
	print('查看是否有重复值：' + str(df.duplicated().value_counts()))
	a1 = len(df)
	df1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
	a2 = len(df1)
	print('文本去重共删除了%s条数据', (a2 - a1))
'''

'''清楚无意义文本处
定位无评论内容
查找仅有‘此用户没有填写评论!追加评论：’的评论,并删除无评论内容
index = df3.loc[df3.values == "此用户没有填写评论"].index.tolist()
list2 = df3[df3.values == '到货神速 双十一力度太给力了'].index.tolist()
df3.drop(list2, axis=0, inplace=True)
list1 = df3[df3.values == "此用户没有填写评论"].index.tolist()
df3.drop(list1, axis=0, inplace=True)  # 出现链式索引的警告，关于现View和Copy的差别
df3.loc[df3.values == '此用户没有填写评论'] = ''
df3.drop(labels='此用户没有填写评论', inplace=True)  # KeyError: "['此用户没有填写评论'] not found in axis"
df3.drop(df3.loc[df3.values == "到货神速 双十一力度太给力了"], axis=0, inplace=True)
查漏，通过将'此用户没有填写评论!追加评论：'进一步确保替换成功
'''

'''短句过滤处
如果是=df2.values的话print(type(comments_data))  # 输出<class 'numpy.ndarray'>
long_str = lambda x: x>=4
df3 = filter(long_str, comments_data)
'''
