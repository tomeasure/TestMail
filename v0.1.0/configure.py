import parse_xml as px
import xml.sax

class Configure():
    def __init__(self):
        self.handler = self.getHandler()
    def getHandler(self):
        handler = px.ConfigureHandler()
        xml.sax.parse('configure.xml', handler)
        return handler
    def getHost(self):
        return self.handler.host
    def getUser(self):
        return self.handler.user
    def getPass(self):
        return self.handler.pswd
    def getPort(self):
        return int(self.handler.port)
    def getSender(self):
        return self.handler.send
    def getReceiver(self):
        return self.handler.recv
    def getFrom(self):
        return self.handler.fm
    def getTo(self):
        return self.handler.to
    def getSubject(self):
        return self.handler.sj