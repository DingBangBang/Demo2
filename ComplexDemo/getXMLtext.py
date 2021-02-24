from datetime import time
import pandas
import requests
from bs4 import BeautifulSoup
import re

from pandas.tests.io.excel.test_xlwt import xlwt


def main():
    i = 0
    list = []
    while i < 300:
        url = 'https://weibo.cn/comment/GxwPfhEks??&uid=1900552512&&page={}'.format(i + 1)
        xml = getXMLText(url)
        getList(list, xml)
        print(url)
        i += 1
        print("已爬取" + str(len(list)))
        time.sleep(5)
        if i % 5 == 0:
            time.sleep(10)
    getExcel(list)


if __name__ == "__main__":
    main()


def getXMLText(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Cookie': 'UOR=mt.meipai.com,widget.weibo.com,www.baidu.com; SINAGLOBAL=9517599856978.625.1598544313007; '
                  'ULV=1609262601335:8:1:1:1933412176892.1453.1609262601332:1604483648941; '
                  'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFaoD7R8pB74NB4Xld.jlo95JpX5o275NHD95Q0eKMN1K-peKqfWs4Dqcjdi'
                  '--fiKysi-88i--4iKnEi-2ci--4iKnEi-2c; ALF=1640798643; '
                  'SCF=Av3NqymmXHIP7qSc12cHKvwyCd8uMj9QwQYfDQKcOnpjgquwlXiI4sqkDPOP5Uijbm6yO_ImZfCVLMoANMb6ts4.; '
                  'SUB=_2A25y7xZlDeRhGeVP7FUY9S_NzTmIHXVRnQCtrDV8PUNbmtANLUmgkW9NTSmLqDw5Jk-CxHxkk94fZwHdBgPXVULt; '
                  'login_sid_t=ec02560d1a02dfa5301466573df6e79e; cross_origin_proto=SSL; '
                  '_s_tentry=passport.weibo.com; wb_view_log=1280*7201.5; Apache=1933412176892.1453.1609262601332; '
                  'SSOLoginState=1609262644; wvr=6; wb_view_log_3177951165=1280*7201.5; '
                  'webim_unReadCount=%7B%22time%22%3A1609263789700%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22'
                  '%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
        # referer：‘https://weibo.com/u/3177951165/home?topnav=1&wvr=6’
        # 这里要自己用f12获取自己登陆的微博cookie
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""


def getInfo(ID):
    # 得到真实id
    if "/u" in ID:
        id = ID.replace("/u/", "")
    else:
        id = ID.replace("/", "")
        url = "https://weibo.cn/" + str(id)
        xml = getXMLText(url)
        soup = BeautifulSoup(xml, "xml")
        id = re.compile(r"\d{10}").search(str(soup))[0]
    # 找到用户地址性别年龄
    infourl = "https://weibo.cn/" + str(id) + "/info"  # 爬取地区和性别
    infohtml = getXMLText(infourl)
    soup = BeautifulSoup(infohtml, "xml")
    c = soup.find_all("div", attrs={"class": "c"})
    sex = "未知"
    addr = "未知"
    birthday = "未知"
    try:
        for m in range(len(c)):
            if "性别" in str(c[m]):
                cc = c[m]
                if "生日" in str(cc):
                    birthday = re.findall(r"[生日].*?[<]", str(cc))[0].replace("生日:", "").replace("<", "")
                sex = re.findall(r"[性别].*?[<]", str(cc))[0].replace("性别:", "").replace("<", "")
                addr = re.findall(r"[地区].*?[<]", str(cc))[0].replace("地区:", "").replace("<", "").split(" ")[0]
                break;
        if re.search(r"\d\d\d\d-\d\d-\d\d$", str(birthday)):
            print(birthday)
            if re.findall(r"\d\d\d\d", str(birthday))[0] != "0001":
                birthday = 2019 - eval(re.findall(r"\d\d\d\d", str(birthday))[0])
        print(sex)
        print(addr)
        print(birthday)
        return id, sex, addr, birthday
    except:
        return id, "未知", "未知", "未知"


def getList(list, xml):
    soup = BeautifulSoup(xml, "xml")
    div0 = soup.find_all("div", attrs={"class": "c"})
    div = []
    for i in range(len(div0)):
        if 'id="C' in str(div0[i]):
            div.append(div0[i])
    for i in range(len(div)):
        try:
            print(div[i])
            time = re.compile(r'<span class="ct".*?</span>').search(str(div[i]))[0].replace('<span class="ct">',
                                                                                            '').replace('</span>',
                                                                                                        '').replace(
                "来自网页", "")
            pat = re.compile(r'<a href=".*?">')
            ID = pat.search(str(div[i]))[0].replace('<a href="', "").replace('">', "")
            username = re.compile(r'<a href=".*?</a>').search(str(div[i]))[0].replace('<a href="', "").replace('">',
                                                                                                               "").replace(
                ID, "").replace("</a>", "")
            # 个人信息
            id, sex, addr, birthday = getInfo(ID)
            # 评论
            ttext = re.compile(r'<span class="ctt.*?</span>').search(str(div[i]))[0]
            # like = re.compile(r"赞.*?</a>").search(str(div[i]))[0].replace("赞[","").replace("]</a>","")
            print(ttext)
            if "回复" in ttext:
                text = re.compile(r'</a>.*</span>').search(str(ttext))[0].replace("</a>:", "").replace("</span>", "")
            else:
                text = ttext.replace('<span class="ctt">', '').replace('</span>', '')
            if "</a>" in text:
                span_a = re.compile(r'<a.*?/a>').search(str(text))
                for m in range(len(span_a)):
                    text = text.replace(span_a[m], "")
            print(text)
            biaoqing = re.findall(r"[[].*?[]]", text)

            if text:
                list.append([id, username, sex, addr, birthday, text, time, biaoqing])
        except:
            continue


def getExcel(list):
    excel = xlwt.Workbook(encoding="utf-8")
    sheet = excel.add_sheet("sheet1")
    sheet.write(0, 0, "id")
    sheet.write(0, 1, "用户名")
    sheet.write(0, 2, "性别")
    sheet.write(0, 3, "地区")
    sheet.write(0, 4, "生日")
    sheet.write(0, 5, "评论")
    sheet.write(0, 6, "时间")
    sheet.write(0, 7, "表情")
    for i in range(len(list)):
        t = list[i]
        sheet.write(i + 1, 0, t[0])
        sheet.write(i + 1, 1, t[1])
        sheet.write(i + 1, 2, t[2])
        sheet.write(i + 1, 3, t[3])
        sheet.write(i + 1, 4, t[4])
        sheet.write(i + 1, 5, t[5])
        sheet.write(i + 1, 6, t[6])
        m = t[7]
        num = 7
        enjoy = []
        for j in range(len(m)):
            if m[j] not in enjoy:
                enjoy.append(m[j])
                sheet.write(i + 1, num, m[j])
                num += 1
            else:
                continue
    excel.save('xxx.xls')
