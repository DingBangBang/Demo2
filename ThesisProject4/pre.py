import pyLDAvis.gensim
import pyLDAvis
from LDA import neg_lda, neg_corpus, neg_dict, pos_lda, pos_corpus, pos_dict

# data2 = pyLDAvis.gensim.prepare(pos_lda, pos_corpus, pos_dict)
# print('以下是正面可视化参数\n')
# print(data2)
# pyLDAvis.save_html(data2, 'postopic.html')
# pyLDAvis.display(data2)
# pyLDAvis.show(data2, open_browser=True)


data1 = pyLDAvis.gensim.prepare(neg_lda, neg_corpus, neg_dict)  #三个参数分别是：计算好的话题模型；文档词频矩阵；词语空间
print('以下是负面可视化参数\n')
print(data1)
pyLDAvis.save_html(data1, 'negtopic.html')
pyLDAvis.display(data1)
pyLDAvis.show(data1, open_browser=True)




# 如果用sklearn或者graphlab
'''
import pyLDAvis
import pyLDAvis.sklearn

#pyLDAvis.enable_notebook()

data = pyLDAvis.sklearn.prepare(lda,tf,tf_vectorizer)
print(data)

#显示图形
pyLDAvis.show(data)

#pyLDAvis.save_json(data,' fileobj.html')

'''

# 输出每个主题的支持文档数：属于该主题的评论（文档）数量
'''
for i in lda.get_document_topics(corpus)[:]:
　　listj=[]
　　for j in i:
　　　　listj.append(j[1])
　　bz=listj.index(max(listj))

　　#print(i[bz][0],i,listj,listj.index(max(listj)))
　　print(i[bz][0])
'''