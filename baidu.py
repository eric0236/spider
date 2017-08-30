# -*- coding: utf-8 -*-

import urllib
import re
import threading
import time

class Spider_Model:
    
    def _init_(self):
        self.page = 1
        self.pages = []
        self.enable =False
        
    def getpage(self,page):
        myurl = "http://m.qiushibaike.com/hot/page" + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent' : user_agent}
        req = urllib.request.Request(myurl,headers = headers)
        myresponse = urllib.request.urlopen(req)
        mypage = myresponse.read()
        unicodepage = mypage.encode('utf-8')
        
        myitems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodepage,re.S)
        items = []
        for item in myitems:
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        return items
    
    def loadpage(self):
        while self.enable:
            if len(self.pages)<2:
                try:
                    mypage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(mypage)
                except:
                    print ('无法链接糗事百科')
            else:
                time.sleep(1)
                
    def showpage(self,nowpage,page):
        for items in nowpage:
            print (u'第%d页' %page, items[0], items[1])
            myinput = input()
            if myinput == 'quit':
                self.enable = False
                break
            
    def start(self):
        self.enable = True
        page = self.page
        print (u'正在加载中，请稍后...')
        
        threading.Thread.start_new_thread(self.loadpage,())
        
        while self.enable:
            if self.pages:
                nowpage =self.pages[0]
                del self.pages[0]
                self.showpage(nowpage,page)
                page += 1
                
print (u"""
---------------------------------------
    程序：糗事百科
    版本：0.3
    作者：why
    日期：2016-10-30
    语言：Python3.5
    操作：输入quit推出糗事百科
    功能：按下回车依次浏览今日的热点
----------------------------------------
""")

print (u'请按下回车浏览今日的糗事百科内容：')
input(' ')
mymodel = Spider_Model()
mymodel.start()