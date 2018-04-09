import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configure as conf

kfg = conf.Configure()

mail_host = kfg.getHost()
mail_user = kfg.getUser()
mail_pass = kfg.getPass()
mail_port = kfg.getPort()
sender = kfg.getSender()
receiver = kfg.getReceiver()  

message = MIMEMultipart()
message['From'] = Header(kfg.getFrom(), 'utf-8')
message['To'] =  Header(kfg.getTo(), 'utf-8')
message['Subject'] = Header(kfg.getSubject, 'utf-8')
att = MIMEText(open('parse_xml.py', 'rb').read(), 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="parse_xml.py"'
message.attach(att)

smtpObj = smtplib.SMTP() 
print('connecting...')
smtpObj.connect(mail_host, mail_port)
print('login...')
smtpObj.starttls() # 防止出现 smtplib.SMTPAuthenticationError: (530, b'Must issue a STARTTLS command first.') 异常
smtpObj.login(mail_user,mail_pass)
print('sending...')
smtpObj.sendmail(sender, receiver, message.as_string())
print ("邮件发送成功")
