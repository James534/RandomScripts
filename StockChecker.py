import urllib.request
from twilio.rest import TwilioRestClient

__author__ = 'James'

class StockChecker():

    def setup(self):
        f = open('data.txt', 'r')
        self.url = f.readline().strip('\n')
        self.sid = f.readline().strip('\n')
        self.auth = f.readline().strip('\n')
        self.clientNumber = f.readline().strip('\n')
        self.serverNumber = f.readline().strip('\n')
        self.client = TwilioRestClient(self.sid, self.auth)
        #print(self.url)

    #getting the website
    def getWebPage(self):
        #site = 'https://store.nintendo.com/ng3/us/po/browse/productDetailColorSizePicker.jsp;jsessionid=kOYmOqFe7N7Kxndnsoo6CzFowHn8muB2ZpacolZS3Tbr_JkXIC_C!-1010601575?categoryNav=true&navAction=jump&navCount=0&atg.multisite.remap=false&productId=prod150200&categoryId=cat160004'
        #site = 'https://store.nintendo.com/ng3/us/po/browse/productDetailColorSizePicker.jsp?categoryNav=true&navAction=jump&navCount=2&atg.multisite.remap=false&productId=prod560259&categoryId=cat160004'
        page = urllib.request.urlopen(self.url)
        source = page.read()
        strSource = str(source)
        return strSource

    def text(self, msg):
        message = self.client.messages.create(msg,self.clientNumber,self.serverNumber)
        print (message.sid)
        print ('texting')

sc = StockChecker()
sc.setup()
strSource = sc.getWebPage()
if (strSource.find('Currently out of stock. Please check back again soon!') == -1):
    sc.text("out of stock")

print ('eof')