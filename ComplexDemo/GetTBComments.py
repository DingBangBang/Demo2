# “王一博推荐明星琥珀卸妆油”41838条评论的爬取及存储
# -*- coding: utf-8 -*-
import pandas as pd
import requests
import re
import time
# import multiprocessing as mp

nick = []
quality = []
date = []
comment = []


'''依次是眉笔、小黑方、小方瓶、卸妆油、55刷
firstlist = [
    'https://rate.tmall.com/list_detail_rate.htm?itemId=528271120914&spuId=127783671&sellerId=2820842454&order=3&currentPage=',
    'https://rate.tmall.com/list_detail_rate.htm?itemId=597476412461&spuId=1263945176&sellerId=2820842454&order=3&currentPage=',
    'https://rate.tmall.com/list_detail_rate.htm?itemId=611288087009&spuId=1506265565&sellerId=2820842454&order=3&currentPage=',
    'https://rate.tmall.com/list_detail_rate.htm?itemId=528249673577&spuId=518213035&sellerId=2820842454&order=3&currentPage=',
    'https://rate.tmall.com/list_detail_rate.htm?itemId=557510761368&spuId=1067672569&sellerId=2820842454&order=3&currentPage='
]
lastlist = [
    '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvRvvbvnQvUvCkvvvvvjiWPLFU6jYVP2L9gjljPmP91jnCPsqUlj1HPsSvljYURvhvChCvvvvUvpCWphRbv8WZUxW5Zd7xnsIsjAZ8lPhODj+XWDJHdX01UxUDCwLIRtxYcsnj3O97R0r7O34U+2KxNxGDCq2XDXtkvo3EKX0Ahc+nUxRv6f9CvmkMpv2NMMYvr6Cv2hOvvh8aphvOvpvvpGavpC9CvvC216CvVhyvvhWsuvhvmhCvCnl+PG/XkvhvCyn2mvpwVQvCvvXvppvvvvvRvpvhvv2MMs9CvvBvpvvvi9hvChCvCCoVvpvhphhvvUvCvCLwMb3NRrMwznAwZHS50ns/zR144v==&needFold=0&_ksTS=1614244910706_365&callback=jsonp366',
    '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvzpvWvRyvUvCkvvvvvjiWPLFU6jtnPLzZgjnEPmP9AjY8nLqhsjiWPFLvlj3C9vhvHnsGdDtDzYswzbs37/NOz2MwqHiIdvhvmpvhup8ZDvvOsOOCvvpvCvvvRvhvCvvvvvvRvpvhvv2MMQ9CvhQppLhvCsN9tnAQRqwiLO2vqU0QKoZH0RFEDLuTWDAvD7zZdigDNr1lKbVAnAaLIfmxfBuKNB3r1j7Z+ull8bmxfwoK5kx/zj7gFLoQKvhv8PMMvPKMpv2NvvmCAhCvmjGvvvW9phvWh9vvvACvpvQovvv28ZCv2WVIvpvUvvmvKt9w6iVUvpvV2vvC9j3RvvhvC9vhvvCvp8OCvvpvvUmmRvhvCvvvvvv=&needFold=0&_ksTS=1614245315496_538&callback=jsonp539',
    '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvZQvLvLgvUvCkvvvvvjiWPLFU6jtnR2zvtjYHPmPOQjnmn2cwsjnvRssUQjrn9vhv2nsG6HTGzYswzmJB7uQCvvyvm8WvMMGvxaUVvpvjzn147r/BrL9Cvvpvvvvv39hvCvvhvvmevpvhvvmv99gCvvpvvPMMvvhvC9vhvvCvpv9CvhQU+nvvCsuxfaBlHdUfb5c6D70fdeQCKWjxsLpZwySOsWLpVBDzBaAy+bZcR2xVI42hiC40f3qxs4V9VXB+m7zwaNo7eVQJIWAQAC4AKvhv8PMMvPKMpv2Nvvv2UhCvmjGvvvW9phvWh9vvvACvpvQovvv28ZCv2WVUvpvV2vvC9j3Ruvhvmvvv9bKOjXAJRvhvCvvvvvvVvpvEjn147rY9Hgy8RvhvCvvvvvmvvpvLSjQP7TSNznswvIt4GDRi4IkisF9CvvpvvvvvRvhvCvvvvvm+vpvoEvLdvITRvVl984GiExRDDazn&needFold=0&_ksTS=1614245365224_1380&callback=jsonp1381',
    '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hv/9vUvbpvUvCkvvvvvjiWPLzw0jtRP2FWQjrCPmPZzjrmR2qv1jYEP2qZ1jnvRvhvCvvvvvvvvpvVvvpvvhCvkvhvC9QvvOCgL89Cvv9vvUmqC8d9Rb9CvmFMMQ2qS6vvzQvvvN3vpv3Mvvv2UhCv2CUvvvW9phvWJpvvvADvpvsCmvhvLvkgqvvjnGAn6jVTVjW73cjxQEewJocxQWsy+kglCwAxycVTVjW73cjxQEyAwkqxQWsyjmglCwAxkcVTVjn8ycjxQEewE9oQD7zydigRvpvhvv2MMTOCvvpvvUmm&needFold=0&_ksTS=1611765007210_466&callback=jsonp467',
    '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvIQvRvpIvUpCkvvvvvjiWPLFU6jtnRsS9zjnEPmPvAjYRn2dZ6jDUPL5UzjDbRTQCvChh9nFJu9vvCFZDjlKx6fm6nIvCvvsNtTDwjDdNzYGOxnA+vpvp9gvFE0OvvURY+oYC6XZzRIOCvvpv9hCvi9hvCvvvpZogvpvIMMYvrMMMvP+vvhPovvvCqQvvB9OvvUHmvvCVC9vv9ZUvvhOZvvmCR89Cvv9vvhh0O1ffug9Cvv4CvhE2gn9UvpCWv2A+dCzvdiTAdch+fX7rj8TK4vlrs8TZHdBYVVzvdiG4jcHCAWkwHFKz8Z0vQE01+byDCwLIRfUTKFEw9E7re8TJEcq9aBJ1nbvAwpvCvvOv9hCvvvvRvpvhMMGvv29CvvpvvhCvRvhvCvvvphm+vpvEvvH2BtyvvvSE&needFold=0&_ksTS=1614245384075_1024&callback=jsonp1025'
]
'''
# for i in firstlist:
#     for j in lastlist
#         url = i + str(i) + j
for i in range(1, 3, 1):
    print("正在爬取第" + str(i) + "页")
    # 构建访问的网址，需要到network中去搜索某一特定评论才能找到在list_detail_rate.htm项目中RequestURL
    first = 'https://rate.tmall.com/list_detail_rate.htm?itemId=557510761368&spuId=1067672569&sellerId=2820842454&order=3&currentPage='
    last = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvCpvUvbpvUpCkvvvvvjiWPLFW1jDnRLqvtjnEPmPpljimRLLhgjtbRFMhzjEVRTOCvvpvvUmmRvhvCvvvvvvRvpvhMMGvvvvCvvOvCvvvphmgvpvIMMGv/qYvvnGvvUjUphvUNQvvvACvpvQovvv2UhCv2CUvvvWiphvWQO9CvvOWvvVvJhTIvpvUvvmvKtQXQv9UvpCWh81Fvva4YExrs8TrEcqvac7Q+ulQbNotlfh0yj6Ofa1l+boJEcqvaNshVBrQpKFZARp7RAYVyO2vqbVQWl4vAWFIRfU6pwet9E7rjv==&needFold=0&_ksTS=1614312455436_436&callback=jsonp437'
    url = first + str(i) + last
    # 访问的头文件，还带这个cookie
    headers = {
        # 用的哪个浏览器
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        # 从哪个页面发出的数据申请，每个网站可能略有不同；会被页面拉黑（标记我的cookie，但是重新登陆获取新的referer即可）
        'referer': 'https://list.tmall.com/search_product.htm?q=%D6%B2%B4%E5%D0%E3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton',
        #'https://list.tmall.com/search_product.htm?q=%D6%B2%B4%E5%D0%E3&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton',
        # 哪个用户想要看数据，是游客还是注册用户,建议使用登录后的cookie，需要删除其中的省略号，直接复制不行
        'cookie': 'cna=MQY3F16TIiUCAXj0KLkDrCSr; isg=BAMDf6e9Z11oDhSkH8Y_-OInkceteJe68MstDTXgvWKY9CAWvElzCjQibgS6z--y; tfstk=c7UCBAb24pvCQyTywW1w8hf5io3CZHLI_HMLOkoQGawNk-V1i0YqhJasqdmKSf1..; l=eBPYPbzmOInY98vFKO5Cnurza779fIRV1kPzaNbMiInca1WdNeRHzNCIr97HldtfgtfU-eKzpOD6ydnM-q4LRE_ceTwhKXIpBqp9-; lid=t_1498050231982_0133; enc=pI1QRFc21Y3%2BeedHEHCwaPQQxxXEGuvHw%2BQPROnTlxuv7WPkm%2FsDxEl8DD1HVRvPSq%2BUF6522Tj3eWc3Oe%2BxqQ%3D%3D; sgcookie=E100yGUBtKmZPVt1SUzKwzJN5TgRxYduHpqQ6LEOTNjgevd9Llmpw%2BiCkCNIEFIKzep26emR9fxKMYiZeNBDsRAMnhFLBsy08lT4W%2Fd1g3G%2FCK0cS; lgc=t_1498050231982_0133; _tb_token_=e76dbbf173ee4; cookie2=18ca72ed93207c71af40832a44f69dfd; xlly_s=1; dnk=t_1498050231982_0133; uc1=existShop=false&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie14=Uoe1hgR2h5poXQ%3D%3D&pas=0; csg=c34b003f; _l_g_=Ug%3D%3D; unb=3334488617; cookie1=B0OtIf8tUpGpFggiRbxP9Rqge9vJMacTRJkR2cf0lYg%3D; login=true; cookie17=UNN%2BwsEaojiS1g%3D%3D; _nk_=t_1498050231982_0133; sg=37e'
    }

    # 尝试获取数据（这里的数据应该是从json里面获取的）
    try:
        proxy = {'http': '108.49.237.244:80'}
        data = requests.get(url, headers=headers, proxies=proxy).text
        print(data)
        time.sleep(10)
        # 通过displayUserNick/auctionSku/rateDate/rateContent分别得到匿名名称、规格、评论时间、评论内容
        nickname = re.findall('"displayUserNick":"(.*?)"', data)
        nick.extend(nickname)
        auctionSku = re.findall('"auctionSku":"(.*?)"', data)
        quality.extend(auctionSku)
        rateDate = re.findall('"rateDate":"(.*?)"', data)
        date.extend(rateDate)
        rateContent = re.findall('"rateContent":"(.*?)"', data)
        comment.extend(rateContent)
    except Exception as e:
        print(str(e))
        print("本页爬取失败")

print('总共成功爬取 ' + str(len(comment)) + ' 条评论如下！')  # print(nick, quality, date, comment)
print(comment)

# 保存数据到Excel
df = pd.DataFrame()
df["用户名"] = nick
df["购买规格"] = quality
df["评论时间"] = date
df["评论内容"] = comment
df.to_excel("评论_汇总_brush.xlsx")
print('成功保存到Excel！')
# 保存数据到csv文件
df.to_csv("comments_summary_brush.csv",  encoding="utf-8")
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
        result = re.findall(r'"rateContent": "(.*?)"",\nfromMall"', data.text) 为空
        result = re.findall(r'"rateContent": "(.*?)",', data.text) 为空
        data_list.extend(result[:-2])
        for r in result:
            r = str(r)[:-2]
            result.extend(r)
'''

# for d in data_list:
#     d = d[:-2]

# while '' in data_list:
#     data_list.remove('')
# print('总共成功爬取 '+str(len(data_list))+' 条评论如下！')

# result = re.findall('rateContent":"(.*?)"fromMall"', data)
# print(result)  可以发现result自身就已经是20个元素的列表
'''
data_list = []
for r in result:
	list = r.split('",')
	data_list.extend(list)
data_list.extend(result)
'''

# 一种尝试是化为规范化json从而按照层级提取rateContent内容
# result = data.json()
# finalresult = result['rateDetail']['rateList']['rateContent']
# 原本是这样通过正则表达式匹配rateContent内容，但是每一句评论的后方始终多了一个",，可以继续尝试remove、replace等函数或直接调试re


'''
    nickname = re.findall('"displayUserNick":"(.*?)"', data)
    for i in nick:
        if nickname != i:
            nick.extend(nickname)
        else:
            break
    # print(nickname)
'''

# # 多进程抓取
# p = mp.Pool()
# p.map_async(func, i)
# p.close()
# p.join()