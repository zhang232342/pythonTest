#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @TIME     :2019/4/11 21:51
# @Author   :CandyZ
# @File     :autoMail.py

import smtplib
import xlrd
import random
from xlutils.copy import copy
from email.mime.text import MIMEText
from email.header import Header

my_sender = 'zhang342342@sina.com'  # 发件人邮箱
my_pass = 'zhangpeng321'  # 发件人邮箱密码
my_user = 'zhang342342@icloud.com'
subject = '请坚持健身'
textRemind = ''
# 设置文件名和路径
fname = 'd:/autoEmail/记录表.xls'
# 打开文件
filename = xlrd.open_workbook(fname)
# 获取当前文档的表(得到的是sheet的个数，一个整数）
sheets = filename.nsheets
sheet = filename.sheets()[0]  # 通过sheet索引获得sheet对象
# print sheet
# 获取行数
nrows = sheet.nrows
# 获取列数
ncols = sheet.ncols
# 获取第一行,第一列数据数据
cell_value = sheet.cell_value(0, 0)
num = int(cell_value+1)
wb = copy(filename)
ws = wb.get_sheet(0)
ws.write(0, 0, num)
wb.save('d:/autoEmail/记录表.xls')
randomValue = random.randint(0, 99)
cell_values = sheet.cell_value(randomValue, 1)
sendMail = '今天是坚持健身的第'+str(num)+'天,请继续坚持下去。'+'\n\n\n'+'语录：'+cell_values

def mail():
    ret = True
    try:
        msg = MIMEText(
            sendMail,
            'plain',
            'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')  # 新浪邮箱设置标题 使用新浪邮箱必写
        msg['From'] = Header(my_sender)  # 设置收件人

        smtp = smtplib.SMTP()  # 启用smtp
        smtp.connect('smtp.sina.com')  # 设置smtp地址
        smtp.login(my_sender, my_pass)  # 登录邮箱
        smtp.sendmail(my_sender, my_user, msg.as_string())  # 发送邮件
        smtp.quit()  # 关闭连接
    except Exception:  # try中未执行 执行下面语句
        ret = False
    return ret


ret = mail()
if ret:
    print('邮件发送成功！')

else:
    print('邮件发送失败')
