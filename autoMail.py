#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @TIME     :2019/4/11 21:51
# @Author   :CandyZ
# @File     :autoMail.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header

my_sender = 'zhang342342@sina.com' #发件人邮箱
my_pass = 'zhangpeng321' #发件人邮箱密码
my_user = '648245419@qq.com'
subject = 'python测试邮件'
def mail():
    ret = True
    try:
        msg = MIMEText('来自机器人发送的测试邮件', 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')#新浪邮箱设置标题 使用新浪邮箱必写
        msg['From'] = Header(my_sender)#设置收件人

        smtp = smtplib.SMTP()#启用smtp
        smtp.connect('smtp.sina.com')#设置smtp地址
        smtp.login(my_sender, my_pass)#登录邮箱
        smtp.sendmail(my_sender, my_user, msg.as_string())#发送邮件
        smtp.quit()#关闭连接
    except Exception:#try中未执行 执行下面语句
        ret = False
    return ret
ret = mail()
if ret:
    print('邮件发送成功！')

else:
    print('邮件发送失败')


