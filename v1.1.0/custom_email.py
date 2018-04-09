import smtplib, poplib, email, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configure as conf

class Email():
    def __init__(self):
        # 准备配置信息...
        self.cd = self.createCD()
        # 准备csv格式的附件
        self.attachment = self.getCsvFile()
        # 准备发送的信息...
        self.smtp_message = self.createSmtpMessage()
        
    def sendMail(self):
        try:
            smtpObj = smtplib.SMTP() 
            print('connecting smtp server...')
            smtpObj.connect(self.cd.smtp_host, self.cd.smtp_port)
            print('login smtp server...')
            # 防止出现 smtplib.SMTPAuthenticationError: (530, b'Must issue a STARTTLS command first.') 异常
            smtpObj.starttls() 
            smtpObj.login(self.cd.smtp_user, self.cd.smtp_pswd)
            print('sending...')
            smtpObj.sendmail(self.cd.smtp_send, self.cd.smtp_recv, self.smtp_message.as_string())
            print("send successfully.")
            smtpObj.quit()
        except:
            print("sorry, an error happend.")

    def recvMail(self):
        try:
            print('connecting pop3 server...')
            server = poplib.POP3(self.cd.pop_host, self.cd.pop_port)
            print('login pop3 server...')
            server.user(self.cd.pop_user)
            server.pass_(self.cd.pop_pswd)
            print("restoring attachment...")
            self.restoringAttachment(server)
            print("restored successfully.")
            server.quit()
        except:
            print("sorry, an Error happend.")

    def createCD(self):
        kfg = conf.Configure()
        return kfg.createConfigureData()

    def createSmtpMessage(self):
        msg = MIMEMultipart()
        msg['From'] = Header(self.cd.smtp_fm, 'utf-8')
        msg['To'] =  Header(self.cd.smtp_to, 'utf-8')
        Subj = "data"
        msg['Subject'] = Header(Subj, 'utf-8')
        # 准备附件...
        if self.attachment:
            # 当需要的文件存在时，将其添加到邮件中去
            for a in self.attachment:
                att = MIMEText(open(a, 'rb').read(), 'base64', 'utf-8')
                att['Content-Type'] = 'application/octet-stream'
                att['Content-Disposition'] = "attachment;filename='" + a + "'"
                # 将附件添加到邮件中去
                msg.attach(att)
        else:
            print("!!!!!!!!!!!!!!!!!there is not attachment in this email.")
        return msg

    def restoringAttachment(self, server):
        emailList = [bytes.decode(i) for i in server.list()[1]]
        newEmailIndex = int(emailList[-1].split()[0])
        msg = [ bytes.decode(i) for i in server.retr(newEmailIndex)[1]]
        msg = email.message_from_string('\n'.join(msg))
        hasAttachment = False
        for part in msg.walk():
            name = part.get_filename()
            if name != None:
                hasAttachment = True
                data = part.get_payload(decode=True)
                with open("__"+name[1:-1], 'wb') as f:
                    f.write(data)
        if not hasAttachment:
            print("!!!!!!!!!!!!!!!!!can't find any attachment.")


    def getCsvFile(self):
        return [d for d in os.listdir() if d[-4:]=='.csv']

if __name__ == "__main__":
    em = Email()
    print("***********************************************")
    em.sendMail()
    import time
    time.sleep(10)
    print("***********************************************")
    em.recvMail()