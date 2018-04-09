Attachment = ["1.txt", "2.txt"]

import smtplib, poplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email
import configure as conf

class Email():
    def __init__(self):
        # 准备配置信息...
        self.kfg = conf.Configure()
        self.cd = self.kfg.createConfigureData()
        # 准备发送的信息...
        self.message = self.createMessage()
    def sendMail(self):
        try:
            smtpObj = smtplib.SMTP() 
            print('connecting...')
            smtpObj.connect(self.cd.host, self.cd.port)
            print('login...')
            # 防止出现 smtplib.SMTPAuthenticationError: (530, b'Must issue a STARTTLS command first.') 异常
            smtpObj.starttls()
            smtpObj.login(self.cd.user, self.cd.pswd)
            print('sending...')
            smtpObj.sendmail(self.cd.send, self.cd.recv, self.message.as_string())
            print("send successfully")
            smtpObj.quit()
        except:
            print("sorry, an error happend")

    def recvMail(self):
        server = poplib.POP3("pop.163.com", 110)
        server.user("tomeasure@163.com")
        server.pass_("Liu15830208453")
        emailList = [bytes.decode(i) for i in server.list()[1]]
        newEmailIndex = int(emailList[-1].split()[0])
        msg = [ bytes.decode(i) for i in server.retr(newEmailIndex)[1]]
        msg = email.message_from_string('\n'.join(msg))
        for part in msg.walk():
            name = part.get_filename()
            if name != None:
                data = part.get_payload(decode=True)
                with open("__"+name[1:-1], 'wb') as f:
                    f.write(data)
        server.quit()
        
    def createMessage(self):
        msg = MIMEMultipart()
        msg['From'] = Header(self.cd.fm, 'utf-8')
        msg['To'] =  Header(self.cd.to, 'utf-8')
        Subj = "data"
        msg['Subject'] = Header(Subj, 'utf-8')
        # 准备附件...
        for a in Attachment:
            att = MIMEText(open(a, 'rb').read(), 'base64', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = "attachment;filename='" + a + "'"
            # 将附件添加到邮件中去
            msg.attach(att)
        return msg
            

if __name__ == "__main__":
    em = Email()
    # em.sendMail()
    em.recvMail()