import smtplib, email, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from tool import configure as conf

class SendMail():
    def __init__(self):
        # 准备配置信息...
        self.cd = self.createCD()
        # 准备csv格式的附件
        self.attachment = self.getCsvFile()
        # 准备发送的信息...
        self.smtp_message = self.createSmtpMessage()

    def sendMail(self):
        """
            发送邮件
        """
        try:
            smtpObj = smtplib.SMTP()
            print('connecting smtp server...')
            smtpObj.connect(self.cd.smtp_host, self.cd.smtp_port)
            print('login smtp server...')
            # 下一行防止出现 smtplib.SMTPAuthenticationError: (530, b'Must issue a STARTTLS command first.') 异常
            smtpObj.starttls()
            smtpObj.login(self.cd.smtp_user, self.cd.smtp_pswd)
            print('sending...')
            smtpObj.sendmail(self.cd.smtp_send, self.cd.smtp_recv, self.smtp_message.as_string())
            print("send successfully.")
            smtpObj.quit()
        except:
            print("sorry, an error happend.")

    def createCD(self):
        """
            使用Configure类中的createConfigureData获取配置信息
        """
        kfg = conf.Configure()
        return kfg.createConfigureData()

    def createSmtpMessage(self):
        """
            创建用于发送的message对象，里面包含有csv格式的附件
        """
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

    def getCsvFile(self):
        """
            在main.py所在的目录下，寻找所有csv文件，并以列表的形式返回
        """
        return [d for d in os.listdir() if d[-4:]=='.csv']

if __name__ == "__main__":
    sm = SendMail()
    print("***********************************************")
    sm.sendMail()
