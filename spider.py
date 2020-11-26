#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @TIME     :2020/11/26 20:36
# @Author   :CandyZ
# @File     :spider.py
import urllib.request,urllib.error
import re
from bs4 import BeautifulSoup
import xlwt
def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #爬取网页
    dataList = getData(baseUrl)
    savePath = "豆瓣电影top250.xls"
    #保存数据
    saveData(dataList,savePath)




#创建正则表达式对象 表示规则
findlink = re.compile(r'<a href="(.*?)">') #影片链接
findNum = re.compile(r'<em class="">.*?</em>')#序号
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*)</span>') #片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') #评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')#评分
findInq = re.compile(r'<span class="inq">(.*)</span>')#概况
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)#相关内容



def getData(baseUrl):
    dataList = []
    for i in range(0,10):
        url = baseUrl + str(i*25)
        html = askUrl(baseUrl)

        #逐一解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"): #查找符合要求的字符串 形成列表
            # print(item)
            data = []
            item = str(item) #转字符串

            link = re.findall(findlink,item)[0] #通过正则查找指定字符串
            data.append(link)

            impSrc = re.findall(findImgSrc,item)[0]
            data.append(impSrc)

            titles = re.findall(findTitle,item) #片名
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace(" / ","") #去掉斜杠
                data.append(otitle) #添加外文名
            else:
                data.append(titles[0])
                data.append(' ')   #外文名留空

            rating = re.findall(findRating,item)[0] #评分
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0] #评价人数
            data.append(judgeNum)

            inq = re.findall(findInq,item) #概述
            if len(inq)!=0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去掉br
            data.append(bd.strip())#去掉前后空格

            dataList.append(data) #电影信息放入datalist
    # print(dataList)

    return dataList

#获取指定内容
def askUrl(url):
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)
    return html

#保存数据
def saveData(datalist,savePath):
    pass
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
    col = ("电影链接","图片链接","中文名","外文名","评分","评价数","概况","相关信息")
    for i in range(8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savePath)

if __name__ == "__main__":
    main()
    print("爬取完毕")