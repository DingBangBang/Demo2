# -*- coding:utf-8 -*-
import pandas as pd

data = pd.read_csv('comments_summary.csv', encoding='utf-8')
data = data[u'评论内容']
data.to_csv('comments_summary.txt', index=False, header=False)
print('转换成功')
