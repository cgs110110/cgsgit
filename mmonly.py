# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
from lxml import etree

def allurl(url,headers):
    for a in range(1,750):
        Newurl = url + str(a) +'.html'
        #print Newurl
        request = urllib2.Request(Newurl, headers=headers)
        response = urllib2.urlopen(request).read()
        pattern = etree.HTML(response)
	#print pattern
        link_list = pattern.xpath('//div[@class="Clbc_Game_l_a"]')
	#print link_list
        for link in link_list:
	    #print link
            allgirl(link,headers = headers)
def allgirl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_num = pattern.xpath('//span[@class="totalpage"]/text()')
    #print link_num
    for num in link_num:
        allimgurl(num,url,headers)

def allimgurl(num,url,headers):
    for Num in range(1,int(num)):
        Newurl = url[:-5] + '_' + str(Num) + '.html'
        #print Newurl
        getimgurl(Newurl,headers)
def getimgurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@id="big-pic"]/p/a/img/@src')
    for link in link_list:
        saveimg(link,headers)
        print link
    #print link_list

def saveimg(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    with open('/home/cgs/mmonly/' + url[-13:],'wb') as f:
        f.write(response)




if __name__ == "__main__":
    url = "http://www.mmonly.cc/mmtp/list_9_"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.mmonly.cc/mmtp/xgmn/175265_4.html"}

allurl(url,headers)
