# “王一博推荐明星琥珀卸妆油”41838条评论的爬取及存储
# -*- coding: utf-8 -*-
import pandas as pd
import requests
import re
import time

nick = []
quality = []
date = []
comment = []
data_list = []

for i in range(1, 2092, 1):
    print("正在爬取第" + str(i) + "页")
    # 构建访问的网址，需要到network中去搜索某一特定评论才能找到在list_detail_rate.htm项目中RequestURL
    first = 'https://rate.tmall.com/list_detail_rate.htm?itemId=528249673577&spuId=518213035&sellerId=2820842454&order=3&currentPage='
    last = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hv/9vUvbpvUvCkvvvvvjiWPLzw0jtRP2FWQjrCPmPZzjrmR2qv1jYEP2qZ1jnvRvhvCvvvvvvvvpvVvvpvvhCvkvhvC9QvvOCgL89Cvv9vvUmqC8d9Rb9CvmFMMQ2qS6vvzQvvvN3vpv3Mvvv2UhCv2CUvvvW9phvWJpvvvADvpvsCmvhvLvkgqvvjnGAn6jVTVjW73cjxQEewJocxQWsy+kglCwAxycVTVjW73cjxQEyAwkqxQWsyjmglCwAxkcVTVjn8ycjxQEewE9oQD7zydigRvpvhvv2MMTOCvvpvvUmm&needFold=0&_ksTS=1611765007210_466&callback=jsonp467'
    url = first + str(i) + last
    # 访问的头文件，还带这个cookie
    headers = {
        # 用的哪个浏览器
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        # 从哪个页面发出的数据申请，每个网站可能略有不同
        'referer': 'https://list.tmall.com/search_product.htm?q=%D6%B2%B4%E5%D0%E3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton',
        # 哪个用户想要看数据，是游客还是注册用户,建议使用登录后的cookie
        'cookie': 'cna=MQY3F16TIiUCAXj0KLkDrCSr; isg=BGNjRropB1uuA_REvybfGAIH8acNWPeaIItUbZXE-UAj1JH2HSlX6FVGyiRa70-S; tfstk=c4kOBe_umeYG8ExQrfdhlkRv5i4OaIALuhaAH3297nhh8gCANsx-EYpvK1Z4v7xd.; l=eBPYPbzmOInY9TPtBO5CFurza77tECA2lkPzaNbMiInca1AFgttRONCIh9W2zdtfgt5UxetzvffAydnH8rz_WE6NfJVNKXIpBNppye1..; cq=ccp%3D0; tk_trace=1; xlly_s=1; dnk=t_1498050231982_0133; uc1=cookie14=Uoe1g86s3uq%2BjA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&pas=0&cookie21=W5iHLLyFeYZ1WM9hVnmS; uc3=l...91a2c115ef7033a6b48502a779e509; sg=37e; csg=43224ab3; _tb_token_=ef331733a3745; enc=aNhZG4tska8trzBRgSHRKOtefZ7s0V8FBMx51cmI3uq9Te%2FWkYJhLijxhq%2B1ZWsD8ZI7N2YwkrE5clkrpJrb%2BQ%3D%3D; pnm_cku822=098%23E1hvq9vUvbpvUvCkvvvvvjiWPLzw0j38PFLwAjivPmPWzji2PLqyzj1HnLMv0jiURvhvCvvvphmgvpvIMMYvrMMMvP%2BvvhOVvvvCqQvvB9OvvUHmvvCVC9vv9oGvvhOZvvmCR89Cvv9vvhh0hZgpVO9Cvv4CvhE2gnvUvpCWvwR9ICz9d34Adc9DYE7rV4g7EcqhaXTAdBQaWXxrj8TJdB61D76Xdigqb64B9C97%2BulsbSLhHd8rVC691W9wHd8raAd6kCh7%2Bull8vvCvvOv9hCvvvvRvpvhvv2MMTOCvvpvvhHh'
    }

    # 尝试获取数据（这里的数据应该是从json里面获取的）
    try:
        proxy = {'http': '58.253.157.212:9999'}
        data = requests.get(url, headers=headers, proxies=proxy).text
        time.sleep(10)
        # 一种尝试是化为规范化json从而按照层级提取rateContent内容
        # result = data.json()
        # finalresult = result['rateDetail']['rateList']['rateContent']
        # 原本是这样通过正则表达式匹配rateContent内容，但是每一句评论的后方始终多了一个",，可以继续尝试remove、replace等函数或直接调试re

        # 通过displayUserNick/auctionSku/rateDate/rateContent分别得到匿名名称、规格、评论时间、评论内容
        nickname = re.findall('"displayUserNick":"(.*?)"', data)
        # print(nickname)
        nick.extend(nickname)
        auctionSku = re.findall('"auctionSku":"(.*?)"', data)
        # print(auctionSku)
        quality.extend(auctionSku)
        rateDate = re.findall('"rateDate":"(.*?)"', data)
        # print(rateDate)
        date.extend(rateDate)
        rateContent = re.findall('"rateContent":"(.*?)"', data)
        # print(rateContent)
        comment.extend(rateContent)

        # result = re.findall('rateContent":"(.*?)"fromMall"', data)
        # print(result)  可以发现result自身就已经是20个元素的列表
        '''
        for r in result:
            list = r.split('",')
            data_list.extend(list)
        data_list.extend(result)
        '''
    except Exception as e:
        print(str(e))
        print("本页爬取失败")

print('总共成功爬取 ' + str(len(comment)) + ' 条评论如下！')
# print(nick, quality, date, comment)
print(comment)

# 保存数据到Excel
df = pd.DataFrame()
df["用户名"] = nick
df["购买规格"] = quality
df["评论时间"] = date
df["评论内容"] = comment
df.to_excel("评论_汇总.xlsx")
print('成功保存到Excel！')
# 保存数据到csv文件
df.to_csv("comments_summary.csv",  encoding="utf-8")
print('成功保存到CSV文件！')

'''
import json
def json_to_dict(data_json):
    j = data_json
    dict = json.loads(s=j)
    print(dict)
'''

'''
data = re.search(r'{.*}',response).group()
data1 = json.loads(data)
data2 = jsonpath(data1,'$.comments[*].content')
for i in data2:
print(i)
print("**"*30)
'''

'''以下是所有关于去掉末尾两位多余字符的尝试：
        # result = re.findall(r'"rateContent": "(.*?)"",\nfromMall"', data.text) 为空
        # result = re.findall(r'"rateContent": "(.*?)",', data.text) 为空
        # data_list.extend(result[:-2])
        # for r in result:
        #     r = str(r)[:-2]
        #     result.extend(r)
        '''

# for d in data_list:
#     d = d[:-2]

# while '' in data_list:
#     data_list.remove('')
# print('总共成功爬取 '+str(len(data_list))+' 条评论如下！')