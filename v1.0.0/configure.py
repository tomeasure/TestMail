import xml.etree.ElementTree as et

class ConfigureData():
    def __init__(self):
        self.host = ''
        self.user = ''
        self.pswd = ''
        self.port = 25
        self.send = ''
        self.recv = ''
        self.fm = ''
        self.to = ''
        
class Configure():
    def __init__(self):
        pass
    def createConfigureData(self):
        cd = ConfigureData()
        tree = et.parse("configure.xml")
        root = tree.getroot()
        self.initialCD(cd, root)
        return cd
    def initialCD(self, cd, root):
        cd.host = self.getHost(root)
        cd.user = self.getUser(root)
        cd.pswd = self.getPswd(root)
        cd.port = self.getPort(root)
        cd.send = self.getSender(root)
        cd.recv = self.getReceiver(root)
        cd.fm = self.getFrom(root)
        cd.to = self.getTo(root)
    def getHost(self, root):
        return root.find("mail").find("host").text
    def getUser(self, root):
        return root.find("mail").find("user").text
    def getPswd(self, root):
        return root.find("mail").find("pass").text
    def getPort(self, root):
        return root.find("mail").find("port").text
    def getSender(self, root):
        return root.find("sender").text
    def getReceiver(self, root):
        return root.find("receiver").text
    def getFrom(self, root):
        return root.find("message").find("from").text
    def getTo(self, root):
        return root.find("message").find("to").text

if __name__ == "__main__":
    kfg = Configure()
    cd = kfg.createConfigureData()
    print("host: ", cd.host)
    print("user: ", cd.user)
    print("sender: ", cd.send)
    print("receiver: ", cd.recv)