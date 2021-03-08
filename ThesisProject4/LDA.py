# 9gensim做LDA主题分析建模
# encoding: utf-8
from gensim import corpora, models
import pandas as pd
from visualization import pos, neg

# 正面主题分析
pos_dict = corpora.Dictionary(pos)  # 建立词典，以计算机可以处理的方式（数字）
pos_corpus = [pos_dict.doc2bow(i) for i in pos]  # 建立语料库，bag of word
pos_lda = models.LdaModel(pos_corpus, num_topics=10, id2word=pos_dict, passes=10)  # LDA模型训练
print('\n以下是gensim实现的LDA模型训练结果：\n')
for i in range(10):
	print('pos_topic' + ' ' + str(i+1)+' : ')
	print(pos_lda.print_topic(i))  # 输出每个主题
# print(pos_lda.show_topics(num_topics=10, num_words=10, formatted=True))
LDA_result_pos = pos_lda.print_topics(num_topics=10, num_words=10)
df_pos = pd.DataFrame(data=LDA_result_pos)
df_pos.to_excel('LDA_result_pos.xlsx', sheet_name='LDA_result_pos', startcol=0, startrow=0)
print('LDA_result_pos 成功输出!\n')

# 负面主题分析
neg_dict = corpora.Dictionary(neg)
neg_corpus = [neg_dict.doc2bow(i) for i in neg]
neg_lda = models.LdaModel(neg_corpus, num_topics=10, id2word=neg_dict, passes=10)
for i in range(10):
	print('neg_topic' + ' ' + str(i+1) + ' : ')
	print(neg_lda.print_topic(i))
LDA_result_neg = neg_lda.print_topics(num_topics=10, num_words=10)
df_neg = pd.DataFrame(data=LDA_result_neg)
df_neg.to_excel('LDA_result_neg.xlsx')
print('LDA_result_neg 成功输出!\n')

# =============================================================================
# ldamodel = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=3, id2word = dictionary, passes=20)
# corpus: 必须。语料库
# num_topics: 必须。LDA 模型要求用户决定应该生成多少个主题。由于我们的文档集很小，所以我们只生成三个主题;
# id2word：必须。LdaModel 类要求我们之前的 dictionary 把 id 都映射成为字符串;
# passes：可选。模型遍历语料库的次数。遍历的次数越多，模型越精确。但是对于非常大的语料库，遍历太多次会花费很长的时间。
# 调整模型的主题数和遍历次数对于得到一个好的结果是很重要的
# doc2bow()方法解析:
# new_doc = 'Human computer interaction computer'
# new_vec = dictionary.doc2bow(new_doc.lower().split())
# 其中的dictionary是已经构建好的Dictionary变量
# print(new_vec)
# 输出为：[(0,1),(1,2)]
# (0,1) --> 0 代表索引，表示第一个词，1表示出现的次数，即：Human出现了1词
# (1,2) --> 代表：computer出现了2词
# 第三个词：interaction没有统计，是因为词典里没有收录该词
# =============================================================================

'''
# 将输出结果保存到Excel中，以矩阵的形式
# LDA输出结果形式为res = [[(0, 0.07522942), (1, 0.9247706)], [(0, 0.9151239), (1, 0.08487616)], [(0, 0.06792135), (1, 0.93207866)]]
def saveAticleTopicsResultToFile(result, outPutFile):
	r = []
	i = 1
	for article in result:
		item = {'article_id/topicType': i}
		for topic_result in article:
			item[str(topic_result[0])] = topic_result[1]
		r.append(item)
		i += 1
	writeDataToExcleFile(r, outPutFile)
'''

'''
#coding=utf-8
import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary
fr=open('cleanChiSegments.txt','r')
train=[]
for line in fr.readlines():
    line=line.split(' ')
    train.append(line)
 
print len(train)
print ' '.join(train[2])
 
dictionary = corpora.Dictionary(train)
corpus = [ dictionary.doc2bow(text) for text in train ]
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
 
topic_list=lda.print_topics(20)
print type(lda.print_topics(20))
print len(lda.print_topics(20))
 
for topic in topic_list:
    print topic
print "第一主题"
print lda.print_topic(1)
 
 
print '给定一个新文档，输出其主题分布'
 
#test_doc = list(new_doc) #新文档进行分词
test_doc=train[2]#查看训练集中第三个样本的主题分布
doc_bow = dictionary.doc2bow(test_doc)      #文档转换成bow
doc_lda = lda[doc_bow]                   #得到新文档的主题分布
#输出新文档的主题分布
print doc_lda
for topic in doc_lda:
    print "%s\t%f\n"%(lda.print_topic(topic[0]), topic[1])
'''