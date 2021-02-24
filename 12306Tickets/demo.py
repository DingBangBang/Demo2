# coding:utf-8
from encodings import utf_8
import requests
from bs4 import BeautifulSoup

proxy = {'http': '58.253.157.212:9999'}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
url = 'https://www.csdn.net/'
response = requests.get(url, headers=headers, proxies=proxy)
# print(response.content.decode('utf_8'))
html_doc = response.content.decode('utf_8')
soup = BeautifulSoup(markup=html_doc, features='lxml')
# print(soup.prettify)
# print('the result of .title', soup.findAll)
print(soup.find('title').text)
print(soup.title)
print(soup.title.text)
print(soup.title.name)
print(soup.find_all('description'))  # none
print(soup.find_all('a'))
'''
list = ['我觉得非常可以",', '我觉得不是很好",']
list.replaceAll('",', '')
'''