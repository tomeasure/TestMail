import xml.sax

class ConfigureHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ''
        self.host = ''
        self.user = ''
        self.pswd = ''
        self.port = ''
        self.send = ''
        self.recv = ''
        self.fm = ''
        self.to = ''
        self.sj = ''
    def startElement(self, tag, attr):
        self.currentData = tag
    def characters(self, content):
        if self.currentData == 'host':
            self.host = content
        elif self.currentData == 'user':
            self.user = content
        elif self.currentData == 'pass':
            self.pswd = content
        elif self.currentData == 'port':
            self.port = content
        elif self.currentData == 'sender':
            self.send = content
        elif self.currentData == 'receiver':
            self.recv = content
        elif self.currentData == 'from':
            self.fm = content
        elif self.currentData == 'to':
            self.to = content
        elif self.currentData == 'subject':
            self.sj = content
    def endElement(self, tag):
        self.currentData = ''