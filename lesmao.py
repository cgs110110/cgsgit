# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
from lxml import etree
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取所有需要爬取的美女html页面
def allurl(url,headers):
    for a in range(1,137):
        Newurl = url + str(a)
        print Newurl
        request = urllib2.Request(Newurl, headers=headers)
        response = urllib2.urlopen(request).read()
        pattern = etree.HTML(response)
        link_list = pattern.xpath('//div[@class="photo"]/a/@href')
        for link in link_list:
            #print link[:-8]
            link2 = link[:-8]
            for a in range(1,5):
                alllink = link2 + str(a) + "-1.html"
                print alllink
                allgirl(alllink,headers = headers)
#获取所有美女的图片html页面
def allgirl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_num = pattern.xpath('//div[@id="thread-pic"]/ul/li/img/@src')
    img_name = pattern.xpath('//div[@id="thread-pic"]/ul/li/img/@alt')
    #print link_num
    for num,img_name in zip(link_num,img_name):
        #saveimg(num,img_name.encode("utf-8"),headers)
       	name = img_name[-10:-4] + num[-21:-18] 
        saveimg(num,name,headers)
	#print name
	#print num[-21:-14]
        #print num
    #print link_list

def saveimg(url,img_name,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    with open('/home/cgs/lesmao/' + img_name + '.jpg','wb') as f:
        f.write(response)




if __name__ == "__main__":
    url = "http://www.lesmao.com/portal.php?page="
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.lesmao.com/"}

allurl(url,headers)
