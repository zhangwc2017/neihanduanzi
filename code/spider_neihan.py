# _*_ coding: utf-8 _*_
import urllib2
import re
class  Spider:
    #内涵段子爬虫类
    def __init__(self):
        #定义爬虫类所需要的基本属性
        self.enable=True  #是否继续加载页面
        self.page=1  #当前应该爬第几张页面
        
    def load_page(self,page):
        url="http://www.neihan8.com/article/list_5_"+str(page)+".html"
        #User-Agent头
        user_agent='Mozilla/5.0(compatible;MSIE 9.0;Windows NT 6.1;Trident/5.0)'
        headers={'User-Agent':user_agent}        
        req=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(req)
        html=response.read()
        
        gbk_html=html.decode('gbk').encode('utf-8')
        pattern=re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list=pattern.findall(gbk_html)
        return item_list

    def printOnePage(self,item_list,page):
        print "******第 %d 页 爬取完毕..*******" %page
        for item in item_list:
            item=item.replace("<p>","").replace("</p>","").replace("<br />","")
            self.writeToFile(item)
    def writeToFile(self,text):
        myFile=open("/home/zhangwc/Applications/git/Scrapy/spider_neihan/data/MyStory.txt",'a')
        myFile.write(text)
        myFile.write("--------------------------------------------------")
        myFile.close()
    #让爬虫开始工作
    def doWork(self):
        while self.enable:
            try:
                item_list=self.load_page(self.page)
            except urllib2.URLError,e:
                print e.reason
                continue
            #对得到的段子item_list处理
            self.printOnePage(item_list,self.page)
            self.page+=1
            print "按回车继续..."
            print "输入 quit 退出"
            command=raw_input()
            if (command=="quit"):
                self.enable=False
                break
#main
if __name__=='__main__':
    print '''
    =============================
            内涵段子小爬虫
    =============================
    '''
    print u'请按下回车开始'
    raw_input()
    #定义一个Spider对象
    mySpider=Spider()
    mySpider.doWork()
