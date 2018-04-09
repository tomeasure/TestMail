import xml.etree.ElementTree as et
configFile = "./config/configure.xml"

class ConfigureData():
    '''
    用于存储信息
    '''
    def __init__(self):
        self.smtp_host = ''
        self.smtp_user = ''
        self.smtp_pswd = ''
        self.smtp_port = 25
        self.smtp_send = ''
        self.smtp_recv = ''
        self.smtp_fm = ''
        self.smtp_to = ''
        self.pop_host = ''
        self.pop_port = 110
        self.pop_user = ''
        self.pop_pswd = ''

        
class Configure():
    '''
    用于创建ConfigureData实例，并根据xml文件初始化
    '''
    def __init__(self):
        pass
    def createConfigureData(self):
        cd = ConfigureData()
        tree = et.parse(configFile)
        root = tree.getroot()
        self.initialCD(cd, root)
        return cd

    def initialCD(self, cd, root):
        cd.smtp_host = self.getSmtpHost(root)
        cd.smtp_user = self.getSmtpUser(root)
        cd.smtp_pswd = self.getSmtpPswd(root)
        cd.smtp_port = self.getSmtpPort(root)
        cd.smtp_send = self.getSmtpSender(root)
        cd.smtp_recv = self.getSmtpReceiver(root)
        cd.smtp_fm = self.getSmtpFrom(root)
        cd.smtp_to = self.getSmtpTo(root)
        cd.pop_host = self.getPopHost(root)
        cd.pop_user = self.getPopUser(root)
        cd.pop_pswd = self.getPopPswd(root)
        cd.pop_port = self.getPopPort(root)

    def getSmtpHost(self, root):
        return root.find("smtp").find("mail").find("host").text
    def getSmtpUser(self, root):
        return root.find("smtp").find("mail").find("user").text
    def getSmtpPswd(self, root):
        return root.find("smtp").find("mail").find("pass").text
    def getSmtpPort(self, root):
        return root.find("smtp").find("mail").find("port").text
    def getSmtpSender(self, root):
        return root.find("smtp").find("sender").text
    def getSmtpReceiver(self, root):
        return root.find("smtp").find("receiver").text
    def getSmtpFrom(self, root):
        return root.find("smtp").find("message").find("from").text
    def getSmtpTo(self, root):
        return root.find("smtp").find("message").find("to").text
    def getPopHost(self, root):
        return root.find("pop").find("host").text
    def getPopUser(self, root):
        return root.find("pop").find("user").text
    def getPopPswd(self, root):
        return root.find("pop").find("pass").text
    def getPopPort(self, root):
        return root.find("pop").find("port").text

if __name__ == "__main__":
    kfg = Configure()
    cd = kfg.createConfigureData()
    print("smtp_host: ", cd.smtp_host)
    print("smtp_user: ", cd.smtp_user)
    print("smtp_sender: ", cd.smtp_send)
    print("smtp_receiver: ", cd.smtp_recv)
    print("pop_host: ", cd.pop_host)