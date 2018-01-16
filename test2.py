# -*- coding:utf-8 -*-
#---------------------------------------  
#   程序：糗事百科爬虫  
#   版本：0.1  
#   作者：gsm  
#   日期：2018-01-15 
#   语言：Python 2.7  
#   功能：将内容存储到txt中。  
#--------------------------------------- 
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import sys
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Spider_Model:  
    def __init__(self,startnum,endnum,filename):
        self.endnum = endnum
        self.startnum = startnum
        self.myUrl = "https://www.qiushibaike.com/hot/page/"
        self.file = open(filename,'w') 
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'   
        self.headers = { 'User-Agent' : self.user_agent }
        self.num=1 
    def Save_text(self):
        for i in range(self.startnum,self.endnum+1):
            page = "%s"%i
            self.myUrl =  self.myUrl + page
            req = urllib2.Request(self.myUrl,headers = self.headers) 
            myResponse = urllib2.urlopen(req) 
            myPage = myResponse.read()
            unicodePage = myPage.decode("utf-8")
            myItems = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',unicodePage,re.S)
            for item in myItems:
                head_test = "%s."%self.num
                item_t = item.replace("\n","")
                item_t = item_t.replace("<br/>","\n")
                item_t = head_test+item_t+"\n"
                self.file.write(item_t)
                self.num = self.num + 1
            time.sleep(1)
myModel = Spider_Model(1,10,"file3.txt")
myModel.Save_text()    
