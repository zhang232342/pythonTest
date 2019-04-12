#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @TIME     :2019/4/10 15:41
# @Author   :CandyZ
# @File     :pyTest.py
import urllib.request

url = 'http://www.baidu.com'
page = urllib.request.urlopen(url)
htmlCode = page.read()
pageFile = open('D:/pageFile.txt', 'wb+')
pageFile.write(htmlCode)
pageFile.close()  # 关闭
print('已写入')
