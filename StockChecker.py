import urllib.request

__author__ = 'James'

class StockChecker():

    def setup(self):
        f = open('data.txt', 'r')
        self.url = f.readline().strip('\n')
        self.sid = f.readline().strip('\n')
        self.auth = f.readline().strip('\n')
        self.recieve = f.readline().strip('\n')
        self.send = f.readline().strip('\n')
        #print(self.url)

    #getting the website
    def getWebPage(self):
        #site = 'https://store.nintendo.com/ng3/us/po/browse/productDetailColorSizePicker.jsp;jsessionid=kOYmOqFe7N7Kxndnsoo6CzFowHn8muB2ZpacolZS3Tbr_JkXIC_C!-1010601575?categoryNav=true&navAction=jump&navCount=0&atg.multisite.remap=false&productId=prod150200&categoryId=cat160004'
        #site = 'https://store.nintendo.com/ng3/us/po/browse/productDetailColorSizePicker.jsp?categoryNav=true&navAction=jump&navCount=2&atg.multisite.remap=false&productId=prod560259&categoryId=cat160004'
        page = urllib.request.urlopen(self.url)
        source = page.read()
        strSource = str(source)
        return strSource


sc = StockChecker()
sc.setup()
strSource = sc.getWebPage()
if (strSource.find('Currently out of stock. Please check back again soon!') == -1):
    print('text me')
