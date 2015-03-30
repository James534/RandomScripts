import urllib.request
import time
from twilio.rest import TwilioRestClient

__author__ = 'James'

class StockChecker():

    def setup(self):
        f = open('data.txt', 'r')
        self.url            = f.readline().strip('\n')
        self.webController  = f.readline().strip('\n')
        self.sid = f.readline().strip('\n')
        self.auth = f.readline().strip('\n')
        self.clientNumber = f.readline().strip('\n')
        self.serverNumber = f.readline().strip('\n')
        self.client = TwilioRestClient(self.sid, self.auth)
        #print(self.url)

    #getting the website
    def getWebPage(self, url):
        page = urllib.request.urlopen(url)
        source = page.read()
        strSource = str(source)
        return strSource.lower()

    def text(self, msg):
        message = self.client.messages.create(
            body="|" + msg,
            to=self.clientNumber,
            from_=self.serverNumber)
        #print (message.sid)
        print ('texting', msg)
        #print (msg)

while True:
    sc = StockChecker()
    sc.setup()
    strSource = sc.getWebPage(sc.url)
    if strSource.find('out of stock') == -1:
        #gets the title of the product (nintendo website)
        #have to custimize these for every website type
        begin = strSource.find('results-header')
        begin += len("results-header") + 2
        end = strSource.find("</h2>", begin)
        #print(strSource[begin:end])
        productName = strSource[begin:end]

        sc.text(productName + " || is in stock")

    #i can change webpage remotely to stop the program
    if sc.getWebPage(sc.webController).find("offline") != -1:
        sc.text("Ending program")
        print("ENDING")
        break

    print('cycle')

    #runs program every hour
    time.sleep(3600)

print ('eof')