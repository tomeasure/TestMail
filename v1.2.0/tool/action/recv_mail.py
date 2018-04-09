import poplib, email
from tool import configure as conf

class RecvMail():
    def __init__(self):
        # 准备配置信息...
        self.cd = self.createCD()
    
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


if __name__ == "__main__":
    em = Email()
    print("***********************************************")
    em.recvMail()