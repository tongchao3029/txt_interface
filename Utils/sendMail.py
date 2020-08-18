import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

def sendMail(content,attachmentpath,receiver):
    mailHost="smtp.qq.com" #设置邮件服务器
    mailUser="888888888888@qq.com"
    mailPasswd="fdfdasfa" #邮箱密码或者是授权码
    sender="888888888@qq.com"
    receivers=receiver#可以写多个地址群发邮件
    #写邮件信息
    message=MIMEMultipart()    #可以带附件的实例
    #message=MIMEText("邮件正文","plain","utf-8")    #只是文本信息
    message["Subject"]="接口测试报告"
    message["From"]=formataddr(["收到接口测试结果", "888888888@qq.com"])  #定制发件人的抬头
    message["To"]=",".join(receivers)
    #message["Accept-Language"]="zh-CN"
    #message["Accept-Charset"]="ISO-8859-1,utf-8,gbk"

    part1=MIMEText(content,"plain","utf-8")
    part2=MIMEBase('application', 'octet-stream')
    part2.set_payload(open(attachmentpath, 'rb').read())
    part2.add_header('Content-Disposition', 'attachment', filename=" 接口测试报告.html")
    encoders.encode_base64(part2)

    message.attach(part1) 
    message.attach(part2)

    try:
        smtpObj=smtplib.SMTP(mailHost)
        smtpObj.login(mailUser,mailPasswd)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件！",e)

if __name__=="__main__":
    sendMail()
    
    
    
