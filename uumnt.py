# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
from lxml import etree

def allurl(url,headers):
    for a in range(1,449):
        Newurl = url + str(a) +'.html'
        print Newurl
        request = urllib2.Request(Newurl, headers=headers)
        response = urllib2.urlopen(request).read()
        pattern = etree.HTML(response)
	#print pattern
        link_list = pattern.xpath('//p[@class="list_h"]/a/@href')
	#print link_list
        for link in link_list:
	    Newurl = "http://www.uumnt.com" + link
	    #print Newurl
            allgirl(Newurl,headers = headers)
def allgirl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_num = pattern.xpath('//div[@class="page"]/a[7]/@href')
    #print link_num
    #print url
    Newurl = url[:-5] + '_'
    #print Newurl
    for num in link_num:
	#pass
	Newnum =  num[-7:-5]
        allimgurl(Newnum,Newurl,headers)

def allimgurl(num,url,headers):
    for Num in range(1,int(num)):
        Newurl = url + str(Num) + '.html'
        #print Newurl
        getimgurl(Newurl,headers)
def getimgurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@class="bg-white p15 center imgac clearfix"]/a/img/@src')
    name_list = pattern.xpath('//div[@class="bg-white p15 center imgac clearfix"]/a/img/@alt')
    for link,name in zip(link_list, name_list):
        saveimg(link,name,headers)
        print link + 'is saving '
	#print name
    #print link_list

def saveimg(url,name,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    #print url
    #print name
    with open('/home/cgs/python/uumnt/' + name + '.jpg','wb') as f:
        f.write(response)
    print  name + "is save ok"



if __name__ == "__main__":
    url = "http://www.uumnt.com/meinv/list_"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"https://newimg.uumnt.com/"}

allurl(url,headers)
