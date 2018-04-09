from tool.action import send_mail, recv_mail

class Email():  
    def sendMail(self):
        sm = send_mail.SendMail()
        sm.sendMail()

    def recvMail(self):
        rm = recv_mail.RecvMail()
        rm.recvMail()

if __name__ == "__main__":
    em = Email()
    print("***********************************************")
    em.sendMail()
    import time
    time.sleep(10)
    print("***********************************************")
    em.recvMail()