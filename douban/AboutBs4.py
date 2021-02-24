from bs4 import BeautifulSoup

# (1)BeautifulSoup的Tag属性：只能拿到html文档中的第一个找到的标签内容
file = open('F:\Demo\douban\index.html', 'rb')  # read bytes
html = file.read()  # 将文件中内容保存为内存中的html格式文件
bs = BeautifulSoup(html, 'html.parser')
print(bs.title)
'''
# (2)Navigable属性：只提取html文档中该标签的内容（字符串）
print(bs.title.string)
print(bs.meta)
print(bs.link)
# print('head:\n', bs.head)
print(bs.a.attrs)  # 输出bs中所有属性键值对形式存储的字典
# (3)BeautifulSoup属性：输出文档本身  # print(type(bs))
# print(bs)
# (4)Comment属性:输出的内容不包含注释
print(bs.a.string, '\n')

# --------------------------------
# 另外去看下bs4的遍历文档树方法，可以访问子父节点上下节点等
# print(bs.contents)

# --------------------------------
# 对文档的搜索方法：
# 一、find_all系列
# （1）find_all:过滤出完全匹配的字符串
print(bs.find_all('a'))
# （2）search()：正则表达式搜索，只要标签中含有a，就把整个部分的内容全部作为列表的一个值输出
import re
print(bs.find_all(re.compile('a')))
# （3）传入一个函数或者方法，根据自定义函数的要求搜索
def is_name_exist(tag):
	return tag.has_attr('link')
list = bs.find_all(is_name_exist)
for item in list:
	print(item)
'''
# 二、参数系列
# kwargs 参数：返回参数符合条件的内容及其子内容
print(bs.find_all(href='http://news.baidu.com'))  # id='head'
# print(bs.find_all(class_=True))
# text参数：查找已知的文本或按照未知文本的类型查询
print(bs.find_all(text=['hao123', '地图', '贴吧']))
import re
print(bs.find_all(text=re.compile('\d')))  # 查找所有有数字的内容（标签里的字符串）
# limit参数：限定搜索条数，提取搜索结果的前五条
print(bs.find_all('a', limit=5))
# css选择器：页面上的层层嵌套，通过一个class/id/div直接定位
print(bs.select('title'))  # '.mnav'指的是class等于这个值，'#u1'指的是id等于u1，
# 'a[class="bri"]'指的是a中指定class 'head>title' '.mnav~ .bri'然后print(list[0].get_text())可以得到'更多产品'

# 三、正则表达式

