from tool.action import send_mail, recv_mail

class Email():
    def __init__(self):
        pass
    def sendMail(self):
        # 实例化SendMail类
        sm = send_mail.SendMail()
        # 发送邮件
        sm.sendMail()

    def recvMail(self):
        # 实例化RecvMail类
        rm = recv_mail.RecvMail()
        # 接收邮件
        rm.recvMail()

if __name__ == "__main__":
    em = Email()
    print("***********************************************")
    em.sendMail()
    import time
    time.sleep(10)
    print("***********************************************")
    em.recvMail()
