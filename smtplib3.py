#!/usr/bin/env python
#coding: utf-8
from email.mime.multipart import MIMEMultipart
#导入MIMEMultipart类
from email.mime.text import MIMEText
#导入MIMEText类
from email.mime.image import MIMEImage
#导入MIMEImage类

HOST = "smtp.gmail.com"
#定义smtp主机
SUBJECT = u"业务性能数据报表"
#定义邮件主题
TO = "testmail@qq.com"
#定义邮件收件人
FROM = "mymail@gmail.com"
#定义邮件发件人

def addimg(src,imgid):
#添加图片函数，参数1：图片路径，参数2：图片id
    fp = open(src,'rb')
#打开文件
    msgImage = MIMEImage(fp,read())
#创建MIMEImage对象，读取图片内容并作为参数
    fp.close()
#关闭文件
    msgImage.add_header('Content-ID',imgid)
#指定图片文件的Content-ID,<img> 标签src用到

    return msgImage
#返回msgImage对象

msgText = MIMEText(""" #创建一个MIMEText对象，HTML元素包括表格<table>及图片<img>
<table width="600" border="0" cellspacing="0" cellpadding="4">
    <tr bgcolor="#CECFAD" height="20" style="front-size: 14px">
      <td colspan=2>*官网性能数据 <a href="monitor.domain.com">更多>></a>></td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100" style="front-size: 13px"> 
      <td>
	<img src="cid:io"></td><td>
	<img scr="cid:key_hit"></td>	
    </tr>
    <tr bgcolor="EFEBDE" height="100" style="front-size:13px">
      <td>
	<img scr="cid:mem"></td><td>
	<img src="cid:swap"></td>
    </tr>
</table>""","html","utf-8")
#<img>标签的src属性是通过Content-ID来引用的

msg.attach(msgtext)
#MIMEMultipart附加MIMEText内容
msg.attach(addimg("img/bytes_io.png","io"))
#使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_mem.png","mem"))
msg.attach(addimg("img/os_swap.png","swap"))
msg['Subject'] = SUBJECT
#邮件主题
msg['From'] = FROM
#邮件发件人，邮件头可见
msg['To'] = TO
#邮件收件人，邮件头部可见
try:
    server = smtplib.SMTP()
#创建一个SMTP()对象
    server.connect(HOST,"25")
#通过connect方法连接smtp主机
    server.starttls()
#启动安全传输模式
    server.login("mymail@gmail.com","mypassword")
#邮件帐号登录校验
    server.sendmail(FROM,TO,msg.as_string())
#邮件发送
    server.quit()
#断开smtp连接
    print "邮件发送成功"
except Exception,e:
    print "失败： "+str(e)

